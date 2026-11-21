"""Exact rational column prices for the retained analytic Jacobi/Legendre block."""

import ast
from collections import defaultdict
from fractions import Fraction
import json
from math import comb
from pathlib import Path


def load_prices():
    source = Path(__file__).with_name("cold-combined-height-130-check.py")
    tree = ast.parse(source.read_text())
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == "scaled"
            for target in node.targets
        ):
            return [Fraction(value, 10**8) for value in ast.literal_eval(node.value)]
    raise ValueError("Round 130's rational price list is missing")


PRICES = load_prices()
SLOPE = PRICES[-1] - PRICES[-2]
Z_CENTER = Fraction("0.12605")
Z_RADIUS = Fraction("0.00001")
RHO = Fraction("0.1261")
JACOBI_PREFACTOR = Fraction("0.356")
LEGENDRE_PREFACTOR = Fraction(1, 1) / Fraction("7.96")
ORDERS = 6


def price(weight):
    weight = abs(weight)
    if weight < len(PRICES):
        return PRICES[weight]
    return PRICES[-1] + (weight - len(PRICES) + 1) * SLOPE


def column_bound(folded):
    mass = sum(folded.values())
    moment = sum(value * price(weight) for weight, value in folded.items())
    bounds = [mass + moment / SLOPE, mass + moment / 5000]
    for source in range(1, len(PRICES) + max(folded) + 1):
        shifted = sum(
            value * (price(source + weight) + price(source - weight)) / 2
            for weight, value in folded.items()
        )
        bounds.append(((source - 1) * moment + shifted) / price(source))
    return max(bounds)


def chebyshev_power(power):
    return {
        mode: Fraction((2 if mode else 1) * comb(power, (power - mode) // 2), 2**power)
        for mode in range(power % 2, power + 1, 2)
    }


def retained_coefficients(legendre):
    center = defaultdict(Fraction)
    error = defaultdict(Fraction)
    for order in range(ORDERS):
        leading = Fraction((-1)**order * comb(2 * order, order), 4**order)
        if legendre:
            leading *= 2 * order + 1
        power = 2 * order if legendre else 2 * order + 1
        for mode, coefficient in chebyshev_power(power).items():
            scalar = leading * coefficient
            center[mode] += scalar * Z_CENTER**order
            if order:
                error[mode] += abs(scalar) * order * RHO**(order - 1) * Z_RADIUS
    prefactor = LEGENDRE_PREFACTOR if legendre else JACOBI_PREFACTOR
    return {mode: prefactor * (abs(value) + error[mode]) for mode, value in center.items()}


def legendre_fibers(cosines):
    folded = defaultdict(Fraction)
    for mode, value in cosines.items():
        folded[mode] += value
        folded[mode + 2] += value / 2
        folded[abs(mode - 2)] += value / 2
    return folded


def main():
    assert PRICES[1] == 1 and 1 < SLOPE < 2
    assert all(weight <= value <= 2 * weight for weight, value in enumerate(PRICES))
    floor = Fraction(2031, 128)
    half = Fraction(1, 2**17)
    minimum = floor - half
    # At n >= 10^8, use s_n^2/4 = 2+1/n and |t-floor| <= 2*half.
    assert (2 + Fraction(1, 10**8)) / minimum < RHO
    assert abs(2 / floor - Z_CENTER) + 4 * half / (floor * minimum) + Fraction(1, 10**8) / minimum < Z_RADIUS
    assert Z_CENTER < RHO < JACOBI_PREFACTOR**2 < 1
    assert Fraction("3.98")**2 < minimum

    pure = retained_coefficients(legendre=False)
    linear = legendre_fibers(retained_coefficients(legendre=True))
    joint = defaultdict(Fraction, pure)
    for weight, value in linear.items():
        joint[weight] += value

    z, cut = RHO, ORDERS
    pure_tail = 4 * JACOBI_PREFACTOR * z**cut * (
        (cut + 1) / (1 - z) + z / (1 - z)**2
    )
    linear_tail = 8 * LEGENDRE_PREFACTOR * z**cut * (
        2 * z * (1 + z) / (1 - z)**3
        + (4 * cut + 3) * z / (1 - z)**2
        + (cut + 1) * (2 * cut + 1) / (1 - z)
    )
    assert column_bound(linear) + linear_tail < Fraction("0.4866")
    assert column_bound(joint) + pure_tail + linear_tail < Fraction("0.9579")
    assert 2 * Fraction("0.528") * Fraction("0.487") < Fraction("0.515")
    assert Fraction("0.959")**2 < Fraction("0.920")
    print(json.dumps({
        "kind": "jacobi_linear_legendre_exact_column_price",
        "retained_taylor_orders": ORDERS,
        "geometric_linear_upper": "0.4866",
        "geometric_joint_upper": "0.9579",
        "eventual_linear_upper": "0.487",
        "eventual_joint_upper": "0.959",
        "eventual_mixed_two_step_upper": "0.515",
        "eventual_joint_square_upper": "0.920",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
