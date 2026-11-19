"""Certify first clipped-cap contact on the real-start prime-173 ray."""
from fractions import Fraction as Q
import json
from pathlib import Path
import runpy

import numpy as np
from flint import acb, arb, arb_mat


phase = runpy.run_path(str(Path(__file__).with_name('astra-phase-86-check.py')))
src, x = phase['src'], phase['x']
K, n, size, rat = src['K'], src['n'], src['N'], src['rat']
site = 43
cap = (1 / arb(2).sqrt()).atan()
broad = Q(129, 10000)
low, high = Q(1294720, 100000000), Q(1294721, 100000000)
counts = {'before': 0, 'approach': 0, 'contact': 0}
slopes = []


def bounds(start, end, left, right, radius, mode):
    data = phase['tube_data'](start, end, left, right, radius)
    if data is None:
        return False
    s, v, angles = data
    t = acb(rat(x), rat(start).union(rat(end)))
    scale = (t / n).sqrt()
    if any(not z.real > 0
           for z in [(s[0] + v[0])/(2*scale), (s[0] - v[0])/(2*scale)]):
        return False
    if mode == 'before':
        return all(abs(a) < cap for a in angles[1:])
    if not all(abs(a) < cap for i, a in enumerate(angles[1:], 1) if i != site):
        return False
    if not angles[site] > 0:
        return False
    jac = src['jac'](s, v)

    def log_slope(rhs):
        ds = jac.solve(src['col'](rhs))
        dv = K * ds
        return (ds[site, 0] + dv[site, 0])/(s[site]+v[site])

    try:
        dy = (log_slope([acb(0)] + [acb(0, arb(4)/n)]*(size-1)) - acb(0,1)/(2*t)).imag
        if not (dy > 42 and dy < 46):
            return False
        if mode == 'contact':
            rhs = [acb(0)] * size
            rhs[site] = 4*t/n
            dq = log_slope(rhs).imag
            if not (dy > rat('44.08') and dy < rat('44.10') and
                    dq > rat('-0.06501') and dq < rat('-0.06497')):
                return False
            slopes.append((dy, dq))
    except ZeroDivisionError:
        return False
    return True


def walk(start, end, seed, left, mode, depth=0):
    assert depth < 30
    predicted = src['numeric_root'](seed, (x, end))
    right = src['anchor'](predicted, (x, end))
    tube = src['tube'](seed, predicted, left, right)
    if tube and bounds(start, end, left, right, tube[0], mode):
        counts[mode] += 1
        return predicted, right
    mid = (start+end)/2
    seed, left = walk(start, mid, seed, left, mode, depth+1)
    return walk(mid, end, seed, left, mode, depth+1)


def point_angle(y, seed, anchor):
    tube = src['tube'](seed, seed, anchor, anchor)
    assert tube is not None
    data = phase['tube_data'](y, y, anchor, anchor, tube[0])
    return data[2][site]


def check_reflection(y, seed, anchor):
    projection = runpy.run_path(str(Path(__file__).with_name('real-phase-projection-89-check.py')))
    radius = src['tube'](seed, seed, anchor, anchor)[0]
    s, v, angles = phase['tube_data'](y, y, anchor, anchor, radius)
    t = acb(rat(x), rat(y))
    scale = (t/n).sqrt()
    plus = [(si+vi)/(2*scale) for si, vi in zip(s, v)]
    minus = [(si-vi)/(2*scale) for si, vi in zip(s, v)]
    nu = [(a.real*b.real).sqrt() for a, b in zip(plus, minus)]
    diagonal = [(b.real/a.real).sqrt() for a, b in zip(plus, minus)]
    tangents = [(a.imag/a.real-b.imag/b.real)/2 for a, b in zip(plus, minus)]
    proj = projection['weighted_projection']
    J = (proj(projection['plus_basis'], diagonal)
         - proj(projection['minus_basis'], [1/d for d in diagonal]))
    # This is the orthonormal even basis; 0 and 43 have multiplicity one.
    D = arb_mat([[tangents[i] if i == j else 0 for j in range(size)] for i in range(size)])
    P = (n/t).imag/(2*nu[0]**2)
    T = tangents[0]/(1+P**2)
    A = J*D*J - arb_mat([[P*((J[i, 0] if j == 0 else 0) + (J[0, j] if i == 0 else 0))
                           for j in range(size)] for i in range(size)])
    den = 1 + T*A[0, 0]
    L = arb_mat([[A[i,j]-T*A[i,0]*A[0,j]/den for j in range(1,size)] for i in range(1,size)])
    feedback = arb_mat([[int(i == j)+L[i-1,j-1]*tangents[j] for j in range(1,size)]
                        for i in range(1,size)])
    dq_rhs = [L[i-1,site-1]/(2*nu[site]) for i in range(1,size)]
    ds = -acb(0,n)/t**2
    fv = ds.imag/(2*nu[0])
    marked_input = (ds.real+P*ds.imag)/(2*nu[0]*(1+P**2))
    dy_rhs = [J[i,0]*fv + A[i,0]*(marked_input-T*J[0,0]*fv)/den for i in range(1,size)]
    rhs = arb_mat([[a,b] for a,b in zip(dq_rhs,dy_rhs)])
    slope = projection['preconditioned_inverse'](feedback, real=True)*rhs
    dq = (slope[site-1,0]-angles[site].sin()/2)/nu[site]
    dy = slope[site-1,1]/nu[site]
    jac = src['jac'](s, v)
    def log_slope(vector):
        ds = jac.solve(src['col'](vector))
        return (ds[site,0] + (K*ds)[site,0])/(s[site]+v[site])
    true_dq = log_slope([4*t/n if i == site else acb(0) for i in range(size)]).imag
    true_dy = (log_slope([acb(0)]+[acb(0,arb(4)/n)]*(size-1)) - acb(0,1)/(2*t)).imag
    assert (dq-true_dq).contains(0) and (dy-true_dy).contains(0)
    assert rat('-0.0651') < dq and dq < rat('-0.0649') and 44 < dy and dy < 45
    print(json.dumps(dict(kind='real_reflection_responses_before_first_tie',
          prime=173, real=str(x), imag=str(y), site=site, even_orbits=size,
          fixed_marked_product_phase_derivative=['-0.0651','-0.0649'],
          physical_vertical_phase_derivative=[44,45],
          direct_complex_jacobian_overlap=True),sort_keys=True))


def main():
    weights = [arb(4)] + [4*rat(x)/n]*(size-1)
    v = src['base']['real_root'](src['Kr'], src['sign'], rat(x), weights)
    real = [(z*z+w).sqrt() for z, w in zip(v, weights)]
    seed = np.array([complex(float(z), 0) for z in real])
    left = src['anchor'](seed, (x, Q(0)))
    assert src['vmax']([acb(z)-a for z, a in zip(real, left[0])]) < arb(2)**-40
    seed, left = walk(Q(0), broad, seed, left, 'before')
    seed, left = walk(broad, low, seed, left, 'approach')
    assert point_angle(low, seed, left) < cap
    check_reflection(low, seed, left)
    seed, left = walk(low, high, seed, left, 'contact')
    assert point_angle(high, seed, left) > cap
    # mu <= |P0| <= |v|/(2u) throughout this real-part chart.
    assert rat(high)/(2*rat(x)) < 1/(2*arb(2).sqrt())
    price = [(-dy/dq) for dy,dq in slopes]
    denominator = [-2*arb(2).sqrt()*dq for _, dq in slopes]
    assert all(678 < v and v < 679 for v in price)
    assert all(rat('.1837') < v and v < rat('.1840') for v in denominator)
    print(json.dumps(dict(kind='first_bulk_clip_contact_and_outgoing_price',
          prime=173, real=str(x), imag_open_bracket=[str(low), str(high)],
          contact_sites=[site], sign=1, phase_y=['44.08','44.10'],
          phase_local_product=['-0.06501','-0.06497'],
          switch_diagonal=['0.1837','0.1840'],
          right_total_excess_derivative=[678,679],
          right_negative_excess_derivative=0, segments=counts,
          precision=src['ctx'].prec),sort_keys=True))


if __name__ == '__main__':
    main()
