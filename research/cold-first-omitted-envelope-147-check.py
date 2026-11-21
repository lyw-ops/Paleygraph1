"""Outward checks for the actual first omitted cold derivative's positive envelope."""

from contextlib import redirect_stdout
import io
import json
from pathlib import Path
import runpy


TRIAL = (
    761672660, 456984603, 398664354, 181829156,
    111320192, 65960392, 38368909, 22947655,
    13671600, 8111113, 4787286, 2715787,
)


def compare_principal_matrix(folded, arb):
    def symmetric_mass(weight):
        return folded[abs(weight)] / (2 if weight else 1)

    for output, target in enumerate(TRIAL, 1):
        image = sum(
            count * ((source - 1) * folded[output]
                     + symmetric_mass(output - source)
                     + symmetric_mass(output + source))
            for source, count in enumerate(TRIAL, 1)
        )
        assert image > arb("0.356") * target, output


def main():
    source = Path(__file__).with_name("cold-resummed-136-check.py")
    with redirect_stdout(io.StringIO()):
        replay = runpy.run_path(str(source))
    old = replay["inherited"]
    arb = replay["arb"]
    symmetric = replay["symmetric"]
    radius = replay["radius"]

    center = list(replay["center"])
    # Round 136 adds the Legendre majorant a at weights zero and two.
    center[0] -= replay["a"]
    center[2] -= replay["a"]
    assert all(entry >= 0 for entry in center)
    center_poly = symmetric(center, radius)

    weights = [
        abs(coefficient).upper() * (2 if k else 1)
        for k, coefficient in enumerate(replay["coefficients"][1])
    ]
    width = len(weights) - 1
    seed_poly = symmetric(weights, width)
    assert width + radius <= replay["cut_weight"]
    residual_tail = 10 * replay["tilted"](weights) * replay["eps"]

    def folded_product(field):
        product = seed_poly * field
        return [
            replay["folded"](product, width + radius, weight)
            for weight in range(width + radius + 1)
        ]

    analytic_tail = replay["old_tail_price"]
    center_rate = replay["price_rate"](folded_product(center_poly)) + analytic_tail
    assert center_rate < arb("0.150")
    for height, envelope in ((601, old["h"]), (602, replay["h"])):
        residual, _ = old["residual"](envelope)
        folded = folded_product(center_poly + residual)
        rate = replay["price_rate"](folded) + residual_tail + analytic_tail
        assert rate < arb("0.408")
        compare_principal_matrix(folded, arb)
        print(json.dumps({
            "kind": "actual_first_omitted_linear_positive_envelope",
            "height": height,
            "eventual_center_upper": "0.150",
            "eventual_first_omitted_upper": "0.408",
            "eventual_full_omitted_upper": "0.550",
            "strict_retained_comparison_lower": "0.356",
            "principal_weights": len(TRIAL),
        }, sort_keys=True))


if __name__ == "__main__":
    main()
