"""Check the weighted transfer identities for sitewise diagonal changes."""

import argparse
import csv
from math import isfinite, sqrt
import sys

import numpy as np

from coset_activation_probe import maximum_mass_cover, solve_mark
from poisson_weights import weighted_iterate
from square_control import square_field_sign
from theta import paley_sign


def attenuation_cases(order, v, u, weights, diagonal):
    yield "strip", diagonal.copy(), np.empty(0, dtype=int)

    bulk_order = np.argsort(np.abs(v[1:]), kind="stable") + 1
    deletion_sets = [
        ("delete_low16", bulk_order[:16]),
        ("delete_high16", bulk_order[-16:]),
    ]
    large = (u + np.abs(v)) / 2
    small = weights / large
    normalizer = sqrt(len(v) * weights.sum())
    for side, label in ((1, "plus"), (-1, "minus")):
        probability = np.where(side * v >= 0, large, small) / normalizer
        _, cover = maximum_mass_cover(probability, order, 7, 1.1)
        deletion_sets.append((f"delete_{label}_cover", cover[cover != 0]))
    for label, deleted in deletion_sets:
        attenuated = diagonal.copy()
        attenuated[deleted] = 0
        yield label, attenuated, deleted

    alpha = 1 - 0.02 * np.abs(diagonal)
    yield "sitewise", alpha * diagonal, np.empty(0, dtype=int)


def compare(sign, order, tau):
    n = len(sign)
    weights = np.full(n, tau / n)
    weights[0] = 1
    v, u, stationary_residual = weighted_iterate(sign, weights, tolerance=1e-10)
    original_diagonal = v / u
    original_multiplier = 2 * np.sqrt(weights[1:]) / u[1:]
    stripped = original_diagonal.copy()
    stripped[0] = 0
    rhs = np.full(n, -1 / n)
    rhs[0] += 1
    total_weight = weights.sum()
    a = 4 * total_weight + v[0] ** 2

    for label, diagonal, deleted in attenuation_cases(order, v, u, weights, stripped):
        solution, entry, residual, _ = solve_mark(sign, diagonal, rhs)
        x = solution - solution.mean()
        mark = x[0]
        k = diagonal @ x / sqrt(n)
        delta = original_diagonal[1:] - diagonal[1:]
        complement = (1 - diagonal[1:]) * (1 + diagonal[1:])
        ell_squared = complement @ (x[1:] ** 2)
        beta = (delta * u[1:]) @ x[1:]
        q = (delta * u[1:]) ** 2 @ (1 / complement)
        r = (original_multiplier ** 2 / complement).sum() / n
        ell_bound = (u[0] * sqrt(q) + sqrt(u[0] ** 2 * q + 4 * a * (total_weight - 1))) / a
        mark_bound = (2 * sqrt(tau * r) + sqrt(q)) * ell_bound / u[0]

        norm_error = abs(mark**2 + ell_squared + (k + 1 / sqrt(n)) ** 2 - 1)
        square_error = abs(
            a / (4 * total_weight) * (mark - v[0] * (u[0] - beta) / a) ** 2
            + ell_squared - (4 * (total_weight - 1) + 2 * u[0] * beta - beta**2) / a
        )
        source_error = abs(
            u[0] * (original_diagonal[0] - mark)
            - (2 * sqrt(tau / n) * original_multiplier + delta * v[1:]) @ x[1:]
        )
        if max(norm_error, square_error, source_error) > 1e-7:
            raise RuntimeError(f"{label} failed to reproduce the identities at order {order}")
        if sqrt(ell_squared) > ell_bound + 1e-7 or abs(entry - original_diagonal[0]) > mark_bound + 1e-7:
            raise RuntimeError(f"{label} exceeded the predicted bound at order {order}")

        yield (
            label, len(deleted), np.linalg.norm(x[deleted]), original_diagonal[0], entry,
            q, r, beta, sqrt(ell_squared), ell_bound, mark_bound,
            norm_error, square_error, source_error, stationary_residual, residual,
        )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primes", nargs="*", type=int)
    parser.add_argument("--square-characteristics", nargs="+", type=int, default=[])
    parser.add_argument("--tau", nargs="+", type=float, default=[0.05, 0.01])
    args = parser.parse_args()
    orders = [(p, p) for p in args.primes] + [(r * r, r) for r in args.square_characteristics]
    if not orders or any(not isfinite(tau) or tau <= 0 for tau in args.tau):
        parser.error("provide field orders and positive finite floors")
    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow((
        "field_order", "characteristic", "tau", "case", "deleted_count", "deleted_column_l2",
        "stationary_mark", "inverse_mark", "q_energy", "r_ratio", "beta", "weighted_bulk_l2",
        "weighted_bulk_bound", "mark_error_bound", "norm_identity_error", "square_identity_error",
        "source_identity_error", "stationary_residual", "inverse_residual",
    ))
    for order, characteristic in sorted(orders):
        sign = paley_sign(order) if order == characteristic else square_field_sign(characteristic)
        for tau in args.tau:
            for row in compare(sign, order, tau):
                writer.writerow((order, characteristic, tau, *row))
            sys.stdout.flush()


if __name__ == "__main__":
    main()
