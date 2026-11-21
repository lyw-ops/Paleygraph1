"""Check an unforced all-height packet invariant with additional signed GL3 returns."""
import json
import runpy
from collections import defaultdict
from math import comb
from pathlib import Path

from flint import acb, arb

HERE = Path(__file__).resolve().parent
r84 = runpy.run_path(str(HERE / "astra-imaginary-84-check.py"))
fields = r84["fields"]
rank_three = r84["rank_three"]
unit = r84["UNIT"]
tags = [
    (1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1),
    (1, 1, 0, 0), (0, 0, 1, 1), (1, 0, 1, 0), (0, 1, 0, 1),
]


def signed_upper(t):
    rows, params = inherited_upper(t)
    _, beta, groups, amended = rank_three["coefficients"](
        t, acb(fields["prev"]["da"]), acb(fields["prev"]["db"]))
    gamma = arb(499) / 500 * beta * groups[1, 1][0, 0]
    for tag in tags:
        powers = rank_three["rank_powers"](4)
        shifts = [[(shape[-1], mult) for shape, mult in terms.items()
                   if shape[:4] == tag] for terms in powers]
        cols = []
        for r in range(9):
            col = defaultdict(lambda: acb(0))
            for l, terms in enumerate(shifts):
                if not terms:
                    continue
                for k in range(10):
                    src = amended[k] if r+l == 0 and k in amended else groups[r+l, k]
                    weight = comb(r+l, r) * (beta/4)**l / (2 if k else 1)
                    for (u, v), coeff in src.items():
                        if u+v > 5:
                            continue
                        if (r, l, k, u, v) == (0, 1, 1, 0, 0):
                            coeff = coeff / 500
                        for e, mult in terms:
                            for side in ((-k, k) if k else (0,)):
                                col[u, v, e+side] += coeff * weight * mult
            cols.append(col)
        for j in range(7):
            debit = defaultdict(lambda: arb(0))
            for (u, v, e), first in cols[j].items():
                second = cols[j+2].get((u, v, e), 0) * comb(j+2, 2) * gamma**2 / 8
                if not second:
                    continue
                gain = r84["cancellation"](first, acb(second))
                if not gain:
                    continue
                for w, mult in rank_three["pair_fiber"](*tag):
                    for k in range(-2*u, 2*u+1, 4):
                        debit[w+k-e] += (v+1) * mult * gain
            for k in range(len(rows[j])):
                saved = (2 * min(debit[k].lower(), debit[-k].lower())
                         if k else debit[0].lower())
                rows[j][k] -= saved
                assert rows[j][k] >= 0
    return rows, params


# Reuse the previous arithmetic proof and slab assembly. Patch only its callable
# in this private runpy-loaded module. The original function does not call itself.
inherited_upper = r84["signed_upper"]
r84["envelope"].__globals__["signed_upper"] = signed_upper


def verify(lo, hi, nx, caps):
    mid = (hi+lo)*unit/2
    half = (hi-lo)*unit/2
    data = r84["envelope"](mid, half, unit, nx, 1, arb(1))
    old = r84["prior"]
    frozen = [arb(x) / 10**20 for x in caps]
    out, leak, cap = old["image"](mid, half, data, frozen)
    assert leak >= 0
    leak += sum(max(arb(0), (x-y).upper())*(k*old["eta"]).cosh()
                for k, (x, y) in enumerate(zip(out, frozen), 1))
    leak += arb(1)/10**12
    imag = cap-arb("2.8284")
    ratio = cap/(4*lo*unit+cap**2-2*imag**2).sqrt()
    assert leak < old["EPS"] and cap < arb("4.654") and ratio < arb(".526")
    print(json.dumps(dict(real_endpoints_units=[lo, hi], imaginary_halfwidth_units=1,
                          real_cells=nx, tilted_excess=str(leak), coordinate_cap=str(cap),
                          secant_rate=str(ratio), field_minimum_n="10^30")), flush=True)


if __name__ == "__main__":
    dataset = json.loads((HERE/"astra-depth-95-caps.json").read_text())
    for entry in dataset:
        verify(*entry)
    # The same frozen coldest box with these eight pools removed.
    r84["envelope"].__globals__["signed_upper"] = inherited_upper
    lo, hi, nx, caps = dataset[0]
    mid, half = (lo+hi)*unit/2, (hi-lo)*unit/2
    data = r84["envelope"](mid, half, unit, nx, 1, arb(1))
    frozen = [arb(x)/10**20 for x in caps]
    out, _, _ = r84["prior"]["image"](mid, half, data, frozen)
    excess = out[0]-frozen[0]
    assert excess > arb("1e-8")
    print(json.dumps(dict(comparison="same coldest cap without eight new pools",
                          first_packet_overrun=str(excess))), flush=True)
