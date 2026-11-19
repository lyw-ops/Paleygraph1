"""Exact arithmetic checks of the order-five quartic and reflection tests."""
import json
import io
from contextlib import redirect_stdout
import runpy
from math import gcd, isqrt
from pathlib import Path

with redirect_stdout(io.StringIO()):
    prior = runpy.run_path(str(Path(__file__).with_name("astra-coset-48-check.py")))
primes = prior["sieve"](200000)
primitive_root = prior["primitive_root"]
chi = prior["chi"]
records = {}
hits = 0
reflections = 0
for p in range(41, len(primes), 20):
    if not primes[p]:
        continue
    n = (p - 1) // 2
    g = primitive_root(p)
    for b in range(3, isqrt(n) + 1, 2):
        if n % (5 * b):
            continue
        q = (p - 1) // 4
        divisors = [r for r in range(3, b + 1, 2) if b % r == 0]
        allowed = [s for s in (-1, 1) if all(
            pow(r, q, p) == pow((-1)**q * s, (r-1)//2, p) for r in divisors)]
        if (gcd(b, 30) == 1 and not allowed and 5*b*b > n
                and 10000*b*b < 2167*n and "quartic_exclusion" not in records):
            records["quartic_exclusion"] = dict(p=p, b=b, quartics=[pow(r,q,p) for r in divisors])
        if (gcd(b, 30) == 1 and allowed and any(r % 5 in (2, 3) for r in divisors)
                and pow(5,q,p) == p-1 and 5*b*b > n and 10000*b*b < 2167*n):
            records.setdefault("quintic_fiber_exclusion", dict(p=p, b=b, allowed_signs=allowed))
        h = pow(g, (p-1)//b, p)
        B = [pow(h, i, p) for i in range(b)]
        s = chi(1-h, p)
        if any(chi(1-v,p) != s for v in B[1:]):
            continue
        assert s in allowed
        for k in (1, 2):
            a = pow(g, k*((p-1)//(5*b)), p)
            if any(chi(1-a*v,p) != s for v in B):
                continue
            hits += 1
            neg = sum(chi(1-a*a*v, p) == -s for v in B)
            assert pow(5, q, p) == ((-1)**neg) % p
            if pow(5,q,p) == p-1:
                assert b % 5 and all(r % 5 in (1,4) for r in divisors)
            if b % 5:
                reflections += 1
                root = pow(a,b*pow(b,-1,5),p)
                d = {v: s*chi(1-root*root*v, p) for v in B}
                assert all(d[v] == d[pow(v,-1,p)] == s*chi(1-pow(root,-2,p)*v,p) for v in B)
                if len(set(d.values())) == 2 and gcd(b,6) == 1:
                    records.setdefault("mixed",dict(p=p,b=b,sigma=s,mismatches=neg))
print(json.dumps(dict(patterns=hits, reflected_patterns=reflections, prime_limit=200000, **records),sort_keys=True))
