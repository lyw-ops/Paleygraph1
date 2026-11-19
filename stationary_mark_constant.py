"""Compare marked and constant responses in each stationary sign block."""

import argparse
import csv
from math import isfinite, sqrt
import sys

import numpy as np
from scipy.sparse.linalg import LinearOperator, cg

from poisson_weights import weighted_iterate
from smoothing import kernel_action
from square_control import square_field_sign
from theta import paley_sign


def compare(sign, tau, alphas):
    n = len(sign)
    weights = np.full(n, tau / n)
    weights[0] = 1
    v, u, stationary_residual = weighted_iterate(sign, weights, tolerance=1e-10)
    gamma = np.arcsinh(v / (2 * np.sqrt(weights)))
    kernel_column = np.fft.ifft(sign).real
    q = 2 * n + 1
    total_weight = weights.sum()

    for alpha in alphas:
        diagonal = np.tanh(alpha * gamma)
        diagonal[0] = 0
        for sigma in (1, -1):
            indices = np.flatnonzero(sigma * diagonal > 0)
            absolute_diagonal = np.abs(diagonal[indices])
            multiplier = np.sqrt(absolute_diagonal)

            def apply(x):
                vector = np.zeros(n)
                vector[indices] = multiplier * x
                return x - sigma * multiplier * kernel_action(sign, vector)[indices]

            mark_source = sigma * multiplier * kernel_column[indices]
            constant_source = multiplier / sqrt(n)
            if len(indices):
                operator = LinearOperator((len(indices), len(indices)), matvec=apply, dtype=np.float64)
                mark, info_mark = cg(operator, mark_source, rtol=1e-12, maxiter=10000)
                constant, info_constant = cg(operator, constant_source, rtol=1e-12, maxiter=10000)
                solve_residual = max(
                    np.linalg.norm(apply(mark) - mark_source),
                    np.linalg.norm(apply(constant) - constant_source),
                )
                if info_mark or info_constant or solve_residual > 1e-9:
                    raise RuntimeError(f"block solve failed at dimension {n}, sign {sigma}, alpha {alpha}")
            else:
                mark = constant = np.empty(0)
                solve_residual = 0.0

            marked_response = mark_source @ mark
            constant_response = constant_source @ constant
            marked_defect = 1 + sigma / n - marked_response
            constant_defect = 1 - constant_response
            cross_defect = 1 / sqrt(n) + constant_source @ mark
            positive_spectrum = (u + sigma * v) / 2
            a = positive_spectrum[0]
            directional_defect = (
                total_weight * constant_defect - 2 * sqrt(total_weight) * a * cross_defect
                + a**2 * marked_defect
            )
            removed = positive_spectrum.copy()
            removed[0] = 0
            removed[indices] -= np.abs(v[indices])
            trial_bound = removed @ (removed - sigma * kernel_action(sign, removed))
            trial_bound += np.dot((1 - absolute_diagonal) / absolute_diagonal, v[indices] ** 2)

            opposite = (1 + (-1 - sigma * n * kernel_column) / (sqrt(q) + 1)) / sqrt(n)
            opposite[0] = (1 + (n - 1 + sigma) / (sqrt(q) + 1)) / sqrt(n)
            witness_cost = ((opposite @ opposite) + 1) / 2
            witness_cost += np.dot(absolute_diagonal / (1 - absolute_diagonal), opposite[indices] ** 2)
            lower_bound = opposite[0] ** 2 / witness_cost
            if not -1e-8 <= directional_defect <= trial_bound + 1e-8 or marked_defect < lower_bound - 1e-8:
                raise RuntimeError(f"quadratic bounds failed at dimension {n}, sign {sigma}, alpha {alpha}")
            estimate = sqrt(total_weight * constant_defect / marked_defect)
            yield (
                alpha, sigma, len(indices), a, marked_response, constant_response,
                marked_defect, constant_defect, cross_defect, directional_defect,
                trial_bound, lower_bound, estimate, solve_residual, stationary_residual,
            )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primes", type=int, nargs="*")
    parser.add_argument("--square-characteristics", type=int, nargs="+", default=[])
    parser.add_argument("--tau", type=float, nargs="+", default=[0.01, 0.0005])
    parser.add_argument("--alpha", type=float, nargs="+", default=[0.5, 1])
    args = parser.parse_args()
    orders = [(p, p) for p in args.primes] + [(r * r, r) for r in args.square_characteristics]
    if not orders or any(not isfinite(tau) or not 0 < tau <= 1 for tau in args.tau):
        parser.error("provide field orders and finite floors in (0,1]")
    if any(not isfinite(alpha) or not 0.5 <= alpha <= 1 for alpha in args.alpha):
        parser.error("alpha must lie in [1/2,1]")
    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow((
        "field_order", "characteristic", "tau", "alpha", "sign", "block_size",
        "stationary_spectrum_mark", "marked_response", "constant_response",
        "marked_defect", "constant_defect", "cross_defect", "directional_defect",
        "trial_bound", "marked_defect_witness_lower", "mark_estimate",
        "solve_residual", "stationary_residual",
    ))
    for order, characteristic in sorted(orders):
        sign = paley_sign(order) if order == characteristic else square_field_sign(characteristic)
        for tau in args.tau:
            for row in compare(sign, tau, args.alpha):
                writer.writerow((order, characteristic, tau, *row))
            sys.stdout.flush()


if __name__ == "__main__":
    main()
