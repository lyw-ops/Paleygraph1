"""Certify a positive balanced tilted cap, then integrate its real signed test."""

import json
from pathlib import Path
import runpy

from flint import acb, acb_mat, arb, arb_mat, ctx
import numpy as np

base = runpy.run_path(str(Path(__file__).with_name("astra-cold-37.py")))
ctx.prec = 256
K = base["even_kernel"](base["paley_sign"](173))
size = K.nrows()
mult = [1] + [2]*(size-2) + [1]
n = sum(mult)
a = 1/arb(2).sqrt()
s = n/acb(arb(1)/50, arb(17)/1000)
Kfloat = np.array(K.tolist(), dtype=float)


def propose(turn):
    row = np.zeros(size, complex)
    cap = float(a)
    for _ in range(800):
        q = (1+cap**2)*(row.imag**2/cap**2-row.real**2)/4
        active = q > 1
        active[0] = False
        totals = np.sqrt(4+row*row)
        totals[0] = np.sqrt(complex(s))*np.sqrt(4+row[0]**2/complex(s))
        totals[active] = np.sign(row.imag[active])*(
            row.imag[active]/cap + 1j*cap*row.real[active])
        row = (row+Kfloat@totals-1j*turn*(mult@totals)/n)/2
    return [arb(float(z)) for z in [*row.real, *row.imag, turn]]


def joint(x):
    turn = x[-1]
    row = [acb(x[i], x[size+i]) for i in range(size)]
    sums, dx, dy, charges = [], [], [], {}
    last = [arb(0)]*len(x)
    for i, z in enumerate(row):
        q = (1+a*a)*(z.imag**2/a**2-z.real**2)/4
        if i and q > 1:
            assert z.imag > 0 or z.imag < 0
            side = 1 if z.imag > 0 else -1
            charges[i] = side, q
            sums.append(side*acb(z.imag/a, a*z.real))
            dx.append(acb(0,side*a))
            dy.append(acb(side/a))
            last[i] = -side*mult[i]*(1+a*a)*z.real/2
            last[i+size] = side*mult[i]*(1+a*a)*z.imag/(2*a*a)
        else:
            assert not i or q < 1
            sums.append((4+z*z).sqrt() if i else s.sqrt()*(4+z*z/s).sqrt())
            dx.append(z/sums[-1])
            dy.append(acb(0,1)*dx[-1])
    assert all(w.real > abs(z.real) for w,z in zip(sums,row))
    assert all(abs((sums[0]+j*row[0]).arg()) < a.atan() for j in (-1,1))
    mean = sum((m*w for m,w in zip(mult,sums)), acb(0))/n
    residual = [z+acb(0,turn)*mean-sum((K[i,j]*sums[j] for j in range(size)),acb(0))
                for i,z in enumerate(row)]
    imbalance = sum(mult[i]*side*(q-1) for i,(side,q) in charges.items())
    jac = []
    for i in range(size):
        entries = []
        for j,d in enumerate(dx+dy):
            delta = acb(int(i==j), int(i+size==j))
            entries.append(delta-acb(K[i,j%size],-turn*mult[j%size]/n)*d)
        jac.append(entries+[acb(0,1)*mean])
    return (arb_mat(len(x),1,[z.real for z in residual]+[z.imag for z in residual]+[imbalance]),
            arb_mat([[z.real for z in r] for r in jac]+[[z.imag for z in r] for r in jac]+[last]),
            charges, row, sums)


def row_norm(matrix):
    return max(sum(abs(matrix[i,j]).upper() for j in range(matrix.ncols()))
               for i in range(matrix.nrows()))


def positive_logs(weights):
    trial = np.zeros(size)
    approx_w = np.array(weights, dtype=float)
    for _ in range(1200):
        trial = Kfloat @ np.sqrt(4*approx_w+trial*trial)
    z = [arb(float(v)) for v in trial]
    def system(vals):
        total = [(v*v+4*w).sqrt() for v,w in zip(vals,weights)]
        residual = arb_mat(size,1,[v-sum(K[i,j]*total[j] for j in range(size))
                                   for i,v in enumerate(vals)])
        jac = arb_mat([[int(i==j)-K[i,j]*vals[j]/total[j]
                        for j in range(size)] for i in range(size)])
        return residual,jac
    for _ in range(2):
        residual,jac = system(z)
        step = jac.solve(residual)
        z = [(v-step[i,0]).mid() for i,v in enumerate(z)]
    gap = arb('1e-17')
    tube = [v+arb(0,gap) for v in z]
    residual,jac = system(z)
    eye = arb_mat([[int(i==j) for j in range(size)] for i in range(size)])
    pre = jac.solve(eye).mid()
    assert row_norm(eye-pre*system(tube)[1]) < arb(1)/2
    assert row_norm(pre*residual) < gap/2
    return [(v/(2*w.sqrt())).asinh() for v,w in zip(tube,weights)]


def unforced_spread(seed):
    """Enclose a unit-bulk pair independently of the signed cap equations."""
    def system(row):
        totals = [(4+z*z).sqrt() if i else s.sqrt()*(4+z*z/s).sqrt()
                  for i,z in enumerate(row)]
        residual = acb_mat(size,1,[z-sum(K[i,j]*totals[j] for j in range(size))
                                   for i,z in enumerate(row)])
        jac = acb_mat([[int(i==j)-K[i,j]*row[j]/totals[j] for j in range(size)]
                       for i in range(size)])
        return residual,jac,totals
    row = [z.mid() for z in seed]
    for _ in range(10):
        residual,jac,_ = system(row)
        step = jac.solve(residual)
        row = [(v-step[i,0]).mid() for i,v in enumerate(row)]
    residual,jac,_ = system(row)
    eye = acb_mat([[int(i==j) for j in range(size)] for i in range(size)])
    pre = jac.solve(eye).mid()
    radius = arb("1e-22")
    box = acb(arb(0,radius),arb(0,radius))
    tube = [v+box for v in row]
    _,patch,totals = system(tube)
    assert row_norm(eye-pre*patch) < arb(1)/4 and row_norm(pre*residual) < radius/2
    A = [(w+z)/2 for z,w in zip(tube,totals)]
    B = [(w-z)/2 for z,w in zip(tube,totals)]
    assert all(v.real > 0 for v in A+B)
    angles = [(v.arg()-w.arg())/2 for v,w in zip(A,B)]
    assert all(angles[i] < angles[43] for i in range(size) if i!=43)
    assert all(angles[i] > angles[29] for i in range(size) if i!=29)
    spread = angles[43]-angles[29]
    assert spread > 2*a.atan() and spread+2*a.atan() < arb.pi()
    print(json.dumps(dict(kind="unit_bulk_spread_excludes_all_tilted_centers",precision=ctx.prec,
                          p=173,t_real="1/50",t_imag="17/1000",maximum_orbit=43,
                          minimum_orbit=29,spread=spread.str(15),
                          cap_diameter=(2*a.atan()).str(15)),sort_keys=True))


def cold_constants():
    theta = a.atan()
    edge = arb("0.01")
    amin, amax = (theta-edge).tan(), (theta+edge).tan()
    cold_x = arb(2031)/128
    cold_y = arb(2)**-17
    modulus = ((cold_x+cold_y)**2+cold_y**2).sqrt()
    assert amin > arb("0.69") and amax < arb("0.73")
    assert (theta+2*edge) < arb("0.64") and theta-2*edge > arb("0.59")
    last_preimage = arb("0.005377")
    assert arb("0.0028")+2*edge*last_preimage/(cold_x-cold_y).sqrt() < arb("0.00283")
    zmax, zim = arb("1.20"), arb("0.504")
    zsum = (4+zmax*zmax).sqrt()
    x, y = zmax+edge*zsum+arb("0.1")/amin, zim+edge*zsum+arb("0.1")
    assert x < arb("1.38") and y < arb("0.63")
    g = x/(2*(1-(y/2)**2).sqrt())
    assert g < arb("0.73") and (y/2).asin() < theta-edge
    det = ((1-2*arb("0.315")**2)**2-(1/arb("0.69")-arb("0.69"))**2*
           arb("0.63")**2/4)/(1+arb("0.73")**2)**2
    assert det > arb("0.24") and (1-det).sqrt() < arb("0.90")
    assert 2*((2+arb(10)**-30)*modulus).sqrt()*arb("1.1")/arb("0.64").cos() < 16
    mark_gain = arb("1.51").tanh()/arb("0.011").cos()**2+arb("0.011").tan()/amin
    assert mark_gain < arb("0.95")
    assert arb("0.01")-2*arb("0.00283") > arb("0.0043")
    assert 23*arb("1.01")**2/arb("0.0043") < 6000
    assert 2*(arb(6000).sqrt()+arb("0.0028")*6000)/amin < 300
    assert 1/(arb("0.36")-arb("0.10")/amin)**2/amin**2 < 60
    assert 2*arb.pi()/arb("0.10")+(zsum+zmax)/amin < 70
    assert 1/arb("0.039")**2/amin**2 < 2000
    assert arb(2000)*6000/2+75 < 7*arb(10)**6
    assert 2*arb("1.4e9")/(cold_x-cold_y) < arb("1.8e8")
    finite = arb("1.8e8")*arb("3.932e-175")**2
    limit = arb("1.8e8")*arb("3.06e-208")**2
    assert finite < arb("2.8e-341") and limit < arb("1.7e-407")
    print(json.dumps(dict(kind="quadratic_cap_cold_constants", precision=ctx.prec,
                          inner_radius="0.004", comparison_radius="0.01",
                          action_error_factor=7000000, side_quadratic_factor=1400000000,
                          physical_total_quadratic_factor=180000000,
                          finite_total_upper=finite.str(11), field_first_upper=limit.str(11)),
                     sort_keys=True))


def main():
    x = propose(0.1413)
    for _ in range(4):
        residual,jac,*_ = joint(x)
        step = jac.solve(residual)
        x = [(v-step[i,0]).mid() for i,v in enumerate(x)]
    radius = arb('1e-24')
    tube = [v+arb(0,radius) for v in x]
    residual,jac,*_ = joint(x)
    eye = arb_mat([[int(i==j) for j in range(len(x))] for i in range(len(x))])
    pre = jac.solve(eye).mid()
    _,patch,charges,row,sums = joint(tube)
    assert row_norm(eye-pre*patch) < arb(1)/2 and row_norm(pre*residual) < radius/2
    assert {i:side for i,(side,q) in charges.items()} == {29:-1,43:1}
    assert abs(tube[-1]) < a
    upper = charges[43][1]-1
    lower = 2*(charges[29][1]-1)
    assert (upper-lower).contains(0) and upper > arb('0.4150') and upper < arb('0.4151')
    b = tube[-1].atan()
    assert b > arb("0.14009") and b < arb("0.14010")
    print(json.dumps(dict(kind="genuine_balanced_rotated_cap",p=173,t_real="1/50",t_imag="17/1000",
                          tan_half_width="1/sqrt(2)",precision=ctx.prec,center=b.str(15),
                          upper_orbits=[43],lower_orbits=[29],upper_excess=upper.str(15),
                          lower_excess=lower.str(15)),sort_keys=True))
    unforced_spread([b.cos()*z+acb(0,b.sin())*w for z,w in zip(row,sums)])
    A = [(w+z)/2 for w,z in zip(sums,row)]
    B = [(w-z)/2 for w,z in zip(sums,row)]
    def pair(z,sign):
        return z.real+sign*z.imag/a
    pp,pm = [[pair(z,side) for z in A] for side in (1,-1)]
    qp,qm = [[pair(z,side) for z in B] for side in (1,-1)]
    tau_p, tau_m = pp[0]*qp[0], pm[0]*qm[0]
    assert tau_m > tau_p > 0
    assert (tau_p-tau_m-2*s.imag/a).contains(0)
    profile = [x*y for x,y in zip(pp,qp)]
    assert all(z > 0 for i,z in enumerate(profile) if i not in charges)
    profile[43],profile[29] = arb(1), arb(1)/2
    gammas = [positive_logs([tau]+profile[1:]) for tau in (tau_p,tau_m)]
    diff = [l-r for l,r in zip(*gammas)]
    integral = diff[43]-diff[29]
    c = 4/(1+a*a)
    bound = (c*charges[43][1]).log() + (2*c*charges[29][1]).log()
    assert integral > bound > 3
    print(json.dumps(dict(kind="balanced_cap_real_signed_dipole",precision=ctx.prec,p=173,
                          upper_lift="1",each_lower_lift="1/2",integral=integral.str(15),
                          lower=bound.str(15),real_mark_plus=tau_p.str(12),
                          real_mark_minus=tau_m.str(12)),sort_keys=True))


if __name__=="__main__":
    cold_constants()
    main()
