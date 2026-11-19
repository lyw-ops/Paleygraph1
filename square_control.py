"""Compare smoothing over prime and prime-square field orders."""

import argparse
import csv
from math import isfinite, isqrt, sqrt
import sys

import numpy as np

from smoothing import smoothing
from theta import paley_sign, prime_divisors


def square_field_sign(prime):
    """Return the Paley sign in cyclic order on the squares of F_(prime²)."""
    if prime < 3 or prime % 2 == 0 or any(
        prime % divisor == 0 for divisor in range(3, isqrt(prime) + 1, 2)
    ):
        raise ValueError(f"expected an odd prime, got {prime}")

    order = prime * prime - 1
    n = order // 2
    character = np.zeros(prime, dtype=np.int8)
    for value in range(1, prime):
        character[value] = 1 if pow(value, (prime - 1) // 2, prime) == 1 else -1
    nonsquare = int(np.flatnonzero(character == -1)[0])

    # Encode a + b*sqrt(nonsquare) by the pair (a, b).
    def multiply(left, right):
        a, b = left
        c, d = right
        return ((a * c + nonsquare * b * d) % prime, (a * d + b * c) % prime)

    def power(base, exponent):
        result = (1, 0)
        while exponent:
            if exponent % 2:
                result = multiply(result, base)
            base = multiply(base, base)
            exponent //= 2
        return result

    divisors = prime_divisors(order)
    generator = next(
        (a, b) for b in range(1, prime) for a in range(prime)
        if all(power((a, b), order // divisor) != (1, 0) for divisor in divisors)
    )
    square_generator = multiply(generator, generator)
    sign = np.empty(n, dtype=np.int8)
    element = (1, 0)
    for index in range(n):
        a, b = element
        norm_of_difference = ((1 - a) ** 2 - nonsquare * b ** 2) % prime
        sign[index] = character[norm_of_difference]
        element = multiply(element, square_generator)
    return sign


def translation_diagnostics(vector, tau):
    n = len(vector)
    bulk_weight = tau / n
    weights = np.full(n, bulk_weight)
    weights[0] = 1
    # Recover both spectra without cancellation at large entries of |vector|.
    larger = (np.hypot(vector, 2 * np.sqrt(weights)) + np.abs(vector)) / 2
    plus = np.where(vector >= 0, larger, weights / larger)
    minus = np.where(vector >= 0, weights / larger, larger)

    ratios = np.maximum(plus / plus[0], minus / minus[0])
    shift = 1 + np.argmax(ratios[1:])
    t = plus[shift] / plus[0]
    deficit = (1 - t) * (1 - bulk_weight / t)
    log_profile = np.log(plus / sqrt(bulk_weight))
    log_profile[0] = 0
    difference = log_profile - np.roll(log_profile, -shift)
    log_distance = np.linalg.norm(difference) / sqrt(n)
    difference[[0, n - shift]] = 0
    bulk_budget = 2 * bulk_weight * np.sum(np.sinh(difference / 2) ** 2)

    correlation = np.fft.irfft(np.fft.rfft(plus).conj() * np.fft.rfft(minus), n)
    correlation_error = np.max(np.abs(correlation - weights.sum()))

    # For a subgroup of size m, cosets are residue classes modulo n/m.
    cosets = []
    for size in range(1, isqrt(n) + 1):
        if n % size == 0:
            mass = plus.reshape(size, n // size).sum(axis=0).max()
            cosets.append((mass, size))
    coset_mass, coset_size = max(cosets)
    return (
        shift, ratios[shift], deficit, log_distance, abs(deficit - bulk_budget),
        correlation_error, coset_mass / plus.sum(), coset_size,
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("base_primes", nargs="+", type=int)
    parser.add_argument("--prime-orders", nargs="*", type=int, default=[])
    parser.add_argument("--tau", type=float, default=0.05)
    parser.add_argument("--tolerance", type=float, default=1e-8)
    parser.add_argument("--max-steps", type=int, default=20000)
    parser.add_argument("--translations", action="store_true", help="probe spectral shifts and subgroup cosets")
    args = parser.parse_args()
    if any(not isfinite(value) or value <= 0 for value in [args.tau, args.tolerance]):
        parser.error("tau and tolerance must be positive and finite")
    if args.max_steps < 3:
        parser.error("max-steps must be at least 3")

    writer = csv.writer(sys.stdout, lineterminator="\n")
    fields = [
        "characteristic", "field_order", "tau", "subfield_clique_over_sqrt_n",
        "marker_1", "marker_2", "marker_3", "last_marker", "mass", "residual_l2",
        "feedback_calls", "iterate_l2", "bulk_scaled_max_abs", "subfield_shell_l2",
    ]
    if args.translations:
        fields += [
            "extreme_shift", "largest_bulk_peak_ratio", "extreme_shift_deficit", "log_shift_l2",
            "shift_budget_error", "cross_correlation_error", "max_small_coset_plus_mass", "coset_size",
        ]
    writer.writerow(fields)
    cases = [(prime * prime, prime) for prime in args.base_primes]
    cases += [(prime, prime) for prime in args.prime_orders]
    for order, prime in sorted(cases):
        if order == prime:
            sign = paley_sign(prime)
            clique_ratio = ""
        else:
            sign = square_field_sign(prime)
            clique_ratio = (prime - 1) / sqrt(len(sign))
        vector, metrics = smoothing(sign, args.tau, args.tolerance, args.max_steps)
        shell_norm = np.linalg.norm(vector[prime - 1::prime - 1]) if order != prime else ""
        diagnostics = translation_diagnostics(vector, args.tau) if args.translations else ()
        writer.writerow((
            prime, order, args.tau, clique_ratio, *metrics,
            np.linalg.norm(vector), sqrt(len(sign)) * np.max(np.abs(vector[1:])), shell_norm, *diagnostics,
        ))


if __name__ == "__main__":
    main()
