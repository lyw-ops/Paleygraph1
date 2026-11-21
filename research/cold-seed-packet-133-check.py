"""Exact rational comparisons for the cold seed packet and counting rates."""
import ast
from fractions import Fraction
import json
from pathlib import Path


source = Path(__file__).resolve().with_name("cold-combined-height-130-check.py")
module = ast.parse(source.read_text())
assign = next(
    stmt for stmt in module.body if isinstance(stmt, ast.Assign)
    and any(isinstance(target, ast.Name) and target.id == "scaled" for target in stmt.targets)
)
prices = [Fraction(value, 10**8) for value in ast.literal_eval(assign.value)]
slope = prices[-1] - prices[-2]
assert prices[0] == 0 and prices[1] == 1
assert all(k <= value <= 2*k for k, value in enumerate(prices))
assert 1 < slope < 2


def price(k):
    k = abs(k)
    if k < len(prices):
        return prices[k]
    return prices[-1] + (k + 1 - len(prices))*slope


comparisons = [
    (k - 1 + (price(k+1) + price(k-1))/2)/price(k)
    for k in range(1, len(prices))
]
comparisons.append(1+1/slope)
schur_constant = max(comparisons)
assert schur_constant < Fraction("1.505")

four_floor = 4*(Fraction(2031, 128)-Fraction(1, 2**17))
seed = Fraction("2.828428")
assert seed**2 > 8+Fraction(4, 10**30)
translated = (schur_constant+Fraction(1, 5000))*seed
assert translated**2 < Fraction("0.535")**2 * four_floor
assert Fraction("0.535")**2 < Fraction("0.287")
print(json.dumps({
    "kind": "translated_seed_packet", "schur_constant_upper": "1.505",
    "eventual_step_upper": "0.535", "eventual_two_step_upper": "0.287",
}, sort_keys=True))

remainder = Fraction("1.971573")
assert (Fraction("4.8")-remainder)**2 < 8
assert 2*seed*remainder*(four_floor-2*remainder**2) > 4*remainder**2*(seed+remainder)**2
assert (seed+remainder)**2 < Fraction("0.516074")**2*(four_floor+(seed+remainder)**2)
assert Fraction("0.5145")*Fraction("0.516074") < Fraction("0.26553")
assert Fraction("0.515")*Fraction("0.516074") < Fraction("0.2658")
print(json.dumps({
    "kind": "full_square_counting_rates", "derivative_height_602_upper": "0.516074",
    "frozen_two_step_upper": "0.26553", "actual_residual_two_step_upper": "0.2658",
}, sort_keys=True))
