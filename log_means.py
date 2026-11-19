"""Probe the mean bulk logarithm along the Paley smoothing path."""

import argparse
import csv
from math import isfinite, sqrt
import sys

import numpy as np

from smoothing import smoothing
from square_control import square_field_sign
from theta import paley_sign


def path_rows(sign, weights, tolerance, max_steps):
    n = len(sign)
    bulk_fraction = 1 - 1 / n
    previous = None
    for tau in weights:
        vector, metrics = smoothing(sign, tau, tolerance, max_steps)
        residual, evaluations = metrics[-2:]
        gamma = np.arcsinh(vector / (2 * sqrt(tau / n)))
        gamma[0] = np.arcsinh(vector[0] / 2)
        mean = gamma[1:].sum() / n
        total_weight = 1 + tau * bulk_fraction
        row = [tau, gamma[0], mean, residual, evaluations - 1]
        if previous is None:
            yield row + ["", "", "", ""]
        else:
            previous_tau, previous_gamma, previous_mean, previous_total_weight = previous
            scale = sqrt(tau * previous_tau)
            difference = gamma - previous_gamma
            common_total = sqrt(total_weight * previous_total_weight)
            positive = np.exp(difference[0]) + scale * np.exp(difference[1:]).sum() / n
            negative = np.exp(-difference[0]) + scale * np.exp(-difference[1:]).sum() / n
            gap = abs(difference[0] + scale * (mean - previous_mean))
            # Rationalize the distance between the normalized root weights.
            budget = bulk_fraction * (sqrt(tau) - sqrt(previous_tau)) ** 2 / (
                common_total + 1 + bulk_fraction * scale
            )
            yield row + [positive - common_total, negative - common_total, gap, budget]
        previous = tau, gamma, mean, total_weight


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primes", nargs="*", type=int)
    parser.add_argument("--square-characteristics", nargs="*", type=int, default=[])
    parser.add_argument("--interval", nargs=2, type=float, default=[0.05, 8.0])
    parser.add_argument("--count", type=int, default=25)
    parser.add_argument("--max-steps", type=int, default=20000)
    parser.add_argument("--tolerance", type=float, default=1e-10)
    args = parser.parse_args()
    orders = [(p, "prime", paley_sign) for p in args.primes]
    orders += [(p, "square", square_field_sign) for p in args.square_characteristics]
    if not orders:
        parser.error("supply prime orders or square characteristics")
    if any(not isfinite(x) or x <= 0 for x in [*args.interval, args.tolerance]):
        parser.error("interval endpoints and tolerance must be finite and positive")
    if args.interval[0] >= args.interval[1] or args.count < 2 or args.max_steps < 3:
        parser.error("use an increasing interval, count at least 2, and max-steps at least 3")

    weights = np.geomspace(*args.interval, args.count)
    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow([
        "q", "field", "tau", "marked_gamma", "bulk_log_mean", "residual_l2", "steps",
        "cross_plus_error", "cross_minus_error", "linearized_gap", "linearized_budget",
    ])
    for characteristic, field, make_sign in orders:
        order = characteristic if field == "prime" else characteristic ** 2
        sign = make_sign(characteristic)
        for row in path_rows(sign, weights, args.tolerance, args.max_steps):
            writer.writerow((order, field, *row))


if __name__ == "__main__":
    main()
