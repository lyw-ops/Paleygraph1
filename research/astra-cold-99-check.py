"""Outward replay for shifted rank-four returns and disjoint outer and inner pools."""
from collections import defaultdict
from math import comb
from pathlib import Path
import json
import runpy

from flint import acb, arb, arb_poly

HERE = Path(__file__).resolve().parent
r98 = runpy.run_path(str(HERE / "astra-exit-98-check.py"))
r97 = r98["prev"]
r96 = r98["r96"]
r95 = r96["previous"]
r84 = r98["r84"]
fields = r98["fields"]
four = r98["four"]
unit = r98["unit"]
shapes = r98["double_shapes"]
quartic = four["four_powers"](4)
for shape, shifts in shapes.items():
    assert {s: m for (f, s), m in quartic.items() if f == shape} == {
        s: 48 for s, m in shifts}
    assert shifts[1][0]-shifts[0][0] == 2


# The eight degree-one standards have 24 copies at their own shifts in
# degree three and one additional copy each, sometimes at a different shift.
extra_standard = defaultdict(lambda: defaultdict(int))
cubic = four["four_powers"](3)
for (shape, d), mult in four["four_powers"](1).items():
    assert mult == 1
    shifts = {b: m-24*(b==d) for (s,b),m in cubic.items() if s==shape}
    assert sum(shifts.values()) == 1 and min(shifts.values()) >= 0
    other = next(b for b,m in shifts.items() if m)
    for w,m in four["four_fiber"](shape).items():
        extra_standard[d-other][w-d] += m


def collect_rank_four(t, rows):
    p3 = r98["p3"]
    _, beta, groups, amend = p3["coefficients"](
        t, acb(fields["prev"]["da"]), acb(fields["prev"]["db"]))
    gamma = arb(499)/500 * beta * groups[1, 1][0, 0]
    fibers = defaultdict(int)
    for shape, ((a, _), _) in shapes.items():
        for w, count in four["four_fiber"](shape).items():
            fibers[w-a] += count
    for tag in [r96["trivial"], *sorted(r97["tags"])]:
        cols = r96["columns"](groups, amend, beta, tag)
        for j in range(6):
            by_site = defaultdict(lambda: arb(0))
            a1 = (j+1)*gamma/8
            a3 = comb(j+3,3)*gamma**3/512
            for step, fiber in extra_standard.items():
                partial = defaultdict(lambda: arb(0))
                for (u,v,source_e), x in cols[j+3].items():
                    e = source_e-step
                    if j == 0 and tag == r96["trivial"] and u==v==0 and abs(e)==1:
                        continue
                    base = a1*cols[j+1].get((u,v,e), acb(0))
                    base += 24*a3*cols[j+3].get((u,v,e), acb(0))
                    gain = r84["cancellation"](base, a3*x)
                    if gain:
                        for k in range(-2*u,2*u+1,4):
                            partial[k-e] += (v+1)*gain
                for site,x in partial.items():
                    for w,m in fiber.items():
                        by_site[site+w] += x*m
            debit = defaultdict(lambda: arb(0))
            for site,x in by_site.items():
                for w,m in p3["pair_fiber"](*tag):
                    debit[site+w] += x*m
            for k in range(len(rows[j])):
                saved = 2*min(debit[k].lower(),debit[-k].lower()) if k else debit[0].lower()
                rows[j][k] -= saved
                assert rows[j][k] >= 0
        for j in range(5):
            quad = comb(j+2, 2)*gamma**2/64
            fourth = comb(j+4, 4)*gamma**4*48/4096
            by_site = defaultdict(lambda: arb(0))
            # A source of exponent i can reach e=i or e=i+2 before the
            # smaller physical shift is added. Keep their union, including endpoints.
            keys = set(cols[j+4])
            keys.update((u,v,e+2) for u,v,e in cols[j+4])
            for u, v, e in keys:
                high = cols[j+4].get((u,v,e), acb(0))
                low = cols[j+4].get((u,v,e-2), acb(0))
                pair = cols[j+2].get((u,v,e), acb(0)) + cols[j+2].get((u,v,e-2), acb(0))
                gain = (abs(fourth).lower()*r84["cancellation"](high, low)
                        + r84["cancellation"](quad*pair, fourth*(high+low)))
                if gain:
                    for k in range(-2*u, 2*u+1, 4):
                        by_site[k-e] += (v+1)*gain
            debit = defaultdict(lambda: arb(0))
            for s, a in by_site.items():
                for w, m in p3["pair_fiber"](*tag):
                    for k, count in fibers.items():
                        debit[s+w+k] += a*m*count
            for k in range(len(rows[j])):
                saved = 2*min(debit[k].lower(),debit[-k].lower()) if k else debit[0].lower()
                rows[j][k] -= saved
                assert rows[j][k] >= 0


def signed_upper(t):
    # Snapshot the three positive envelopes during the *same* evaluation.
    # The difference across R96 is excluded because it already uses later inputs.
    snapshots = {}
    hooks = [(r84["fields"], "upper", "native"),
             (r96["previous"], "signed_upper", "95"),
             (r97["r96"], "signed_upper", "96")]
    originals = []
    for obj, key, name in hooks:
        original = obj[key]
        originals.append(original)
        def save(t, fn=original, label=name):
            rows, pars = fn(t)
            snapshots[label] = [list(row) for row in rows[:7]]
            return rows, pars
        obj[key] = save
    try:
        rows, pars = r98["signed_upper"](t)
    finally:
        for (obj, key, _), original in zip(hooks, originals):
            obj[key] = original
    collect_rank_four(t, rows)
    # Only zero-later savings are copied to a single future child. At outer
    # arity zero omit the two possible native mixed Legendre amendments.
    savings = []
    for j in range(7):
        savings.append([max(arb(0), (a-b+c-d).lower()) for a,b,c,d in zip(
            snapshots["native"][j], snapshots["95"][j], snapshots["96"][j], rows[j])])
    _, beta, groups, amend = r98["p3"]["coefficients"](
        t, acb(fields["prev"]["da"]), acb(fields["prev"]["db"]))
    gamma = arb(499)/500*beta*groups[1,1][0,0]
    delta = -2*gamma*fields["kern"]["linear_scalar"](groups,beta)
    z = fields["old"]["prefix"](t)[0]
    w = fields["joint"]["coefficient"](t,0,2,0)
    v = fields["selected"](t)
    for j in range(6):
        source = r84["prior"]["symmetric"](savings[j+1])
        child = abs(delta).lower()*fields["kern"]["G"]
        child += abs(v).lower()*fields["field"].left_shift(1)
        if j:
            child += abs(z).lower()*fields["old"]["R"].left_shift(3)
            child += abs(w).lower()*fields["field"].left_shift(1)
        offset = len(savings[j+1])-1 + 5
        gain = source*child*(j+1)
        for k in range(len(rows[j])):
            rows[j][k] -= (2 if k else 1)*gain[offset+k].lower()
            assert rows[j][k] >= 0
    # Previously positive rank-three complement. Contract its two W children
    # to the arithmetic unit and propagate this independent debit through
    # every outer child of the native positive polynomial.
    p3 = r98["p3"]
    assert p3["rank_powers"](2)[2][(0,0,0,0,0)] == 4
    center = abs(gamma).lower()*r84["F"].left_shift(1) + abs(delta).lower()*fields["kern"]["G"]
    center += abs(z).lower()*fields["old"]["R"].left_shift(3)
    center += (abs(w).lower()+abs(v).lower())*fields["field"].left_shift(1)
    powers = [arb_poly([1])]
    for _ in range(26):
        powers.append(powers[-1]*center)
    for r in range(27):
        debit = defaultdict(lambda: arb(0))
        for k in range(27-r):
            direct_coeffs = amend[k] if r==0 and k in amend else groups[r,k]
            for (u,vv), direct in direct_coeffs.items():
                if r<=8 and k<=9 and u+vv<=5:
                    continue
                second = groups[r+2,k].get((u,vv))
                if second is None:
                    continue
                gain = r84["cancellation"](direct,comb(r+2,2)*beta**2/4*second)
                for b in range(-2*u,2*u+1,4):
                    for e in ((-k,k) if k else (0,)):
                        debit[b-e] += (vv+1)*gain/(2 if k else 1)
        if not debit:
            continue
        radius = max(map(abs,debit))
        base = arb_poly([min(debit[i].lower(),debit[-i].lower())
                         for i in range(-radius,radius+1)])
        for j in range(r+1):
            h = r-j
            gain = comb(r,j)*base*powers[h]
            for k in range(len(rows[j])):
                rows[j][k] -= (2 if k else 1)*gain[radius+5*h+k].lower()
                assert rows[j][k]>=0
    return rows, pars


r84["envelope"].__globals__["signed_upper"] = signed_upper

if __name__ == "__main__":
    caps = json.loads((HERE / "astra-cold-99-caps.json").read_text())
    for row in caps:
        r95["verify"](*row)
    r84["envelope"].__globals__["signed_upper"] = r98["signed_upper"]
    lo, hi, nx, cap = caps[0]
    mid, half = (lo+hi)*unit/2, (hi-lo)*unit/2
    data = r84["envelope"](mid, half, unit, nx, 1, arb(1))
    frozen = [arb(x)/10**20 for x in cap]
    overrun = r84["prior"]["image"](mid, half, data, frozen)[0][0]-frozen[0]
    assert overrun > r84["prior"]["EPS"]
    print(json.dumps(dict(kind="previous_first_packet_overrun", excess=str(overrun),
                          exterior_quartic_shifts=[[a for a,m in ss] for ss in shapes.values()],
                          multiplicity_per_shift=48)),flush=True)
