"""Rational polygon enclosures of optimal chords and collision on the prime 97 face."""
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import json
import runpy
from flint import arb

here = Path(__file__).parent
src = runpy.run_path(str(here / "astra-face-54-check.py"))
plus, minus = src["faces"]()
rec = json.loads((here / "translated-caps-71-checks.jsonl").read_text())
demand = {i: Q(k, 19) for i, k in rec["nonzero_site_counts"]}
r = [tuple(src["rounded"](x / plus[0][0]) for x in row) for row in plus]
e = Q(6, 10**19)
at = src["at"]
cons = [(Q(0),1,0), (Q(1),-1,0), (Q(0),0,1), (Q(1),0,-1)]
cons += [(a+e,b,c) for a,b,c in r if (a,b,c) != (0,0,0)]
verts = set()
for a,b in combinations(cons,2):
    pt = src["intersection"](a,b)
    if pt is not None and all(at(c,pt)>=0 for c in cons):
        verts.add(pt)
# Strictly feasible inner witnesses approximate every outer vertex.
inside = []
for pt in verts:
    w = Q(1,10**10)
    trial = tuple((1-w)*x+w*Q(1,10000) for x in pt)
    assert all(at(row, tuple(map(src["rb"], trial))) >= 0 for row in plus)
    inside.append(trial)
assert all(-3*e <= at(r[i],v) <= 1+3*e for v in verts for i in demand)
lo = {i:max(at(r[i],v) for v in inside)-e for i in demand}
hi = {i:max(at(r[i],v) for v in verts)+e for i in demand}
assert min(lo.values())>0
def chord(p, caps):
    return sum(f*caps[i]*at(r[i],p) for i,f in demand.items())
def square(p):
    return sum(f*at(r[i],p)**2 for i,f in demand.items())
err = 5*sum(demand.values())*e
# The unconstrained stationary point and stationary points on all edges
# cover the minimum of the rounded convex quadratic on the outer polygon.
def ip(j,k):
    return sum(f*r[i][j]*r[i][k] for i,f in demand.items())
grad = [tuple(ip(j,k) for k in range(3)) for j in (1,2)]
candidates = list(verts)
p = src["intersection"](*grad)
if p and all(at(c,p)>=0 for c in cons):
    candidates.append(p)
for a,b,c in cons:
    tangent = tuple(c*x-b*y for x,y in zip(*grad))
    p = src["intersection"]((a,b,c), tangent)
    if p and all(at(v,p)>=0 for v in cons):
        candidates.append(p)
pt = min(candidates,key=square)
trial = tuple((1-Q(1,10**10))*x+Q(1,10**14) for x in pt)
assert all(at(row,tuple(map(src["rb"],trial)))>=0 for row in plus)
def interval(a,b):
    scale = 10**8
    return [int(a*scale//1),int(-(-b*scale//1))]
rec = dict(field=97,scale="1e-8", window_starts=[1,19],window_length=3,
    minimum_quadratic=interval(square(pt)-err,square(trial)+err),
    minimum_optimal_even_chord=interval(min(chord(p,lo) for p in verts)-err,
                                         min(chord(p,hi) for p in inside)+err),
    maximum_optimal_even_chord=interval(max(chord(p,lo) for p in inside)-err,
                                         max(chord(p,hi) for p in verts)+err),
    maximum_even_quadratic=interval(max(map(square,inside))-err,max(map(square,verts))+err))
# Allow the strongest affine majorant pinned at both actual coordinate extrema.
low_outer = {i:min(at(r[i],v) for v in verts)-e for i in demand}
low_inner = {i:min(at(r[i],v) for v in inside)+e for i in demand}
def twosided(p, left, right):
    return sum(f*((left[i]+right[i])*at(r[i],p)-left[i]*right[i])
               for i,f in demand.items())
# Uniform absolute endpoint error on the unit box, including outer vertices.
width = max(max(hi[i]-lo[i], low_inner[i]-low_outer[i]) for i in demand)
err2 = err+4*width*sum(demand.values())
rec.update(minimum_tight_affine=interval(min(twosided(p,low_outer,hi) for p in verts)-err2,
                                        min(twosided(p,low_outer,hi) for p in inside)+err2),
           maximum_tight_affine=interval(max(twosided(p,low_outer,hi) for p in inside)-err2,
                                        max(twosided(p,low_outer,hi) for p in verts)+err2))
print(json.dumps(rec,sort_keys=True))
