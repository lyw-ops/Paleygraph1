#!/usr/bin/env python3
r"""Round 185, call ordinary-prime-near-critical-band-autocorrelation: checks and models.

Two modes.

  --check P [P ...]   EXACT integer checks at small primes (p = 1 mod 4 not required):
      (i)  the quadrilinear form C#(lambda)[f1,f2,f3,f4] computed by brute force over the
           Round 180 relation (Y1-D1)(1-D3) = lambda (Y3-D3)(1-D1), all coordinates in
           F_p minus {0,1}, Y1 != D1, Y3 != D3, equals sum_r m12(lambda r) m34(r) with
           m_ab(r) = sum_{(Y,D) on row r} f_a(Y) f_b(D), r = (Y-D)/(1-D);
      (ii) m_ab(r) <= c_{v_a,v_b}(1-r), v(z) = f(1-z) for z != 0, and the Hoelder bound
           C#(lambda)^4 <= prod_i E^x(v_i) (exact integers);
      (iii) the R180 line family is injective in (D1, D3) for every lambda != 0, 1.
      Random nonnegative integer weights f_i, every lambda in F_p minus {0,1}.

  P [P ...]           FLOATING flat-law models (evidence only). nu uniform on S, g = |f|^2
      as in research/paley-184-rowmass-models.py (whose setup is re-implemented here).
      Models with band mass: ap+rand b (S = A + B, A an arithmetic progression of
      length ~ m/b chosen to maximize sector alignment, B random of size b), aphalf,
      rand. For each: sup_{lambda!=1} C, max W, X, sum W^{3/2}, band L^2 mass
      Lambda_band = sum_{p^{-1/8} < g < p^{-1/192}} g^2, and the decomposition of
      C(lambda) into the height classes of Theorems 1-2 of the report:
        L: g < tau0 = p^{-1/7};  B: tau0 <= g < tau1;  H: g >= tau1,
      for tau1 = p^{-1/214} (the theorem's cut) and tau1 = 1/2 (illustration).
      Printed: sup over lambda != 1 of the all-H term, of the terms with a B role and
      no L role, of the terms with an L role, and E^x(h_H) (the bound used for all-H).
"""
import sys
import random
import numpy as np


# ---------------------------------------------------------------- exact checks

def exact_check(p, seed=1):
    rng = random.Random(seed * 1000 + p)
    inv = [0] + [pow(x, p - 2, p) for x in range(1, p)]
    pts = list(range(2, p))   # F_p minus {0,1}
    f = [[0] * p for _ in range(4)]
    for i in range(4):
        for x in pts:
            f[i][x] = rng.randint(0, 3)

    def row(Y, D):
        return (Y - D) * inv[(1 - D) % p] % p

    def m(a, b):
        out = [0] * p
        for Y in pts:
            for D in pts:
                if Y != D:
                    out[row(Y, D)] += f[a][Y] * f[b][D]
        return out

    m12, m34 = m(0, 1), m(2, 3)
    # v_i(z) = f_i(1 - z) for z != 0;  c_{va,vb}(k) = sum_z v_b(z) v_a(k z)
    v = [[0] * p for _ in range(4)]
    for i in range(4):
        for z in range(1, p):
            v[i][z] = f[i][(1 - z) % p]

    def cab(a, b, k):
        return sum(v[b][z] * v[a][k * z % p] for z in range(1, p))

    def E(i):
        return sum(sum(v[i][z] * v[i][k * z % p] for z in range(1, p)) ** 2 for k in range(1, p))

    Es = [E(i) for i in range(4)]
    bad = 0
    for r in range(1, p):
        k = (1 - r) % p
        if k != 0:
            if m12[r] > cab(0, 1, k) or m34[r] > cab(2, 3, k):
                bad += 1
    for lam in range(2, p):
        brute = 0
        for Y1 in pts:
            for D1 in pts:
                if Y1 == D1:
                    continue
                for D3 in pts:
                    # Y3 = D3 + (Y1-D1)(1-D3) / (lam (1-D1))
                    Y3 = (D3 + (Y1 - D1) * (1 - D3) * inv[lam * (1 - D1) % p]) % p
                    if Y3 in (0, 1) or Y3 == D3:
                        continue
                    brute += f[0][Y1] * f[1][D1] * f[2][Y3] * f[3][D3]
        rowsum = sum(m12[lam * r % p] * m34[r] for r in range(1, p))
        if brute != rowsum:
            bad += 1
        if brute ** 4 > Es[0] * Es[1] * Es[2] * Es[3]:
            bad += 1
        # line family injectivity: line (1-D3)(X-D1) = lam(1-D1)(Z-D3), normalised
        seen = set()
        for D1 in pts:
            for D3 in pts:
                a, b = (1 - D3) % p, (-lam * (1 - D1)) % p
                c = (-(1 - D3) * D1 + lam * (1 - D1) * D3) % p
                ia = inv[a]
                key = (b * ia % p, c * ia % p)
                if key in seen:
                    bad += 1
                seen.add(key)
    print(f"p = {p}: rows <= c_(va,vb): ok; brute = row formula, Hoelder C^4 <= prod E, "
          f"line injectivity over {p-2} lambdas: {'OK' if bad == 0 else f'{bad} FAILURES'}")
    return bad == 0


# ---------------------------------------------------------------- models

def prim_root(p):
    m = p - 1
    fac, t = [], 2
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
    assert p % 4 == 1
    th = prim_root(p)
    N = p - 1
    n = N // 2
    exp = np.zeros(N, dtype=np.int64)
    x = 1
    for t in range(N):
        exp[t] = x
        x = x * th % p
    log = np.full(p, -1, dtype=np.int64)
    log[exp] = np.arange(N)
    leg = np.zeros(p, dtype=np.int64)
    leg[exp] = np.where(np.arange(N) % 2 == 0, 1, -1)
    xs = exp[0::2]
    chi1 = leg[(1 - xs) % p]
    k = (np.fft.fft(chi1) / np.sqrt(p)).real
    return dict(p=p, N=N, n=n, exp=exp, log=log, xs=xs, chi1=chi1, k=k)


def rf(a):
    return np.fft.rfft(a)


def corr(a, b):
    """c[t] = sum_s a[s] b[s+t] (cyclic)."""
    return np.fft.irfft(np.conj(rf(a)) * rf(b), len(a))


def conv(a, b):
    return np.fft.irfft(rf(a) * rf(b), len(a))


def best_ap(k, m, rho, n):
    from math import gcd
    ds = np.arange(-(m - 1), m)
    wts = (m - np.abs(ds)).astype(float)
    best = (-np.inf, 1)
    for a in range(1, n):
        if gcd(a, n) == 1:
            v = rho * np.dot(wts, k[(a * ds) % n])
            if v > best[0]:
                best = (v, a)
    return best[1]


def gfun(env, S):
    p, n = env['p'], env['n']
    S = np.asarray(sorted(set(int(s) % n for s in S)))
    ind = np.zeros(n)
    ind[S] = 1.0
    f = np.fft.ifft(ind) * n / len(S)
    gQ = np.abs(f) ** 2
    g = np.zeros(p)
    g[env['xs']] = gQ
    g[1] = 0.0           # x = 1 is excluded from every role (interior exclusion)
    return g, len(S)


def rows_from(env, ga, gb):
    """masked row m_ab(r) = c_{ha,hb}(1-r) for 1-r in Q minus {1}, indexed by log r."""
    p, N, exp, log = env['p'], env['N'], env['exp'], env['log']
    ha = ga[(1 - exp) % p]
    hb = gb[(1 - exp) % p]
    c = corr(hb, ha)                    # c[t] = sum_z hb(z) ha(theta^t z)
    lu = log[(1 - exp) % p]             # log(1 - r) for r = theta^t (r != 1)
    ok = (lu >= 0) & (lu % 2 == 0) & (lu != 0)
    mr = np.zeros(N)
    mr[ok] = c[lu[ok]]
    return mr


def Ex(env, gpart):
    p, exp = env['p'], env['exp']
    h = gpart[(1 - exp) % p]
    c = corr(h, h)
    return float(np.sum(c ** 2))


def measure(env, S, tau1s):
    p, N = env['p'], env['N']
    g, m = gfun(env, S)
    G = g.sum() + 1.0
    mr = rows_from(env, g, g)
    C = corr(mr, mr)
    W = conv(mr, mr)
    X = float(C[0])
    supC = float(C[1:].max())
    lamstar = int(np.argmax(C[1:])) + 1
    maxW = float(W.max())
    W32 = float(np.sum(np.clip(W, 0, None) ** 1.5))
    lo, hi = p ** (-1 / 8), p ** (-1 / 192)
    band = (g > lo) & (g < hi)
    Lam = float(np.sum(g[band] ** 2))
    tau0 = p ** (-1 / 7)
    out = dict(m=m, G=G / np.sqrt(p), supC=supC / p, supC118=supC / p ** (11 / 8), maxW=maxW / p,
               X=X / p, W32=W32 / p ** (43 / 16), Lam=Lam / p ** (3 / 8), lam=lamstar,
               fracB=float(np.sum(g[band]) / g.sum()), dec={})
    for tau1 in tau1s:
        parts = {'L': g * (g < tau0), 'B': g * ((g >= tau0) & (g < tau1)), 'H': g * (g >= tau1)}
        keys = list(parts)
        rowsab = {(a, b): rows_from(env, parts[a], parts[b]) for a in keys for b in keys}
        CH = np.zeros(N)
        CB = np.zeros(N)
        CL = np.zeros(N)
        for a in keys:
            for b in keys:
                for c in keys:
                    for d in keys:
                        # C(lambda) = sum_r m12(r) m34(lambda r) with roles (Y1,D1) = (a,b), (Y3,D3) = (c,d)
                        t = corr(rowsab[(a, b)], rowsab[(c, d)])
                        rl = {a, b, c, d}
                        if 'L' in rl:
                            CL += t
                        elif 'B' in rl:
                            CB += t
                        else:
                            CH += t
        assert np.allclose(CH + CB + CL, C, rtol=1e-8, atol=1e-6 * max(1.0, X))
        out['dec'][tau1] = dict(H=float(CH[1:].max()) / p, B=float(CB[1:].max()) / p,
                                L=float(CL[1:].max()) / p, EH=Ex(env, parts['H']) / p,
                                atstar=(CH[lamstar] / p, CB[lamstar] / p, CL[lamstar] / p))
    return out


def models(p, seed=0):
    env = setup(p)
    n, k = env['n'], env['k']
    m = int(round(n / np.sqrt(p)))
    rng = np.random.default_rng(seed + p)
    rows = [('rand', rng.choice(np.arange(1, n), m, replace=False))]
    a2 = best_ap(k, 2 * m, 1, n)
    rows.append(('aphalf', rng.choice((a2 * np.arange(1, 2 * m + 1)) % n, m, replace=False)))
    for b in (2, 4, 8, 16):
        la = max(2, m // b)
        a3 = best_ap(k, la, 1, n)
        A = (a3 * np.arange(1, la + 1)) % n
        for _ in range(100):
            B = rng.choice(np.arange(n), b, replace=False)
            Ss = (A[:, None] + B[None, :]).ravel() % n
            if len(set(Ss.tolist())) == la * b and 0 not in set(Ss.tolist()):
                break
        rows.append((f'ap+rand b={b}', Ss))
    return env, rows


def main():
    args = sys.argv[1:]
    if args and args[0] == '--check':
        ps = [int(a) for a in args[1:]] or [13, 17, 29, 37]
        allok = all(exact_check(p) for p in ps)
        print("EXACT CHECKS OK" if allok else "EXACT CHECK FAILED")
        return
    ps = [int(a) for a in args] or [1009, 4001]
    print("flat-law models with band mass; floating evidence only (rho = +1 alignment)")
    for p in ps:
        env, rows = models(p)
        tau1s = (p ** (-1 / 214), 0.5)
        print(f"\np = {p}: tau0 = p^-1/7 = {p**(-1/7):.3f}, tau1 = p^-1/214 = {tau1s[0]:.3f} or 0.5; "
              f"band (p^-1/8, p^-1/192) = ({p**(-1/8):.3f}, {p**(-1/192):.3f})")
        print(f"{'model':>14} {'|S|':>5} {'G/rp':>5} {'bandL1':>6} {'Lam/p^3/8':>9} {'X/p':>6} {'maxW/p':>6} "
              f"{'supC/p':>6} {'supC/p^11/8':>11} {'sW^1.5/p^43/16':>14} | tau1 "
              f"{'H/p':>6} {'B/p':>6} {'L/p':>6} {'E(hH)/p':>7}")
        for name, S in rows:
            r = measure(env, S, tau1s)
            for j, t1 in enumerate(tau1s):
                d = r['dec'][t1]
                head = (f"{name:>14} {r['m']:5d} {r['G']:5.3f} {r['fracB']:6.3f} {r['Lam']:9.3f} {r['X']:6.3f} "
                        f"{r['maxW']:6.3f} {r['supC']:6.3f} {r['supC118']:11.4f} {r['W32']:14.4f}") if j == 0 \
                    else ' ' * 99
                print(f"{head} | {t1:4.2f} {d['H']:6.3f} {d['B']:6.3f} {d['L']:6.3f} {d['EH']:7.3f}")
            sys.stdout.flush()


if __name__ == '__main__':
    main()
