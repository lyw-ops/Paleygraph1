"""Certified finite time nine-center comparison with tilted loss accounting."""
import json
from fractions import Fraction
from pathlib import Path
import runpy

from flint import acb, arb, arb_poly, ctx

source = Path(__file__).resolve().parent
fields = runpy.run_path(str(source / "astra-joint-65-check.py"))
joint = fields["joint"]
ctx.prec = 192
N = 50
KEEP = 80
eta = arb(1)/5
eps = arb(5)/10**7
tilt = [(eta*k).cosh() for k in range(161)]
assert all(k-1 < arb(14)/5*tilt[k] for k in range(11))
assert arb(14)/5*eta*(eta*10).sinh() > 1


def symmetric(row, radius):
    return arb_poly([row[abs(k)]/(2 if k else 1)
                     if abs(k)<len(row) else 0 for k in range(-radius,radius+1)])


def polynomial(row, x):
    y = arb(0)
    for c in reversed(row):
        y = y*x+c
    return y


def prefix(height=600):
    floor = arb(2031)/128
    half = arb(1)/2**17
    t = acb(arb(floor,half),arb(0,half))
    rows,pars = fields["upper"](t)
    assert all(x<1 for x in pars)
    rows = [[v.upper() for v in row] for row in rows]
    assert all(v>=0 for row in rows for v in row)
    norms = [sum(x*y for x,y in zip(row,tilt)) for row in rows]
    folded = [symmetric(row,KEEP) for row in rows]
    a,b,c,d,z,w,v = pars
    def weight(poly,r):
        return sum(poly[r+i]*(2 if i else 1)*tilt[i] for i in range(r+1))
    seed=fields["kern"]["dim"]
    center_mass=seed+2*a+3*b+4*c+arb(23)*d/4+8*(z+w+v)
    center_norm=seed*tilt[1]+a*(1+tilt[2])+b*(1+3*tilt[1]/2+3*tilt[3]/2)
    center_norm+=c*weight(fields["kern"]["F"],4)+d*weight(fields["kern"]["G"],5)
    center_norm+=z*weight(fields["old"]["R"],2)+(v+w)*weight(fields["field"],4)
    assert center_mass<arb(377)/100
    bn=arb(1)
    for l in range(1,16):bn*=(arb(3)/2-l)/l
    h=[arb(0)]*N
    maxcap=maxleak=arb(0)
    tol=arb(1)/10**12
    assert (8+arb(4)/10**30).sqrt()<seed.upper()
    assert arb(3)/2*(34+11+16)/10**15<tol
    for depth in range(1,height+1):
        zero=sum(i*x for i,x in enumerate(h))+arb(14)/5*eps+arb(1)/10**8
        norm=zero+sum(x*y for x,y in zip(h,tilt[1:]))
        core=symmetric([zero]+h,N)
        # Each intermediate cut removes only positive masses. The final difference
        # of tilted norms charges all paths touching any cut, including reentry.
        power=arb_poly([0]*KEEP+[1])
        partial=arb_poly()
        for j,kr in enumerate(folded):
            if j:
                p=power*core
                power=arb_poly([p[i+N] for i in range(2*KEEP+1)])
            prod=kr*power
            partial += arb_poly([prod[i+2*KEEP] for i in range(N+1)])
        retained=partial[0]+sum(2*partial[k]*tilt[k] for k in range(1,N+1))
        leak=polynomial(norms,norm+eps)-retained
        ratio=(center_norm+norm+eps)**2/(4*(floor-half))
        assert ratio<1
        leak+=2*abs(t).sqrt()*abs(bn)*ratio**15/(1-ratio)
        # All bad-lift and marked discrepancies are inserted explicitly in Q_1.
        h=[(2*partial[k]).upper() for k in range(1,N+1)]
        h[0]+=tol
        assert leak < eps, (depth, float(leak))
        maxleak=max(maxleak,leak.upper())
        cap=center_mass+sum(k*x for k,x in enumerate(h,1))+4*eps
        assert cap < arb(48)/10, (depth,float(cap))
        maxcap=max(maxcap,cap.upper())
    assert maxcap<arb(4768)/1000 and maxleak<arb(394)/10**9
    # The real Jacobi seed and its mass differ by <1e-11, which fits the
    # 0.032 margin between the verified cap and the derivative cap.
    assert maxcap-seed.lower()<2
    low=floor-half
    def derivative(m,b):
        return m/(4*low-2*b*b+m*m).sqrt()
    assert derivative(arb(48)/10,arb(2))<arb(55)/100
    assert derivative(arb(48)/10,arb(0))<arb(52)/100
    assert derivative(arb(53)/10,arb(5)/2)<arb(2)/3
    assert (arb(96)/10)*(arb(55)/100)**599*arb(10**307).sqrt()<arb(1)/4
    assert (arb(96)/10)*(arb(52)/100)**599<arb(1)/10**169
    return dict(kind="actual_full_mark_nine_center_finite_prefix", bits=ctx.prec,
                floor="2031/128", real_and_imaginary_halfwidth="1/131072",
                steps=height, all_site_upper="4.768", residual_leak_upper="394e-9",
                residual_budget="5e-7", stationary_n_range=[10**30,10**307],
                normalized_terminal_real_increment_upper="1e-169",
                actual_stationary_real_mark_limsup_upper="4e-170")


if __name__=="__main__":
    f=Fraction
    low=f(2031,128)-f(1,4)
    high=f(2031,128)+f(1,4)
    # Each squared comparison has a positive denominator on the whole disk.
    def derivative_squared(m,b):
        return m*m/(4*low-2*b*b+m*m)
    assert derivative_squared(5,f(22,10))<f(3,5)**2
    assert derivative_squared(f(65,10),f(37,10))<f(3,4)**2
    assert (2*high)**2/(4*low-f(32,10)**2)**3<f(9,100)**2
    assert f(9,100)+f(1,32)<f(1,8)
    print(json.dumps(dict(kind="physical_newton_fourth_norm_rational",
                         floor="2031/128",disk_radius="1/4",input_modulus_upper=5,
                         input_imaginary_upper="2.2",step_counting_fourth_norm_upper=1,
                         linear_defect_counting_second_norm_upper="1/32",
                         quadratic_remainder_constant_upper="9/100",
                         closing_ball_radius="1/2",closing_lipschitz_upper="3/4"),
                     sort_keys=True),flush=True)
    print(json.dumps(prefix(),sort_keys=True),flush=True)
