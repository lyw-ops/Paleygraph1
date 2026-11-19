"""Enclose two-mark rank integrals using several linear Fourier LP costs."""

import argparse
import csv
import sys

import numpy as np
from scipy.optimize import linprog

from face_ranks import edge_weight_intervals, spectrum_basis
from square_control import square_field_sign
from theta import optimize, paley_sign
from two_mark_geometry import shifts_to_test


AXES = np.array([[0.0, 0.0], [1.0, 0.0], [0.0, 1.0]])
SQUARE = np.array([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0]])


def cut_polygon(points, direction, support):
    """Intersect an ordered polygon with one half-plane."""
    gaps = points @ direction - support
    clipped = []
    for i, point in enumerate(points):
        previous = i - 1
        if (gaps[previous] <= 0) != (gaps[i] <= 0):
            fraction = gaps[previous] / (gaps[previous] - gaps[i])
            clipped.append(points[previous] + fraction * (point - points[previous]))
        if gaps[i] <= 0:
            clipped.append(point)
    return np.asarray(clipped)


def support_oracle(basis, shift, direction, cap):
    rows = basis[[0, shift]]
    if basis.shape[1] == 0:
        return np.ones(2) / cap, 1 / cap
    cost = direction @ rows
    constraints = -basis
    options = dict(A_ub=constraints, b_ub=np.ones(len(basis)), bounds=(-2, 2))
    result = linprog(-cost, **options, method="highs")
    if not result.success:
        result = linprog(-cost, **options, method="highs-ipm")
    if not result.success:
        raise RuntimeError(result.message)

    spectrum = 1 + basis @ result.x
    repair = max(0.0, -np.min(spectrum))
    point = np.clip((spectrum[[0, shift]] + repair) / ((1 + repair) * cap), 0, 1)
    dual = np.maximum(-result.ineqlin.marginals, 0)
    dual_residual = cost - constraints.T @ dual
    # The last term bounds the residual cost on the coefficient box.
    upper = (1 + np.sum(dual) + 2 * np.sum(np.abs(dual_residual))) / cap
    return point, upper


def rank_integral(points):
    points = np.unique(np.round(points, 12), axis=0)
    return sum(end - start for start, end, _, _ in edge_weight_intervals(points))


def frontier_bounds(basis, shift, cap, divisions):
    inner = list(AXES)
    outer = SQUARE.copy()
    max_disk_discrepancy = 0.0
    max_support_error = 0.0
    for j in range((divisions + 1) // 2, divisions):
        direction = np.array([j, divisions - j]) / divisions
        point, upper = support_oracle(basis, shift, direction, cap)
        for coordinates, normal in ((point, direction), (point[::-1], direction[::-1])):
            inner.extend((coordinates, [coordinates[0], 0], [0, coordinates[1]]))
            outer = cut_polygon(outer, normal, upper + 1e-11)
        achieved = direction @ point
        max_support_error = max(max_support_error, upper - achieved)
        disk = np.linalg.norm(direction)
        max_disk_discrepancy = max(max_disk_discrepancy, abs(achieved - disk), abs(upper - disk))

    return (
        rank_integral(outer) - 0.5,
        rank_integral(np.asarray(inner)) - 0.5,
        max_disk_discrepancy,
        max_support_error,
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primes", type=int, nargs="*")
    parser.add_argument("--square-characteristics", type=int, nargs="*", default=[])
    parser.add_argument("--shifts", type=int, default=12)
    parser.add_argument("--divisions", type=int, default=16)
    parser.add_argument("--seed", type=int, default=26)
    args = parser.parse_args()
    orders = [(p, p) for p in args.primes] + [(r * r, r) for r in args.square_characteristics]
    if not orders or args.shifts < 1 or args.divisions < 2:
        parser.error("provide field orders, positive shift count, and at least two divisions")

    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow((
        "q", "characteristic", "n", "shift", "sample_kind", "multiplicity", "divisions",
        "rank_term_lower", "rank_term_upper", "sampled_disk_discrepancy", "max_support_gap",
    ))
    for q, characteristic in sorted(orders):
        square_base = characteristic if q != characteristic else None
        sign = square_field_sign(square_base) if square_base is not None else paley_sign(q)
        n = len(sign)
        cap = optimize(sign, 1)[1][0]
        basis = spectrum_basis(sign, 1)
        settings = shifts_to_test(n, args.shifts, np.random.default_rng(args.seed), square_base)
        measured = {}
        for shift, kind, multiplicity in settings:
            if shift not in measured:
                measured[shift] = frontier_bounds(basis, shift, cap, args.divisions)
            writer.writerow((q, characteristic, n, shift, kind, multiplicity, args.divisions, *measured[shift]))
            sys.stdout.flush()


if __name__ == "__main__":
    main()
