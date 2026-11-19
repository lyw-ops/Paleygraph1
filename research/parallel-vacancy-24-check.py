"""Exact nonsquare vacancies for every critical even subgroup in a finite range.

Run with ../.venv/bin/python from research, or .venv/bin/python from repo root.
NumPy performs only bounded int64 modular arithmetic. All reported bounds use
integers. No FFT, sampling, or probabilistic primality test is used.
"""
from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import json
from math import isqrt
from pathlib import Path
import time
import numpy as np


def sieve_spf(limit):
    spf = np.arange(limit + 1, dtype=np.int64)
    for q in range(2, isqrt(limit) + 1):
        if spf[q] == q:
            sl = spf[q*q::q]
            sl[sl == np.arange(q*q, limit+1, q, dtype=np.int64)] = q
    return spf


def factor(n, spf):
    out = []
    while n > 1:
        q = int(spf[n])
        out.append(q)
        while n % q == 0:
            n //= q
    return out


def primitive_root(p, spf):
    factors = factor(p-1, spf)
    g = 2
    while any(pow(g, (p-1)//q, p) == 1 for q in factors):
        g += 1
    return g


def subgroup(p, b, g):
    h = pow(g, (p-1)//b, p)
    B = [1]
    for _ in range(1, b):
        B.append(B[-1]*h % p)
    assert len(set(B)) == b and B[-1]*h % p == 1
    return B


def nonsquare_cells_identity(p, B, squares):
    """Independently enumerate cyclotomic cells and their signed label sum."""
    b = len(B)
    d = {x: (-1)**j for j, x in enumerate(B)}
    cosets = {}
    for x in range(1, p):
        if x not in cosets:
            cosets.update({x*y % p: (x, d[y]) for y in B})
    cells = {}
    for a in range(1, p):
        beta = (1-a) % p
        if beta and bool(squares[a]) != bool(squares[beta]):
            ca, da = cosets[a]
            cb, db = cosets[beta]
            oldn, oldl = cells.get((ca, cb), (0, 0))
            cells[ca, cb] = oldn+1, oldl+da*db
    return cells


def check_case(p, b, g, *, independent=False):
    B = subgroup(p, b, g)
    Y = np.array([(1-x) % p for x in B[1:]], dtype=np.int64)
    invY = np.array([pow(int(y), -1, p) for y in Y], dtype=np.int64)
    R = np.zeros(p, dtype=np.int64)
    # Bound temporary memory even for larger explicit runs.
    for start in range(0, len(Y), 128):
        products = (Y[start:start+128, None]*invY[None, :]) % p
        R += np.bincount(products.ravel(), minlength=p)
    assert int(R[1]) == b-1 and int(R.sum()) == (b-1)**2
    assert np.array_equal(R[2:], R[(1-np.arange(2, p)) % p])
    R[1] = 0
    residues = np.arange(1, (p+1)//2, dtype=np.int64)
    squares = np.zeros(p, dtype=bool)
    squares[(residues*residues) % p] = True
    ns = ~squares
    ns[0] = False
    assert int(ns.sum()) == (p-1)//2
    V = int(np.count_nonzero((R == 0) & ns))
    a = int(squares[Y].sum())
    mass = int(R[ns].sum())
    assert mass == 2*a*(b-1-a)
    excess = int(np.maximum(R[ns]-1, 0).sum())
    assert V == (p-1)//2 - mass + excess
    sigma = (-1)**(b//2)
    signs = np.where(squares[Y], 1, -1)
    d = np.array([(-1)**j for j in range(1, b)], dtype=np.int64)
    S = int((signs*d).sum())
    rplus = int(np.count_nonzero((signs != sigma*d) & (d == 1)))
    rminus = int(np.count_nonzero((signs != sigma*d) & (d == -1)))
    r = rplus+rminus
    assert S == sigma*(b-1-2*r)
    assert S*S+2*V <= p
    assert 2*V <= p-(b-1)**2+4*r*(b-1-r)
    goodplus, goodminus = b//2-1-rplus, b//2-rminus
    same_labels = 2*(rplus*goodplus+rminus*goodminus)
    assert excess <= 2*same_labels
    if independent:
        slow = Counter((1-x)*pow(1-y, -1, p) % p
                       for x in B[1:] for y in B[1:] if x != y)
        assert all(int(R[u]) == slow[u] for u in range(p))
        cells = nonsquare_cells_identity(p, B, squares)
        assert sum(L*L for N, L in cells.values()) == (p-S*S)//2
        assert sum(N == 1 for N, L in cells.values()) == V
        assert sum((N*N+L*L)//2-N for N, L in cells.values()) == same_labels
    return dict(p=p, b=b, cofactor=(p-1)//b, vacancies=V,
                nonsquares=(p-1)//2, nonsquare_mass=mass, excess=excess,
                twist_sum=S, sigma=sigma, exceptions=r,
                exceptions_dplus=rplus, exceptions_dminus=rminus,
                spectral_slack=p-S*S-2*V,
                histogram_sha256=hashlib.sha256(R.astype('<i8').tobytes()).hexdigest())


def enumerate_cases(limit, lo_num, hi_num, denominator, spf):
    """Integer comparisons lo_num/denominator <= b/sqrt(p) <= hi_num/denominator."""
    maxb = isqrt(limit*hi_num*hi_num)//denominator+2
    cases = []
    for b in range(2, maxb+1, 2):
        # p=b*k+1; B lies in squares exactly when k is even.
        pmin = max(5, (b*b*denominator**2+hi_num**2-1)//hi_num**2)
        pmax = min(limit, b*b*denominator**2//lo_num**2)
        for k in range(max(2, (pmin-1+b-1)//b), (pmax-1)//b+1):
            if k % 2:
                continue
            p = b*k+1
            if int(spf[p]) == p:
                assert p % 4 == 1
                assert lo_num**2*p <= b*b*denominator**2 <= hi_num**2*p
                cases.append((p, b))
    return sorted(cases)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--max-prime', type=int, default=1_000_000)
    parser.add_argument('--lo-num', type=int, default=19)
    parser.add_argument('--hi-num', type=int, default=21)
    parser.add_argument('--denominator', type=int, default=20)
    parser.add_argument('--output', type=Path, default=Path(__file__).with_name('parallel-vacancy-24-certified.jsonl'))
    args = parser.parse_args()
    assert 5 <= args.max_prime < 1_000_000_000
    assert 0 < args.lo_num <= args.hi_num
    started = time.monotonic()
    spf = sieve_spf(args.max_prime)
    cases = enumerate_cases(args.max_prime, args.lo_num, args.hi_num, args.denominator, spf)
    rows = []
    roots = {}
    for p, b in cases:
        if p not in roots:
            roots[p] = primitive_root(p, spf)
        rows.append(check_case(p, b, roots[p], independent=p <= 5000))
        if len(rows) % 100 == 0:
            print(f'{len(rows)}/{len(cases)} cases; {time.monotonic()-started:.1f}s', flush=True)
    weakest = min(rows, key=lambda r: r['vacancies']/r['nonsquares'])
    strongest = max(rows, key=lambda r: abs(r['twist_sum'])/(r['p']**0.5))
    # Prove the summary minima by exact cross-multiplication.
    assert all(r['vacancies']*weakest['nonsquares'] >= weakest['vacancies']*r['nonsquares'] for r in rows)
    assert all(r['twist_sum']**2*strongest['p'] <= strongest['twist_sum']**2*r['p'] for r in rows)
    meta = dict(kind='exhaustive_exact_range', max_prime=args.max_prime,
                lo_num=args.lo_num, hi_num=args.hi_num, denominator=args.denominator,
                cases=len(rows), distinct_primes=len(roots),
                minimum_vacancy_fraction_case=weakest,
                maximum_squared_normalized_twist_case=strongest,
                elapsed_seconds=round(time.monotonic()-started, 3))
    with args.output.open('w') as f:
        for row in [meta]+rows:
            f.write(json.dumps(row, sort_keys=True)+'\n')
    print(json.dumps(meta, indent=2), flush=True)


if __name__ == '__main__':
    main()
