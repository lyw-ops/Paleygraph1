"""Compare a half-angle inverse and weighted trial residuals at Paley orders."""

import argparse
import csv
from math import isfinite, sqrt
import sys

import numpy as np

from coset_activation_probe import solve_mark
from poisson_weights import weighted_iterate
from sensitivity import linearized_operator
from smoothing import kernel_action
from square_control import square_field_sign
from theta import optimize, paley_sign


def compare(sign, tau, depths, solve_lp):
    n = len(sign)
    weights = np.full(n, tau / n)
    weights[0] = 1
    roots = np.sqrt(weights)
    w = weights.sum()
    v, u, stationary_residual = weighted_iterate(sign, weights, tolerance=1e-10)
    gamma = np.arcsinh(v / (2 * roots))
    half = np.tanh(gamma / 2)
    half[0] = 0
    e = np.full(n, -1 / n)
    e[0] += 1
    column, mark, half_residual, _ = solve_mark(sign, half, e)
    source_coefficient = u[0] - 2 * roots[1]
    source_error = np.linalg.norm(linearized_operator(sign, half) @ v - source_coefficient * e)
    column_error = np.linalg.norm(column - v / source_coefficient)
    if source_error > 1e-8 or abs(mark - v[0] / source_coefficient) > 1e-8:
        raise RuntimeError(f"half-angle source failed at dimension {n}")
    half_gap = 1 - np.max(np.abs(half))
    full_gap = 1 - np.max(np.abs(v[1:] / u[1:]))
    half_weighted_norm = sqrt(((1 - half[1:] ** 2) * (v[1:] / source_coefficient) ** 2).sum())
    half_energy = 4 * (weights[1:] @ np.sinh(gamma[1:] / 2) ** 2)
    for alpha in (0.5, 0.625, 0.75, 1):
        energy = 4 * (weights[1:] @ np.sinh((1 - alpha) * gamma[1:]) ** 2)
        if energy > 2 * w ** (1 - alpha) * tau**alpha + 1e-8:
            raise RuntimeError(f"hyperbolic attenuation bound failed at dimension {n}")

    trial = np.zeros(n)
    checkpoints = set(depths)
    for depth in range(1, max(depths) + 1):
        trial = (trial + kernel_action(sign, np.hypot(trial, 2 * roots))) / 2
        if depth not in checkpoints:
            continue
        r = trial - kernel_action(sign, np.hypot(trial, 2 * roots))
        eta = np.arcsinh(trial / (2 * roots))
        midpoint = (eta + gamma) / 2
        inv_multiplier = np.cosh(midpoint)
        weighted_residual = np.linalg.norm(inv_multiplier * r)
        error = abs(v[0] - trial[0])
        difference = v - trial
        midpoint_source_error = np.linalg.norm(
            linearized_operator(sign, np.tanh(midpoint)) @ difference + kernel_action(sign, r)
        )
        if midpoint_source_error > 1e-8 or error > 2 * inv_multiplier[0] * weighted_residual + 1e-8:
            raise RuntimeError(f"midpoint certificate failed at dimension {n}, depth {depth}")

        cost = n * np.exp(np.abs(eta)) * r**2
        cost[0] = 0
        stationary_cost = (u @ cost) / sqrt(n * w)
        upper_weighted_bulk_sq = 0.5 * np.dot(r[1:], r[1:]) + 0.25 * sqrt(w / tau) * stationary_cost
        if np.linalg.norm((inv_multiplier * r)[1:]) ** 2 > upper_weighted_bulk_sq + 1e-8:
            raise RuntimeError(f"stationary cost bound failed at dimension {n}, depth {depth}")
        plus_lp = minus_lp = ""
        if solve_lp:
            plus_lp = cost @ optimize(sign, 1, cost)[1] / n
            minus_lp = cost @ optimize(sign, -1, cost)[1] / n
        yield (
            depth, v[0], trial[0], mark, error, full_gap, half_gap, half_weighted_norm, half_energy,
            np.linalg.norm(r), weighted_residual, r[0], stationary_cost, plus_lp, minus_lp,
            source_error, column_error, half_residual, midpoint_source_error, stationary_residual,
        )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primes", nargs="*", type=int)
    parser.add_argument("--square-characteristics", nargs="+", type=int, default=[])
    parser.add_argument("--tau", nargs="+", type=float, default=[0.05, 0.01])
    parser.add_argument("--depths", nargs="+", type=int, default=[16, 64, 256, 1024])
    parser.add_argument("--lp-max-order", type=int, default=500)
    args = parser.parse_args()
    orders = [(p, p) for p in args.primes] + [(r * r, r) for r in args.square_characteristics]
    if not orders or any(not isfinite(tau) or not 0 < tau <= 1 for tau in args.tau) or min(args.depths) < 1:
        parser.error("provide field orders, floors in (0,1] and positive depths")
    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow((
        "field_order", "characteristic", "tau", "depth", "stationary_marker", "trial_marker",
        "half_mark", "marker_error", "full_diagonal_gap", "half_diagonal_gap", "half_weighted_bulk_l2",
        "half_q_energy", "residual_l2", "weighted_residual_l2", "residual_mark", "stationary_cost",
        "plus_lp", "minus_lp", "half_source_error", "half_column_error", "half_inverse_residual",
        "midpoint_source_error", "stationary_residual",
    ))
    for order, characteristic in sorted(orders):
        sign = paley_sign(order) if order == characteristic else square_field_sign(characteristic)
        for tau in args.tau:
            for row in compare(sign, tau, args.depths, order <= args.lp_max_order):
                writer.writerow((order, characteristic, tau, *row))
            sys.stdout.flush()


if __name__ == "__main__":
    main()
