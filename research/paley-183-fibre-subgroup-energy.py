#!/usr/bin/env python3
"""Round 183 (call ordinary-prime-first-mass-fibre-dilation): exact subgroup class.

Exact integer counts (evidence only for the asymptotic question).  For a
subgroup H of Q (squares mod p, p = 1 mod 4) the admissible weight
g_H = delta_1 + (1/4) 1_{H minus 1} has, by Proposition C of the report,
    M_w(g_H) = (3/4096) * E_off(H),
    E_off(H) = sum_{kappa in Q minus 1} (c(kappa)^2 - c(kappa)),
    c(kappa) = #{(Y,D) in (H minus 1)^2 : 1 - Y = kappa (1 - D)}   (fibre sizes).
Shkredov (arXiv:1504.04522v1, Theorem 6) bounds E_off(H) <= E^x(H-1) << |H|^2 log|H|
only for |H|^2 < p.  This script samples |H| / sqrt(p) in about [0.9, 1.1] (inside or at
the edge) and about [1.8, 2.2] (outside), and prints
    E_off / |H|^2,  E_off / (|H|^2 log|H|),  max_kappa c(kappa)  (largest fibre),
    and 4096 M_w / (3 p) = E_off / p.
Replay:  .venv/bin/python -B research/paley-183-fibre-subgroup-energy.py [maxp]
(default maxp = 4000000; about 1 minute, peak about 1 GB at the largest p).
"""
import math
import sys

import numpy as np


def is_prime(q):
    if q < 2:
        return False
    i = 2
    while i * i <= q:
        if q % i == 0:
            return False
        i += 1
    return True


def divisors(m):
    out = set()
    i = 1
    while i * i <= m:
        if m % i == 0:
            out.add(i)
            out.add(m // i)
        i += 1
    return sorted(out)


def prim_root(p):
    m = p - 1
    fs = [q for q in divisors(m) if q > 1 and is_prime(q)]
    return next(c for c in range(2, p) if all(pow(c, m // q, p) != 1 for q in fs))


def run_one(p, d):
    n = (p - 1) // 2
    th = prim_root(p)
    # powers and logs (exact, int64)
    pw = np.empty(p - 1, dtype=np.int64)
    x = 1
    # vectorised power table in blocks
    blk = 1 << 16
    base = np.empty(blk, dtype=np.int64)
    y = 1
    for k in range(blk):
        base[k] = y
        y = y * th % p
    step = y  # th^blk
    cur = 1
    for st in range(0, p - 1, blk):
        e = min(blk, p - 1 - st)
        pw[st:st + e] = base[:e] * cur % p
        cur = cur * step % p
    lg = np.empty(p, dtype=np.int64)
    lg[pw] = np.arange(p - 1)
    h0 = pw[np.arange(0, p - 1, 2 * (n // d))]       # H = <th^(2n/d)>, |H| = d
    assert len(h0) == d
    H = h0[h0 != 1]
    one_minus = (1 - H) % p
    lgm = lg[one_minus]
    # kappa = (1-Y)/(1-D): log kappa = lg(1-Y) - lg(1-D) mod p-1 ; kappa in Q iff even
    L = (lgm[:, None] - lgm[None, :]) % (p - 1)
    np.fill_diagonal(L, -1)                    # Y != D  (kappa != 1)
    L = L[(L >= 0) & (L % 2 == 0)]
    c = np.bincount(L // 2, minlength=n).astype(np.int64)
    assert c[0] == 0
    Eoff = int((c * c - c).sum())
    return Eoff, int(c.max())


def main():
    maxp = int(sys.argv[1]) if len(sys.argv) > 1 else 4_000_000
    print("    p      |H|  |H|/sqrtp   E_off/|H|^2  E_off/(|H|^2 log|H|)  max fibre  E_off/p (=4096 M_w/(3p))")
    targets = []
    T = 1000
    while T <= maxp:
        targets.append(T)
        T *= 4
    for T in targets:
        for lo, hi in ((0.9, 1.1), (1.8, 2.2)):
            q = T
            while True:
                if q % 4 == 1 and is_prime(q):
                    ds = [d for d in divisors((q - 1) // 2) if lo * math.sqrt(q) <= d <= hi * math.sqrt(q)]
                    if ds:
                        break
                q += 1
            d = ds[0]
            Eoff, mx = run_one(q, d)
            print(f"{q:8d} {d:6d}   {d/math.sqrt(q):6.3f}      {Eoff/d**2:8.4f}        {Eoff/(d*d*math.log(d)):8.4f}"
                  f"         {mx:4d}      {Eoff/q:9.4f}", flush=True)


if __name__ == "__main__":
    main()
