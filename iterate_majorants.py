"""Build Fourier certificates from averaged iterates and translated witnesses."""

import argparse
import csv
from math import floor, isfinite, sqrt
import sys

import numpy as np

from smoothing import certify_spectrum, kernel_action
from square_control import square_field_sign
from theta import paley_sign


def basic_witness(sign, side):
    n = len(sign)
    row = (sign == side).astype(float) * (2 / (sqrt(2 * n + 1) + 1))
    row[0] = 1
    return row.sum(), n * row[:n // 2 + 1]


def repair_spectrum(sign, target, side, witness_mark, witness_transform):
    """Majorize target by a sum in its required complementary Fourier space."""
    n = len(sign)
    correction = (target - side * kernel_action(sign, target) - target.mean()) / 2
    threshold_index = max(0, n - 1 - floor(witness_mark))
    threshold = np.partition(correction, threshold_index)[threshold_index]
    excess = np.maximum(correction - threshold, 0)
    translates = np.fft.irfft(witness_transform * np.fft.rfft(excess), n) / witness_mark
    repaired = target - correction + threshold + translates
    mean_repair = threshold + excess.sum() / witness_mark
    return repaired, correction, mean_repair


def averaged_targets(sign, tau, depths):
    n = len(sign)
    weights = np.full(n, 4 * tau / n)
    weights[0] = 4
    z = np.zeros(n)
    sum_activation = np.zeros(n)
    sum_z = np.zeros(n)
    depths_set = set(depths)
    for depth in range(1, max(depths) + 1):
        activation = np.sqrt(z ** 2 + weights)
        sum_activation += activation
        sum_z += z
        z = (z + kernel_action(sign, activation)) / 2
        if depth in depths_set:
            yield depth, z, sum_activation, sum_z


def comparison_rows(sign, tau, depths, certify):
    n = len(sign)
    root_n = sqrt(n)
    scale = sqrt(1 + tau * (1 - 1 / n)) * root_n
    witnesses = {side: basic_witness(sign, side) for side in (-1, 1)}

    for depth, z, sum_activation, sum_z in averaged_targets(sign, tau, depths):
        kz = kernel_action(sign, z)
        for side in (-1, 1):
            target = (sum_activation + side * sum_z) / (2 * depth)
            witness_mark, witness_transform = witnesses[side]
            repaired, correction, mean_repair = repair_spectrum(
                sign, target, side, witness_mark, witness_transform,
            )
            raw = target - correction + correction.max()
            mark_level = correction[1:].max()
            mark_excess = max(0, correction[0] - mark_level)
            mark_repair = mark_excess / witness_mark
            mark_only_mark = target[0] - correction[0] + mark_level + mark_excess
            mark_only_mean = target.mean() + mark_level + mark_repair
            upper = n / certify_spectrum(sign, side, repaired) if certify else ""
            projection_error = np.max(np.abs(correction - (kz - side * z) / (2 * depth)))
            yield (
                depth, -side, scale * mean_repair, root_n * raw.mean() / raw[0],
                root_n * mark_only_mean / mark_only_mark, root_n * repaired.mean() / repaired[0],
                np.min(repaired - target), projection_error, upper,
            )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primes", nargs="*", type=int)
    parser.add_argument("--square-characteristics", nargs="*", type=int, default=[])
    parser.add_argument("--tau", nargs="+", type=float, default=[0.05, 0.005])
    parser.add_argument("--depths", nargs="+", type=int, default=[8, 32, 128, 512])
    parser.add_argument("--certify-max-order", type=int, default=0)
    args = parser.parse_args()
    orders = [(p, "prime", paley_sign) for p in args.primes]
    orders += [(p, "square", square_field_sign) for p in args.square_characteristics]
    if not orders:
        parser.error("supply prime orders or square characteristics")
    if any(not isfinite(tau) or tau <= 0 for tau in args.tau) or min(args.depths) < 1:
        parser.error("tau and depths must be positive and finite")

    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow([
        "q", "field", "tau", "depth", "side_bounded", "top_sum_drift_bound",
        "constant_normalized_upper", "mark_only_normalized_upper", "shifted_normalized_upper",
        "min_majorant_slack", "telescoping_error", "certified_upper",
    ])
    for characteristic, field, make_sign in orders:
        order = characteristic if field == "prime" else characteristic ** 2
        sign = make_sign(characteristic)
        for tau in args.tau:
            for row in comparison_rows(sign, tau, args.depths, order <= args.certify_max_order):
                writer.writerow((order, field, tau, *row))


if __name__ == "__main__":
    main()
