"""Enclose the reciprocal theta path's fourth moments and signed derivative."""

import argparse
import csv
from fractions import Fraction
from math import isfinite, sqrt
import sys

import numpy as np

from quadratic_theta import damped_trials, rounded_anchored_fft
from square_control import square_field_sign
from theta import paley_sign


def trial_stats(sign, vector, side, width):
    """Energy and allowed moments of the exactly anchored rational trial."""
    from flint import arb

    numerators, scale, transform = rounded_anchored_fft(vector)
    allowed_second = arb(0)
    forbidden_second = arb(0)
    allowed_fourth = arb(0)
    for mode, value in zip(sign, transform):
        if mode:
            amplitude = abs(value)
            second = amplitude * amplitude
            if mode == side:
                allowed_second += second
                allowed_fourth += second * second
            else:
                forbidden_second += second
    n = len(sign)
    energy = (
        arb(sum(numerators)**2) + width * allowed_second + forbidden_second / width
    ) / (n * scale**2)
    return energy, width * allowed_second / (n * scale**2), allowed_fourth / (n * scale**4)


def norm_endpoints(center, energy, opposite_energy, error):
    from flint import arb

    return max(arb(0), (center / energy.sqrt() - error).lower()), (
        center * opposite_energy.sqrt() + error
    ).upper()


def certified_stats(sign, plus, minus, width):
    from flint import arb, ctx

    ctx.prec = 160
    rational = Fraction(width)
    width_ball = arb(rational.numerator) / rational.denominator
    stats = [trial_stats(sign, x, side, width_ball) for x, side in ((plus, 1), (minus, -1))]
    first_energy, second_energy = stats[0][0], stats[1][0]
    error = max(arb(0), (first_energy * second_energy - 1).upper()).sqrt()
    fourth_error = arb(len(sign)).sqrt().sqrt() * error / width_ball.sqrt()

    second = []
    fourth = []
    for (energy, energy_sector, moment), opposite in zip(stats, (second_energy, first_energy)):
        second.append(norm_endpoints(energy_sector.nonnegative_part().sqrt(), energy, opposite, error))
        root = moment.nonnegative_part().sqrt().nonnegative_part().sqrt()
        fourth.append(norm_endpoints(root, energy, opposite, fourth_error))

    first_low, first_high = second[0]
    second_low, second_high = second[1]
    derivative = (first_low * first_low - second_high * second_high,
                  first_high * first_high - second_low * second_low)
    scale = 10**10

    def rational_endpoints(lower, upper):
        return (
            Fraction(int((scale * lower).lower().floor().unique_fmpz()), scale),
            Fraction(int((scale * upper).upper().ceil().unique_fmpz()), scale),
        )

    def fourth_power(value):
        square = value * value
        return square * square

    return (
        *rational_endpoints(*(fourth_power(x) for x in fourth[0])),
        *rational_endpoints(*(fourth_power(x) for x in fourth[1])),
        *rational_endpoints(*derivative),
        rational_endpoints(arb(0), first_high * first_high / width_ball)[1],
        rational_endpoints(arb(0), second_high * second_high / width_ball)[1],
    )


def probe(sign, widths, tolerance, rounds, certify):
    n = len(sign)
    for width, marker, plus, minus, residual in damped_trials(sign, widths, tolerance, rounds):
        plus_modes = np.abs(np.fft.fft(plus)[sign == 1])**2
        minus_modes = np.abs(np.fft.fft(minus)[sign == -1])**2
        plus_energy = plus_modes.sum() / n
        minus_energy = minus_modes.sum() / n
        plus_fourth = plus_modes @ plus_modes / n
        minus_fourth = minus_modes @ minus_modes / n
        derivative = width * (plus_energy - minus_energy)
        bounds = certified_stats(sign, plus, minus, width) if certify else (None,) * 8
        yield (
            width, width * sqrt(2 * n + 1), marker, residual, plus_energy, minus_energy, plus_fourth, minus_fourth,
            derivative, width * sqrt((n - 1) / n * (plus_fourth + minus_fourth)), *bounds,
        )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primes", nargs="*", type=int)
    parser.add_argument("--square-characteristics", nargs="*", type=int, default=[])
    parser.add_argument("--widths", nargs="*", type=float, default=[])
    parser.add_argument("--scaled-widths", nargs="*", type=float, default=[])
    parser.add_argument("--tolerance", type=float, default=2e-10)
    parser.add_argument("--rounds", type=int, default=48)
    parser.add_argument("--certify-max-order", type=int, default=0)
    args = parser.parse_args()
    cases = [(p, p, paley_sign) for p in args.primes]
    cases += [(h**2, h, square_field_sign) for h in args.square_characteristics]
    if not cases or not (args.widths or args.scaled_widths):
        parser.error("supply orders and at least one width")
    if args.rounds < 1 or any(x <= 0 or not isfinite(x) for x in (args.tolerance, *args.widths, *args.scaled_widths)):
        parser.error("provide positive finite widths and tolerance and a positive round count")

    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow((
        "field_order", "characteristic", "width", "width_times_root_order", "trial_log_mark",
        "residual", "trial_plus_allowed_energy", "trial_minus_allowed_energy",
        "plus_scaled_fourth", "minus_scaled_fourth", "trial_signed_energy",
        "trial_absolute_energy_bound", "certified_plus_lower", "certified_plus_upper",
        "certified_minus_lower", "certified_minus_upper", "certified_signed_lower", "certified_signed_upper",
        "certified_plus_allowed_energy_upper", "certified_minus_allowed_energy_upper",
    ))
    for q, h, make_sign in sorted(cases):
        widths = sorted(set(args.widths + [k / sqrt(q) for k in args.scaled_widths]), reverse=True)
        if widths[0] > 1:
            parser.error("each resulting width must be at most one")
        for row in probe(make_sign(h), widths, args.tolerance, args.rounds, q <= args.certify_max_order):
            writer.writerow((q, h, *row))
            sys.stdout.flush()


if __name__ == "__main__":
    main()
