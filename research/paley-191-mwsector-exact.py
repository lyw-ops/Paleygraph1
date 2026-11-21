#!/usr/bin/env python3
r"""Round 191, call ordinary-first-mass-sector-obstruction: exact checks.

Written for research/native-claude-ordinary-first-mass-sector-obstruction-191.md.
Exact Fractions / integers modulo p, except Part IV, which is a labelled floating check
of trigonometric facts about the Fejer kernel and of the mixture-law formula.

Part I   Identity replay (Round 183 Prop. A, w kept), random rational g on Q, g(1)=1,
         no symmetry, p = 41, 61, 101:
            fibre form  sum_r sum_{b != b'} mu(r,b) mu(r,b') w(b/b')  (Round 171 chart)
         == row form    sum_{kappa in Q\1} sum_{P,P' in R_kappa} mu(P)mu(P') w(AD/(CY))
         == 4-variable  sum_{x1x2=x3x4, x3/x2 in Q\1} h h h h w((1-x3)(1-x4)/((1-x1)(1-x2)))
         == log-correlation form used by the models script (cyclic correlation of
            nu_kappa on Z/n = log_zeta Q, weighted by w).
Part II  Restriction lemma (Lemma 1 of the report), exact: for g with g >= tau' on I'\1 and
         w >= tau'' on Sigma(I')\1, Sigma(I') = I'I'I'^-1 I'^-1,
            M_w(g) >= M_w|_{I'} >= tau'^4 tau'' X_off(1_I'),
         X_off(1_I') = sum_{kappa in Q\1} (c(kappa)^2 - c(kappa)),
         c(kappa) = #{(Y,D) in (I'\1)^2 : 1-Y = kappa(1-D)}.
         g is a random rational law with a "mixture plateau" on the window
         {zeta^k : 1 <= |k| <= 4K'} and arbitrary values elsewhere.
Part III Subgroup laws (exact): g = 1_H gives w == 0, so M_w(1_H) = 0 while X(1_H) > 0
         (w can remove a whole sector-type piece for one law); the 1/2-mixture
         g_H = delta_1 + (1/4)1_{H\1} (Round 183 Prop. C) gives
         M_w = (3/4096) E_off(H) = (1/4)^4 (3/16) X_off(1_H): Lemma 1 is sharp there.
Part IV  (floating, labelled) Fejer kernel F_L(j) = (sin(pi L j/n)/(L sin(pi j/n)))^2:
         F_L >= 4/pi^2 and
         (4/3)(L^2-1)(j/n)^2 <= 1 - F_L(j) <= (pi^2/3)(L^2-1)(j/n)^2  for 1 <= |j| <= n/(2L);
         the eta-mixture law nu = (1-eta) 1_J/L + eta unif(Q^) has g = delta_1 + (1-eta)^2 F_L
         off 1, computed from nu by character sums.
Part V   Masked -> unmasked step of the Round 189 audit, exact integers:
         E^x(I'-1) <= 16 (X(1_I') + |I'|^2) for symmetric GPs I' at several p.

Replay:  .venv/bin/python -B research/paley-191-mwsector-exact.py      (prints ALL EXACT CHECKS OK)
"""
import cmath
import math
import random
from fractions import Fraction as F


def inv(a, p):
    return pow(a % p, p - 2, p)


def prim_root(p):
    m, fac, q = p - 1, [], 2
    mm = m
    while q * q <= mm:
        if mm % q == 0:
            fac.append(q)
            while mm % q == 0:
                mm //= q
        q += 1
    if mm > 1:
        fac.append(mm)
    return next(c for c in range(2, p) if all(pow(c, m // r, p) != 1 for r in fac))


def setup(p):
    n = (p - 1) // 2
    gam = prim_root(p)
    zeta = gam * gam % p
    log = [-1] * p
    x = 1
    for k in range(n):
        log[x] = k
        x = x * zeta % p
    Q = {x for x in range(1, p) if log[x] >= 0}
    return n, zeta, log, Q


# ---------------------------------------------------------------- the four forms of M_w
def fibre_Mw(p, Q, g, w):
    QQ = [x for x in sorted(Q) if x != 1]
    byr = {}
    for Y in QQ:
        for D in QQ:
            if Y == D:
                continue
            r = (Y - D) * inv(1 - D, p) % p
            b = D * (1 - Y) * inv(Y * (1 - D), p) % p
            if b in Q:
                byr.setdefault(r, []).append((b, g[Y] * g[D]))
    tot = F(0)
    for L in byr.values():
        assert len({b for b, _ in L}) == len(L)
        for b1, v1 in L:
            for b2, v2 in L:
                if b1 != b2:
                    tot += v1 * v2 * w[b1 * inv(b2, p) % p]
    return tot


def rows(p, Q, labels):
    """kappa -> list of (Y,D), Y,D in labels (subset of Q\\1), Y != D, kappa in Q\\1."""
    out = {}
    for Y in labels:
        for D in labels:
            if Y == D:
                continue
            k = (1 - Y) * inv(1 - D, p) % p
            if k in Q and k != 1:
                out.setdefault(k, []).append((Y, D))
    return out


def row_Mw(p, Q, g, w, labels=None):
    if labels is None:
        labels = [x for x in sorted(Q) if x != 1]
    tot = F(0)
    for L in rows(p, Q, labels).values():
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
        if x != 1:
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
                if k not in Q or k == 1 or (1 - x1) % p == 0 or (1 - x2) % p == 0:
                    continue
                s = (1 - x3) * (1 - x4) * inv((1 - x1) * (1 - x2), p) % p
                tot += h[x1] * h[x2] * h[x3] * h[x4] * w[s]
    return tot


def logcorr_Mw(p, n, log, Q, g, w):
    """The indexing used by paley-191-mwsector-models.py, in exact arithmetic."""
    wl = [F(0)] * n
    for x in Q:
        wl[log[x]] = w[x]
    tot = F(0)
    for kap in Q:
        if kap == 1:
            continue
        nu = {}
        for D in Q:
            if D == 1:
                continue
            Y = (1 - kap * (1 - D)) % p
            if Y == 0 or log[Y] < 0 or Y == 1:
                continue
            u = (log[kap] + log[D] - log[Y]) % n
            nu[u] = nu.get(u, F(0)) + g[Y] * g[D]
        items = list(nu.items())
        for u, a in items:
            for v, b in items:
                tot += a * b * wl[(u - v) % n]
    return tot


def X_off_labels(p, Q, labels):
    """X_off(1_I') = sum_kappa (c^2 - c) and X(1_I') = sum_kappa c^2, labels = I'\\1."""
    R = rows(p, Q, labels)
    X = sum(len(L) ** 2 for L in R.values())
    diag = sum(len(L) for L in R.values())
    return X - diag, X


# ---------------------------------------------------------------- Part I
def part1():
    rnd = random.Random(191)
    for p in (41, 61, 101):
        n, zeta, log, Q = setup(p)
        g = [F(0)] * p
        for x in Q:
            g[x] = F(rnd.randint(0, 12), 12)
        g[1] = F(1)
        w = [gx * (1 - gx) for gx in g]
        a = fibre_Mw(p, Q, g, w)
        b = row_Mw(p, Q, g, w)
        c = fourvar_Mw(p, Q, g, w)
        d = logcorr_Mw(p, n, log, Q, g, w)
        assert a == b == c == d, (p, a, b, c, d)
        print(f"I   p={p}: fibre == row == four-variable == log-correlation form, "
              f"M_w = {float(a):.6f}  OK")


# ---------------------------------------------------------------- Part II
def part2():
    rnd = random.Random(1912)
    for p, L in ((101, 2), (197, 3), (197, 2), (229, 2)):
        n, zeta, log, Q = setup(p)
        K = n // (8 * L)
        assert K >= 1 and 4 * K <= n / (2 * L)
        win = {pow(zeta, k % n, p) for k in range(-4 * K, 4 * K + 1)} - {1}
        Ip = [pow(zeta, k % n, p) for k in range(-K, K + 1)]
        Ip_l = sorted(set(Ip) - {1})
        Sigma = {A * D * inv(C * Y, p) % p for A in Ip for D in Ip for C in Ip for Y in Ip}
        assert Sigma - {1} <= win
        g = [F(0)] * p
        for x in Q:
            if x in win:
                g[x] = F(rnd.randint(10, 25), 100)        # plateau in [1/10, 1/4]
            else:
                g[x] = F(rnd.randint(0, 20), 20)          # arbitrary in [0, 1]
        g[1] = F(1)
        w = [gx * (1 - gx) for gx in g]
        Mw = row_Mw(p, Q, g, w)
        Mw_I = row_Mw(p, Q, g, w, labels=Ip_l)
        t1 = min(g[x] for x in Ip_l)
        t2 = min(w[s] for s in Sigma if s != 1)
        Xoff, X = X_off_labels(p, Q, Ip_l)
        lb = t1 ** 4 * t2 * Xoff
        assert Mw >= Mw_I >= lb, (p, Mw, Mw_I, lb)
        print(f"II  p={p} L={L} K'={K} |I'|={len(Ip)}: M_w={float(Mw):.4f} >= M_w|I'={float(Mw_I):.5f} "
              f">= tau'^4 tau'' X_off = {float(lb):.3e} (X_off(1_I')={Xoff}, X={X})  OK")


# ---------------------------------------------------------------- Part III
def part3():
    for p in (101, 109, 113):
        n, zeta, log, Q = setup(p)
        for d in [d for d in range(3, n + 1) if n % d == 0]:
            h0 = pow(zeta, n // d, p)
            H = {pow(h0, k, p) for k in range(d)}
            Hl = sorted(H - {1})
            # pure subgroup law g = 1_H: w == 0
            g = [F(1) if x in H else F(0) for x in range(p)]
            w = [gx * (1 - gx) for gx in g]
            assert all(v == 0 for v in w)
            Xoff, X = X_off_labels(p, Q, Hl)
            # 1/2-mixture g_H = delta_1 + (1/4) 1_{H\1}
            g2 = [F(0)] * p
            for x in Hl:
                g2[x] = F(1, 4)
            g2[1] = F(1)
            w2 = [gx * (1 - gx) for gx in g2]
            Mw2 = row_Mw(p, Q, g2, w2)
            assert Mw2 == F(3, 4096) * Xoff == F(1, 4) ** 4 * F(3, 16) * Xoff
            print(f"III p={p} |H|={d}: M_w(1_H) = 0 (w == 0) while X(1_H) = {X}; "
                  f"M_w(g_H) = (3/4096) X_off(1_H) = {float(Mw2):.5f} = Lemma-1 bound (sharp)  OK")


# ---------------------------------------------------------------- Part IV (floating)
def fejer(L, j, n):
    if j % n == 0:
        return 1.0
    return (math.sin(math.pi * L * j / n) / (L * math.sin(math.pi * j / n))) ** 2


def part4():
    worst_lo, worst_hi = 1e9, 1e9
    for n in (50, 98, 500, 1004, 5004):
        for L in range(2, 40):
            if n // (2 * L) < 1:
                continue
            for j in range(1, n // (2 * L) + 1):
                Fj = fejer(L, j, n)
                assert Fj >= 4 / math.pi ** 2 - 1e-12
                lo = 4 / 3 * (L * L - 1) * (j / n) ** 2
                hi = math.pi ** 2 / 3 * (L * L - 1) * (j / n) ** 2
                assert lo - 1e-12 <= 1 - Fj <= hi + 1e-12, (n, L, j)
                worst_lo = min(worst_lo, (1 - Fj) - lo)
                worst_hi = min(worst_hi, hi - (1 - Fj))
    print(f"IV  (floating) F_L >= 4/pi^2 and (4/3)(L^2-1)(j/n)^2 <= 1-F_L <= (pi^2/3)(L^2-1)(j/n)^2 "
          f"for 1<=|j|<=n/(2L): min slacks {worst_lo:.2e}, {worst_hi:.2e}  OK")
    # mixture law from nu by character sums
    for p, L, eta, a0 in ((101, 3, 0.5, 7), (197, 4, 0.3, 0), (229, 5, 0.75, 40)):
        n, zeta, log, Q = setup(p)
        nu = [eta / n] * n
        for j in range(a0, a0 + L):
            nu[j % n] += (1 - eta) / L
        assert abs(sum(nu) - 1) < 1e-12
        err = 0.0
        for k in range(n):
            f = sum(nu[j] * cmath.exp(2j * math.pi * j * k / n) for j in range(n))
            gk = abs(f) ** 2
            want = 1.0 if k == 0 else (1 - eta) ** 2 * fejer(L, k, n)
            err = max(err, abs(gk - want))
        assert err < 1e-10
        print(f"IV  (floating) p={p} L={L} eta={eta}: g of nu=(1-eta)1_J/L+eta*unif = delta_1+(1-eta)^2 F_L "
              f"off 1 (max err {err:.1e}); n max nu = {n * max(nu):.2f}  OK")


# ---------------------------------------------------------------- Part V
def part5():
    for p in (401, 1009, 2017, 4001):
        n, zeta, log, Q = setup(p)
        K = max(2, int(math.isqrt(p)) // 6)
        Ip = [pow(zeta, k % n, p) for k in range(-K, K + 1)]
        Ip_l = sorted(set(Ip) - {1})
        Xoff, X = X_off_labels(p, Q, Ip_l)
        S = [(x - 1) % p for x in Ip if x != 1]          # I' - 1 subset of F_p^*
        cnt = {}
        for a in S:
            for b in S:
                q = a * inv(b, p) % p
                cnt[q] = cnt.get(q, 0) + 1
        E = sum(v * v for v in cnt.values())
        assert E <= 16 * (X + len(Ip) ** 2)
        print(f"V   p={p} |I'|={len(Ip)}: E^x(I'-1)={E} <= 16(X(1_I')+|I'|^2) = {16 * (X + len(Ip) ** 2)}; "
              f"E/X = {E / X:.3f}, X_off/|I'|^2 = {Xoff / len(Ip) ** 2:.3f}  OK")


if __name__ == "__main__":
    part1()
    part2()
    part3()
    part4()
    part5()
    print("ALL EXACT CHECKS OK")
