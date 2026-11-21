"""Outward positive comparison after deleting the entire two-center subrow."""

from contextlib import redirect_stdout
import io
import json
from pathlib import Path
import runpy


TRIAL = (
    1000000, 620099, 529458, 265125, 165286, 101643,
    61637, 37913, 23322, 14264, 8665, 5081,
)


def verify_principal_lower(row, arb):
    def symmetric_mass(weight):
        return row[abs(weight)] / (2 if weight else 1)

    for output, target in enumerate(TRIAL, 1):
        image = sum(
            count * ((source - 1) * row[output]
                     + symmetric_mass(output - source)
                     + symmetric_mass(output + source))
            for source, count in enumerate(TRIAL, 1)
        )
        assert image > arb("0.4607") * target, output


def main():
    source = Path(__file__).with_name("cold-resummed-136-check.py")
    with redirect_stdout(io.StringIO()):
        replay = runpy.run_path(str(source))
    old = replay["inherited"]
    arb = replay["arb"]
    arb_poly = replay["arb_poly"]
    symmetric = replay["symmetric"]
    folded = replay["folded"]
    tilted = replay["tilted"]
    radius = replay["radius"]
    cut_weight = replay["cut_weight"]
    eps = replay["eps"]
    analytic_tail = replay["old_tail_price"]

    # Remove the two folded entries of the Legendre center in the majorant.
    fixed_other = list(replay["center"])
    amplitude = replay["a"]
    fixed_other[0] -= amplitude
    fixed_other[2] -= amplitude
    assert all(entry >= 0 for entry in fixed_other)
    pure = symmetric([amplitude, arb(0), amplitude], radius)

    seed_rows = []
    for coefficients in replay["coefficients"][1:]:
        weights = [abs(coefficient).upper() * (2 if k else 1)
                   for k, coefficient in enumerate(coefficients)]
        width = len(weights) - 1
        seed_rows.append((symmetric(weights, width), width, tilted(weights)))

    for height, envelope in ((601, old["h"]), (602, replay["h"])):
        residual, _ = old["residual"](envelope)
        other_row = [entry + folded(residual, radius, k)
                     for k, entry in enumerate(fixed_other)]
        other = symmetric(other_row, radius)
        full = pure + other
        full_tilt = tilted(other_row) + tilted([amplitude, arb(0), amplitude])
        pure_power = arb_poly([1])
        mixed = arb_poly([0])
        parts = [[arb(0)] * (cut_weight + 1) for _ in range(2)]
        losses = [arb(0), arb(0)]
        for j, (seed, width, seed_tilt) in enumerate(seed_rows, 1):
            mixed = full * mixed + other * pure_power
            pure_power *= pure
            comparison = seed * mixed
            midpoint = width + j * radius
            index = int(j > 1)
            for k in range(cut_weight + 1):
                parts[index][k] += folded(comparison, midpoint, k)
            losses[index] += sum(
                folded(comparison, midpoint, k) * (arb(k) / 5).cosh()
                for k in range(cut_weight + 1, midpoint + 1)
            )
            losses[index] += seed_tilt * j * eps * (full_tilt + eps)**(j - 1)

        price_rate = replay["price_rate"]
        linear = price_rate(parts[0]) + 10 * losses[0] + analytic_tail
        higher = price_rate(parts[1]) + 10 * losses[1] + analytic_tail
        whole = [x + y for x, y in zip(*parts)]
        total = price_rate(whole) + 10 * sum(losses) + analytic_tail
        assert linear < arb("0.408")
        assert higher < arb("0.134")
        assert total < arb("0.542")
        verify_principal_lower(whole, arb)
        print(json.dumps({
            "kind": "actual_two_center_omission_positive_envelope",
            "height": height,
            "eventual_linear_upper": "0.408",
            "eventual_higher_upper": "0.134",
            "eventual_total_upper": "0.542",
            "strict_retained_comparison_lower": "0.4607",
            "principal_weights": len(TRIAL),
        }, sort_keys=True))


if __name__ == "__main__":
    main()
