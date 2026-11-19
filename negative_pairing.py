"""Compare the projected-iterate negative pairing with stationary-free bounds."""

import argparse
import csv
from math import isfinite, sqrt
import sys

import numpy as np

from iterate_majorants import averaged_targets, basic_witness
from poisson_weights import weighted_iterate
from smoothing import certify_spectrum, kernel_action
from square_control import square_field_sign
from theta import optimize, paley_sign


def capped_maximum(cost, mass, ceiling):
    """Maximize a linear cost over nonnegative weights with a common ceiling."""
    if mass <= 0:
        return 0.0
    whole = min(int(mass / ceiling), len(cost))
    if whole == len(cost):
        return ceiling * cost.sum()
    partition = np.partition(cost, len(cost) - whole - 1)
    threshold = partition[len(cost) - whole - 1]
    top_sum = partition[len(cost) - whole:].sum()
    return ceiling * top_sum + (mass - whole * ceiling) * threshold


def repair_negative(sign, side, negative, forbidden):
    """Construct a nonnegative sector majorant of the negative part."""
    n = len(sign)
    height, transform = basic_witness(sign, side)
    split = n - 1 - int(height)
    best_mean = float("inf")
    best = None
    for alpha in (0., .5, 1., 1.5, 2.):
        offset = alpha * forbidden
        cost = negative - offset
        threshold = np.partition(cost, split)[split]
        remaining = np.maximum(cost - threshold, 0)
        estimate = threshold + remaining.sum() / height
        if estimate < best_mean:
            translates = np.fft.irfft(transform * np.fft.rfft(remaining), n) / height
            best = threshold + translates + offset
            best_mean = estimate
    return best, best_mean


def comparison_rows(sign, tau, depths, solve_lp, certify):
    n = len(sign)
    weights = np.full(n, tau / n)
    weights[0] = 1
    mass = sqrt(n * weights.sum())
    scale = mass / n
    ceiling = scale * (sqrt(2 * n + 1) + 1)
    stationary = {}
    residual = None
    if tau > 0:
        v, u, residual = weighted_iterate(sign, weights, tolerance=1e-10)
        if residual > 1e-8:
            raise RuntimeError(f"stationary solve did not converge at order {2 * n + 1}, floor {tau}")
        large = (u + abs(v)) / 2
        small = weights / large
        stationary = {side: np.where(side * v >= 0, large, small) for side in (-1, 1)}

    for depth, z, activation_sum, z_sum in averaged_targets(sign, tau, depths):
        for side in (-1, 1):
            average = (activation_sum + side * z_sum) / (2 * depth)
            trial = average + side * z / depth
            negative = np.maximum(-trial, 0)
            negative[0] = 0
            forbidden = (negative + side * kernel_action(sign, negative) - negative.mean()) / 2
            raw_cap = capped_maximum(negative, mass, ceiling)
            adjusted_costs = [negative - alpha * forbidden for alpha in (0., .5, 1., 1.5, 2.)]
            projected_cap = min(capped_maximum(cost, mass, ceiling) for cost in adjusted_costs)
            lp = scale * (negative @ optimize(sign, -side, negative)[1]) if solve_lp else None
            stationary_mark = actual = fixed_mark_cap = cauchy = None
            if stationary:
                stationary_mark = stationary[side][0]
                b = stationary[-side]
                actual = negative @ b
                fixed_mark_cap = min(
                    cost[0] * b[0] + capped_maximum(cost[1:], mass - b[0], ceiling)
                    for cost in adjusted_costs
                )
                minimum_bound = min(projected_cap, fixed_mark_cap, lp if lp is not None else float("inf"))
                if actual > minimum_bound + 1e-8:
                    raise RuntimeError("stationary pairing exceeded its feasible-spectrum upper bound")
                cauchy = np.linalg.norm(negative) * np.linalg.norm(b[1:])
            repair, repair_mean = repair_negative(sign, side, negative, forbidden)
            repaired = trial + repair
            if np.min(repair - negative) < -1e-10:
                raise RuntimeError("negative-part repair failed")
            normalized_upper = certified_upper = None
            if repaired[0] > 0:
                normalized_upper = sqrt(n) * repaired.mean() / repaired[0]
                certified_upper = n / certify_spectrum(sign, side, repaired) if certify else None
            yield (
                depth, side, stationary_mark, trial[0], mass * trial.mean(),
                np.count_nonzero(negative) / n, actual, lp, raw_cap, projected_cap, fixed_mark_cap,
                cauchy, residual, mass * repair_mean, normalized_upper, certified_upper,
            )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primes", nargs="*", type=int)
    parser.add_argument("--square-characteristics", nargs="*", type=int, default=[])
    parser.add_argument("--tau", nargs="+", type=float, default=[.0005])
    parser.add_argument("--depths", nargs="+", type=int, default=[32, 128, 512])
    parser.add_argument("--lp-max-order", type=int, default=2500)
    parser.add_argument("--certify-max-order", type=int, default=0)
    args = parser.parse_args()
    cases = [(p, p, paley_sign) for p in args.primes]
    cases += [(p**2, p, square_field_sign) for p in args.square_characteristics]
    if not cases:
        parser.error("supply prime orders or square characteristics")
    if min(args.depths) < 1 or any(not isfinite(tau) or tau < 0 for tau in args.tau):
        parser.error("depths must be positive and floors nonnegative and finite")

    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow((
        "field_order", "characteristic", "tau", "depth", "trial_sign", "stationary_mark",
        "trial_mark", "cross_total", "negative_density", "actual", "lp", "raw_cap",
        "projected_cap", "fixed_mark_cap", "cauchy", "stationary_residual", "repair_bound",
        "normalized_upper", "certified_upper",
    ))
    for order, characteristic, make_sign in sorted(cases):
        sign = make_sign(characteristic)
        for tau in args.tau:
            rows = comparison_rows(sign, tau, args.depths, order <= args.lp_max_order, order <= args.certify_max_order)
            for row in rows:
                writer.writerow((order, characteristic, tau, *row))
            sys.stdout.flush()


if __name__ == "__main__":
    main()
