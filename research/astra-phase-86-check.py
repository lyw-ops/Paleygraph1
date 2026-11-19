"""Enclose the first right-angle spread of the real-start stationary row at p=173."""
from fractions import Fraction
import json
from pathlib import Path
import runpy

import numpy as np
from flint import acb, acb_mat, arb

src = runpy.run_path(str(Path(__file__).with_name("astra-cold-37-monodromy.py")))
base, n, count = src["base"], src["n"], src["N"]
rat, K = src["rat"], src["K"]
x = Fraction(1, 50)
first, last = Fraction(2158, 100000), Fraction(2161, 100000)
upper_site, lower_site = 43, 29
half_pi = arb.pi() / 2
outer = (arb(3) / 2).atan()
stats = {"before": 0, "crossing": 0, "after": 0}
derivatives = []


def rectangle(left, right, radius):
    error = acb(arb(0, radius), arb(0, radius))
    return [acb(a.real.union(b.real), a.imag.union(b.imag)) + error
            for a, b in zip(left, right)]


def tube_data(start, end, left, right, radius):
    s = rectangle(left[0], right[0], radius)
    v = rectangle(left[1], right[1], (src["knorm"] * radius).upper())
    t = acb(rat(x), rat(start).union(rat(end)))
    scale = (t / n).sqrt()
    factors = [(a + b) / (2 * (1 if j == 0 else scale)) for j, (a,b) in enumerate(zip(s,v))]
    if any(not a.real > 0 for a in factors):
        return None
    return s, v, [a.arg() for a in factors]


def interior(phase):
    return max(a.upper() for a in phase) - min(a.lower() for a in phase) < half_pi


def crossing_slope(s, v, phase):
    if not all(a > -outer and a < outer for a in phase):
        return None
    if any(not phase[upper_site] > p for j,p in enumerate(phase) if j != upper_site):
        return None
    if any(not phase[lower_site] < p for j,p in enumerate(phase) if j != lower_site):
        return None
    rhs = src["col"]([acb(0)] + [acb(0,arb(4)/n)]*(count-1))
    try:
        ds = src["jac"](s,v).solve(rhs)
    except ZeroDivisionError:
        return None
    dv = K * ds
    def unscaled_log_derivative(j):
        return (ds[j,0]+dv[j,0])/(s[j]+v[j])
    # The two extreme sites are bulk, so their square-root scale derivatives cancel.
    slope = (unscaled_log_derivative(upper_site) - unscaled_log_derivative(lower_site)).imag
    return slope if slope > 55 and slope < 65 else None


def walk(start, end, seed, left, mode, depth=0):
    assert depth < 28
    proposal = src["numeric_root"](seed,(x,end))
    right = src["anchor"](proposal,(x,end))
    certificate = src["tube"](seed,proposal,left,right)
    if certificate:
        radius, _ = certificate
        data = tube_data(start,end,left,right,radius)
        if data:
            if mode == "before":
                accepted = interior(data[2]) and all(a > -outer and a < outer for a in data[2])
            elif mode == "after":
                accepted = True
            else:
                slope = crossing_slope(*data)
                accepted = slope is not None
                if accepted:
                    derivatives.append(slope)
            if accepted:
                stats[mode] += 1
                return proposal,right,radius
    middle = (start+end)/2
    middle_seed, anchor, _ = walk(start,middle,seed,left,mode,depth+1)
    return walk(middle,end,middle_seed,anchor,mode,depth+1)


def main():
    weights = [arb(4)] + [4*rat(x)/n]*(count-1)
    v = base["real_root"](src["Kr"],src["sign"],rat(x),weights)
    real = [(a*a+w).sqrt() for a,w in zip(v,weights)]
    seed = np.array([complex(float(a),0) for a in real])
    left = src["anchor"](seed,(x,Fraction(0)))
    assert src["vmax"]([acb(a)-b for a,b in zip(real,left[0])]) < arb(2)**-40
    seed,left,_ = walk(Fraction(0),first,seed,left,"before")
    seed,left,_ = walk(first,last,seed,left,"crossing")
    seed,left,radius = walk(last,last,seed,left,"crossing")
    _,_,phase = tube_data(last,last,left,left,radius)
    graph = phase[upper_site] - phase[lower_site]
    assert graph > half_pi
    print(json.dumps(dict(kind="first_unforced_spread_contact",prime=173,real=str(x),
        imag_open_bracket=[str(first),str(last)],minimum_sites=[lower_site,n-lower_site],
        maximum_sites=[upper_site],spread_slope_outer_bounds=[55,65],
        spread_slope_enclosure=min(d.lower() for d in derivatives).union(
            max(d.upper() for d in derivatives)).str(12),
        final_spread=graph.str(12),phase_enlarged_sector_through_contact=True,
        segments={k:stats[k] for k in ["before","crossing"]},precision=src["ctx"].prec),
        sort_keys=True))
    after = Fraction(11,500)
    seed,left,_ = walk(last,after,seed,left,"after")
    seed,left,radius = walk(after,after,seed,left,"after")
    _,_,phase = tube_data(after,after,left,left,radius)
    certify_projected_return(after,phase)


def certify_projected_return(y, phase):
    t = acb(rat(x),rat(y))
    orientation, gap = rat("0.38"),rat("0.001")
    rows = [[],[],[]]
    diagonal = []
    for j,phi in enumerate(phase):
        multiplicity = 1 if j in [0,count-1] else 2
        weight = acb(n) if j == 0 else t
        scale = (multiplicity*abs(weight)).sqrt()
        w = acb(0,2*phi).exp()
        for row,val in zip(rows,[w,w.conjugate(),weight/abs(weight)]):
            row.append(scale*val)
        diagonal.append((2*phi-orientation).cos())
    negatives = [i for i,d in enumerate(diagonal) if d < 0]
    assert negatives == [lower_site,upper_site] and all(d < 0 or d > 0 for d in diagonal)
    M = acb_mat(rows)
    H = 10*(M.conjugate().transpose()*M)
    for j,d in enumerate(diagonal):
        H[j,j] += d - gap
    # Float Cholesky only proposes a preconditioner. Its dyadic entries and the
    # entire norm of I-P(H-gap I)P* are verified in complex ball arithmetic.
    floating = np.array([[complex(H[i,j]) for j in range(count)] for i in range(count)])
    inv = np.linalg.inv(np.linalg.cholesky(floating))
    P = acb_mat([[src["ac"](v) for v in row] for row in inv])
    error = src["matnorm"](src["eye"] - P*H*P.conjugate().transpose())
    assert error < rat("0.01")
    assert phase[upper_site] > outer
    print(json.dumps(dict(kind="unforced_post_contact_moment_compression",prime=173,
        real=str(x),imag=str(y),raw_negative_orbits=negatives,penalty=10,
        orientation=str(orientation.mid()),even_eigenvalue_lower="0.001",
        preconditioned_error_upper=error.str(12),enlarged_sector_exited=True,
        additional_segments=stats["after"]),sort_keys=True))


def forced_constants():
    L = rat("2031/128") - arb(2)**-17
    eta = arb(2)**-17
    gamma = eta / (2*L)
    beta = eta**2 / (4*L*(1+L))
    x_im = 2 + rat("4.768")*gamma
    secant = arb(870).sqrt() + rat("0.011") * 870
    def charge_excess(r):
        return (x_im*r+secant*r*r)/2
    cap = beta + charge_excess(rat("0.011"))
    limiting = charge_excess(rat("3.06e-208"))
    assert cap < rat("0.014") and cap < (rat("0.12").sin())**2
    assert limiting < rat("3.07e-208")
    for k in [1,2]:
        assert (2*k*L).sqrt() > rat("5.63")*arb(k).sqrt()
    print(json.dumps(dict(kind="height_600_forced_phase_charge",square_half_width="1/131072",
        gamma_upper=gamma.str(12),unforced_normalized_budget_upper=beta.str(12),
        forced_normalized_budget_upper=cap.str(12),limiting_excess_upper=limiting.str(12),
        marked_phase_abs_upper="0.12",single_orbit_residual_lower_per_sqrt_cardinality="5.63"),
        sort_keys=True))


if __name__ == "__main__":
    forced_constants()
    main()
