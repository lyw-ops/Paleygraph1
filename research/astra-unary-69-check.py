"""Pieri signed unary credits and lower sibling prices at the real floor."""
from collections import Counter
from math import comb
from pathlib import Path
import runpy
from flint import acb, arb, arb_poly, ctx

old = runpy.run_path(str(Path(__file__).with_name("astra-nonlinear-68-check.py")))
p, previous, t = old["p"], old["previous"], old["t"]
D = p["D"]
scaled = p["scaled"]


def tables(extra=False):
    algebra = p["prev"]["old"]
    a, b, c, d = p["prev"]["coefficients"]()
    z = p["old"]["prefix"](acb(t))[0].real
    w = p["joint"]["coefficient"](acb(t), 0, 2, 0).real
    v = p["selected"](acb(t)).real
    s = p["kern"]["dim"]

    def join(tab, factor, scale):
        return algebra["add_inputs"](tab, [{e: x*scale**j for e,x in row.items()}
                                           for j,row in enumerate(factor)])

    tab = [{2*i-j: comb(j,i)*(s/2)**j for i in range(j+1)} for j in range(D+1)]
    for lo, hi, scale, perverse in ((2,4,b/4,False),(6,8,c/8,False),(8,16,d/16,True)):
        factors = [(len(algebra["WEIGHTS"][i]),algebra["DETS"][i]) for i in range(lo,hi)]
        tab = join(tab,algebra["scalar_powers"](factors,D,perverse),scale)
    tab = join(tab,[{0:p["kern"]["p3"]["P"][j].get((0,0),0)} for j in range(D+1)],a)
    tab = join(tab,[{0:k} for k in p["old"]["moments"](D)],z)
    tab = join(tab,algebra["scalar_powers"]([(4,4)],D,True),w)
    mu = p["symplectic_moments"](2,D)
    tab = join(tab,[{0:sum(comb(j,k)*mu[k]*mu[j-k] for k in range(j+1))}
                    for j in range(D+1)],v)
    second = algebra["scalar_powers"]([(4,-2)],D,False)
    marked_one = old["linear"]["marked_factors"](D)
    # The -2 determinant exponent on the exchanged lift inverts each marked
    # row, and duality makes each such row reciprocal.
    one = join(tab,second,c/8)
    scalar = join(one,algebra["scalar_powers"]([(4,2)],D,False),c/8)
    marked = join(one,marked_one,c/8)
    extent = s+2*abs(a)+3*abs(b)+4*abs(c)+arb(23)*abs(d)/4+8*(abs(v)+abs(w)+abs(z))
    if extra:
        cross=join(join(tab,marked_one,c/8),marked_one,c/8)
        factors=[[],[]]
        states={(0,0,0,0):1}
        for n in range(D+1):
            rows=[{},{}]
            for shape,mult in states.items():
                shift=shape[-1]
                part=tuple(x-shift for x in shape)
                for i,signature in enumerate(((2,1,1,0),(2,2,0,0))):
                    if part==signature:
                        rows[i][2*shift+2]=mult
            for i,row in enumerate(rows):
                factors[i].append(row)
            if n<D:
                nxt=Counter()
                for shape,mult in states.items():
                    for j in range(4):
                        for k in (-1,1):
                            child=list(shape)
                            child[j]+=k
                            if child==sorted(child,reverse=True):
                                nxt[tuple(child)]+=mult
                states=nxt
        assert factors[0][2]=={0:2} and factors[1][2]=={}
        return [scalar]+[join(one,f,c/8) for f in factors]+[cross],marked,extent
    return scalar, marked, extent


def project(tab, extent, j, e):
    bn, branch = arb(1), arb(0)
    for k in range(1,D//2+1):
        bn *= (arb(3)/2-k)/k
        if 2*k >= j:
            branch += 2*t.sqrt()*bn*comb(2*k,j)/(4*t)**k*tab[2*k-j].get(e,0)
    k += 1
    bn *= (arb(3)/2-k)/k
    ratio = extent**2/(4*t)*comb(2*k+2,j)/comb(2*k,j)
    assert ratio < 1
    tail = 2*t.sqrt()*abs(bn)*(extent**2/(4*t))**k*comb(2*k,j)/(extent**j*(1-ratio))
    return branch+arb(0,tail.upper())

