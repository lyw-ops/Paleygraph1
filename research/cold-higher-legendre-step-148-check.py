"""Exact column prices for the cold derivative with at least two Legendre factors."""

from collections import defaultdict
from contextlib import redirect_stdout
from fractions import Fraction
import io
import json
from math import comb
from pathlib import Path
import runpy


def convolve(left, right):
    output = defaultdict(Fraction)
    for a, left_mass in left.items():
        for b, right_mass in right.items():
            output[a + b] += left_mass * right_mass
    return output


def powers(source, largest):
    result = [{0: Fraction(1)}]
    for _ in range(largest):
        result.append(convolve(result[-1], source))
    return result


def main():
    source = Path(__file__).with_name("cold-jacobi-linear-legendre-145-check.py")
    comparison = runpy.run_path(str(source))
    with redirect_stdout(io.StringIO()):
        comparison["main"]()
    u = comparison["JACOBI_PREFACTOR"]
    v = Fraction("0.244") * comparison["LEGENDRE_PREFACTOR"]
    width = u + 2 * v
    cut = 8
    assert width < 1
    jacobi = powers({-1: Fraction(1, 2), 1: Fraction(1, 2)}, 2 * cut - 1)
    legendre = powers(
        {-2: Fraction(1, 2), 0: Fraction(1), 2: Fraction(1, 2)}, 2 * cut - 1
    )
    retained = defaultdict(Fraction)
    for order in range(1, cut):
        degree = 2 * order + 1
        scale = Fraction(comb(2 * order, order), 4**order)
        for count in range(2, degree + 1):
            coefficient = scale * comb(degree, count) * u**(degree - count) * v**count
            for weight, mass in convolve(jacobi[degree - count], legendre[count]).items():
                retained[abs(weight)] += coefficient * mass

    square = width**2
    tail = 4 * width**(2 * cut + 1) * (
        (cut + 1) / (1 - square) + square / (1 - square)**2
    )
    assert comparison["column_bound"](retained) + tail < Fraction("0.00905")
    assert Fraction("0.634") + Fraction("0.0092") < Fraction("0.644")
    assert Fraction("0.644")**2 < Fraction("0.415")
    print(json.dumps({
        "kind": "whole_two_center_cold_derivative",
        "first_omitted_binomial_order": cut,
        "geometric_higher_legendre_upper": "0.00905",
        "eventual_higher_legendre_upper": "0.0092",
        "eventual_two_center_step_upper": "0.644",
        "eventual_two_center_square_upper": "0.415",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
