#!/usr/bin/env python3
"""Round 183 (call ordinary-prime-first-mass-fibre-dilation): model computations.

FLOATING EVIDENCE ONLY (numpy float64 FFTs).  Nothing here is about the actual
near-critical optimiser; every model is an admissible g = |f|^2 with
f = sum_eta nu_eta eta on Q, nu a probability on the characters of Q (so
g(1) = 1, 0 <= g <= 1, supp g in Q, g positive definite on Q), and the printed
cap ratio n*max(nu)/sqrt(p).

For each model the script computes, on the Round 171 chart (mu(r,b) = g(Y)g(D),
mask b in Q, Y != D), slope fibre by slope fibre (kappa = 1 - r in Q\\{1}):
  m(kappa)      fibre mass,  |nu_kappa|_2^2,
  M_w(kappa)  = sum_{b != b'} mu(r,b) mu(r,b') w(b/b')   (w = g(1-g) KEPT),
  E^x(nu_kappa) per-fibre multiplicative energy,
and in aggregate
  M_w, E_off = sum_kappa (m^2 - |nu|^2), the w-saving factor M_w / (E_off/4),
  the bounded-fibre split of Proposition B (share of M_w from fibres with m <= tau),
  the spectral restriction of M_w to Spec_theta(w) = {chi : |w^(chi)| >= p^-theta w^(1)}
  (Round 182 Proposition 2 form, w kept), max Phi on the spectrum,
  the per-fibre Hoelder bound |w|_2 * sum_kappa E^x(nu_kappa)^(1/2).

Models (c = target cap ratio):
  dir   nu uniform on an interval of L characters (g = Fejer-type kernel |D_L/L|^2)
  fej   nu triangular on (-L, L)       (f = Fejer kernel >= 0, g = Fejer^2)
  sub   g_H = delta_1 + (1/4) 1_{H minus 1}, nu = (1/2)unif(H^perp) + (1/2)unif(Q^)
  mix2  nu = (1/2)unif(H1^perp) + (1/2)unif(H2^perp), |H1|,|H2| ~ sqrt p, gcd small
  cosfej nu triangular on the multiples of s (g periodic under the subgroup of
        order s; a smeared coset H_s * P, |H_s| ~ p^(1/4), |P| ~ c p^(1/4))

Replay (about 9 minutes and 3.2 GB peak for the six default-plus-80000 targets; seconds for 2000,5000):
  .venv/bin/python -B research/paley-183-fibre-models.py
Optional argument: comma-separated target primes (default 2000,5000,10000,20000,40000).
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
    out = []
    i = 1
    while i * i <= m:
        if m % i == 0:
            out.append(i)
            out.append(m // i)
        i += 1
    return sorted(set(out))


def prim_root(p):
    m = p - 1
    fs = [q for q in divisors(m) if q > 1 and is_prime(q)]
    return next(c for c in range(2, p) if all(pow(c, m // q, p) != 1 for q in fs))


def find_prime(target, ok):
    q = target
    while True:
        if q % 4 == 1 and is_prime(q) and ok(q):
            return q
        q += 1


class Field:
    def __init__(self, p):
        self.p = p
        self.n = (p - 1) // 2
        th = prim_root(p)
        L = np.zeros(p, dtype=np.int64)
        x = 1
        for k in range(p - 1):
            L[x] = k
            x = x * th % p
        self.qx = np.array([pow(th, 2 * j, p) for j in range(self.n)], dtype=np.int64)
        jidx = -np.ones(p, dtype=np.int64)
        jidx[self.qx] = np.arange(self.n)
        self.jidx = jidx            # index of x in Q (x = theta^(2j)), -1 off Q


def g_from_nu(F, nu):
    f = np.fft.ifft(nu) * F.n      # f(theta^(2j)) = sum_a nu_a e(aj/n)
    g = np.abs(f) ** 2
    return g


def analyse(F, gQ, label, capratio):
    p, n = F.p, F.n
    gQ = np.clip(gQ, 0.0, 1.0)
    gQ[0] = 1.0
    gF = np.zeros(p)
    gF[F.qx] = gQ
    wQ = gQ * (1 - gQ)
    wQ[0] = 0.0
    W = np.fft.fft(wQ)
    G = gQ.sum()
    Gam2 = (gQ[1:] ** 2).sum()
    supp = np.nonzero(gQ[1:] > 1e-14)[0] + 1   # j indices of D in supp, D != 1
    Dx = F.qx[supp]
    jD = supp
    gD = gQ[supp]
    Phi = np.zeros(n)
    ms, nu2s, mws, exs, nsupp = [], [], [], [], []
    B = max(1, int(4_000_000 // max(1, len(supp))))
    B = min(B, 512)
    kap_j = np.arange(1, n)
    for st in range(0, len(kap_j), B):
        kj = kap_j[st:st + B]
        kx = F.qx[kj]
        Y = (kx[:, None] * Dx[None, :] + 1 - kx[:, None]) % p
        jY = F.jidx[Y]
        valid = jY >= 0
        mu = np.where(valid, gF[Y] * gD[None, :], 0.0)
        jb = (kj[:, None] + jD[None, :] - jY) % n
        rows = np.arange(len(kj))[:, None] * n + jb
        V = np.bincount(rows[valid], weights=mu[valid], minlength=len(kj) * n).reshape(len(kj), n)
        Vh = np.fft.fft(V, axis=1)
        P2 = (Vh.real ** 2 + Vh.imag ** 2)
        Phi += P2.sum(0)
        ms.append(V.sum(1))
        nu2s.append((V * V).sum(1))
        mws.append((P2 @ W).real / n)
        exs.append((P2 * P2).sum(1) / n)
        mx = V.max(1, keepdims=True)
        nsupp.append((V >= 0.01 * np.maximum(mx, 1e-300)).sum(1) * (mx[:, 0] > 0))
    m = np.concatenate(ms)
    nu2 = np.concatenate(nu2s)
    mwk = np.concatenate(mws)
    exk = np.concatenate(exs)
    ns = np.concatenate(nsupp)
    Mw = (Phi * W).real.sum() / n
    Eoff = (m * m - nu2).sum()
    M1 = m.sum()
    out = {}
    out["Mw"] = Mw
    out["Mw_rows"] = mwk.sum()
    out["ratio"] = Mw / (Eoff / 4) if Eoff > 0 else float("nan")
    out["G"] = G
    out["Gam2"] = Gam2
    out["M1"] = M1
    out["Eoff"] = Eoff
    out["maxm"] = m.max()
    out["argmax_size"] = int(ns[np.argmax(m)])
    out["share"] = {t: mwk[m <= t].sum() / Mw if Mw > 0 else float("nan") for t in (1, 2, 4, 8)}
    out["rich"] = {t: (m[m > t] ** 2).sum() for t in (1, 2, 4)}
    wn2 = math.sqrt((wQ ** 2).sum())
    out["hold"] = wn2 * np.sqrt(np.maximum(exk, 0)).sum()
    spec = {}
    for th in (0.125, 0.25):
        S = np.abs(W) >= p ** (-th) * W[0].real
        part = (Phi[S] * W[S]).real.sum() / n
        S1 = S.copy()
        S1[0] = False
        mxphi = Phi[S1].max() if S1.any() else 0.0
        spec[th] = (int(S.sum()), part / Mw if Mw > 0 else float("nan"), mxphi / Phi[0], mxphi / math.sqrt(p))
    out["spec"] = spec
    # consistency: row sum equals spectral sum
    assert abs(out["Mw"] - out["Mw_rows"]) <= 1e-6 * max(1.0, abs(out["Mw"]))
    sp = ";".join(f"th={th:.3f}:|S|={v[0]},share={v[1]:.3f},maxPhi/Phi0={v[2]:.3f},maxPhi/sqrtp={v[3]:.1f}"
                  for th, v in spec.items())
    print(f"{label:<14} p={p:6d} cap={capratio:5.2f} G/sqrtp={G/math.sqrt(p):5.3f} Gam2/sqrtp={Gam2/math.sqrt(p):5.3f} "
          f"M_w/p={Mw/p:8.5f} (E_off/4)/p={Eoff/4/p:8.5f} saving={out['ratio']:6.3f} "
          f"maxm={out['maxm']:6.3f}[{out['argmax_size']}] "
          f"share(m<=1,2,4,8)={out['share'][1]:.3f},{out['share'][2]:.3f},{out['share'][4]:.3f},{out['share'][8]:.3f} "
          f"rich(m>2)/p={out['rich'][2]/p:8.5f} Hold/p={out['hold']/p:7.3f} | {sp}", flush=True)
    return out


def near_div(m, x, lo=0.8, hi=1.25):
    ds = [d for d in divisors(m) if lo * x <= d <= hi * x]
    return ds


def run(targets):
    print("model          p  cap = n*max(nu)/sqrt p ; saving = M_w/(E_off/4) ; [k] = #entries >= 1% of max on the heaviest fibre")
    for T in targets:
        # dense Fejer-type models
        p = find_prime(T, lambda q: True)
        F = Field(p)
        n = F.n
        for c in (0.5, 1.0):
            L = max(2, round(n / (c * math.sqrt(p))))
            nu = np.zeros(n)
            nu[:L] = 1.0 / L
            analyse(F, g_from_nu(F, nu), f"dir c={c}", n * nu.max() / math.sqrt(p))
            nu = np.zeros(n)
            a = np.arange(-L + 1, L)
            nu[a % n] = (L - np.abs(a)).astype(float)
            nu /= nu.sum()
            analyse(F, g_from_nu(F, nu), f"fej c={c}", n * nu.max() / math.sqrt(p))
        # exact subgroup family g_H and mixtures
        for c in (0.5, 1.0, 2.0):
            p = find_prime(T, lambda q: len(near_div((q - 1) // 2, c * math.sqrt(q), 0.9, 1.12)) > 0)
            F = Field(p)
            n = F.n
            d = near_div(n, c * math.sqrt(p), 0.9, 1.12)[0]
            gQ = np.zeros(n)
            gQ[:: n // d] = 0.25
            gQ[0] = 1.0
            analyse(F, gQ, f"sub |H|={d}", (d + 1) / 2 / math.sqrt(p))
        def ok2(q):
            ds = near_div((q - 1) // 2, math.sqrt(q), 0.7, 1.4)
            return any(math.gcd(a, b) <= 2 for a in ds for b in ds if a < b)
        p = find_prime(T, ok2)
        F = Field(p)
        n = F.n
        ds = near_div(n, math.sqrt(p), 0.7, 1.4)
        d1, d2 = next((a, b) for a in ds for b in ds if a < b and math.gcd(a, b) <= 2)
        nu = np.zeros(n)
        nu[np.arange(0, n, d1)] += 0.5 / (n // d1)   # H1^perp = multiples of d1, |H1| = d1
        nu[np.arange(0, n, d2)] += 0.5 / (n // d2)
        # characters a with a*j = 0 for j in (n/d)Z are the multiples of d, so H^perp = dZ/n
        # has n/d elements and f = 1_H with |H| = d.
        analyse(F, g_from_nu(F, nu), f"mix2 {d1},{d2}", n * nu.max() / math.sqrt(p))
        # smeared coset: triangle on multiples of s
        for c in (0.5, 1.0):
            p = find_prime(T, lambda q: len(near_div((q - 1) // 2, q ** 0.25, 0.8, 1.3)) > 0)
            F = Field(p)
            n = F.n
            s = near_div(n, p ** 0.25, 0.8, 1.3)[0]
            Lp = max(2, round(n / (c * math.sqrt(p))))
            if Lp >= n // (2 * s):
                continue
            nu = np.zeros(n)
            t = np.arange(-Lp + 1, Lp)
            nu[(s * t) % n] = (Lp - np.abs(t)).astype(float)
            nu /= nu.sum()
            analyse(F, g_from_nu(F, nu), f"cosfej s={s} c={c}", n * nu.max() / math.sqrt(p))


if __name__ == "__main__":
    tg = [2000, 5000, 10000, 20000, 40000]
    if len(sys.argv) > 1:
        tg = [int(x) for x in sys.argv[1].split(",")]
    run(tg)
