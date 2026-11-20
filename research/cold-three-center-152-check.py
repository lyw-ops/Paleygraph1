"""Price the full three-center step and its exact marked omission."""

from contextlib import redirect_stdout
from fractions import Fraction
import io
import json
from pathlib import Path
import runpy


def main():
    directory = Path(__file__).parent
    with redirect_stdout(io.StringIO()):
        replay = runpy.run_path(str(directory / "cold-resummed-136-check.py"))
    legendre = runpy.run_path(str(directory / "cold-signed-legendre-omission-150-check.py"))
    canonical = runpy.run_path(str(directory / "cold-W-all-order-return-152-check.py"))
    old = replay["inherited"]
    arb, acb, arb_poly = (replay[key] for key in ("arb", "acb", "arb_poly"))
    symmetric, folded, tilted = (replay[key] for key in ("symmetric", "folded", "tilted"))
    radius, cut_weight, eps = (replay[key] for key in ("radius", "cut_weight", "eps"))
    fields = replay["fields"]
    kern, prev = fields["kern"], fields["prev"]
    t = replay["t"]
    alpha, beta, *_ = kern["p3"]["coefficients"](t, acb(prev["da"]), acb(prev["db"]))
    assert abs(alpha) < arb("0.244") and abs(beta) < arb("0.082585")
    unit = replay["seed"] / (2 * t.sqrt())
    assert abs(unit) < arb("0.356") and abs(1 / (2 * t.sqrt())) < 1 / arb("7.96")

    # The R136 table starts at positive nonseed degree. Insert the seed-only
    # Laurent coefficients, half the positive-index cosine coefficients.
    seed_only, _ = canonical["cosines"](unit, arb, acb)
    seed_coefficients = [[coefficient / 2 for coefficient in seed_only], *replay["coefficients"][1:]]
    max_degree = len(seed_coefficients) - 1
    powers = legendre["tensor_counts"](max_degree)
    rows = []
    for j in range(max_degree + 1):
        labels = legendre["signed_labels"](j, seed_coefficients, powers, alpha, acb)
        width = 2 * (max_degree - j)
        weights = legendre["folded_label_row"](labels, width, arb)
        rows.append((symmetric(weights, width), width, tilted(weights)))

    alpha_cap, beta_cap = replay["a"], replay["b"]
    rank_three = [beta_cap, 3 * beta_cap / 2, arb(0), beta_cap / 2]
    pure_W = symmetric(rank_three, 3)
    W_power = arb_poly([1])
    selected = [arb(0)] * (cut_weight + 1)
    W_only = [arb(0)] * (cut_weight + 1)
    for j, (multiplier, width, _) in enumerate(rows):
        word = multiplier * W_power
        W_power *= pure_W
        midpoint = width + 3*j
        assert midpoint <= cut_weight
        for k in range(midpoint + 1):
            entry = folded(word, midpoint, k)
            selected[k] += entry
            if j:
                W_only[k] += entry

    v = arb("0.356") + (2 * arb("0.244") + 3 * arb("0.083")) / arb("7.96")
    ratio = v**2
    selected_tail = 4*v**29 * (15/(1-ratio) + ratio/(1-ratio)**2)
    B3 = replay["price_rate"](selected) + selected_tail
    W_insertion = replay["price_rate"](W_only) + selected_tail
    assert B3 < arb("0.6931") and W_insertion < arb("0.0635")
    assert arb("0.0635") * (arb("0.6931") + arb("0.644")) < arb("0.085")
    assert Fraction("0.6931")**2 + Fraction("0.017") * Fraction("1.048") + Fraction("0.50179639") == 1
    print(json.dumps({
        "kind": "actual_three_center_translated_step",
        "three_center_eventual_upper": "0.6931",
        "W_insertion_eventual_upper": "0.0635",
        "three_vs_two_center_square_upper": "0.085",
    }, sort_keys=True))

    fixed_other = list(replay["center"])
    fixed_other[0] -= alpha_cap + beta_cap
    fixed_other[1] -= 3 * beta_cap / 2
    fixed_other[2] -= alpha_cap
    # Remove the complete inherited upper first, then use the exact W row.
    fixed_other[3] -= 3 * beta_cap / 2
    assert all(x >= 0 for x in fixed_other)
    pure_W = symmetric(rank_three, radius)
    for height, envelope in ((601, old["h"]), (602, replay["h"])):
        residual, _ = old["residual"](envelope)
        other_row = [entry + folded(residual, radius, k) for k, entry in enumerate(fixed_other)]
        other = symmetric(other_row, radius)
        full = other + pure_W
        full_tilt = tilted(other_row) + tilted(rank_three)
        W_power = arb_poly([1])
        mixed = arb_poly([0])
        retained = [arb(0)] * (cut_weight + 1)
        loss = arb(0)
        for j, (multiplier, width, multiplier_tilt) in enumerate(rows[1:], 1):
            mixed = full * mixed + other * W_power
            W_power *= pure_W
            product = multiplier * mixed
            midpoint = width + j*radius
            for k in range(cut_weight + 1):
                retained[k] += folded(product, midpoint, k)
            loss += sum(folded(product, midpoint, k) * (arb(k)/5).cosh()
                        for k in range(cut_weight + 1, midpoint + 1))
            loss += multiplier_tilt * j * eps * (full_tilt + eps)**(j - 1)
        omission = replay["price_rate"](retained) + 10*loss + replay["old_tail_price"]
        ceiling = "0.4112" if height == 601 else "0.4122"
        assert omission < arb(ceiling)
        print(json.dumps({
            "kind": "actual_omission_outside_three_centers",
            "height": height,
            "eventual_omission_upper": ceiling,
        }, sort_keys=True))


if __name__ == "__main__":
    main()
