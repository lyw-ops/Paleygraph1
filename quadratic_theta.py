"""Evaluate reciprocal regularized Paley theta programs by FFT."""

import argparse
import csv
from fractions import Fraction
from math import asinh, isfinite, log, sqrt
import sys

import numpy as np

from poisson_weights import weighted_iterate
from smoothing import kernel_action
from square_control import square_field_sign
from theta import paley_sign


def sector_norms(sign, vector, side):
    constant = vector.mean()
    reflected = side * kernel_action(sign, vector)
    centered = vector - constant
    allowed = (centered + reflected) / 2
    forbidden = (centered - reflected) / 2
    return len(vector) * constant**2, allowed @ allowed, forbidden @ forbidden


def rounded_anchored_fft(vector):
    """Fourier transform of an exact nonnegative trial at anchor one."""
    from flint import acb

    scale = 10**12
    numerators = [round(scale * float(value / vector[0])) for value in vector]
    numerators[0] = scale
    return numerators, scale, acb.dft(numerators)


def certified_upper_energy(sign, vector, side, width):
    """Round an anchored nonnegative vector and enclose its quadratic energy."""
    from flint import arb, ctx

    ctx.prec = 128
    numerators, scale, transform = rounded_anchored_fft(vector)
    width_fraction = Fraction(width)
    width_ball = arb(width_fraction.numerator) / width_fraction.denominator
    allowed = sum((abs(value)**2 for value, sign_value in zip(transform, sign) if sign_value == side), arb(0))
    forbidden = sum((abs(value)**2 for value, sign_value in zip(transform, sign) if sign_value == -side), arb(0))
    energy = (
        arb(sum(numerators)**2) + width_ball * allowed + forbidden / width_ball
    ) / (len(sign) * scale**2)
    return Fraction(int((energy * scale).upper().ceil().unique_fmpz()), scale)


def damped_trials(sign, widths, tolerance, rounds):
    n = len(sign)
    weights = np.zeros(n)
    weights[0] = 1
    vector = None
    for width in widths:
        damping = (1 - width) / (1 + width)
        vector, _, residual = weighted_iterate(
            sign, weights, tolerance=tolerance, rounds=rounds, damping=damping, initial=vector,
        )

        plus = np.maximum(vector, 0)
        minus = np.maximum(-vector, 0)
        marker = asinh(vector[0] / 2)
        plus[0] = np.exp(marker)
        minus[0] = 1 / plus[0]
        yield width, marker, plus, minus, residual


def probe(sign, widths, tolerance, rounds, certify=False):
    n = len(sign)
    for width, marker, plus, minus, residual in damped_trials(sign, widths, tolerance, rounds):
        constant_plus, allowed_plus, forbidden_plus = sector_norms(sign, plus, 1)
        constant_minus, allowed_minus, forbidden_minus = sector_norms(sign, minus, -1)
        energy_plus = constant_plus + width * allowed_plus + forbidden_plus / width
        energy_minus = constant_minus + width * allowed_minus + forbidden_minus / width
        gap = (1 + width)**2 / (4 * width) * residual**2
        gap_error = abs(energy_plus + energy_minus - 2 - gap)
        if gap_error > 1e-8 or energy_plus * energy_minus < 1 - 1e-9:
            raise RuntimeError("metric residual identity failed")
        # Theta's regularized log marker equals -log(M_+)/2.
        lower = marker - log(energy_plus) / 2
        upper = marker + log(energy_minus) / 2
        certified_lower = certified_upper = None
        if certify:
            certified_upper = certified_upper_energy(sign, plus, 1, width)
            certified_lower = 1 / certified_upper_energy(sign, minus, -1, width)
        yield (
            width, width * sqrt(2 * n + 1), marker, lower, upper,
            sqrt(constant_plus), width * allowed_plus, width * allowed_minus,
            (width * allowed_minus - width * allowed_plus) / 2,
            np.count_nonzero(plus[1:]), np.count_nonzero(minus[1:]), residual, gap_error,
            certified_lower, certified_upper,
        )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primes", nargs="*", type=int)
    parser.add_argument("--square-characteristics", nargs="*", type=int, default=[])
    parser.add_argument("--widths", nargs="*", type=float, default=[])
    parser.add_argument("--scaled-widths", nargs="*", type=float, default=[])
    parser.add_argument("--tolerance", type=float, default=2e-9)
    parser.add_argument("--rounds", type=int, default=16)
    parser.add_argument("--certify-max-order", type=int, default=0)
    args = parser.parse_args()
    cases = [(p, p, paley_sign) for p in args.primes]
    cases += [(p**2, p, square_field_sign) for p in args.square_characteristics]
    if not cases or not (args.widths or args.scaled_widths):
        parser.error("supply field orders and fixed widths or widths scaled by 1/sqrt(order)")
    if any(not isfinite(x) or x <= 0 for x in [args.tolerance, *args.widths, *args.scaled_widths]):
        parser.error("widths and tolerance must be positive and finite")
    if args.rounds < 1:
        parser.error("rounds must be positive")

    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow((
        "field_order", "characteristic", "width", "width_times_root_order",
        "trial_marker", "marker_lower", "marker_upper", "normalized_mass",
        "weighted_plus_energy", "weighted_minus_energy", "trial_log_width_derivative",
        "trial_plus_bulk_support", "trial_minus_bulk_support", "fixed_point_residual", "metric_identity_error",
        "certified_M_plus_lower", "certified_M_plus_upper",
    ))
    for order, characteristic, make_sign in sorted(cases):
        widths = sorted(set(args.widths + [scale / sqrt(order) for scale in args.scaled_widths]), reverse=True)
        if widths[0] > 1:
            parser.error("each resulting width must be at most one")
        sign = make_sign(characteristic)
        for row in probe(sign, widths, args.tolerance, args.rounds, order <= args.certify_max_order):
            writer.writerow((order, characteristic, *row))
            sys.stdout.flush()


if __name__ == "__main__":
    main()
