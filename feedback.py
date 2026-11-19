"""Measure mixed correlations and fourth-update terms in Fourier smoothing."""

import argparse
import csv
from math import isfinite, sqrt
import sys

import numpy as np
from numpy.polynomial.chebyshev import chebval

from theta import paley_sign


def apply_feedback(sign, values):
    return np.fft.fft(sign * np.fft.ifft(values).real).real


def mixed_moments(prime, degrees):
    sign = paley_sign(prime)
    x = np.fft.fft(sign).real / sqrt(prime)
    for degree in degrees:
        polynomial = chebval(x, [0] * degree + [1])
        feedback = apply_feedback(sign, polynomial)
        yield (
            prime, degree, np.mean(polynomial * feedback), np.mean(x * feedback ** 2),
            np.mean(x ** 3 * feedback ** 2), np.mean(feedback ** 3),
            np.mean(feedback ** 2), np.max(np.abs(feedback)),
        )


def fourth_step(prime, smoothing_weights):
    sign = paley_sign(prime)
    n = len(sign)
    x = np.fft.fft(sign).real / sqrt(n)
    first = 2 * x
    quadratic = apply_feedback(sign, 2 * (n / prime) * x ** 2)
    proxy = apply_feedback(sign, (first + quadratic) ** 2)
    proxy_moment = np.mean(x * proxy ** 2)

    for tau in smoothing_weights:
        def phi(values):
            return np.hypot(values, 2 * sqrt(tau))

        second = first + apply_feedback(sign, phi(first))
        correction = apply_feedback(sign, phi(second))
        slope = np.mean(x * first / phi(first) * correction)
        fourth = np.mean(x * phi(first + correction))
        curvature = np.mean(x * (phi(first + correction) + phi(first - correction)) / 2)
        yield (
            prime, tau, fourth, slope, curvature, proxy_moment,
            sqrt(np.mean(correction ** 2)), np.max(np.abs(correction)),
        )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primes", nargs="+", type=int)
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--degrees", nargs="+", type=int, default=[2, 4, 6])
    modes.add_argument(
        "--fourth", nargs="+", type=float, metavar="TAU",
        help="measure fourth-update terms at the given positive smoothing weights",
    )
    args = parser.parse_args()
    if any(degree <= 0 or degree % 2 for degree in args.degrees):
        parser.error("degrees must be positive and even")

    writer = csv.writer(sys.stdout, lineterminator="\n")
    if args.fourth:
        if any(not isfinite(tau) or tau <= 0 for tau in args.fourth):
            parser.error("smoothing weights must be positive and finite")
        writer.writerow((
            "p", "tau", "fourth_bulk_marker", "linear_response", "even_response",
            "quadratic_proxy_moment", "feedback_l2_normalized", "feedback_max_abs",
        ))
        for prime in args.primes:
            writer.writerows(fourth_step(prime, args.fourth))
        return

    writer.writerow((
        "p", "degree", "mean_T_B", "mean_x_B2", "mean_x3_B2",
        "mean_B3", "mean_B2", "max_abs_B",
    ))
    for prime in args.primes:
        writer.writerows(mixed_moments(prime, args.degrees))


if __name__ == "__main__":
    main()
