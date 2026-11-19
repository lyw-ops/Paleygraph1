"""Exact Mellin determinant checks for the quadratic Legendre source."""
import json
from math import gcd
from pathlib import Path
import runpy

from flint import fmpz_poly

known = runpy.run_path(str(Path(__file__).with_name("rank-four-arithmetic-56-check.py")))
data = known["data"]
cycconv = known["cycconv"]
reduce_at_character = known["reduce_at_character"]
determinant_times_24 = known["determinant_times_24"]


def raw_source(p, d):
    field, ell, _, _ = data(p,d)
    square = cycconv(ell,ell)
    legendre = [a*b for a,b in zip(ell,square)]
    assert sum(legendre)==2
    symmetric = cycconv(legendre,legendre)
    row = [a*(b+2*(field.q+1)) for a,b in zip(ell,symmetric)]
    return field,row


def check(p, d):
    base, ell, _, _ = data(p,d)
    q,n = base.q,base.q-1
    modulus = fmpz_poly.cyclotomic(n)
    traces = []
    logs = []
    for extension in range(1,5):
        field,row = raw_source(p,d*extension)
        norm = field.g**((field.q-1)//n)
        generator = field.embed(base,base.g)
        log = next(k for k in range(n) if generator**k == norm)
        assert gcd(log,n)==1
        folded = [0]*n
        for index,value in enumerate(row):
            folded[index*log % n] += value
        traces.append(folded)
        logs.append(log)
    count=0
    for k in range(1,n):
        if k==n//2:
            continue
        values = [reduce_at_character(row,k,modulus,n) for row in traces]
        jacobi = reduce_at_character(ell,k,modulus,n)
        expected = 24*q**6*jacobi**4
        assert (determinant_times_24(values)-expected) % modulus == 0
        count+=1
    assert count==q-3
    print(json.dumps(dict(kind="quadratic_legendre_source_determinant",field=q,
                          good_characters=count, jacobi_exponent=4,constant=1,
                          norm_generator_logs=logs, largest_field=q**4),sort_keys=True))


if __name__ == "__main__":
    for p,d in ((5,1),(3,2),(13,1)):
        check(p,d)
