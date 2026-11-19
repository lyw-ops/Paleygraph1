"""Certified seed-angle secants and an integer replay of the slow Jacobi path."""
import json
from collections import Counter

from flint import arb, ctx


def advance(fibers, sign):
    shifted = [
        {w + shift: m for w, m in fiber.items()}
        for fiber, shift in zip(fibers, (sign, -sign))
    ]
    result = [Counter(), Counter()]
    for index, fiber in enumerate(shifted):
        for w, m in fiber.items():
            if w:
                result[index if w < 0 else 1 - index][w] += m
    total = sum(abs(w) * m for fiber in result for w, m in fiber.items())
    rank, remainder = divmod(total, 2)
    assert remainder == 0
    for fiber in result:
        fiber[0] = rank - sum(fiber.values())
        assert fiber[0] >= 0
    return tuple(+fiber for fiber in result)


def predicted(j):
    k, phase = divmod(j, 4)
    a = 2*k
    rows = [
        ({-2: a+1, 1: a, 2: 1}, {0: a+2, 1: a}),
        ({-1: a+1, 0: a+2}, {-1: a+2, 2: a, 3: 1}),
        ({0: a+3, 1: a, 2: 1}, {-2: a+2, 1: a+2}),
        ({-1: a+3, 2: a+2}, {-1: a+2, 0: a+2, 1: 1}),
    ]
    return tuple(+Counter(part) for part in rows[phase])


def secant(denominator, intervals):
    seed = arb(8).sqrt()
    radius = arb(97)/50
    total = arb(0)
    for i in range(intervals):
        # Left endpoint of a positive decreasing integrand on [0, pi/2].
        c = (arb.pi()*i/(2*intervals)).cos()
        x = seed*c + radius
        total += x*x/(denominator + x*x)
    return (total/intervals).sqrt()


if __name__ == "__main__":
    ctx.prec = 128
    lower = arb(2031)/128 - arb(1)/2**17
    real = secant(4*lower, 8192)
    complex_cap = secant(4*lower-2*(arb(97)/50)**2, 8192)
    assert real < arb(428236)/10**6 and complex_cap < arb(449922)/10**6
    assert arb(8)/5*(arb(428236)/10**6)**599 < arb(383)/10**223
    assert 4*(arb(449922)/10**6)**600 < arb(306)/10**210
    print(json.dumps({"bits": 128, "intervals": 8192, "real_upper_sum": str(real),
                      "complex_upper_sum": str(complex_cap)}))
    pair = advance(({-1: 1}, {1: 1}), -1)
    for j in range(1025):
        assert pair == predicted(j)
        assert all(sum(fiber.values()) == j+2 for fiber in pair)
        pair = advance(pair, (1, 1, -1, -1)[j % 4])
    print(json.dumps({"checked_phases": 1025, "initial_rank": 2, "last_rank": 1026}))
