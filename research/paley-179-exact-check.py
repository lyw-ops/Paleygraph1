"""Check finite two-copy charts and rational margins used in Round 179."""

from fractions import Fraction as Q
from itertools import product


def check_chart(p):
    squares = {x * x % p for x in range(1, p)}
    pairs = 0
    for s in squares - {1}:
        rows = []
        for r, b in product(range(2, p), squares - {1}):
            if s == b:
                continue
            a = r * s * pow(s - b, -1, p) % p
            c = r * b * pow((1 - r) * (s - b), -1, p) % p
            y = r * pow(1 - b, -1, p) % p
            d = r * b * pow((1 - r) * (1 - b), -1, p) % p
            if not {a, c, y, d} <= squares - {1}:
                continue
            v, x, u = (pow(label, -1, p) for label in (a, y, c))
            f = v * (1 - v) % p
            assert ((x - v) * (u - v) - f * (s - 1)) % p == 0
            assert (d * a * x * u - s) % p == 0
            rows.append((v, x, u, f))
        for (v, x, u, f), (vp, xp, up, fp) in product(rows, repeat=2):
            k = (xp - vp) * pow(x - v, -1, p) % p
            companion = fp * pow(f * k, -1, p) % p
            assert (up - vp - companion * (u - v)) % p == 0
            d = (vp - k * v) % p
            dp = (vp - companion * v) % p
            first_invariant = d * (k + d - 1) * pow(k, -1, p) % p
            second_invariant = dp * (companion + dp - 1) * pow(companion, -1, p) % p
            assert first_invariant == second_invariant
            pairs += 1
    return pairs


def check_cold_margins():
    center, half_width = Q(2031, 128), Q(1, 2**17)
    radius, lower_real = Q(2338, 1000), Q(349, 1000)
    assert 8 * Q(95, 100)**2 > (radius + lower_real)**2
    assert 1 - (Q(22, 7) / 10)**2 / 2 > Q(95, 100)
    assert 4 * (center - half_width) - radius**2 > Q(76, 10)**2
    assert 4 * (center + 2 * half_width) + (Q(282843, 100000) + radius)**2 < 91
    assert Q(282843, 100000)**2 > 8
    numerator = lower_real * Q(76, 10) - 2 * radius * half_width / Q(76, 10)
    assert numerator / 91 > Q(29, 1000)
    assert 4 * (center + half_width) + lower_real**2 < 64
    assert (lower_real / 8)**2 > 5 * Q(19, 1000)**2
    assert 4 * (Q(152704318, 10**12)**2 + Q(144290996, 10**12)**2) > Q(42, 10**5)**2
    assert Q(42, 10**5) * Q(19, 1000)**611 > Q(1, 10**1056)
    assert Q(3673, 1600) - Q(9, 4) == Q(73, 1600)


if __name__ == "__main__":
    check_cold_margins()
    for prime in (13, 17, 29, 37):
        print(f"p={prime}: checked {check_chart(prime)} ordered interior pairs")
