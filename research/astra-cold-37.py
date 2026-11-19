"""Certify actual marked Taylor coefficients on Cayley disks by Arb arithmetic.

The initial floating Picard estimate only seeds Newton refinement. All
certificate statements are checked from Arb balls and an explicit real
contraction test. Run with -B from the repository root.
"""
from fractions import Fraction
import json
from pathlib import Path
import sys

from flint import acb, arb, arb_mat, ctx

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from smoothing import smoothing
from square_control import square_field_sign
from theta import paley_sign


def rat(value):
    x = Fraction(value)
    return arb(x.numerator) / x.denominator


def column(entries):
    return arb_mat(len(entries), 1, entries)


def even_kernel(sign):
    n = len(sign)
    kernel = acb.dft([int(x) for x in sign], inverse=True)
    assert all(z.imag.contains(0) for z in kernel)
    assert all(sign[i] == sign[-i] for i in range(n))
    s = n // 2 + 1
    orbit = [[0]] + [[j, n-j] for j in range(1, n//2)] + [[n//2]]
    return arb_mat([[sum((kernel[(i-l) % n].real for l in labels), arb(0))
                     for labels in orbit] for i in range(s)])


def system(K, d, multiply_on_left):
    s = len(d)
    return arb_mat([[int(i == j)-K[i,j]*(d[i] if multiply_on_left else d[j])
                     for j in range(s)] for i in range(s)])


def real_root(K, sign, a, w):
    """Refine a point, then rigorously enclose the unique positive-floor root."""
    n = len(sign)
    seeds = smoothing(sign, float(a), 1e-12, 20000)[0]
    x = [arb(float(t)) for t in seeds[:len(w)]]
    for _ in range(8):
        phi = [(xi*xi + wi).sqrt() for xi, wi in zip(x, w)]
        derivative = [xi/pi for xi, pi in zip(x, phi)]
        residual = K*column(phi) - column(x)
        step = system(K, derivative, False).solve(residual)
        x = [(xi+si).mid() for xi, si in zip(x, step.entries())]
    phi = [(xi*xi + wi).sqrt() for xi, wi in zip(x, w)]
    residual = (K*column(phi) - column(x)).entries()
    norm = sum((abs(e).upper()**2 * (1 if i in (0, n//2) else 2)
                for i, e in enumerate(residual)), arb(0)).sqrt()
    radius = arb(2)**(-ctx.prec + 64)
    b = [(abs(xi).upper()+radius).upper() for xi in x]
    lip = max((bi/(bi**2+wi).sqrt()).upper() for bi,wi in zip(b,w))
    assert lip < 1 and norm < (1-lip)*radius, (lip, norm, radius)
    return [xi+arb(0, radius) for xi in x]


def certificate(q, characteristic, center, degree, radius, precision=640):
    ctx.prec = precision
    sign = square_field_sign(characteristic) if characteristic else paley_sign(q)
    n = len(sign)
    a = rat(center)
    K = even_kernel(sign)
    size = K.nrows()
    w = [arb(4)] + [4*a/n]*(size-1)
    v = real_root(K, sign, a, w)
    s = [(vi*vi+wi).sqrt() for vi,wi in zip(v,w)]
    inverse = system(K, [vi/si for vi,si in zip(v,s)], True).inv()
    vs, ss = [v], [s]
    marks = [(v[0]/2).asinh()]
    # t=a(1+h)/(1-h), so every positive-order coefficient of 4w_bulk is 8a/n.
    bulk_source = [arb(0)] + [8*a/n]*(size-1)
    for k in range(1, degree+1):
        g = bulk_source.copy()
        for j in range(1, (k+1)//2):
            for i in range(size):
                g[i] += 2*(vs[j][i]*vs[k-j][i] - ss[j][i]*ss[k-j][i])
        if k % 2 == 0:
            j = k//2
            for i in range(size):
                g[i] += vs[j][i]**2-ss[j][i]**2
        sk = (inverse*column([z/(2*si) for z,si in zip(g,s)])).entries()
        vk = (K*column(sk)).entries()
        vs.append(vk)
        ss.append(sk)
        cm = (k*vk[0] - sum((j*marks[j]*ss[k-j][0]
                               for j in range(1,k)), arb(0)))/(k*s[0])
        marks.append(cm)
    product = abs(marks[-1]) * rat(radius)**degree
    assert product > 1
    real_axis = [Fraction(center)*(1-Fraction(radius))/(1+Fraction(radius)),
                 Fraction(center)*(1+Fraction(radius))/(1-Fraction(radius))]
    print(json.dumps(dict(kind='actual_marked_ramification_in_cayley_disk',
                          order=q, field_characteristic=characteristic or q,
                          center=center, cayley_radius=radius, degree=degree,
                          precision=precision, coefficient=marks[-1].str(24),
                          coefficient_times_radius_power=product.str(20),
                          base_mark=marks[0].str(20),
                          real_axis_diameter=list(map(str,real_axis))),
                     sort_keys=True), flush=True)


if __name__ == '__main__':
    certificate(113, None, '1/5', 48, '7/8')
    certificate(173, None, '1/20', 47, '3/5')
    certificate(121, 11, '3/4', 48, '3/4')
