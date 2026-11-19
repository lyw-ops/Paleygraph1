"""Compare marked inverses after splitting the stationary diagonal by cosets."""

import argparse
import csv
from math import isfinite, isqrt, sqrt
import sys

import numpy as np
from scipy.sparse.linalg import minres

from poisson_weights import weighted_iterate
from sensitivity import linearized_operator
from smoothing import kernel_action
from square_control import square_field_sign
from theta import paley_sign


def maximum_mass_cover(probability, order, count, size_ratio):
    n = len(probability)
    max_size = int(size_ratio * n / sqrt(order))
    divisors = sorted({v for d in range(1, isqrt(n) + 1) if n % d == 0 for v in (d, n // d)})
    best = (0.0, 0, 0)
    offsets = np.empty(0, dtype=int)
    for size in divisors:
        if size > max_size:
            break
        modulus = n // size
        cosets = min(count, modulus, max_size // size)
        masses = probability.reshape(size, modulus).sum(axis=0)
        selected = np.argsort(-masses, kind="stable")[:cosets]
        value = (float(masses[selected].sum()), cosets, size)
        if value > best:
            best = value
            offsets = (selected[:, None] + modulus * np.arange(size)).ravel()
    return best, offsets


def solve_mark(sign, diagonal, rhs):
    operator = linearized_operator(sign, diagonal)
    solution, status = minres(operator, rhs, rtol=1e-12, maxiter=12000)
    error = rhs - operator @ solution
    residual = np.linalg.norm(error)
    if status != 0 or residual > 2e-8:
        raise RuntimeError(f"marked solve failed with status {status} and residual {residual}")
    entry = np.dot(rhs, solution) + np.dot(solution, error)
    error_bound = residual**2 / (1 - np.max(np.abs(diagonal)))
    return solution, entry, residual, error_bound


def compare(sign, order, tau, count, size_ratio):
    n = len(sign)
    weights = np.full(n, tau / n)
    weights[0] = 1
    vector, total, stationary_residual = weighted_iterate(sign, weights, tolerance=1e-10)
    large = (total + np.abs(vector)) / 2
    small = weights / large
    normalizer = sqrt(n * weights.sum())
    diagonal = vector / total
    diagonal[0] = 0
    rhs = np.full(n, -1 / n)
    rhs[0] += 1
    base = kernel_action(sign, rhs)
    full, full_entry, full_residual, full_bound = solve_mark(sign, diagonal, rhs)

    for side in (1, -1):
        probability = np.where(side * vector >= 0, large, small) / normalizer
        (mass, cosets, size), indices = maximum_mass_cover(probability, order, count, size_ratio)
        covered = np.zeros(n, dtype=bool)
        covered[indices] = True
        inside_diagonal = np.where(covered, diagonal, 0)
        outside_diagonal = diagonal - inside_diagonal
        inside, inside_entry, inside_residual, inside_bound = solve_mark(sign, inside_diagonal, rhs)
        outside, outside_entry, outside_residual, outside_bound = solve_mark(sign, outside_diagonal, rhs)
        interaction = full_entry - inside_entry - outside_entry + base[0]
        cross = np.dot(full * inside_diagonal, outside - base) + np.dot(full * outside_diagonal, inside - base)
        yield (
            side, cosets, size, mass, base[0], full_entry, inside_entry, outside_entry,
            interaction, abs(interaction - cross), stationary_residual,
            max(full_residual, inside_residual, outside_residual),
            max(full_bound, inside_bound, outside_bound),
        )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primes", type=int, nargs="*")
    parser.add_argument("--square-characteristics", type=int, nargs="*", default=[])
    parser.add_argument("--tau", type=float, nargs="+", default=[0.05, 0.01, 0.002])
    parser.add_argument("--cosets", type=int, default=7)
    parser.add_argument("--size-ratio", type=float, default=1.1)
    args = parser.parse_args()
    orders = [(p, p) for p in args.primes] + [(r * r, r) for r in args.square_characteristics]
    if not orders or args.cosets < 1 or any(not isfinite(x) or x <= 0 for x in (*args.tau, args.size_ratio)):
        parser.error("provide orders, positive floors, a positive coset count and a positive size ratio")
    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow((
        "q", "characteristic", "tau", "cover_side", "cosets", "coset_size", "cover_mass",
        "base_entry", "full_entry", "inside_entry", "outside_entry", "interaction",
        "identity_error", "stationary_residual", "max_inverse_residual", "max_residual_bound",
    ))
    for order, characteristic in sorted(orders):
        sign = paley_sign(order) if order == characteristic else square_field_sign(characteristic)
        for tau in args.tau:
            for row in compare(sign, order, tau, args.cosets, args.size_ratio):
                writer.writerow((order, characteristic, tau, *row))
            sys.stdout.flush()


if __name__ == "__main__":
    main()
