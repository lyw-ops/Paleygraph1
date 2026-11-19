"""Minimize a smoothed upper-tail cost on the fixed-mark Fourier slice."""

import argparse
from fractions import Fraction
import json
from math import isfinite, sqrt
from pathlib import Path
import runpy

import numpy as np


RESEARCH = Path(__file__).resolve().parent
ANCHOR = runpy.run_path(str(RESEARCH / 'anchored-repair-20.py'))
R17 = ANCHOR['R17']


def geometry(sign, side):
    _, pinned, padding, kappa, column, finish = ANCHOR['anchored_tools'](sign, side)
    n = len(sign)
    omega = (1 + sqrt(2*n + 1))/(2*n)
    eta = (1 - omega/kappa)/(omega + omega**2/kappa)
    caps = 1/(1 + eta*(kappa + column[1:]))
    return pinned, padding, kappa, column, caps, finish


def hinge_envelope(scores, caps, penalty, previous=0.):
    """Return a budget threshold, its certified-form objective, and weights."""
    tau = 0.
    positive = np.maximum(scores, 0.)
    weights = caps * np.minimum(positive/penalty, 1.)
    if weights.sum() > 1.:
        lower, upper = 0., float(positive.max())
        tau = min(max(previous, lower), upper)
        for _ in range(60):
            excess = scores - tau
            interior = (excess > 0) & (excess < penalty)
            weights = caps * np.clip(excess/penalty, 0., 1.)
            mass = float(weights.sum())
            if abs(mass-1.) <= 2e-13:
                break
            if mass > 1:
                lower = tau
            else:
                upper = tau
            slope = float(caps[interior].sum())
            proposal = tau + penalty*(mass-1)/slope if slope else (lower+upper)/2
            tau = proposal if lower < proposal < upper else (lower+upper)/2
        else:
            tau = upper
            weights = caps*np.clip((scores-tau)/penalty, 0., 1.)
    excess = np.maximum(scores - tau, 0.)
    core = np.minimum(excess, penalty)
    upper_value = tau + caps @ (core**2/(2*penalty) + excess-core)
    lower_value = float(scores @ weights - (penalty/2)*(weights @ (weights/caps)))
    if abs(upper_value - lower_value) > 5e-10*max(1., abs(upper_value)):
        raise RuntimeError('the capped threshold did not solve its scalar equation')
    return float(tau), float(upper_value), weights


def optimize(sign, side, raw, target_mean, penalty, steps):
    pinned, padding, kappa, column, caps, finish = geometry(sign, side)
    n = len(sign)
    start = raw + (target_mean - raw.mean())*padding
    current = start.copy()
    trial = current.copy()
    alpha = penalty/float(np.max(caps/padding[1:]**2))
    momentum = 1.
    tau = 0.
    best_value = np.inf
    chosen = None
    best_dual = (0., None)
    records = []
    opposite_finish = ANCHOR['anchored_tools'](sign, -side)[-1]
    for k in range(steps+1):
        tau, value, v = hinge_envelope(-trial[1:]/padding[1:], caps, penalty, tau)
        weights = np.r_[0., v/padding[1:]]
        projected = pinned(weights)
        if value < best_value:
            best_value = value
            chosen = (trial.copy(), k, tau)
        if k in (0, 4, 16, steps):
            gamma = -float(column @ weights)/kappa
            record = dict(iteration=k, soft_value=value, budget_threshold=tau, best_soft_value=best_value,
                          capped_mass=float(v.sum()), gradient_norm=float(np.linalg.norm(projected)),
                          effective_size=float(weights.sum()**2/(weights@weights)) if weights.any() else 0.,
                          hard_tail=max(0., float(finish(-trial)[0].mean())))
            if gamma > 0:
                dual = weights - projected
                dual[0] += gamma
                dual += opposite_finish(-dual)[0]
                dual /= dual.sum()
                margin = raw[0]*dual[0] - target_mean
                cost = float((dual[1:]*padding[1:]) @ (dual[1:]*padding[1:]/caps))
                scale = max(0., min(1., margin/(penalty*cost))) if cost else 0.
                record['projected_dual_lower'] = float(scale*(margin-penalty*scale*cost/2))
                if record['projected_dual_lower'] > best_value + 5e-9:
                    raise RuntimeError('the projected dual exceeded a primal value')
                if record['projected_dual_lower'] > best_dual[0]:
                    best_dual = (record['projected_dual_lower'], dual)
            records.append(record)
        if k < steps:
            updated = trial + alpha*projected
            next_momentum = (1 + sqrt(1+4*momentum**2))/2
            trial = updated + ((momentum-1)/next_momentum)*(updated-current)
            current, momentum = updated, next_momentum
    best, depth, threshold = chosen
    return records, best-start, depth, threshold, best_dual


def reference_geometry(sign, side, balls):
    """Enclose the stationary projection and exact fixed-mark padding."""
    from flint import acb, arb, ctx

    seed, phi0, error = balls
    ctx.prec = 128
    n = len(sign)
    root_n = arb(n).sqrt()
    allowed = sign == -side
    kappa = arb(int(np.count_nonzero(allowed)))/n
    omega = (1 + arb(2*n+1).sqrt())/(2*n)
    eta = (1-omega/kappa)/(omega+omega**2/kappa)
    column = [value.real for value in acb.dft([int(keep) for keep in allowed], inverse=True)]
    padding = [1 - value/kappa for value in column]
    caps = [1/(1 + eta*(kappa+value)) for value in column[1:]]
    y = [max(arb(0), -side*value) for value in seed]
    y[0] = (phi0-side*seed[0])/2
    f = acb.dft(y)
    reference = acb.dft([value if keep or i==0 else acb(0) for i, (value, keep) in enumerate(zip(f, allowed))],
                        inverse=True)
    raw = [root_n*value.real for value in reference]
    c = f[0].real/root_n
    row_error = (root_n + (n+1/kappa).sqrt())*error
    return allowed, kappa, column, padding, caps, raw, c, row_error


def certify_upper(balls, target_mean, penalty, candidate, threshold):
    """Use the scalar upper formula on an exact affine Fourier trial."""
    from flint import acb, arb

    allowed, kappa, column, padding, caps, raw, c, error = balls
    scale = 10**13
    coefficients = np.fft.fft(candidate).real
    integers = [round(scale*value) if keep else 0 for value, keep in zip(coefficients, allowed)]
    n = len(allowed)
    for i in range(1, n//2+1):
        integers[-i] = integers[i]
    rounded = [value.real/scale for value in acb.dft(integers, inverse=True)]
    mean, alpha, t = (binary_ball(value) for value in (target_mean, penalty, threshold))
    output = t
    for i in range(1,n):
        correction = rounded[i] - rounded[0]*column[i]/kappa
        y_lower = raw[i] + (mean-c)*padding[i] + correction - error
        excess = (-y_lower/padding[i]-t).upper()
        if excess <= 0:
            continue
        output += caps[i-1]*(excess**2/(2*alpha) if excess <= alpha else excess-alpha/2)
    return str(output.upper())


def binary_ball(value):
    from flint import arb

    rational = Fraction(value)
    return arb(rational.numerator)/rational.denominator


def square_formula(balls, square_root, mean, penalty):
    """The subfield tests the dual with a free overall scale."""
    from flint import arb

    _, _, _, _, _, raw, _, error = balls
    h = (square_root+1)//2
    margin = raw[0]/h - binary_ball(mean)
    margin_lower = (margin-error/h).lower()
    cost = (arb(h-2) + arb(2)/(h-1))/h
    alpha = binary_ball(penalty)
    scale = max(arb(0), min(arb(1), (margin_lower/(alpha*cost)).lower()))
    lower = scale*(margin_lower-alpha*scale*cost/2)
    return lower.lower()


def rounded_mass_one(sign, side, candidate):
    """Enclose the mark and bulk of an exact nonnegative mass-one row."""
    from flint import acb, arb

    n = len(sign)
    scale = 10**14
    coefficients = np.fft.fft(candidate).real
    integers = [round(scale*value) if a == side else 0 for value, a in zip(coefficients, sign)]
    for i in range(1,n//2+1):
        integers[-i] = integers[i]
    integers[0] = scale
    spectrum = [value.real for value in acb.dft(integers, inverse=True)]
    slack = min(value.lower() for value in spectrum)
    bump = max(0, int((-slack).upper().ceil().unique_fmpz()))
    mass = scale + n*bump
    mark = arb(sum(integers)+n*bump)/(n*mass)
    if not mark > 0:
        raise RuntimeError('independent dual rounding lost its positive mark')
    row = [(value+bump)/mass for value in spectrum[1:]]
    return mark, row


def certify_dual(sign, side, balls, penalty, target_mean, candidate):
    """Round into the opposite sector and pay any bulk negativity by a constant."""
    from flint import arb

    _, _, _, padding, caps, raw, _, error = balls
    mark, row = rounded_mass_one(sign, side, candidate)
    cost_upper = sum((value*pad)**2/cap for value,pad,cap in zip(row,padding[1:],caps)).upper()
    margin_lower = ((raw[0]-error)*mark-binary_ball(target_mean)).lower()
    alpha = binary_ball(penalty)
    if not margin_lower > 0:
        return arb(0)
    scale_dual = min(arb(1), (margin_lower/(alpha*cost_upper)).lower())
    return (scale_dual*(margin_lower-alpha*scale_dual*cost_upper/2)).lower()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--primes', nargs='*', type=int, default=[9413, 153649, 1000033])
    parser.add_argument('--square-roots', nargs='*', type=int, default=[97, 389])
    parser.add_argument('--width', type=float, default=1/64)
    parser.add_argument('--mean', type=float, default=1.)
    parser.add_argument('--penalties', nargs='+', type=float, default=[.125, 1., 8.])
    parser.add_argument('--steps', type=int, default=64)
    parser.add_argument('--certify-max-order', type=int, default=0)
    args = parser.parse_args()
    if not (0 < args.width < 1 and args.steps>=0 and isfinite(args.mean) and args.mean>0):
        parser.error('use a positive mean, width in (0,1), and nonnegative depth')
    if any(not isfinite(value) or value<=0 for value in args.penalties):
        parser.error('penalties must be positive and finite')
    cases = [(p, p, None, R17['paley_sign']) for p in args.primes]
    cases += [(s*s, s, s, R17['square_field_sign']) for s in args.square_roots]
    cert = runpy.run_path(str(RESEARCH/'parallel-defect-16.py')) if args.certify_max_order else None
    for order, characteristic, square_root, maker in sorted(cases):
        sign = maker(characteristic)
        n = len(sign)
        width, _, plus, minus, residual = next(R17['damped_trials'](sign, [args.width], 1e-11, 48))
        reference = cert['reference_balls'](sign, width, plus, minus) if order<=args.certify_max_order else None
        for side, y in ((1, minus), (-1, plus)):
            raw = sqrt(n)*np.fft.ifft((sign != side)*np.fft.fft(y)).real
            balls = reference_geometry(sign, side, reference) if reference is not None else None
            for penalty in args.penalties:
                records, candidate, depth, threshold, dual = optimize(sign, side, raw, args.mean, penalty, args.steps)
                if balls is not None:
                    from flint import arb

                    records[-1].update(certified_upper=certify_upper(balls, args.mean, penalty, candidate, threshold),
                                       certified_trial_depth=depth)
                    if square_root and side==1:
                        lower = square_formula(balls, square_root, args.mean, penalty)
                        if not arb(records[-1]['certified_upper']) >= lower:
                            raise RuntimeError('the interval upper trial missed the square lower bound')
                        records[-1]['subfield_certified_lower'] = str(lower)
                    elif dual[0] > 1e-6:
                        lower = certify_dual(sign, side, balls, penalty, args.mean, dual[1])
                        if not arb(records[-1]['certified_upper']) >= lower:
                            raise RuntimeError('the interval upper trial missed the rounded dual lower bound')
                        records[-1]['rounded_dual_certified_lower'] = str(lower)
                for record in records:
                    print(json.dumps(dict(order=order, square_root=square_root, side=side, width=width,
                                          target_mean=args.mean, penalty=penalty, reference_residual=residual)|record), flush=True)


if __name__ == '__main__':
    main()
