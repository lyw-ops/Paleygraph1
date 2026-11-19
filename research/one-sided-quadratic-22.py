"""Compute interval bounds for the reciprocal one-sided Fourier quadratic."""

import argparse
from fractions import Fraction
import json
from math import sqrt
from pathlib import Path
import runpy

import numpy as np


RESEARCH = Path(__file__).resolve().parent
R17 = runpy.run_path(str(RESEARCH / 'parallel-repair-17.py'))


def iterate(project, width, start, steps):
    current = start.copy()
    trial = current.copy()
    momentum = 1.
    best = (np.inf, None, None, None)
    n = len(start)
    for step in range(steps + 1):
        if step in (0, 16, 64, steps):
            filtered = project(current)
            value = float(current.sum())**2/n + float(filtered @ filtered)/width
            if value < best[0]:
                best = value, current.copy(), filtered, step
        if step == steps:
            break
        updated = np.maximum(trial - project(trial) - width*trial.mean(), 0.)
        updated[0] = 1.
        next_momentum = (1 + sqrt(1 + 4*momentum**2))/2
        trial = updated + ((momentum-1)/next_momentum)*(updated-current)
        current, momentum = updated, next_momentum
    return best


def one_case(sign, side, width, start, steps, mark, target_mean):
    n = len(sign)
    project, kappa, omega, _, _ = R17['sector_tools'](sign, -side)
    unit = np.zeros(n)
    unit[0] = 1.
    column = project(unit)
    other_column = unit - 1/n - column
    other_kappa = other_column[0]
    if kappa <= 0 or other_kappa <= 0:
        raise ValueError('the experiment requires both nonconstant sectors')
    if start is None:
        start = np.maximum(1 + other_column/omega, 0.)
        start /= start[0]
    value, b, filtered, step = iterate(project, width, start, steps)
    b_mean = float(b.mean())
    witness = b_mean + filtered/width
    witness += max(0., -float(witness.min()))
    witness_projection = witness - witness.mean()
    witness_cost = n*float(witness.mean())**2 + width*float(witness_projection @ witness_projection)
    lower = float(witness[0])**2/witness_cost
    if lower > value + 2e-9:
        raise RuntimeError('the reciprocal witness exceeded the upper trial')
    witness_off = witness[1:]
    effective_size = float(witness_off.sum())**2/float(witness_off @ witness_off)
    mark_over_mean = float(witness[0])/(sqrt(n)*float(witness.mean()))
    scaled = mark*sqrt(n)
    needed_mean = scaled*b_mean
    projection_error = scaled*sqrt(float(filtered @ filtered) + float(filtered[0])**2/other_kappa)
    result = dict(step=step, width=width, trial_upper=value, witness_lower=lower,
                  normalized_witness_mark=mark_over_mean, witness_effective_size=effective_size,
                  trial_required_mean=needed_mean, projection_bound=projection_error)
    if needed_mean <= target_mean:
        padding = 1 - other_column/other_kappa
        repaired = scaled*(b - filtered + filtered[0]*other_column/other_kappa)
        repaired += (target_mean-needed_mean)*padding
        defect = float(np.linalg.norm(np.minimum(repaired, 0.)))
        if defect > projection_error + 1e-9 or abs(repaired[0]-scaled) > 1e-9:
            raise RuntimeError('the pinned repair exceeded its projection bound')
        result['pinned_trial_defect'] = defect
    return result, b, witness


def rational_ball(value, arb):
    number = Fraction(value)
    return arb(number.numerator)/number.denominator


def certify(sign, side, scale, b, witness, mark, target_mean, square_root):
    from flint import acb, arb, ctx

    ctx.prec = 128
    n = len(sign)
    root_n = arb(n).sqrt()
    width = rational_ball(scale, arb)/root_n
    mark = rational_ball(mark, arb)
    target_mean = rational_ball(target_mean, arb)
    quantum = 10**14
    allowed = sign == side
    integers = [round(float(value)*quantum) for value in b]
    if integers[0] != quantum or min(integers) < 0:
        raise RuntimeError('the rounded upper trial is not anchored and nonnegative')
    spectrum = acb.dft(integers)
    mass = arb(sum(integers))/quantum
    half = n//2
    energy = sum((abs(spectrum[j])/quantum)**2*(1 if j+j == n else 2)
                 for j in range(1, half+1) if allowed[j])/n
    upper = (mass**2/n + energy/width).upper()
    required_mean = (mark*mass/root_n).upper()

    coefficients = np.fft.rfft(witness).real
    integers = [round(float(coefficients[j if j <= half else n-j])*quantum) if keep or j == 0 else 0
                for j, keep in enumerate(allowed)]
    inverse = acb.dft(integers, inverse=True)
    smallest = min(value.real.lower() for value in inverse)
    if smallest < 0:
        integers[0] += n*int((-smallest).upper().ceil().unique_fmpz())
    marked_sum = sum(integers)
    if marked_sum <= 0:
        raise RuntimeError('the rounded Fourier witness has nonpositive anchor')
    witness_lower = (arb(marked_sum)**2/(n*(arb(integers[0])**2 +
                     width*sum(value**2 for value in integers[1:])))).lower()
    if witness_lower > upper:
        raise RuntimeError('the certified interval is empty')
    result = dict(certified_lower=str(witness_lower), certified_upper=str(upper),
                  certified_required_mean_upper=str(required_mean))
    if required_mean <= target_mean:
        kappa = arb(int(np.count_nonzero(allowed)))/n
        other_kappa = 1 - arb(1)/n - kappa
        projection_bound = (mark*root_n*(energy*(1 + kappa/other_kappa)).sqrt()).upper()
        result['certified_pinned_bound_over_n14'] = str((projection_bound/root_n.sqrt()).upper())
    if square_root is not None and side == 1:
        h = (square_root+1)//2
        subfield = (1/(arb(h*h)/n + width*(h-arb(h*h)/n))).lower()
        if subfield > upper:
            raise RuntimeError('the certified upper trial missed the subfield bound')
        result['certified_subfield_lower'] = str(subfield)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('primes', type=int, nargs='*')
    parser.add_argument('--square-roots', type=int, nargs='*', default=[])
    parser.add_argument('--scales', type=Fraction, nargs='+', default=list(map(Fraction, ('1/4', '1', '4', '16'))))
    parser.add_argument('--mark', type=Fraction, default=Fraction('0.98'))
    parser.add_argument('--mean', type=Fraction, default=Fraction(1))
    parser.add_argument('--steps', type=int, default=128)
    parser.add_argument('--certify-max-order', type=int, default=0)
    args = parser.parse_args()
    if args.mark <= 0 or args.mean <= 0 or args.steps < 0:
        parser.error('use positive mark and mean and a nonnegative number of steps')
    cases = [(p, p, None, R17['paley_sign']) for p in args.primes]
    cases += [(s*s, s, s, R17['square_field_sign']) for s in args.square_roots]
    for order, characteristic, square_root, maker in sorted(cases):
        sign = maker(characteristic)
        n = len(sign)
        for side in (1, -1):
            start = None
            for scale in sorted(set(args.scales), reverse=True):
                width = float(scale)/sqrt(n)
                if not 0 < width <= 1:
                    parser.error('all widths R/sqrt(n) must lie in (0, 1]')
                result, start, witness = one_case(sign, side, width, start, args.steps,
                                                  float(args.mark), float(args.mean))
                if order <= args.certify_max_order:
                    result.update(certify(sign, side, scale, start, witness, args.mark, args.mean, square_root))
                print(json.dumps(dict(order=order, square_root=square_root, witness_sign=side,
                                      scale=str(scale), mark=str(args.mark), mean=str(args.mean)) | result), flush=True)


if __name__ == '__main__':
    main()
