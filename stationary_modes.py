"""Probe the coupling of a near-zero direction to the stationary Paley iterate."""

import argparse
import csv
from math import isfinite, sqrt
import sys

import numpy as np
from scipy.sparse.linalg import minres

from sensitivity import marked_system
from smoothing import smoothing
from square_control import square_field_sign
from theta import paley_sign


def inverse_iteration(operator, rhs, iterations, tolerance, max_steps):
    direction = rhs / np.linalg.norm(rhs)
    largest_residual = 0.0
    for _ in range(iterations):
        solved, status = minres(operator, direction, rtol=tolerance, maxiter=max_steps)
        if status != 0:
            raise RuntimeError(f"inverse iteration failed with MINRES status {status}")
        residual = np.linalg.norm(operator @ solved - direction)
        largest_residual = max(largest_residual, residual)
        solved -= solved.mean()
        direction = solved / np.linalg.norm(solved)
    return direction, largest_residual


def probe(sign, tau, threshold, tolerance, max_steps, iterations):
    n = len(sign)
    fixed_point, metrics = smoothing(sign, tau, tolerance, max_steps)
    operator, rhs, total, _ = marked_system(sign, tau, fixed_point)
    direction, inverse_residual = inverse_iteration(operator, rhs, iterations, tolerance / 10, max_steps)
    image = operator @ direction
    width = np.linalg.norm(image)
    rayleigh = np.dot(direction, image)
    eigen_residual = np.linalg.norm(image - rayleigh * direction)
    band_width = 2 * width
    marked_lower = max(0.0, abs(direction[0]) - eigen_residual / (band_width - abs(rayleigh)))

    support = sqrt(n) * np.abs(fixed_point) > threshold
    support[0] = False
    return (
        np.arcsinh(fixed_point[0] / 2), np.count_nonzero(support),
        np.sum(np.abs(fixed_point[support])) / sqrt(n),
        np.dot(direction[support], direction[support]),
        width, sqrt(2 * n + 1) * width, rayleigh, eigen_residual,
        direction[0] ** 2 / width, marked_lower ** 2 / band_width, tau * total[0] ** 2 / 2,
        metrics[-2], inverse_residual,
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primes", nargs="*", type=int)
    parser.add_argument("--square-characteristics", nargs="*", type=int, default=[])
    parser.add_argument("--tau", nargs="+", type=float, default=[0.05, 0.5])
    parser.add_argument("--threshold", type=float, default=12.0)
    parser.add_argument("--tolerance", type=float, default=1e-9)
    parser.add_argument("--max-steps", type=int, default=10000)
    parser.add_argument("--inverse-steps", type=int, default=5)
    args = parser.parse_args()
    if not args.primes and not args.square_characteristics:
        parser.error("provide at least one prime or square characteristic")
    if any(not isfinite(value) or value <= 0 for value in [*args.tau, args.threshold, args.tolerance]):
        parser.error("tau, threshold and tolerance must be positive and finite")
    if args.max_steps < 3 or args.inverse_steps < 1:
        parser.error("max-steps must be at least 3 and inverse-steps must be positive")

    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow((
        "field_order", "characteristic", "tau", "bulk_scaled_abs_threshold",
        "log_marked_mass", "support_size", "stationary_l1_on_support_over_sqrt_n",
        "direction_energy_share_on_support", "hy_norm", "hy_norm_times_sqrt_q",
        "rayleigh_value", "direction_eigen_residual_l2", "marked_coordinate_squared_over_hy_norm",
        "band_mass_over_width_lower_at_2hy_norm", "stationary_mass_bound_ratio_threshold",
        "smoothing_residual_l2", "max_inverse_residual_l2",
    ))
    orders = [(p, p) for p in args.primes] + [(r * r, r) for r in args.square_characteristics]
    for order, characteristic in sorted(orders):
        sign = paley_sign(characteristic) if order == characteristic else square_field_sign(characteristic)
        for tau in args.tau:
            result = probe(sign, tau, args.threshold, args.tolerance, args.max_steps, args.inverse_steps)
            writer.writerow((order, characteristic, tau, args.threshold, *result))


if __name__ == "__main__":
    main()
