"""Price the two-height positive comparison outside the three-center square."""

from contextlib import redirect_stdout
import io
import json
from pathlib import Path
import runpy


TRIAL = (1000000, 406701, 238886, 141182, 84238, 49987,
         29805, 17832, 10694, 6401, 3782, 2038)


def geometry(directory, replay):
    legendre = runpy.run_path(str(directory / "cold-signed-legendre-omission-150-check.py"))
    canonical = runpy.run_path(str(directory / "cold-W-all-order-return-152-check.py"))
    old = replay["inherited"]
    arb, acb, arb_poly = (replay[key] for key in ("arb", "acb", "arb_poly"))
    symmetric, folded, tilted = (replay[key] for key in ("symmetric", "folded", "tilted"))
    radius, cut, eps = (replay[key] for key in ("radius", "cut_weight", "eps"))
    fields = replay["fields"]
    kern, prev = fields["kern"], fields["prev"]
    t = replay["t"]
    alpha, beta, *_ = kern["p3"]["coefficients"](t, acb(prev["da"]), acb(prev["db"]))
    assert abs(alpha) < arb("0.244") and abs(beta) < arb("0.083")
    unit = replay["seed"] / (2*t.sqrt())
    assert abs(unit) < arb("0.356") and abs(1/(2*t.sqrt())) < 1/arb("7.96")
    seed_only, _ = canonical["cosines"](unit, arb, acb)
    coefficients = [[c/2 for c in seed_only], *replay["coefficients"][1:]]
    degree = len(coefficients) - 1
    powers = legendre["tensor_counts"](degree)
    rows = []
    for j in range(degree + 1):
        labels = legendre["signed_labels"](j, coefficients, powers, alpha, acb)
        width = 2*(degree-j)
        weights = legendre["folded_label_row"](labels, width, arb)
        rows.append((symmetric(weights, width), width, tilted(weights)))

    a, b = replay["a"], replay["b"]
    W = [b, 3*b/2, arb(0), b/2]
    W_poly = symmetric(W, 3)
    power = arb_poly([1])
    selected = [arb(0)] * (3*degree + 1)
    for j, (multiplier, width, _) in enumerate(rows):
        product = multiplier * power
        midpoint = width + 3*j
        for k in range(midpoint + 1):
            selected[k] += folded(product, midpoint, k)
        power *= W_poly
    v = arb("0.356") + (2*arb("0.244") + 3*arb("0.083"))/arb("7.96")
    ratio = v**2
    selected_tail = 4*v**29 * (15/(1-ratio) + ratio/(1-ratio)**2)

    fixed_other = list(replay["center"])
    for k, deduction in enumerate((a+b, 3*b/2, a, 3*b/2)):
        fixed_other[k] -= deduction
    assert all(x >= 0 for x in fixed_other)
    W_poly = symmetric(W, radius)
    omissions = []
    full_rows = []
    for envelope in (old["h"], replay["h"]):
        residual, _ = old["residual"](envelope)
        other_row = [entry + folded(residual, radius, k) for k, entry in enumerate(fixed_other)]
        other = symmetric(other_row, radius)
        full = other + W_poly
        full_tilt = tilted(other_row) + tilted(W)
        power = arb_poly([1])
        mixed = arb_poly([0])
        retained = [arb(0)] * (cut + 1)
        loss = arb(0)
        for j, (multiplier, width, multiplier_tilt) in enumerate(rows[1:], 1):
            mixed = full * mixed + other * power
            power *= W_poly
            product = multiplier * mixed
            midpoint = width + j*radius
            for k in range(cut+1):
                retained[k] += folded(product, midpoint, k)
            loss += sum(folded(product, midpoint, k) * (arb(k)/5).cosh()
                        for k in range(cut+1, midpoint+1))
            loss += multiplier_tilt*j*eps*(full_tilt+eps)**(j-1)
        omissions.append((retained, 10*loss + replay["old_tail_price"]))
        _, leak = old["derivative_rate"](envelope)
        full_rows.append((old["retained"](residual, 1), 10*leak))
    return (selected, selected_tail), omissions, full_rows


def base_price(moment, row, cost, k):
    if not k:
        return 0
    return (k-1)*moment + sum(
        mass*(cost(k+j)+cost(abs(k-j)))/2 for j, mass in enumerate(row)
    )


def block_rate(pairs, replay):
    price = replay["price"]
    slope = replay["slope"]
    end = len(replay["inherited"]["prices"]) + max(len(outer)+len(inner) for outer, inner in pairs)
    columns = [replay["arb"](0) for _ in range(end+1)]
    affine = replay["arb"](0)
    off_pair = replay["arb"](0)
    for outer, inner in pairs:
        outer_moment = sum(mass*price(k) for k, mass in enumerate(outer))
        first = [base_price(outer_moment, outer, price, i) for i in range(end+len(inner))]
        inner_moment = sum(mass*first[k] for k, mass in enumerate(inner))
        for k in range(1, end+1):
            columns[k] += base_price(inner_moment, inner, first.__getitem__, k)
        outer_slope = sum(outer)*slope + outer_moment
        affine += (sum(inner)*outer_slope + inner_moment)/slope
        off_pair += sum(inner)*sum(outer) + (inner_moment + sum(inner)*outer_moment)/5000
    return max(x.upper() for x in [affine, off_pair, *(columns[k]/price(k) for k in range(1, end+1))])


def principal_action(row, vector):
    def symmetric_mass(k):
        return row[abs(k)] / (2 if k else 1)

    return [
        sum(count*((j-1)*row[i] + symmetric_mass(i-j) + symmetric_mass(i+j))
            for j, count in enumerate(vector, 1))
        for i in range(1, len(vector)+1)
    ]


def main():
    directory = Path(__file__).parent
    with redirect_stdout(io.StringIO()):
        replay = runpy.run_path(str(directory / "cold-resummed-136-check.py"))
    arb = replay["arb"]
    (B, B_tail), ((E1, E1_tail), (E2, E2_tail)), ((A1, A1_tail), _) = geometry(directory, replay)
    assert replay["price_rate"](B) + B_tail < arb("0.6931")
    assert replay["price_rate"](E1) + E1_tail < arb("0.4112")
    assert replay["price_rate"](E2) + E2_tail < arb("0.4122")
    assert replay["price_rate"](A1) + A1_tail < arb("1.048")
    tail = E2_tail*arb("1.048") + A1_tail*arb("0.4122") + B_tail*arb("0.4112") + E1_tail*arb("0.6931")
    retained = block_rate(((E2, A1), (B, E1)), replay)
    assert retained + tail < arb("0.66381")
    forward = principal_action(E2, principal_action(A1, TRIAL))
    reverse = principal_action(B, principal_action(E1, TRIAL))
    assert all(x+y > arb("0.6174")*target for x,y,target in zip(forward, reverse, TRIAL))
    print(json.dumps({
        "kind": "two_height_positive_composition_outside_B3",
        "two_height_actual_difference_upper": "0.66381",
        "retained_principal_positive_lower": "0.6174",
        "principal_weights": len(TRIAL),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
