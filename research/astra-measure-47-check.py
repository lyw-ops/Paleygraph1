"""Replay the finite rank-majorant, stencil, and rational coefficient checks."""
import json
from fractions import Fraction

from flint import arb, ctx

ctx.prec = 192
one = arb(1)


def record(kind, **items):
    print(json.dumps(dict(kind=kind, **items), sort_keys=True))


h = arb(2) / 5
rho = arb(201) / 200
b = h*h / (1-h*h).sqrt()
assert rho / arb(20).sqrt() + b < h
# The derivative of h^2/sqrt(1-h^2) is strictly increasing.
lo, hi = arb(412936) / 1000000, arb(412940) / 1000000


def derivative(v):
    d = 1-v*v
    return v*(2-v*v)/(d*d.sqrt())


assert derivative(lo) < 1 < derivative(hi)
maximum_upper = hi - lo*lo / (1-lo*lo).sqrt()
maximum_lower = lo - lo*lo / (1-lo*lo).sqrt()
assert 2/maximum_upper**2 > arb(3925)/100
assert 2/maximum_lower**2 < arb(3926)/100
n0 = 2**90
assert rho*((2+one/n0)/40).sqrt()+(1+8*arb(3).sqrt()/2**15)*b < h
assert Fraction(201, 200)**500 > 8
record("quantitative-majorant", rank_at_degree="2^(d-1)",
       truncation="floor(log2(n)/3)", threshold_check_n="2^90",
       asymptotic_power="1/500")
record("analytic-majorant", rho="201/200", h="2/5",
       fixed_floor_threshold_interval=["39.25", "39.26"])


def envelope(t):
    return (arb(2).sqrt()*(1+(1-8/arb.pi()**2)*t)/(1+t).sqrt()).log()


T = arb(41)
k = arb(7)/5
r = (4/T)**2


def paired(t):
    x = (t/T)**2
    A = (x+r)/(x-r)
    B = -2*r*(x-1)/((x-r)*(r-1))
    return A*((1+t)/(1+T)).log()+B*(5/(1+T)).log()


upper = envelope(one)+k*envelope(arb(3))
lower = abs(paired(one)-k*paired(arb(3)))/2
assert upper < arb(319)/1000 and lower > arb(395)/1000
x, y = (1/T)**2, (3/T)**2
assert (x-1)/x-k*(y-1)/y < 0 < (x-1)-k*(y-1)
record("signed-stencil", floors=[1, 3, 41], coefficient="7/5",
       upper="0.319", measure_lower="0.395", sign_change=True)

a = arb(2)/3
rank = 135
assert 41*(one-1/arb(64)).sqrt() > 40
square_lower = (2/(1+a)).log()/2
budget = ((1+T)/(1+a)).log()*((T-a)/(T+a))**rank
assert square_lower-budget > arb(5)/100
record("square-asymptotic-stencil", degree=rank, cold="2/3", anchor=41,
       excess_lower="0.05")

# Actual square-25 Jacobi column from parallel-stationary.md.
F = Fraction
lam = [-1, 1, -3, -5, 5, 1, 3, 1, 5, -5, -3, 1]
n = len(lam)


def fourier_involution(v):
    return [sum(F(lam[(i-j) % n], n)*v[j] for j in range(n)) for i in range(n)]


degree = 9
H, U = [[F(0)]*n], [[F(1)]*n]
for d in range(1, degree+1):
    Ud = [sum((H[l][i]*H[d-l][i]-U[l][i]*U[d-l][i]
               for l in range(1, d)), F(0))/2 for i in range(n)]
    Hd = fourier_involution(Ud)
    if d == 1:
        Hd = [v+F(col, 2*n) for v, col in zip(Hd, lam)]
    U.append(Ud)
    H.append(Hd)
for d in range(degree+1):
    for i in range(n):
        identity = sum(U[l][i]*U[d-l][i]-H[l][i]*H[d-l][i]
                       for l in range(d+1))
        assert identity == int(d == 0)
D = [sum(row[i] for row in U) for i in range(n)]
actual = fourier_involution(D)
assert all(actual[i]+F(lam[i], 2*n) == sum(row[i] for row in H)
           for i in range(n))
assert any(H[-1])
record("rational-coordinate-recurrence", field=25, floor=48, degree=degree,
       coefficients_checked=(degree+1)*n, exact_forcing=True)
