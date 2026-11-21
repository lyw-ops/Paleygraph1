"""Replay exact identities and exponent comparisons in the Round 178 notes."""

from collections import Counter
from fractions import Fraction as Q
from itertools import product


def relative_fibers(lines, p):
    for (left, right) in product(lines.values(), repeat=2):
        slope, intercept = left
        next_slope, next_intercept = right
        a = next_slope * pow(slope, -1, p) % p
        yield a, (next_intercept - a * intercept) % p


def check_relative_fibers(p):
    parabola = {x: (x * (x - 1) % p, x) for x in range(2, p)}
    counts = Counter(relative_fibers(parabola, p))
    assert all(count <= 2 for h, count in counts.items() if h != (1, 0))
    for c in range(1, p):
        family = {}
        for x in range(2, p):
            if x != c:
                inverse = pow((x - 1) * (x - c), -1, p)
                family[x] = (x * inverse % p, -c * inverse % p)
        assert len(set(family.values())) == len(family)
        counts = Counter(relative_fibers(family, p))
        exceptional = {(1, 0)}
        if c == p - 1:
            exceptional.add((p - 1, p - 1))
        assert all(count <= 2 for h, count in counts.items() if h not in exceptional)


def check_inverted_chart(p):
    for x, y in product(range(2, p), repeat=2):
        if x == y:
            continue
        r = (y - x) * pow(x * (y - 1), -1, p) % p
        b = (x - 1) * pow(y - 1, -1, p) % p
        k = r * pow(b, -1, p) % p
        u = (1 + k * x) % p
        assert y == (x + k * x * (x - 1)) % p
        assert r == k * pow(u, -1, p) % p
        assert b == pow(u, -1, p)
        for s in range(2, p):
            if s == b:
                continue
            physical_a = r * s * pow(s - b, -1, p) % p
            physical_c = r * b * pow((1 - r) * (s - b), -1, p) % p
            assert physical_a == k * s * pow(s * u - 1, -1, p) % p
            assert physical_c == k * pow((u - k) * (s * u - 1), -1, p) % p


def check_exponents():
    kappa = Q(3, 418)
    affine = Q(2) + (Q(3, 2) - kappa) / 2
    one_match = 2 * (affine / 8 + Q(1, 2) + Q(5, 16)) + Q(1, 2) - 1
    assert affine == Q(11, 4) - Q(3, 836)
    assert one_match == Q(29, 16) - Q(3, 3344)
    assert Q(2) + Q(11, 8) / 2 == Q(43, 16)
    delta, epsilon = Q(1, 800), Q(1, 1600)
    alpha = Q(18, 13) + Q(4, 13) * max(49 * epsilon, 36 * epsilon + 9 * delta)
    cutoff = Q(99, 200)
    target = Q(139, 64) + cutoff / 4
    assert alpha == Q(279, 200)
    assert target == Q(147, 64) - delta == Q(3673, 1600)
    assert target - (2 * alpha - cutoff) == Q(1, 1600)


if __name__ == "__main__":
    check_exponents()
    for prime in (5, 13, 17, 29):
        check_relative_fibers(prime)
        check_inverted_chart(prime)
        print(f"p={prime}: checked relative fibers and physical charts")
