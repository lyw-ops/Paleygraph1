"""Arb check of the first-tie deficit quantile and the signed square on a cold ray."""
from fractions import Fraction
import json
from pathlib import Path
import runpy

from flint import acb, arb, ctx
import numpy as np

old = runpy.run_path(str(Path(__file__).with_name("astra-velocity-92-check.py")))
ctx.prec = 256
a, x, y, n, size, mult = (old[key] for key in ("a", "x", "y", "n", "size", "mult"))
solve = old["positive_sheet"]


def record(kind, **data):
    print(json.dumps(dict(kind=kind, precision=ctx.prec, **data), sort_keys=True))


def constants():
    delta = arb(10)**-8
    e = 1-delta
    q = e.sqrt()
    rho = arb(99)/100
    g = (rho*(2*delta/(3-delta)).sqrt()).atanh()
    cut = arb(1)/100
    small = (2*q*(1-cut**2/3).sqrt()*(1-rho**2)/(3-delta)
             - cut**2/(q+(1-cut**2).sqrt())**2)
    large = (1-2*q*(1-(arb(2)/3).sqrt())
             - 2*q*(arb(2)/3).sqrt()*g.sinh()/cut
             - (1-q)**2/cut**2)
    beta = arb(13)/1000
    assert small > beta and large > beta
    scaled = 2*q*g*a*(x-y)**arb("1.5")*(1-y/(a*(x-y))).sqrt()/y
    assert scaled > arb('947.03') and beta/(1+beta) > arb(128)/10000
    record("cold_selected_deficit_quantile_constants",
           floor="2031/128", delta="1e-8", rho="99/100",
           local_net_price_small=small.str(13), local_net_price_large=large.str(13),
           qualifying_deficit_fraction_lower=(beta/(1+beta)).str(13),
           qualifying_scaled_interval_average_lower=scaled.str(13))


def physical_replay():
    tube, sums = solve([n/acb(x,arb(0).union(y))]+[acb(1)]*(size-1), arb("0.0001"))
    for u, v in zip(tube, sums):
        assert all(f.real > 0 and abs(f.imag) < a*f.real for f in (v+u,v-u))
    u, v = solve([n/acb(x,y)]+[acb(1)]*(size-1), arb("1e-53"))
    assert sum(m*abs(row-mid.mid()).upper()**2 for m,row,mid in zip(mult,u,tube)).sqrt() < arb("0.0001")
    A = [(v0+u0)/2 for u0,v0 in zip(u,v)]
    B = [(v0-u0)/2 for u0,v0 in zip(u,v)]
    P = [[v.real+s*v.imag/a for v in A] for s in (1,-1)]
    Q = [[v.real+s*v.imag/a for v in B] for s in (1,-1)]
    for row in P+Q:
        assert all(v>0 for v in row)
    k = [p*q for p,q in zip(P[0][1:], Q[0][1:])]
    for w,p,q in zip(k, P[1][1:],Q[1][1:]):
        assert (w-p*q).contains(0)
    e = 1-arb(2)*arb(10)**-14
    selected = [i for i,w in enumerate(k) if w<e]
    assert all(k[i]>e for i in range(len(k)) if i not in selected)
    kp = [e if i in selected else w for i,w in enumerate(k)]
    tau = [p[0]*q[0] for p,q in zip(P,Q)]
    gs = []
    mean_price = arb(0)
    mark_price = arb(0)
    for p,q,t in zip(P,Q,tau):
        weights = [t]+kp
        uu, vv = solve(weights, arb("1e-45"), real=True)
        gs.append([(b/(2*w.sqrt())).asinh() for b,w in zip(uu,weights)])
        aa, bb = (vv[0]+uu[0])/2, (vv[0]-uu[0])/2
        mark_price += ((aa*q[0]).sqrt()-(p[0]*bb).sqrt())**2/2
        mean_price += (sum(m*w for m,w in zip(mult,weights)).sqrt()
                       -sum(m*w for m,w in zip(mult,[t]+k)).sqrt())**2/2
    budget = arb(0)
    loss = arb(0)
    average_amp_price = arb(0)
    mass = arb(0)
    qualifying = arb(0)
    rho = arb(99)/100
    threshold = 2*(rho*(2*(1-e)/(2+e)).sqrt()).atanh()
    for i,(w,wp) in enumerate(zip(k,kp),1):
        z = A[i].imag / abs(A[i])
        nu = A[i].real / abs(A[i])
        a0 = nu+z/a
        b0 = nu-z/a
        assert (w-a0*b0).contains(0)
        g = gs[0][i]-gs[1][i]
        rp = a0.sqrt()*(-g/4).exp()
        rm = b0.sqrt()*(g/4).exp()
        loss += mult[i]*wp.sqrt()*(rp-rm)**2
        amp_diff = (gs[0][i]+gs[1][i])/2-(abs(A[i])/abs(B[i])).log()/2
        average_amp_price += mult[i]*wp.sqrt()*(rp**2+rm**2)*2*(amp_diff/2).sinh()**2
        if i-1 in selected:
            budget += mult[i]*(wp.sqrt()-w.sqrt())**2
            weight = mult[i]*(e-w)
            mass += weight
            signed = g if z>0 else -g
            assert signed>threshold or signed<threshold
            if signed>threshold:
                qualifying += weight
    reconstructed = loss+average_amp_price+mark_price+mean_price
    assert budget.is_finite() and reconstructed.is_finite() and (budget-reconstructed).contains(0)
    assert 0<loss and loss<budget and (qualifying/mass-1).contains(0)
    record("physical_nominated_ray_signed_square", prime=173, floor="2031/128+i/131072",
           selected_e="1-2e-14", full_selected_sites=sum(mult[i+1] for i in selected),
           squared_root_budget=budget.str(12), signed_square_loss=loss.str(12),
           mean_change_price=mean_price.str(12), marked_price=mark_price.str(12),
           bulk_log_midpoint_price=average_amp_price.str(12), four_terms_recover_budget=True,
           qualifying_fraction=(qualifying/mass).str(12), tie=False)



def physical_first_tie():
    contact = runpy.run_path(str(Path(__file__).with_name("astra-contact-91-check.py")))
    src = contact["src"]
    rat, x0 = src["rat"], contact["x"]
    weights = [arb(4)] + [4*rat(x0)/n]*(size-1)
    physical = src["base"]["real_root"](src["Kr"], src["sign"], rat(x0), weights)
    sums = [(u*u+w).sqrt() for u,w in zip(physical, weights)]
    start = np.array([complex(float(row),0) for row in sums])
    left = src["anchor"](start,(x0,Fraction(0)))
    assert src["vmax"]([acb(row)-enclosed for row,enclosed in zip(sums,left[0])]) < arb(2)**-40
    start, left = contact["walk"](Fraction(0), contact["broad"], start, left, "before")
    start, left = contact["walk"](contact["broad"], contact["low"], start, left, "approach")
    assert contact["point_angle"](contact["low"], start, left) < contact["cap"]
    end = src["numeric_root"](start, (x0,contact["high"]))
    right = src["anchor"](end, (x0,contact["high"]))
    radius = src["tube"](start, end, left, right)[0]
    assert contact["bounds"](contact["low"], contact["high"],left,right,radius,"contact")
    assert contact["point_angle"](contact["high"], end, right) > contact["cap"]
    sums, diff, angles = contact["phase"]["tube_data"](contact["low"],contact["high"],left,right,radius)
    t = acb(rat(x0), rat(contact["low"]).union(rat(contact["high"])))
    scale = (t/n).sqrt()
    A0, B0 = (sums[0]+diff[0])/(2*scale), (sums[0]-diff[0])/(2*scale)
    tau = [(A0.real+s*A0.imag/a)*(B0.real+s*B0.imag/a) for s in (1,-1)]
    e = 1-arb(10)**-8
    k = [1-3*ang.sin()**2 for ang in angles[1:-1]] + [arb(0)]
    assert all(v<e for v in k) and all(v>0 for v in k[:-1])
    logs = []
    for mark in tau:
        mid = mark.mid()
        floor = n*e/mid
        weights = [arb(4)]+[4*e/mid]*(size-1)
        row = src["base"]["real_root"](src["Kr"],src["sign"],floor,weights)
        # Each bulk log derivative in the square-root mark is bounded by 1/sqrt(e).
        width = (mark.sqrt()-mid.sqrt()).abs_upper()/e.sqrt()
        logs.append([(v/(2*(e/mid).sqrt())).asinh()+arb(0,width) for v in row[1:]])
    G = [gp-gm for gp,gm in zip(*logs)]
    threshold = 2*(arb("0.99")*(2*(1-e)/(2+e)).sqrt()).atanh()
    budget, loss, qualified_mass, total_mass = (arb(0) for _ in range(4))
    wrong = []
    for i,(ang,g,ki) in enumerate(zip(angles[1:],G,k),1):
        z, nu = ang.sin(), ang.cos()
        if i==size-1:
            left_factor, right_factor = 2*(arb(2)/3).sqrt(), arb(0)
        else:
            left_factor, right_factor = nu+z/a, nu-z/a
        d = left_factor.sqrt()*(-g/4).exp()-right_factor.sqrt()*(g/4).exp()
        b = e.sqrt()-ki.sqrt()
        loss += mult[i]*e.sqrt()*d*d
        budget += mult[i]*b*b
        weight = mult[i]*(e-ki)
        total_mass += weight
        sign = 1 if ang>0 else -1
        assert sign*ang>0
        if sign*g>threshold:
            qualified_mass += weight
        else:
            assert sign*g<0
            wrong.append(i)
    assert wrong==[9] and arb('0.9995')<qualified_mass/total_mass<1
    assert loss>0 and loss<budget
    record("actual_small_floor_first_tie_signed_quantile",prime=173,real=str(x0),
           imag_open_bracket=[str(contact["low"]),str(contact["high"])],tied_site=43,
           e="1-1e-8",qualifying_deficit_fraction=(qualified_mass/total_mass).str(6),
           full_selected_sites=n-1,full_qualifying_sites=n-1-sum(mult[i] for i in wrong),
           opposite_sign_even_orbits=wrong,tie_signed_log_difference=G[-1].str(7),
           signed_square_loss=loss.str(6),squared_root_budget=budget.str(7))


if __name__ == "__main__":
    constants()
    physical_replay()
    physical_first_tie()
