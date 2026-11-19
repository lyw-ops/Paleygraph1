"""Compare scalar Jacobi seed corrections to their compact-group limit."""

import argparse
from fractions import Fraction
import json
from math import sqrt
from pathlib import Path
import runpy

import numpy as np
from numpy.polynomial.chebyshev import chebvander
from scipy.optimize import minimize


RESEARCH = Path(__file__).resolve().parent
PINNED = runpy.run_path(str(RESEARCH / 'pinned-penalty-24.py'))
R17 = PINNED['R17']


def symplectic_traces(generator, samples, half_dimension):
    """Sample Haar USp(2k) by quaternionic Gram–Schmidt."""
    basis = []
    traces = np.zeros(samples)
    k = half_dimension
    for j in range(k):
        vector = generator.normal(size=(samples, 2*k)) + 1j*generator.normal(size=(samples, 2*k))
        for previous in basis:
            vector -= np.sum(previous.conj()*vector, axis=1)[:, None]*previous
        vector /= np.linalg.norm(vector, axis=1)[:, None]
        partner = np.concatenate((-vector[:, k:].conj(), vector[:, :k].conj()), axis=1)
        basis.extend((vector, partner))
        traces += 2*vector[:, j].real
    return traces


def optimize(base, features):
    def value_gradient(coefficients):
        row = base + features @ coefficients
        negative = np.minimum(row, 0.)
        return float(negative @ negative)/len(base), 2*(features.T @ negative)/len(base)

    result = minimize(value_gradient, np.zeros(features.shape[1]), jac=True, method='BFGS',
                      options={'gtol': 1e-10, 'maxiter': 500})
    value, gradient = value_gradient(result.x)
    if np.linalg.norm(gradient) > 2e-7:
        raise RuntimeError(f'the scalar coefficient solve did not converge: {result.message}')
    correction = features @ result.x
    return dict(trial_negative_rms=sqrt(value),
                trial_correction_rms=float(np.linalg.norm(correction))/sqrt(len(base)),
                coefficient_norm=float(np.linalg.norm(result.x)),
                gradient_norm=float(np.linalg.norm(gradient)),
                coefficients=[float(value) for value in result.x]), correction


def scalar_radius_bound(threshold):
    """Certify the radius test at a supplied rational threshold."""
    from flint import arb, ctx

    ctx.prec = 128
    t = arb(threshold.numerator)/threshold.denominator
    angle = t.acos()
    sine = (1-t*t).sqrt()
    first = (sine-t*angle)/arb.pi()
    mixed = (angle-t*sine)/(2*arb.pi())
    second = ((t*t+arb(1)/2)*angle-arb(3)/2*t*sine)/arb.pi()
    projected = ((second-first**2)/2-mixed**2).sqrt()
    lower = ((arb(2).sqrt()*mixed-first)/projected).lower()
    return dict(threshold=str(threshold), certified_radius_over_sqrt_n_lower=str(lower))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('primes', nargs='*', type=int)
    parser.add_argument('--square-roots', nargs='*', type=int, default=[])
    parser.add_argument('--degrees', nargs='+', type=int, default=[2, 4, 8])
    parser.add_argument('--mean', type=float, default=1.)
    parser.add_argument('--samples', type=int, default=0)
    parser.add_argument('--seed', type=int, default=2501)
    parser.add_argument('--radius-bound', action='store_true')
    parser.add_argument('--repair-steps', type=int, default=0,
                        help='also compare unrestricted projected squared-defect descent')
    args = parser.parse_args()
    if min(args.degrees) < 2 or args.mean <= 0 or min(args.samples, args.repair_steps) < 0:
        parser.error('use degree at least two, positive mean, and nonnegative sample count')
    degrees = sorted(set(args.degrees))
    if args.radius_bound:
        for threshold in (Fraction(1, 3), Fraction(161, 500)):
            print(json.dumps(scalar_radius_bound(threshold)), flush=True)
    if args.samples:
        generator = np.random.default_rng(args.seed)
        x = np.cos(2*np.pi*generator.random(args.samples))
        polynomials = chebvander(x, max(degrees))
        symbols = []
        for degree in range(2, max(degrees)+1):
            half = degree//2
            symbols.append((symplectic_traces(generator, args.samples, half)
                            + symplectic_traces(generator, args.samples, half))/2)
        all_features = (polynomials[:, 2:] - np.column_stack(symbols))/2
        base = args.mean-sqrt(2)*x
        for degree in degrees:
            result, _ = optimize(base, all_features[:, :degree-1])
            print(json.dumps(dict(model='compact_groups', samples=args.samples, seed=args.seed,
                                  mean=args.mean, degree=degree) | result), flush=True)
    cases = [(p, None, R17['paley_sign']) for p in args.primes]
    cases += [(h*h, h, R17['square_field_sign']) for h in args.square_roots]
    for order, square_root, maker in sorted(cases):
        sign = maker(order if square_root is None else square_root)
        n = len(sign)
        x = np.fft.fft(sign).real/sqrt(order)
        polynomials = chebvander(x, max(degrees))
        for side in (1, -1):
            _, project, padding, kappa, column, _ = PINNED['ANCHOR']['anchored_tools'](sign, side)
            base = args.mean+(sqrt(n)-args.mean)*column/kappa
            features = np.column_stack([project(polynomials[:, d]) for d in range(2, max(degrees)+1)])
            for degree in degrees:
                result, _ = optimize(base[1:], features[1:, :degree-1])
                print(json.dumps(dict(model='finite_field', order=order, square_root=square_root,
                                      side=side, mean=args.mean, degree=degree) | result), flush=True)
            if args.repair_steps:
                result, correction, _, _, _ = PINNED['descend'](
                    sign, side, 1., args.mean, args.repair_steps)
                print(json.dumps(dict(model='projected_descent', order=order, square_root=square_root,
                                      side=side, mean=args.mean, steps=args.repair_steps,
                                      trial_negative_rms=result['trial_defect_over_n14']/n**.25,
                                      trial_correction_rms=float(np.linalg.norm(correction))/sqrt(n))),
                      flush=True)


if __name__ == '__main__':
    main()
