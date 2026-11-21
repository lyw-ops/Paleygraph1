#!/usr/bin/env python3
r"""Round 186, call ordinary-prime-sup-c-heavy-price: exact identity checks and floating models.

Two modes.

  --check P [P ...]   EXACT integer checks at small primes, for random sets
                      A, B, X1..X4 inside F_p minus {0,1} and V = B^{-1}:
    (i)   Lemma M incidence structure: the lines l_{u,v}: Z = v(uX + 1 - u),
          (u,v) in F_p^* x V, are pairwise distinct, nonvertical and nonhorizontal;
          for every row solution (x,y) in A x B of 1-y = u(1-x) and every v in V the
          point (x, v y) lies in A x VB and on l_{u,v}; the map
          (u,v,x,y) -> (line, point) is injective; hence for T = {u : m(u) >= h}
          I(A x VB, {l_{u,v}}_{u in T, v in V}) >= h |T| |V|.
    (ii)  the pair energy of Lemma 5's Cauchy-Schwarz:
          E(1_{1-A},1_{1-B}) := sum_kappa c(kappa)^2, c(kappa) = sum_z 1_{1-B}(z) 1_{1-A}(kappa z)
          equals sum_u m(u)^2 (rows of Lemma M), and is symmetric in (A, B).
    (iii) triangle inequality E(1-(B1 u B2), 1-A)^{1/2} <= E(1-B1,1-A)^{1/2} + E(1-B2,1-A)^{1/2}
          for disjoint B1, B2 (checked exactly by squaring).
    (iv)  C#_lambda[1_X1, 1_X2, 1_X3, 1_X4]^2 <= E(1-X1,1-X2) E(1-X3,1-X4) for every
          lambda in F_p minus {0,1} (brute force over the Round 180 relation).

  P [P ...]           FLOATING models (evidence only): nu uniform on S (the Round 185 flat
                      laws: rand, aphalf, ap+rand b), g = |f|^2.  For dyadic levels
                      U_a = {a/2 < g <= a}, a = 2^-k >= p^{-1/7}, it prints
      * K_a = |U|^3 / E^x(U) (the BSG input; Lemma S1 gives K <= C sqrt p/(a^2 |U|) * ...),
      * the pair energies E(1-U_a, 1-U_b) / (|U_a||U_b|) (near-sharp scale is O(1)),
      * the largest pair price a b E(1-U_a,1-U_b)^{1/2} / p^{2/3} over all level pairs
        (Theorem A pays p^{2/3 + 3 min(e_a, e_b)} for this quantity).
"""
import sys
import random
import numpy as np


# ---------------------------------------------------------------- exact checks
def isqrt_le(a, b, c):
    """exact test of sqrt(a) <= sqrt(b) + sqrt(c) for nonnegative integers."""
    if a <= b + c:
        return True
    return (a - b - c) ** 2 <= 4 * b * c


def exact_check(p, seed=1):
    rng = random.Random(seed * 7919 + p)
    inv = [0] + [pow(x, p - 2, p) for x in range(1, p)]
    pts = list(range(2, p))
    bad = 0

    def rnd_set(k):
        return set(rng.sample(pts, k))

    def rows(A, B):
        m = [0] * p
        for x in A:
            for y in B:
                u = (1 - y) * inv[(1 - x) % p] % p
                m[u] += 1
        return m

    def Epair(A, B):
        # c(kappa) = sum_z 1_{1-B}(z) 1_{1-A}(kappa z)
        oneB = [(1 - y) % p for y in B]
        Aset = set(A)
        tot = 0
        for k in range(1, p):
            c = sum(1 for z in oneB if (1 - k * z) % p in Aset)
            tot += c * c
        return tot

    for trial in range(3):
        A = rnd_set(rng.randint(2, max(3, p // 3)))
        B = rnd_set(rng.randint(2, max(3, p // 3)))
        V = sorted({inv[b] for b in B})
        VB = {v * y % p for v in V for y in B}
        # (i) lines and incidences
        lines = {}
        for u in range(1, p):
            for v in V:
                slope, icpt = v * u % p, v * (1 - u) % p
                if slope == 0:
                    bad += 1          # would be horizontal
                key = (slope, icpt)
                if key in lines:
                    bad += 1          # not distinct
                lines[key] = (u, v)
        m = rows(A, B)
        seen = set()
        for x in A:
            for y in B:
                u = (1 - y) * inv[(1 - x) % p] % p
                for v in V:
                    P = (x, v * y % p)
                    if P[1] not in VB:
                        bad += 1
                    slope, icpt = v * u % p, v * (1 - u) % p
                    if (slope * P[0] + icpt) % p != P[1]:
                        bad += 1      # point not on its line
                    key = ((slope, icpt), P)
                    if key in seen:
                        bad += 1      # incidence map not injective
                    seen.add(key)
        for h in (1, 2, 3):
            Th = [u for u in range(1, p) if m[u] >= h]
            Ls = {(v * u % p, v * (1 - u) % p) for u in Th for v in V}
            I = sum(1 for (s, c) in Ls for x in A if (s * x + c) % p in VB)
            if I < h * len(Th) * len(V):
                bad += 1
        # (ii)
        E1 = Epair(A, B)
        if E1 != sum(t * t for t in m) or E1 != Epair(B, A):
            bad += 1
        if sum(m) != len(A) * len(B):
            bad += 1
        # (iii)
        Bl = sorted(B)
        B1, B2 = set(Bl[: len(Bl) // 2]), set(Bl[len(Bl) // 2:])
        if not isqrt_le(Epair(A, B), Epair(A, B1), Epair(A, B2)):
            bad += 1
    # (iv) quadrilinear Cauchy-Schwarz for sets
    X = [rnd_set(rng.randint(2, max(3, p // 2))) for _ in range(4)]

    def mrow(Xa, Xb):
        out = [0] * p
        for Y in Xa:
            for D in Xb:
                if Y != D:
                    out[(Y - D) * inv[(1 - D) % p] % p] += 1
        return out
    m12, m34 = mrow(X[0], X[1]), mrow(X[2], X[3])
    E12, E34 = Epair(X[0], X[1]), Epair(X[2], X[3])
    for lam in range(2, p):
        # brute force C#: (Y1-D1)(1-D3) = lam (Y3-D3)(1-D1)
        Cb = 0
        for Y1 in X[0]:
            for D1 in X[1]:
                if Y1 == D1:
                    continue
                for Y3 in X[2]:
                    for D3 in X[3]:
                        if Y3 != D3 and ((Y1 - D1) * (1 - D3) - lam * (Y3 - D3) * (1 - D1)) % p == 0:
                            Cb += 1
        Cr = sum(m12[lam * r % p] * m34[r] for r in range(1, p))
        if Cb != Cr or Cb * Cb > E12 * E34:
            bad += 1
    return bad


# ---------------------------------------------------------------- models
def prim_root(p):
    m, fac, t = p - 1, [], 2
    while t * t <= m:
        if m % t == 0:
            fac.append(t)
            while m % t == 0:
                m //= t
        t += 1
    if m > 1:
        fac.append(m)
    for g in range(2, p):
        if all(pow(g, (p - 1) // q, p) != 1 for q in fac):
            return g


def setup(p):
    th = prim_root(p)
    N = p - 1
    exp = np.zeros(N, dtype=np.int64)
    x = 1
    for t in range(N):
        exp[t] = x
        x = x * th % p
    log = np.full(p, -1, dtype=np.int64)
    log[exp] = np.arange(N)
    xs = exp[0::2]
    leg = np.zeros(p, dtype=np.int64)
    leg[exp] = np.where(np.arange(N) % 2 == 0, 1, -1)
    k = (np.fft.fft(leg[(1 - xs) % p]) / np.sqrt(p)).real
    return dict(p=p, N=N, n=N // 2, exp=exp, log=log, xs=xs, k=k)


def corr(a, b):
    return np.fft.irfft(np.conj(np.fft.rfft(a)) * np.fft.rfft(b), len(a))


def best_ap(k, m, n):
    from math import gcd
    ds = np.arange(-(m - 1), m)
    wts = (m - np.abs(ds)).astype(float)
    best = (-np.inf, 1)
    for a in range(1, n):
        if gcd(a, n) == 1:
            v = np.dot(wts, k[(a * ds) % n])
            if v > best[0]:
                best = (v, a)
    return best[1]


def gfun(env, S):
    p, n = env['p'], env['n']
    S = np.asarray(sorted(set(int(s) % n for s in S)))
    ind = np.zeros(n)
    ind[S] = 1.0
    f = np.fft.ifft(ind) * n / len(S)
    g = np.zeros(p)
    g[env['xs']] = np.abs(f) ** 2
    g[1] = 0.0
    return g


def model_laws(env, seed=0):
    p, n, k = env['p'], env['n'], env['k']
    m = int(round(n / np.sqrt(p)))
    rng = np.random.default_rng(seed + p)
    out = [('rand', rng.choice(np.arange(1, n), m, replace=False))]
    a2 = best_ap(k, 2 * m, n)
    out.append(('aphalf', rng.choice((a2 * np.arange(1, 2 * m + 1)) % n, m, replace=False)))
    for b in (2, 4):
        la = max(2, m // b)
        a3 = best_ap(k, la, n)
        A = (a3 * np.arange(1, la + 1)) % n
        for _ in range(100):
            B = rng.choice(np.arange(n), b, replace=False)
            Ss = (A[:, None] + B[None, :]).ravel() % n
            if len(set(Ss.tolist())) == la * b and 0 not in set(Ss.tolist()):
                break
        out.append((f'ap+rand b={b}', Ss))
    return out


def run_models(p):
    env = setup(p)
    exp, N = env['exp'], env['N']
    tau0 = p ** (-1 / 7)
    print(f"p = {p}:  tau0 = p^-1/7 = {tau0:.3f}")
    for name, S in model_laws(env):
        g = gfun(env, S)
        G = g.sum() + 1.0
        levels = []
        a = 1.0
        while a / 2 >= tau0 / 2 and a > 1e-9:
            U = (g > a / 2) & (g <= a)
            U[1] = False
            if U.sum() > 0:
                levels.append((a, U))
            a /= 2
        # shifted indicator in log coordinates: z = theta^t, v(z) = 1_U(1 - z)
        vs = [(a, U.sum(), U[(1 - exp) % p].astype(float)) for a, U in levels]
        worst = (0.0, None)
        maxratio = 0.0
        rows = []
        for i, (a, na, va) in enumerate(vs):
            ca = corr(va, va)
            Eaa = float(np.sum(ca ** 2))
            # multiplicative energy of U itself (in log coordinates of Q): K = |U|^3/E
            lu = np.zeros(N)
            idx = env['log'][np.nonzero(levels[i][1])[0]]
            lu[idx] = 1.0
            EU = float(np.sum(corr(lu, lu) ** 2))
            K = na ** 3 / EU
            rows.append((a, int(na), K, Eaa / na ** 2))
            for j, (b, nb, vb) in enumerate(vs):
                if j < i:
                    continue
                Eab = float(np.sum(corr(vb, va) ** 2))
                ratio = Eab / (na * nb * (1 + na * nb / p))
                maxratio = max(maxratio, ratio)
                price = a * b * np.sqrt(Eab) / p ** (2 / 3)
                if price > worst[0]:
                    worst = (price, (a, b))
        print(f"  {name:12s} G/sqrt p = {G/np.sqrt(p):.3f}; max_ab E(1-U_a,1-U_b)/(|U_a||U_b|(1+|U_a||U_b|/p)) = {maxratio:.3f};"
              f" max pair price ab E^1/2 / p^(2/3) = {worst[0]:.4f} at (a,b) = {worst[1]}")
        for (a, na, K, r) in rows[:5]:
            print(f"      level a = {a:.4g}: |U| = {na:5d} (|U|/sqrt p = {na/np.sqrt(p):.3f}), K = |U|^3/E^x(U) = {K:8.3f},"
                  f" E^x(1-U)/|U|^2 = {r:.3f}")


def main():
    args = sys.argv[1:]
    if args and args[0] == '--check':
        ps = [int(x) for x in args[1:]] or [13, 17, 29, 37]
        tot = 0
        for p in ps:
            b = exact_check(p)
            print(f"p = {p}: {'ok' if b == 0 else f'{b} FAILURES'}")
            tot += b
        print("EXACT CHECKS OK" if tot == 0 else "EXACT CHECKS FAILED")
        return
    for p in [int(x) for x in args] or [4001, 16001]:
        assert p % 4 == 1
        run_models(p)


if __name__ == '__main__':
    main()
