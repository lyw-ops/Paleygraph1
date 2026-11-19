"""Compute the diagonal of the two-frequency projected Fourier polytopes."""

import argparse
import csv
import sys

import numpy as np
from scipy.optimize import linprog

from square_control import square_field_sign
from theta import optimize, paley_sign


def centered_lp(sign, side, parity):
    """Build the reflection-invariant constraints for an integer or half-integer center."""
    n = len(sign)
    modes = np.arange(1, n // 2 + 1 - parity)
    modes = modes[sign[modes] == side]
    representatives = np.arange(parity, n // 2 + 1) - parity / 2
    constraints = -np.cos((2 * np.pi / n) * np.multiply.outer(representatives, modes))
    constraints[np.abs(constraints) < 1e-12] = 0
    return modes, constraints


def common_height(n, shift, lp):
    """Maximize the common value of the two marks in the symmetric LP."""
    modes, constraints = lp
    if len(modes) == 0:
        return 1.0
    cost = np.cos((np.pi * shift / n) * modes)
    cost[np.abs(cost) < 1e-12] = 0
    # On a nonnegative spectrum of mean one, every Fourier coefficient has modulus at most one.
    options = dict(A_ub=constraints, b_ub=np.ones(len(constraints)), bounds=(-2, 2))
    result = linprog(-cost, **options, method="highs")
    if not result.success:
        result = linprog(-cost, **options, method="highs-ipm")
    if not result.success:
        raise RuntimeError(result.message)
    return 1 - result.fun


def shifts_to_test(n, count, rng, square_base):
    # Inversion identifies h with -h, each with multiplicity two except n/2.
    if count < n // 2:
        shifts = rng.integers(1, n, size=count)
        settings = [(min(h, n - h), "random", 1) for h in shifts]
    else:
        settings = [(h, "enumerated", 1 if 2 * h == n else 2) for h in range(1, n // 2 + 1)]
    if square_base is not None:
        settings.append((square_base - 1, "subfield-annihilator", 0))
        if square_base % 4 == 1:
            settings.append(((square_base + 1) // 2, "norm-one-annihilator", 0))
    return settings


def compare(sign, count, seed, square_base=None):
    n = len(sign)
    theta = [optimize(sign, side)[1][0] for side in (1, -1)]
    settings = shifts_to_test(n, count, np.random.default_rng(seed), square_base)
    programs = {(side, parity): centered_lp(sign, side, parity)
                for parity in {shift % 2 for shift, _, _ in settings} for side in (1, -1)}
    results = {}
    for shift, kind, multiplicity in settings:
        if shift not in results:
            results[shift] = [common_height(n, shift, programs[side, shift % 2]) / cap
                              for side, cap in zip((1, -1), theta)]
        plus, minus = results[shift]
        yield shift, kind, multiplicity, plus, minus, 1 / plus - 1.5, 1.5 - 2 * plus, abs(plus * minus - 0.5)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primes", type=int, nargs="*")
    parser.add_argument("--square-characteristics", type=int, nargs="*", default=[])
    parser.add_argument("--shifts", type=int, default=24)
    parser.add_argument("--seed", type=int, default=26)
    args = parser.parse_args()
    orders = [(p, p) for p in args.primes] + [(r * r, r) for r in args.square_characteristics]
    if not orders or args.shifts < 1:
        parser.error("provide field orders and a positive number of shifts")

    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow((
        "q", "characteristic", "n", "shift", "sample_kind", "multiplicity", "diagonal_plus",
        "diagonal_minus", "rank_term_lower", "rank_term_upper", "diagonal_polarity_error",
    ))
    for q, characteristic in sorted(orders):
        is_square = q != characteristic
        sign = square_field_sign(characteristic) if is_square else paley_sign(q)
        for row in compare(sign, args.shifts, args.seed, characteristic if is_square else None):
            writer.writerow((q, characteristic, len(sign), *row))
        sys.stdout.flush()


if __name__ == "__main__":
    main()
