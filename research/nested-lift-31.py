"""Unfold the nested Paley field to full-character complex fields.

All emitted moments are floating diagnostics; no monodromy group or
limiting moment is asserted. The finite alias identities are algebraic.
"""

import argparse
import json
from math import sqrt
from pathlib import Path
import sys

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from theta import prime_divisors, prime_field_generator, paley_sign
from square_control import square_field_sign


def full_sign(q, root=None):
    if root is None:
        generator = prime_field_generator(q)
        character = np.full(q, -1, dtype=np.int8)
        character[0] = 0
        character[[x*x % q for x in range(1,q//2+1)]] = 1
        sign = np.empty(q-1, dtype=np.int8)
        value = 1
        for j in range(q-1):
            sign[j] = character[(1-value)%q]
            value = value*generator % q
        return sign
    p = root
    character = np.array([0]+[1 if pow(x,(p-1)//2,p)==1 else -1
                              for x in range(1,p)], dtype=np.int8)
    nonsquare = int(np.flatnonzero(character == -1)[0])
    def mul(x,y):
        a,b=x;c,d=y
        return ((a*c+nonsquare*b*d)%p,(a*d+b*c)%p)
    def power(x,k):
        ans=(1,0)
        while k:
            if k%2:ans=mul(ans,x)
            x=mul(x,x);k//=2
        return ans
    factors=prime_divisors(q-1)
    generator=next((a,b) for b in range(1,p) for a in range(p)
                   if all(power((a,b),(q-1)//d)!=(1,0) for d in factors))
    sign=np.empty(q-1,dtype=np.int8);value=(1,0)
    for j in range(q-1):
        a,b=value
        sign[j]=character[((1-a)**2-nonsquare*b*b)%p]
        value=mul(value,generator)
    return sign


def analyze(q, root=None):
    sign=full_sign(q,root)
    n=(q-1)//2
    subgroup=square_field_sign(root) if root else paley_sign(q)
    assert np.array_equal(sign[::2],subgroup)
    def act(s,v):
        return np.fft.fft(s*np.fft.ifft(v))
    j=np.fft.fft(sign)/sqrt(q)
    v=act(sign,j*j)
    r=act(sign,j*v)
    shift=lambda f:np.roll(f,n)
    x=np.fft.fft(subgroup).real/sqrt(n)
    y=act(subgroup,x*x).real
    z=act(subgroup,x*y).real
    x_alias=sqrt(q/n)*j[:n].real
    y_alias=q/(4*n)*(v[:n]+v[n:]).real-x/sqrt(n)
    z_alias=sqrt(q/n)*q/(4*n)*(r[:n]+r[n:]).real-y/sqrt(n)
    errors=dict(seed_shift_conjugation=float(np.max(np.abs(shift(j)-j.conj()))),
                first_feedback_imag=float(np.max(np.abs(v.imag))),
                x_alias=float(np.max(np.abs(x_alias-x))),
                y_alias=float(np.max(np.abs(y_alias-y))),
                z_alias=float(np.max(np.abs(z_alias-z))))
    assert max(errors.values())<1e-9,errors
    good=np.ones(q-1,dtype=bool);good[[0,n]]=False
    J,V,R=j[good],v[good],r[good]
    S=shift(r)[good]
    c=float(np.mean(j.real*r.real**3))
    d=float(np.mean(j.real*r.real**2*shift(r).real))
    c3=np.mean(j.conj()*r**3)
    c3alt=np.mean(j*r**3)
    c21=np.mean((j+j.conj())*r*r*r.conj())
    expanded_c=float((c3+c3alt).real/8+3*c21.real/8)
    assert abs(c-expanded_c)<1e-10
    a=sqrt(q/n); b=a*q/(4*n)
    mixed=float(np.mean(x*z**3))
    lifted=a*b**3*(2*c+6*d)
    exact_lifted=float(np.mean(x*(z+y/sqrt(n))**3))
    assert abs(lifted-exact_lifted)<1e-9
    def mean(value):
        a=np.mean(value)
        return dict(real=float(a.real),imag=float(a.imag))
    row=dict(order=q,square_root=root,errors=errors,
             max_abs_nested_full=float(np.max(np.abs(R))),
             moments=dict(abs_r2=mean(abs(R)**2),abs_r4=mean(abs(R)**4),
                          r3_conj_j=mean(R**3*J.conj()),r3_j=mean(R**3*J),
                          r2_conjr_conjj=mean(R**2*R.conj()*J.conj()),
                          r2_conjr_j=mean(R**2*R.conj()*J),
                          r_rshift=mean(R*S),r_conj_rshift=mean(R*S.conj()),
                          abs_r2_abs_rshift2=mean(abs(R)**2*abs(S)**2),
                          real_r4=mean(R.real**4),real_r3_real_rshift=mean(R.real**3*S.real),
                          xz3=mean(x*z**3)),
             cubic_reduction=dict(C=c,D=d,coefficient=a*b**3,
                                  C_from_complex_terms=expanded_c,
                                  full_r3_conj_j=dict(real=float(c3.real),imag=float(c3.imag)),
                                  full_r3_j=dict(real=float(c3alt.real),imag=float(c3alt.imag)),
                                  full_mixed_21_sum=dict(real=float(c21.real),imag=float(c21.imag)),
                                  exact_lifted_moment=exact_lifted,
                                  reduced_lifted_moment=lifted,
                                  actual_mixed_moment=mixed,
                                  remainder=mixed-lifted),
             scope='floating full-character diagnostics; no group or limiting-value assertion')
    print(json.dumps(row,sort_keys=True),flush=True)


def exact_subgroup_audit(q,root=None):
    sign=full_sign(q,root).tolist()
    subgroup=sign[::2]
    def conv(x,y):
        N=len(x)
        return [sum(int(x[j])*int(y[(i-j)%N]) for j in range(N)) for i in range(N)]
    full=conv(sign,sign);half=conv(subgroup,subgroup)
    assert all(s*(2*half[i]-full[2*i]+2)==0 for i,s in enumerate(subgroup))
    print(json.dumps(dict(kind='exact integer subgroup convolution audit',order=q,
                          square_root=root,passed=True),sort_keys=True),flush=True)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('primes',nargs='*',type=int,default=[401,9413,153649])
    parser.add_argument('--square-roots',nargs='*',type=int,default=[97,389])
    args=parser.parse_args()
    for q,root in [(13,None),(17,None),(25,5),(49,7)]:
        exact_subgroup_audit(q,root)
    for p in args.primes:analyze(p)
    for p in args.square_roots:analyze(p*p,p)


if __name__=='__main__':main()
