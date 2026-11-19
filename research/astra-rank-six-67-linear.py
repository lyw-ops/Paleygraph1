"""Arb projection of the first rank-six linear return against the nine-center seed."""
from collections import Counter
from math import comb
from pathlib import Path
import json
import runpy

from flint import acb, arb, ctx


def marked_factors(degree):
    # A shape (l+1,l+1,l,l) is L^(2l+1) times the actual rank-six Z.
    states = {(0,0,0,0): 1}
    moments = []
    for j in range(degree+1):
        row = {}
        for shape, value in states.items():
            l = shape[3]
            if shape == (l+1,l+1,l,l):
                row[2*l+1] = -value
        assert row == {-e:v for e,v in row.items()}
        moments.append(row)
        if j == degree:
            break
        nxt = Counter()
        for shape, value in states.items():
            for i in range(4):
                for direction in (-1,1):
                    child = list(shape)
                    child[i] += direction
                    if child == sorted(child, reverse=True):
                        nxt[tuple(child)] += value
        states = nxt
    assert moments[2] == {-1:-1, 1:-1}
    return moments


def linear():
    prior = runpy.run_path(str(Path(__file__).with_name("astra-joint-65-check.py")))
    degree = prior["D"]
    prev, kern = prior["prev"], prior["kern"]
    algebra = prev["old"]
    a,b,c,d = prev["coefficients"]()
    t = prev["t0"]
    s = kern["dim"]
    z = prior["old"]["prefix"](acb(t))[0].real
    w = prior["joint"]["coefficient"](acb(t),0,2,0).real
    v = prior["selected"](acb(t)).real

    def join(tab, factor, scale):
        weights = [{e:x*scale**j for e,x in row.items()} for j,row in enumerate(factor)]
        return algebra["add_inputs"](tab,weights)

    table = [{2*i-j:comb(j,i)*(s/2)**j for i in range(j+1)} for j in range(degree+1)]
    for lo,hi,scale,perverse in ((2,4,b/4,False),(5,8,c/8,False),(8,16,d/16,True)):
        factors = [(len(algebra["WEIGHTS"][i]),algebra["DETS"][i]) for i in range(lo,hi)]
        table = join(table,algebra["scalar_powers"](factors,degree,perverse),scale)
    table = join(table, marked_factors(degree), c/8)
    table = join(table,[{0:kern["p3"]["P"][j].get((0,0),0)} for j in range(degree+1)],a)
    table = join(table,[{0:k} for k in prior["old"]["moments"](degree)],z)
    table = join(table,algebra["scalar_powers"]([(4,4)],degree,True),w)
    mu = prior["symplectic_moments"](2,degree)
    table = join(table,[{0:sum(comb(j,k)*mu[k]*mu[j-k] for k in range(j+1))}
                        for j in range(degree+1)],v)
    extent = s+2*abs(a)+3*abs(b)+4*abs(c)+arb(23)*abs(d)/4+8*(abs(v)+abs(z)+abs(w))
    rt = extent**2/(4*t)
    acc = arb(0)
    bn = arb(1)
    for k in range(1,degree//2+1):
        bn *= (arb(3)/2-k)/k
        acc += 2*t.sqrt()*bn*(2*k)/(4*t)**k*table[2*k-1].get(2,0)
    k = degree//2+1
    bn *= (arb(3)/2-k)/k
    # A normalized irreducible character has Haar L1 norm at most one.
    ratio = rt*(k+1)/k
    assert ratio < 1
    acc += arb(0,(2*t.sqrt()*abs(bn)*rt**k*(2*k)/(extent*(1-ratio))).upper())
    # Both rank-six sources have physical transport sign minus; their inner
    # amplitudes coincide by lift exchange. Round 65's table bounds both D labels.
    amplitude = arb(144291005,10)/10**12
    change = -2*amplitude*acc
    baseline = arb(48539,9)/10**12

    def bracket(x,scale):
        return [int((x*scale).lower().floor().unique_fmpz()), int((x*scale).upper().ceil().unique_fmpz())]

    assert change < 0 and baseline+change > 0
    return dict(floor="2031/128", precision=ctx.prec, projection="m^2",
                unary_single_exterior_times_1e12=bracket(acc,10**12),
                two_leaf_linear_change_times_1e18=bracket(change,10**18),
                positive_direct_plus_two_linear_terms_times_1e12=bracket(baseline+change,10**12))


if __name__ == "__main__":
    ctx.prec = 192
    print(json.dumps(linear(),sort_keys=True))
