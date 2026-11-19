"""Independent small dense checks of the written deterministic estimates."""
from fractions import Fraction
import json
from pathlib import Path
import sys

from flint import arb, ctx

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from square_control import square_field_sign
from theta import paley_sign


def square(x):
    return x*x


def run(order, is_square):
    signs = square_field_sign(7) if is_square else paley_sign(order)
    n = len(signs)
    coefficients = [
        sum(int(s) * (2 * arb.pi() * j * offset / n).cos()
            for j, s in enumerate(signs)) / n
        for offset in range(n)
    ]

    def apply(row):
        return [sum(coefficients[(i-j) % n] * row[j] for j in range(n))
                for i in range(n)]

    def project(row, side):
        mean = sum(row) / n
        return [(x - mean + side*y) / 2 for x, y in zip(row, apply(row))]

    c = arb(1) / (20 * n)
    w = [arb(1)] + [c] * (n-1)
    W = sum(w)
    D = 2 * arb(order).sqrt() * (W/n).sqrt()
    lower_raw = c / (D+c.sqrt())
    vec = [[arb(0)] * n]
    activation = []
    mu = []
    energy = [arb(0)]
    for _ in range(26):
        phi = [(x*x + 4*weight).sqrt() for x, weight in zip(vec[-1], w)]
        activation.append(phi)
        mu.append(sum(phi)/(2*n))
        vec.append(apply(phi))
        energy.append(sum(x*x for x in vec[-1]))
    for k in (1, 2, 5, 8):
        length = 16
        loss = 4*n*sum(square(mu[t+k]-mu[t]) for t in range(length))
        terminal = sum(square(x-y) for x, y in zip(vec[length+k], vec[length]))
        assert energy[k]-terminal > loss
        for start in (0, 4, 9):
            g = [arb(n).sqrt()*x for x in mu[start:start+k]]
            mean = sum(g)/k
            assert W / 2 > sum(square(x-mean) for x in g)/k
    for T in (1, 4, 12):
        mean = sum(mu[1:T+1])/T
        r = c/mean**2
        for side in (-1, 1):
            avg = [arb(0)]*n
            projected = [arb(0)]*n
            for t in range(1, T+1):
                raw = [(x+side*y)/2 for x, y in zip(activation[t], vec[t])]
                avg = [a+x/T for a, x in zip(avg, raw)]
                projected = [a+x/T for a, x in zip(projected, project(raw, side))]
            assert min(x.lower() for x in avg) > lower_raw
            X = [mean+x for x in projected]
            direct_floor = lower_raw-2*arb(order).sqrt()*(mu[T-1]+mu[T]+mu[0])/(4*T)
            assert min(x.lower() for x in X) > direct_floor
            h2 = sum(square((x-u)/mean) for x, u in zip(X, avg))/n
            for kappa in (arb(1)/20, arb(1)/2):
                terms = [2*kappa-x/mean for x in X[1:]]
                assert all((x>0) or (x<0) for x in terms)
                deficit_mean = sum(x for x in terms if x > 0)/n
                assert deficit_mean < 9*kappa**2/(4*r)+h2/(4*kappa)
    print(json.dumps(dict(kind='arb_actual_dense_completion_and_shift_check',
                          order=order, square=is_square, depth=26, precision=ctx.prec,
                          both_sectors=True, shifts=[1,2,5,8], prefix_tests=[1,4,12]),
                     sort_keys=True))


def relaxation(m):
    n = m*m
    count = n-m-1
    u = [m] + [Fraction(1,m)]*m + [1]*count
    v = [m] + [Fraction(m,2)]*m + [Fraction(n//2-m,count)]*count
    e = [0] + [Fraction(-2,m)]*m + [Fraction(2,count)]*count
    assert sum(u) == sum(v) == n and sum(e) == 0
    assert all(x*y >= Fraction(1,3) for x, y in zip(u,v))
    assert sum(x*x for x in e) == Fraction(4,m)+Fraction(4,count)
    for cutoff in [Fraction(1,m*m),Fraction(1,m),Fraction(1),Fraction(3)]:
        mass = sum(max(2*cutoff-x-y,0) for x,y in zip(u[1:],e[1:]))
        assert mass/m > 2*cutoff
    print(json.dumps(dict(kind='exact_scalar_relaxation_check', m=m, n=n,
                          field_claim=False), sort_keys=True))


if __name__ == '__main__':
    ctx.prec = 320
    run(37, False)
    run(49, True)
    for size in [8, 16, 64]:
        relaxation(size)
