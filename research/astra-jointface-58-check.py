"""Verify actual cold histories, rooted Dirichlet costs, and a full-face move."""
import importlib.util
import json
from fractions import Fraction as F
from pathlib import Path

from flint import acb, arb, ctx

here = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("face", here / "astra-face-54-check.py")
face = importlib.util.module_from_spec(spec)
spec.loader.exec_module(face)
ctx.prec = 384
n = face.n


def apply_k(row):
    freq = acb.dft(row)
    return [x.real for x in acb.dft([int(s)*z for s, z in zip(face.mask, freq)], inverse=True)]


def square(x):
    return x*x


def checked_zero(x):
    assert x.contains(0) and x.rad() < arb("1e-35"), x


def fixed_units(x):
    scaled = x*10**9
    return [int(scaled.lower().floor().unique_fmpz()), int(scaled.upper().ceil().unique_fmpz())]


# Directed mixture of the cyclic shifts by 0, 1 and 7. Both Fourier sectors
# are invariant, also without symmetry of the matrix. A column is the source.
shifts = [(0, arb(1)/2), (1, arb(1)/3), (7, arb(1)/6)]
edges = [((j+d) % n, j, weight) for d, weight in shifts for j in range(n)]
leak = arb(1)/2
v = [arb(0)]*n
seed = apply_k([arb(int(i==0)) for i in range(n)])
max_ratio = arb(0)
min_late_anti = None
for t in range(1, 33):
    phi = [abs(x) for x in v]
    b = (4+square(v[0])).sqrt()-phi[0]
    phi[0] = (4+square(v[0])).sqrt()
    mean = sum(phi)/n
    w = [x-mean for x in phi]
    nxt = apply_k(phi)
    for x, y in zip(apply_k(nxt), w):
        checked_zero(x-y)
    before = sum(weight*square(v[i]-v[j]) for i, j, weight in edges)/2
    after = sum(weight*square(nxt[i]-nxt[j]) for i, j, weight in edges)/2
    folding = sum(weight*(abs(v[i]*v[j])-v[i]*v[j]) for i, j, weight in edges)
    root = sum(weight*abs(v[j if i==0 else i]) for i, j, weight in edges if (i==0) != (j==0))
    checked_zero(after-before-4*leak+folding+b*root)
    max_ratio = max(max_ratio, (after/(4*leak*t)).upper())
    anti = sum(weight*square(nxt[i]+nxt[j]) for i, j, weight in edges)
    rotated = sum(weight*square(w[i]+w[j]) for i, j, weight in edges)
    checked_zero(anti-rotated)
    assert mean < 1
    floor = 2*leak*square(2-2*mean) + (1-leak)*square(4-2*mean)
    assert anti > floor
    column_test = sum(weight*(nxt[i]+nxt[j])*seed[j] for i, j, weight in edges)
    assert column_test > 2-2*mean
    if t==1:
        checked_zero(after-4*leak)
        checked_zero(anti-8*(1+1-leak-arb(2)/n))
    if t>=16:
        min_late_anti = anti.lower() if min_late_anti is None else min(min_late_anti, anti.lower())
    v = nxt
print(json.dumps(dict(kind="directed_sector_map", field=97, precision=ctx.prec, times=[1,32],
        shifts=[0,1,7], weights=["1/2","1/3","1/6"], seed_displacement_saturates=True,
        minimum_squared_antipodal_cost_16_through_32_units_1e9=fixed_units(min_late_anti),
        max_displacement_ratio_units_1e9=fixed_units(max_ratio)), sort_keys=True))

P, N = face.faces()
baseline = [row[0] for row in P]
perturb = [row[2]/32 for row in P]
candidate = [a+b for a,b in zip(baseline,perturb)]
assert all(x>=0 for x in candidate)
checked_zero(sum(perturb))
checked_zero(perturb[0])
for x,y in zip(apply_k(perturb),perturb):
    checked_zero(x-y)
positive = [i for i,x in enumerate(perturb) if x>0]
negative = [i for i,x in enumerate(perturb) if x<0]
assert len(positive)+len(negative)==sum(not x.is_zero() for x in perturb)
variation = sum(perturb[i] for i in positive)
coherence = 2*arb(97).sqrt()/n
assert all(abs(x)<coherence*variation for x in perturb)
assert all(N[i].is_zero() for i in positive+negative)
scores = [face.rounded(arb(n).sqrt()*x) for x in v]
sites = sorted(set(scores)|{-x for x in scores})


def objective(prob):
    prob, opp = [[face.rounded(x) for x in row] for row in [prob, N]]
    value = sites[0]+sum((b-a)*max(sum(p for x,p in zip(scores,prob) if x>a),
                                   sum(p for x,p in zip(scores,opp) if -x>a))
                         for a,b in zip(sites,sites[1:]))
    err = F(2,face.scale)*(1+n*(sites[-1]-sites[0]))
    return face.rb(value).union(face.rb(value-err)).union(face.rb(value+err))


gain = objective(baseline)-objective(candidate)
assert gain > arb("0.003")
# Construct a single column-stochastic matrix explicitly by only sending
# surplus mass to deficit sites. All other columns are fixed.
out = list(baseline)
for j in negative:
    retain = 1+perturb[j]/baseline[j]
    assert retain>=0 and retain<1
    out[j] = retain * baseline[j]
for i in positive:
    out[i] += sum((-perturb[j])*perturb[i]/variation for j in negative)
for a,b in zip(out,candidate):
    checked_zero(a-b)
print(json.dumps(dict(kind="one_common_support_conditioned_move",field=97, time=32,
        precision=ctx.prec, anchor_ratios=["0","1/32"], changed_plus_sites=[len(positive),len(negative)],
        unchanged_minus=True, root_unchanged=True, variation_units_1e9=fixed_units(variation),
        common_quantile_improvement_units_1e9=fixed_units(gain)), sort_keys=True))

# The two threshold bands require incompatible directions when independently
# minimizing the exact envelope. Test every site's band membership with Arb.
def band(lo, hi):
    lo, hi = arb(lo), arb(hi)
    actual = [arb(n).sqrt()*x for x in v]
    assert all(x<lo or x>hi for x in actual)
    assert all(-x<lo or -x>hi for x in actual)
    slopes = [sum(row[d] for x,row in zip(actual,P) if x>hi) for d in range(3)]
    opposite = sum(x for a,x in zip(actual,N) if -a>hi)
    return slopes[0]-opposite, slopes[1], slopes[2]


margin_a, ax, ay = band("3.45","3.60")
margin_b, bx, by = band("0.60","0.65")
assert margin_a>arb("0.02") and min(ax,ay)>arb("0.30")
assert margin_b>arb("0.03") and bx>0 and -arb("0.281")<by<-arb("0.28")
assert margin_b+by/32>0
large_parameter_gap = arb("0.15")*arb("0.30")/64
small_parameter_gap = arb("0.05")*(arb("0.28")/32-arb("0.281")/64)
assert min(large_parameter_gap,small_parameter_gap)>arb("0.000217")
print(json.dumps(dict(kind="thresholdwise_minimum_incompatibility",field=97,time=32,
        threshold_bands=[["3.45","3.60"],["0.60","0.65"]],precision=ctx.prec,
        first_band_slope_units_1e9=[fixed_units(ax),fixed_units(ay)],
        second_band_slope_units_1e9=[fixed_units(bx),fixed_units(by)],
        common_minus_separate_minimum_strict_lower="0.000217"), sort_keys=True))
