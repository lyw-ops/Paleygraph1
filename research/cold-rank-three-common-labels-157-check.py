"""Recompose the cold two-height comparison after disjoint rank-three label merges."""

from contextlib import redirect_stdout
import io
import json
from math import comb
from pathlib import Path
import runpy


def label_savings(low, high, j, copies, beta, beta_cap, legendre, arb, acb):
    """Fold savings for the W^copies and W^(copies+2) sectors at fixed H arity."""
    unit = arb(1)/4 if copies == 0 else arb(3)/4
    high_factor = unit * comb(j+copies+2, copies+2)
    low_factor = comb(j+copies, copies)
    coefficients = {}
    width = 0
    for key in low.keys() & high.keys():
        a, b = low[key], high[key]
        old = low_factor*beta_cap**copies*abs(a).upper()
        old += high_factor*beta_cap**(copies+2)*abs(b).upper()
        merged = beta**copies*(low_factor*a + high_factor*beta**2*b)
        savings = (old-abs(merged).upper()).lower()
        if savings > 0:
            coefficients[key] = acb(savings)
            shift, legendre_a, legendre_b = key
            width = max(width, shift + 2*max(legendre_a, legendre_b))
    folded = legendre["folded_label_row"](coefficients, width, arb)
    return folded, width, len(coefficients)


def main():
    directory = Path(__file__).parent
    with redirect_stdout(io.StringIO()):
        replay = runpy.run_path(str(directory / "cold-resummed-136-check.py"))
    compose = runpy.run_path(str(directory / "cold-three-center-composition-153-check.py"))
    legendre = runpy.run_path(str(directory / "cold-signed-legendre-omission-150-check.py"))
    cosines = runpy.run_path(str(directory / "cold-W-all-order-return-152-check.py"))["cosines"]
    arb, acb, t = (replay[key] for key in ("arb", "acb", "t"))
    symmetric, folded = (replay[key] for key in ("symmetric", "folded"))
    radius, cut = (replay[key] for key in ("radius", "cut_weight"))
    kern, prev = (replay["fields"][key] for key in ("kern", "prev"))
    alpha, beta, *_ = kern["p3"]["coefficients"](t, acb(prev["da"]), acb(prev["db"]))
    beta_cap = replay["b"]
    assert abs(beta) <= beta_cap
    unit = replay["seed"]/(2*t.sqrt())
    assert abs(unit) < arb("0.356") and abs(1/(2*t.sqrt())) < 1/arb("7.96")
    seed, _ = cosines(unit, arb, acb)
    coefficients = [[x/2 for x in seed], *replay["coefficients"][1:]]
    degree = len(coefficients)-1
    powers = legendre["tensor_counts"](degree)
    labels = [legendre["signed_labels"](k, coefficients, powers, alpha, acb)
              for k in range(degree+1)]
    W = symmetric([arb(1), arb(3)/2, arb(0), arb(1)/2], 3)

    unit_rows = []
    match_counts = [0, 0]
    for j in range(degree-1):
        parts = []
        for copies in (0, 1):
            if j+copies+2 > degree:
                continue
            row, width, count = label_savings(labels[j+copies], labels[j+copies+2],
                j, copies, beta, beta_cap, legendre, arb, acb)
            poly = symmetric(row, width)
            if copies:
                poly *= W
                width += 3
            parts.append((poly, width))
            match_counts[copies] += count
        unit_rows.append(parts)
    assert all(count > 0 for count in match_counts)

    (B, B_tail), ((E1, E1_tail), (E2, E2_tail)), ((A1, A1_tail), _) = compose["geometry"](directory, replay)

    def debit(row, parts, power=None, radius_shift=0):
        for poly, width in parts:
            if power is not None:
                poly = poly * power
            midpoint = width + radius_shift
            for k in range(min(len(row), midpoint+1)):
                row[k] -= folded(poly, midpoint, k).lower()

    debit(B, unit_rows[0])
    fixed_other = list(replay["center"])
    a = replay["a"]
    for k, amount in enumerate((a+beta_cap, 3*beta_cap/2, a, 3*beta_cap/2)):
        fixed_other[k] -= amount
    old = replay["inherited"]
    for destination, envelope in ((E1, old["h"]), (E2, replay["h"])):
        residual, _ = old["residual"](envelope)
        house = [x+folded(residual, radius, k) for k,x in enumerate(fixed_other)]
        assert all(x >= 0 for x in house)
        term = symmetric(house, radius)
        power = replay["arb_poly"]([1])
        for j in range(1, len(unit_rows)):
            power *= term
            debit(destination, unit_rows[j], power, j*radius)

    assert all(x >= 0 for row in (B, E1, E2) for x in row)
    assert len(E1) == len(E2) == cut+1
    retained = compose["block_rate"](((E2, A1), (B, E1)), replay)
    tail = (E2_tail*arb("1.048") + A1_tail*arb("0.4122")
            + B_tail*arb("0.4112") + E1_tail*arb("0.6931"))
    result = retained + tail
    trial = compose["TRIAL"]
    principal = compose["principal_action"]
    first = principal(E2, principal(A1, trial))
    second = principal(B, principal(E1, trial))
    witness = min((x+y).lower()/z for x,y,z in zip(first, second, trial))
    upper = "0.66365735"
    lower = "0.61729"
    assert result < arb(upper) and witness > arb(lower)
    print(json.dumps({
        "kind": "rank_three_disjoint_labels_direct_two_height_composition",
        "matched_unit_slots": match_counts[0],
        "matched_standard_slots": match_counts[1],
        "direct_two_height_eventual_upper": upper,
        "retained_principal_positive_lower": lower,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
