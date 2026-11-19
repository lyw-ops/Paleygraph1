"""Replay the one-sided weighted bulk identities at a stationary pair."""

import argparse
import csv
from math import isfinite, sqrt
import sys

import numpy as np

from coset_activation_probe import solve_mark
from poisson_weights import weighted_iterate
from square_control import square_field_sign
from theta import paley_sign


def ordered_cases(diagonal, direction, v):
    positive = direction * diagonal > 0
    high = direction * v > 3.5 / sqrt(len(v))
    high[0] = False
    yield "delete_sign", np.where(positive, 0, diagonal), positive
    yield "delete_high", np.where(high, 0, diagonal), high
    clipped = direction * np.minimum(direction * diagonal, 0.8)
    yield "clip_sign", clipped, np.zeros(len(v), dtype=bool)
    shifted = np.tanh(np.arctanh(diagonal) - direction / 4)
    shifted[0] = 0
    yield "shift", shifted, np.zeros(len(v), dtype=bool)


def compare(sign, tau):
    n = len(sign)
    weights = np.full(n, tau / n)
    weights[0] = 1
    v, u, stationary_residual = weighted_iterate(sign, weights, tolerance=1e-10)
    diagonal = v / u
    diagonal[0] = 0
    rhs = np.full(n, -1 / n)
    rhs[0] += 1
    _, full_entry, full_residual, _ = solve_mark(sign, diagonal, rhs)
    weight_sum = weights.sum()
    epsilon = sqrt((weight_sum - 1) / weight_sum)

    for direction in (1, -1):
        opposite = (u - direction * v) / 2
        ratio = opposite[0] ** 2 / weight_sum
        baseline = 2 - (1 + ratio) * (1 + direction * full_entry)
        for label, exterior, deleted in ordered_cases(diagonal, direction, v):
            if np.max(direction * (exterior - diagonal)) > 1e-14:
                raise RuntimeError(f"{label} is not ordered in direction {direction}")
            solution, entry, residual, _ = solve_mark(sign, exterior, rhs)
            x = solution - solution.mean()
            mark = x[0]
            t = 1 + direction * mark
            g = direction * (full_entry - entry)
            if t <= 0 or g < -1e-8:
                raise RuntimeError(f"{label} failed monotonicity or the strict mark bound")
            complement = (1 - exterior[1:]) * (1 + exterior[1:])
            ell = sqrt(complement @ (x[1:] ** 2))
            y = ell / sqrt(t)
            kappa = (exterior @ x + 1) / sqrt(n)
            xi = direction / sqrt(weight_sum) * (
                (1 + direction * exterior[1:]) * opposite[1:]
            ) @ x[1:]
            source_error = abs(kappa - sqrt(ratio) * t - xi)
            norm_error = abs(mark**2 + ell**2 + kappa**2 - 1)
            law_error = abs(y - sqrt((1 + ratio) * max(g, 0)))
            law_bound = epsilon * (2 * sqrt(ratio * t) + epsilon * y) + sqrt(abs(baseline))
            if max(source_error, norm_error) > 2e-7 or law_error > law_bound + 2e-7:
                raise RuntimeError(f"{label} failed the weighted identities at dimension {n}")
            q_energy = (((diagonal[1:] - exterior[1:]) * u[1:]) ** 2 / complement).sum()
            yield (
                direction, label, len(deleted.nonzero()[0]), full_entry, entry, g, t,
                ell, np.linalg.norm(x[deleted]), y, law_error, law_bound, q_energy,
                source_error, norm_error, stationary_residual, max(full_residual, residual),
            )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primes", type=int, nargs="*")
    parser.add_argument("--square-characteristics", type=int, nargs="+", default=[])
    parser.add_argument("--tau", type=float, nargs="+", default=[0.05, 0.005, 0.0005])
    args = parser.parse_args()
    orders = [(p, p) for p in args.primes] + [(r * r, r) for r in args.square_characteristics]
    if not orders or any(not isfinite(tau) or not 0 < tau <= 1 for tau in args.tau):
        parser.error("provide field orders and finite floors in (0,1]")
    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow((
        "field_order", "characteristic", "tau", "direction", "case", "deleted_count",
        "full_mark", "exterior_mark", "signed_mark_loss", "distance_from_endpoint",
        "weighted_bulk_l2", "deleted_column_l2", "normalized_weighted_bulk_l2",
        "law_error", "law_bound", "q_energy", "source_identity_error", "norm_identity_error",
        "stationary_residual", "inverse_residual",
    ))
    for order, characteristic in sorted(orders):
        sign = paley_sign(order) if order == characteristic else square_field_sign(characteristic)
        for tau in args.tau:
            for row in compare(sign, tau):
                writer.writerow((order, characteristic, tau, *row))
            sys.stdout.flush()


if __name__ == "__main__":
    main()
