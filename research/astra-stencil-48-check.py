"""Exact and interval checks for the real marked stencils."""
import json
from fractions import Fraction as F
from math import comb, factorial
from flint import arb, ctx

ctx.prec = 192


def report(kind, **fields):
    print(json.dumps(dict(kind=kind, **fields), sort_keys=True))


def envelope(t):
    return (arb(2).sqrt() * (1 + (1-8/arb.pi()**2)*t) / (1+t).sqrt()).log()


T = arb(28)
r = (4/T)**2


def paired(t):
    x = (t/T)**2
    return (x+r)/(x-r)*((1+t)/(1+T)).log() - 2*r*(x-1)/((x-r)*(r-1))*(5/(1+T)).log()


for j in range(512):
    v = arb(2*j+1, 1) / 2048
    budget_lower = abs(paired(v)-arb(7)/5*paired(arb(3)))/2
    assert budget_lower - envelope(v) - arb(7)/5*envelope(arb(3)) > arb(49)/1000
report("continuum-limiting-budget", cold_interval=["0", "1/2"], other_floors=[3, 28],
       subdivisions=512, uniform_margin_gt="0.049")

step = F(1, 2**3300)
radius = F(1, 2**62)
for q, a, k, R, old_lower in [(113,F(1,5),48,F(7,8),F(353,100)),
                              (173,F(1,20),47,F(3,5),F(1423,100)),
                              (121,F(3,4),48,F(3,4),F(206,100))]:
    ratio = k*step/radius
    remainder = k**k * ratio / (factorial(k) * radius**k * (1-ratio))
    assert remainder < F(1, 2**100)
    coeffs = []
    for s in [F(1,4*k*k), F(4,k*k)]:
        u = (1-s)/(1+s)
        prev, cur = 0, 1
        for _ in range(k-1):
            prev, cur = cur, 2*u*cur-prev
        coeffs.append(4*(-1)**(k-1)*cur/(1+s)**2)
    assert coeffs[0]*coeffs[1] < 0 and min(map(abs, coeffs)) > 5
    assert old_lower / R**k > 2000
    report("finite-stencil-transfer", field=q, cold_center=str(a), order=k,
           spacing="2^-3300", analytic_radius="2^-62", kernel_sign_change=True,
           excess_gt=1998, inherited_jet=True)
