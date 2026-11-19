"""Exact compact-group moments and finite nested Paley diagnostics.

Exact rational invariant counts use Schur--Weyl duality for SU(3), with
both determinant characters retained. Field comparisons are floating only.
"""

import argparse
from fractions import Fraction
from functools import lru_cache
from importlib import import_module
import json
from math import comb, factorial, sqrt
from pathlib import Path
import sys

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
lift = import_module("nested-lift-31")


@lru_cache(None)
def partitions3(n):
    return tuple((a, b, n-a-b) for a in range(n, -1, -1)
                 for b in range(min(a, n-a), -1, -1)
                 if 0 <= n-a-b <= b)


def tableaux(shape):
    hooks = 1
    for i, row in enumerate(shape):
        for j in range(row):
            hooks *= row-j + sum(other > j for other in shape[i+1:])
    return factorial(sum(shape)) // hooks


@lru_cache(None)
def su3_trace_moment(a, b):
    if (a-b) % 3:
        return 0
    answer = 0
    for left in partitions3(a):
        for right in partitions3(b):
            if left[0]-right[0] == left[1]-right[1] == left[2]-right[2]:
                answer += tableaux(left)*tableaux(right)
    return answer


def joint_xz(r, s):
    if (r+s) % 2:
        return Fraction(0)
    numerator = 0
    for i in range(r+1):
        h = 2*i-r
        for a in range(s+1):
            for b in range(s-a+1):
                first = su3_trace_moment(a, b)
                if not first:
                    continue
                for c in range(s-a-b+1):
                    d = s-a-b-c
                    second = su3_trace_moment(c, d)
                    if not second or h-(a-b)//3+(c-d)//3:
                        continue
                    multinomial = factorial(s)//(factorial(a)*factorial(b)*factorial(c)*factorial(d))
                    numerator += comb(r, i)*multinomial*first*second
    return Fraction(numerator, 2**((r+3*s)//2))


def su2_trace_moment(n):
    return 0 if n % 2 else comb(n, n//2)//(n//2+1)


def y_moment(n):
    return Fraction(sum(comb(n, i)*su2_trace_moment(i)*su2_trace_moment(n-i)
                        for i in range(n+1)), 2**n)


def laurent_product(left, right):
    result = {}
    for (a,b), x in left.items():
        for (c,d), y in right.items():
            key = (a+c,b+d)
            result[key] = result.get(key,0)+x*y
    return {key:value for key,value in result.items() if value}


def independent_weyl_audit():
    """A separate Laurent constant-term computation, without tableaux."""
    coordinates = [(1,0), (0,1), (-1,-1)]
    vandermonde = {(0,0):1}
    for i in range(3):
        for j in range(i+1,3):
            vandermonde = laurent_product(vandermonde,
                                         {coordinates[i]:1, coordinates[j]:-1})
    conjugate = {(-a,-b):value for (a,b),value in vandermonde.items()}
    density = laurent_product(vandermonde,conjugate)
    powers, opposite = [{(0,0):1}], [{(0,0):1}]
    for _ in range(8):
        powers.append(laurent_product(powers[-1],dict.fromkeys(coordinates,1)))
        opposite.append(laurent_product(opposite[-1],
                                        {(-a,-b):1 for a,b in coordinates}))
    for a in range(9):
        for b in range(9):
            value = laurent_product(laurent_product(powers[a],opposite[b]),density).get((0,0),0)
            assert value == 6*su3_trace_moment(a,b)
    return {"kind":"exact_independent_weyl_constant_term_audit",
            "su3_moment_pairs_checked":81,"powers_each_max":8,"passed":True}


MONOMIALS = ((2,0,0), (0,2,0), (0,0,2), (0,0,4), (2,0,2),
             (1,0,3), (0,0,6), (2,0,4), (1,0,5), (3,0,3),
             (0,2,2), (2,2,2), (0,4,0), (0,2,4), (0,0,8),
             (2,0,6), (1,0,7), (1,1,3), (1,0,1), (2,0,3))


def field_row(q, root=None):
    full = lift.full_sign(q, root)
    sign = full[::2]
    n = len(sign)
    def act(s, vector):
        return np.fft.fft(s*np.fft.ifft(vector))
    x = np.fft.fft(sign).real/sqrt(n)
    y = act(sign, x*x).real
    z = act(sign, x*y).real
    j = np.fft.fft(full)/sqrt(q)
    first = act(full, j*j)
    raw = act(full, j*first)
    # raw = A composed with frequency inversion + J/q, exactly.
    pure = (raw-j/q)[(-np.arange(2*n)) % (2*n)]
    shift = lambda array: np.roll(array, n)
    exact_x = sqrt(q)/(2*sqrt(n))*(j[:n]+shift(j)[:n]).real
    exact_y = q/(4*n)*(first[:n]+shift(first)[:n]).real-x/sqrt(n)
    exact_z = q**1.5/(8*n**1.5)*(pure[:n]+shift(pure)[:n]
                               +pure[:n].conj()+shift(pure)[:n].conj()).real
    exact_z -= y/sqrt(n)
    exact_z += x/(2*n)
    error = max(float(np.max(np.abs(exact_x-x))), float(np.max(np.abs(exact_y-y))),
                float(np.max(np.abs(exact_z-z))))
    assert error < 2e-10
    good = np.arange(n) != 0
    records = []
    for r, t, s in MONOMIALS:
        expected = joint_xz(r, s)*y_moment(t)
        value = float(np.mean((x[good]**r)*(y[good]**t)*(z[good]**s)))
        records.append({"powers": [r,t,s], "limiting_exact": str(expected),
                        "finite_good_mean": value, "difference": value-float(expected)})
    full_good = np.ones(2*n,dtype=bool)
    full_good[[0,n]] = False
    A,C,J = pure[full_good],shift(pure)[full_good],j[full_good]
    phase_tests = []
    for label,array,expected in (("J*A^3",J*A**3,1),
                                 ("conj(J)*A^3",J.conj()*A**3,0),
                                 ("A^3*C^3",A**3*C**3,1),
                                 ("A^3*conj(C)^3",A**3*C.conj()**3,0),
                                 ("J^2*A^6",J**2*A**6,5)):
        value = np.mean(array)
        phase_tests.append({"word":label,"limiting_exact":expected,
                            "finite_real":float(value.real),"finite_imag":float(value.imag)})
    return {"kind": "floating_joint_field_diagnostic", "q": q, "square_root": root,
            "good_subgroup_frequencies": n-1, "exact_alias_error": error,
            "max_abs_pure_rank_three_good": float(np.max(np.abs(pure[np.r_[good, good]]))),
            "records": records,"oriented_determinant_tests":phase_tests,
            "scope": "finite floating means; convergence theorem is proved separately"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--small-only", action="store_true")
    args = parser.parse_args()
    print(json.dumps(independent_weyl_audit(),sort_keys=True),flush=True)
    for r,t,s in MONOMIALS:
        value = joint_xz(r,s)*y_moment(t)
        print(json.dumps({"kind": "exact_compact_invariant_count", "powers": [r,t,s],
                          "moment": str(value)},sort_keys=True), flush=True)
    assert joint_xz(2,2) == Fraction(1,2)
    assert joint_xz(0,4) == Fraction(3,4)
    assert joint_xz(1,3) == Fraction(1,8)
    assert y_moment(4) == Fraction(5,8)
    fields = [(9413,None), (9409,97)]
    if not args.small_only:
        fields += [(153649,None), (151321,389), (1000033,None)]
    for q,root in fields:
        print(json.dumps(field_row(q,root),sort_keys=True),flush=True)


if __name__ == "__main__":
    main()
