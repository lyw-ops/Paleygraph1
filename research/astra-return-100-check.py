"""Arb192 replay for rank-three returns and repeated rank-four determinant shifts."""
import json
import runpy
from collections import Counter, defaultdict
from math import comb
from pathlib import Path

from flint import acb, arb, arb_poly

HERE = Path(__file__).resolve().parent
r99 = runpy.run_path(str(HERE / "astra-cold-99-check.py"))
r84, fields = r99["r84"], r99["fields"]
p3 = r99["r98"]["p3"]
unit = r99["unit"]
powers = p3["rank_powers"](4)
scalar = (0, 0, 0, 0)
standards = {label[:4] for label in powers[1]}
labels = [scalar, *sorted(standards)]
shifts = {tag: [[(s[-1], count) for s, count in terms.items() if s[:4] == tag]
                for terms in powers] for tag in labels}
assert dict(shifts[scalar][3]) == {-1: 2, 1: 2}
assert dict(shifts[scalar][4]) == {0: 48}


four = r99["four"]
families = {}
shape_counts = Counter()
for h in (3, 4):
    lower_shapes = {s for m in range(h) for s, d in four["four_powers"](m)}
    higher = defaultdict(list)
    for (s, d), n in four["four_powers"](h).items():
        if s not in lower_shapes:
            higher[s].append((d, n))
    for s, subset in higher.items():
        if len(subset) < 2:
            continue
        shape_counts[h, len(subset)] += 1
        ordered = sorted(subset)
        d0 = ordered[0][0]
        pattern = tuple((d-d0, n) for d, n in ordered)
        f = families.setdefault((h, pattern), Counter())
        for w, mult in four["four_fiber"](s).items():
            f[w-d0] += mult


assert shape_counts == {(3, 2): 16, (4, 2): 76, (4, 3): 3}


def collect_outer(rows, beta, groups, amended, gamma, later):
    debits = [defaultdict(lambda: arb(0)) for _ in range(6)]
    for tag in [scalar, *sorted(r99["r97"]["tags"])]:
        columns = r99["r96"]["columns"](groups, amended, beta, tag)
        for (h, pattern), boundary in families.items():
            for j in range(9-h):
                col = columns[j+h]
                # A displaced source can reach an exponent absent at the first shift.
                keys = {(u,v,e+shift) for u,v,e in col for shift, _ in pattern}
                aggregate = defaultdict(lambda: arb(0))
                scale = comb(j+h, h)*abs(gamma/8).lower()**h
                for u,v,e in keys:
                    terms = [n*col[u,v,e-shift] for shift,n in pattern if (u,v,e-shift) in col]
                    if len(terms) < 2:
                        continue
                    total = terms[0]
                    saving = arb(0)
                    for term in terms[1:]:
                        saving += r84["cancellation"](total, term)
                        total += term
                    if saving:
                        for k in range(-2*u,2*u+1,4):
                            aggregate[k-e] += (v+1)*saving
                for k, gain in aggregate.items():
                    for w, m in p3["pair_fiber"](*tag):
                        for a, mult in boundary.items():
                            debits[j][k+w+a] += scale*gain*m*mult
    for r, deb in enumerate(debits):
        if not deb:
            continue
        radius = max(map(abs,deb))
        base = arb_poly([min(deb[i].lower(),deb[-i].lower()) for i in range(-radius,radius+1)])
        for j in range(r+1):
            h = r-j
            gain = comb(r,j)*base*later**h
            for k in range(len(rows[j])):
                rows[j][k] -= (2 if k else 1)*gain[radius+5*h+k].lower()
                assert rows[j][k] >= 0


def signed_upper(t):
    rows, params = r99["signed_upper"](t)
    _, beta, groups, amended = p3["coefficients"](
        t, acb(fields["prev"]["da"]), acb(fields["prev"]["db"]))
    gamma = arb(499)/500 * beta * groups[1, 1][0, 0]
    delta = -2*gamma*fields["kern"]["linear_scalar"](groups, beta)
    z = fields["old"]["prefix"](t)[0]
    w = fields["joint"]["coefficient"](t, 0, 2, 0)
    v_amp = fields["selected"](t)
    later = abs(delta).lower()*fields["kern"]["G"] + abs(z).lower()*fields["old"]["R"].left_shift(3)
    later += (abs(w).lower()+abs(v_amp).lower())*fields["field"].left_shift(1)
    center = abs(gamma).lower()*r84["F"].left_shift(1) + later
    collect_outer(rows, beta, groups, amended, gamma, later)
    outer = [arb_poly([1])]
    for _ in range(26):
        outer.append(outer[-1]*center)
    for r in range(27):
        debits = defaultdict(lambda: arb(0))
        for tag in labels:
            accumulated = {}
            leg_fiber = defaultdict(lambda: arb(0))
            for h, terms in enumerate(shifts[tag]):
                if not terms or r+h > 28:
                    continue
                weight = comb(r+h, r)*(beta/4)**h
                for k in range(29-r-h):
                    source = amended[k] if r+h == 0 and k in amended else groups[r+h, k]
                    for (u, v), value in source.items():
                        if r <= 8 and k <= 9 and u+v <= 5:
                            continue
                        amount = value*weight/(2 if k else 1)
                        for d, m in terms:
                            term = amount*m
                            for e in ((d-k, d+k) if k else (d,)):
                                key = (u,v,e)
                                if key in accumulated:
                                    # R99 already used the degree-zero/two scalar saving.
                                    if tag != scalar or h > 2:
                                        gain = r84["cancellation"](accumulated[key], term)
                                        if gain:
                                            for b in range(-2*u, 2*u+1, 4):
                                                leg_fiber[b-e] += (v+1)*gain
                                    accumulated[key] += term
                                else:
                                    accumulated[key] = term
            for s, value in leg_fiber.items():
                for b, count in p3["pair_fiber"](*tag):
                    debits[s+b] += count*value
        if not debits:
            continue
        radius = max(map(abs, debits))
        base = arb_poly([min(debits[k].lower(), debits[-k].lower())
                         for k in range(-radius, radius+1)])
        for j in range(r+1):
            h = r-j
            saved = comb(r,j)*base*outer[h]
            for k in range(len(rows[j])):
                rows[j][k] -= (2 if k else 1)*saved[radius+5*h+k].lower()
                assert rows[j][k] >= 0
    return rows, params


r84["envelope"].__globals__["signed_upper"] = signed_upper

if __name__ == "__main__":
    caps = json.loads((HERE / "astra-return-100-caps.json").read_text())
    for entry in caps:
        r99["r95"]["verify"](*entry)
    lo, hi, nx, cap = caps[0]
    mid, half = (lo+hi)*unit/2, (hi-lo)*unit/2
    t = acb(arb(mid, half), arb(0, unit))
    _, beta, groups, _ = p3["coefficients"](t, acb(fields["prev"]["da"]), acb(fields["prev"]["db"]))
    # Self-reflected arithmetic fiber (r,u,v,e)=(12,0,0,0), outside the prefix.
    direct = groups[12,0][0,0] + comb(14,2)*beta**2/4*groups[14,0][0,0]
    cubic = 2*comb(15,3)*(beta/4)**3*groups[15,1][0,0]
    witness = r84["cancellation"](direct, cubic)
    assert witness > arb("1.9e-16")
    r84["envelope"].__globals__["signed_upper"] = r99["signed_upper"]
    previous = r84["envelope"](mid, half, unit, nx, 1, arb(1))
    frozen = [arb(x)/10**20 for x in cap]
    excess = r84["prior"]["image"](mid, half, previous, frozen)[0][0]-frozen[0]
    assert excess > r84["prior"]["EPS"]
    print(json.dumps(dict(kind="return_comparison", previous_first_packet_overrun=str(excess),
                          rank_three_scalar_cubic_saving_at_12_0_0_0=str(witness),
                          rank_four_shape_counts_by_degree_and_shifts=[[h,k,n] for (h,k),n in sorted(shape_counts.items())])), flush=True)
