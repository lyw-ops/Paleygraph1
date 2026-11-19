"""Exact half-turn reachability and interval checks on the prime 97 faces."""
import importlib.util
import json
from pathlib import Path

from flint import acb, arb, ctx

src = Path(__file__).with_name("astra-face-54-check.py")
spec = importlib.util.spec_from_file_location("face", src)
face = importlib.util.module_from_spec(spec)
spec.loader.exec_module(face)
ctx.prec = 384
n, half = face.n, face.n // 2
plus, minus = face.faces()


def units(x):
    y = x * 10**9
    return [int(y.lower().floor().unique_fmpz()), int(y.upper().ceil().unique_fmpz())]


def small(x):
    assert x.contains(0) and x.rad() < arb("1e-33"), x


# Verify each direction in the unnormalized cyclotomic number field.
for orbit in face.free:
    rhs = [-r[0] for r in face.system(1, [orbit])]
    c, rank = face.solve(face.system(1, face.active[1]), rhs, face.modulus)
    assert rank == len(face.active[1])
    d = face.vector(face.active[1]+[orbit], c+[face.one], face.zero)
    assert all((d[j]+d[j+half]) % face.modulus == face.zero for j in range(half))
    assert d[0] == d[half] == face.zero

base = [r[0] for r in plus]
h = [r[2]/32 for r in plus]
donors = [arb(0).max(-x) for x in h]
trial = [x+y for x,y in zip(base,h)]
assert all(x>=0 for x in trial)
for j in range(n):
    assert donors[j] <= base[j]
    small(donors[(j+half)%n]-donors[j]-h[j])
    if donors[j]>0:
        assert minus[j].is_zero() and minus[(j+half)%n].is_zero() and j not in (0,half)
# The single profile obstruction by coverage is independent of the weights.
blocked_indices = []
for b in range(1,n+1):
    if n%b == 0 and {j%b for j in range(n) if minus[j]>0} == set(range(b)):
        blocked_indices.append(b)
print(json.dumps(dict(kind="cyclotomic_half_turn_full_even_face",p=97,shift=half,
    odd_null_directions=face.free,minus_face_dimension=0,
    opposite_hits_all_cosets_at_indices=blocked_indices,
    gain_trial_transported_mass_1e9=units(sum(donors))),sort_keys=True))

# The signed-moment debit is tested on two actual plus rows and the minus row.
rows = [base,trial,minus]
signs = [1,1,-1]
sqrt_n = arb(n).sqrt()
marks = [sqrt_n*r[0] for r in rows]
A = B = arb(0)
H = [arb(0)]*3
v = [arb(0)]*n
mins = []
for t in range(1,33):
    phi = [abs(x) for x in v]
    phi[0] = (4+v[0]**2).sqrt()
    bump = phi[0]-abs(v[0])
    mean = sum(phi)/n
    A += (1-mean*sqrt_n/2)**2
    B += 2-bump
    for k,(r,s) in enumerate(zip(rows,signs)):
        H[k] += sqrt_n*sum(u*(abs(x)-s*x) for u,x in zip(r,v))
    f = acb.dft(phi)
    v = [a.real for a in acb.dft([int(s)*x for s,x in zip(face.mask,f)],inverse=True)]
    E = sum(x*x for x in v)
    assert E.lower() > ((phi[0]-mean)**2).upper()
    Y = [sqrt_n*x for x in v]
    m = [s*sum(u*x for u,x in zip(r,Y)) for r,s in zip(rows,signs)]
    for a,mu,hinge in zip(marks,m,H):
        small(mu-2*t*(a-1)+a*B-E/4-A-hinge)
    # At this prime the plus sign is larger. Adding both signed comparisons
    # also tests the mark-independent two-face statement.
    rhs = (E/2+2*A)+(marks[0]+marks[2]-2)*2*t-(marks[0]+marks[2])*B
    small((m[0]+m[1]+2*m[2])/2-rhs-(H[0]+H[1]+2*H[2])/2)
    if t>=16:
        mins.append(rhs.lower())
    if t==32:
        # Independent finite integration at rounded rational levels.
        scores = [face.rounded(x) for x in Y]
        grid = sorted(set(scores)|{-x for x in scores})
        def cost(row):
            p = [face.rounded(x) for x in row]
            q = [face.rounded(x) for x in minus]
            out = grid[0]
            for lo,hi in zip(grid,grid[1:]):
                out += (hi-lo)*max(sum(y for x,y in zip(scores,p) if x>lo),
                                   sum(y for x,y in zip(scores,q) if -x>lo))
            error = 2*(1+n*(grid[-1]-grid[0]))/face.scale
            return face.rb(out-error).union(face.rb(out+error))
        gain = cost(base)-cost(trial)
        assert gain > arb(".003649205")
        charged = (cost(trial)-E/4)/t
assert marks[0]>1 and marks[2]<1
print(json.dumps(dict(kind="actual_cold_flow_and_signed_moments",p=97,precision=ctx.prec,
    times=[1,32],minimum_averaged_mean_lower_16_to_32_units_1e9=units(min(mins)),
    half_turn_gain_32_units_1e9=units(gain),charged_trial_per_step_32_units_1e9=units(charged)),
    sort_keys=True))

# Keep the singleton even minus optimum. Relax only the plus Fourier equations;
# root, true exposed support, cap and every half-turn-pair mass are retained.
interior = [a+(b+c)/100 for a,b,c in plus]
greedy = interior[:]
for j in range(1,half):
    k = j+half
    if not (minus[j].is_zero() and minus[k].is_zero()):
        continue
    if k == (-j)%n:  # exact tie by inversion
        continue
    assert Y[j] < Y[k] or Y[k] < Y[j]
    mass = interior[j]+interior[k]
    if Y[j]<Y[k]:
        greedy[j] = mass.min(interior[0])
    else:
        greedy[j] = arb(0).max(mass-interior[0])
    greedy[k] = mass-greedy[j]
# Project first-half changes onto the full even null space over the reals.
dirs = [[r[a] for r in plus[:half]] for a in (1,2)]
dot = lambda a,b: sum(x*y for x,y in zip(a,b))
delta = [g-u for g,u in zip(greedy[:half],interior[:half])]
u,w = dirs
aa,bb,cc = dot(u,u),dot(u,w),dot(w,w)
det = aa*cc-bb**2
assert det>0
cu = (cc*dot(u,delta)-bb*dot(w,delta))/det
cw = (aa*dot(w,delta)-bb*dot(u,delta))/det
proj = [cu*r[1]+cw*r[2] for r in plus]
projected_trial = [x+d/40 for x,d in zip(interior,proj)]
assert all(x>=0 for x in projected_trial)
for j,x in enumerate(projected_trial):
    if j!=0:
        assert x < interior[0]
    if minus[j]>0 and j!=0:
        assert x.is_zero()
defect_cost = sum(abs(Y[j]-Y[j+half])*abs(delta[j]-proj[j]) for j in range(half))
greedy_cost = cost(greedy)
assert greedy_cost < arb("2.504908000")
assert defect_cost > arb(".70051")
projected_gain = cost(interior)-cost(projected_trial)
assert projected_gain > arb(".0025")
print(json.dumps(dict(kind="sharp_pair_mass_relaxation_and_fourier_repair",p=97,t=32,
    fixed_minus=True,plus_reference_ratios=["1/100","1/100"],step="1/40",
    greedy_cost_1e9=units(greedy_cost),fourier_repair_cost_bound_1e9=units(defect_cost),
    feasible_projected_gain_1e9=units(projected_gain),
    feasible_projected_charged_per_step_1e9=units((cost(projected_trial)-E/4)/32)),sort_keys=True))
