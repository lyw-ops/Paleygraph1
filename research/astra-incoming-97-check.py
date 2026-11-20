"""Arb replay for additional rank-four returns and the real incoming secants."""
from collections import defaultdict
from math import comb
from pathlib import Path
import json
import runpy

from flint import acb, arb

HERE = Path(__file__).resolve().parent
r96 = runpy.run_path(str(HERE / "astra-paired-96-check.py"))
r84 = r96["r84"]
p3 = r96["p3"]
fields = r96["fields"]
unit = r96["unit"]
known = set(r96["tags"])
tags = {shape[:4] for p in p3["rank_powers"](4) for shape in p}
tags.remove((0, 0, 0, 0))


def signed_upper(t):
    rows, pars = r96["signed_upper"](t)
    _, beta, groups, amend = p3["coefficients"](
        t, acb(fields["prev"]["da"]), acb(fields["prev"]["db"]))
    gamma = arb(499)/500*beta*groups[1, 1][0, 0]
    F = r84["F"]
    debits = [defaultdict(lambda: arb(0)) for _ in range(7)]
    for tag in sorted(tags):
        data = r96["columns"](groups, amend, beta, tag)
        fiber = p3["pair_fiber"](*tag)
        for j, debit in enumerate(debits):
            for h in (0, 1):
                if j+h+2 > 8 or (h == 0 and tag in known):
                    continue
                scale = (j+1)*gamma if h else acb(1)
                extra = comb(j+h+2, j)*gamma**(h+2)*(3 if h else 1)/8
                s = defaultdict(lambda: arb(0))
                for (u,v,e), x in data[j+h].items():
                    y = data[j+h+2].get((u,v,e))
                    if y is None:
                        continue
                    gain = r84["cancellation"](scale*x, extra*y)
                    if gain:
                        for b in range(-2*u,2*u+1,4):
                            s[b-e] += (v+1)*gain
                if h:
                    s = {k:sum(F[a+4]*s.get(k-a,0) for a in range(-4,5))
                         for k in range(min(s, default=0)-4,max(s, default=0)+5)}
                for k, x in s.items():
                    for w, m in fiber:
                        debit[k+w] += m*x
    for j,debit in enumerate(debits):
        for k in range(len(rows[j])):
            saved = 2*min(debit[k].lower(),debit[-k].lower()) if k else debit[0].lower()
            rows[j][k] -= saved
            assert rows[j][k] >= 0
    return rows, pars


r84["envelope"].__globals__["signed_upper"] = signed_upper

if __name__ == "__main__":
    four = r84["rank_four"]
    cubic = four["four_powers"](3)
    assert all(cubic[label] >= 24 for label in four["four_powers"](1))
    assert four["four_powers"](2)[four["ZERO"], 0] == 8
    caps = json.loads((HERE / "astra-incoming-97-caps.json").read_text())
    for row in caps:
        r96["previous"]["verify"](*row)
    r84["envelope"].__globals__["signed_upper"] = r96["signed_upper"]
    lo,hi,nx,cap = caps[0]
    mid,half = (lo+hi)*unit/2,(hi-lo)*unit/2
    data = r84["envelope"](mid,half,unit,nx,1,arb(1))
    frozen = [arb(x)/10**20 for x in cap]
    extra = r84["prior"]["image"](mid,half,data,frozen)[0][0]-frozen[0]
    assert extra > r84["prior"]["EPS"]
    print(json.dumps(dict(kind="previous_first_packet_overrun",excess=str(extra))),flush=True)
    L = arb(2031)/128 - arb(1)/2**17
    q = arb("0.8")
    a = q.sqrt()
    r = arb("0.169724")*arb("0.51358")**600
    r_lim = 4*arb("0.428236")**600
    X = arb("4.768")
    assert (X+arb("0.010955"))/(4*L+(X+arb("0.010955"))**2).sqrt() < arb("0.515")
    b = arb(4)
    d = (X+b)/(4*L+(X+b)**2).sqrt()
    c = arb("6.15")**2*(4*arb(10)**695).sqrt()*r**2/b**2
    threshold = (q*q-d*d)/(q*(1-d*d))
    assert c < threshold
    linear = arb("0.010955")/(1-arb("0.984138"))
    entrance = 4*L.sqrt()-X
    def erasure(size, residual):
        return 178*arb("1.514")*size.sqrt()*residual/(1-a)
    cost = erasure(arb(10)**434, r_lim)
    assert entrance-linear-cost > arb("9.4")
    assert (entrance-linear-cost)/178 > arb(".0528")
    assert entrance-linear-erasure(arb(10)**342,r) > arb("9.4")
    print(json.dumps(dict(kind="incoming_real_secant",max_prime="4e695",
        high_compression=str(c),allowed_compression=str(threshold),
        first_exit=str(entrance),frozen_linear_cap=str(linear),
        prime_limsup_erased_cost=str(cost),
        signed_exterior_lower=str(entrance-linear-cost))),flush=True)
