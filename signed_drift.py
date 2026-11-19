"""Compare signed iterate correlations with stationary and LP spectra."""

import argparse
import csv
from math import isfinite, sqrt
import sys

import numpy as np

from smoothing import kernel_action, smoothing
from square_control import square_field_sign
from theta import optimize, paley_sign


def drift_rows(sign, tau, depths, solve_lp):
    n = len(sign)
    weights = np.full(n, tau / n)
    weights[0] = 1
    total_weight = weights.sum()
    roots = np.sqrt(weights)
    target, metrics = smoothing(sign, tau, 1e-10, 20000)
    gamma = np.arcsinh(target / (2 * roots))
    stationary_log = np.dot(weights, gamma)
    plus = roots * np.exp(gamma)
    minus = roots * np.exp(-gamma)

    vector = np.zeros(n)
    total_log = total_mass = cross_plus = cross_minus = 0.0
    depth_set = set(depths)
    for depth in range(1, max(depths) + 1):
        activation = np.hypot(vector, 2 * roots)
        gamma = np.arcsinh(vector / (2 * roots))
        total_log += np.dot(weights, gamma)
        total_mass += activation.sum() / sqrt(n)
        cross_plus += np.dot(roots * np.exp(-gamma), plus)
        cross_minus += np.dot(roots * np.exp(gamma), minus)
        vector = (vector + kernel_action(sign, activation)) / 2
        if depth not in depth_set:
            continue

        mean_log = total_log / depth
        baseline = sqrt(total_weight) * total_mass / (2 * depth)
        plus_drift = np.dot(vector, plus) / depth
        minus_drift = -np.dot(vector, minus) / depth
        plus_lp = minus_lp = ""
        if solve_lp:
            scale = sqrt(total_weight / n) / depth
            plus_lp = scale * np.dot(vector, optimize(sign, 1, vector)[1])
            minus_lp = -scale * np.dot(vector, optimize(sign, -1, -vector)[1])
        yield (
            depth, stationary_log, mean_log, baseline, plus_drift, minus_drift, plus_lp, minus_lp,
            cross_plus / depth - baseline - plus_drift,
            cross_minus / depth - baseline - minus_drift,
            np.linalg.norm(vector) ** 2 / depth, metrics[-2],
        )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primes", nargs="*", type=int)
    parser.add_argument("--square-characteristics", nargs="*", type=int, default=[])
    parser.add_argument("--tau", nargs="+", type=float, default=[0.05, 0.5])
    parser.add_argument("--depths", nargs="+", type=int, default=[8, 32, 128, 512])
    parser.add_argument("--lp-max-order", type=int, default=2500)
    args = parser.parse_args()
    orders = [(p, "prime", paley_sign) for p in args.primes]
    orders += [(p, "square", square_field_sign) for p in args.square_characteristics]
    if not orders:
        parser.error("supply prime orders or square characteristics")
    if any(not isfinite(tau) or tau <= 0 for tau in args.tau) or min(args.depths) < 1:
        parser.error("tau and depths must be positive and finite")

    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow([
        "q", "field", "tau", "depth", "stationary_log", "mean_iterate_log", "baseline",
        "plus_drift", "minus_drift", "plus_lp", "minus_lp", "plus_identity_error",
        "minus_identity_error", "iterate_norm_sq_over_depth", "stationary_residual_l2",
    ])
    for characteristic, field, make_sign in orders:
        order = characteristic if field == "prime" else characteristic ** 2
        sign = make_sign(characteristic)
        for tau in args.tau:
            for row in drift_rows(sign, tau, args.depths, order <= args.lp_max_order):
                writer.writerow((order, field, tau, *row))


if __name__ == "__main__":
    main()
