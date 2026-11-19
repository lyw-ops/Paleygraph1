"""Probe random sparse frequency weights with the FFT log certificate."""

import argparse
import csv
from math import isfinite
import sys

import numpy as np
from scipy.sparse.linalg import minres

from rank_partitions import sample_weights
from sensitivity import linearized_operator
from smoothing import kernel_action
from square_control import square_field_sign
from theta import paley_sign


def weighted_iterate(sign, weights, tolerance=1e-9, rounds=32, damping=1, initial=None):
    """Run safeguarded Newton steps on the mean-zero smoothing equation."""
    root_weights = 2 * np.sqrt(weights)
    vector = damping * kernel_action(sign, root_weights) if initial is None else initial.copy()
    for _ in range(rounds):
        for _ in range(32):
            total = np.hypot(vector, root_weights)
            residual = damping * kernel_action(sign, total) - vector
            norm = np.linalg.norm(residual)
            if norm <= tolerance:
                return vector, total, norm
            vector = vector + residual

        total = np.hypot(vector, root_weights)
        residual = damping * kernel_action(sign, total) - vector
        norm = np.linalg.norm(residual)
        if norm <= tolerance:
            return vector, total, norm

        derivative = np.divide(vector, total, out=np.zeros_like(vector), where=total > 0)
        operator = linearized_operator(sign, damping * derivative)
        direction, status = minres(operator, kernel_action(sign, residual), rtol=1e-7, maxiter=256)
        if status < 0:
            raise RuntimeError(f"MINRES failed with status {status}")
        direction -= direction.mean()
        for step in 2.0 ** -np.arange(10):
            proposed = vector + step * direction
            proposed_residual = damping * kernel_action(sign, np.hypot(proposed, root_weights)) - proposed
            if np.linalg.norm(proposed_residual) < (1 - 0.1 * step) * norm:
                vector = proposed
                break

    total = np.hypot(vector, root_weights)
    residual = np.linalg.norm(damping * kernel_action(sign, total) - vector)
    return vector, total, residual


def projected_spectrum(sign, side, spectrum):
    coefficients = np.fft.rfft(spectrum)
    coefficients[1:] *= sign[1:len(coefficients)] == side
    projected = np.fft.irfft(coefficients, len(sign))
    positive_floor = np.finfo(float).eps * max(1, np.max(projected))
    projected += max(0, positive_floor - np.min(projected))
    return projected / projected.mean()


def log_bounds(sign, weights, floor_mass):
    """Return the signed log interval from a pair of projected spectra."""
    floored = weights + floor_mass / len(sign)
    vector, total, residual = weighted_iterate(sign, floored)
    larger = (total + np.abs(vector)) / 2
    smaller = floored / larger
    plus = projected_spectrum(sign, 1, np.where(vector >= 0, larger, smaller))
    minus = projected_spectrum(sign, -1, np.where(vector >= 0, smaller, larger))

    support = weights > 0
    mass = weights[support]
    entropy = mass @ np.log(len(sign) * mass)
    lower = 2 * (mass @ np.log(plus[support])) - entropy
    upper = entropy - 2 * (mass @ np.log(minus[support]))
    if upper < lower - 1e-10:
        raise RuntimeError("the complementary log interval is inverted")
    return lower, upper, residual


def probe(sign, counts, samples, law, floor_mass, seed):
    rng = np.random.default_rng(seed)
    for count in counts:
        repeats = 1 if law == "fixed" and count == 1 else samples
        intervals = []
        residuals = []
        actual_counts = []
        for _ in range(repeats):
            actual = count if law == "fixed" else 1 + rng.poisson(count)
            weights = sample_weights(len(sign), actual, rng)
            lower, upper, residual = log_bounds(sign, weights, floor_mass)
            intervals.append((lower, upper))
            residuals.append(residual)
            actual_counts.append(actual)

        array = np.array(intervals)
        lower, upper = array.mean(axis=0)
        midpoints = array.mean(axis=1)
        standard_error = np.std(midpoints, ddof=1) / np.sqrt(repeats) if repeats > 1 else 0.0
        yield (
            count, repeats, np.mean(actual_counts), lower, upper, standard_error,
            np.max(array[:, 1] - array[:, 0]), max(residuals),
        )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primes", type=int, nargs="*")
    parser.add_argument("--square-characteristics", type=int, nargs="*", default=[])
    parser.add_argument("--counts", type=int, nargs="+", default=[1, 2, 4, 8, 16, 32, 128, 512])
    parser.add_argument("--samples", type=int, default=24)
    parser.add_argument("--floor", type=float, default=0.001)
    parser.add_argument("--seed", type=int, default=26)
    parser.add_argument("--law", choices=("fixed", "size-biased-poisson"), default="fixed")
    args = parser.parse_args()
    orders = [(p, p) for p in args.primes] + [(r * r, r) for r in args.square_characteristics]
    if (not orders or args.samples < 2 or min(args.counts) < 1
            or not isfinite(args.floor) or args.floor <= 0):
        parser.error("provide field orders, positive counts and floor, and at least two samples")

    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow((
        "q", "characteristic", "n", "law", "floor_mass", "count", "samples", "actual_count_mean",
        "signed_lower_mean", "signed_upper_mean", "midpoint_standard_error", "max_interval_width",
        "max_stationary_residual",
    ))
    for order, characteristic in sorted(orders):
        sign = paley_sign(order) if order == characteristic else square_field_sign(characteristic)
        for row in probe(sign, args.counts, args.samples, args.law, args.floor, args.seed):
            writer.writerow((order, characteristic, len(sign), args.law, args.floor, *row))
            sys.stdout.flush()


if __name__ == "__main__":
    main()
