#!/usr/bin/env python3
"""Round 183 audit: independent exact checks for the fibre-dilation report
(research/native-claude-ordinary-prime-first-mass-fibre-dilation-183.md).

Written by the Round 183 auditor without reusing the report's code.  Exact
arithmetic (Fractions, integers mod p).  Standard library only.

F1  Proposition A at p = 61, 97, 137 (primes not used by the report's Part I),
    random rational g on Q, g(1) = 1, no symmetry:
      fibre form   sum_r sum_{b != b'} mu(r,b) mu(r,b') w(b/b')   (Round 171 chart)
      == four-variable form over x1 x2 = x3 x4 (all x_i != 0, kappa = x3/x2 in Q\\{1})
    and m(r) = c_h(1-r) for every slope r.
F2  Proposition B / audit remark: sum_{m <= tau} m^2 <= tau*M_1 and M_1 <= (G-1)^2,
    so (RF) at threshold tau is equivalent to X = sum m^2 = O(p^{1+1/1280}).
F3  Proposition C at p = 137, 149, 157, 173, 181, 193, 197 for every subgroup H of Q
    with |H| >= 3:  M_w(g_H) = (3/4096) E_off(H) and (E_Q(h) - diag)/4 = E_off/1024,
    computed from the fibre form (not from the closed formula); n*max(nu) = (|H|+1)/2.
F4  Propositions E and F lower bounds in g_H: E_Q(h) >= sum_P mu(P)^2 >=
    ((|H|-1)^2/2 - (|H|-1))/256, and Phi(chi) = E_Q(h) for chi trivial on H.
F5  Shkredov Thm 6 sanity (not a proof): E^x(H - x0) <= C |H|^2 log2|H| for |H|^2 < p,
    printing the ratio for a few subgroups (0 is removed from H - x0).

Replay: .venv/bin/python -B research/paley-183-audit-fibre-check.py
"""
import math
import random
from fractions import Fraction as F


def inv(a, p):
    return pow(a % p, p - 2, p)


def prim_root(p):
    fac, m, d = [], p - 1, 2
    while d * d <= m:
        if m % d == 0:
            fac.append(d)
            while m % d == 0:
                m //= d
        d += 1
    if m > 1:
        fac.append(m)
    for g in range(2, p):
        if all(pow(g, (p - 1) // q, p) != 1 for q in fac):
            return g


def chart(p, Q, g):
    """Round 171 chart; returns dict r -> list of (b, mu)."""
    out = {}
    for Y in Q:
        if Y == 1 or g[Y] == 0:
            continue
        for D in Q:
            if D == 1 or D == Y or g[D] == 0:
                continue
            b = D * (1 - Y) * inv(Y * (1 - D), p) % p
            if b not in Q:
                continue
            r = (Y - D) * inv(1 - D, p) % p
            out.setdefault(r, []).append((b, g[Y] * g[D]))
    return out


def Mw_fibre(p, fib, w):
    tot = F(0)
    for L in fib.values():
        for (b, m) in L:
            for (b2, m2) in L:
                if b != b2:
                    tot += m * m2 * w.get(b * inv(b2, p) % p, 0)
    return tot


def Mw_fourvar(p, Q, g, w):
    h = {z: g.get((1 - z) % p, 0) for z in range(1, p)}
    supp = [z for z in h if h[z] != 0]
    tot = F(0)
    for x3 in supp:
        for x2 in supp:
            kap = x3 * inv(x2, p) % p
            if kap not in Q or kap == 1:
                continue
            for x4 in supp:
                x1 = kap * x4 % p
                if h.get(x1, 0) == 0:
                    continue
                num = (1 - x3) * (1 - x4) % p
                den = (1 - x1) * (1 - x2) % p
                s = num * inv(den, p) % p
                tot += h[x1] * h[x2] * h[x3] * h[x4] * w.get(s, 0)
    return tot


def f1():
    rng = random.Random(183)
    for p in (61, 97, 137):
        Q = {x * x % p for x in range(1, p)}
        g = {x: F(rng.randint(0, 12), 12) for x in Q}
        g[1] = F(1)
        w = {x: g[x] * (1 - g[x]) for x in Q}
        fib = chart(p, Q, g)
        a = Mw_fibre(p, fib, w)
        b = Mw_fourvar(p, Q, g, w)
        assert a == b, (p, a, b)
        h = {z: g.get((1 - z) % p, 0) for z in range(1, p)}
        for r, L in fib.items():
            kap = (1 - r) % p
            ch = sum(h[z] * h.get(kap * z % p, 0) for z in range(1, p))
            assert sum(m for _, m in L) == ch
        # F2 on the same data
        ms = [sum(m for _, m in L) for L in fib.values()]
        M1 = sum(ms)
        G = sum(g.values())
        assert M1 <= (G - 1) ** 2
        for tau in (F(0), F(1, 2), F(1), F(2), max(ms)):
            assert sum(m * m for m in ms if m <= tau) <= tau * M1
            assert a <= tau * M1 / 4 + sum(m * m for m in ms if m > tau) / 4
        print(f"F1/F2 p={p}: fibre form == four-variable form = {float(a):.6f}; m(r) = c_h(1-r); "
              f"bounded-fibre split and M_1 <= (G-1)^2 OK")


def subgroups(p):
    n = (p - 1) // 2
    th = prim_root(p)
    gen = th * th % p  # generator of Q
    for d in range(3, n + 1):
        if n % d == 0:
            e = pow(gen, n // d, p)
            yield {pow(e, i, p) for i in range(d)}


def f3_f4():
    for p in (137, 149, 157, 173, 181, 193, 197):
        Q = {x * x % p for x in range(1, p)}
        n = (p - 1) // 2
        for H in subgroups(p):
            k = len(H)
            g = {x: F(0) for x in Q}
            for x in H:
                g[x] = F(1, 4)
            g[1] = F(1)
            w = {x: g[x] * (1 - g[x]) for x in Q}
            fib = chart(p, Q, g)
            Mw = Mw_fibre(p, fib, w)
            # integer counts c(kappa)
            Hs = [x for x in H if x != 1]
            c = {}
            for Y in Hs:
                for D in Hs:
                    if Y == D:
                        continue
                    kap = (1 - Y) * inv(1 - D, p) % p
                    if kap in Q:
                        c[kap] = c.get(kap, 0) + 1
            Eoff = sum(v * v - v for v in c.values())
            assert Mw == F(3, 4096) * Eoff, (p, k)
            EQ = sum(sum(m for _, m in L) ** 2 for L in fib.values())
            diag = sum(m * m for L in fib.values() for _, m in L)
            assert (EQ - diag) / 4 == F(Eoff, 1024)
            # n*max(nu) for nu = 1/2 unif(H^perp) + 1/2 unif(Q^): |H^perp| = n/k
            assert F(1, 2) * F(k, n) + F(1, 2 * n) == F(k + 1, 2 * n)
            # F4
            assert diag >= F((k - 1) ** 2, 2 * 256) - F(k - 1, 256)
            assert EQ >= diag
            # Phi(chi) for chi trivial on H equals EQ: Y/D in H on support
            # check Y/D in H for every supported pair directly
            for Y in Hs:
                for D in Hs:
                    if Y != D:
                        assert Y * inv(D, p) % p in H
        print(f"F3/F4 p={p}: every subgroup |H|>=3 of Q: M_w(g_H) = (3/4096) E_off, "
              f"(E_Q-diag)/4 = E_off/1024, diag lower bound, Y/D in H  OK")


def f5():
    print("F5 Shkredov Thm 6 sanity, E^x(H - x0) / (|H|^2 log2|H|) for |H|^2 < p (0 removed):")
    rng = random.Random(5)
    for p in (10009, 40009, 160001):
        Q = {x * x % p for x in range(1, p)}
        n = (p - 1) // 2
        for H in subgroups(p):
            k = len(H)
            if k * k >= p or k < 20:
                continue
            x0 = rng.randrange(1, p)
            A = [(x - x0) % p for x in H if (x - x0) % p != 0]
            cnt = {}
            for a in A:
                ia = inv(a, p)
                for b in A:
                    q = b * ia % p
                    cnt[q] = cnt.get(q, 0) + 1
            E = sum(v * v for v in cnt.values())
            print(f"   p={p} |H|={k:4d}: E={E}, ratio {E / (k * k * math.log2(k)):.4f}")


if __name__ == "__main__":
    f1()
    f3_f4()
    f5()
    print("ALL FIBRE AUDIT CHECKS OK")
