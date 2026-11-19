"""Compute and certify ordinary theta for both Paley localization supports."""

import argparse
import csv
from fractions import Fraction
from math import ceil, factorial, floor, isqrt, pi, sqrt
import sys

import numpy as np
from scipy.optimize import linprog


def prime_divisors(order):
    factors = set()
    remaining = order
    for divisor in range(2, isqrt(order) + 1):
        while remaining % divisor == 0:
            factors.add(divisor)
            remaining //= divisor
    if remaining > 1:
        factors.add(remaining)
    return factors


def prime_field_generator(prime):
    if prime < 5 or prime % 4 != 1 or any(
        prime % divisor == 0 for divisor in range(3, isqrt(prime) + 1, 2)
    ):
        raise ValueError(f"expected a prime congruent to 1 mod 4, got {prime}")

    order = prime - 1
    factors = prime_divisors(order)
    return next(
        candidate for candidate in range(2, prime)
        if all(pow(candidate, order // factor, prime) != 1 for factor in factors)
    )


def paley_sign(prime):
    # The square of a primitive root generates all nonzero squares.
    root = prime_field_generator(prime)
    character = np.full(prime, -1, dtype=np.int8)
    character[0] = 0
    character[[x * x % prime for x in range(1, prime // 2 + 1)]] = 1
    n = (prime - 1) // 2
    sign = np.array([character[(1 - pow(root, 2 * j, prime)) % prime] for j in range(n)])
    return sign


def optimize(sign, edge_sign, frequency_cost=None):
    """Maximize the marked mass or an even linear cost on the spectrum."""
    n = len(sign)
    frequencies = np.arange(1, n // 2 + 1)
    support = frequencies[sign[frequencies] == edge_sign]
    if len(support) == 0:
        row = np.zeros(n)
        row[0] = 1
        return row, np.ones(n)

    # Each variable contains all the mass in one inverse pair of offsets.
    cost = np.ones(len(support))
    if frequency_cost is not None:
        # An arbitrary cost need not favor a nonnegative marked mass.
        frequencies = np.r_[0, frequencies]
        cost = np.fft.fft(frequency_cost).real[support]
    phases = np.multiply.outer(frequencies, support) % n
    cosine = np.cos((2 * pi / n) * phases)
    result = linprog(
        -cost,
        A_ub=-cosine,
        b_ub=np.ones(len(frequencies)),
        bounds=(None, None),
        method="highs",
    )
    if not result.success:
        raise RuntimeError(result.message)
    row = np.zeros(n)
    row[0] = 1
    row[support] += result.x / 2
    row[-support] += result.x / 2
    return row, np.fft.fft(row).real


def cosine_intervals(n, scale):
    """Integer enclosures for scale*cos(2*pi*j/n), using rational arithmetic."""
    # Machin's identity and the next term of the alternating arctan series.
    terms = 24

    def arctan_sum(q):
        return sum(Fraction((-1) ** i, (2 * i + 1) * q ** (2 * i + 1)) for i in range(terms))

    pi_middle = 16 * arctan_sum(5) - 4 * arctan_sum(239)
    pi_error = Fraction(20, (2 * terms + 1) * 5 ** (2 * terms + 1))
    lower = [scale]
    upper = [scale]
    for j in range(1, n // 2 + 1):
        x = 2 * pi_middle * j / n
        approximation = sum((-1) ** i * x ** (2 * i) / factorial(2 * i) for i in range(terms))
        # The cosine tail decreases from term 24 onwards, and cosine is 1-Lipschitz.
        error = x ** (2 * terms) / factorial(2 * terms) + pi_error
        lower.append(max(-scale, floor(scale * (approximation - error))))
        upper.append(min(scale, ceil(scale * (approximation + error))))
    return lower, upper


def certify(sign, edge_sign, row, cosines, scale):
    """Round a candidate, repair its diagonal, and prove a rational lower bound."""
    n = len(sign)
    lower, upper = cosines
    weights = [(0, scale)]
    for j in range(1, n // 2 + 1):
        if sign[j] == edge_sign:
            pair_mass = row[j] if j == n - j else row[j] + row[n - j]
            weights.append((j, round(scale * float(pair_mass))))

    # f is real and even. The integer sum below bounds scale²*F(f)(k).
    min_bound = 0
    for k in range(1, n // 2 + 1):
        bound = 0
        for j, weight in weights:
            angle = (k * j) % n
            angle = min(angle, n - angle)
            enclosure = lower if weight >= 0 else upper
            bound += weight * enclosure[angle]
        # Python ints prevent overflow in these exact products.
        min_bound = min(min_bound, bound)
    extra = (-min_bound + scale - 1) // scale
    total = sum(weight for _, weight in weights) + extra
    # delta at 0 is a feasible fallback and also checks the trivial Fourier mode.
    return max(Fraction(1), Fraction(total, scale + extra))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primes", type=int, nargs="+")
    parser.add_argument("--certify", action="store_true", help="add exact rational intervals")
    args = parser.parse_args()

    writer = csv.writer(sys.stdout, lineterminator="\n")
    fields = ["p", "n", "theta_complement", "theta_local", "ratio_to_sqrt_n", "product_error"]
    if args.certify:
        fields += ["complement_lower", "complement_upper", "local_lower", "local_upper"]
    writer.writerow(fields)
    for prime in args.primes:
        sign = paley_sign(prime)
        n = len(sign)
        plus_row, plus_fourier = optimize(sign, 1)
        minus_row, minus_fourier = optimize(sign, -1)
        plus, minus = plus_fourier[0], minus_fourier[0]
        row = [prime, n, plus, minus, plus / sqrt(n), plus * minus - n]
        if args.certify:
            scale = 10**10
            cosines = cosine_intervals(n, scale)
            lo_plus = certify(sign, 1, plus_row, cosines, scale)
            lo_minus = certify(sign, -1, minus_row, cosines, scale)
            row.extend((lo_plus, n / lo_minus, lo_minus, n / lo_plus))
        writer.writerow(row)


if __name__ == "__main__":
    main()
