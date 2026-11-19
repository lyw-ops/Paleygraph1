"""Check the real-column transfer on an actual cold ray, with Arb enclosures."""
import json
from pathlib import Path
import runpy

import numpy as np
from flint import acb, arb, ctx

base = runpy.run_path(str(Path(__file__).with_name('astra-cold-37.py')))
ctx.prec = 256
sign = base['paley_sign'](173)
n = len(sign)
K = base['even_kernel'](sign)
size = K.nrows()
mult = [1, *([2] * (size - 2)), 1]
Kfloat = np.array([[float(K[i, j]) for j in range(size)] for i in range(size)])
a = 1 / arb(2).sqrt()
x = arb(2031) / 128
y = arb(2)**-17


def positive_sheet(weights, radius, real=False):
    convert = float if real else complex
    proposed = np.zeros(size, dtype=float if real else complex)
    w = np.array([convert(z) for z in weights])
    for _ in range(70):
        proposed = Kfloat @ np.sqrt(proposed**2 + 4*w)
    center = [arb(float(z)) if real else acb(arb(z.real), arb(z.imag)) for z in proposed]
    # Refine the approximate point with arithmetic at the full working precision.
    for _ in range(70):
        total = [(u*u + 4*b).sqrt() for u, b in zip(center, weights)]
        center = [sum((K[i, j]*total[j].mid() for j in range(size)), 0).mid()
                  for i in range(size)]
    total = [(u*u + 4*b).sqrt() for u, b in zip(center, weights)]
    res = [sum((K[i,j]*total[j] for j in range(size)), 0)-center[i] for i in range(size)]
    error = sum((m*abs(r).upper()**2 for m, r in zip(mult, res)), arb(0)).sqrt()
    box = arb(0, radius) if real else acb(arb(0, radius), arb(0, radius))
    enclosed = [u+box for u in center]
    outer = [(u*u+4*b).sqrt() for u,b in zip(enclosed, weights)]
    lip = max(abs(u/v).upper() for u,v in zip(enclosed, outer))
    assert all(z.real > 0 for z in outer) and lip < 1 and error < (1-lip)*radius
    return enclosed, outer


def weighted(lambdas, values):
    return sum((m*w*v for m,w,v in zip(mult,lambdas,values)), arb(0))


def main():
    # A single contraction neighborhood identifies the complex endpoint with the real start.
    s_range = n/acb(x, arb(0).union(y))
    tube, tube_total = positive_sheet([s_range]+[acb(1)]*(size-1), arb('0.0001'))
    for u, v in zip(tube, tube_total):
        assert all(f.real > 0 and abs(f.imag) < a*f.real for f in (v+u, v-u))
    z, total = positive_sheet([n/acb(x,y)]+[acb(1)]*(size-1), arb('1e-53'))
    assert sum((m*abs(point-t.mid()).upper()**2 for m,point,t in zip(mult,z,tube)),
               arb(0)).sqrt() < arb("0.0001")
    A = [(u+w)/2 for u,w in zip(total,z)]
    B = [(u-w)/2 for u,w in zip(total,z)]
    assert all(z.real > 0 for z in A+B)
    p_plus = [z.real+z.imag/a for z in A]
    p_minus = [z.real-z.imag/a for z in A]
    q_plus = [z.real+z.imag/a for z in B]
    q_minus = [z.real-z.imag/a for z in B]
    k = [p*q for p,q in zip(p_plus,q_plus)]
    assert all(v > 0 for v in p_plus+p_minus+q_plus+q_minus)
    assert all((v-p*q).contains(0) for v,p,q in zip(k[1:],p_minus[1:],q_minus[1:]))
    eps = 1-arb(2)*arb(10)**-14
    subset = [i for i in range(1,size) if k[i]<eps]
    assert all(k[i] > eps for i in range(1,size) if i not in subset)
    assert subset == [5,16,24,34,35,36]
    label = [0 if i not in subset else (1 if A[i].imag > 0 else -1) for i in range(size)]
    assert all(label[i]*A[i].imag > 0 for i in subset)
    mass = [eps-k[i] if i in subset else arb(0) for i in range(size)]
    norm = weighted(mass,[1]*size)
    lam = [v/norm for v in mass]
    bulk = [eps if i in subset else k[i] for i in range(1,size)]
    tau = [k[0],p_minus[0]*q_minus[0]]
    gammas = []
    for t in tau:
        sol, _ = positive_sheet([t]+bulk, arb('1e-44'), real=True)
        gammas.append([(u/(2*w.sqrt())).asinh() for u,w in zip(sol,[t]+bulk)])
    lhs = eps.sqrt()*weighted(lam,[s*(gp-gm) for s,gp,gm in zip(label,*gammas)])
    favorable = [p_plus[i]*q_minus[i] if label[i]==1 else q_plus[i]*p_minus[i]
                 for i in range(size)]
    rhs = eps.sqrt()*weighted(lam,[(v/eps).log() for v in favorable])
    simple = 2*eps.sqrt()*(((1-eps)/(1+eps/2)).sqrt()).atanh()
    assert lhs > rhs > simple > 0
    ds_abs = tau[1].sqrt()-tau[0].sqrt()
    assert ds_abs > 0
    # Differentiate the unweighted-coordinate physical real equation on the entire interval.
    tau_box = tau[0].union(tau[1])
    u,v = positive_sheet([tau_box]+bulk,arb('0.0001'),real=True)
    d = [ui/vi for ui,vi in zip(u,v)]
    jac = base['system'](K,d,False)
    du = jac.solve(base['column']([K[i,0]*4*tau_box.sqrt()/v[0] for i in range(size)]))
    signed = -eps.sqrt()*weighted(lam,[s*h/t for s,h,t in zip(label,du.entries(),v)])
    assert signed > 0 and (lhs/ds_abs-signed).contains(0)
    print(json.dumps(dict(kind='actual_cold_floor_real_transfer',prime=173,real='2031/128',
        imag='1/131072',precision=ctx.prec,epsilon='1-2e-14',selected_even_orbits=subset,
        full_sites=sum(mult[i] for i in subset),incoming_integral=lhs.str(17),
        phase_bound=rhs.str(17),threshold_bound=simple.str(17),
        scaled_oriented_column_whole_real_interval=(arb(n).sqrt()*signed).str(6),
        endpoint_secant_and_direct_interval_derivative_overlap=True),sort_keys=True))
    # Re-solve at the same two marks with exactly ordinary unit bulk throughout.
    flat_logs = []
    for t in tau:
        sol, _ = positive_sheet([t]+[arb(1)]*(size-1), arb('1e-44'), real=True)
        flat_logs.append([(u/2).asinh() for u in sol[1:]])
    G = [gp-gm for gp,gm in zip(*flat_logs)]
    zphase = [w.imag/abs(w) for w in A[1:]]
    balance = arb(0)
    quartic_G = arb(0)
    quartic_z = arb(0)
    paying = 0
    for i, (g, v) in enumerate(zip(G,zphase), 1):
        first = p_plus[i]*q_minus[i]*(-g).exp()
        second = q_plus[i]*p_minus[i]*g.exp()
        upper = (first+second+abs(first-second))/2
        price = upper.log()
        assert price < 0 or price > 0
        if price < 0:
            paying += mult[i]
        balance += mult[i]*v**2*price
        quartic_G += mult[i]*g**4
        quartic_z += mult[i]*v**4
    assert balance < 0 and quartic_z < (arb(21)/5)*quartic_G
    print(json.dumps(dict(kind='actual_cold_floor_unit_bulk_fourth_power_transfer',
        prime=173, real='2031/128', imag='1/131072', precision=ctx.prec,
        full_sites_paying=paying, signed_balance=balance.str(14),
        phase_fourth_sum=quartic_z.str(14), real_integral_fourth_sum=quartic_G.str(14)),
        sort_keys=True))
    cold_min=x-y
    for delta in [arb(3)/4,arb(10)**-8]:
        e=1-delta
        c=2*e.sqrt()*(delta/(1+e/2)).sqrt().atanh()
        coefficient=c*a*cold_min*cold_min.sqrt()*(1-y/(a*cold_min)).sqrt()
        print(json.dumps(dict(kind='cold_first_contact_necessary_constant',
              bulk_min=e.str(14),coefficient_times_inverse_abs_y=coefficient.str(12),
              minimum_scaled_column_on_square=(coefficient/y).str(12)),sort_keys=True))


if __name__=='__main__':
    main()
