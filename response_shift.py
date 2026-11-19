"""Replay the marked response for a prescribed, nearly saturated frequency set."""

import argparse
import csv
from math import ceil, isqrt, sqrt
import sys

import numpy as np

from square_control import square_field_sign
from theta import paley_sign


def marked_entry(sign, support, diagonal):
    """Compute the marked entry using only the compression and marked column."""
    n = len(sign)
    kernel = np.fft.fft(sign).real / n
    differences = (support[:, None] - support[None, :]) % n
    block = kernel[differences]
    column = kernel[support]
    shifted_column = np.linalg.solve(np.eye(len(support)) - diagonal * block, column)
    return kernel[0] + diagonal * np.dot(column, shifted_column)


def coset_supports(n, position_order):
    annihilator = np.arange(0, n, position_order)
    opposite_shifts = np.unique(np.concatenate((annihilator + 1, annihilator + position_order - 1)))
    return (
        ("annihilator_without_mark", annihilator[1:]),
        ("half_shift_coset", annihilator + position_order // 2),
        ("opposite_shift_cosets", opposite_shifts),
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primes", nargs="*", type=int)
    parser.add_argument("--square-characteristics", nargs="*", type=int, default=[])
    parser.add_argument("--compare-cosets", action="store_true", help="compare the annihilator and two translations")
    args = parser.parse_args()
    if not args.primes and not args.square_characteristics:
        parser.error("provide at least one prime or square characteristic")

    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow(("field_order", "characteristic", "support", "support_size", "diagonal", "marked_entry"))
    orders = [(p, p) for p in args.primes] + [(r * r, r) for r in args.square_characteristics]
    for order, characteristic in sorted(orders):
        square = order != characteristic
        sign = square_field_sign(characteristic) if square else paley_sign(characteristic)
        n = len(sign)
        diagonal = 1 - 1 / order
        if args.compare_cosets:
            if square:
                position_order = characteristic - 1
            else:
                scale = sqrt(order)
                divisors = (b for b in range(2, 2 * isqrt(order) + 1, 2) if n % b == 0)
                position_order = min(divisors, key=lambda b: abs(b - scale))
                if position_order < scale / 2:
                    parser.error(f"no even divisor in the critical size range for {order}")
            for kind, support in coset_supports(n, position_order):
                writer.writerow((order, characteristic, kind, len(support), diagonal, marked_entry(sign, support, diagonal)))
            continue
        size = ceil(n / sqrt(order)) - 1
        if square:
            support = np.arange(1, size + 1) * (characteristic - 1)
            kind = "subfield_annihilator_without_mark"
        else:
            left = size // 2
            support = np.r_[np.arange(-left, 0), np.arange(1, size - left + 1)] % n
            kind = "centered_interval_without_mark"
        writer.writerow((order, characteristic, kind, size, diagonal, marked_entry(sign, support, diagonal)))


if __name__ == "__main__":
    main()
