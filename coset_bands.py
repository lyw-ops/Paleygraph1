"""Compare signed spectral gaps on unions of frequency cosets."""

import argparse
import csv
from math import isfinite, isqrt, sqrt
import sys

import numpy as np
from scipy.linalg import helmert

from sensitivity import marked_system
from smoothing import smoothing
from square_control import square_field_sign
from theta import paley_sign


def coset_union_blocks(sign, position_order, offsets):
    """Compress positional multiplication by the Paley sign on each coset."""
    n = len(sign)
    frequency_size = n // position_order
    count = len(offsets)
    positions = np.arange(n) / n
    blocks = np.empty((frequency_size, count, count), dtype=np.complex128)
    diagonal = sign.reshape(position_order, frequency_size).mean(axis=0)
    for i, left in enumerate(offsets):
        blocks[:, i, i] = diagonal
        for j, right in enumerate(offsets[:i]):
            twisted_sign = sign * np.exp(2j * np.pi * (left - right) * positions)
            sums = twisted_sign.reshape(position_order, frequency_size).mean(axis=0)
            blocks[:, i, j] = sums
            blocks[:, j, i] = sums.conj()
    return blocks, diagonal


def nearest_position_order(n, target, count):
    divisors = set()
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            divisors.update((d, n // d))
    return min(
        (b for b in divisors if b > count),
        key=lambda b: (abs(count * (n // b) - target), b),
    )


def dense_mean_zero_spectrum(sign, diagonal):
    n = len(sign)
    kernel = np.fft.fft(sign).real / n
    positions = np.arange(n)
    basis = helmert(n, full=False)
    circulant = kernel[(positions[:, None] - positions[None, :]) % n]
    return np.linalg.eigvalsh(basis @ (circulant - np.diag(diagonal)) @ basis.T)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primes", nargs="*", type=int)
    parser.add_argument("--square-characteristics", nargs="*", type=int, default=[])
    parser.add_argument("--cosets", nargs="+", type=int, default=[1, 2, 3])
    parser.add_argument("--tau", type=float, default=0.05)
    parser.add_argument("--tolerance", type=float, default=1e-9)
    parser.add_argument("--max-steps", type=int, default=10000)
    args = parser.parse_args()
    if not args.primes and not args.square_characteristics:
        parser.error("provide at least one prime or square characteristic")
    if any(not isfinite(value) or value <= 0 for value in (args.tau, args.tolerance)):
        parser.error("tau and tolerance must be positive and finite")
    if args.max_steps < 3 or min(args.cosets) < 1:
        parser.error("require at least three smoothing steps and positive coset counts")

    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow((
        "field_order", "characteristic", "tau", "cosets", "position_subgroup_order", "support_size",
        "support_size_minus_critical", "sign", "compression_endpoint", "endpoint_row_bound",
        "exterior_max_signed_diagonal", "band_gap_lower", "dense_band_gap", "smoothing_residual_l2",
    ))
    orders = [(p, p) for p in args.primes] + [(r * r, r) for r in args.square_characteristics]
    for order, characteristic in sorted(orders):
        sign = paley_sign(order) if order == characteristic else square_field_sign(characteristic)
        n = len(sign)
        if max(args.cosets) >= n:
            parser.error(f"coset count must be less than the number of frequencies for {order}")
        critical_size = n / sqrt(order)
        vector, metrics = smoothing(sign, args.tau, args.tolerance, args.max_steps)
        _, _, _, diagonal = marked_system(sign, args.tau, vector)
        dense = dense_mean_zero_spectrum(sign, diagonal) if n <= 256 else None
        for count in args.cosets:
            if order != characteristic and count == 1:
                b = characteristic - 1
            else:
                b = nearest_position_order(n, critical_size, count)
            offsets = np.arange(count)
            exterior = np.arange(n) % b >= count
            blocks, block_diagonal = coset_union_blocks(sign, b, offsets)
            eigenvalues = np.linalg.eigvalsh(blocks)
            size = n // b * count
            for side in (1, -1):
                rho = float(np.max(side * diagonal[exterior]))
                endpoint = float(np.max(side * eigenvalues))
                row_bound = (count - 1) * sqrt(order) / b + float(np.max(side * block_diagonal))
                gap_lower = (1 - rho) * (1 - endpoint) / 2
                gap = ""
                if dense is not None:
                    positive = side * dense[side * dense > 0]
                    if positive.size:
                        gap = float(np.min(positive))
                writer.writerow((
                    order, characteristic, args.tau, count, b, size, size - critical_size, side, endpoint,
                    row_bound, rho, gap_lower, gap, metrics[-2],
                ))


if __name__ == "__main__":
    main()
