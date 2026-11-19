"""Exact bounds for the separated-seed rank majorant at floor 28."""

from fractions import Fraction
from math import comb, factorial
import json


def check_majorant():
    floor = 28
    seed = Fraction(5657, 2000)
    radius = Fraction(33, 20)
    root_upper = Fraction(5291503, 1000000)
    rho = Fraction(50001, 50000)
    cutoff = 12
    total = seed + radius
    ratio = total**2 / (4 * floor)
    assert seed**2 > 8 and root_upper**2 > floor and ratio < Fraction(1, 5)
    assert 8 * rho**2 < seed**2
    assert sum(comb(125000, j) * (rho - 1)**j for j in range(4)) > 8

    walk_mean = [
        Fraction(sum(comb(k, j) * abs(2 * j - k) for j in range(k + 1)), 2**k)
        for k in range(2 * cutoff + 1)
    ]
    value = derivative = Fraction(0)
    coefficient = Fraction(1)
    for index in range(1, cutoff + 1):
        degree = 2 * index
        coefficient *= abs(Fraction(3, 2) - index) / index
        weight = 2 * root_upper * coefficient / (4 * floor)**index
        for k in range(degree + 1):
            power = degree - k
            term = (
                weight * comb(degree, k) * seed**k * radius**power
                * (walk_mean[k] + power)
            )
            value += term
            derivative += power * term / radius

    # The generic bounds for A_m and A'_m are m total^m and m^2 total^(m-1).
    # From the first omitted term, the ratios of the resulting simple bounds
    # are at most ((cutoff + 2)/(cutoff + 1))^2 / 5 < 1/4.
    first = cutoff + 1
    assert Fraction(first + 1, first)**2 / 5 < Fraction(1, 4)
    tail = 2 * root_upper * Fraction(4, 3) * ratio**first
    value += tail * (2 * first)
    derivative += tail * (2 * first)**2 / total
    value_upper = Fraction(16493, 10000)
    derivative_upper = Fraction(9935, 10000)
    assert value < value_upper < radius
    assert derivative < derivative_upper < 1
    return {
        "kind": "exact_separated_seed_majorant",
        "minimum_floor": floor,
        "seed_upper": str(seed),
        "remainder_radius": str(radius),
        "summed_terms": cutoff,
        "value_upper": str(value_upper),
        "derivative_upper": str(derivative_upper),
    }


if __name__ == "__main__":
    print(json.dumps(check_majorant(), sort_keys=True))
    assert 32**2 * Fraction(4, 5) > 28**2
    assert sum(Fraction(4**j, factorial(j)) for j in range(6)) > 33
    assert Fraction(1, 7) > Fraction(14, 100)  # Half log(4/3) = atanh(1/7).
    assert 4 * Fraction(63, 65)**128 < Fraction(74, 1000)
    assert Fraction(14, 100) - Fraction(74, 1000) > Fraction(6, 100)
    print(json.dumps({
        "kind": "exact_reduced_square_stencil_constants",
        "anchor": 32,
        "cold": "1/2",
        "degree": 128,
        "eventual_excess_lower": "3/50",
    }, sort_keys=True))
