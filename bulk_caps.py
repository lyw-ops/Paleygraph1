"""Compare capped stationary Fourier mass with fixed-depth smoothing."""

import argparse
import csv
from math import isfinite, sqrt
import sys

import numpy as np

from smoothing import kernel_action, smoothing
from square_control import square_field_sign
from theta import paley_sign


def cap_statistics(sign, vector, tau, cap):
    n = len(sign)
    bulk = sqrt(n) * vector[1:]
    total = np.hypot(bulk, 2 * sqrt(tau))
    larger = (total + np.abs(bulk)) / 2
    plus = np.where(bulk >= 0, larger, tau / larger)
    minus = np.where(bulk >= 0, tau / larger, larger)
    capped_plus = np.minimum(plus, cap)
    capped_minus = np.minimum(minus, cap)
    capped_total = np.zeros(n)
    capped_total[1:] = capped_plus + capped_minus
    capped_feedback = kernel_action(sign, capped_total) / sqrt(n)
    plus_high = np.r_[False, plus > cap]
    minus_high = np.r_[False, minus > cap]
    plus_count = np.count_nonzero(plus_high)
    minus_count = np.count_nonzero(minus_high)
    difference_density = 0.0
    if plus_count and minus_count:
        counts_by_shift = np.fft.irfft(
            np.fft.rfft(plus_high) * np.fft.rfft(minus_high).conj(), n,
        )
        difference_density = np.count_nonzero(counts_by_shift > 0.5) / n
    return (
        np.sum(capped_total) / n,
        np.sum(capped_plus - capped_minus) / n,
        np.sum(plus - capped_plus) / n,
        np.sum(minus - capped_minus) / n,
        capped_feedback[0],
        np.max(np.abs(capped_feedback)),
        plus_count,
        minus_count,
        difference_density,
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primes", nargs="*", type=int)
    parser.add_argument("--square-characteristics", nargs="*", type=int, default=[])
    parser.add_argument("--tau", nargs="+", type=float, default=[0.05, 0.5])
    parser.add_argument("--caps", nargs="+", type=float, default=[2, 4, 8, 16])
    parser.add_argument("--depths", nargs="+", type=int, default=[4, 32])
    parser.add_argument("--max-steps", type=int, default=20000)
    parser.add_argument("--tolerance", type=float, default=1e-10)
    args = parser.parse_args()
    orders = [(p, "prime", paley_sign) for p in args.primes]
    orders += [(p, "square", square_field_sign) for p in args.square_characteristics]
    if not orders:
        parser.error("supply prime orders or square characteristics")
    if any(not isfinite(x) or x <= 0 for x in [*args.tau, *args.caps, args.tolerance]):
        parser.error("tau, caps and tolerance must be positive and finite")
    if min(args.caps) <= sqrt(max(args.tau)):
        parser.error("every cap must exceed sqrt(tau)")
    if min(args.depths) < 2 or args.max_steps < 3:
        parser.error("depths must be at least 2 and max-steps at least 3")

    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow([
        "q", "field", "tau", "iterate", "steps", "cap", "marker", "max_abs_v",
        "residual_l2", "capped_mass", "capped_imbalance", "plus_tail", "minus_tail",
        "capped_feedback_mark", "capped_feedback_sup", "plus_high_count", "minus_high_count",
        "difference_density",
    ])
    for characteristic, field, make_sign in orders:
        order = characteristic if field == "prime" else characteristic ** 2
        sign = make_sign(characteristic)
        for tau in args.tau:
            candidates = [("stationary", args.tolerance, args.max_steps)]
            candidates += [("picard", 0, depth + 1) for depth in args.depths]
            for label, tolerance, steps in candidates:
                vector, metrics = smoothing(sign, tau, tolerance, steps)
                residual, evaluations = metrics[-2:]
                for cap in args.caps:
                    writer.writerow((
                        order, field, tau, label, evaluations - 1, cap, vector[0],
                        np.max(np.abs(vector)), residual,
                        *cap_statistics(sign, vector, tau, cap),
                    ))


if __name__ == "__main__":
    main()
