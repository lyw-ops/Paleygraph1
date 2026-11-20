"""Price the center and Picard parts of the actual linear cold remainder."""

from contextlib import redirect_stdout
import io
import json
from pathlib import Path
import runpy


with redirect_stdout(io.StringIO()):
    replay = runpy.run_path(str(Path(__file__).with_name("cold-resummed-136-check.py")))

old = replay["inherited"]
arb = replay["arb"]
radius = replay["radius"]
folded = replay["folded"]
symmetric = replay["symmetric"]
seed_weights = [abs(value).upper() * (2 if k else 1)
                for k, value in enumerate(replay["coefficients"][1])]
width = len(seed_weights) - 1
seed = symmetric(seed_weights, width)
analytic_tail = replay["old_tail_price"]
residual_tail = 10 * replay["eps"] * replay["tilted"](seed_weights)
assert width + radius <= replay["cut_weight"]


def geometric_rate(field):
    product = seed * field
    return replay["price_rate"]([
        folded(product, width + radius, k) for k in range(width + radius + 1)
    ])


center = symmetric(replay["center"], radius)
assert geometric_rate(center) + analytic_tail < arb("0.267")

for depth, envelope in ((601, old["h"]), (602, replay["h"])):
    residual, _ = old["residual"](envelope)
    assert geometric_rate(residual) + analytic_tail + residual_tail < arb("0.260")
    print(json.dumps({
        "kind": "actual_linear_split",
        "height": depth,
        "eventual_center_upper": "0.267",
        "eventual_picard_residual_upper": "0.260",
        "center_only_sufficient_budget": "0.070",
        "nonlinear_budget": "0.142",
    }, sort_keys=True))
