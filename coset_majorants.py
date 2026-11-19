"""Compare Fourier repairs that combine point and subgroup-coset witnesses."""

import argparse
import csv
from math import floor, isfinite, sqrt
import sys

import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix, csr_matrix, hstack

from iterate_majorants import averaged_targets, basic_witness, repair_spectrum
from smoothing import certify_spectrum
from square_control import square_field_sign
from theta import optimize, paley_sign


def subgroup_witness(sign, side):
    if np.all(sign[1:] == side):
        return float(len(sign)), np.full(len(sign) // 2 + 1, float(len(sign)))
    _, spectrum = optimize(sign, side)
    # Keep the permitted support and remove a possible numerical positivity defect.
    spectrum += max(0, -spectrum.min())
    spectrum /= spectrum.mean()
    return spectrum[0], np.fft.rfft(spectrum)


def repair_thresholds(correction, point_mark, coset_mark, subgroup_size):
    """Optimize the constant and the coset levels for the point repair."""
    ordered = np.sort(correction.reshape(-1, subgroup_size), axis=0)[::-1]
    coset_size = len(ordered)
    pieces = min(coset_size, point_mark / coset_mark)
    whole = floor(pieces)
    remainder = pieces - whole
    width = whole + int(remainder > 0)
    weights = np.ones((width, subgroup_size))
    if remainder > 0:
        weights[-1, :] = remainder
    values = ordered[:width].ravel()
    ranked = np.argsort(values)[::-1]
    cumulative = np.cumsum(weights.ravel()[ranked])
    index = min(len(ranked) - 1, np.searchsorted(cumulative, point_mark))
    baseline = values[ranked[index]]
    coset_heights = np.zeros(subgroup_size)
    if whole < coset_size:
        coset_heights = np.maximum(ordered[whole] - baseline, 0)
    return baseline, coset_heights


def combined_majorant(correction, point_witness, coset_witness, subgroup_size):
    n = len(correction)
    point_mark, point_transform = point_witness
    coset_mark, coset_transform = coset_witness
    baseline, heights = repair_thresholds(correction, point_mark, coset_mark, subgroup_size)
    excess = np.maximum(correction - baseline - np.tile(heights, n // subgroup_size), 0)
    point = np.fft.irfft(point_transform * np.fft.rfft(excess), n) / point_mark
    coset = np.fft.irfft(coset_transform * np.fft.rfft(heights), subgroup_size) / coset_mark
    majorant = baseline + point + np.tile(coset, n // subgroup_size)
    mean = baseline + excess.sum() / point_mark + heights.sum() / coset_mark
    return majorant, mean


def quotient_majorant(correction, point_witness, subgroup_sign, side):
    """Optimize the whole quotient spectrum before repairing individual entries."""
    n = len(correction)
    b = len(subgroup_sign)
    point_mark, point_transform = point_witness
    scale = sqrt(n)
    sorted_cost = np.sort((scale * correction).reshape(-1, b), axis=0)[::-1]
    rows = np.arange(n)
    block = rows % b
    prefix_length = 1 + rows // b
    # The sum of positive excess on a coset is the maximum over prefix sums.
    inequalities = coo_matrix((
        np.concatenate((-prefix_length, -np.ones(n))),
        (np.tile(rows, 2), np.concatenate((block, b + block))),
    ), shape=(n, 2 * b)).tocsr()
    offsets = np.flatnonzero(subgroup_sign[:b // 2 + 1] == -side)
    phases = (2 * np.pi / b) * np.outer(offsets, np.arange(b))
    cosines = np.cos(phases)
    sines = np.sin(phases[2 * offsets != b])
    mask = csr_matrix(np.concatenate((cosines, sines)))
    equalities = hstack((mask, csr_matrix(mask.shape)), format="csr")
    fit = linprog(
        np.r_[np.full(b, 1 / b), np.full(b, 1 / point_mark)],
        A_ub=inequalities,
        b_ub=-np.cumsum(sorted_cost, axis=0).ravel(),
        A_eq=equalities,
        b_eq=np.zeros(len(cosines) + len(sines)),
        bounds=[(None, None)] * b + [(0, None)] * b,
        method="highs",
    )
    if not fit.success:
        raise RuntimeError(fit.message)
    # Project back to the permitted support and average under inversion.
    profile_row = np.fft.ifft(fit.x[:b]).real / scale
    profile_row[subgroup_sign == -side] = 0
    lifted = np.tile(np.fft.fft(profile_row).real, n // b)
    excess = np.maximum(correction - lifted, 0)
    majorant = lifted + np.fft.irfft(point_transform * np.fft.rfft(excess), n) / point_mark
    return majorant, lifted.mean() + excess.sum() / point_mark


def comparison_rows(sign, subgroup_size, tau, depths, certify, solve_quotient):
    n = len(sign)
    subgroup_sign = sign[::n // subgroup_size]
    point_witnesses = {side: basic_witness(sign, side) for side in (-1, 1)}
    coset_witnesses = {side: subgroup_witness(subgroup_sign, side) for side in (-1, 1)}
    scale = sqrt(n * (1 + tau * (1 - 1 / n)))

    def comparison(depth, side, correction, point_mean, point_upper, target=None):
        point_witness = point_witnesses[side]
        coset_witness = coset_witnesses[side]
        majorant, mean = combined_majorant(correction, point_witness, coset_witness, subgroup_size)
        combined_mean = mean
        quotient_mean = ""
        if solve_quotient:
            profile_majorant, profile_mean = quotient_majorant(correction, point_witness, subgroup_sign, side)
            quotient_mean = scale * profile_mean
            if profile_mean < mean:
                majorant, mean = profile_majorant, profile_mean
        upper = certified = ""
        if target is not None:
            repaired = target - correction + majorant
            upper = sqrt(n) * repaired.mean() / repaired[0]
            if certify:
                certified = n / certify_spectrum(sign, side, repaired)
        return (
            depth, -side, coset_witness[0], point_mean, scale * combined_mean, quotient_mean,
            np.min(majorant - correction), point_upper, upper, certified,
        )

    # Compare a single coset plateau of height 1/sqrt(n), centered to have mean zero.
    plateau = ((np.arange(n) % subgroup_size == 0) - 1 / subgroup_size) / sqrt(n)
    for side in (-1, 1):
        h = point_witnesses[side][0]
        point_mean = scale * (min(1, (n // subgroup_size) / h) - 1 / subgroup_size) / sqrt(n)
        yield comparison(0, side, plateau, point_mean, "")

    for depth, _, sum_activation, sum_z in averaged_targets(sign, tau, depths):
        for side in (-1, 1):
            target = (sum_activation + side * sum_z) / (2 * depth)
            point, correction, point_mean = repair_spectrum(sign, target, side, *point_witnesses[side])
            point_upper = sqrt(n) * point.mean() / point[0]
            yield comparison(depth, side, correction, scale * point_mean, point_upper, target)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("prime_subgroups", nargs="*", metavar="P:B")
    parser.add_argument("--square-characteristics", nargs="*", type=int, default=[])
    parser.add_argument("--tau", type=float, default=0.05)
    parser.add_argument("--depths", nargs="+", type=int, default=[16, 64, 256, 512])
    parser.add_argument("--certify-max-order", type=int, default=0)
    parser.add_argument("--quotient-lp-max-order", type=int, default=0)
    args = parser.parse_args()
    if not isfinite(args.tau) or args.tau <= 0 or min(args.depths) < 1:
        parser.error("tau and depths must be positive and finite")
    try:
        orders = [(p, "prime", b, paley_sign(p)) for p, b in (
            tuple(map(int, pair.split(":"))) for pair in args.prime_subgroups
        )]
        orders += [(p * p, "square", p - 1, square_field_sign(p)) for p in args.square_characteristics]
    except ValueError as error:
        parser.error(str(error))
    if not orders:
        parser.error("supply prime orders with subgroup sizes or square characteristics")
    if any(b < 2 or len(sign) % b != 0 for _, _, b, sign in orders):
        parser.error("each subgroup size must be a divisor of (q-1)/2 and at least 2")

    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow([
        "q", "field", "subgroup_size", "tau", "depth", "side_bounded", "opposite_subgroup_mark",
        "point_drift_bound", "combined_drift_bound", "quotient_lp_drift_bound", "min_majorant_slack",
        "point_normalized_upper", "repaired_normalized_upper", "certified_upper",
    ])
    for order, field, b, sign in orders:
        for row in comparison_rows(
            sign, b, args.tau, args.depths, order <= args.certify_max_order, order <= args.quotient_lp_max_order,
        ):
            writer.writerow((order, field, b, args.tau, *row))


if __name__ == "__main__":
    main()
