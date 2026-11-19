"""Check the two-label rank integral for small Paley localizations."""

import argparse
import csv
from itertools import batched, combinations
from math import log, sqrt
import sys

import numpy as np
from scipy.integrate import quad
from scipy.spatial import ConvexHull

from square_control import square_field_sign
from theta import optimize, paley_sign


TOLERANCE = 1e-8


def spectrum_basis(sign, edge_sign):
    """Give the full real mean-zero Fourier basis on one sign support."""
    n = len(sign)
    coordinate = 2 * np.pi * np.arange(n) / n
    columns = []
    for frequency in range(1, n // 2 + 1):
        if sign[frequency] != edge_sign:
            continue
        columns.append(np.cos(frequency * coordinate))
        if frequency * 2 != n:
            columns.append(np.sin(frequency * coordinate))
    return np.column_stack(columns) if columns else np.empty((n, 0))


def spectrum_vertices(sign, edge_sign):
    """Enumerate intersections of independent zero-coordinate constraints."""
    n = len(sign)
    basis = spectrum_basis(sign, edge_sign)
    dimension = basis.shape[1]
    if dimension == 0:
        return np.ones((1, n))

    vertices = []
    for indices in batched(combinations(range(n), dimension), 4096):
        equations = basis[np.asarray(indices)]
        independent = np.linalg.svd(equations, compute_uv=False)[:, -1] > TOLERANCE
        equations = equations[independent]
        if len(equations) == 0:
            continue
        solution = np.linalg.solve(equations, -np.ones((*equations.shape[:2], 1)))[:, :, 0]
        candidates = 1 + solution @ basis.T
        vertices.append(candidates[np.min(candidates, axis=1) >= -TOLERANCE])
    return np.unique(np.round(np.maximum(np.vstack(vertices), 0), 10), axis=0)


def pareto_edges(points):
    """Yield supporting edges whose two normal coordinates are positive."""
    dimension = np.linalg.matrix_rank(points - points[0], tol=TOLERANCE)
    if dimension == 0:
        return
    if dimension == 1:
        endpoints = points[[np.argmin(points[:, 0]), np.argmax(points[:, 0])]]
        difference = endpoints[1] - endpoints[0]
        normal = np.array([-difference[1], difference[0]])
        if min(normal) > TOLERANCE:
            yield endpoints, normal
        return

    hull = ConvexHull(points)
    for indices, equation in zip(hull.simplices, hull.equations):
        normal = equation[:2]
        if min(normal) > TOLERANCE:
            yield points[indices], normal


def edge_weight_intervals(points):
    """Weights selecting the relative interior of each positive-normal edge."""
    for endpoints, normal in pareto_edges(points):
        offset = endpoints[0] @ normal
        start, end = sorted(endpoints[:, 0] * normal[0] / offset)
        yield start, end, offset / normal[0], offset / normal[1]


def pair_statistics(vertices, shift):
    points = np.unique(vertices[:, [0, shift]], axis=0)
    positive_logs = np.log(points[np.min(points, axis=1) > 0])
    intervals = list(edge_weight_intervals(points))

    def objective(weight):
        for start, end, x_scale, y_scale in intervals:
            if start < weight < end:
                return weight * log(weight * x_scale) + (1 - weight) * log((1 - weight) * y_scale)
        return np.max(positive_logs @ [weight, 1 - weight])

    breaks = sorted({value for interval in intervals for value in interval[:2] if 0 < value < 1})
    integrated_objective = quad(objective, 0, 1, points=breaks, epsabs=1e-10)[0]
    rank_integral = sum(end - start for start, end, _, _ in intervals)
    return rank_integral, integrated_objective


def compare(sign):
    n = len(sign)
    vertices = [spectrum_vertices(sign, side) for side in (1, -1)]
    theta_plus, theta_minus = (optimize(sign, side)[1][0] for side in (1, -1))
    theta_difference = log(theta_plus / theta_minus)
    vertex_error = max(abs(np.max(points[:, 0]) - theta) for points, theta in zip(
        vertices, (theta_plus, theta_minus),
    ))

    first_term = 0.0
    a_2 = theta_difference / n  # Equal labels already select a vertex of the weight simplex.
    complementarity_error = 0.0
    for shift in range(1, n):
        (plus_rank, plus_objective), (minus_rank, minus_objective) = (
            pair_statistics(points, shift) for points in vertices
        )
        first_term += (plus_rank - minus_rank) / (2 * n)
        a_2 += (plus_objective - minus_objective) / n
        complementarity_error = max(complementarity_error, abs(plus_rank + minus_rank - 1))
    return (
        theta_plus / sqrt(n), theta_difference, first_term, a_2,
        abs(theta_difference - first_term - a_2), complementarity_error, vertex_error,
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primes", type=int, nargs="*")
    parser.add_argument("--square-characteristics", type=int, nargs="*", default=[])
    args = parser.parse_args()
    orders = [(prime, "prime", paley_sign) for prime in args.primes]
    orders += [(prime, "prime-square", square_field_sign) for prime in args.square_characteristics]
    if not orders:
        parser.error("provide prime orders or square characteristics")
    if any((prime if kind == "prime" else prime * prime) > 41 for prime, kind, _ in orders):
        parser.error("vertex enumeration is restricted to field orders at most 41")

    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow((
        "q", "kind", "n", "theta_over_sqrt_n", "twice_log_theta_ratio", "two_label_term",
        "a_2", "identity_error", "rank_complementarity_error", "theta_vertex_error",
    ))
    for prime, kind, field_sign in orders:
        sign = field_sign(prime)
        writer.writerow((2 * len(sign) + 1, kind, len(sign), *compare(sign)))


if __name__ == "__main__":
    main()
