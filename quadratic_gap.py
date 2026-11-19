"""Bound one sign's energy at a width from a nonnegative larger-width trial."""

import argparse
import csv
from fractions import Fraction
from math import isfinite, sqrt
import sys

import numpy as np

from quadratic_theta import damped_trials, rounded_anchored_fft
from square_control import square_field_sign
from theta import paley_sign


def threshold(bulk, capacity):
    if capacity >= len(bulk):
        return 0.0
    k = int(max(0, capacity))
    return float(max(0, -np.partition(bulk, k)[k]))


def trial_metrics(sign, side, b, r, s):
    n = len(sign)
    transform = np.fft.fft(b)
    modes = np.abs(transform)**2 / n
    pure = modes[sign == side].sum()
    foreign = modes[sign == -side].sum()
    upper = modes[0] + r * pure + foreign / r
    capacity = sqrt(n * upper) - 1
    shifts = []
    deficits = []
    for width in (r, s):
        multiplier = np.where(sign == side, width, 1 / width)
        multiplier[0] = 1
        bulk = np.fft.ifft(multiplier * transform).real[1:]
        t = threshold(bulk, capacity)
        shifts.append(t)
        deficits.append(max(0.0, bulk @ b[1:] + np.maximum(-bulk - t, 0).sum() + t * capacity))
    move_cost = (r - s)**2 / r * pure + r * (1 / r - 1 / s)**2 * foreign
    return upper, pure, move_cost, deficits, shifts


def numeric_bound(upper, pure, move_cost, deficit, r):
    root_error = (sqrt(move_cost) + sqrt(move_cost + 4 * deficit)) / 2
    lower = upper - 2 * deficit - move_cost
    return (sqrt(pure) + root_error / sqrt(r))**2 / lower if lower > 0 else None


def binary_ball(value):
    from flint import arb

    rational = Fraction(value)
    return arb(rational.numerator) / rational.denominator


def rounded_trial_sectors(sign, side, b):
    from flint import arb

    n = len(sign)
    numerators, scale, transform = rounded_anchored_fft(b)
    allowed = arb(0)
    forbidden = arb(0)
    for position, value in zip(sign, transform):
        if position:
            amplitude = abs(value)
            squared = amplitude * amplitude
            if position == side:
                allowed += squared
            else:
                forbidden += squared
    denominator = n * scale**2
    return (
        numerators, scale, transform, arb(sum(numerators)**2) / denominator,
        allowed / denominator, forbidden / denominator,
    )


def capped_deficit_upper(sign, side, numerators, scale, transform, width, shift, capacity):
    from flint import acb, arb

    shift = binary_ball(shift)
    pressure = [
        coefficient if p == 0 else coefficient * width if p == side else coefficient / width
        for p, coefficient in zip(sign, transform)
    ]
    bulk = [value.real / scale for value in acb.dft(pressure, inverse=True)[1:]]
    deficit = sum((g * i / scale + max(arb(0), (-g - shift).upper())
                   for g, i in zip(bulk, numerators[1:])), arb(0)) + shift * capacity
    return max(arb(0), deficit.upper())


def certified_bound(sign, side, b, r, s, shifts):
    from flint import arb, ctx

    ctx.prec = 128
    r, s = binary_ball(r), binary_ball(s)
    numerators, scale, transform, mean, pure, foreign = rounded_trial_sectors(sign, side, b)
    upper = mean + r * pure + foreign / r
    move_cost = (s - r) * (s - r) / r * pure + r * (1 / r - 1 / s) * (1 / r - 1 / s) * foreign
    capacity = (len(sign) * upper).sqrt() - 1
    bounds = []
    scale_out = 10**8
    for width, split_cost, shift in zip((r, s), (arb(0), move_cost), shifts):
        deficit = capped_deficit_upper(sign, side, numerators, scale, transform, width, shift, capacity)
        split_cost = max(arb(0), split_cost.upper())
        root_error = (split_cost.sqrt() + (split_cost + 4 * deficit).sqrt()) / 2
        lower = upper - 2 * deficit - split_cost
        bound = None
        if lower > 0:
            norm = pure.nonnegative_part().sqrt() + root_error / r.sqrt()
            value = norm * norm / lower
            bound = Fraction(int((scale_out * value).upper().ceil().unique_fmpz()), scale_out)
        bounds.append(bound)
    return bounds


def probe(sign, r, s, certify, compare_target):
    widths = [s, r] if compare_target else [s]
    trials = damped_trials(sign, widths, tolerance=2e-10, rounds=72)
    reference = next(trials)
    target = next(trials) if compare_target else None
    for side, off in ((1, 2), (-1, 3)):
        trial = reference[off]
        b = np.minimum(trial / trial[0], 1.0)
        upper, pure, move_cost, deficits, shifts = trial_metrics(sign, side, b, r, s)
        observed = None
        if target is not None:
            observed = np.sum(np.abs(np.fft.fft(target[off])[sign == side])**2) / len(sign)
        bounds = certified_bound(sign, side, b, r, s, shifts) if certify else (None, None)
        yield (
            side, reference[-1], target[-1] if target is not None else None,
            observed, deficits[0] / r, deficits[1] / r,
            move_cost / r, numeric_bound(upper, pure, 0.0, deficits[0], r),
            numeric_bound(upper, pure, move_cost, deficits[1], r), *bounds,
        )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primes", nargs="*", type=int)
    parser.add_argument("--square-characteristics", nargs="*", type=int, default=[])
    parser.add_argument("--width-factor", type=float, default=1.5)
    parser.add_argument("--certify-max-order", type=int, default=0)
    parser.add_argument("--skip-target-solve", action="store_true",
                        help="leave the floating-point target comparison blank")
    args = parser.parse_args()
    cases = [(p, p, paley_sign) for p in args.primes]
    cases += [(h**2, h, square_field_sign) for h in args.square_characteristics]
    if not cases or args.width_factor <= 1 or not isfinite(args.width_factor):
        parser.error("provide orders and a finite width factor greater than one")
    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow((
        "order", "characteristic", "width", "reference_width", "sign", "reference_residual",
        "target_residual", "numerical_target_energy", "direct_gap_over_r", "ref_gap_over_r",
        "move_cost_over_r", "direct_upper", "split_upper", "certified_direct_upper", "certified_split_upper",
    ))
    for q, h, maker in sorted(cases):
        r = q**(-1 / 3)
        s = args.width_factor * r
        if s > 1:
            parser.error(f"reference width exceeds one at order {q}")
        for row in probe(maker(h), r, s, q <= args.certify_max_order, not args.skip_target_solve):
            writer.writerow((q, h, r, s, *row))
            sys.stdout.flush()


if __name__ == "__main__":
    main()
