"""Outward verification of an entire failing ray of generic reference pairs."""
import importlib.util
import json
from pathlib import Path

from flint import acb, arb

spec = importlib.util.spec_from_file_location("face54", Path(__file__).with_name("astra-face-54-check.py"))
face = importlib.util.module_from_spec(spec)
spec.loader.exec_module(face)
plus_mass, minus_mass = face.faces()
n = face.n
zero = arb(0)
one = arb(1)
v = [zero] * n
for _ in range(32):
    activation = [abs(x) for x in v]
    activation[0] = (4 + v[0]**2).sqrt()
    f = acb.dft(activation)
    v = [z.real for z in acb.dft([int(s)*z for s, z in zip(face.mask, f)], inverse=True)]
charge = sum(x*x for x in v)/4
score = [arb(n).sqrt()*x for x in v]
sides = [[], []]
for i in range(n//2 + 1):
    mult = 1 if i in (0, n//2) else 2
    for sign, row in enumerate((plus_mass[i], (minus_mass[i], zero, zero))):
        if any(x != 0 for x in row):
            sides[sign].append((i, (-1)**sign*score[i], tuple(mult*x for x in row)))
for side in sides:
    side.sort(key=lambda item: float(item[1]))
    assert all(l[1] < r[1] for l, r in zip(side, side[1:]))

def at(row, x, y):
    return row[0] + row[1]*x + row[2]*y

def edges(x, y):
    # An internal cut is tagged by its side and atom index in score order.
    cuts = []
    for s, side in enumerate(sides):
        prefix = (zero, zero, zero)
        for k, (_, _, mass) in enumerate(side):
            assert at(mass, x, y) > 0
            prefix = tuple(a+b for a,b in zip(prefix, mass))
            if k+1 < len(side):
                cuts.append((s, k, prefix))
        assert all((a-b).contains(0) for a,b in zip(prefix, (one, zero, zero)))
    cuts.sort(key=lambda cut: float(at(cut[2], x, y)))
    cuts.append((-1, -1, (one, zero, zero)))
    cursor = [0, 0]
    prev = (-1, -1, (zero, zero, zero))
    result = []
    for s, k, end in cuts:
        first, second = (side[i] for side,i in zip(sides,cursor))
        cost = (first[1] + second[1] + abs(first[1]-second[1]))/2
        weight = tuple(b-a for a,b in zip(prev[2],end))
        whole_atom = None
        if s >= 0 and s == prev[0]:
            assert k == prev[1]+1
            whole_atom, _, weight = sides[s][k]
            whole_atom = (s, whole_atom)
        assert at(weight,x,y)>0
        result.append((weight,cost,whole_atom))
        if s >= 0:
            assert cursor[s] == k
            cursor[s] += 1
        prev = (s,k,end)
    return result

upper = one/10**8
window = zero.union(upper)
forest = edges(upper,upper)
assert len(forest) == 25
thin = [(w,tag) for w,_,tag in forest if tag in ((0,10),(0,21))]
assert len(thin) == 2
# Both flags correspond to the exact independent unit anchors divided by
# the same normalization, with the same orbit multiplicity.
thin_by_id = {tag[1]: w for w,tag in thin}
w1, w2 = thin_by_id[10], thin_by_id[21]
assert w1[0] == w1[2] == w2[0] == w2[1] == 0
a = w1[1]
assert a > 0 and (a-w2[2]).contains(0)
regular = [(w,c) for w,c,tag in forest if tag not in ((0,10),(0,21))]
assert all(at(w,window,window)>0 for w,_ in regular)
h = [sum(w[j+1]*c for w,c,_ in forest) for j in range(2)]

# Enclose xG throughout [0,upper] by removing the two simple poles.
def matrix(i,j):
    return (a if i==j else zero) + window*sum(
        w[i+1]*w[j+1]/at(w,window,window) for w,_ in regular)
m00,m01,m11 = matrix(0,0),matrix(0,1),matrix(1,1)
det = m00*m11-m01*m01
assert det>0
z0,z1 = (m11*h[0]-m01*h[1])/det, (m00*h[1]-m01*h[0])/det
assert z0>1 and z1<0
for w,_ in regular:
    assert window*(w[1]*z0+w[2]*z1)/at(w,window,window)<z0
gain_per_x = (h[0]*z0+h[1]*z1)/z0
assert gain_per_x>arb(36)/100 and gain_per_x<arb(37)/100
base = sum(w[0]*c for w,c,_ in forest)
ref = base + window*(h[0]+h[1])
y1,y2 = one/1000,one/100
witness = sum(at(w,y1,y2)*c for w,c,_ in edges(y1,y2))
assert ref-witness > one/1000

def nano(x):
    return [int((x.lower()*10**9).floor().unique_fmpz()),
            int((x.upper()*10**9).ceil().unique_fmpz())]

print(json.dumps(dict(field=97, time=32, reference="(x,x), 0<x<=10^-8",
    support_atoms=[len(s) for s in sides], overlap_edges=len(forest),
    vanishing_plus_orbits=[10,21], maximal_step_hits_plus_orbit=10,
    fixed_gradient_nano=[nano(s) for s in h], gain_over_x_nano=nano(gain_per_x),
    reference_charged_nano=nano(ref-charge), witness_charged_nano=nano(witness-charge),
    gap_over_witness_nano=nano(ref-witness)),sort_keys=True))

# After the first step the face x=0 has one tangent; reproject and use
# the full feasible line. A scalar survival kink gives a global minorant.
y_after = window*(one-z1/z0)
assert y_after < one/1000 and h[1] < 0
assert all(at(w,zero,zero.union(one/1000))>0 for w,_ in regular)
atoms = sorted([(z,s,i,m) for s,side in enumerate(sides) for i,z,m in side],
               key=lambda item:float(item[0]))
totals = [[one,zero,zero], [one,zero,zero]]
layers = []
for (z,s,i,mass), (next_z,*_) in zip(atoms,atoms[1:]):
    gap = next_z-z
    assert gap>0
    totals[s] = [a-b for a,b in zip(totals[s],mass)]
    difference = [a-b for a,b in zip(*totals)]
    layers.append(((s,i),gap,difference,totals[1][0]))
key = (1,24)
_,length,d,_ = next(layer for layer in layers if layer[0]==key)
assert d[2]<0
optimal_y = -d[0]/d[2]
for i,_,m in sides[0]:
    if i==10:
        assert m[0] == m[2] == 0
    else:
        assert at(m,zero,optimal_y)>0
fixed_grad = [zero,zero]
value = atoms[0][0]
for tag,length_i,diff,neg_mass in layers:
    excess = at(diff,zero,optimal_y)
    value += length_i*neg_mass
    if tag==key:
        continue    # diff[0]+diff[2]*optimal_y is exactly zero by definition
    if excess>0:
        value += length_i*excess
        fixed_grad = [g+length_i*j for g,j in zip(fixed_grad,diff[1:])]
    else:
        assert excess<0
mix = -fixed_grad[1]/(length*d[2])
assert 0<mix<1
normal = fixed_grad[0]+mix*length*d[1]
assert normal>0
assert optimal_y>y_after
assert ref>value and (fixed_grad[1]+length*d[2])<0<fixed_grad[1]
print(json.dumps(dict(field=97,time=32,second_projection="x=0, increasing y",
    unique_global_optimal_y_nano=nano(optimal_y), attained_charged_nano=nano(value-charge),
    full_gap_nano=nano(ref-value), active_survival_lower_site="minus orbit 24",
    plus_survival_mix_nano=nano(mix), inward_global_price_nano=nano(normal)),sort_keys=True))
