"""Exact two-variable Paley central curves, discriminants and Arb checks.

The examples are p=17 (plus) and q=25 (minus). All symbolic identities
use integer multivariate polynomials. Root locations and stationary
normalizations use outward-rounded Arb/Acb arithmetic. No optimizer.
"""

from fractions import Fraction
import json
from pathlib import Path
import sys

from flint import acb, arb, ctx, fmpz_mat, fmpz_mpoly_ctx, fmpz_poly

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from theta import paley_sign
from square_control import square_field_sign


D17 = [1073741824,5100273664,22632464384,57327747072,
       113510973440,154099908608,126234796032,60087177216,
       15454106432,1677787440,1541785]
D25 = [452770725888,1798183452672,3282372771840,3748777500672,
       3044953824768,1804241889792,741518110656,194885931744,
       29203924365,1917983520,663424]


def emit(row):
    print(json.dumps(row, sort_keys=True), flush=True)


def ordinary(poly):
    coefficients = poly.to_dict()
    assert all(key[0] == 0 for key in coefficients)
    degree = max(key[1] for key in coefficients)
    return fmpz_poly([int(coefficients.get((0,i),0)) for i in range(degree+1)])


def model(order):
    ring = fmpz_mpoly_ctx.get(['r','tau'])
    r,t = ring.gens()
    if order == 17:
        Q = (4*t*t*r**5+(-4*t*t+32*t)*r**4
             +(-21*t*t-144*t-64)*r**3+(-6*t*t+32*t+128)*r*r
             +(15*t*t+144*t-64)*r+8*t*t-64*t)
        L = 8-t-(8+t)*r
        N = r*(16+6*t-2*(8-t)*r-4*t*r*r)
        denominator = 4*L
        A = 16+6*t
        eliminated = A*N*N-32*t*N*L-16*(8+7*t)*r*r*L*L
        assert eliminated == 8*(3*t+8)*r*Q
        disc_factor = ring.from_dict({(0,i):x for i,x in enumerate(D17)})
        assert Q.discriminant(0) == 2**18*t**4*disc_factor
        expected_den = -2**20*(t-8)*t*t*(3*t+8)**2
        expected_sum = -2**20*(t-8)*(3*t+8)*(7*t+8)**3*t**4
        assert Q.resultant(denominator,0) == expected_den
        assert Q.resultant(denominator+N,0) == expected_sum
        assert Q.subs({'r':-1}) == 256
        assert Q.subs({'r':1}) == -4*t*t
        coefficients = D17
    else:
        Q = ((5*t*t+12*t)*r**5+(-4*t*t+36*t+144)*r**4
             +(-34*t*t-384*t-864)*r**3+(-20*t*t+144*t+1152)*r*r
             +(21*t*t+360*t-432)*r+16*t*t-192*t)
        L = 12-t-(12+t)*r
        N = -r*L-8*t*(1-r*r)
        denominator = r*L-3*(4+t)*(1-r*r)
        eliminated = L*N*N-denominator**2*(r*r*L+4*t*r*(1-r*r))
        assert eliminated == 4*t*(r-1)*(r+1)*Q
        disc_factor = ring.from_dict({(0,i):x for i,x in enumerate(D25)})
        assert Q.discriminant(0) == 2304*(11*t+12)**4*disc_factor
        expected_den = -1728*(t+4)*t*t*(11*t+12)**4
        expected_sum = -20736*t*(2*t+3)*(11*t+12)**5
        assert Q.resultant(denominator,0) == expected_den
        assert Q.resultant(denominator+N,0) == expected_sum
        assert Q.subs({'r':-1}) == 2592
        assert Q.subs({'r':1}) == -8*t*(2*t+3)
        coefficients = D25
    emit({'kind':'exact_curve_elimination','order':order,'Q':str(Q),
          'discriminant':str(Q.discriminant(0)),
          'reconstruction_denominator_resultant':str(expected_den),
          'normalization_denominator_resultant':str(expected_sum),
          'minus_one_not_a_root':True,
          'scope':'two finite fields; not a uniform prime-domain theorem'})
    descending = coefficients[::-1]
    H = [[descending[2*j-i+1] if 0<=2*j-i+1<=10 else 0
          for j in range(10)] for i in range(10)]
    minors = [int(fmpz_mat([row[:k] for row in H[:k]]).det())
              for k in range(1,11)]
    assert all(value>0 for value in minors)
    emit({'kind':'exact_degree_ten_hurwitz','order':order,
          'coefficients_ascending':coefficients,
          'leading_hurwitz_minors':[str(x) for x in minors],
          'all_positive':True})
    roots = fmpz_poly(coefficients).complex_roots()
    assert sum(mult for z,mult in roots)==10
    assert all(z.real.upper()<0 for z,mult in roots)
    emit({'kind':'validated_discriminant_locations','order':order,
          'roots':[str(z) for z,mult in roots],
          'all_strictly_in_left_half_plane':True})
    return Q


def stationary(order, Q, tau):
    p,d = tau.numerator,tau.denominator
    coefficients = Q.to_dict()
    degree = max(key[1] for key in coefficients)
    polynomial = fmpz_poly([sum(int(value)*p**j*d**(degree-j)
                               for (i0,j),value in coefficients.items() if i0==i)
                            for i in range(6)])
    T = arb(p)/d
    n = (order-1)//2
    W = 1+(n-1)*T/n
    scale = (W/n).sqrt()
    candidates = []
    for z,mult in polynomial.complex_roots():
        if not z.imag.is_zero() or not (z.real>-1 and z.real<1):
            continue
        r = z.real
        if order == 17:
            if tau == 8 and r.contains(0):
                h = arb(1)
            else:
                L = 8-T-(8+T)*r
                h = r*(16+6*T-2*(8-T)*r-4*T*r*r)/(4*L)
            if not 1+h>0:
                continue
            alpha = 2/(1+h)
            x,y = alpha*r,alpha-1
            spectrum = [1+x*(arb.pi()*i/4).cos()+y*(-1)**i for i in range(n)]
            side = 1
        else:
            L = 12-T-(12+T)*r
            h = (-r*L-8*T*(1-r*r))/(r*L-3*(4+T)*(1-r*r))
            if not 1+h>0:
                continue
            alpha = 3/(1+h)
            x,y = alpha*r/2,alpha-1
            spectrum = [1+x*((arb.pi()*i/6).cos()+(5*arb.pi()*i/6).cos())
                        +y*(2*arb.pi()*i/3).cos() for i in range(n)]
            side = -1
        if all(value>0 for value in spectrum):
            candidates.append((r,h,spectrum,side))
    assert len(candidates)==1,(order,str(tau),len(candidates))
    r,h,spectrum,side = candidates[0]
    weights = [arb(1)]+[T/n]*(n-1)
    chosen = [scale*x for x in spectrum]
    opposite = [w/x for w,x in zip(weights,chosen)]
    A,B = (chosen,opposite) if side==1 else (opposite,chosen)
    signs = paley_sign(order) if order==17 else square_field_sign(5)
    v,phi = [a-b for a,b in zip(A,B)],[a+b for a,b in zip(A,B)]
    transformed = acb.dft([acb(x) for x in phi])
    applied = acb.dft([int(s)*x for s,x in zip(signs,transformed)])
    residual = [(x/n).real-y for x,y in zip(applied,v)]
    assert all(x.contains(0) for x in residual)
    assert (sum(A)/n-scale).contains(0) and (sum(B)/n-scale).contains(0)
    emit({'kind':'validated_stationary_reconstruction','order':order,
          'tau':str(tau),'chosen_sector':side,'r_interval':str(r),
          'reconstructed_h_interval':str(h),'marked_log_interval':str(A[0].log()),
          'residual_upper':str(max(abs(x).upper() for x in residual)),
          'positive_spectra_proved':True,
          'scope':'finite-field stationary normalization, no asymptotic estimate'})


def main():
    ctx.prec=224
    for order in (17,25):
        Q=model(order)
        for tau in (Fraction(1,20),Fraction(1),Fraction((order-1)//2),Fraction(20)):
            stationary(order,Q,tau)


if __name__=='__main__':
    main()
