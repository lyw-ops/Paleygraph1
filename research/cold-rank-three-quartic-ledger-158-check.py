"""Pool every rank-three label through W degree four and bound later regroupings."""

from collections import defaultdict
from contextlib import redirect_stdout
import io
import json
from math import comb
from pathlib import Path
import runpy


def multiplier_rows(labels, beta, beta_cap, replay, legendre, rank_three):
    """Return exact low-degree label moduli and a positive higher-degree envelope."""
    arb, acb = replay["arb"], replay["acb"]
    poly = replay["arb_poly"]
    symmetric = replay["symmetric"]
    folded_label_row = legendre["folded_label_row"]
    degree = len(labels)-1
    W = symmetric([arb(1), arb(3)/2, arb(0), arb(1)/2], 3)
    W_powers = [(beta_cap*W)**ell for ell in range(degree+1)]
    full = [symmetric(folded_label_row(row, 2*(degree-j), arb), 2*(degree-j))
            for j, row in enumerate(labels)]
    rank_powers = rank_three["rank_powers"](4)
    pair_fiber = rank_three["pair_fiber"]
    for j in range(degree+1):
        width = 3*(degree-j)
        grouped = defaultdict(acb)
        for ell in range(min(4, degree-j)+1):
            factor = comb(j+ell, ell) * (beta/4)**ell
            for (k, leg_a, leg_b), a in labels[j+ell].items():
                for (r,s,u,v,m), multiplicity in rank_powers[ell].items():
                    coefficient = factor*a*multiplicity
                    for e in ((m-k, m+k) if k else (m,)):
                        grouped[r,s,u,v,e,leg_a,leg_b] += coefficient

        low_upper = [arb(0)]*(2*width+1)
        low_lower = [arb(0)]*(2*width+1)
        for (r,s,u,v,e,leg_a,leg_b), coefficient in grouped.items():
            value = abs(coefficient)*(leg_b+1)
            for w, multiplicity in pair_fiber(r,s,u,v):
                high, low = value.upper()*multiplicity, value.lower()*multiplicity
                for offset in range(-2*leg_a, 2*leg_a+1, 4):
                    position = width+w-e+offset
                    assert 0 <= position < len(low_upper)
                    low_upper[position] += high
                    low_lower[position] += low

        high = poly()
        for ell in range(5, degree-j+1):
            part = full[j+ell] * W_powers[ell] * comb(j+ell, ell)
            part_width = 2*(degree-j-ell)+3*ell
            high += part.left_shift(width-part_width)
        upper = poly(low_upper) + high
        lower = poly([max(arb(0), (atom-high[k]).lower()) for k,atom in enumerate(low_lower)])
        yield width, upper, lower


def comparisons(rows, replay, selected_size):
    """Extend each folded comparison using the original positive H measures."""
    arb, poly = replay["arb"], replay["arb_poly"]
    symmetric, folded = replay["symmetric"], replay["folded"]
    old = replay["inherited"]
    radius, cut = replay["radius"], replay["cut_weight"]
    a, b = replay["a"], replay["b"]
    fixed = list(replay["center"])
    for k, amount in enumerate((a+b, 3*b/2, a, 3*b/2)):
        fixed[k] -= amount
    weights = []
    for envelope in (old["h"], replay["h"]):
        residual, _ = old["residual"](envelope)
        house = [x+folded(residual, radius, k) for k,x in enumerate(fixed)]
        assert all(mass >= 0 for mass in house)
        weights.append(symmetric(house, radius))

    width, upper, lower = rows[0]
    B_upper = [folded(upper, width, k) for k in range(selected_size)]
    B_lower = [folded(lower, width, k) for k in range(selected_size)]
    results = []
    for measure in weights:
        E_upper = [arb(0)]*(cut+1)
        E_lower = [arb(0)]*(cut+1)
        power = poly([1])
        for j, (width, upper, lower) in enumerate(rows[1:], 1):
            power *= measure
            midpoint = width+j*radius
            upper_row, lower_row = upper*power, lower*power
            for k in range(min(cut, midpoint)+1):
                E_upper[k] += folded(upper_row, midpoint, k)
                E_lower[k] += folded(lower_row, midpoint, k)
        results.append((E_upper, E_lower))
    return (B_upper, B_lower), results


def main():
    directory = Path(__file__).parent
    with redirect_stdout(io.StringIO()):
        replay = runpy.run_path(str(directory / "cold-resummed-136-check.py"))
    compose = runpy.run_path(str(directory / "cold-three-center-composition-153-check.py"))
    legendre = runpy.run_path(str(directory / "cold-signed-legendre-omission-150-check.py"))
    cosines = runpy.run_path(str(directory / "cold-W-all-order-return-152-check.py"))["cosines"]
    arb, acb, t = (replay[key] for key in ("arb", "acb", "t"))
    kern, prev = (replay["fields"][key] for key in ("kern", "prev"))
    rank_three = kern["p3"]
    alpha, beta, *_ = rank_three["coefficients"](t, acb(prev["da"]), acb(prev["db"]))
    beta_cap = replay["b"]
    assert abs(beta) <= beta_cap
    unit = replay["seed"]/(2*t.sqrt())
    assert abs(unit) < arb("0.356") and abs(1/(2*t.sqrt())) < 1/arb("7.96")
    seed, _ = cosines(unit, arb, acb)
    coefficients = [[x/2 for x in seed], *replay["coefficients"][1:]]
    powers = legendre["tensor_counts"](len(coefficients)-1)
    labels = [legendre["signed_labels"](j, coefficients, powers, alpha, acb)
              for j in range(len(coefficients))]
    rows = list(multiplier_rows(labels, beta, beta_cap, replay, legendre, rank_three))

    (B_old, B_tail), ((_, E1_tail), (_, E2_tail)), ((A1, A1_tail), _) = compose["geometry"](directory, replay)
    (B, B_floor), ((E1, E1_floor), (E2, E2_floor)) = comparisons(rows, replay, len(B_old))
    retained = compose["block_rate"](((E2, A1), (B, E1)), replay)
    tail = (E2_tail*arb("1.048") + A1_tail*arb("0.4122")
            + B_tail*arb("0.4112") + E1_tail*arb("0.6931"))
    result = retained + tail
    principal = compose["principal_action"]
    trial = compose["TRIAL"]
    first = principal(E2_floor, principal(A1, trial))
    second = principal(B_floor, principal(E1_floor, trial))
    witness = min((x+y).lower()/count for x,y,count in zip(first, second, trial))
    upper = "0.66349297"
    lower = "0.61707"
    assert result < arb(upper) and witness > arb(lower)
    print(json.dumps({
        "kind": "cold_rank_three_quartic_ledger",
        "direct_two_height_eventual_upper": upper,
        "fixed_H_full_W_grouping_positive_floor": lower,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
