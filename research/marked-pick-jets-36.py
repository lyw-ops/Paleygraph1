"""Exact rational jets of the actual marked central path at equal weights.

The group-algebra recurrence uses exact rational cyclic convolution and
the integer Paley multiplier. Negative transformed Pick matrices obstruct
a full right-half-plane marked continuation; positive finite tests do
not establish continuation. See the accompanying note when accepted.
"""
import argparse
import json
from pathlib import Path
import sys
from flint import fmpq, fmpq_mat, fmpq_poly

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from theta import paley_sign
from square_control import square_field_sign


def truncate(poly, degree):
    return fmpq_poly([poly[i] for i in range(degree)])


def cyclic(poly, n):
    return fmpq_poly([poly[i]+(poly[i+n] if i+n<len(poly) else 0)
                      for i in range(n)])


def jets(sign, side, order):
    n=len(sign)
    mask=[int(j!=0 and s==side) for j,s in enumerate(sign)]
    def project(poly):
        return fmpq_poly([poly[i]*mask[i] for i in range(n)])
    mask_poly=fmpq_poly(mask)
    U=[fmpq_poly([1])]
    R=[fmpq_poly([1])]
    roots=[fmpq(1)]
    for k in range(1,order+1):
        C=sum((cyclic(U[j]*R[k-j],n) for j in range(1,k)),fmpq_poly([]))
        Uk=project(-C+R[-1])-mask_poly*(sum(R[-1].coeffs())/n)
        Rk=-Uk-C
        U.append(Uk);R.append(Rk);roots.append(sum(Uk.coeffs()))
        assert Uk[0]==0
        assert all(Uk[j]==0 for j in range(n) if not mask[j])
        assert project(Rk+R[k-1])-mask_poly*(sum(R[k-1].coeffs())/n)==0
        assert cyclic(sum((U[j]*R[k-j] for j in range(k+1)),fmpq_poly([])),n)==0
    root=fmpq_poly(roots)
    g=fmpq_poly([])
    h=root-1
    for k in range(1,order+1):
        g+=truncate(h**k,order+1)*fmpq((-1)**k,k)
    sqrt_minus=fmpq_poly([])
    coefficient=fmpq(1)
    for k in range(1,order+1):
        coefficient*=fmpq(3-2*k,2*k)
        sqrt_minus+=fmpq_poly([0]*k+[coefficient])
    composed=fmpq_poly([])
    for k in range(order,-1,-1):
        composed=truncate(composed*sqrt_minus,order+1)+g[k]
    assert composed[1]==fmpq(n-1-side,4*n)
    return roots,composed


def check(q,root,size):
    sign=square_field_sign(root) if root else paley_sign(q)
    for side in (1,-1):
        roots,g=jets(sign,side,2*size-1)
        minors=[]
        for k in range(1,size+1):
            determinant=fmpq_mat([[g[i+j+1] for j in range(k)]
                                 for i in range(k)]).det()
            minors.append(determinant)
        print(json.dumps(dict(kind='exact_transformed_marked_Pick_jet_test',
              q=q,side=side,size=size,
              actual_normalized_mark_coefficients=[str(x) for x in roots],
              transformed_coefficients=[str(g[k]) for k in range(2*size)],
              leading_hankel_minors=[str(x) for x in minors],
              leading_minor_signs=[int(x>0)-int(x<0) for x in minors],
              negative_detected=any(x<0 for x in minors),
              scope='exact necessary test for full RHP continuation; finite positive tests are inconclusive'),
              sort_keys=True),flush=True)


if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--primes',type=int,nargs='*',default=[])
    ap.add_argument('--square-roots',type=int,nargs='*',default=[])
    ap.add_argument('--size',type=int,default=6)
    args=ap.parse_args()
    for p in args.primes: check(p,None,args.size)
    for r in args.square_roots: check(r*r,r,args.size)
