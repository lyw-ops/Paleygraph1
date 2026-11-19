"""Certify lower bounds for all-cycle coverings on the actual p=97 optimal faces."""
import importlib.util
import json
from math import isqrt
from pathlib import Path

import numpy as np
from flint import acb, arb, ctx
from scipy.optimize import linprog


def load(name):
    path = Path(__file__).with_name(name)
    spec = importlib.util.spec_from_file_location('face54', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def edge_check():
    edges = 0
    least = 10000
    for p in range(29, 302, 4):
        if any(p % d == 0 for d in range(2, isqrt(p) + 1)):
            continue
        squares = {i*i % p for i in range(1, p)}
        chi = [0] + [1 if i in squares else -1 for i in range(1,p)]
        for d in squares - {1}:
            sign = chi[(1-d) % p]
            seen = sum(chi[(1-e)%p] == sign and chi[(d-e)%p] == sign for e in squares)
            trace = sum(chi[e]*chi[(1-e)%p]*chi[(d-e)%p] for e in range(p))
            assert 8*seen == p - 11 - 4*sign + trace and trace*trace <= 4*p
            least = min(seen, least)
            edges += 1
    print(json.dumps(dict(kind='triangle_extension_exact', maximum_prime_checked=293,
                          oriented_ratios=edges, minimum_extensions=least), sort_keys=True))


def pack(T, q, cosines):
    # Even per-orbit masses. Only the verification of the proposal determines the receipt.
    if not T:
        return arb(0)
    sizes = np.array([1 if j in (0,24) else 2 for j in T])
    cols = [[row[j] for j in T] for row in cosines]
    c = np.array([[float(x) for x in row] for row in cols])
    opt = linprog(-np.ones(len(T)), A_ub=np.vstack((1+2*c, 1-2*c, np.ones(len(T)))),
                  b_ub=np.ones(2*len(c)+1), bounds=[(0, float(q)*h) for h in sizes], method='highs')
    assert opt.success
    w = [arb(max(0,round(x*10**9)))/10**9 for x in opt.x]
    m = sum(w)
    if not m > 0:
        return arb(0)
    error = max(abs(sum(a*b for a,b in zip(w,row))).upper() for row in cols)
    den = max([arb(1), (m+2*error).upper()] + [(a/(q*int(h))).upper() for a,h in zip(w,sizes)])
    return (m/den).lower()


def main():
    edge_check()
    face = load('astra-face-54-check.py')
    ctx.prec = 384
    P,N = face.faces()
    n = len(N)
    # An explicit cyclotomic all-simple-cycle packing on the TRUE minus support.
    numerator = {0:2,24:3}
    for j in (4,12,16,20):
        numerator[j] = numerator[-j % n] = 2
    assert all(N[j] > 0 and arb(v)/39 < N[0] for j,v in numerator.items())
    assert sum(numerator.values()) == 21 and face.mask[24] == 1
    for f in range(1,n//2):
        if face.mask[f] != 1:
            continue
        c = sum(w*face.powers[(j*f)%n] for j,w in numerator.items()) % face.modulus
        assert c in (3*face.one,-3*face.one) or abs(face.ball(c)) < 3
    print(json.dumps(dict(kind='true_exposed_parity',field=97,side='minus',parity='even',
                          simple_cycle_packing='7/13',true_mass='1/2',denominator=39,
                          per_site_numerators=numerator),sort_keys=True))
    # Strict relative interior on both sides exposes the exact opposed supports.
    interior = [a+(b+c)/10000 for a,b,c in P]
    law = {1: interior, -1: N}
    supports = {s: {j for j,x in enumerate(row) if x > 0} for s,row in law.items()}
    assert supports[1] & supports[-1] == {0} and len(supports[1] | supports[-1]) == n
    assert all(x.is_zero() or x>0 for row in law.values() for x in row)
    cosines = {s: [[(arb(2*j*f)/n).cos_pi() for j in range(n//2+1)]
                   for f in range(1,n//2+1) if face.mask[f] == -s] for s in law}
    cache={s:{} for s in law}
    v=[arb(0)]*n
    records=[]
    for t in range(1,33):
        activation=[abs(x) for x in v]
        activation[0]=(4+v[0]**2).sqrt()
        f=acb.dft(activation)
        v=[x.real for x in acb.dft([int(s)*x for s,x in zip(face.mask,f)],inverse=True)]
        if t < 16:
            continue
        scale=10**6
        z = [arb(n).sqrt()*x for x in v]
        rounded=[round(float(x)*scale) for x in z]
        assert all(abs(x-arb(k)/scale) < arb(1)/scale for x,k in zip(z,rounded))
        assert all(rounded[i]==rounded[-i%n] for i in range(n))
        sites=sorted({s*rounded[j] for s in law for j in supports[s]})
        whole=arb(sites[0])/scale
        lower=whole
        for a,b in zip(sites,sites[1:]):
            mass={}
            bounds={}
            for s in law:
                T=tuple(j for j in sorted(supports[s]) if j<=n//2 and s*rounded[j]>a)
                mass[s]=sum((1 if j in (0,n//2) else 2)*law[s][j] for j in T)
                if T not in cache[s]:
                    cache[s][T]=pack(T,law[s][0],cosines[s])
                # A true row restricted to T is feasible in every translated cycle packing.
                bounds[s]=max(arb(mass[s]).lower(),cache[s][T])
            gap=arb(b-a)/scale
            whole+=gap*max(arb(mass[s]).upper() for s in law)
            lower+=gap*max(bounds.values())
        whole+=arb(1)/scale
        lower-=arb(1)/scale
        E=sum(x*x for x in v)/4
        records.append((t,lower,whole,E))
    gap=min(((lo-hi)/t).lower() for t,lo,hi,E in records)
    charged=min(((lo-E)/t).lower() for t,lo,hi,E in records)
    def floor6(x):
        return int((x*10**6).lower().floor().unique_fmpz())
    assert gap>0 and charged>0
    print(json.dumps(dict(kind='integrated_all_cycle_lower',field=97,precision_bits=ctx.prec,
         integer_units='1e-6',all_integer_depths=[16,32],threshold_family='actual exposed tails',
         distinct_tail_proposals={s:len(v) for s,v in cache.items()},
         minimum_cover_minus_full_face_per_step_lower=floor6(gap),
         minimum_cover_minus_terminal_quarter_energy_per_step_lower=floor6(charged),
         endpoints=[dict(t=t,cover_lower=floor6(lo),full_face_upper=-floor6(-hi),
                 quarter_energy_lower=floor6(E),quarter_energy_upper=-floor6(-E))
                 for t,lo,hi,E in records if t in (16,32)]),sort_keys=True))

if __name__=='__main__':
    main()
