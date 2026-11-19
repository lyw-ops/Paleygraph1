"""Arb continuation of the actual p=173 scalar around a rational cold rectangle."""
from fractions import Fraction as Q
import json
from pathlib import Path
import runpy

import numpy as np
from flint import acb, acb_mat, arb, ctx

base = runpy.run_path(str(Path(__file__).with_name('astra-cold-37.py')))
ctx.prec = 128
order = 173
sign = base['paley_sign'](order)
n = len(sign)
Kr = base['even_kernel'](sign)
K = acb_mat(Kr)
N = K.nrows()
Kf = np.array([[float(Kr[i,j]) for j in range(N)] for i in range(N)])
rat = base['rat']


def matnorm(M):
    return max(sum((abs(M[i,j]).upper() for j in range(M.ncols())), arb(0)).upper()
               for i in range(M.nrows()))


def vmax(x):
    return max(abs(z).upper() for z in x)


def ac(z):
    return acb(float(z.real), float(z.imag))


def jac(s, v):
    return acb_mat([[2*((s[i] if i == j else 0)-v[i]*K[i,j])
                     for j in range(N)] for i in range(N)])


def col(x):
    return acb_mat(N,1,x)


def numeric_root(start, t):
    s = start.copy()
    w = np.full(N, 4*complex(float(t[0]),float(t[1]))/n)
    w[0] = 4
    for _ in range(9):
        v = Kf@s
        J = 2*(np.diag(s)-v[:,None]*Kf)
        res = s*s-v*v-w
        delta = np.linalg.solve(J,res)
        s -= delta
        if np.max(abs(delta)) < 1e-12:
            return s
    return s


def anchor(z, t):
    s = [ac(x) for x in z]
    v = (K*col(s)).entries()
    tball = acb(rat(t[0]),rat(t[1]))
    w = [acb(4)]+[4*tball/n]*(N-1)
    residual = col([x*x-y*y-wi for x,y,wi in zip(s,v,w)])
    return (s,v,residual,jac(s,v))


def half_point(p,q):
    return tuple((x+y)/2 for x,y in zip(p,q))


knorm = matnorm(K)
eye = acb_mat([[int(i==j) for j in range(N)] for i in range(N)])
max_eta = arb(0)
max_rad = arb(0)
count = 0


def tube(z0, z1, left, right):
    """A parameterized closed ball about the affine chord; returns its radius."""
    s0,v0,f0,J0 = left
    s1,v1,f1,J1 = right
    zmid = (z0+z1)/2
    vf = Kf@zmid
    Qf = np.linalg.inv(2*(np.diag(zmid) - vf[:,None]*Kf))
    pre = acb_mat([[ac(w) for w in row] for row in Qf])
    eta0 = max(matnorm(eye-pre*J0),matnorm(eye-pre*J1))
    if not eta0 < arb(1)/2:
        return None
    quad = col([(u1-u0)**2-(v_1-v_0)**2
                for u0,u1,v_0,v_1 in zip(s0,s1,v0,v1)])
    E = (max(vmax((pre*f0).entries()),vmax((pre*f1).entries()))
         + vmax((pre*quad).entries())/4).upper()
    radius = max((2*E).upper(), arb(2)**-40)
    eta = (eta0 + 2*matnorm(pre)*(1+knorm**2)*radius).upper()
    if eta < arb(1)/2:
        return radius,eta
    return None


def step(p,q,z0,left,depth=0):
    global max_eta,max_rad,count
    assert depth < 25
    z1 = numeric_root(z0,q)
    right = anchor(z1,q)
    result = tube(z0,z1,left,right)
    if result is None:
        mid = half_point(p,q)
        zm,am,_ = step(p,mid,z0,left,depth+1)
        return step(mid,q,zm,am,depth+1)
    radius,eta = result
    count += 1
    max_eta = max(max_eta,eta)
    max_rad = max(max_rad,radius)
    return z1,right,radius


def marked(anchor_data, radius):
    s,v,*_ = anchor_data
    error = ((1+knorm)*radius/2).upper()
    return (s[0]+v[0])/2 + acb(arb(0,error),arb(0,error))


def main():
    # Center (0.0331, 0.03517), half-side 1/10000.
    x, y, r = Q(331,10000), Q(3517,100000), Q(1,10000)
    real = (x,Q(0))
    bottom = (x,y-r)
    corners = [(x+r,y-r),(x+r,y+r),(x-r,y+r),(x-r,y-r),bottom]
    w = [arb(4)]+[4*rat(x)/n]*(N-1)
    v = base['real_root'](Kr,sign,rat(x),w)
    s = [(vi*vi+wi).sqrt() for vi,wi in zip(v,w)]
    z = np.array([complex(float(u),0) for u in s])
    left = anchor(z,real)
    assert vmax([acb(u)-v0 for u,v0 in zip(s,left[0])]) < arb(2)**-40
    z,left,radius = step(real,bottom,z,left)
    entry = marked(left,radius)
    approach_count = count
    p = bottom
    for corner in corners:
        z,left,radius = step(p,corner,z,left)
        p = corner
    returned = marked(left,radius)
    assert not entry.overlaps(returned)
    print(json.dumps(dict(kind='validated_actual_prime_scalar_monodromy',
          prime=order, rectangle_center=[str(x),str(y)], half_side=str(r),
          physical_axis_start=str(x), approach_segments=approach_count,
          loop_segments=count-approach_count, working_precision=ctx.prec,
          rigorous_uniform_contraction_upper=max_eta.str(8),
          maximum_spectrum_ball_radius_upper=max_rad.str(8),
          marked_value_before_loop=str(entry), marked_value_after_loop=str(returned),
          marked_enclosures_disjoint=True),sort_keys=True),flush=True)


if __name__=='__main__':
    main()
