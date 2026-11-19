"""Exact rational checks of the extrapolation formula and square margin."""
from fractions import Fraction as Q
from math import factorial, prod
import json


def chebyshev(order, x):
    previous, current = Q(1), x
    for _ in range(order):
        previous, current = current, 2 * x * current - previous
    return previous


def kernel(node, z):
    return (node - 1) * z**2 / (1 - (1 - node) * z)


def check_interpolant(order):
    d = Q(1, 25)
    nodes = [1 - Q(i, 4 * (order + 1)) for i in range(1, order + 1)]
    pole = 1 / (1 - d)

    def denominator(z):
        return prod(1 - (1 - x) * z for x in nodes)

    normalization = denominator(pole) / chebyshev(order, 2 * pole - 1)
    coefficients = []
    for i, x in enumerate(nodes):
        node_pole = 1 / (1 - x)
        other_factors = prod(1 - (1 - y) * node_pole
                             for j, y in enumerate(nodes) if j != i)
        coefficient = -(d - 1) * normalization * chebyshev(order, 2 * node_pole - 1)
        coefficient /= (1 - (1 - d) * node_pole) * (x - 1) * other_factors
        coefficients.append(coefficient)

    # After cancelling z^2 and clearing (1-(1-d)z)D(z), degree is at most J.
    for i in range(1, order + 3):
        z = Q(i, order + 3)
        residual = normalization * chebyshev(order, 2 * z - 1) / denominator(z)
        reconstructed = sum(c * kernel(x, z) for c, x in zip(coefficients, nodes))
        assert reconstructed == kernel(d, z) * (1 - residual)
    return {"kind": "rational_partial_fraction_identity", "order": order,
            "distinct_nonzero_test_points": order + 2, "cleared_degree_bound": order}


for degree in (1, 2, 5, 10):
    print(json.dumps(check_interpolant(degree), sort_keys=True))

assert sum(Q(8**i, factorial(i)) for i in range(12)) > 2049
assert 8 * Q(4095, 4097)**12000 < Q(24, 1000)
# log(4/3) = 2 atanh(1/7) > 2/7.
assert Q(1, 14) > Q(7, 100)
assert Q(7, 100) - Q(24, 1000) > Q(4, 100)
print(json.dumps({"kind": "square_asymptotic_margin_constants", "degree": 12000,
                  "cold_lower": "7/100", "budget_upper": "24/1000",
                  "eventual_excess_lower": "4/100"}, sort_keys=True))
