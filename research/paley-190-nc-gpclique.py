#!/usr/bin/env python3
r"""Round 190, call ordinary-nc-excludes-sector-laws: geometric-progression Paley cliques.

Exact integer computation (numpy int64), evidence only.

For a prime p = 1 mod 4 and zeta in Q \ {1}, let R(zeta) be the largest R such that
chi(1 - zeta^k) is the same nonzero value for every k = 1..R (the run stops at the first
k with chi(1 - zeta^k) different or zeta^k = 1). By Lemma 2 of the report, a symmetric
geometric progression I = {zeta^k : |k| <= K} with I.I^{-1} \ {1} inside one sector T_rho
exists iff R(zeta) >= 2K, and then I (or a nonsquare multiple) is a clique of the Paley
graph of size 2K+1. Under (NC) every Round 189 interval-type law (g >= tau on I.I^{-1},
tau fixed) needs such an I with |I| of order sqrt p (Theorem 1 of the report).

Printed per prime: max R over zeta generating Q (ratio gamma^2, gamma a primitive root:
the Round 189 interval family), max R over all zeta in Q \ {1} (the run is capped by
ord(zeta) - 1, so a subgroup clique gives R = ord - 1), the ratio of each to sqrt p,
log2 p, and the Hanson-Petridis clique bound (sqrt(2p-1)+1)/2.

Usage: .venv/bin/python -B research/paley-190-nc-gpclique.py LO HI [STEP]
         (all primes p = 1 mod 4 in [LO, HI], or every STEP-th such prime)
       .venv/bin/python -B research/paley-190-nc-gpclique.py --list P1 P2 ...
"""
import sys
import math
import numpy as np


def primes_1mod4(lo, hi):
    sieve = np.ones(hi + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(hi ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = False
    return [int(q) for q in np.nonzero(sieve)[0] if q >= lo and q % 4 == 1]


def prim_root(p):
    fac, m, q = [], p - 1, 2
    while q * q <= m:
        if m % q == 0:
            fac.append(q)
            while m % q == 0:
                m //= q
        q += 1
    if m > 1:
        fac.append(m)
    for g in range(2, p):
        if all(pow(g, (p - 1) // q, p) != 1 for q in fac):
            return g
    raise ValueError


def runs(p):
    n = (p - 1) // 2
    gam = prim_root(p)
    g2 = gam * gam % p
    # zeta_k = gamma^{2k}, k = 1..n-1 ; generator of Q iff gcd(k, n) = 1
    zeta = np.empty(n, dtype=np.int64)
    x = 1
    for k in range(n):
        zeta[k] = x
        x = x * g2 % p
    zeta = zeta[1:]
    ks = np.arange(1, n)
    sq = np.zeros(p, dtype=np.int8)
    sq[(np.arange(1, p, dtype=np.int64) ** 2) % p] = 1
    chi = np.where(sq == 1, 1, -1).astype(np.int8)
    chi[0] = 0
    sign = chi[(1 - zeta) % p]
    R = np.zeros(len(zeta), dtype=np.int64)
    alive = np.ones(len(zeta), dtype=bool)
    cur = zeta.copy()
    step = 0
    while alive.any():
        step += 1
        ok = alive & (chi[(1 - cur) % p] == sign)
        R[ok] = step
        alive = ok
        cur = np.where(alive, cur * zeta % p, cur)
    gen = np.gcd(ks, n) == 1
    return R[gen].max(), R.max(), int(ks[np.argmax(R)])


def brute(p):
    """Pure-Python R(zeta) for every zeta in Q minus {1}; returns (max over generators, max)."""
    n = (p - 1) // 2
    gam = prim_root(p)
    leg = lambda a: 0 if a % p == 0 else (1 if pow(a, n, p) == 1 else -1)
    best_g = best = 0
    for k in range(1, n):
        z = pow(gam, 2 * k, p)
        s0 = leg(1 - z)
        R, w = 0, z
        while leg(1 - w) == s0 and s0 != 0:
            R += 1
            w = w * z % p
        best = max(best, R)
        if math.gcd(k, n) == 1:
            best_g = max(best_g, R)
        # clique check: I = {z^j : 0 <= j <= R//1} has all differences in one class
        if R >= 2:
            pts = [pow(z, j, p) for j in range(R + 1)]
            cls = {leg(a - b) for a in pts for b in pts if a != b}
            assert cls == {s0} or cls == {s0 * leg(-1)}, (p, k, cls)
    return best_g, best


def main(argv):
    if argv and argv[0] == "--check":
        for p in primes_1mod4(5, 400):
            rg, ra, _ = runs(p)
            assert (rg, ra) == brute(p), p
        print("brute-force runs and clique property agree for all p = 1 mod 4 below 400: OK")
        return
    if argv and argv[0] == "--list":
        ps = [int(a) for a in argv[1:]]
    else:
        lo, hi = int(argv[0]), int(argv[1])
        st = int(argv[2]) if len(argv) > 2 else 1
        ps = primes_1mod4(lo, hi)[::st]
    worst_gen = 0.0
    worst_all = 0.0
    for p in ps:
        rg, ra, karg = runs(p)
        hp = (math.sqrt(2 * p - 1) + 1) / 2
        worst_gen = max(worst_gen, rg / math.sqrt(p))
        worst_all = max(worst_all, ra / math.sqrt(p))
        print(f"p={p} maxR(generators)={rg} ({rg/math.sqrt(p):.4f} sqrt p) "
              f"maxR(all)={ra} ({ra/math.sqrt(p):.4f} sqrt p, zeta=gamma^(2*{karg})) "
              f"log2 p={math.log2(p):.1f} HP bound={hp:.1f}")
    print(f"max over primes: maxR(gen)/sqrt p = {worst_gen:.4f}, maxR(all)/sqrt p = {worst_all:.4f}")


if __name__ == "__main__":
    main(sys.argv[1:])
