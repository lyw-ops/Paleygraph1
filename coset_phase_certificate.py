"""Exhaust the necessary Fourier profiles for a critical coset cover."""

import argparse
from collections import Counter
from functools import reduce
from itertools import combinations, product
from math import gcd, isqrt, prod

from coset_phase_check import has_difference_clique, zero_orders


def phase_totients(rank, small_primes_only=False):
    """Return the totients of the divisors of the common phase modulus."""
    prime_powers = []
    limit = rank if small_primes_only and rank >= 3 else 2 * rank
    for prime in range(2, limit + 1):
        if any(prime % d == 0 for d in range(2, isqrt(prime) + 1)):
            continue
        powers = [(1, 1)]
        power = prime
        while power <= 2 * rank or prime <= rank:
            powers.append((power, power - power // prime))
            if power > 2 * rank:
                break
            power *= prime
        prime_powers.append(powers)
    return {
        prod(d for d, _ in factors): prod(totient for _, totient in factors)
        for factors in product(*prime_powers)
    }


def offset_orders(modulus, totients, budget):
    allowed_orders = sorted(d for d, totient in totients.items() if d > 1 and totient <= budget)
    order_at_offset = {
        a * (modulus // d): d
        for d in allowed_orders
        for a in range(1, d)
        if gcd(a, d) == 1
    }
    return allowed_orders, order_at_offset


def candidate_masks(rank, totients):
    modulus = max(totients)
    budget = rank * rank - 1  # The saturated trivial Fourier coefficient costs one.
    allowed_orders, order_at_offset = offset_orders(modulus, totients, budget)
    offsets = sorted(order_at_offset)

    def extend(prefix, candidates, used, remaining_budget, maximum_order):
        remaining = rank - len(prefix)
        if remaining == 0:
            step = reduce(gcd, prefix, modulus)
            yield modulus // step, tuple(x // step for x in prefix)
            return
        if remaining == 1:
            for x, _, cost in candidates:
                if cost <= remaining_budget:
                    yield from extend((*prefix, x), (), (), 0, maximum_order)
            return

        for index, (x, orders, cost) in enumerate(candidates):
            if len(candidates) - index < remaining:
                break
            seen = used | orders
            available = remaining_budget - cost
            tail = []
            for y, previous_orders, _ in candidates[index + 1:]:
                new_order = order_at_offset.get(y - x)
                if new_order is None or new_order > maximum_order:
                    continue
                new_orders = previous_orders | {new_order}
                new_cost = sum(totients[d] for d in new_orders - seen)
                if new_cost <= available:
                    tail.append((y, new_orders, new_cost))
            if len(tail) >= remaining - 1:
                yield from extend((*prefix, x), tail, seen, available, maximum_order)

    # Translate a pair of maximum difference order to 0 and modulus / order.
    # Multiplication by a unit gives the latter normalization. All remaining
    # representatives are larger, because their gcd with the modulus is no smaller.
    for maximum_order in allowed_orders:
        first = modulus // maximum_order
        used = {maximum_order}
        available = budget - totients[maximum_order]
        candidates = []
        for x in offsets:
            if x <= first or order_at_offset[x] > maximum_order:
                continue
            other_order = order_at_offset.get(x - first)
            if other_order is None or other_order > maximum_order:
                continue
            orders = {order_at_offset[x], other_order}
            cost = sum(totients[d] for d in orders - used)
            if cost <= available:
                candidates.append((x, orders, cost))
        yield from extend((0, first), candidates, used, available, maximum_order)


def symmetric_candidate_masks(rank, totients):
    modulus = max(totients)
    budget = rank * rank - 1
    allowed_orders, order_at_offset = offset_orders(modulus, totients, budget)
    offsets = sorted(order_at_offset)

    def pair_orders(pairs, maximum_order):
        orders = {order_at_offset.get(abs(x - y), maximum_order + 1) for x, y in pairs}
        return orders if all(order <= maximum_order for order in orders) else None

    def extend(prefix, candidates, used, remaining_budget, maximum_order):
        remaining = rank - len(prefix)
        if remaining == 0:
            step = reduce(gcd, prefix, modulus)
            yield modulus // step, tuple(x // step for x in sorted(prefix))
            return

        for index, (orbit, orders, cost) in enumerate(candidates):
            if len(orbit) > remaining:
                continue
            seen = used | orders
            available = remaining_budget - cost
            tail = []
            for next_orbit, old_orders, _ in candidates[index + 1:]:
                if len(next_orbit) > remaining - len(orbit):
                    continue
                cross_orders = pair_orders(product(orbit, next_orbit), maximum_order)
                if cross_orders is None:
                    continue
                new_orders = old_orders | cross_orders
                new_cost = sum(totients[d] for d in new_orders - seen)
                if new_cost <= available:
                    tail.append((next_orbit, new_orders, new_cost))
            if sum(len(item[0]) for item in tail) >= remaining - len(orbit):
                yield from extend((*prefix, *orbit), tail, seen, available, maximum_order)

    # The normalized mask contains 0 and first. Its reflection must send 0
    # to a member, and must also include the image of first.
    for maximum_order in allowed_orders:
        first = modulus // maximum_order
        pool = {0, *(x for x in offsets if x >= first and order_at_offset[x] <= maximum_order)}
        for center in sorted(pool):
            seed = {0, first, center, (center - first) % modulus}
            if not seed <= pool or len(seed) > rank:
                continue
            used = pair_orders(combinations(seed, 2), maximum_order)
            if used is None:
                continue
            available = budget - sum(totients[d] for d in used)
            if available < 0:
                continue

            candidates = []
            for x in sorted(pool - seed):
                y = (center - x) % modulus
                if y < x or y not in pool:
                    continue
                orbit = (x,) if x == y else (x, y)
                orders = pair_orders((*product(orbit, seed), *combinations(orbit, 2)), maximum_order)
                if orders is None:
                    continue
                cost = sum(totients[d] for d in orders - used)
                if cost <= available:
                    candidates.append((orbit, orders, cost))
            yield from extend(tuple(seed), candidates, used, available, maximum_order)


def certify(rank, symmetric=False, small_primes_only=False):
    totients = phase_totients(rank, small_primes_only)
    profiles = Counter()
    masks = 0
    maximum_quotient = 0
    enumerate_masks = symmetric_candidate_masks if symmetric else candidate_masks
    for order, mask in enumerate_masks(rank, totients):
        masks += 1
        maximum_quotient = max(maximum_quotient, order)
        forbidden = zero_orders(order, mask)
        zeros = sum(totients[d] for d in forbidden)
        if 2 * rank * zeros >= (rank - 1) * order:
            profiles[(order, forbidden)] += 1

    weaker = 0
    for order, forbidden in profiles:
        if has_difference_clique(order, forbidden, (order + rank - 1) // rank):
            continue
        # To contradict the prime clique bound it suffices to exceed d / (r sqrt(2)).
        threshold = isqrt(order * order // (2 * rank * rank)) + 1
        if not has_difference_clique(order, forbidden, threshold):
            raise RuntimeError(f"unresolved phase profile {rank=} {order=} {forbidden=}")
        weaker += 1

    print(
        f"rank={rank} symmetric={symmetric} modulus={max(totients)} masks={masks} "
        f"max_quotient={maximum_quotient} "
        f"density_survivors={sum(profiles.values())} profiles={len(profiles)} weaker={weaker}",
        flush=True,
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ranks", type=int, nargs="*", default=[6])
    parser.add_argument("--symmetric", action="store_true", help="scan masks invariant under a reflection")
    parser.add_argument("--small-primes-only", action="store_true", help="use the sharper phase prime cutoff")
    args = parser.parse_args()
    if min(args.ranks) < 2:
        parser.error("ranks must be at least two")
    for rank in args.ranks:
        certify(rank, args.symmetric, args.small_primes_only)


if __name__ == "__main__":
    main()
