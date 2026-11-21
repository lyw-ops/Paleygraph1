"""Replay quotient occupation and the signed translated-block prefix on the real cold path."""
import json
from pathlib import Path
import runpy

from flint import acb, arb, ctx, fmpq
import numpy as np
from scipy.optimize import linprog


prior = runpy.run_path(str(Path(__file__).with_name("astra-recur-95-check.py")))
apply = prior["apply"]
interval = prior["enclose"]
ctx.prec = 384


def certify_minimum(costs, allowed):
    b = len(costs)
    unit, floor = arb(1)/b, arb(1)/8
    # An even quotient probability has block weights unit+D*x. Its Fourier
    # coefficients x are bounded by one since it is a probability.
    D = [[(1 if 2*j == b else 2)*arb.cos_pi_fmpq(fmpq(2*r*j,b))/b
          for j in allowed] for r in range(b)]
    directions = D+[D[0]]
    gaps = [-unit]*b+[floor-unit]
    c = [sum(a[j]*v for a,v in zip(D,costs)) for j in range(len(allowed))]
    base_cost = unit*sum(costs)
    grid = 10**12
    def rational(value):
        return arb(round(float(value)*grid))/grid
    def propose(slack):
        return linprog(np.array(c,dtype=float),A_ub=-np.array(directions,dtype=float),
                       b_ub=-np.array(gaps,dtype=float)-slack,
                       bounds=[(-1.,1.)]*len(allowed),method="highs",
                       options={"primal_feasibility_tolerance": 1e-10,
                                "dual_feasibility_tolerance": 1e-10})
    trial, supporting = propose(2e-10), propose(0.)
    assert trial.success and supporting.success
    x = [rational(z) for z in trial.x]
    assert all(sum(a*t for a,t in zip(row,x)) > d for row,d in zip(directions,gaps))
    upper = base_cost+sum(a*t for a,t in zip(c,x))
    multipliers = [rational(max(0.,-v)) for v in supporting.ineqlin.marginals]
    assert all(v >= 0 for v in multipliers)
    residual = [a-sum(row[j]*v for row,v in zip(directions,multipliers))
                for j,a in enumerate(c)]
    lower = base_cost+sum(y*d for y,d in zip(multipliers,gaps))-sum(map(abs,residual))
    assert upper-lower < arb(1)/10**8 and upper > lower
    return [interval(lower)[0],interval(upper)[1]]


def replay():
    p, n, m, J, k = 769, 384, 8, 16, 8
    b = n // m
    signs = list(map(int, prior["paley_sign"](p)))
    root = arb(n).sqrt()
    column = apply([1] + [0] * (n-1), signs)
    lam = sum(column[::b])
    assert abs(lam) < arb(1)/2

    # A six-element allowed clique supplies an exact nonnegative quotient row.
    clique = [0, 1, 19, 30, 11, 29]
    assert all(signs[m*((i-j) % b)] == 1 for i in clique for j in clique if i != j)
    index = [int(i in clique) for i in range(b)]
    weights = [(z.real*z.real+z.imag*z.imag)/(b*len(clique)) for z in acb.dft(index)]
    assert all(w.is_finite() for w in weights)
    assert (sum(weights)-1).contains(0)
    assert (weights[0]-arb(1)/8).contains(0)
    q = [weights[i % b]/m for i in range(n)]
    assert all((v-z+arb(1)/n).contains(0) for v,z in zip(apply(q,signs),q))
    y = [arb(0)]*n
    prefix = [arb(0)]*n
    plus = [arb(0)]*m
    minus = [arb(0)]*m
    wrong = arb(0)
    signed = arb(0)
    spent = arb(0)
    for j in range(J):
        amplitude = list(map(abs,y))
        prefix = [u+v for u,v in zip(prefix,amplitude)]
        source = amplitude.copy()
        source[0] = (4*n+y[0]**2).sqrt()
        beta = (source[0]-amplitude[0])/root
        g = sum(source)/(2*n)
        wrong += sum(w*(-v).max(0) for w,v in zip(q,y))
        spent += 2*g
        signed += 2*sum(w*(-v).max(0) for w,v in zip(q,y))+beta*root*q[0]-2*g
        if 1 <= j <= k:
            for a,v in enumerate(y[::b]):
                plus[a] += v.max(0)
                minus[a] += (-v).max(0)
        y = apply(source,signs)
        actual = sum(w*v for w,v in zip(q,y))
        assert (signed-actual).contains(0)
        if j == k:
            minority = sum(u.min(v) for u,v in zip(plus,minus))/m
            assert wrong > weights[0]*minority
        if j >= k:
            assert actual > 2*weights[0]*minority-spent

    full = [v/J for v in prefix]
    costs = [arb(0)]+[sum(full[a::b])/m for a in range(1,b)]
    minimum = certify_minimum(costs,[j for j in range(1,b//2+1) if signs[m*j]==1])
    q_charge = sum(w*v for w,v in zip(q,full))
    q_exterior = sum(w*v for i,(w,v) in enumerate(zip(q,full)) if i % b)
    mean = sum(full)/n
    outputs = []
    for a in range(b):
        exterior = [v if i % b != a else arb(0) for i,v in enumerate(full)]
        ordinary = sum(apply(exterior,signs)[a::b])/m
        hat = acb.dft(exterior)
        phase = acb.dft([int(i == a) for i in range(b)])
        fiber = sum(s*z*w.conjugate() for s,z,w in zip(signs[::m],hat[::m],phase))/n
        assert (fiber-ordinary).contains(0)
        assert sum(z*w.conjugate() for z,w in zip(hat[::m],phase)).contains(0)
        outputs.append(ordinary)
    weighted = sum(w*z for w,z in zip(weights,outputs))
    assert (weighted-(1-lam)*q_charge+mean).contains(0)
    maximum = max(range(b),key=lambda i: float(outputs[i].mid()))
    assert all(outputs[maximum] > v for a,v in enumerate(outputs)
               if a != maximum and (a+maximum) % b)
    assert (outputs[maximum]-outputs[-maximum % b]).contains(0)
    return dict(prime=p, prefix=J, minority_prefix=k, block_order=m,
                block_root_mass="1/8", allowed_clique=clique, sign=1,
                temporal_minority_mean=interval(minority), lambda_block=interval(lam),
                full_quotient_charge=interval(q_charge), exterior_quotient_charge=interval(q_exterior),
                minimum_exterior_quotient_charge=minimum,
                weighted_signed_block_exterior=interval(weighted),
                maximum_block_offset=maximum, maximum_signed_block_exterior=interval(outputs[maximum]),
                precision_bits=ctx.prec, units="1e-9")


if __name__ == "__main__":
    print(json.dumps(replay(),sort_keys=True))
