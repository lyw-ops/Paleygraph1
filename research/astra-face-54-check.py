"""Enclose the quantile LP on both entire optimal faces at p=97."""
from fractions import Fraction as F
from itertools import combinations
import json
from pathlib import Path
import sys

from flint import arb, acb, ctx, fmpq_poly, fmpz_poly

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from endpoint_extension_certificate import solve
from theta import paley_sign

ctx.prec = 320
n = 48
mask = paley_sign(97)
modulus = fmpq_poly(fmpz_poly.cyclotomic(n))
powers = [fmpq_poly([0, 1])**i % modulus for i in range(n)]
cosine = [(arb(2*i)/n).cos_pi() for i in range(n)]
active = {1: [2,3,5,6,7,8,11,13,14,18,19,22], -1: [1,4,9,12,15,16,17,20,23,24]}
free = [10,21]
scale = 10**19
zero = fmpq_poly()
one = fmpq_poly([1])


def ball(poly):
    return sum((arb(c.numerator)/c.denominator)*cosine[i] for i,c in enumerate(poly)) if poly else arb(0)


def rb(x):
    return arb(x.numerator)/x.denominator


def rounded(x):
    # Decimal proposal is accepted only by outward interval comparison.
    k = int((x*scale).mid().floor().unique_fmpz())
    v = F(k, scale)
    assert abs(x-rb(v)) < arb(2)/scale
    return v


def system(s, ids):
    return [[sum(powers[(j*h)%n] for h in {i,(-i)%n}) for i in ids]
            for j in range(1,25) if mask[j] == -s]


def vector(ids, coeff, root):
    out = [zero]*n
    out[0] = root
    for i,c in zip(ids,coeff):
        out[i] = out[-i%n] = c
    return out


def faces():
    base = {}
    mass = {}
    for s,ids in active.items():
        mat = system(s,ids)
        coeff,rank = solve(mat,[-one]*len(mat),modulus)
        assert rank == len(ids) and all(ball(c)>0 for c in coeff)
        base[s] = vector(ids,coeff,one)
        mass[s] = sum(base[s]) % modulus
    assert mass[1]*mass[-1] % modulus == n
    # Opposite exposure leaves both shared coordinates available; minus is fixed.
    mat = system(-1,active[-1]+free)
    _, rank = solve(mat,[zero]*len(mat),modulus)
    assert rank == len(active[-1])+len(free)
    dirs = []
    for i in free:
        col = system(1,[i])
        coeff,rank = solve(system(1,active[1]),[-r[0] for r in col],modulus)
        assert rank == len(active[1])
        d = vector(active[1]+[i],coeff+[one],zero)
        assert sum(d) % modulus == zero
        dirs.append(d)
    coeffs = [base[1]]+dirs
    pos = [tuple(ball(c[i])/ball(mass[1]) for c in coeffs) for i in range(n)]
    neg = [ball(c)/ball(mass[-1]) for c in base[-1]]
    return pos,neg


def add(a,b):
    return tuple(x+y for x,y in zip(a,b))


def sub(a,b):
    return tuple(x-y for x,y in zip(a,b))


def at(f,pt):
    return f[0]+f[1]*pt[0]+f[2]*pt[1]


def intersection(a,b):
    det = a[1]*b[2]-a[2]*b[1]
    if det:
        return ((a[2]*b[0]-a[0]*b[2])/det,(a[0]*b[1]-a[1]*b[0])/det)


def certificate(t,Y,P,N,E):
    # Keep exact rational scores and uniform error bars valid on the entire box.
    p = [tuple(map(rounded,row)) for row in P]
    m = [rounded(x) for x in N]
    z = [rounded(x) for x in Y]
    sites = sorted(set(z) | {-x for x in z})
    constraints = [(F(0),1,0),(F(1),-1,0),(F(0),0,1),(F(1),0,-1)]
    for row in p:
        if any(row):
            constraints.append(add(row,(F(6,scale),0,0)))
    cells=[]
    for a,b in zip(sites,sites[1:]):
        left = tuple(sum(row[j] for score,row in zip(z,p) if score>a) for j in range(3))
        right = sum(w for score,w in zip(z,m) if -score>a)
        cells.append((b-a,left,right))
    def envelope(pt):
        return sites[0]+sum(gap*max(at(left,pt),right) for gap,left,right in cells)
    cuts=constraints+[sub(left,(right,0,0)) for _,left,right in cells]
    best=None
    for a,b in combinations(cuts,2):
        pt=intersection(a,b)
        if pt is None or any(at(c,pt)<0 for c in constraints):
            continue
        value=envelope(pt)
        if best is None or value<best[0]:
            best=value,pt
    val,pt=best
    # A tiny movement towards a strictly positive relative-interior row proves feasibility.
    interior=(F(1,10000),)*2
    w=F(1,10**11)
    trial=tuple((1-w)*x+w*y for x,y in zip(pt,interior))
    assert all((at(row,tuple(map(rb,trial)))>=0) for row in P)
    err=F(2,scale)+(sites[-1]-sites[0])*6*n/scale
    lo=val-err
    hi=envelope(trial)+err
    baseline=envelope((0,0))
    assert hi-lo<F(1,10**8)
    def interval(x,y):
        # Fixed rational endpoints for deterministic shortened receipts.
        den=10**9
        return [int(x*den//1),int(-(-y*den//1))]
    print(json.dumps(dict(t=t,field=97,units='1e-9',whole_face=interval(lo,hi),
        least_norm=interval(baseline-err,baseline+err),
        charged_per_step=interval((lo-rounded(E)/4-F(1,scale))/t,
                                  (hi-rounded(E)/4+F(1,scale))/t),
        free_anchor_ratios=[round(float(x),8) for x in trial]),sort_keys=True),flush=True)


def main():
    P,N=faces()
    v=[arb(0)]*n
    for t in range(1,33):
        a=[abs(x) for x in v]
        a[0]=(4+v[0]**2).sqrt()
        f=acb.dft(a)
        v=[x.real for x in acb.dft([int(s)*x for s,x in zip(mask,f)],inverse=True)]
        if t in (1,2,4,8,16,32):
            certificate(t,[arb(n).sqrt()*x for x in v],P,N,sum(x*x for x in v))

if __name__=='__main__':
    main()
