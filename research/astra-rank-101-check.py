"""Arb192 arithmetic proof for four linear/cubic later-center returns."""
from collections import Counter, defaultdict
from math import comb
from pathlib import Path
import json
import runpy

from flint import acb, arb, arb_poly

HERE = Path(__file__).resolve().parent
r100 = runpy.run_path(str(HERE / "astra-return-100-check.py"))
r99 = r100["r99"]
p3, r84, fields, unit = (r100[key] for key in ("p3", "r84", "fields", "unit"))
zero = r100["scalar"]
tags = [zero, *sorted(r99["r97"]["tags"])]


def rank_five_control():
    # Use signatures of rational GL representations directly. Equal signatures
    # include the central character and therefore the arithmetic determinant.
    ranks = (6,6,5,5,5,5,7,7)
    empty = tuple((0,)*d for d in ranks)
    def step(previous):
        counts = Counter()
        for shapes, m in previous.items():
            for i, shape in enumerate(shapes):
                for a in range(len(shape)):
                    for sign in (-1,1):
                        changed = list(shape)
                        changed[a] += sign
                        if changed != sorted(changed, reverse=True):
                            continue
                        counts[shapes[:i]+(tuple(changed),)+shapes[i+1:]] += m
        return counts
    linear = step({empty:1})
    cubic = step(step(linear))
    assert len(linear) == 16 and set(cubic[k] for k in linear) == {48}
    return len(linear)


def signed_upper(t):
    # Round 99 passes its six explicitly debited one-child source rows to
    # symmetric(), after excluding the two-child debit of round 96.
    # Tap precisely those calls, within that invocation only.
    sources = []
    globals99 = r99["signed_upper"].__globals__
    prior = r84["prior"]
    symmetric = prior["symmetric"]
    signed99 = r100["r99"]["signed_upper"]
    def snapshot99(box):
        def save(row):
            source = symmetric(row)
            sources.append((source, len(row)-1))
            return source
        prior["symmetric"] = save
        try:
            return signed99(box)
        finally:
            prior["symmetric"] = symmetric
    assert globals99["r84"]["prior"] is prior
    r100["r99"]["signed_upper"] = snapshot99
    try:
        rows, params = r100["signed_upper"](t)
    finally:
        r100["r99"]["signed_upper"] = signed99
    assert [radius for _, radius in sources] == [5*(28-r) for r in range(1,7)]
    _, beta, groups, amended = p3["coefficients"](
        t, acb(fields["prev"]["da"]), acb(fields["prev"]["db"]))
    gamma = arb(499)/500 * beta * groups[1,1][0,0]
    delta = -2*gamma*fields["kern"]["linear_scalar"](groups,beta)
    z = fields["old"]["prefix"](t)[0]
    w = fields["joint"]["coefficient"](t,0,2,0)
    v = fields["selected"](t)
    square = delta**2/16 + z**2 + 2*w**2 + 2*v**2
    linear = abs(delta).lower()*fields["kern"]["G"]
    linear += abs(z).lower()*fields["old"]["R"].left_shift(3)
    linear += (abs(w).lower()+abs(v).lower())*fields["field"].left_shift(1)
    # All two-child terms except arithmetic units. Use the exact same lower
    # amplitudes for the power and its unit so coefficients stay monotone.
    quadratic = linear**2
    quadratic[10] -= (abs(delta).lower()**2/16 + abs(z).lower()**2
                      + 2*abs(w).lower()**2 + 2*abs(v).lower()**2)
    assert all(x >= 0 for x in quadratic.coeffs())
    for r, (source, radius) in enumerate(sources, 1):
        if r < 2:
            continue
        j = r-2
        gain = comb(r,2)*source*quadratic
        for k in range(len(rows[j])):
            rows[j][k] -= (2 if k else 1)*gain[radius+10+k].lower()
            assert rows[j][k] >= 0
    gains = [defaultdict(lambda: arb(0)) for _ in range(6)]
    for tag in tags:
        cols = r99["r96"]["columns"](groups, amended, beta, tag)
        scalar = []
        for r in range(1,9):
            column = defaultdict(lambda: acb(0), cols[r])
            if r+2 <= 8:
                wt = comb(r+2,2)*gamma**2/8
                for key, value in cols[r+2].items():
                    column[key] += wt*value
            if r+4 <= 8:
                wt = comb(r+4,4)*gamma**4/4096
                for (u,vv,e), value in cols[r+4].items():
                    for shift,mult in ((-2,2),(0,196),(2,2)):
                        column[u,vv,e+shift] += wt*mult*value
            scalar.append(column)
        for j in range(6):
            sums = defaultdict(lambda: arb(0))
            for (u,vv,e), c3 in scalar[j+2].items():
                if j==0 and tag==zero and e==0 and (u,vv) in ((0,1),(1,0)):
                    continue   # Native R and D root linear/cubic collections.
                c1 = scalar[j].get((u,vv,e))
                if c1 is None:
                    continue
                gain = r84["cancellation"]((j+1)*c1, 3*comb(j+3,3)*square*c3)
                if gain:
                    for b in range(-2*u,2*u+1,4):
                        sums[b-e] += (vv+1)*gain
            for k,x in sums.items():
                for b,num in p3["pair_fiber"](*tag):
                    gains[j][k+b] += x*num
    for j, gains_j in enumerate(gains):
        radius = max(map(abs,gains_j), default=0)
        base = arb_poly([min(gains_j[k].lower(),gains_j[-k].lower())
                         for k in range(-radius,radius+1)])
        gain = base*linear
        for k in range(len(rows[j])):
            rows[j][k] -= (2 if k else 1)*gain[radius+5+k].lower()
            assert rows[j][k] >= 0
    return rows, params


r84["envelope"].__globals__["signed_upper"] = signed_upper

if __name__ == "__main__":
    assert rank_five_control() == 16
    caps = json.loads((HERE/"astra-rank-101-caps.json").read_text())
    for entry in caps:
        r99["r95"]["verify"](*entry)
    lo, hi, nx, cap = caps[0]
    mid, half = (lo+hi)*unit/2, (hi-lo)*unit/2
    r84["envelope"].__globals__["signed_upper"] = r100["signed_upper"]
    previous = r84["envelope"](mid, half, unit, nx, 1, arb(1))
    frozen = [arb(x)/10**20 for x in cap]
    out = r84["prior"]["image"](mid, half, previous, frozen)[0]
    excess, packet = max(((out[k]-frozen[k]).lower(), k+1) for k in range(len(frozen)))
    assert excess > r84["prior"]["EPS"]
    t = acb(arb(mid,half),arb(0,unit))
    _, beta, g, am = p3["coefficients"](t, acb(fields["prev"]["da"]), acb(fields["prev"]["db"]))
    gamma = arb(499)/500 * beta * g[1,1][0,0]
    delta = -2*gamma*fields["kern"]["linear_scalar"](g,beta)
    col = r99["r96"]["columns"](g,am,beta,zero)
    def scalar_at_one(r):
        return (col[r][0,0,1]+comb(r+2,2)*gamma**2/8*col[r+2][0,0,1]
                + comb(r+4,4)*gamma**4/4096*(196*col[r+4][0,0,1]
                  +2*col[r+4][0,0,-1]+2*col[r+4][0,0,3]))
    witness = r84["cancellation"](delta*scalar_at_one(1),3*delta**3/16*scalar_at_one(3))
    assert witness > arb("3.57e-10")
    print(json.dumps(dict(kind="before_linear_cubic_collection",
                          rank_five_standards=16, matching_cubic_copies=48,
                          previous_packet=packet, previous_overrun_lower=str(excess),
                          pure_G_normalized_saving=str(witness))), flush=True)
