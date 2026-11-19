"""Separate the low dissipation modes in the averaged half-angle tail."""

import argparse
import csv
from math import isfinite, sqrt
import sys

import numpy as np
from scipy.sparse.linalg import LinearOperator, eigsh
from scipy.special import gammainc
from scipy.stats import poisson

from poisson_weights import weighted_iterate
from smoothing import kernel_action
from square_control import square_field_sign
from theta import paley_sign


def average_orbit(propagate, b, start, average):
    steps = int(poisson.isf(1e-14, 2 * start))
    powers = np.arange(steps + 1)
    low = gammainc(powers + 1, start)
    high = gammainc(powers + 1, 2 * start)
    if average == "tent":
        middle = gammainc(powers + 1, 1.5 * start)
        first_moment = (
            2 * gammainc(powers + 2, 1.5 * start)
            - gammainc(powers + 2, start)
            - gammainc(powers + 2, 2 * start)
        )
        coefficients = 4 / start**2 * (
            (powers + 1) * first_moment + start * (low + 2 * high - 3 * middle)
        )
    else:
        coefficients = (high - low) / start
    coefficients = np.stack((np.maximum(coefficients, 0), poisson.pmf(powers, start)))
    weighted = np.zeros((2, len(b)))
    iterate = b.copy()
    for step in range(steps + 1):
        weighted += coefficients[:, step, None] * iterate
        if step < steps:
            iterate = propagate(iterate)
    return weighted


def low_block(sign, multiplier, indices, direction, threshold):
    count = len(indices)
    if not count:
        return np.empty(0), np.empty((0, 0)), 0.0
    block_multiplier = multiplier[indices]

    def action(x):
        extended = np.zeros(len(sign))
        extended[indices] = block_multiplier * x
        return x - direction * block_multiplier * kernel_action(sign, extended)[indices]

    request = 4
    while request < count - 1:
        operator = LinearOperator((count, count), matvec=action, dtype=np.float64)
        initial = np.random.default_rng(26).standard_normal(count)
        values, vectors = eigsh(operator, k=request, which="SA", v0=initial, tol=1e-11)
        if np.max(values) > threshold:
            break
        request *= 2
    else:
        matrix = np.column_stack([action(x) for x in np.eye(count)])
        values, vectors = np.linalg.eigh(matrix)

    kept = values <= threshold
    values, vectors = values[kept], vectors[:, kept]
    residual = max(
        (np.linalg.norm(action(vector) - value * vector) for value, vector in zip(values, vectors.T)),
        default=0.0,
    )
    return values, vectors, residual


def compare(sign, tau, times, eta_scale, average):
    n = len(sign)
    weights = np.full(n, tau / n)
    weights[0] = 1
    v, u, residual = weighted_iterate(sign, weights, tolerance=1e-10)
    half = np.tanh(np.arcsinh(v / (2 * np.sqrt(weights))) / 2)
    half[0] = 0
    multiplier = np.sqrt(np.abs(half))
    direction = np.where(half < 0, -1, 1)
    start = direction * multiplier * np.fft.ifft(sign).real
    a = u[0] - 2 * np.sqrt(tau / n)
    h = direction * multiplier * v / a

    def propagate(x):
        return direction * multiplier * kernel_action(sign, multiplier * x)

    source_error = np.linalg.norm(h - propagate(h) - start)
    energy = h @ start
    if source_error > 1e-8 or energy <= 0:
        raise RuntimeError(f"invalid stationary source at dimension {n} and floor {tau}")
    blocks = []
    for side in (1, -1):
        indices = np.flatnonzero(direction == side)
        values, basis, eig_residual = low_block(
            sign, multiplier, indices, side, eta_scale / sqrt(min(times))
        )
        blocks.append((indices, values, basis, eig_residual))

    for time in times:
        eta = eta_scale / sqrt(time)
        averaged, early = average_orbit(propagate, start, time, average)
        tails = [averaged @ (direction * h)]
        counts = []
        for indices, values, basis, _ in blocks:
            kept = values <= eta
            counts.append(np.count_nonzero(kept))
            modes = basis[:, kept]
            tails.append((averaged[indices] @ modes) @ (h[indices] @ modes))
        high = tails[0] - (tails[1] - tails[2])
        dissipation = sqrt(max(averaged @ (averaged - propagate(averaged)), 0))
        bound = sqrt(energy) * min(dissipation / eta, np.linalg.norm(averaged) / sqrt(eta))
        eig_residual = max(block[-1] for block in blocks)
        if abs(high) > bound + 2e-8 or eig_residual > 1e-8:
            raise RuntimeError(f"low-mode test failed at dimension {n} and time {time}")
        yield (
            time, eta, v[0] / a, tails[0], *counts, tails[1], tails[2], high, bound,
            energy, np.linalg.norm(early), dissipation, source_error, eig_residual, residual,
        )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primes", nargs="*", type=int)
    parser.add_argument("--square-characteristics", nargs="+", type=int, default=[])
    parser.add_argument("--tau", nargs="+", type=float, default=[0.01, 0.0005])
    parser.add_argument("--times", nargs="+", type=int, default=[32, 128, 512])
    parser.add_argument("--eta-scale", type=float, default=0.15)
    parser.add_argument("--average", choices=("uniform", "tent"), default="tent")
    args = parser.parse_args()
    if min(args.times) < 4 or any(not isfinite(tau) or not 0 < tau <= 1 for tau in args.tau):
        parser.error("times must be at least four and floors must lie in (0,1]")
    if not isfinite(args.eta_scale) or not 0 < args.eta_scale <= 1:
        parser.error("eta scale must lie in (0,1]")
    orders = [(p, p) for p in args.primes] + [(r * r, r) for r in args.square_characteristics]
    if not orders:
        parser.error("provide prime orders or square characteristics")
    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow((
        "field_order", "characteristic", "tau", "average", "time", "eta", "half_mark", "signed_average_tail",
        "plus_low_rank", "minus_low_rank", "plus_low_pairing", "minus_low_pairing", "high_tail",
        "high_bound", "stationary_energy", "source_norm_at_time", "averaged_dissipation",
        "source_error", "eigen_residual", "stationary_residual",
    ))
    for order, characteristic in sorted(orders):
        sign = paley_sign(order) if order == characteristic else square_field_sign(characteristic)
        for tau in args.tau:
            for row in compare(sign, tau, args.times, args.eta_scale, args.average):
                writer.writerow((order, characteristic, tau, args.average, *row))
            sys.stdout.flush()


if __name__ == "__main__":
    main()
