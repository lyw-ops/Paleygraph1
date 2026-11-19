"""Certify root-residual prices of genuine opposite laws on the round-80 heads."""
import json
import runpy
from pathlib import Path

import numpy as np
from flint import acb, arb, arb_mat, ctx
from scipy.optimize import linprog

base = Path(__file__).resolve().parent
prior = runpy.run_path(str(base / 'endpoint-direction-45-check.py'))
ctx.prec = 384


def bounds(value):
    v = 10**8 * value
    return [int(v.lower().floor().unique_fmpz()), int(v.upper().ceil().unique_fmpz())]


def true_heads(p, b, given=None):
    signs = prior['paley_sign'](p)
    if given is None:
        pair, reason = prior['solve_prime_pair'](signs)
        assert reason is None
    else:
        pair = given
    side = 1 if pair[1][0] > pair[-1][0] else -1
    assert pair[side][0] > pair[-side][0]
    n = len(signs)
    root = arb(n).sqrt()
    q = [v/root for v in pair[side]]
    r = [v/root for v in pair[-side]]
    apply = prior['apply_multiplier']
    state = [arb(0)]*n
    raw = [arb(0)]*n
    for t in range(b+1):
        phi = [(4+state[0]**2).sqrt()] + list(map(abs, state[1:]))
        if t:
            w = arb(1 if t == b else 2)/(2*b-1)
            raw = [v+w*root*(h-int(side)*y)/2 for v,h,y in zip(raw,phi,state)]
        if t < b:
            state = apply(phi,signs)
        else:
            terminal = apply([root*(h+side*y)/2 for h,y in zip(phi,state)],
                             [int(v in (0,side)) for v in signs])
    opposite = [int(v == -side) for v in signs]
    col = [v.real for v in acb.dft(opposite,inverse=True)]
    primary = apply(raw,[int(v in (0,-side)) for v in signs])
    inc = (primary[0]/root-sum(raw)/n).max(0)
    primary = [v+inc*(1-c/col[0]) for v,c in zip(primary,col)]
    u = arb(1)/100
    assert all(v < -u or v > -u for v in primary[1:])
    S = [i for i in range(1,n) if primary[i] < -u and q[i] > 0]
    assert S and all(terminal[j] > (2*b-1)*u for j in S)
    assert all(v < arb(1)/n or v > arb(1)/n for v in q[1:])
    x = [(v-arb(1)/n).max(0) for v in q]
    M = sum(x[1:])
    mass = sum(q[i] for i in S)
    rho = root*sum(q[i]**2 for i in S)/(mass*M)
    k = [v.real*n/arb(p).sqrt() for v in acb.dft(list(map(int,signs)),inverse=True)]
    W = [side*sum(q[i]*k[(j-i)%n] for i in S)/mass for j in range(n)]
    assert all(v > rho/8 or v < rho/8 for v in W[1:])
    F = [j for j in range(1,n) if W[j] > rho/8 and x[j] > 0]
    assert F and set(F) == {(-j)%n for j in F} and all(r[j].is_zero() for j in F)
    Wmean = sum(q[j]*W[j] for j in range(n))
    L = n*sum(q[j]**2 for j in S)
    assert (Wmean-(L/mass-1)/arb(p).sqrt()).contains(0)
    mu = sum(v-y for v,y in zip(q,x))
    m = n*mass**2/L
    moment_lo = L/(arb(p).sqrt()*mass)*(1-((mu-mu**2)*(1-m/n)/L).sqrt())
    moment_lo -= 1/arb(p).sqrt()+x[0]*W[0]
    moment = sum(x[j]*W[j] for j in range(1,n))
    assert moment > moment_lo
    return signs, side, q, r, F, M, rho, W, moment, moment_lo


def measure(p,b):
    signs, side, q, r, F, M, rho, W, moment, moment_lo = true_heads(p,b)
    n = len(q)
    a = q[0]
    qF = sum(q[j] for j in F)
    clip = qF-arb(len(F))/n
    reps = list(range(1,n//2+1))
    active = [j for j in reps if q[j] > 0]
    freq = [t for t in reps if signs[t] == -side]
    c = [(arb(2*j)/n).cos_pi() for j in range(n)]
    matrix = arb_mat([[c[(t*j)%n] for t in freq] for j in active])
    coeff = list(matrix.solve(arb_mat([[int(j in F)] for j in active])))
    raw = [sum(h*c[(t*j)%n] for t,h in zip(freq,coeff)) for j in range(n)]
    # The invertible exact system gives raw = 1_F on the exposed active bulk.
    assert all((raw[j]-int(j in F)).contains(0) for j in range(1,n) if q[j] > 0)
    repair = [j for j in range(n) if j == 0 or q[j].is_zero()]
    assert all(r[j] > 0 for j in repair)
    lam = 1+max([0]+[int((-raw[j]/r[j]).upper().ceil().unique_fmpz()) for j in repair])
    law = [(v+lam*t)/lam for v,t in zip(raw,r)]  # raw has exact mean zero
    assert all(law[j] > 0 for j in repair) and (sum(law)-1).contains(0)
    level = arb(n)/lam
    price = (1-n*a*law[0])/level
    assert (price-qF).contains(0) and all((n*law[j]-level).contains(0) for j in F)

    # Nonnegative translates of the fixed opposite optimizer. Group inverse shifts.
    shifts = [h for h in reps if r[(-h)%n] < r[0]]
    assert all(r[(-h)%n] < r[0] for h in reps)
    budgets = [arb(1)/n-a*r[(-h)%n] for h in shifts]
    assert all(v > 0 for v in budgets)
    ids = [j for j in reps if j in F]
    columns = [[(r[(j-h)%n]+r[(j+h)%n])/(2*budget) for h,budget in zip(shifts,budgets)] for j in ids]
    mat = np.array([[float(x.mid()) for x in row] for row in columns])
    primal = linprog(np.ones(len(shifts)),A_ub=-mat,b_ub=-np.ones(len(ids)),bounds=(0,None))
    dual = linprog(-np.ones(len(ids)),A_ub=mat.T,b_ub=np.ones(len(shifts)),bounds=(0,None))
    assert primal.success and dual.success
    # Dyadic nonnegative weights proposed by LP; rescaling certifies all inequalities.
    weights = [arb(float(max(0,x))) for x in primal.x]
    minimum = min(sum(v*y for v,y in zip(row,weights)).lower() for row in columns)
    lower_weights = [arb(float(max(0,x))) for x in dual.x]
    maximum = max(sum(y*row[k] for row,y in zip(columns,lower_weights)).upper() for k in range(len(shifts)))
    assert minimum > 0 and maximum > 0
    hi = sum(weights)/minimum
    lo = sum(lower_weights)/maximum
    assert hi-lo < arb(1)/10**7
    eff = max((sum(q[j]*r[(j-h)%n] for j in F)/budget).upper() for h,budget in zip(shifts,budgets))
    assert 0 < eff < 1 and lo > qF
    # All-translate point caps, then one-dimensional bounded fractional knapsack.
    caps = [(min([a]+[(arb(1)/n-a*r[(-h)%n])/r[(j-h)%n] for h in range(n)
                      if r[(j-h)%n] > 0])-arb(1)/n).max(0) for j in F]
    excess = [W[j]-rho/8 for j in F]
    def mass_lower(field_moment):
        gap = field_moment-M*rho/8
        return max([arb(0)]+[(gap/y-sum(cap*(z/y-1).max(0) for cap,z in zip(caps,excess))).lower()
                             for y in excess])
    direct = mass_lower(moment_lo)
    sorted_price = mass_lower(moment)
    assert sorted_price < clip and direct <= sorted_price
    return dict(p=p,b=b,heads=len(F),mass=bounds(qF),clipped=bounds(clip),
                finite_moment_clipped_lower=bounds(direct),measured_moment_clipped_lower=bounds(sorted_price),
                clipped_over_rho_M=bounds(clip/(rho*M)),
                full_cone_law_level=bounds(level),full_cone_root_budget=bounds(1-n*a*law[0]),
                translate_capture_upper=bounds(eff),efficiency_price_lower=bounds(qF/eff),
                translate_optimum=[bounds(lo)[0],bounds(hi)[1]],
                translate_optimum_minus_floor_over_exact=[bounds((lo-arb(len(F))/n)/clip)[0],
                                                           bounds((hi-arb(len(F))/n)/clip)[1]],
                precision=ctx.prec,units='1e-8')


def degenerate_face():
    face = runpy.run_path(str(base / 'astra-face-54-check.py'))
    ctx.prec = 384
    primary, opposite = face['faces']()
    n = len(primary)
    interior = arb(1)/1000
    q = [v+interior*(a+b) for v,a,b in primary]
    assert all(x.is_zero() or x>0 for x in q)
    pair = {1:[arb(n).sqrt()*v for v in q], -1:[arb(n).sqrt()*v for v in opposite]}
    signs, side, _, r, F, *_ = true_heads(97,4,pair)
    assert F == [5,13,18,30,35,43] and side == 1
    # These two binding coordinates specify the alternate optimizer exactly.
    binding = [3,19]
    constraints = arb_mat([[primary[j][1],primary[j][2]] for j in binding])
    u,v = list(constraints.solve(arb_mat([[-primary[j][0]] for j in binding])))
    best = [c+a*u+b*v for c,a,b in primary]
    for j in binding+[n-k for k in binding]:
        assert best[j].contains(0)
        best[j] = arb(0)
    assert all(x.is_zero() or x>0 for x in best)
    assert (sum(best)-1).contains(0) and (q[0]-best[0]).contains(0)
    a = q[0]
    reps = list(range(1,n//2+1))
    active = [j for j in reps if best[j]>0]
    freq = [t for t in reps if signs[t] == -side]
    cosine = [(arb(2*j)/n).cos_pi() for j in range(n)]
    block = arb_mat([[cosine[(j*t)%n] for t in freq] for j in active])
    co = list(block.solve(arb_mat([[int(j in F)] for j in active])))
    raw = [sum(c*cosine[(j*t)%n] for c,t in zip(co,freq)) for j in range(n)]
    assert all((raw[j]-int(j in F)).contains(0) for j in range(1,n) if best[j]>0)
    assert all(raw[j]>0 for j in binding+[n-k for k in binding])
    repair = [j for j in range(n) if r[j]>0]
    lam = 1+max([0]+[int((-raw[j]/r[j]).upper().ceil().unique_fmpz()) for j in repair])
    w = [(x+lam*y)/lam for x,y in zip(raw,r)]
    level = arb(n)/lam
    assert all(w[j]>0 for j in repair)
    assert all(((n*w[j]-level).contains(0) if j in F else
                (w[j]>0 or j in active or n-j in active)) for j in range(n))
    price = (1-n*a*w[0])/level
    qF = sum(q[j] for j in F)
    bestF = sum(best[j] for j in F)
    assert (price-bestF).contains(0) and price-qF>arb(7712)/100000
    floor = arb(len(F))/n
    return dict(p=97,b=4,heads=F,exact_clipped_mass=bounds(qF-floor),
                full_cone_clipped_price=bounds(price-floor),forced_surcharge=bounds(price-qF),
                full_cone_law_level=bounds(level),full_cone_root_budget=bounds(1-n*a*w[0]),
                chosen_face_parameters=['1/1000','1/1000'],maximizer_binding=binding,
                units='1e-8',precision=ctx.prec)


if __name__ == '__main__':
    print(json.dumps(degenerate_face(),sort_keys=True),flush=True)
    for prime,time in [(101,4),(257,5),(409,6),(769,7)]:
        print(json.dumps(measure(prime,time),sort_keys=True),flush=True)
