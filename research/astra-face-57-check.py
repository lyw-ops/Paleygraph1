"""Full positive completion separately at each genuine p=97 cold score threshold."""
import importlib.util
import json
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
from flint import arb, acb, ctx

here = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("face54", here/"astra-face-54-check.py")
face = importlib.util.module_from_spec(spec)
spec.loader.exec_module(face)
ctx.prec = 384
P, N = face.faces()
n = len(N)
q = [tuple(map(face.rounded,row)) for row in P]
h = list(map(face.rounded,N))
one = F(1)
slack = F(6,face.scale)
constraints = [(0,one,0),(one,-one,0),(0,0,one),(one,0,-one)]
constraints.extend(face.add(row,(slack,0,0)) for row in q if any(row))
outer = []
for a,b in combinations(constraints,2):
    x = face.intersection(a,b)
    if x is not None and all(face.at(c,x)>=0 for c in constraints) and x not in outer:
        outer.append(x)
interior = (F(1,10000),)*2
assert all(face.at(row,tuple(map(face.rb,interior)))>=0 for row in P)
inner = [tuple((1-F(1,10**10))*u+v/10**10 for u,v in zip(x,interior)) for x in outer]
assert all(face.at(row,tuple(map(face.rb,x)))>=0 for row in P for x in inner)
den = 10**9
def enclosure(lo,hi):
    return [int(lo*den//1),int(-(-hi*den//1))]
def evaluate(t,v):
    scores = [face.rounded(arb(n).sqrt()*u) for u in v]
    sites = sorted(set(scores)|{-x for x in scores})
    cols = []
    for a,b in zip(sites,sites[1:]):
        pl = tuple(sum(row[i] for z,row in zip(scores,q) if z>a) for i in range(3))
        mi = sum(w for z,w in zip(scores,h) if -z>a)
        cols.append((b-a,pl,mi))
    def integrate(rows,per_threshold):
        if per_threshold:
            return sites[0]+sum(d*max(mi,max(face.at(pl,x) for x in rows)) for d,pl,mi in cols)
        return max(sites[0]+sum(d*max(mi,face.at(pl,x)) for d,pl,mi in cols) for x in rows)
    # Rounded weights and exact score displacements are charged uniformly, also
    # for an envelope of multiple genuine score distributions.
    error = F(2,face.scale)+(sites[-1]-sites[0])*n*slack
    V = [integrate(inner,True)-error,integrate(outer,True)+error]
    W = [integrate(inner,False)-error,integrate(outer,False)+error]
    E = sum(x*x for x in v)/4
    e = face.rounded(E)
    return dict(t=t,thresholdwise_max=enclosure(*V),common_pair_max=enclosure(*W),
                switching_gap=enclosure(V[0]-W[1],V[1]-W[0]),
                charged_thresholdwise_per_step=enclosure((V[0]-e-F(2,face.scale))/t,
                                                          (V[1]-e+F(2,face.scale))/t))
v = [arb(0)]*n
rows = []
for t in range(1,33):
    a = [abs(x) for x in v]
    a[0] = (4+v[0]**2).sqrt()
    f = acb.dft(a)
    v = [k.real for k in acb.dft([int(s)*u for s,u in zip(face.mask,f)],inverse=True)]
    if t>=16:
        rows.append(evaluate(t,v))
print(json.dumps(dict(kind="fully_completed_thresholds",field=97,precision=ctx.prec,units="1e-9",
    all_integer_depths=[16,32],outer_vertices=len(outer),checked_inner_vertices=len(inner),
    min_switching_gap=min(r['switching_gap'][0] for r in rows),
    positive_switching_times=[r['t'] for r in rows if r['switching_gap'][0]>0],
    min_charged_thresholdwise_per_step=min(r['charged_thresholdwise_per_step'][0] for r in rows),
    endpoint_rows=[rows[0],rows[-1]]),sort_keys=True))

# On a true cold threshold, perturb one minus orbit then correct the same
# perturbation on disjoint lower orbits separately for every three frequencies.
from flint import arb_mat
scores=[arb(n).sqrt()*x for x in v]
high=[16]
low=[1,4,9,12,15,17,20,23,24]
assert all((-scores[j]>arb(41)/10) if j in high else (-scores[j]<arb(38)/10)
           for j in range(25) if N[j]>0)
assert all(scores[j]<arb(38)/10 for j,row in enumerate(P) if any(not a.is_zero() for a in row))
D=[f for f in range(1,25) if face.mask[f]==1]
increment=arb(1)/1000
assert 2*N[16]<arb(278)/1000 and 2*N[16]+increment < arb(1)/3
assert N[16]+increment/2 < N[0]
checked=0
for triple in combinations(D,3):
    f=[0,*triple]
    B=arb_mat([[(arb(2*d*j)/n).cos_pi() for j in low] for d in f])
    target=arb_mat([[-increment*(arb(2*d*16)/n).cos_pi()] for d in f])
    gram=B*B.transpose()
    correction=B.transpose()*gram.solve(target)
    for k,j in enumerate(low):
        updated=N[j]+correction[k,0]/(1 if j==24 else 2)
        assert updated>0 and updated<N[0],(triple,j,updated)
    checked+=1
print(json.dumps(dict(kind="rooted_three_frequency_positive_completion",field=97,time=32,
    closed_threshold_interval=["3.8","4.1"],side="minus",tail_orbit=16,
    forbidden_inverse_orbits=D,three_frequency_blocks=checked,added_common_orbit_mass="1/1000",
    integrated_gap_above_exact_thresholdwise_lower="3/10000",precision=ctx.prec),sort_keys=True))

# Locate the least number of inverse-frequency orbits that pins this tail.
# Orbit-mass coefficients are real cosines in the 48th cyclotomic field.
def cyclo(f,j):
    return (face.powers[f*j % n]+face.powers[-f*j % n])/2
freq_row={f:[cyclo(f,j) for j in low+[16]] for f in [0,*D]}
slack=[]
for j in low:
    mult=1 if j==24 else 2
    slack.append(min(N[j].lower(),(N[0]-N[j]).lower())*mult)
admissible=(2*(N[0]-N[16])).lower()
tested=0
for A in combinations(D,5):
    rows=[freq_row[f] for f in (0,*A)]
    delta,rank=face.solve([r[:-1] for r in rows],[-r[-1] for r in rows],face.modulus)
    assert all((sum(a*b for a,b in zip(r[:-1],delta))+r[-1])%face.modulus==face.zero for r in rows)
    for d,margin in zip(delta,slack):
        if d:
            admissible=min(admissible,(margin/abs(face.ball(d)).upper()).lower())
    tested+=1
pin=(1,7,11,13,18,24)
rows=[freq_row[f] for f in (0,*pin)]
dual,rank=face.solve(list(map(list,zip(*rows))),[face.zero]*len(low)+[face.one],face.modulus)
for k,j in enumerate(low+[16]):
    assert sum(d*r[k] for d,r in zip(dual,rows))%face.modulus==(face.one if j==16 else face.zero)
eta_units=int((admissible*10**9).lower().floor().unique_fmpz())
assert eta_units>0
print(json.dumps(dict(kind="exact_rooted_block_threshold",field=97,time=32,sign="minus",
    lower_orbits=low,upper_orbits=[16],five_blocks_checked=tested,
    common_tail_mass_increment_certified_units_1e_9=eta_units,
    minimum_pinning_block_size=6,pinning_block=pin),sort_keys=True))
