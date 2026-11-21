"""Outward packet bounds for the full analytic pure Jacobi seed multiplier."""

import ast
import json
from math import comb
from pathlib import Path

from flint import acb, arb, ctx


ctx.prec = 192
source = Path(__file__).with_name("cold-combined-height-130-check.py")
tree = ast.parse(source.read_text())
price_list = next(
    node for node in tree.body if isinstance(node, ast.Assign)
    and any(isinstance(target, ast.Name) and target.id == "scaled" for target in node.targets)
)
prices = [arb(value)/10**8 for value in ast.literal_eval(price_list.value)]
slope = prices[-1] - prices[-2]
assert 1 < slope < 2
assert all(k <= value <= 2*k for k, value in enumerate(prices))


def price(k):
    if abs(k) < len(prices):
        return prices[abs(k)]
    return prices[-1] + (abs(k)+1-len(prices))*slope


floor = arb(2031)/128
half = arb(1)/2**17
t = acb(arb(floor, half), arb(0, half))
seed = arb("2.8284275", arb("0.0000005"))
assert arb("2.828427")**2 < 8
assert 8 + arb(4)/10**30 < arb("2.828428")**2
z = seed/(4*t.sqrt())
cut = 14
coefficients = [acb(0)]*(2*cut)
for l in range(cut):
    arity = 2*l+1
    leading = (-1)**l*(arb(comb(2*l, l))/4**l)*z**arity
    for k in range(1, arity+1, 2):
        coefficients[k] += comb(arity, (arity-k)//2)*leading

masses = [2*abs(value).upper() for value in coefficients]
mass = sum(masses)
moment = sum(value*price(k) for k, value in enumerate(masses))
ratios = [mass+moment/slope]
for k in range(1, len(prices)+len(masses)):
    shifted = sum(value*(price(k+j)+price(k-j))/2
                  for j, value in enumerate(masses))
    ratios.append(((k-1)*moment+shifted)/price(k))
retained = max(max(value.upper() for value in ratios),
               (mass+moment/5000).upper())

rho = arb("2.828428")**2/(4*(floor-half))
assert 0 < rho < 1
tail = (4*rho.sqrt()*rho**cut
        *((cut+1)/(1-rho)+rho/(1-rho)**2))
assert retained + tail < arb("0.5279")
assert arb("0.528")**2 < arb("0.279")
print(json.dumps({
    "kind": "pure_seed_analytic_packet", "bits": ctx.prec, "retained_binomial_orders": cut,
    "geometric_translated_rate_upper": "0.5279",
    "eventual_step_upper": "0.528", "eventual_two_step_upper": "0.279",
}, sort_keys=True))
