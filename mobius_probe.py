"""Count overlaps of subgroups under the Möbius map on square roots."""

import argparse
from collections import Counter
import csv
from math import isqrt, sqrt
import sys

from theta import prime_divisors, prime_field_generator


def mobius_square(t, prime):
    image = (1 - t) * pow(1 + t, -1, prime) % prime
    return image * image % prime


def prime_overlaps(prime):
    generator = prime_field_generator(prime)
    n = (prime - 1) // 2
    factors = prime_divisors(n)
    scale = isqrt(prime)
    orders = [b for b in range(max(1, scale // 2), 2 * scale + 1) if n % b == 0]
    for b in orders:
        # Exponents 0 through b-1 select one representative of each square root pair.
        step = pow(generator, n // b, prime)
        image_orders = Counter({1: 1})  # The identity orbit is fixed separately.
        for exponent in range(1, b):
            t = pow(step, exponent, prime)
            image = mobius_square(t, prime)
            order = n
            for divisor in factors:
                while order % divisor == 0 and pow(image, order // divisor, prime) == 1:
                    order //= divisor
            image_orders[order] += 1
        for d in orders:
            count = sum(number for order, number in image_orders.items() if d % order == 0)
            yield b, d, count


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primes", nargs="*", type=int)
    parser.add_argument("--square-characteristics", nargs="*", type=int, default=[])
    args = parser.parse_args()
    if not args.primes and not args.square_characteristics:
        parser.error("provide at least one prime or square characteristic")

    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow([
        "field_order", "characteristic", "input_subgroup_order", "output_subgroup_order",
        "intersection", "normalized_overlap", "method",
    ])
    fields = [(p, p) for p in args.primes] + [(p * p, p) for p in args.square_characteristics]
    for order, prime in sorted(fields):
        if order == prime:
            for b, d, count in prime_overlaps(prime):
                writer.writerow((order, prime, b, d, count, count / sqrt(b * d), "enumeration"))
        else:
            if prime < 3 or prime % 2 == 0 or any(
                prime % divisor == 0 for divisor in range(3, isqrt(prime) + 1, 2)
            ):
                raise ValueError(f"expected an odd prime, got {prime}")
            b = prime - 1
            for d in (b // 2, (prime + 1) // 2):
                writer.writerow((order, prime, b, d, d, sqrt(d / b), "subfield identity"))


if __name__ == "__main__":
    main()
