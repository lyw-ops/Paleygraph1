#!/usr/bin/env python3
r"""Round 191, call ordinary-first-mass-sector-obstruction: floating models (evidence only).

Report: research/native-claude-ordinary-first-mass-sector-obstruction-191.md.

Mode A  (laws):   .venv/bin/python -B research/paley-191-mwsector-models.py laws P [P ...]
  For each prime P = 1 mod 4 and five laws written in log coordinates x = zeta^k (zeta = gamma^2):
    int      pure interval law, g = F_L(k), L = round(n/sqrt p)            (Round 189 Prop. 3(c))
    mix      eta-mixture, nu = (1-eta)1_J/L + eta unif(Q^), eta = 1/2: g = delta_1 + (1/4)F_L
    Dth      diluted interval D_theta, theta = 1/4                            (Round 190 Theorem 4)
    Dmix     D_theta^eta, theta = 1/4, eta = 1/2: nu uniform on S1 u S2, S1 theta-dense in an
             interval, |S1| = m/2, S2 a uniformly random (m/2)-set elsewhere  (Theorem 4' of the report)
    Dmix9    D_theta^eta, theta = 0.45, eta = 0.1
  prints  G/sqrt p, Gamma_tot/sqrt p, M_w/p (fibre form via FFT), X/p (= E_Q(h)), M_w/X,
          K' = floor(n/(8 L_eff)), |I'|, X_off(1_I') (integer), tau' = min_{I'\1} g,
          tau'' = min w on Sigma(I')\1, LB = tau'^4 tau'' X_off(1_I'), M_w/X_off(1_I'),
          M_w|I' / X_off(1_I')  and  <(j/K')^2>  over the nontrivial I'-quadruples.
  and for the flat laws the sector-free (NC) diagnostics of Round 190 Theorem 4:
          E(S)/|S|^3, max_{a!=0} |S cap (S+a)|/|S|, max fraction of S in a coset of a subgroup of
          Z/n of order <= 2 m_0, max relative g-mass on a coset of a subgroup of Q of order in
          [sqrt p/4, 4 sqrt p] (excluding the point 1).
Mode J  (near-diagonal distribution; integers, exact counts):
          .venv/bin/python -B research/paley-191-mwsector-models.py jdist C P [P ...]
  For I = {zeta^k : |k| <= K}, K = round(C sqrt p): counts the nontrivial masked energy
  quadruples of 1 - I (pairs P != P' on a common pencil line 1-Y = kappa(1-D), kappa in Q\1)
  by j = exponent of AD/(CY) in [-4K, 4K] \ {0}, and compares the profile with the
  four-uniform baseline (j = a + d - c - y, a, c, d, y independent uniform on [-K, K]).
Mode C  (--check): compares the FFT fibre form with a brute-force row form at p <= 113.

numpy; seeds deterministic in p.
"""
import math
import sys

import numpy as np


# ---------------------------------------------------------------- arithmetic setup
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


def setup(p, need_log=True):
    n = (p - 1) // 2
    gam = prim_root(p)
    zeta = gam * gam % p
    zp = np.empty(n, dtype=np.int64)
    x = 1
    for k in range(n):
        zp[k] = x
        x = x * zeta % p
    logt = None
    if need_log:
        logt = np.full(p, -1, dtype=np.int64)
        logt[zp] = np.arange(n, dtype=np.int64)
    return n, zeta, zp, logt


# ---------------------------------------------------------------- laws (g in log coordinates)
def fejer(L, n):
    k = np.arange(n)
    out = np.ones(n)
    nz = k != 0
    out[nz] = (np.sin(np.pi * L * k[nz] / n) / (L * np.sin(np.pi * k[nz] / n))) ** 2
    return out


def g_from_S(S, n):
    v = np.zeros(n)
    v[S] = 1.0 / len(S)
    f = np.fft.ifft(v) * n            # f(k) = sum_j nu_j e(jk/n)
    return np.abs(f) ** 2


def law(name, p, n, rng):
    m0 = n / math.sqrt(p)
    m = int(round(m0))
    if name == "int":
        L = int(round(n / math.sqrt(p)))
        return fejer(L, n), L, None
    if name == "mix":
        L = int(round(n / math.sqrt(p) / 2))       # cap: n max nu = n/(2L) + 1/2 ~ sqrt p
        g = 0.25 * fejer(L, n)
        g[0] = 1.0
        return g, L, None
    if name in ("Dth", "Dmix", "Dmix9"):
        theta, eta = {"Dth": (0.25, 0.0), "Dmix": (0.25, 0.5), "Dmix9": (0.45, 0.1)}[name]
        m1 = int(round((1 - eta) * m))
        Lp = int(round(m1 / theta))
        a0 = 1 + int(rng.integers(0, n - Lp - 1))
        J = np.arange(a0, a0 + Lp)
        S1 = rng.choice(J, size=m1, replace=False)
        rest = np.setdiff1d(np.arange(1, n), J)
        S2 = rng.choice(rest, size=m - m1, replace=False) if m - m1 > 0 else np.array([], dtype=int)
        S = np.concatenate([S1, S2]).astype(np.int64)
        return g_from_S(S, n), Lp, S
    raise ValueError(name)


# ---------------------------------------------------------------- M_w and X via the fibre form
def mw_fft(p, n, zp, logt, g, chunk=256):
    w = g * (1 - g)
    W = np.fft.fft(w)
    Dk = np.arange(1, n, dtype=np.int64)
    D = zp[1:]
    gD = g[1:]
    S = np.zeros(n)
    X = 0.0
    diag = 0.0
    kks = np.arange(1, n, dtype=np.int64)
    for c0 in range(0, len(kks), chunk):
        kk = kks[c0:c0 + chunk]
        kap = zp[kk]
        Y = (1 - (kap[:, None] * ((1 - D[None, :]) % p)) % p) % p
        ly = logt[Y]
        valid = (ly > 0)                       # Y in Q and Y != 1  (log 0 <-> Y = 1)
        rows_i, cols_i = np.nonzero(valid)
        u = (kk[rows_i] + Dk[cols_i] - ly[rows_i, cols_i]) % n
        val = g[ly[rows_i, cols_i]] * gD[cols_i]
        nu = np.zeros((len(kk), n))
        np.add.at(nu, (rows_i, u), val)
        V = np.fft.fft(nu, axis=1)
        S += (np.abs(V) ** 2).sum(axis=0)
        msum = nu.sum(axis=1)
        X += float((msum ** 2).sum())
        diag += float((nu ** 2).sum())
    Mw = float((W.real * S).sum() / n)
    return Mw, X, diag


def mw_brute(p, n, zp, logt, g):
    w = g * (1 - g)
    Qs = [int(x) for x in zp[1:]]
    rows = {}
    for Y in Qs:
        for D in Qs:
            if Y == D:
                continue
            k = (1 - Y) * pow(1 - D, p - 2, p) % p
            if logt[k] > 0:
                rows.setdefault(k, []).append((Y, D))
    tot = 0.0
    for L in rows.values():
        for (Y, D) in L:
            for (A, C) in L:
                s = A * D * pow(C * Y, p - 2, p) % p
                tot += g[logt[Y]] * g[logt[D]] * g[logt[A]] * g[logt[C]] * w[logt[s]]
    return tot


# ---------------------------------------------------------------- restricted energy on a GP
def gp_quadruples(p, n, zeta, K):
    """Nontrivial masked energy quadruples of 1 - I, I = {zeta^k: |k|<=K}, labels != 1.
    Returns arrays (iP, iP') of label-pair indices and j = signed exponent of AD/(CY),
    and the fibre sizes, using only O(K^2) memory."""
    ks = np.array([k for k in range(-K, K + 1) if k != 0], dtype=np.int64)
    vals = np.array([pow(zeta, int(k) % n, p) for k in ks], dtype=np.int64)
    om = (1 - vals) % p
    inv_om = np.array([pow(int(x), p - 2, p) for x in om], dtype=np.int64)
    chi = np.array([1 if pow(int(x), (p - 1) // 2, p) == 1 else -1 for x in om])
    N = len(ks)
    iy, idd = np.meshgrid(np.arange(N), np.arange(N), indexing="ij")
    iy = iy.ravel()
    idd = idd.ravel()
    keep = (iy != idd) & (chi[iy] * chi[idd] == 1)
    iy, idd = iy[keep], idd[keep]
    kap = (om[iy] * inv_om[idd]) % p
    order = np.argsort(kap, kind="stable")
    kap, iy, idd = kap[order], iy[order], idd[order]
    _, start, cnt = np.unique(kap, return_index=True, return_counts=True)
    js = []
    maxc = int(cnt.max()) if len(cnt) else 0
    M = len(kap)
    for off in range(1, maxc):
        same = np.nonzero(kap[:M - off] == kap[off:])[0]
        if len(same) == 0:
            continue
        a, b = same, same + off           # P = (Y,D) at a, P' = (A,C) at b
        j = ks[iy[b]] + ks[idd[a]] - ks[idd[b]] - ks[iy[a]]
        js.append(j)
        js.append(-j)                     # ordered pair (P', P)
    j = np.concatenate(js) if js else np.array([], dtype=np.int64)
    return j, cnt, ks


def restricted(p, n, zeta, g, K):
    j, cnt, ks = gp_quadruples(p, n, zeta, K)
    Xoff = int((cnt.astype(np.int64) * (cnt - 1)).sum())
    X = int((cnt.astype(np.int64) ** 2).sum())
    assert Xoff == len(j)
    return j, Xoff, X


def restricted_Mw(p, n, zeta, g, K):
    """M_w|_{I'} = sum over nontrivial I'-quadruples of g(Y)g(D)g(A)g(C) w(s)."""
    w = g * (1 - g)
    ks = np.array([k for k in range(-K, K + 1) if k != 0], dtype=np.int64)
    vals = np.array([pow(zeta, int(k) % n, p) for k in ks], dtype=np.int64)
    om = (1 - vals) % p
    inv_om = np.array([pow(int(x), p - 2, p) for x in om], dtype=np.int64)
    chi = np.array([1 if pow(int(x), (p - 1) // 2, p) == 1 else -1 for x in om])
    N = len(ks)
    iy, idd = np.meshgrid(np.arange(N), np.arange(N), indexing="ij")
    iy, idd = iy.ravel(), idd.ravel()
    keep = (iy != idd) & (chi[iy] * chi[idd] == 1)
    iy, idd = iy[keep], idd[keep]
    kap = (om[iy] * inv_om[idd]) % p
    order = np.argsort(kap, kind="stable")
    kap, iy, idd = kap[order], iy[order], idd[order]
    _, cnt = np.unique(kap, return_counts=True)
    tot = 0.0
    M = len(kap)
    gk = lambda e: g[e % n]
    for off in range(1, int(cnt.max()) if len(cnt) else 0):
        same = np.nonzero(kap[:M - off] == kap[off:])[0]
        if len(same) == 0:
            continue
        a, b = same, same + off
        y, d, A, C = ks[iy[a]], ks[idd[a]], ks[iy[b]], ks[idd[b]]
        mu = gk(y) * gk(d) * gk(A) * gk(C)
        j = A + d - C - y
        tot += float((mu * (w[j % n] + w[(-j) % n])).sum())     # (P,P') and (P',P)
    return tot


# ---------------------------------------------------------------- (NC) sector-free diagnostics
def nc_diag(S, g, n, p):
    m = len(S)
    v = np.zeros(n)
    v[S] = 1
    V = np.fft.fft(v)
    r = np.rint(np.fft.ifft(np.abs(V) ** 2).real).astype(np.int64)   # r[a] = |S cap (S+a)|
    E = float((r.astype(float) ** 2).sum())
    maxov = float(r[1:].max()) / m
    m0 = n / math.sqrt(p)
    cos_max = 0.0
    for e in range(2, int(2 * m0) + 1):
        if n % e:
            continue
        step = n // e
        cos_max = max(cos_max, np.bincount(S % step, minlength=step).max() / m)
    G = g.sum()
    gm = g.copy()
    gm[0] = 0.0
    mass_max = 0.0
    sp = math.sqrt(p)
    for d in range(2, n + 1):
        if n % d or not (sp / 4 <= d <= 4 * sp):
            continue
        step = n // d
        mass_max = max(mass_max, np.bincount(np.arange(n) % step, weights=gm, minlength=step).max() / G)
    return E / m ** 3, maxov, cos_max, mass_max


# ---------------------------------------------------------------- modes
PMAX_FULL = 30000      # full M_w (FFT fibre form, O(n^2 log n)) only up to this p


def mode_laws(primes):
    print("law    p      G/sp   Gt/sp  Mw/p     X/p     Mw/X   K'  |I'| Xoff(I') tau'   tau''  "
          "LB        Mw/Xoff   Mw|I'/Xoff <(j/K')^2> | E/m^3  maxov  coset  cmass")
    for p in primes:
        full = p <= PMAX_FULL
        if full:
            n, zeta, zp, logt = setup(p)
        else:
            n = (p - 1) // 2
            zeta = prim_root(p) ** 2 % p
        sp = math.sqrt(p)
        for name in ("int", "mix", "Dth", "Dmix", "Dmix9"):
            rng = np.random.default_rng(p * 7 + len(name))
            g, Leff, S = law(name, p, n, rng)
            G = g.sum()
            Gt = (g ** 2).sum()
            if full:
                Mw, X, diag = mw_fft(p, n, zp, logt, g)
            else:
                Mw, X = float("nan"), float("nan")
            K = n // (8 * Leff)
            if K >= 1:
                j, Xoff, XI = restricted(p, n, zeta, g, K)
                ks = np.arange(-K, K + 1)
                ks = ks[ks != 0]
                t1 = g[ks % n].min()
                win = np.arange(1, 4 * K + 1)
                ww = g * (1 - g)
                t2 = ww[np.concatenate([win, -win]) % n].min()
                LB = t1 ** 4 * t2 * Xoff
                MwI = restricted_Mw(p, n, zeta, g, K)
                j2 = float(((j / K) ** 2).mean()) if len(j) else float("nan")
            else:
                Xoff, t1, t2, LB, MwI, j2 = 0, float("nan"), float("nan"), 0.0, 0.0, float("nan")
            line = (f"{name:6s} {p:6d} {G / sp:6.3f} {Gt / sp:6.3f} {Mw / p:8.5f} {X / p:7.4f} "
                    f"{Mw / X:6.4f} {K:3d} {2 * K + 1:4d} {Xoff:8d} {t1:6.3f} {t2:6.4f} {LB:9.3e} "
                    f"{(Mw / Xoff if Xoff else float('nan')):9.3e} "
                    f"{(MwI / Xoff if Xoff else float('nan')):9.3e} {j2:7.3f}")
            if S is not None:
                e3, mo, cm, ms = nc_diag(S, g, n, p)
                line += f" | {e3:6.3f} {mo:6.3f} {cm:6.3f} {ms:6.3f}"
            if full:
                assert Mw >= MwI - 1e-9 * max(1.0, Mw)
            assert MwI >= LB * (1 - 1e-9)
            if name == "int" and K >= 1 and Xoff:
                # Proposition 2(b): two-sided comparison with X_2 = sum j^2 (pure Fejer law)
                X2 = float((j.astype(float) ** 2).sum())
                u = (Leff ** 2 - 1) / n ** 2
                lo = (4 / math.pi ** 2) ** 5 * (4 / 3) * u * X2
                hi = (math.pi ** 2 / 3) * u * X2
                assert lo * (1 - 1e-9) <= MwI <= hi * (1 + 1e-9), (lo, MwI, hi)
                line += f"  [Prop2b: {lo / MwI:.3f} <= 1 <= {hi / MwI:.3f}]"
            print(line, flush=True)


def baseline(K):
    """pmf of j = a + d - c - y, a,c,d,y iid uniform on [-K,K], on [-4K,4K]."""
    u = np.ones(2 * K + 1) / (2 * K + 1)
    pmf = np.convolve(np.convolve(u, u), np.convolve(u, u))
    return pmf          # index t <-> j = t - 4K


def mode_jdist(C, primes):
    eps = (0.125, 0.25, 0.5, 1.0)
    print("p           K     |I|   Xoff/|I|^2  " + "  ".join(f"P(|j|<={e}K) base" for e in eps)
          + "   <(j/K)^2> base")
    for p in primes:
        n, zeta, zp, _ = setup(p, need_log=False) if p < 3 * 10 ** 7 else (None, None, None, None)
        if n is None:
            n = (p - 1) // 2
            gam = prim_root(p)
            zeta = gam * gam % p
        K = int(round(C * math.sqrt(p)))
        j, cnt, ks = gp_quadruples(p, n, zeta, K)
        Xoff = len(j)
        N = 2 * K + 1
        pmf = baseline(K)
        jj = np.arange(-4 * K, 4 * K + 1)
        nz = jj != 0
        base = pmf.copy()
        base[~nz] = 0
        base /= base.sum()
        parts = []
        for e in eps:
            obs = float((np.abs(j) <= e * K).mean())
            bas = float(base[np.abs(jj) <= e * K].sum())
            parts.append(f"{obs:8.4f} {bas:6.4f}")
        m2 = float(((j / K) ** 2).mean())
        m2b = float((base * (jj / K) ** 2).sum())
        print(f"{p:10d} {K:6d} {N:6d} {Xoff / N ** 2:9.4f}   " + "  ".join(parts)
              + f"   {m2:7.4f} {m2b:6.4f}", flush=True)


def mode_check():
    rng = np.random.default_rng(5)
    for p in (41, 61, 101, 113):
        n, zeta, zp, logt = setup(p)
        g = rng.integers(0, 13, size=n) / 12.0
        g[0] = 1.0
        a, X, diag = mw_fft(p, n, zp, logt, g)
        b = mw_brute(p, n, zp, logt, g)
        assert abs(a - b) <= 1e-9 * max(1, abs(b)), (p, a, b)
        print(f"check p={p}: FFT fibre form {a:.9f} == brute row form {b:.9f}")
        # restricted pieces
        K = max(1, n // 16)
        MwI = restricted_Mw(p, n, zeta, g, K)
        labels = [int(zp[k % n]) for k in range(-K, K + 1) if k != 0]
        tot = 0.0
        rows = {}
        for Y in labels:
            for D in labels:
                if Y == D:
                    continue
                k = (1 - Y) * pow(1 - D, p - 2, p) % p
                if logt[k] > 0:
                    rows.setdefault(k, []).append((Y, D))
        w = g * (1 - g)
        for L in rows.values():
            for (Y, D) in L:
                for (A, C) in L:
                    if (A, C) == (Y, D):
                        continue
                    s = A * D * pow(C * Y, p - 2, p) % p
                    tot += g[logt[Y]] * g[logt[D]] * g[logt[A]] * g[logt[C]] * w[logt[s]]
        assert abs(MwI - tot) <= 1e-9 * max(1, tot), (MwI, tot)
        print(f"check p={p}: restricted M_w|I' (K'={K}) {MwI:.9f} == brute {tot:.9f}")
    print("CHECK OK")


if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == "--check":
        mode_check()
    elif len(sys.argv) >= 3 and sys.argv[1] == "laws":
        mode_laws([int(a) for a in sys.argv[2:]])
    elif len(sys.argv) >= 4 and sys.argv[1] == "jdist":
        mode_jdist(float(sys.argv[2]), [int(a) for a in sys.argv[3:]])
    else:
        print(__doc__)
