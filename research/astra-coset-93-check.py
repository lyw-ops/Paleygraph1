"""Check restricted-sign critical divisors, the cycle algebra and a physical mask."""
from fractions import Fraction
from math import isqrt
from pathlib import Path
import json
import runpy
import sys

from flint import arb, ctx, fmpq

base = Path(__file__).resolve().parent
sys.path.insert(0, str(base.parent))
from theta import paley_sign

prior = runpy.run_path(str(base / "astra-quotient-75-check.py"))
ctx.prec = 192


def enclosure(x):
    return [int((10**9 * x).lower().floor().unique_fmpz()),
            int((10**9 * x).upper().ceil().unique_fmpz())]


def cycle_constants():
    caps = {}
    for g in (5, 7, 9):
        c = arb.cos_pi_fmpq(fmpq(1, g))
        caps[g] = enclosure(c / (1+c))
    s = 1 / arb(2).sqrt()
    density = (2 - s) / 6
    corr = 2 * arb.cos_pi_fmpq(fmpq(1, 9)) - arb.cos_pi_fmpq(fmpq(4, 9))
    assert density * 11 > 2 and density * 10 > 2 and density * 14 > 3
    assert 2 * density * corr > s
    w = arb(4627)/10000
    r = w/(1-w)
    margin = (2-arb(2).sqrt()*w)/3*(2*r-((1-r)/2).sqrt()) - arb(2).sqrt()*w
    assert margin > arb(1)/10**6
    return dict(test="index_nine_and_cycles", quotient_cap_test="4627/10000",
                positive_margin=enclosure(margin), caps=caps, minimum_density=enclosure(density),
                required_twisted_coefficient=enclosure(2*density*corr),
                available_coefficient=enclosure(s), units="1e-9", precision_bits=ctx.prec)


def find_clique(h, forbidden, target):
    neighbors = [sum(1 << ((j+z) % h) for z in forbidden) for j in range(h)]
    best = [0]
    for z in sorted(forbidden):
        clique = [0, z]
        choices = neighbors[0] & neighbors[z]
        while choices and len(clique) < target:
            remaining = choices
            top, top_count = -1, -1
            while remaining:
                bit = remaining & -remaining
                j = bit.bit_length() - 1
                count = (choices & neighbors[j]).bit_count()
                if count > top_count:
                    top, top_count = j, count
                remaining -= bit
            clique.append(top)
            choices &= neighbors[top]
        if len(clique) > len(best):
            best = clique
        if len(best) >= target:
            break
    assert len(set(best)) == len(best)
    assert all((x-y) % h in forbidden for x in best for y in best if x != y)
    return best


def prime_sweep(limit=3000):
    counts = dict(total=0, clique=0, quotient=0)
    survivors = []
    exceptions = []
    for p in range(5, limit+1, 4):
        if any(p % j == 0 for j in range(3, isqrt(p)+1, 2)):
            continue
        n = (p-1)//2
        cp = (1 + isqrt(1+4*n))//2
        signs = paley_sign(p)
        for h in range(2*cp+1, min(n-1, isqrt(36*n))+1):
            if n % h:
                continue
            restricted = signs[::n//h]
            for sigma in (-1, 1):
                counts["total"] += 1
                F = {j for j, v in enumerate(restricted) if v == -sigma}
                target = isqrt((h*h-1)//n) + 1
                clique = find_clique(h, F, target)
                if len(clique)**2 * n >= h*h:
                    counts["clique"] += 1
                    continue
                opposite = prior["lower_theta"](restricted, -sigma)
                upper = Fraction(h, 1) / opposite
                if upper**2 <= n:
                    counts["quotient"] += 1
                    exceptions.append([p, h, sigma, str(upper)])
                else:
                    survivors.append([p, h, sigma, str(upper)])
    assert counts["total"] == counts["clique"] + counts["quotient"] + len(survivors)
    return dict(test="all_divisors", limit=limit, range="2 c_p < h <= 6 sqrt(n), h proper",
                counts=counts, quotient_closures=exceptions, unresolved=survivors)


def actual_mask():
    delayed = runpy.run_path(str(base / "astra-quartic-89-check.py"))
    ctx.prec = 384
    signs = list(map(int, delayed["face"]["mask"]))
    b, masks, heights = delayed["delayed_masks"](signs)
    K = [0, 16, 32]
    C = [8, 24, 40]
    D = sorted(set(C) & set(masks[8]))
    assert b == 11 and D == [8, 40] and not set(K).intersection(masks[8])
    restricted = paley_sign(97)[::6]
    lower = prior["lower_theta"](restricted, 1)
    upper = Fraction(len(restricted), 1) / prior["lower_theta"](restricted, -1)
    mass_score = Fraction(len(D), len(C)*2*len(restricted))
    assert Fraction(97630, 10**6) < mass_score*lower <= mass_score*upper < Fraction(97632, 10**6)
    h = sum((heights[i].max(0) for i in C), arb(0)) / len(C)
    # The central restricted minus graph is triangle-free but contains a five-cycle.
    F = {j for j,s in enumerate(signs[::3]) if s == 1}
    assert all((x-y) % 16 not in F for x in F for y in F)
    cycle = [0, 6, 12, 2, 9]
    assert all((i-j)%16 in F for i,j in zip(cycle,cycle[1:]+cycle[:1]))
    return dict(test="actual_physical_mask", prime=97, terminal=b, length=8,
                K=K, C=C, P_intersection_C=D, central_score=0,
                outer_joint_score_lower=str(mass_score*lower), outer_joint_score_upper=str(mass_score*upper),
                outer_mean_positive_height=enclosure(h), forbidden_minus_five_cycle=cycle,
                precision_bits=ctx.prec, height_units="1e-9")


if __name__ == "__main__":
    for result in (cycle_constants(), prime_sweep(), actual_mask()):
        print(json.dumps(result, sort_keys=True))
