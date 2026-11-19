"""Signed reciprocal seed mixtures with full Gram and padded positivity checks.

Floating-point convex optimization diagnostics, not interval certificates.
"""

import argparse
from fractions import Fraction
import json
from math import sqrt
from pathlib import Path
import sys

import numpy as np
from scipy.optimize import linprog, minimize

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from quadratic_theta import damped_trials
from square_control import square_field_sign
from theta import paley_sign


def project(sign, vector, side):
    return np.fft.ifft(np.fft.fft(vector) * (sign == side)).real


def solve_mixture(gram, columns, padding, mean, variation):
    """Use a constraint generation QP; verify positivity at every coordinate."""
    n, k = columns.shape
    roots = np.sqrt(np.maximum(np.diag(gram), 0))
    first = int(np.argmin(roots))
    alpha = np.eye(k)[first]
    start = np.r_[alpha, abs(alpha)]
    cuts = set()
    all_margins = mean*padding + columns @ alpha
    if np.min(all_margins[1:]) < -1e-8:
        raise RuntimeError('the single-width starting source is not positive')
    initial_indices = np.argpartition(all_margins[1:], min(16, n-2))[:min(16, n-1)] + 1
    cuts.update(map(int, initial_indices))

    def objective(z):
        a = z[:k]
        return float(a @ gram @ a), np.r_[2*gram @ a, np.zeros(k)]

    equality = {'type': 'eq', 'fun': lambda z: z[:k].sum()-1,
                'jac': lambda z: np.r_[np.ones(k), np.zeros(k)]}
    tv_matrix = np.block([[np.eye(k), np.eye(k)], [-np.eye(k), np.eye(k)],
                          [np.zeros((1, k)), -np.ones((1, k))]])
    tv_offset = np.r_[np.zeros(2*k), variation]
    for iteration in range(100):
        selected = np.array(sorted(cuts))
        positive_matrix = np.column_stack((columns[selected], np.zeros((len(selected), k))))
        matrix = np.vstack((tv_matrix, positive_matrix))
        offset = np.r_[tv_offset, mean*padding[selected]]
        constraints = [equality, {'type': 'ineq', 'fun': lambda z: matrix @ z+offset,
                                  'jac': lambda z: matrix}]
        result = minimize(objective, start, jac=True, method='SLSQP',
                          constraints=constraints,
                          options={'ftol': 2e-13, 'maxiter': 1500})
        if not result.success:
            raise RuntimeError(f'mixture QP: {result.message}')
        start = result.x
        alpha = start[:k]
        margins = mean*padding + columns @ alpha
        if margins[1:].min() >= -2e-8:
            assert abs(alpha.sum()-1) < 1e-8
            assert abs(alpha).sum() <= variation+1e-7
            return alpha, iteration+1, sorted(cuts), margins
        worst = np.argpartition(margins[1:], min(32, n-2))[:min(32, n-1)] + 1
        previous = len(cuts)
        cuts.update(int(i) for i in worst if margins[i] < -1e-9)
        if len(cuts) == previous:
            raise RuntimeError('constraint generation stalled')
    raise RuntimeError('too many constraint-generation rounds')


def certify_mixture(sign, B, alpha, padding, mean, variation, cuts, side, input_path):
    """Enclose a tangent dual for the exact rationalized row family."""
    from flint import acb, arb, ctx
    ctx.prec = 128
    n, k = B.shape
    scale = 10**10
    numerators = np.rint(B*scale).astype(np.int64)
    numerators[0] = scale
    assert np.min(numerators) >= 0
    # Move slightly toward a positive single-width source before rounding.
    # This makes the upper trial feasible at the exact requested mean.
    interior = np.eye(k)[int(np.argmin(B.sum(axis=0)))]
    trial_alpha = (1-1e-6)*alpha+1e-6*interior
    alpha_num = [round(float(x)*scale) for x in trial_alpha[:-1]]
    alpha_num.append(scale-sum(alpha_num))
    assert sum(abs(x) for x in alpha_num) <= round(variation*scale)
    v = np.array(alpha_num)/scale
    rounded_B = numerators/scale
    F = np.column_stack([project(sign, rounded_B[:, j], side) for j in range(k)])
    kappa = np.count_nonzero(sign == -side)/n
    G = F.T @ F+np.outer(F[0], F[0])/kappa
    C = sqrt(n)*rounded_B-np.outer(padding, rounded_B.sum(axis=0)/sqrt(n))
    selected = np.asarray(cuts)
    derivative = 2*G @ v
    # Maximize eta - mu*lambda.M - TV*||2Gv-eta-C^T lambda||_infinity.
    A = np.vstack((np.column_stack((-C[selected].T, -np.ones(k), -np.ones(k))),
                   np.column_stack((C[selected].T, np.ones(k), -np.ones(k)))))
    result = linprog(np.r_[mean*padding[selected], -1., variation], A_ub=A,
                     b_ub=np.r_[-derivative, derivative],
                     bounds=[(0, None)]*len(cuts)+[(None, None), (0, None)],
                     method='highs')
    assert result.success, result.message
    lambda_num = [max(0, round(float(x)*scale)) for x in result.x[:-2]]
    eta_num = round(float(result.x[-2])*scale)
    payload = dict(n=n, side=side, scale=scale, row_numerators=numerators.T.tolist(),
                   coefficient_numerators=alpha_num, constraint_indices=cuts,
                   lambda_numerators=lambda_num, eta_numerator=eta_num,
                   mean=str(Fraction(str(mean))), variation=str(Fraction(str(variation))))
    Path(input_path).write_text(json.dumps(payload)+'\n')
    return replay_certificate(sign, payload)


def replay_certificate(sign, payload):
    """All proof bounds use the saved integers and Arb, independent of optimizers."""
    from flint import acb, arb, ctx
    ctx.prec = 128
    n, side, scale = payload['n'], payload['side'], payload['scale']
    integers = payload['row_numerators']
    k = len(integers)
    assert isinstance(n, int) and n > 2 and len(sign) == n
    assert side in (-1, 1) and isinstance(scale, int) and scale > 0 and k > 0
    assert sign[0] == 0 and all(x in (-1, 1) for x in sign[1:])
    assert np.array_equal(sign[1:], sign[:0:-1])
    assert all(len(row) == n and row[0] == scale and
               all(isinstance(x, int) and x >= 0 for x in row) and
               row[1:] == row[:0:-1] for row in integers)
    assert len(payload['coefficient_numerators']) == k
    assert all(isinstance(x, int) for x in payload['coefficient_numerators'])
    assert len(payload['constraint_indices']) == len(payload['lambda_numerators'])
    assert all(isinstance(i, int) and 0 < i < n for i in payload['constraint_indices'])
    assert all(isinstance(x, int) and x >= 0 for x in payload['lambda_numerators'])
    assert isinstance(payload['eta_numerator'], int)
    root = arb(n).sqrt()
    kappa = arb(int(np.count_nonzero(sign == -side)))/n
    ell = [x.real for x in acb.dft([int(x == -side) for x in sign], inverse=True)]
    M = [1-x/kappa for x in ell]
    assert all(x > 0 for x in M[1:])
    transforms = [acb.dft(row) for row in integers]
    indices = np.flatnonzero(sign == side)
    d = [sum((row[int(i)].real for i in indices), arb(0))/(n*scale)
         for row in transforms]
    G = [[sum(((transforms[j][int(i)]*transforms[h][int(i)].conjugate()).real
               for i in indices), arb(0))/(n*scale**2)+d[j]*d[h]/kappa
          for h in range(k)] for j in range(k)]
    v = [arb(x)/scale for x in payload['coefficient_numerators']]
    lambdas = [arb(x)/scale for x in payload['lambda_numerators']]
    eta = arb(payload['eta_numerator'])/scale
    requested = Fraction(payload['mean'])
    mu = arb(requested.numerator)/requested.denominator
    requested_T = Fraction(payload['variation'])
    TV = arb(requested_T.numerator)/requested_T.denominator
    mass = [arb(sum(row))/(scale*root) for row in integers]
    def column(i, j):
        return root*arb(integers[j][i])/scale-M[i]*mass[j]
    Gv = [sum((G[i][j]*v[j] for j in range(k)), arb(0)) for i in range(k)]
    quadratic = sum((v[i]*Gv[i] for i in range(k)), arb(0))
    residual = [2*Gv[j]-eta-sum((lam*column(i, j) for lam, i in
                zip(lambdas, payload['constraint_indices'])), arb(0)) for j in range(k)]
    error = max(abs(x).upper() for x in residual)
    lower = (eta-mu*sum((lam*M[i] for lam, i in
             zip(lambdas, payload['constraint_indices'])), arb(0))
             -TV*error-quadratic).lower()
    needed_mu = max((-sum((column(i, j)*v[j] for j in range(k)), arb(0))/M[i]).upper()
                    for i in range(1, n))
    if needed_mu < mu:
        feasible_mean = requested
    else:
        mean_num = int((needed_mu*scale).upper().ceil().unique_fmpz())+1
        feasible_mean = Fraction(mean_num, scale)
    adjusted_mu = arb(feasible_mean.numerator)/feasible_mean.denominator
    assert all(adjusted_mu*M[i]+sum((column(i, j)*v[j] for j in range(k)), arb(0)) > 0
               for i in range(1, n))
    assert sum(payload['coefficient_numerators']) == scale
    assert sum(abs(x) for x in payload['coefficient_numerators']) <= requested_T*scale
    output = dict(certificate_family='exact rationalized nonnegative reciprocal trials',
                  requested_mean=payload['mean'], variation=payload['variation'],
                  feasible_mean=str(feasible_mean),
                  squared_projection_cost_over_n_lower=str(max(arb(0), lower)),
                  squared_projection_cost_over_n_trial_upper=str(quadratic.upper()),
                  projection_cost_over_n14_lower=str((root*max(arb(0), lower)).sqrt().lower()),
                  projection_cost_over_n14_trial_upper=str((root*quadratic).sqrt().upper()),
                  tangent_residual_infinity_upper=str(error))
    return output


def run_case(order, characteristic, square, widths, mean, variations, sizes, tolerance,
             certify=False):
    sign = square_field_sign(characteristic) if square else paley_sign(order)
    n = len(sign)
    samples = list(damped_trials(sign, widths, tolerance=tolerance, rounds=96))
    for forbidden_side in (1, -1):
        target_side = -forbidden_side
        ell = project(sign, np.eye(1, n, 0)[0], target_side)
        kappa = ell[0]
        padding = np.ones(n)-ell/kappa
        bs, fs = [], []
        for r, marker, plus, minus, residual in samples:
            if residual > 2e-8:
                raise RuntimeError(f'reciprocal reference residual {residual}')
            row = plus if target_side == 1 else minus
            b = row/row[0]
            bs.append(b)
            fs.append(project(sign, b, forbidden_side))
        for size in sizes:
            indices = np.unique(np.rint(np.linspace(0, len(widths)-1, size)).astype(int))
            B = np.column_stack([bs[i] for i in indices])
            F = np.column_stack([fs[i] for i in indices])
            mass = B.sum(axis=0)/sqrt(n)
            marked = F[0]
            gram = F.T @ F+np.outer(marked, marked)/kappa
            columns = sqrt(n)*B-np.outer(padding, mass)
            for variation in variations:
                alpha, rounds, cuts, source = solve_mixture(
                    gram, columns, padding, mean, variation)
                f = sqrt(n)*(F @ alpha)
                row = source-f+f[0]*ell/kappa
                delta = row-source
                assert abs(row[0]-sqrt(n)) < 1e-7
                assert abs(row.mean()-mean) < 1e-8
                assert np.linalg.norm(project(sign, row, forbidden_side)) < 1e-6
                cost2 = float(alpha @ gram @ alpha)
                assert abs(np.dot(delta, delta)/n-cost2) < 1e-8
                required_mean = float(np.max(-((columns @ alpha)[1:])/padding[1:]))
                record = dict(order=order, characteristic=characteristic, square=square,
                           forbidden_side=forbidden_side, mean=mean,
                           widths=[widths[i] for i in indices], variation_cap=variation,
                           coefficients=alpha.tolist(), total_variation=float(abs(alpha).sum()),
                           projection_cost_over_sqrt_n=sqrt(max(cost2, 0)),
                           projection_cost_over_n14=n**.25*sqrt(max(cost2, 0)),
                           projected_negative_over_n14=float(np.linalg.norm(np.minimum(row, 0)))/n**.25,
                           forbidden_root=float(marked @ alpha),
                           forbidden_norm=float(np.linalg.norm(F @ alpha)),
                           source_minimum=float(source[1:].min()),
                           required_source_mean=required_mean,
                           active_constraint_rounds=rounds, constraints=len(cuts),
                           max_reference_residual=max(x[-1] for x in samples))
                if certify:
                    path = Path(__file__).with_name(f'reciprocal-seed-26-q{order}-side{forbidden_side}'
                                                    f'-k{len(indices)}-tv{variation:g}-input.json')
                    record['certificate_input'] = path.name
                    record['certificate'] = certify_mixture(sign, B, alpha, padding, mean,
                                                             variation, cuts, forbidden_side, path)
                yield record


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('primes', nargs='*', type=int)
    parser.add_argument('--square-roots', nargs='*', type=int, default=[])
    parser.add_argument('--widths', nargs='+', type=float, default=[.7, .5, .32, .2, .12, .08])
    parser.add_argument('--width-scale', choices=['fixed', 'n14'], default='fixed')
    parser.add_argument('--mean', type=float, default=1.01)
    parser.add_argument('--variation', nargs='+', type=float, default=[1., 3., 10., 30.])
    parser.add_argument('--sizes', nargs='+', type=int, default=[2, 4, 6])
    parser.add_argument('--tolerance', type=float, default=2e-10)
    parser.add_argument('--certify', action='store_true')
    parser.add_argument('--replay-input', type=Path)
    args = parser.parse_args()
    if args.replay_input:
        payload = json.loads(args.replay_input.read_text())
        q = 2*payload['n']+1
        characteristic = int(round(sqrt(q)))
        sign = square_field_sign(characteristic) if characteristic**2 == q else paley_sign(q)
        print(json.dumps(replay_certificate(sign, payload)), flush=True)
        return
    if not args.primes and not args.square_roots:
        parser.error('provide a field')
    if min(args.widths) <= 0 or min(args.variation) < 1 or min(args.sizes) < 1:
        parser.error('positive widths, variation at least one and positive sizes required')
    cases = [(p, p, False) for p in args.primes]
    cases += [(p*p, p, True) for p in args.square_roots]
    for q, p, square in sorted(cases):
        n = (q-1)//2
        scale = 1 if args.width_scale == 'fixed' else n**-.25
        widths = sorted({r*scale for r in args.widths}, reverse=True)
        if max(widths) >= 1:
            parser.error('scaled widths must be less than one')
        for row in run_case(q, p, square, widths, args.mean, args.variation,
                            args.sizes, args.tolerance, args.certify):
            print(json.dumps(row), flush=True)


if __name__ == '__main__':
    main()
