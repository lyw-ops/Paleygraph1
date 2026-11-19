"""Exact cyclic-convolution certificate for a finite nested arithmetic sign.

Requires the audited rank-three determinant theorem in astra-nested-moment-31.md.
Uses exact FLINT integer polynomials; Arb only encloses the explicit error bound.
"""

import argparse
from fractions import Fraction
import json
from pathlib import Path
import sys

from flint import arb, ctx, fmpz_poly

sys.path.insert(0,str(Path(__file__).resolve().parent))
from importlib import import_module
full_sign=import_module('nested-lift-31').full_sign


def certificate(prime):
    sign=[int(x) for x in full_sign(prime)]
    N=len(sign)
    modulus=fmpz_poly([-1]+[0]*(N-1)+[1])
    def conv(x,y):
        values=[int(x) for x in ((fmpz_poly(x)*fmpz_poly(y))%modulus).coeffs()]
        return values+[0]*(N-len(values))
    def direct(x,y):
        return [sum(x[j]*y[(i-j)%N] for j in range(N)) for i in range(N)]
    double=conv(sign,sign)
    twist=[a*b for a,b in zip(sign,double)]
    u=[a*b for a,b in zip(sign,conv(sign,twist))]
    # Exact Pfaff relation: u = r o inversion + sign.
    pure=[u[(-i)%N]-sign[(-i)%N] for i in range(N)]
    first=conv(sign,pure)
    pair=conv(pure,pure)
    numerator=sum(first[j]*pair[(-j)%N] for j in range(N))
    value=Fraction(numerator,prime**5)
    if prime<=41:
        assert double==direct(sign,sign)
        assert first==direct(sign,pure) and pair==direct(pure,pure)
        assert numerator==direct(direct(direct(pure,pure),pure),sign)[0]
    ctx.prec=160
    exact=arb(value.numerator)/value.denominator
    # Word R^3 tensor M has dimension27 and rank<=108. At most20
    # bad input characters, with product-versus-word trace error<=54 each.
    error=108/arb(prime).sqrt()+arb(1080)/(prime-1)
    gap=(exact+1-error).lower()
    excludes_negative=bool(gap>0)
    return dict(order=prime,full_character_count=N,
                exact_contraction=str(value),raw_integer_numerator=str(numerator),
                raw_integer_denominator=str(prime**5),
                error_bound=str(error.upper()),
                negative_phase_exclusion_gap=str(gap),
                phase_plus_one_certified=excludes_negative,
                phase_result=1 if excludes_negative else None,
                small_direct_integer_crosscheck=prime<=41,
                scope='finite field sign, assuming audited rank-three determinant theorem; no all-primes sign claim')


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('primes',nargs='*',type=int,default=[13,9413,153649])
    args=p.parse_args()
    for prime in args.primes:
        print(json.dumps(certificate(prime),sort_keys=True),flush=True)


if __name__=='__main__':main()
