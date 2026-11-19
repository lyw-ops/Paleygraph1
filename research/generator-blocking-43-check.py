"""Exact counting checks for near-square cyclic interval blockers."""

import json
from itertools import combinations
from math import gcd


def units(n):
    return [i for i in range(1, n) if gcd(i, n) == 1]


def prime_factors(n):
    factors = set()
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            factors.add(divisor)
        while n % divisor == 0:
            n //= divisor
        divisor += 1
    if n > 1:
        factors.add(n)
    return factors


def check_blocker(n, support):
    m = len(support)
    length = m//2
    reserve = m*(m+1)-n
    if reserve < 0 or length == 0:
        return None
    short_gap_budget = reserve // (m+1-length)
    unit_list = units(n)
    cap_numer = 2**(len(prime_factors(n))+1)*n
    short_pairs = 0
    for unit in unit_list:
        scaled = sorted(unit*x % n for x in support)
        gaps = [b-a for a, b in zip(scaled, scaled[1:] + [scaled[0]+n])]
        if max(gaps) > m+1:
            return None
        assert sum(m+1-g for g in gaps) == reserve
        assert sum(g <= length for g in gaps) <= short_gap_budget
        counts = [0]*(length+1)
        for a, b in combinations(scaled, 2):
            diff = b-a
            if diff <= length:
                counts[diff] += 1
            if n-diff <= length:
                counts[n-diff] += 1
        if short_gap_budget < m:
            assert max(counts) <= short_gap_budget
            assert sum(counts) <= short_gap_budget*(short_gap_budget+1)//2
        short_pairs += sum(counts)

    outside = 0
    phi = len(unit_list)
    for a, b in combinations(sorted(support), 2):
        diff = b-a
        d = gcd(diff, n)
        if d*cap_numer <= length*phi:
            outside += 2
            # The orbit comprises the units modulo n/d multiplied by d.
            orbit_count = sum(1 for value in range(1, length//d+1)
                              if gcd(value, n//d) == 1)
            order_phi = len(units(n//d))
            hits = sum(1 for unit in unit_list if (unit*diff) % n <= length)
            assert hits*order_phi == phi*orbit_count
            assert hits*2*n >= phi*length
    if short_gap_budget < m:
        assert outside*length <= n*short_gap_budget*(short_gap_budget+1)
    return {
        "short_gap_budget": short_gap_budget,
        "unit_direction_short_pairs": short_pairs,
        "outside_order_cut_pairs": outside,
    }


def check_small_masks(n, m):
    total = 0
    outside = 0
    for support in combinations(range(n), m):
        result = check_blocker(n, support)
        if result is not None:
            total += 1
            outside += result["outside_order_cut_pairs"]
    assert total > 0
    print(json.dumps(dict(kind="exhaustive_small_masks", n=n, m=m,
                          blockers=total, outside_order_cut_pairs=outside),
                     sort_keys=True))


def check_affine_cosets(prime):
    n = (prime-1)//2
    generator = next(x for x in range(2, prime)
                     if len({pow(x, j, prime) for j in range(n)}) == n
                     and pow(x, n, prime) == 1)
    checked = []
    for b in range(2, n+1):
        if n % b:
            continue
        step = pow(generator, n//b, prime)
        signs = {pow((1-pow(step, j, prime)) % prime, n, prime) for j in range(1, b)}
        if len(signs) == 1:
            # Its annihilator consists of the multiples of b in Z/n.
            result = check_blocker(n, range(0, n, b))
            assert result is not None
            checked.append([b, 1 if signs == {1} else -1])
    print(json.dumps(dict(kind="exact_prime_affine_annihilators", prime=prime,
                          n=n, monochromatic_subgroup_size_and_sign=checked),
                     sort_keys=True))


if __name__ == "__main__":
    for n, m in ((12, 4), (18, 5)):
        check_small_masks(n, m)
    for root, extras in ((32, (1,)), (48, (1, 11))):
        n = root*root
        support = sorted(list(range(0, n, root)) + list(extras))
        result = check_blocker(n, support)
        assert result is not None and result["outside_order_cut_pairs"] > 0
        print(json.dumps(dict(kind="near_square_cyclic_mask", n=n, m=len(support),
                              **result), sort_keys=True))
    for prime in (13, 17, 41, 101, 193, 257):
        check_affine_cosets(prime)
