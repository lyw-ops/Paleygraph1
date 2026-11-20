"""Exact five-fold quotient classification and certified physical-window scores."""
from fractions import Fraction
from itertools import combinations
from math import gcd
from pathlib import Path
import json
import runpy

import numpy as np
from flint import arb, ctx, fmpq

base = Path(__file__).resolve().parent
ctx.prec = 192


def enclosure(x):
    return [int((10**9*x).lower().floor().unique_fmpz()),
            int((10**9*x).upper().ceil().unique_fmpz())]


def quotient_patterns():
    d = Fraction(213, 1000)
    deletion = Fraction(1, 10000)
    tau = Fraction(18, 25)
    radius = Fraction(1, 10**8)
    assert (2-tau-6*deletion-Fraction(3,3000))/6 > d
    assert 4*radius+Fraction(2, 10**6) < Fraction(1, 200000)
    assert Fraction(1, 5*10**6) > radius
    # 5k - 3 <= m <= k/d implies k <= 8, using parity.
    assert 10*(5 - 1/d) > 3
    cases = [(m, k) for k in (2, 4, 6, 8)
             for m in range(5*k-3, int(k/d)+1, 2)]
    found = {}
    for m, k in cases:
        units = [n for n in range(1, m) if gcd(n, m) == 1]
        patterns = set()
        for half in combinations(range(1, (m+1)//2), k//2):
            full = set(half) | {m-a for a in half}
            five = {0}
            for _ in range(5):
                five = {(u+x) % m for u in five for x in full}
            if 0 in five:
                continue
            if any({(x+j) % m for x in five} == five for j in range(1, m)):
                continue
            def representative(u):
                return tuple(sorted(min((u*x) % m, (-u*x) % m) for x in half))
            patterns.add(min(map(representative, units)))
        found[m] = sorted(patterns)
    expected = {7: [(1,)], 9: [(1,)], 17: [(1, 3)], 27: [(1, 3, 5)],
                37: [(1, 3, 5, 7)]}
    assert found == expected
    certificate = []
    for m, (half,) in found.items():
        j = (m-1)//2
        h = j*pow(2, -1, m) % m
        coefficients = [-4*arb.cos_pi_fmpq(fmpq(2*j*x, m))
                        -2*arb.cos_pi_fmpq(fmpq(2*h*x, m)) for x in half]
        assert all(c > 0 for c in coefficients)
        density = arb(d.numerator)/d.denominator
        max_c = coefficients[0]
        for c in coefficients[1:]:
            max_c = max_c.max(c)
        bound = 2*sum(coefficients)/m - max_c*(arb(2*len(half))/m-density)
        assert bound - arb(3)/1500 > arb(18)/25
        assert bound - arb(3)/3000 > arb(18)/25 + arb(6)/10000
        certificate.append(dict(index=m, representatives=list(half), twist=j, half_twist=h,
                                required_coefficient=enclosure(bound)))
    return dict(test="fivefold_stabilizers", density_lower=str(d), minimum_order=1500,
                tau_upper=str(tau), resilient_minimum_order=3000, symmetric_deletion=str(deletion),
                phase_radius_turns=str(radius), bounded_character_order=10**6,
                precision_bits=ctx.prec, units="1e-9", cases=certificate)


def physical_windows():
    pin = runpy.run_path(str(base / "astra-quartic-89-check.py"))
    prior = runpy.run_path(str(base / "astra-quotient-75-check.py"))
    ctx.prec = 384
    signs = list(map(int, pin["face"]["mask"]))
    rows, _ = pin["face"]["faces"]()
    x = [row[0] for row in rows]
    a = x[0]
    n = len(x)
    terminal, masks, _ = pin["delayed_masks"](signs)
    weights = dict.fromkeys(masks, Fraction(1, len(masks)))
    threshold = arb(7)/50
    family, scores = [], {d: (Fraction(0), Fraction(0)) for d in masks}
    count = [sum((w for d, w in weights.items() if i in masks[d]), Fraction(0)) for i in range(n)]
    def member(h, coset):
        mass = sum(x[i] for i in coset)
        assert mass > threshold or mass < threshold
        if mass < threshold:
            return
        t = 1 if coset[0] == 0 else 2
        b = n//(t*h)
        restricted = np.array(signs[::n//b])
        if all(v <= 0 for v in restricted):
            lo = hi = Fraction(1)
        elif all(v >= 0 for v in restricted):
            lo = hi = Fraction(b)
        else:
            lo = Fraction(prior["lower_theta"](restricted, 1))
            hi = b/Fraction(prior["lower_theta"](restricted, -1))
        coeff = (lo/(t*b), hi/(t*b))
        occ = {d: Fraction(len(set(coset) & set(P)), h) for d, P in masks.items()}
        for d in scores:
            scores[d] = tuple(max(v, c*occ[d]) for v,c in zip(scores[d], coeff))
        mean = sum(count[i] for i in coset)/h
        family.append((h, coset[0], coeff, occ, mean))
    for h in range(1, n+1):
        if n % h:
            continue
        assert a*h > 2 or a*h < 2
        if a*h > 2:
            continue
        step = n//h
        member(h, list(range(0, n, step)))
        if step % 2 == 0:
            member(h, list(range(step//2, n, step)))
    assert [(h, i) for h, i, *_ in family] == [(1, 0), (2, 0), (3, 0), (4, 0),
            (4, 6), (6, 0), (8, 0), (12, 0), (12, 2)]
    assert scores[2] == (Fraction(1, 4), Fraction(1, 4))
    assert scores[4] == scores[8] and scores[4][1] < Fraction(1, 10)
    assert [i for i,v in enumerate(count) if v == 1] == [8, 40]
    total_upper = sum(hi*mean for _,_,(_,hi),_,mean in family)
    avg_upper = sum(weights[d]*scores[d][1] for d in weights)
    selected = min(scores, key=lambda d: scores[d][1])
    assert scores[selected][1] <= avg_upper <= total_upper
    return dict(test="physical_three_window_selector", prime=97, terminal=terminal,
                x="even primary face at both zero anchors", mass_cutoff="7/50",
                order_cutoff="2/a", candidates=[[h,i] for h,i,*_ in family],
                persistent_all_three=[i for i,v in enumerate(count) if v==1],
                max_joint_bounds={str(d):list(map(str, bounds)) for d,bounds in scores.items()},
                selected_length=selected, sum_of_coset_mean_score_upper=str(total_upper),
                precision_bits=ctx.prec)


if __name__ == "__main__":
    for result in (quotient_patterns(), physical_windows()):
        print(json.dumps(result, sort_keys=True))
