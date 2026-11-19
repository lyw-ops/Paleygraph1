"""Independent coverage and exact integer audit of the finite vacancy certificate.

Uses only the Python standard library. Its coverage check enumerates primes first
and tests subgroup orders in their window, reversing the scanner's enumeration.
"""
from collections import Counter
from fractions import Fraction
from math import isqrt
from pathlib import Path
import json

PATH = Path(__file__).with_name('parallel-vacancy-24-certified.jsonl')
meta, *rows = [json.loads(line) for line in PATH.read_text().splitlines()]
limit = meta['max_prime']
a, c, den = meta['lo_num'], meta['hi_num'], meta['denominator']
prime = bytearray(b'\x01')*(limit+1)
prime[:2] = b'\x00\x00'
for q in range(2, isqrt(limit)+1):
    if prime[q]:
        prime[q*q::q] = b'\x00'*((limit-q*q)//q+1)
expected = set()
for p in range(5, limit+1, 4):
    if not prime[p]:
        continue
    low = isqrt(a*a*p//(den*den))
    if low*low*den*den < a*a*p:
        low += 1
    high = isqrt(c*c*p//(den*den))
    for b in range(low+(low % 2), high+1, 2):
        if (p-1) % (2*b) == 0:
            expected.add((p,b))
actual = {(r['p'], r['b']) for r in rows}
assert actual == expected and len(actual) == len(rows) == meta['cases']
assert len({p for p,b in actual}) == meta['distinct_primes']
for row in rows:
    p,b,S,V = (row[k] for k in ['p','b','twist_sum','vacancies'])
    assert prime[p] and p % 4 == 1 and (p-1) % (2*b) == 0
    assert S*S+2*V <= p
    assert row['nonsquares'] == (p-1)//2
    assert V == (p-1)//2-row['nonsquare_mass']+row['excess']
    assert row['sigma'] == (-1)**(b//2)
    assert S == row['sigma']*(b-1-2*row['exceptions'])

strata = []
for lower in [0, 1000, 10000, 100000, 500000]:
    subset = [r for r in rows if r['p'] >= lower]
    v = min(subset, key=lambda r: Fraction(r['vacancies'],r['nonsquares']))
    s = max(subset, key=lambda r: Fraction(r['twist_sum']**2,r['p']))
    e = min(subset, key=lambda r: Fraction(r['b']-1-abs(r['twist_sum']),2*r['b']))
    for r in subset:
        assert r['vacancies']*v['nonsquares'] >= v['vacancies']*r['nonsquares']
        assert r['twist_sum']**2*s['p'] <= s['twist_sum']**2*r['p']
        assert (r['b']-1-abs(r['twist_sum']))*e['b'] >= (e['b']-1-abs(e['twist_sum']))*r['b']
    strata.append(dict(lower_prime=lower,cases=len(subset),
                       vacancy_min=[v['vacancies'],v['nonsquares']],
                       vacancy_min_at=[v['p'],v['b']],
                       squared_twist_max=[s['twist_sum']**2,s['p']],
                       squared_twist_max_at=[s['p'],s['b']],
                       best_sign_mismatch_min=[e['b']-1-abs(e['twist_sum']),2*e['b']],
                       best_sign_mismatch_min_at=[e['p'],e['b']]))

# Direct standard-library recomputation at each extremum and all small cases.
selected = {tuple(st[k]) for st in strata for k in ['vacancy_min_at','squared_twist_max_at','best_sign_mismatch_min_at']}
selected.update((r['p'],r['b']) for r in rows if r['p'] <= 5000)
by_case = {(r['p'],r['b']):r for r in rows}
for p,b in sorted(selected):
    row = by_case[p,b]
    B = {x for x in range(1,p) if pow(x,b,p) == 1}
    assert len(B) == b
    Y = {(1-x) % p for x in B-{1}}
    sq = {x*x % p for x in range(1,(p+1)//2)}
    R = Counter(y*pow(z,-1,p) % p for z in Y for y in Y if y != z)
    V = sum(R[u] == 0 for u in range(1,p) if u not in sq)
    S = sum((1 if (1-x) % p in sq else -1)*(1 if pow(x,b//2,p)==1 else -1) for x in B-{1})
    assert V == row['vacancies'] and S == row['twist_sum']
    assert sum(R[u] for u in range(1,p) if u not in sq) == row['nonsquare_mass']

out = dict(coverage='all cases matched independent prime-first enumeration',
           cases=len(rows),distinct_primes=meta['distinct_primes'],
           directly_recomputed_cases=len(selected),strata=strata)
Path(__file__).with_name('parallel-vacancy-24-audit.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
