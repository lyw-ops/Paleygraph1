#!/usr/bin/env python3
"""Round 182 independent audit (session/r182-audit): shifted-level-energy report.

Independent of research/paley-182-shifted-energy-*.py (written from the report's
statements, not from those scripts).

Part 1 (exact Fractions): exponent arithmetic of Lemma SE, Proposition 3,
  Proposition 4, criterion (b1) and the trivial-frequency cost, recomputed from
  first principles; also an exact LP-style check that the chosen (eps, delta)
  balance the four terms of Proposition 3 and that no term exceeds 17/46.
Part 2 (exact Fractions, p = 53, 61): Proposition 1 (row-pair reformulation) on a
  prime not used by the report, with an independent chart implementation and
  arbitrary rational g on Q with g(1) = 1 (no inversion symmetry imposed, since
  the report says (H3) is not needed).
Part 3 (exact integers): Lemma SE bookkeeping.  For several B with N <= sqrt p:
  sum_u m(u) = N^2, m(1) = N, the incidence identity
  #{(u,v,x,y)} = sum_u m(u)*|V| equals the number of point-line incidences
  between B x VB and the lines l_{u,v} counted with multiplicity one (injectivity),
  and E^x(1-B) / (K^(2/3) N^(8/3)) is reported (evidence only).
Part 4 (floating, evidence only): Lemma S2 |sum_x g(x) chi(1-x)| <= sqrt p for
  g = |f|^2 from a random probability on the characters of Q, all chi != 1.

Part 5 (exact Fractions, p = 29, 53; blind-overlap identity): with the op-norm
  report's mu(r,b) = g(Y)g(D) on the Round 171 chart (mask b in Q, Y != D),
  M_w = sum_r sum_{b != b'} mu(r,b) mu(r,b') w(b/b')   and   E_Q(h) = sum_r m(r)^2,
  i.e. the direct first mass is the w-weighted intercept-ratio correlation inside the
  slope fibres of the same mu, and E_Q(h) is the slope-energy T_1^x(m) of the op-norm
  trace identity.

Replay: python3 -B research/paley-182-audit-shifted-energy-check.py
Standard library only; small memory.
"""
import cmath
import math
import random
from fractions import Fraction as F


# ---------------------------------------------------------------- Part 1
def part1():
    # Lemma SE: t(h) <= K^(2/3) + C K^2 N^4 / h^4 ; split at H = K^(2/3) N^(2/3)
    # E <= N^2 + H N^2 + sum_dyadic h^2 t(h)  ->  exponents in (K, N):
    terms = {
        "row u=1": (F(0), F(2)),
        "rows m<H: H N^2": (F(2, 3), F(8, 3)),
        "dyadic K^(2/3) h^2 (h<=N)": (F(2, 3), F(2)),
        "dyadic K^2 N^4 / H^2": (F(2) - 2 * F(2, 3), F(4) - 2 * F(2, 3)),
    }
    for k, (a, b) in terms.items():
        assert a <= F(2, 3) and b <= F(8, 3), k
    # SdZ hypothesis translation: a=N, b=KN, n=tN: a b^2 <= n^3 <=> K^2 <= t^3
    # incidence bound a^(3/4) b^(1/2) n^(3/4) = K^(1/2) N^2 t^(3/4)
    assert F(3, 4) + F(1, 2) + F(3, 4) == 2
    # h N t <= 2 C K^(1/2) N^2 t^(3/4)  =>  t^(1/4) <= 2C K^(1/2) N / h => t <= 16 C^4 K^2 N^4/h^4
    print("P1 Lemma SE: E^x(1-B) << K^(2/3) N^(8/3); compare R177 K^(16/13) N^(36/13):",
          F(8, 3) < F(36, 13), F(2, 3) < F(16, 13))

    # BSG piece: |B| >> m K^(-1/2), |B/B| << K^4 |B|; Lemma SE with K_SE = K^4.
    # N(1_{1-B})/|B| << (K^4)^(1/6) |B|^(2/3-1) ; |B|^(-1/3) <= m^(-1/3) K^(1/6)
    a_exp = F(4, 6) + F(1, 6)  # exponent of K_j in the price per point
    assert a_exp == F(5, 6)
    m_exp = -F(1, 3) - a_exp   # after K_j <= Q0/m_j
    assert m_exp == -F(7, 6)
    # Phase 1: (G/t) * Q0^(5/6) * p^(-7/12), Q0 = p^(1/2) t^(-2), G = p^(1/2)
    ph1_p = F(1, 2) + F(5, 6) * F(1, 2) + m_exp * F(1, 2)
    ph1_t = -1 - F(5, 6) * 2
    assert (ph1_p, ph1_t) == (F(1, 3), -F(8, 3))
    # Phase 2: sum_dyadic 2M Q0^(5/6) M^(-7/6) ~ Q0^(5/6) M_min^(-1/6), M_min = p^(1/2-delta)
    # leftover: |S_small|^(3/4) ; light part: (tau G^3)^(1/4)
    def worst(eps, delta):
        e1 = ph1_p + F(5, 3) * eps                     # int_tau^1 t^(-8/3)
        e2 = F(5, 6) * F(1, 2) - F(1, 6) * (F(1, 2) - delta) + F(2, 3) * eps  # int t^(-5/3)
        e3 = F(3, 4) * (F(1, 2) - delta)
        e4 = F(1, 4) * (F(3, 2) - eps)
        return [e1, e2, e3, e4]
    ex = worst(F(1, 46), F(1, 138))
    print("P1 Prop 3 four norm exponents at eps=1/46, delta=1/138:", [str(e) for e in ex])
    assert max(ex) == F(17, 46) and ex[1] == F(289, 828)
    assert 4 * F(17, 46) == F(34, 23) == F(3, 2) - F(1, 46)
    # brute search over a rational grid: no (eps, delta) beats 17/46 for this bookkeeping
    best = min((max(worst(F(i, 2000), F(j, 2000))), i, j)
               for i in range(1, 200) for j in range(1, 200))
    print("P1 grid optimum of the bookkeeping (eps,delta in (0,0.1)):", best[0], float(best[0]),
          ">= 17/46 :", best[0] >= F(17, 46))
    assert best[0] >= F(17, 46)
    # Prop 4: price per point K^a m^(beta/4-1-a)... phase 1 p^(beta/8) t^(-1-2a);
    # balance beta/8 + 2 a eps = 3/8 - eps/4
    for beta, c, label in ((F(8, 3), F(2, 3) * 4 / 4, "SE"), (F(2), F(0), "sharp K-free")):
        pass
    a_sharp = F(0) + (1 - F(2) / 4) / 2
    eps_sharp = (F(3, 8) - F(2) / 8) / (2 * a_sharp + F(1, 4))
    assert a_sharp == F(1, 4) and eps_sharp == F(1, 6)
    # with Lemma SE in this parametrisation: N(1_{1-B}) <= K_SE^(1/6) |B|^(2/3), K_SE=K^4,
    # so c = 2/3, beta/4 = 2/3 -> beta = 8/3 ; a = 2/3 + (1-2/3)/2 = 5/6 ; eps = (3/8-1/3)/(5/3+1/4)
    a_se = F(2, 3) + (1 - F(2, 3)) / 2
    eps_se = (F(3, 8) - F(8, 3) / 8) / (2 * a_se + F(1, 4))
    assert a_se == F(5, 6) and eps_se == F(1, 46)
    print("P1 Prop 4 formula reproduces eps=1/46 (Lemma SE) and eps=1/6 (sharp K-free lemma): OK")
    # trivial frequency: G * E_Q(h) / (p-1) -> 1/2 + 34/23 - 1
    assert F(1, 2) + F(34, 23) - 1 == F(45, 46)
    assert F(34, 23) > F(11, 8) and F(4, 3) < F(11, 8)
    # (b1): Young below p^(-1/2): p^(-1/2) G^3 = p ; layer cake p^(eta/4) p^(1/4) log p
    print("P1 trivial frequency p^(45/46); 34/23 > 11/8 (no M_w gain); cap 4/3 < 11/8: OK")


# ---------------------------------------------------------------- Part 2
def sq(p):
    return {x * x % p for x in range(1, p)}


def inv(a, p):
    return pow(a % p, p - 2, p)


def part2():
    rnd = random.Random(20261120)
    for p in (53, 61):
        Q = sq(p)
        QQ = sorted(Q - {1})
        g = [F(0)] * p
        for x in Q:
            g[x] = F(rnd.randint(0, 12), 12)
        g[1] = F(1)
        w = [g[x] * (1 - g[x]) for x in range(p)]
        # direct chart (Round 178-180 labels, independent implementation)
        Mw = F(0)
        ntup = 0
        for s in QQ:
            for b in QQ:
                if b == s:
                    continue
                isb = inv(s - b, p)
                i1b = inv(1 - b, p)
                for r in range(2, p):
                    i1r = inv(1 - r, p)
                    A = r * s * isb % p
                    C = r * b * i1r * isb % p
                    Y = r * i1b % p
                    D = r * b * i1r * i1b % p
                    if A in Q and C in Q and Y in Q and D in Q and 1 not in (A, C, Y, D):
                        ntup += 1
                        Mw += w[s] * g[A] * g[C] * g[Y] * g[D]
        # rows: kappa in Q\{1}, P=(Y,D) with 1-Y = kappa(1-D), Y,D in Q\{1}
        rows = {}
        for Y in QQ:
            for D in QQ:
                k = (1 - Y) * inv(1 - D, p) % p
                rows.setdefault(k, []).append((Y, D))
        Mrow = F(0)
        nrow = 0
        for k, L in rows.items():
            if k not in Q or k == 1:
                continue
            for (Y, D) in L:
                for (A, C) in L:
                    s = A * D * inv(C * Y, p) % p
                    if s == 1:
                        assert (A, C) == (Y, D)
                        continue
                    nrow += 1
                    Mrow += w[s] * g[A] * g[C] * g[Y] * g[D]
        h = {z: g[(1 - z) % p] for z in range(1, p)}
        Ex = F(0)
        EQ = F(0)
        for k in range(1, p):
            c = sum(h[z] * h[k * z % p] for z in range(1, p))
            Ex += c * c
            if k in Q and k != 1:
                EQ += c * c
        diag = sum((g[Y] * g[D]) ** 2 for k, L in rows.items() if k in Q and k != 1 for (Y, D) in L)
        assert Mw == Mrow, (p, Mw, Mrow)
        assert 4 * Mw <= EQ - diag <= Ex
        print(f"P2 p={p}: chart tuples={ntup} row tuples(s!=1)={nrow}; M_w(chart)==M_w(rows) exactly;"
              f" 4M_w={float(4*Mw):.4f} <= E_Q-diag={float(EQ-diag):.4f} <= E^x(h)={float(Ex):.4f}")
        assert ntup == nrow


# ---------------------------------------------------------------- Part 3
def mrows(B, p):
    m = {}
    Bs = list(B)
    for x in Bs:
        ix = inv(1 - x, p)
        for y in Bs:
            u = (1 - y) * ix % p
            m[u] = m.get(u, 0) + 1
    return m


def part3():
    rnd = random.Random(7)
    for p in (1009, 4001, 16001):
        N = int(math.isqrt(p))
        # generator
        def is_gen(gq):
            n = p - 1
            fs = [q for q in range(2, n + 1) if n % q == 0 and all(q % r for r in range(2, int(q ** .5) + 1))]
            return all(pow(gq, n // q, p) != 1 for q in fs)
        gq = next(c for c in range(2, p) if is_gen(c))
        sets = {}
        sets["logint"] = [pow(gq, k, p) for k in range(5, 5 + N)]
        sets["random"] = rnd.sample(range(2, p), N)
        # subgroup-ish: largest divisor d of p-1 with d <= N
        d = max(dd for dd in range(2, N + 1) if (p - 1) % dd == 0)
        H = [pow(gq, (p - 1) // d * k, p) for k in range(d)]
        sets[f"subgroup d={d} minus 1"] = [x for x in H if x != 1]
        for name, B in sets.items():
            B = [x for x in B if x not in (0, 1)]
            n = len(B)
            m = mrows(B, p)
            assert sum(m.values()) == n * n and m.get(1, 0) == n
            E = sum(v * v for v in m.values())
            Binv = {inv(x, p) for x in B}
            K = len({a * b % p for a in Binv for b in B}) / n
            # incidence injectivity at a small sample of v's
            V = list(Binv)[:5]
            inc = set()
            cnt = 0
            for x in B:
                for y in B:
                    u = (1 - y) * inv(1 - x, p) % p
                    if u == 1:
                        continue
                    for v in V:
                        line = (v * u % p, v * (1 - u) % p)
                        pt = (x, v * y % p)
                        assert (line[0] * pt[0] + line[1]) % p == pt[1]
                        inc.add((line, pt))
                        cnt += 1
            assert len(inc) == cnt
            print(f"P3 p={p} {name:22s} N={n:4d} K={K:7.2f} E/N^2={E/n**2:6.3f} "
                  f"E/(K^(2/3)N^(8/3))={E/(K**(2/3)*n**(8/3)):.4f}")


# ---------------------------------------------------------------- Part 4
def part4():
    rnd = random.Random(99)
    for p in (61, 101, 149):
        n = (p - 1) // 2
        # primitive root
        def is_gen(c):
            m = p - 1
            fs = [q for q in range(2, m + 1) if m % q == 0 and all(q % r for r in range(2, int(q ** .5) + 1))]
            return all(pow(c, m // q, p) != 1 for q in fs)
        gq = next(c for c in range(2, p) if is_gen(c))
        logt = {pow(gq, k, p): k for k in range(p - 1)}
        nu = [rnd.random() ** 3 for _ in range(n)]
        s = sum(nu)
        nu = [v / s for v in nu]
        # f on Q: x = gq^(2j); characters of Q: eta_a(x) = e(a j / n)
        g = [0.0] * p
        for x in range(1, p):
            k = logt[x]
            if k % 2:
                continue
            j = k // 2
            f = sum(nu[a] * cmath.exp(2j * math.pi * a * j / n) for a in range(n))
            g[x] = abs(f) ** 2
        mx = 0.0
        for c in range(1, p - 1):   # chi_c(z) = e(c log z /(p-1)), c != 0
            tot = sum(g[x] * cmath.exp(2j * math.pi * c * logt[(1 - x) % p] / (p - 1))
                      for x in range(2, p) if g[x] > 0)
            mx = max(mx, abs(tot))
        assert mx <= math.sqrt(p) + 1e-9
        print(f"P4 p={p}: g(1)={g[1]:.6f}, max_chi!=1 |sum g(x) chi(1-x)| / sqrt p = {mx/math.sqrt(p):.4f} (<= 1)")


# ---------------------------------------------------------------- Part 5
def part5():
    rnd = random.Random(55)
    for p in (29, 53):
        Q = sq(p)
        QQ = sorted(Q - {1})
        g = [F(0)] * p
        for x in Q:
            g[x] = F(rnd.randint(0, 10), 10)
        g[1] = F(1)
        w = [g[x] * (1 - g[x]) for x in range(p)]
        # M_w by the direct Round 178-180 chart
        Mw = F(0)
        for s_ in QQ:
            for b in QQ:
                if b == s_:
                    continue
                for r in range(2, p):
                    A = r * s_ * inv(s_ - b, p) % p
                    C = r * b * inv((1 - r) * (s_ - b), p) % p
                    Y = r * inv(1 - b, p) % p
                    D = r * b * inv((1 - r) * (1 - b), p) % p
                    if all(z in Q and z != 1 for z in (A, C, Y, D)):
                        Mw += w[s_] * g[A] * g[C] * g[Y] * g[D]
        # op-norm mu on the Round 171 chart
        mu = {}
        for Y in QQ:
            for D in QQ:
                if Y == D:
                    continue
                r = (Y - D) * inv(1 - D, p) % p
                b = D * (1 - Y) * inv(Y * (1 - D), p) % p
                if b not in Q:
                    continue
                mu[(r, b)] = g[Y] * g[D]
        byr = {}
        for (r, b), v in mu.items():
            byr.setdefault(r, []).append((b, v))
        Mw2 = sum(v1 * v2 * w[b1 * inv(b2, p) % p] for L in byr.values()
                  for (b1, v1) in L for (b2, v2) in L if b1 != b2)
        m2 = sum(sum(v for _, v in L) ** 2 for L in byr.values())
        h = {z: g[(1 - z) % p] for z in range(1, p)}
        EQ = sum(sum(h[z] * h[k * z % p] for z in range(1, p)) ** 2 for k in Q if k != 1)
        assert Mw == Mw2 and m2 == EQ
        print(f"P5 p={p}: M_w == sum_r sum_(b!=b') mu(r,b)mu(r,b')w(b/b') and E_Q(h) == sum_r m(r)^2 (exact)")


if __name__ == "__main__":
    part1()
    part2()
    part3()
    part4()
    part5()
    print("ALL AUDIT CHECKS OK")
