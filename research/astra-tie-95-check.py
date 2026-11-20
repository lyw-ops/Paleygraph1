"""Arb checks for the real fixed profile and its signed cold comparison."""
import json
from pathlib import Path
import runpy

from flint import acb, arb, ctx

base = runpy.run_path(str(Path(__file__).with_name("astra-velocity-92-check.py")))
ctx.prec = 256
a, x, y, n, size, mult, solve = (base[key] for key in
    ("a", "x", "y", "n", "size", "mult", "positive_sheet"))


def norm(rows):
    return sum((m*z*z for m, z in zip(mult[1:], rows)), arb(0)).sqrt()


def cold_constants(delta):
    q = (1-delta).sqrt()
    rho = y/(a*(x-y))
    shift = 3*rho/(1-rho)
    lip = a*(3*delta).sqrt()/(2*q)
    contraction = lip*(2+2*shift)/q
    defect = ((3*delta).sqrt()/q * a/(q*(arb(2)/3).sqrt()).sqrt()
              + 2*lip*shift/q)
    displacement = defect/(1-contraction)
    price = (1+displacement)**2*(1+shift**2)-1
    return shift, contraction, displacement, price


def constants():
    delta = arb(10)**-8
    shift, contraction, displacement, price = cold_constants(delta)
    beta = arb("0.013")
    fraction = (beta-price)/(1+beta)
    assert shift < arb("2.05e-6")
    assert contraction < arb("0.000123") and displacement < arb("0.000136")
    assert price < arb("0.000273") and fraction > arb("0.01256")
    threshold = 2*(1-delta).sqrt() * (2*delta/(3-delta)).sqrt().atanh()
    scaled = threshold*a*(x-y)**arb("1.5")*(1-y/(a*(x-y))).sqrt()/y
    assert scaled > arb("956.59")
    wide = arb(27)/100
    wide_mark = 2*wide.sqrt()*((1-wide)/(1+wide/2)).sqrt().atanh()
    wide_scaled = wide_mark*a*(x-y)**arb("1.5")*(1-y/(a*(x-y))).sqrt()/y
    assert wide_scaled > arb("6.72e6")
    ka = (3*(1+a*a)).sqrt()/(1-a)
    def tie_price(e):
        return e/(ka+1+((ka+1)**2-(ka**2-1)*e).sqrt())
    near_price, wide_price = tie_price(1-delta), tie_price(wide)
    assert near_price > arb("0.08128") and wide_price > arb("0.01731")
    print(json.dumps(dict(kind="prime_uniform_fixed_profile", lipschitz=contraction.str(14),
                          displacement_per_root_budget=displacement.str(14),
                          excess_budget_ratio=price.str(14),
                          retained_actual_deficit_fraction=fraction.str(14),
                          unlabelled_scaled_column=scaled.str(14), wide_scaled_column=wide_scaled.str(14),
                          tie_root_price_near=near_price.str(14), tie_root_price_wide=wide_price.str(14)), sort_keys=True))


def physical_test():
    s = n/acb(x,y)
    u, d = s.real, s.imag/a
    delta = 2*arb(10)**-14
    qfloor = (1-delta).sqrt()
    shift, contraction, _, _ = cold_constants(delta)
    lip = a*(3*delta).sqrt()/(2*qfloor)

    def pair(mark, q):
        weights = [mark, *(z*z for z in q)]
        row, _ = solve(weights, arb("1e-49"), real=True)
        return [(v/(2*w.sqrt())).asinh() for v,w in zip(row,weights)]

    def endpoints(h, q):
        plus, minus = pair(h+d,q), pair(h-d,q)
        return [a-b for a,b in zip(plus,minus)]

    def fmap(q):
        h = u.mid()
        for _ in range(3):
            logs = endpoints(h,q)
            f = (1-a*a)*h/2+(1+a*a)*(h*h-d*d).sqrt()*logs[0].cosh()/2
            h = (h+u-f).mid()
        logs = endpoints(h,q)
        f = (1-a*a)*h/2+(1+a*a)*(h*h-d*d).sqrt()*logs[0].cosh()/2
        herror = 2*abs(f-u).upper()/(1-a*a)
        hlow = min(u.lower(),h.lower())-abs(d).upper()
        # Both true and trial marks are positive. Integrate the marked derivative.
        gerr = herror/(qfloor*hlow.sqrt())
        logs = [z+arb(0,gerr.upper()) for z in logs[1:]]
        qnext = []
        selected = []
        for i,z in enumerate(logs,1):
            natural = 1/(1+(1+a*a)*(z/2).sinh()**2).sqrt()
            assert natural < qfloor or natural > qfloor
            if natural < qfloor:
                selected.append(i)
            qnext.append(natural.max(qfloor))
        return qnext, logs, h+arb(0,herror.upper()), selected

    q = [arb(1)]*(size-1)
    for _ in range(2):
        values, _, _, active = fmap(q)
        q = [qfloor if i in active else z.mid() for i,z in enumerate(values,1)]
        assert all(qfloor < z < 1 for i,z in enumerate(q,1) if i not in active)
    qnext, logs, h, selected = fmap(q)
    error = norm([z-t for z,t in zip(qnext,q)]).upper()/(1-contraction)
    assert error < arb("1.51e-41")
    gerror = (2+2*shift)/qfloor*error
    logs = [g+arb(0,gerror.upper()) for g in logs]
    weights = [1+(1+a*a)*(g/2).sinh()**2 for g in logs]
    active = [i for i,w in enumerate(weights,1) if w*qfloor*qfloor>1]
    assert active == selected and all(weights[i-1]*qfloor*qfloor<1
                                      for i in range(1,size) if i not in active)
    prices = [(qfloor*w.sqrt()-1) if i in active else arb(0)
              for i,w in enumerate(weights,1)]
    assert all(prices[i-1]>0 for i in active)
    total = norm(prices)
    assert active == [5,16,24,34,35,36] and sum(mult[i] for i in active)==12
    assert arb("2.8828e-15") < total < arb("2.8829e-15")
    print(json.dumps(dict(kind="genuine_nominated_floor_nontrivial_fixed_profile",
                          prime=173, floor="2031/128+i/131072", delta="2e-14",
                          iteration_error_counting_l2=error.str(11),
                          real_mark_midpoint_near=h.str(16), active_orbits=active,
                          full_active_sites=sum(mult[i] for i in active),
                          l2_reconstructed_root_product_excess=total.str(13)),
                     sort_keys=True))


def small_floor_contact():
    # The R91 contact certificate puts the actual first tie in this interval.
    contact_imag = arb("0.01294720").union(arb("0.01294721"))
    s = n/acb(arb(1)/50,contact_imag)
    u, d = s.real, s.imag/a
    e = 1-arb(10)**-8
    trial = arb("3899.4")

    def flat_logs(mark):
        mid = mark.mid()
        weights = [arb(4)]+[4*e/mid]*(size-1)
        row = base["base"]["real_root"](base["K"],base["sign"],n*e/mid,weights)
        radius = abs(mark.sqrt()-mid.sqrt()).upper()
        # At a varying mark r^2, the bulk log derivative is at most 1/sqrt(e)
        # and the marked one is at most 1/r. The stationary logs are scale invariant.
        return [(v/w.sqrt()).asinh()+arb(0,(radius/(mark.sqrt().lower() if i==0
                                                    else e.sqrt())).upper())
                for i,(v,w) in enumerate(zip(row,weights))]

    gp, gm = flat_logs(trial+d), flat_logs(trial-d)
    gap = trial/4 + 3*(trial*trial-d*d).sqrt()*(gp[0]-gm[0]).cosh()/4-u
    midpoint = trial+arb(0,4*abs(gap).upper())
    gp, gm = flat_logs(midpoint+d), flat_logs(midpoint-d)
    logs = [x-y for x,y in zip(gp[1:],gm[1:])]
    roots = [(e*(1+(1+a*a)*(g/2).sinh()**2)).sqrt() for g in logs]
    assert all(z>1 for z in roots)
    # Each trial bulk square root is the cutoff itself, hence this is an
    # exact fixed point for every floor in the certified contact bracket.
    price = norm([z-1 for z in roots])
    assert arb("1.50") < price < arb("1.54")
    print(json.dumps(dict(kind="real_fixed_profile_on_certified_true_tie_bracket",
                          prime=173, real="1/50", imag=["0.01294720","0.01294721"],
                          delta="1e-8", full_active_sites=n-1, true_tied_site=43,
                          marked_midpoint=midpoint.str(9),
                          root_excess_counting_norm=price.str(7)),sort_keys=True))


if __name__ == "__main__":
    constants()
    physical_test()
    small_floor_contact()
