"""Check the canonical clipped excess on a finite prime and the cold constants."""
from fractions import Fraction as Q
import json
from pathlib import Path
import runpy

import numpy as np
from flint import acb, arb, arb_mat, ctx


base = runpy.run_path(str(Path(__file__).with_name('astra-cold-37.py')))
ctx.prec = 192
p = 173
sign = base['paley_sign'](p)
n = len(sign)
K = base['even_kernel'](sign)
mult = [1] + [2] * (n//2 - 1) + [1]
size = len(mult)
a = (1 / arb(2)).sqrt()
t = acb(1 / arb(50), arb(2161) / 100000)
s = n / t


def candidate():
    kernel = np.array([[float(K[i,j]) for j in range(size)] for i in range(size)])
    weight = complex(s)
    row = np.zeros(size, dtype=complex)
    for _ in range(4500):
        sigma = np.where(row.imag >= 0, 1, -1)
        product = 0.75 * row.imag**2 - 0.375 * row.real**2
        sums = np.where(product <= 1, np.sqrt(4+row*row),
                        2**0.5 * abs(row.imag) + 1j * sigma * row.real/2**0.5)
        sums[0] = np.sqrt(weight) * np.sqrt(4 + row[0]**2 / weight)
        row = (row + kernel @ sums) / 2
    return [acb(arb(float(z.real)), arb(float(z.imag))) for z in row]


def evaluate(z):
    sums, derivatives = [], []
    for i, v in enumerate(z):
        if i == 0:
            mark_log = (v / (2*s.sqrt())).asinh()
            # Secants to every genuine mark are strictly contractive.
            assert abs(mark_log.imag) < a.atan() and abs(t.arg()) / 2 < a.atan()
            sums.append(s.sqrt() * (4+v*v/s).sqrt())
            d = v / sums[-1]
            derivatives.append((d.real, -d.imag, d.imag, d.real))
        else:
            q = 3*v.imag**2/4 - 3*v.real**2/8
            if q < 1:
                sums.append((4+v*v).sqrt())
                d = v / sums[-1]
                derivatives.append((d.real, -d.imag, d.imag, d.real))
            else:
                assert q > 1
                assert v.imag > 0 or v.imag < 0
                sigma = 1 if v.imag > 0 else -1
                sums.append(acb(abs(v.imag)/a, a * v.real * sigma))
                derivatives.append((0, sigma/a, sigma*a, 0))
    residual = [sum((K[i,j]*sums[j] for j in range(size)), acb(0)) - z[i]
                for i in range(size)]
    return sums, derivatives, residual


def verify():
    z = candidate()
    for _ in range(2):
        _, derivatives, residual = evaluate(z)
        jacobian = arb_mat([[int(i == j) - K[i % size, j % size]
                             * derivatives[j % size][2*(i//size)+j//size]
                             for j in range(2*size)] for i in range(2*size)])
        rhs = arb_mat(2*size, 1, [v.real for v in residual] + [v.imag for v in residual])
        step = jacobian.solve(rhs)
        z = [acb((v.real+step[i,0]).mid(), (v.imag+step[i+size,0]).mid())
             for i,v in enumerate(z)]
    sums, _, residual = evaluate(z)
    rho = max(abs(v).upper() for v in residual)
    assert rho < arb('1e-48')
    assert sum(m*abs(v) for m,v in zip(mult,z))/n < 40
    assert abs(t.arg()) < arb.pi()/3
    mean = sum((m*v for m,v in zip(mult,sums)), acb(0))/(2*n)
    # E|U| < 32. The real Hilbert identity and a=1/sqrt(2)
    # give |M-M_Z| <= sqrt(72*rho) at every genuine clipped root.
    error = (72*rho).sqrt().upper()
    mean_ball = mean + acb(arb(0,error), arb(0,error))
    price = mean_ball**2 - (n-1+s)/n
    assert price.imag.contains(0)
    print(json.dumps(dict(kind='canonical_clipped_product_excess', p=p, kappa=2,
                          real='1/50', imag='2161/100000',
                          excess=price.real.str(17), residual_upper='1e-48'), sort_keys=True))


def cold_constants():
    assert (Q('.786')**2-Q('.654')**2/8)/(1+Q('.75')**2)**2 > Q('.20')
    assert 1-Q('.20') < Q('.90')**2
    assert 20*Q('1.55') / Q('.0094') < 3400
    assert Q('3.163')**2 > 10
    assert (Q('2.1')+Q('3.163')*Q('.0028'))*Q('3.163')+Q('.602') < Q('7.3')
    assert Q('7.3') / Q('3.98') < Q('1.84')
    assert Q('1.84')*Q('3.932') < Q('7.24') and Q('1.84')*Q('3.06') < Q('5.64')
    assert Q('1.85')*16384/3 < 10104
    assert Q(3400)**2 * 16384 < 3*16000**2 * Q('3.98')**4
    assert Q(10104)*Q('3.932e-175')*2**34 < Q('6.84e-161')
    print(json.dumps(dict(kind='cold_clipped_residual_bounds', total_excess_per_residual='1.84',
                          cap_sqrt_product_per_normalized_squared_residual=3400), sort_keys=True))


if __name__ == '__main__':
    verify()
    cold_constants()
