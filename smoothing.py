"""Probe the marked coordinate in complementary Fourier smoothing."""

import argparse
import csv
from fractions import Fraction
from math import isfinite, sqrt
import sys

import numpy as np

from theta import paley_sign


def kernel_action(sign, vector):
    """Apply the real circulant multiplier K to a real frequency vector."""
    n = len(sign)
    return np.fft.irfft(sign[:n // 2 + 1] * np.fft.rfft(vector), n)


def smoothing(sign, tau, tolerance, max_steps):
    n = len(sign)
    weights = np.full(n, 4 * tau / n)
    weights[0] = 4

    def feedback(vector):
        return kernel_action(sign, np.sqrt(vector ** 2 + weights))

    vector = np.zeros(n)
    early_markers = []
    for step in range(1, max_steps + 1):
        full = feedback(vector)
        residual = np.linalg.norm(full - vector)
        if step <= 3:
            early_markers.append(float(full[0]))
        if step >= 3 and residual <= tolerance:
            break
        if step < max_steps:
            vector = full

    # Use the iterate at which the reported residual was measured.
    marker = vector[0]
    mass = (sqrt(marker ** 2 + 4) + marker) / 2
    return vector, (*early_markers, marker, mass, residual, step)


def certify_spectrum(sign, side, mass):
    """Project and round an even spectrum, then certify the Fourier row."""
    from flint import acb, ctx

    ctx.prec = 96
    n = len(sign)
    scale = 10**12
    row = np.fft.irfft(mass[:n // 2 + 1], n)
    half = [scale] + [
        round(scale * float(row[j] / row[0])) if sign[j] == side else 0
        for j in range(1, n // 2 + 1)
    ]
    # By construction these integers are symmetric and vanish off the support.
    numerators = half + half[-2:0:-1]
    spectrum = acb.dft(numerators)
    min_lower = min(value.real.lower() for value in spectrum[1:n // 2 + 1])
    repair = max(0, -int(min_lower.floor().unique_fmpz()))
    # Add repair to the diagonal, then restore diagonal 1. Delta is a fallback.
    return max(Fraction(1), Fraction(sum(numerators) + repair, scale + repair))


def certify(sign, vector, tau):
    """Project and round both candidate rows, then validate with an interval DFT."""
    n = len(sign)
    weights = np.full(n, 4 * tau / n)
    weights[0] = 4
    total = np.sqrt(vector ** 2 + weights)
    plus = certify_spectrum(sign, 1, (total + vector) / 2)
    minus = certify_spectrum(sign, -1, (total - vector) / 2)
    return plus, n / minus, minus, n / plus


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primes", nargs="+", type=int)
    parser.add_argument("--tau", nargs="+", type=float, default=[0.2, 0.05, 0.01])
    parser.add_argument("--max-steps", type=int, default=2000)
    parser.add_argument("--tolerance", type=float, default=1e-8)
    parser.add_argument("--certify", action="store_true", help="bound both sides by interval DFT")
    parser.add_argument("--norms", action="store_true", help="report norms of the final numerical iterate")
    args = parser.parse_args()
    if any(not isfinite(value) or value <= 0 for value in [*args.tau, args.tolerance]):
        parser.error("tau and tolerance must be positive and finite")
    if args.max_steps < 3:
        parser.error("max-steps must be at least 3")

    writer = csv.writer(sys.stdout, lineterminator="\n")
    fields = [
        "p", "tau", "first_marker", "second_marker", "third_marker",
        "final_marker", "mass", "residual_l2", "steps",
    ]
    if args.certify:
        fields += ["complement_lower", "complement_upper", "local_lower", "local_upper"]
    if args.norms:
        fields += ["iterate_l2", "bulk_scaled_max_abs"]
    writer.writerow(fields)
    for prime in args.primes:
        # +1 on H's edges makes p_tau the witness for theta(complement of H).
        sign = paley_sign(prime)
        for tau in args.tau:
            vector, metrics = smoothing(sign, tau, args.tolerance, args.max_steps)
            bounds = certify(sign, vector, tau) if args.certify else ()
            norms = ()
            if args.norms:
                norms = (np.linalg.norm(vector), sqrt(len(sign)) * np.max(np.abs(vector[1:])))
            writer.writerow((prime, tau, *metrics, *bounds, *norms))


if __name__ == "__main__":
    main()
