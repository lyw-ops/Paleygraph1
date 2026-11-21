"""Price genuine rank-four and next-center units inside the original H rows."""

from collections import defaultdict
from contextlib import redirect_stdout
import io
import json
from math import comb
from pathlib import Path
import runpy


def complete_low_labels(j, labels, beta, powers, acb):
    grouped = defaultdict(acb)
    for ell in range(min(4, len(labels)-1-j)+1):
        factor = comb(j+ell, ell)*(beta/4)**ell
        for (k, la, lb), value in labels[j+ell].items():
            for (r,s,u,v,m), multiplicity in powers[ell].items():
                coefficient = factor*value*multiplicity
                for e in ((m-k, m+k) if k else (m,)):
                    grouped[r,s,u,v,e,la,lb] += coefficient
    return grouped


def main():
    directory = Path(__file__).parent
    with redirect_stdout(io.StringIO()):
        replay = runpy.run_path(str(directory / "cold-resummed-136-check.py"))
    prior = runpy.run_path(str(directory / "cold-rank-three-quartic-ledger-158-check.py"))
    compose = runpy.run_path(str(directory / "cold-three-center-composition-153-check.py"))
    legendre = runpy.run_path(str(directory / "cold-signed-legendre-omission-150-check.py"))
    cosines = runpy.run_path(str(directory / "cold-W-all-order-return-152-check.py"))["cosines"]

    arb, acb, t = (replay[key] for key in ("arb", "acb", "t"))
    symmetric, folded, poly = (replay[key] for key in ("symmetric", "folded", "arb_poly"))
    radius, cut = (replay[key] for key in ("radius", "cut_weight"))
    kern, prev = (replay["fields"][key] for key in ("kern", "prev"))
    rank_three = kern["p3"]
    alpha, beta, groups, _ = rank_three["coefficients"](t, acb(prev["da"]), acb(prev["db"]))
    gamma = arb(499)/500 * beta * groups[1, 1][0, 0]
    delta = -2*gamma*kern["linear_scalar"](groups, beta)
    beta_cap, gamma_cap, delta_cap = (replay[key] for key in ("b", "c", "d"))
    assert abs(beta) <= beta_cap and abs(gamma) <= gamma_cap and abs(delta) <= delta_cap
    unit = replay["seed"]/(2*t.sqrt())
    assert abs(unit) < arb("0.356") and abs(1/(2*t.sqrt())) < 1/arb("7.96")
    seed, _ = cosines(unit, arb, acb)
    coefficients = [[x/2 for x in seed], *replay["coefficients"][1:]]
    degree = len(coefficients)-1
    leg_powers = legendre["tensor_counts"](degree)
    labels = [legendre["signed_labels"](j, coefficients, leg_powers, alpha, acb)
              for j in range(degree+1)]

    original = list(prior["multiplier_rows"](labels, beta, beta_cap, replay, legendre, rank_three))
    (B_old,B_tail), ((_,E1_tail),(_,E2_tail)), ((A1,A1_tail),_) = compose["geometry"](directory,replay)
    (B,_), ((E1,_),(E2,_)) = prior["comparisons"](original,replay,len(B_old))
    power = rank_three["rank_powers"](4)

    # Only J_h degree one is selected, with (F_degree,G_degree)=(0,0),(2,0),(0,2).
    low, high = (complete_low_labels(j, labels, beta, power, acb) for j in (1,3))
    c = 3*(gamma**2/8+delta**2/16)
    c_cap = 3*(gamma_cap**2/8+delta_cap**2/16)
    width = 3*(degree-1)
    signed_debit = [arb(0)]*(2*width+1)
    matches = 0
    signed_savings = []
    for label in low.keys() & high.keys():
        r,s,u,v,e,la,lb = label
        x, y = low[label], high[label]
        price = lb+1
        old = (abs(x)*price).upper()+c_cap*(abs(y)*price).upper()
        save = (old-(abs(x+c*y)*price).upper()).lower()
        if save <= 0:
            continue
        matches += 1
        signed_savings.append((abs(x)+abs(3*gamma**2*y/8)+abs(3*delta**2*y/16)-abs(x+c*y)).lower())
        for w, multiplicity in rank_three["pair_fiber"](r,s,u,v):
            for shift in range(-2*la,2*la+1,4):
                position = width+w-e+shift
                assert 0 <= position < len(signed_debit)
                signed_debit[position] += save*multiplicity

    fixed = list(replay["center"])
    a, b = replay["a"], beta_cap
    for k, amount in enumerate((a+b,3*b/2,a,3*b/2)):
        fixed[k] -= amount
    for field, cap, mid in ((kern["F"],gamma_cap,4),(kern["G"],delta_cap,5)):
        for k in range(mid+1):
            fixed[k] -= cap*folded(field,mid,k)
    old = replay["inherited"]
    for row,envelope in ((E1,old["h"]),(E2,replay["h"])):
        residual,_ = old["residual"](envelope)
        rest = [x+folded(residual,radius,k) for k,x in enumerate(fixed)]
        assert all(v >= 0 for v in rest)
        removal = poly(signed_debit)*symmetric(rest,radius)
        for k in range(min(cut,width+radius)+1):
            row[k] -= folded(removal,width+radius,k).lower()
        assert all(v >= 0 for v in row)

    assert matches and max(signed_savings) > arb("1e-7")
    retained = compose["block_rate"](((E2,A1),(B,E1)),replay)
    tail = (E2_tail*arb("1.048") + A1_tail*arb("0.4122")
            + B_tail*arb("0.4112") + E1_tail*arb("0.6931"))
    result = retained+tail
    upper = "0.66348896"
    lower = "2.9e-7"
    assert result < arb(upper) and max(signed_savings) > arb(lower)
    print(json.dumps({
        "kind":"actual_H_rank_four_and_next_scalar_units",
        "signed_label_matches":matches,
        "direct_two_height_eventual_upper":upper,
        "one_actual_signed_coefficient_saving_lower":lower,
    },sort_keys=True))


if __name__ == "__main__":
    main()
