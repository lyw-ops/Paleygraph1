"""Enumerate sign defects on self-inverse cosets at near-square prime orders."""

import argparse
import csv
import sys

from flint import fmpz

from theta import prime_field_generator


def sign_sum(prime, subgroup_order, step, representative):
    """Sum the quadratic sign over one multiplicative coset."""
    exponent = (prime - 1) // 2
    total = 0
    value = representative
    for _ in range(subgroup_order):
        sign = pow(1 - value, exponent, prime)
        total += -1 if sign == prime - 1 else sign
        value = value * step % prime
    return total


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("max_subgroup_order", type=int)
    parser.add_argument("--max-offset", type=int, default=8, help="bound on |j| in p=b²+jb+1")
    args = parser.parse_args()
    if args.max_subgroup_order < 2 or args.max_offset < 0:
        parser.error("need a subgroup order bound of at least two and a nonnegative offset bound")

    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow(("prime", "subgroup_order", "offset", "coset", "sign_sum", "deficit"))
    for b in range(2, args.max_subgroup_order + 1):
        for offset in range(-args.max_offset, args.max_offset + 1):
            prime = b * (b + offset) + 1
            if prime <= 1 or prime % 4 != 1 or (prime - 1) % (2 * b) != 0:
                continue
            if not fmpz(prime).is_prime():
                continue

            coset_count = (prime - 1) // (2 * b)
            generator = prime_field_generator(prime)
            step = pow(generator, 2 * coset_count, prime)
            identity = sign_sum(prime, b, step, 1)
            writer.writerow((prime, b, offset, "identity", identity, b - abs(identity)))
            if coset_count % 2 == 0:
                other = sign_sum(prime, b, step, pow(generator, coset_count, prime))
                writer.writerow((prime, b, offset, "other_self_inverse", other, b - abs(other)))


if __name__ == "__main__":
    main()
