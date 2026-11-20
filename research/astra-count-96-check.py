"""Outward arithmetic for the stripped marked-column test at first comparison contact."""
import json
from pathlib import Path
import runpy

from flint import acb, arb, arb_mat, ctx

HERE = Path(__file__).resolve().parent
base = runpy.run_path(str(HERE / "astra-velocity-92-check.py"))
ctx.prec = 256


def emit(**row):
    print(json.dumps(row, sort_keys=True))


def constants():
    delta = arb(10)**-8
    y = arb(2)**-17
    x = arb(2031)/128-y
    root_budget = arb(3).sqrt()*y/(2*x**arb("1.5"))
    nmin = arb(10)**30
    mu = (2+1/nmin).sqrt()/nmin.sqrt()
    rate = arb("0.984138")
    marked_bound = (2+1/nmin).sqrt()/(1-rate)
    L = (arb("4.768")/(2*x.sqrt())).asinh()
    retained = 1/(2*L+mu.atanh()).cosh()
    bulk = delta.sqrt()*root_budget/(3*(1+(1-delta/3).sqrt()))
    mark = y**2/(2*x**arb("2.5"))
    r = arb("0.169724")*arb("0.51358")**100
    trial_cost = arb("0.076")*r
    gap = (bulk**2+mark**2).sqrt()+trial_cost
    # True and completed trial marked weights exceed n/16 in the cold square.
    # Thus their geometric mean square roots exceed sqrt(n)/4.
    marked_tilt = 4*gap+2*arb("0.001180")/nmin.sqrt()
    # Mark log of completed vs uncompleted trial has a sharper pointwise
    # estimate from |R_0| <= norm_count(R), as well as its sup bound.
    hnorm = arb("1.001")*arb("1.001")*gap+arb("0.4")*r
    exterior = retained*delta.sqrt()-marked_tilt.exp()*marked_bound*root_budget
    assert marked_bound < 90 and retained > arb("0.58262")
    assert r < arb("3e-30") and gap < arb("1.75e-12")
    assert marked_tilt < arb("8e-12") and hnorm < arb("1.8e-12")
    def remaining(m, jacobi_cap):
        loss = 1/(2*L+jacobi_cap.atanh()).cosh()
        return loss*delta.sqrt()-marked_tilt.exp()*marked_bound*root_budget*arb(m).sqrt()
    after_fifteen = remaining(16,16*mu)
    block = remaining(16,arb(1)/10)
    after_thirty_eight = remaining(39,39*mu)
    inverse_half = (2*((1+(after_fifteen/delta.sqrt())**2).sqrt()-1)).sqrt()
    assert exterior > arb("4.89e-5") and after_fifteen > arb("2.09e-5")
    assert inverse_half > arb("0.207") and block > arb("1.63e-5")
    assert after_thirty_eight > arb("5.7e-8")
    def shifted_remaining(m):
        compression = L.tanh()+178*m/nmin.sqrt()
        return ((1-compression**2).sqrt()*delta.sqrt()
                -marked_tilt.exp()*marked_bound*root_budget*arb(m).sqrt())
    joint_single = shifted_remaining(1)
    joint_erased = shifted_remaining(84)
    assert joint_single > arb("7.648e-5") and joint_single/178 > arb("4.296e-7")
    assert joint_erased > arb("3.84e-7")
    emit(kind="prime_uniform_first_comparison_threshold", min_n="1e30",
         scaled_frozen_mark_column=marked_bound.str(14),
         stripped_diagonal_coefficient=retained.str(14),
         normalized_real_weight_distance=gap.str(14),
         normalized_half_log_sinh=hnorm.str(14),
         marked_tilt_difference=marked_tilt.str(14),
         signed_exterior_lower=exterior.str(15),
         after_fifteen_additional_deletions=after_fifteen.str(15),
         trimmed_half_log_counting_lower=inverse_half.str(15),
         after_thirty_eight_additional_deletions=after_thirty_eight.str(15),
         block_exterior_per_root_hits=block.str(15),
         eventual_joint_shifted_exterior=joint_single.str(15),
         eventual_joint_l1_per_root_n=(joint_single/178).str(15),
         eventual_joint_after_83_deletions=joint_erased.str(15))


def reflection(K, logs):
    size = K.nrows()
    d = [z.tanh() for z in logs]
    m = [1/z.cosh() for z in logs]
    invcol = base["base"]["system"](K, d, False).solve(K)
    return arb_mat([[m[i]*invcol[i,j]*m[j]-(d[i] if i == j else 0)
                     for j in range(size)] for i in range(size)])


def physical():
    n, T, y, sign = (base[k] for k in ("n","x","y","sign"))
    # R92 identifies this point with the unforced real-start ray.
    U, total = base["positive_sheet"]([n/acb(T,y)]+[acb(1)]*(n//2), arb("1e-52"))
    A = [(u+v)/2 for u,v in zip(total,U)]
    B = [(u-v)/2 for u,v in zip(total,U)]
    alpha, beta = [z.real for z in A], [z.real for z in B]
    w = [u*v for u,v in zip(alpha,beta)]
    g = [(u/v).log()/2 for u,v in zip(alpha,beta)]
    k = acb.dft([int(z) for z in sign],inverse=True)
    K = arb_mat([[k[(i-j)%n].real for j in range(n)] for i in range(n)])
    full = lambda f: [f[min(i,n-i)] for i in range(n)]
    Rtrue = reflection(K,full(g))
    s = n/acb(T,y)
    root = abs(s.imag)*arb(3).sqrt()/(2*w[0].sqrt())
    x = [root*Rtrue[i,0] for i in range(n)]
    for i in range(1,n):
        ratio = A[min(i,n-i)].imag/abs(A[min(i,n-i)])
        assert (x[i]-arb(3).sqrt()*ratio*(1 if s.imag>0 else -1)).contains(0)
    hits = [i for i in range(1,n//2+1) if all(abs(x[i])>abs(x[j])
            for j in range(1,n//2+1) if j!=i)]
    assert len(hits)==1
    i = hits[0]
    assert (1-x[i]**2/3-w[i]).contains(0)
    # Use both the ordinary positive real pair and the bare Jacobi seed,
    # which give independently constructed, nonidentical reference responses.
    real, _ = base["positive_sheet"]([n/T]+[arb(1)]*(n//2),arb("1e-52"),real=True)
    flat = [(v/(2*(n/T if j==0 else arb(1)).sqrt())).asinh() for j,v in enumerate(real)]
    seed = [(arb(n).sqrt()*K[j,0]/(arb(n) if j==0 else T).sqrt()).asinh()
            for j in range(n//2+1)]
    for label,ref in (("unit_real_stationary",flat),("jacobi_seed",seed)):
        R = reflection(K,full(ref))
        lag = full([u-v for u,v in zip(g,ref)])
        c,sn = [z.cosh() for z in lag], [z.sinh() for z in lag]
        coef = c[0]+sn[0]*Rtrue[0,0]
        initial = coef*root*R[i,0]
        rhs = sum((R[i,j]*sn[j]*x[j] for j in range(1,n) if j!=i),arb(0))
        left = (c[i]-R[i,i]*sn[i])*x[i]
        assert (left-initial-rhs).contains(0)
        assert abs(left-initial-rhs).upper()<arb("1e-48")
        assert abs(rhs).lower()>0 and coef>0
        h = [(z/2).sinh()*2 for z in lag]
        hn = (sum((z*z for z in h),arb(0))/n).sqrt()
        emit(kind="physical_cold_unit_product_boundary",prime=173,real="2031/128",
             imag="1/131072", cutoff_one_minus_e=(x[i]**2).str(16),
             maximal_inversion_orbit=i,reference=label,
             signed_site_coordinate=x[i].str(16), frozen_mark_source=initial.str(16),
             stripped_site_left=left.str(16),signed_exterior_sum=rhs.str(16),
             normalized_half_log_sinh=hn.str(14))


if __name__=="__main__":
    constants()
    physical()
