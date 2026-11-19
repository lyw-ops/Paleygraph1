"""Certify the finite cases in square-endpoint uniqueness by exact modular rank."""

import argparse
from math import gcd
from random import Random

from flint import fmpz, fmpz_poly, nmod_mat

from square_control import square_field_sign
from theta import prime_divisors


FINITE_CASES = (3, 5, 7, 11, 13, 17, 19, 41, 43, 89, 101, 109, 113, 137, 229, 349)


def saturated_frequencies(prime, sign):
    n = len(sign)
    frequencies = set(range(0, n, prime - 1))
    subfield_size = (prime + 1) // 2
    if prime % 4 == 3:
        frequencies.update(range(subfield_size, n, 2 * subfield_size))
    exceptional_orders = []
    if prime % 24 in (17, 19):
        exceptional_orders.append(24)
    if prime % 60 in (41, 49):
        exceptional_orders.append(60)
    possible_exceptions = {
        (2 * n // order) * exponent % n
        for order in exceptional_orders
        for exponent in range(1, order)
        if gcd(exponent, order) == 1
    }
    if possible_exceptions - frequencies:
        cyclotomic = fmpz_poly.cyclotomic(n)
        for frequency in possible_exceptions - frequencies:
            coefficients = [0] * n
            for j, value in enumerate(sign):
                coefficients[(j * frequency) % n] += int(value)
            if fmpz_poly(coefficients) % cyclotomic == prime:
                frequencies.add(frequency)
    return sorted(frequencies)


def certify(prime):
    sign = square_field_sign(prime)
    n = len(sign)
    frequencies = saturated_frequencies(prime, sign)
    auxiliary = n + 1
    while not fmpz(auxiliary).is_prime():
        auxiliary += n
    factors = prime_divisors(auxiliary - 1)
    generator = next(
        a for a in range(2, auxiliary)
        if all(pow(a, (auxiliary - 1) // factor, auxiliary) != 1 for factor in factors)
    )
    root = pow(generator, (auxiliary - 1) // n, auxiliary)
    powers = [pow(root, exponent, auxiliary) for exponent in range(n)]
    forbidden = [i for i, value in enumerate(sign) if value == -1]
    Random(26).shuffle(forbidden)
    rows = [[powers[i * k % n] for k in frequencies] for i in forbidden[:12 * len(frequencies)]]
    rank = nmod_mat(rows, auxiliary).rank()
    if rank != len(frequencies) - 1:
        raise RuntimeError(f"rank certificate did not reach one-dimensional kernel at {prime**2}")
    return prime, len(frequencies), rank, len(rows), auxiliary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("square_characteristics", nargs="*", type=int, default=FINITE_CASES)
    for prime in parser.parse_args().square_characteristics:
        print(*certify(prime))


if __name__ == "__main__":
    main()
