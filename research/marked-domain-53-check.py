"""Interval margins for an exact complex Picard invariant."""
import json
from pathlib import Path
import runpy

from flint import acb, arb, ctx

feedback = runpy.run_path(str(Path(__file__).with_name("astra-feedback-52-check.py")))
histogram = runpy.run_path(str(Path(__file__).with_name("astra-histogram-53-check.py")))
warm = feedback["warm"]
polynomial_cost = feedback["polynomial_cost"]
HALF_WIDTH = arb(1) / 4


def laurent(t, group_signs):
    """Combine modes on rectangular balls, or use radial termwise bounds."""
    modes = [[acb(0) for _ in range(2 * warm.CUTOFF + 1)]
             for _ in range(2 * warm.CUTOFF + 1)]
    weight = 2 * t.sqrt()
    for ell in range(1, warm.CUTOFF + 1):
        weight *= (arb(3) / 2 - ell) / (4 * ell * t)
        coefficient = weight if group_signs else abs(weight)
        for j in range(2 * ell + 1):
            power = 2 * ell - j
            factor = coefficient * warm.comb(2 * ell, j) * (warm.SEED / 2) ** power
            for i in range(power // 2 + 1):
                k = power - 2 * i
                modes[j][k] += factor * warm.comb(power, i) * (2 if k else 1)
    return modes


def bounds(t, b, c, group_signs):
    rank, moment, _ = polynomial_cost(laurent(t, group_signs), b, c, arb(1))
    radius = abs(t)
    ratio = (warm.SEED + b) ** 2 / (4 * radius)
    assert ratio < 1
    first = warm.CUTOFF + 1
    geometric = 1 / (1 - ratio)
    weighted = first * geometric + ratio * geometric**2
    squared = first**2 * geometric + (2 * first + 1) * ratio * geometric**2
    squared += 2 * ratio**2 * geometric**3
    tail = 2 * radius.sqrt() * ratio**first
    return ((rank + 2 * tail * weighted).upper(),
            (moment + tail * (4 * squared + 2 * weighted * c / b)).upper())


def rectangle(first, last, divisions, b, c, rank_cap, moment_cap):
    b, c = arb(b) / 1000, arb(c) / 1000
    rank_cap, moment_cap = arb(rank_cap) / 10000, arb(moment_cap) / 10000
    assert rank_cap < b and moment_cap < c
    for slab in range(first, last):
        t = acb(warm.slab(slab, divisions), arb(0, HALF_WIDTH))
        rank, moment = bounds(t, b, c, True)
        assert rank < rank_cap and moment < moment_cap, (slab, rank, moment)
    assert warm.SEED + b < arb(46) / 10
    print(json.dumps(dict(kind="complex_rank_moment_rectangle", slabs=[first, last],
                          divisions=divisions, imaginary_half_width="1/4",
                          rank_cap=str(rank_cap), moment_cap=str(moment_cap)),
                     sort_keys=True))


def radial():
    rank, moment = bounds(acb(22), arb(165) / 100, arb(349) / 100, False)
    assert rank < arb(164) / 100 < arb(165) / 100
    assert moment < arb(345) / 100 < arb(349) / 100
    print(json.dumps(dict(kind="radial_rank_moment_majorant", radius_minimum=22,
                          rank_cap="1.64", moment_cap="3.45"), sort_keys=True))


def packet_rectangle():
    start, stop, divisions = 2108, 2320, 128
    width = arb(1) / 32
    size = 2 * warm.CUTOFF + 1
    envelope = [[arb(0) for _ in range(size)] for _ in range(size)]
    for slab in range(start, stop):
        t = acb(warm.slab(slab, divisions), arb(0, width))
        for j, row in enumerate(laurent(t, True)):
            for k, value in enumerate(row):
                envelope[j][k] = max(envelope[j][k], abs(value).upper())
    caps = [arb(value) / 10**10 for value in histogram["CAPS"]]
    rho = arb(1)
    output, mass, moment = histogram["histogram_step"](envelope, caps, rho)
    lower_modulus = arb(start) / divisions
    upper_modulus = abs(acb(arb(stop) / divisions, width))
    mass_tail, moment_tail = histogram["taylor_tail"](
        lower_modulus, upper_modulus, mass, moment, rho)
    output[-2] += mass_tail
    output[-1] += moment_tail
    cap_ratio = arb(9996) / 10000
    assert all(value < cap_ratio * cap for value, cap in zip(output, caps))
    assert mass < arb(147) / 100 and warm.SEED + mass < arb(46) / 10
    print(json.dumps(dict(kind="complex_packet_rectangle", slabs=[start, stop],
                          divisions=divisions, imaginary_half_width="1/32",
                          rank_cap="1.47", component_ratio_cap="0.9996"),
                     sort_keys=True))


if __name__ == "__main__":
    ctx.prec = 192
    rectangle(2319, 2336, 128, 1740, 3700, 17393, 36899)
    rectangle(1168, 1216, 64, 1700, 3620, 16950, 35950)
    rectangle(304, 368, 16, 1650, 3490, 16200, 34250)
    radial()
    packet_rectangle()
