"""Outward checks of survival price ranges and both one-sided price failures."""
from contextlib import redirect_stdout
from io import StringIO
import json
from pathlib import Path
import runpy

from flint import arb

here = Path(__file__).resolve().parent
with redirect_stdout(StringIO()):
    old = runpy.run_path(str(here / "astra-coupling-64-check.py"))
    geometry = runpy.run_path(str(here / "astra-charged-61-check.py"))
face = old["face"]
at = old["at"]
nano = old["nano"]
zero, one = arb(0), arb(1)
vertices = [(face.ball(x),face.ball(y)) for x,y in geometry["vertices"]]
layers = old["layers"]
charge = old["charge"]
first_score = old["atoms"][0][0]
small = one/10**80

def max_zero(x):
    return (x+abs(x))/2

def compare_to_min(values):
    for index, value in enumerate(values):
        if all(value < x for i,x in enumerate(values) if i!=index):
            return index
    raise AssertionError(values)

def true_cost(x,y):
    return first_score-charge + sum(w*(neg+max_zero(at(diff,x,y)))
                                    for _,w,diff,neg in layers)

def priced_cost(weights,x,y):
    return first_score-charge + sum(w*(neg+lam*at(diff,x,y))
                           for (_,w,diff,neg), lam in zip(layers,weights))

# Enlarging each range outwards preserves the theorem, including exact
# endpoint ties or fixed-zero thresholds. Every proposal below is checked.
weights = []
budget = zero
ambiguous = []
for tag,w,diff,neg in layers:
    vals = [at(diff,x,y) for x,y in vertices]
    lo = min(v.lower() for v in vals)-small
    hi = max(v.upper() for v in vals)+small
    assert all(lo<v and v<hi for v in vals)
    if hi<=0:
        weights.append(zero)
    elif lo>=0:
        weights.append(one)
    else:
        weights.append(hi/(hi-lo))
        budget += w*hi*(-lo)/(hi-lo)
        if min(-lo,hi)>small*10:
            ambiguous.append(tag)
values = [priced_cost(weights,x,y) for x,y in vertices]
choice = compare_to_min(values)
lower = values[choice]
primal = true_cost(*vertices[choice])
opt = old["value"]-charge
assert primal>=lower and primal<lower+budget+one/10**18 and lower<opt and opt<primal
print(json.dumps(dict(kind="fourier_feasible_survival_chord_trial",field=97,time=32,
    selected_vertex_anchor_nano=[nano(z) for z in vertices[choice]],
    appreciably_ambiguous_lower_sites=ambiguous, lower_charged_nano=nano(lower),
    upper_charged_nano=nano(primal), full_optimum_charged_nano=nano(opt),
    range_budget_nano=nano(budget), actual_primal_error_nano=nano(primal-opt)),
    sort_keys=True))

# Opposite perturbations of the tied survival difference. The slope in
# the free variable y is nonzero on each side; y is two-sided at the optimum.
key = old["key"]
ystar = old["optimal_y"]
d = old["d"]
for orientation in [-1,1]:
    # x=h, y=y*+kh gives exactly diff=h*orientation at the tied layer.
    slope = (orientation-d[1])/d[2]
    interval = zero.union(one/10**8)
    for i,_,row in old["sides"][0]:
        if i==10:
            assert row[0]==row[2]==0 and row[1]>0
        else:
            assert at(row,interval,ystar+slope*interval)>0
    indicators = []
    for tag,w,diff,neg in layers:
        if tag==key:
            indicators.append(one if orientation==1 else zero)
        else:
            val = at(diff,interval,ystar+slope*interval)
            assert val>0 or val<0
            indicators.append(one if val>0 else zero)
    prices = [priced_cost(indicators,x,y) for x,y in vertices]
    index = compare_to_min(prices)
    price_min = prices[index]
    assert (priced_cost(indicators,zero,ystar)-opt).contains(0)
    fixed_loss = opt-price_min
    growth = sum(w*lam*(diff[1]+slope*diff[2])
                 for (_,w,diff,_),lam in zip(layers,indicators))
    assert growth>0 and fixed_loss>one/10000
    # Round 64 cap metric on attainable plus total orbit probabilities.
    root_mass = old["plus_mass"][0][0]
    gram = [[sum(row[k+1]*row[l+1] / ((1 if i in (0,face.n//2) else 2)*root_mass)
                 for i,_,row in old["sides"][0] if i!=0)
              for l in range(2)] for k in range(2)]
    g = [sum(w*lam*diff[k+1] for (_,w,diff,_),lam in zip(layers,indicators))
         for k in range(2)]
    a,b = gram[0]
    _,c = gram[1]
    norm = ((c*g[0]**2-2*b*g[0]*g[1]+a*g[1]**2)/(a*c-b**2)).sqrt()
    assert norm>0
    print(json.dumps(dict(kind="strict_side_of_minimizing_survival_kink",field=97,time=32,
        signed_survival_direction=orientation, anchor_slope_nano=nano(slope),
        reference_gap_per_h_nano=nano(growth),cap_tangent_dual_norm_nano=nano(norm),
        attained_price_gap_limit_nano=nano(fixed_loss),
        minimizing_linear_vertex_nano=[nano(v) for v in vertices[index]]),
        sort_keys=True))

# Fixed-sign thresholds are pointwise dominated by the matching pure price.
# Include undecided endpoint-equality cases in the exhaustive enumeration.
from itertools import product
candidate = []
varying = []
for k,(_,w,diff,neg) in enumerate(layers):
    vals = [at(diff,*v) for v in vertices]
    if all(v>0 for v in vals):
        candidate.append(one)
    elif all(v<0 for v in vals):
        candidate.append(zero)
    else:
        varying.append(k)
        candidate.append(zero)
pure_bounds = []
for bits in product((zero,one),repeat=len(varying)):
    for k,bit in zip(varying,bits):
        candidate[k] = bit
    values = [priced_cost(candidate,*v) for v in vertices]
    pure_bounds.append(min(v.lower() for v in values).union(
                       min(v.upper() for v in values)))
best = max(v.lower() for v in pure_bounds).union(max(v.upper() for v in pure_bounds))
assert opt-best>one/10**5
print(json.dumps(dict(kind="all_unsplit_layer_prices",field=97,time=32,
    enumerated_profiles=len(pure_bounds),best_lower_charged_nano=nano(best),
    strict_loss_nano=nano(opt-best)),sort_keys=True))
