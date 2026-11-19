"""Exact normalization audits and float word diagnostics; no stationary solve.
Run with python -B. Writes JSONL to stdout only. Imported field constructors
are read-only. Float moments do not identify arithmetic invariant spaces.
"""
from fractions import Fraction as F
from math import isqrt, sqrt
from pathlib import Path
import sys
import json
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from theta import paley_sign
from square_control import square_field_sign


def emit(**kw):
    print(json.dumps(kw, sort_keys=True), flush=True)


def K(s, a):
    return np.fft.ifft(s * np.fft.fft(a)).real


def fields(s):
    n = len(s)
    x = np.fft.fft(s).real/sqrt(n)
    y = K(s, x*x)
    z = K(s, x*y)
    d = K(s, x**4)
    return x, y, z, d


def conv(a,b):
    n=len(a)
    return [sum(a[j]*b[(i-j)%n] for j in range(n)) for i in range(n)]


def exact(q, r=0):
    s = [int(v) for v in (square_field_sign(r) if r else paley_sign(q))]
    n=len(s)
    ss=conv(s,s)
    t=[a*b for a,b in zip(s,ss)]
    st=conv(s,t)
    u=[a*b for a,b in zip(s,st)]
    tt,uu=conv(t,t),conv(u,u)
    values={
        'x2': F(ss[0],n),
        'y2': F(tt[0],n*n),
        'y4': F(conv(tt,tt)[0],n**4),
        'x2y2': F(conv(ss,tt)[0],n**3),
        'x2z2': F(conv(ss,uu)[0],n**4),
        'z4': F(conv(uu,uu)[0],n**6),
        'xz3': F(conv(conv(s,u),uu)[0],n**5),
    }
    x,y,z,d=fields(np.array(s))
    obs={'x2':np.mean(x*x),'y2':np.mean(y*y),'y4':np.mean(y**4),
         'x2y2':np.mean(x*x*y*y),'x2z2':np.mean(x*x*z*z),
         'z4':np.mean(z**4),'xz3':np.mean(x*z**3)}
    err=max(abs(float(values[k])-obs[k]) for k in values)
    assert err < 2e-10
    # Exact Parseval for y=K(x^2), including the root.
    assert values['y2'] == F(conv(ss,ss)[0],n*n)-values['x2']**2
    emit(kind='exact_cyclic_convolution',q=q,r=r,
         rational_moments={k:str(v) for k,v in values.items()},
         max_float_crosscheck_error=err,passed=True)


def sieve(N):
    a=bytearray(b'\x01')*(N+1); a[0:2]=b'\x00\x00'
    for p in range(2,isqrt(N)+1):
        if a[p]: a[p*p::p]=b'\x00'*(((N-p*p)//p)+1)
    return [p for p in range(2,N+1) if a[p]]


def diag(q,r=0):
    s=square_field_sign(r) if r else paley_sign(q)
    x,y,z,d=fields(s)
    # All frequencies; removing bounded good-character exceptions is o(1)
    # at these fixed polynomial complexities, but none is asserted identified.
    obs={
        'x2':np.mean(x*x),'x4':np.mean(x**4), 'x6':np.mean(x**6),
        'y2':np.mean(y*y),'y4':np.mean(y**4),'y6':np.mean(y**6),
        'x2y2':np.mean(x*x*y*y),'x4y2':np.mean(x**4*y*y),
        'x2y4':np.mean(x*x*y**4),
        'z2':np.mean(z*z),'x2z2':np.mean(x*x*z*z),'z4':np.mean(z**4),
        'd2':np.mean(d*d),'d4':np.mean(d**4), 'xz3':np.mean(x*z**3),
    }
    known={'x2':1.,'x4':1.5,'x6':2.5,'y2':.5,'y4':.625,
           'y6':35/32,'x2y2':.5,'x4y2':.75,'x2y4':.625,
           'z2':.5,'d2':17/8,'d4':739/64}
    emit(kind='floating_word_diagnostic',q=q,r=r,
         legendre_signs={str(a):(1 if r else (1 if pow(a,(q-1)//2,q)==1 else -1))
                         for a in (2,3,5)},
         moments={k:float(v) for k,v in obs.items()},
         proven_limit_errors={k:float(obs[k]-v) for k,v in known.items()},
         uncomputed_invariant_tests=['x2z2','z4','xz3'])


def cm(p):
    # E: y^2=x^3-x. Exact integer point count, with zero character retained.
    a=0
    for x in range(p):
        v=(x*x*x-x)%p
        a-=0 if v==0 else (1 if pow(v,(p-1)//2,p)==1 else -1)
    emit(kind='exact_cm_phase_example_not_a_paley_word',p=p,a_p=a,
         signs={str(k):pow(k,(p-1)//2,p) for k in (2,3,5)},
         trace_sym2_normalized=str(F(a*a,p)-1),
         trace_H1_square_normalized=str(F(a*a,p)-2))


def main():
    # U(1) negative-type countermodel: mixed second moment 2 Re(c^e).
    re,im=F(3,5),F(4,5)
    assert re*re+im*im==1
    emit(kind='exact_category_countermodel_not_a_paley_word',
         c_real=str(re),c_imag=str(im),
         prime_mixed_second=str(2*re),
         square_mixed_second=str(2*(re*re-im*im)),
         gap=str(2*re-2*(re*re-im*im)))
    for q,r in [(13,0),(17,0),(25,5),(49,7),(121,11)]: exact(q,r)
    for p in (241,601,1201): cm(p)
    ps=sieve(301000)
    chosen=[next(p for p in ps if p>=lo and p%120==1)
            for lo in (10000,50000,150000,290000)]
    chosen += [9413,37253,153649]
    for p in chosen: diag(p)
    for r in (97,193,389,541): diag(r*r,r)

if __name__=='__main__': main()
