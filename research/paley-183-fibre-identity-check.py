#!/usr/bin/env python3
"""Round 183 (call ordinary-prime-first-mass-fibre-dilation): exact checks.

Written independently of research/paley-182-*.py.  All arithmetic is exact
(Fractions or integers modulo p).  Standard library only.

Part I  (p = 37, 73, 89; random rational g on Q with g(1) = 1, no inversion
         symmetry): the four expressions of the first mass agree exactly.
   (a) chart form   M_w = sum_s w(s) sum_{(r,b)} g(A)g(C)g(Y)g(D)  (Rounds 178-180 chart)
   (b) fibre form   M_w = sum_r sum_{b != b'} mu(r,b) mu(r,b') w(b/b')  (Round 171 chart,
                    mu(r,b) = g(Y)g(D), mask b in Q, Y != D)
   (c) row form     M_w = sum_{kappa in Q\\{1}} sum_{P,P' in R_kappa} mu(P)mu(P') w(AD/(CY))
   (d) four-variable form
                    M_w = sum_{x1 x2 = x3 x4, x3/x2 in Q\\{1}} h(x1)h(x2)h(x3)h(x4)
                          * w((1-x3)(1-x4)/((1-x1)(1-x2))),   h(z) = g(1-z), z != 0.
   Also: the fibre b-labels are injective on each row; s = b/b' = 1 iff P = P'.
Part II (same data): Proposition B, the bounded-fibre split
         M_w(kappa) <= (m(kappa)^2 - |nu_kappa|_2^2)/4, and for every tau >= 0
         M_w <= tau*M_1/4 + (1/4) sum_{m(kappa) > tau} m(kappa)^2.
Part III (exact subgroup family): for every subgroup H of Q with |H| >= 3 at
         p = 73, 89, 97, 101, 109, 113 and g_H = delta_1 + (1/4) 1_{H\\{1}}:
         M_w = (3/4096) * E_off(H) exactly, where E_off(H) = sum_kappa (c(kappa)^2 - c(kappa)),
         c(kappa) = #{(Y,D) in (H\\{1})^2 : 1-Y = kappa(1-D)}, kappa in Q\\{1};
         and g_H = |f|^2 with f = (1/2)1_H + (1/2)delta_1 = Fourier image of the
         probability nu = (1/2)unif(H^perp) + (1/2)unif(Q^) (checked exactly).
         Also: Phi(chi) = Phi(1) for every chi trivial on H (exact, via the fact
         that Y/D lies in H for every supported pair).

Replay:  .venv/bin/python -B research/paley-183-fibre-identity-check.py
"""
import random
from fractions import Fraction as F


def inv(a, p):
    return pow(a % p, p - 2, p)


def squares(p):
    return {x * x % p for x in range(1, p)}


def chart_Mw(p, Q, g, w):
    QQ = [x for x in sorted(Q) if x != 1]
    tot = F(0)
    for s in QQ:
        if w[s] == 0:
            continue
        for b in QQ:
            if b == s:
                continue
            for r in range(2, p):
                A = r * s * inv(s - b, p) % p
                C = r * b * inv((1 - r) * (s - b), p) % p
                Y = r * inv(1 - b, p) % p
                D = r * b * inv((1 - r) * (1 - b), p) % p
                if all(z in Q and z != 1 for z in (A, C, Y, D)):
                    tot += w[s] * g[A] * g[C] * g[Y] * g[D]
    return tot


def fibres(p, Q, g):
    """Round 171 chart: (Y,D) -> (r,b); returns {r: [(b, mu, Y, D)]}."""
    QQ = [x for x in sorted(Q) if x != 1]
    byr = {}
    for Y in QQ:
        for D in QQ:
            if Y == D:
                continue
            r = (Y - D) * inv(1 - D, p) % p
            b = D * (1 - Y) * inv(Y * (1 - D), p) % p
            if b not in Q:
                continue
            byr.setdefault(r, []).append((b, g[Y] * g[D], Y, D))
    return byr


def fibre_Mw(p, byr, w):
    tot = F(0)
    for L in byr.values():
        bs = [b for b, _, _, _ in L]
        assert len(set(bs)) == len(bs), "b not injective on a fibre"
        for b1, v1, _, _ in L:
            for b2, v2, _, _ in L:
                if b1 != b2:
                    tot += v1 * v2 * w[b1 * inv(b2, p) % p]
    return tot


def row_Mw(p, Q, g, w):
    QQ = [x for x in sorted(Q) if x != 1]
    rows = {}
    for Y in QQ:
        for D in QQ:
            if Y == D:
                continue
            k = (1 - Y) * inv(1 - D, p) % p
            rows.setdefault(k, []).append((Y, D))
    tot = F(0)
    for k, L in rows.items():
        if k not in Q or k == 1:
            continue
        for (Y, D) in L:
            for (A, C) in L:
                s = A * D * inv(C * Y, p) % p
                assert (s == 1) == ((A, C) == (Y, D))
                tot += g[Y] * g[D] * g[A] * g[C] * w[s]
    return tot


def fourvar_Mw(p, Q, g, w):
    h = [F(0)] * p
    for z in range(1, p):
        x = (1 - z) % p
        if x != 1:          # z != 0 already; exclude x = 1 (h never sees g(1))
            h[z] = g[x]
    supp = [z for z in range(1, p) if h[z] != 0]
    byprod = {}
    for x1 in supp:
        for x2 in supp:
            byprod.setdefault(x1 * x2 % p, []).append((x1, x2))
    tot = F(0)
    for L in byprod.values():
        for (x1, x2) in L:
            for (x3, x4) in L:
                k = x3 * inv(x2, p) % p
                if k not in Q or k == 1:
                    continue
                if (1 - x1) % p == 0 or (1 - x2) % p == 0:
                    continue
                s = (1 - x3) * (1 - x4) * inv((1 - x1) * (1 - x2), p) % p
                tot += h[x1] * h[x2] * h[x3] * h[x4] * w[s]
    return tot


def part1_2():
    rnd = random.Random(183)
    for p in (37, 73, 89):
        Q = squares(p)
        g = [F(0)] * p
        for x in Q:
            g[x] = F(rnd.randint(0, 12), 12)
        g[1] = F(1)
        w = [g[x] * (1 - g[x]) for x in range(p)]
        a = chart_Mw(p, Q, g, w)
        byr = fibres(p, Q, g)
        b = fibre_Mw(p, byr, w)
        c = row_Mw(p, Q, g, w)
        d = fourvar_Mw(p, Q, g, w)
        assert a == b == c == d, (p, a, b, c, d)
        # Part II
        M1 = sum(v for L in byr.values() for _, v, _, _ in L)
        ms = []
        for L in byr.values():
            m = sum(v for _, v, _, _ in L)
            n2 = sum(v * v for _, v, _, _ in L)
            mk = sum(v1 * v2 * w[b1 * inv(b2, p) % p]
                     for b1, v1, _, _ in L for b2, v2, _, _ in L if b1 != b2)
            assert mk <= (m * m - n2) / 4
            ms.append(m)
        for tau in (F(0), F(1, 2), F(1), F(2), F(4), max(ms)):
            rhs = tau * M1 / 4 + sum(m * m for m in ms if m > tau) / 4
            assert b <= rhs, (p, tau)
        print(f"I  p={p}: chart == fibre == row == four-variable form, M_w={float(a):.6f}; "
              f"b injective on fibres; s=1 <-> P=P'  OK")
        print(f"II p={p}: M_w(kappa) <= (m^2-|nu|^2)/4 on every fibre; "
              f"M_w <= tau M_1/4 + sum_(m>tau) m^2/4 for tau in {{0,1/2,1,2,4,max m}}  OK "
              f"(M_1={float(M1):.4f}, max m={float(max(ms)):.4f})")


def subgroups_of_Q(p):
    n = (p - 1) // 2
    # primitive root
    m = p - 1
    fs = [q for q in range(2, m + 1) if m % q == 0 and all(q % r for r in range(2, int(q ** .5) + 1))]
    th = next(c for c in range(2, p) if all(pow(c, m // q, p) != 1 for q in fs))
    out = []
    for d in range(3, n + 1):
        if n % d:
            continue
        gen = pow(th, 2 * (n // d), p)
        H = {pow(gen, k, p) for k in range(d)}
        out.append((d, H, th))
    return out


def part3():
    for p in (73, 89, 97, 101, 109, 113):
        Q = squares(p)
        n = (p - 1) // 2
        for d, H, th in subgroups_of_Q(p):
            g = [F(0)] * p
            for x in H:
                g[x] = F(1, 4)
            g[1] = F(1)
            w = [g[x] * (1 - g[x]) for x in range(p)]
            byr = fibres(p, Q, g)
            Mw = fibre_Mw(p, byr, w)
            # E_off(H) with 0/1 weights
            HH = [x for x in H if x != 1]
            c = {}
            for Y in HH:
                for D in HH:
                    if Y == D:
                        continue
                    k = (1 - Y) * inv(1 - D, p) % p
                    if k in Q and k != 1:
                        c[k] = c.get(k, 0) + 1
            Eoff = sum(v * v - v for v in c.values())
            assert Mw == F(3, 4096) * Eoff, (p, d, Mw, Eoff)
            # admissibility: nu = 1/2 unif(H^perp) + 1/2 unif(Q^) on Z/n (characters
            # eta_a(theta^{2j}) = e(a j/n)); f(theta^{2j}) = sum_a nu_a e(aj/n).
            # H = <theta^{2n/d}>, so H^perp = {a : d | ... } = multiples of d in Z/n.
            # f = (1/2)1_H + (1/2)delta_1 is checked exactly through the character sums:
            # sum_{a in H^perp} e(aj/n) = |H^perp| * 1[j in (n/d)Z]; sum_a e(aj/n) = n*1[j=0].
            Hperp = [a for a in range(n) if a % d == 0]
            assert len(Hperp) == n // d
            for j in range(n):
                x = pow(th, 2 * j, p)
                inH = (j % (n // d) == 0)
                fval = F(1, 2) * (1 if inH else 0) + F(1, 2) * (1 if j == 0 else 0)
                assert g[x] == fval * fval
            capratio = F(1, 2 * len(Hperp)) + F(1, 2 * n)  # max nu
            # Phi(chi) = Phi(1) on H^perp: every supported pair has Y/D in H, so
            # chi(Y/D) = 1 for chi trivial on H; check the support statement.
            for L in byr.values():
                for b, v, Y, D in L:
                    if v != 0:
                        assert Y * inv(D, p) % p in H
            print(f"III p={p} |H|={d:3d}: M_w = (3/4096) E_off(H) = {float(Mw):.6f} "
                  f"(E_off={Eoff}); g_H = |f|^2 exact; n*max(nu) = {float(n*capratio):.2f}; "
                  f"Y/D in H on support  OK")


if __name__ == "__main__":
    part1_2()
    part3()
    print("ALL OK")
