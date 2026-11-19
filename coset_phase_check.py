"""Check difference cliques for cyclic sums of equally weighted characters."""

import argparse
from collections import Counter
from functools import cache
from itertools import combinations
from math import gcd
from random import Random

from flint import fmpz_poly


@cache
def cyclotomic_divisors(order):
    return [(d, fmpz_poly.cyclotomic(d)) for d in range(2, order + 1) if order % d == 0]


def zero_orders(order, exponents):
    coefficients = [0] * (max(exponents) + 1)
    for exponent in exponents:
        coefficients[exponent] = 1
    mask = fmpz_poly(coefficients)
    return tuple(d for d, poly in cyclotomic_divisors(order) if not mask % poly)


@cache
def has_difference_clique(order, forbidden, size):
    if not forbidden:
        return True
    allowed = [h for h in range(1, order) if order // gcd(order, h) not in forbidden]
    adjacency = [sum(1 << ((i + h) % order) for h in allowed) for i in range(order)]

    def search(candidates, remaining):
        if remaining == 0:
            return True
        while candidates.bit_count() >= remaining:
            vertex = candidates & -candidates
            candidates ^= vertex
            if search(candidates & adjacency[vertex.bit_length() - 1], remaining - 1):
                return True
        return False

    # The graph is invariant under translation, so a clique may contain zero.
    return search(adjacency[0], size - 1)


def scan(ranks, orders, samples):
    rng = Random(26)
    for rank in ranks:
        counts = Counter()
        for order in orders:
            if order < rank:
                continue
            choices = range(1, order)
            if samples is None:
                patterns = combinations(choices, rank - 1)
            else:
                patterns = (tuple(rng.sample(choices, rank - 1)) for _ in range(samples))
            target = (order + rank - 1) // rank
            for other_exponents in patterns:
                exponents = (0, *other_exponents)
                forbidden = zero_orders(order, exponents)
                counts["tested"] += 1
                counts["nontrivial"] += bool(forbidden)
                if not has_difference_clique(order, forbidden, target):
                    counts["misses"] += 1
                    if counts["misses"] == 1:
                        print(f"first miss: rank={rank} order={order} exponents={exponents}", flush=True)
        print(f"rank={rank} tested={counts['tested']} nontrivial={counts['nontrivial']} misses={counts['misses']}", flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ranks", type=int, nargs="+", default=[4, 5])
    parser.add_argument("--max-order", type=int, default=38)
    parser.add_argument("--orders", type=int, nargs="+")
    parser.add_argument("--samples", type=int)
    args = parser.parse_args()
    orders = args.orders or list(range(2, args.max_order + 1))
    if min(args.ranks) < 2 or min(orders, default=1) < 2 or (args.samples is not None and args.samples < 1):
        parser.error("ranks and orders must be at least two and sample count must be positive")
    scan(args.ranks, orders, args.samples)


if __name__ == "__main__":
    main()
