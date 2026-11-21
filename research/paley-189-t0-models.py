#!/usr/bin/env python3
"""Round 189 (ordinary-prime-intercept-fibre-t0): floating-point models.
Evidence only; small p cannot test an exponent.

For each law it computes, in the kappa form of the report (section 1):
  X      = sum_{beta in Q, beta != 1} c(beta)^2           (= Lambda_0, Lemma A1)
  c      = sum mu^2
  T0     = sum_k sum_e c_e(k) A_e(k) - Z                (= sum_l g(l) Delta(l,0))
  SA2    = sum_{k != 1} sum_e A_e(k)^2                   (triangle-restricted energy)
  CPL    = sum_{k != 1} sum_e c_e(k) min(c_e(k), c_e(1-k), c_{chi(k)e}(1-1/k))
  ICR    = sum_{k != 1} sum_e c_e(k) c_e(1-k)            (anharmonic cross sum)
  D0     = max_{l != 1} Delta(l,0)
  T3     = sum_{x,y} g(x) g(y) g(y/x)                    (multiplicative triangles)
Laws (nu flat on S subset Z/n, |S| ~ n/sqrt p, g = |f|^2): rand, interval,
halfint; controls: gp01 = indicator of a symmetric geometric progression in Q of
length ~ sqrt p (inversion symmetric, not of the form |f|^2), subgroup laws
g = 1_H when (p-1)/2 has a divisor d in [sqrt p / 2, 2 sqrt p].

Run: .venv/bin/python -B research/paley-189-t0-models.py 401 809 1601 3209
"""
import math
import sys

import numpy as np


def prime_factors(n):
    out, q = [], 2
    while q * q <= n:
        if n % q == 0:
            out.append(q)
            while n % q == 0:
                n //= q
        q += 1
    if n > 1:
        out.append(n)
    return out


def setup(p):
    for gen in range(2, p):
        if all(pow(gen, (p - 1) // q, p) != 1 for q in prime_factors(p - 1)):
            break
    n = (p - 1) // 2
    g2 = gen * gen % p
    qelts = np.zeros(n, dtype=np.int64)
    x = 1
    for k in range(n):
        qelts[k] = x
        x = x * g2 % p
    chi = -np.ones(p, dtype=np.int64)
    chi[0] = 0
    chi[qelts] = 1
    inv = np.array([0] + [pow(int(x), p - 2, p) for x in range(1, p)], dtype=np.int64)
    return n, qelts, chi, inv


def law_g(p, n, qelts, S):
    nu = np.zeros(n)
    nu[S] = 1.0 / len(S)
    f = np.fft.ifft(nu) * n  # f(gamma^{2k}) = sum_j nu_j e(jk/n) up to orientation
    g = np.zeros(p)
    g[qelts] = np.abs(f) ** 2
    g[1] = 1.0
    return g


def quantities(p, g, chi, inv):
    xs = np.arange(p)
    psi = np.zeros(p)
    psi[1:] = g[(1 + xs[1:]) % p]
    supp = np.nonzero(psi)[0]
    cls = chi[supp]
    cE = {1: np.zeros(p), -1: np.zeros(p)}
    AE = {1: np.zeros(p), -1: np.zeros(p)}
    for k in range(1, p):
        kz = k * supp % p
        w = psi[supp] * psi[kz]
        ratio = (1 + kz) * inv[(1 + supp) % p] % p
        wa = w * g[ratio]
        for e in (1, -1):
            msk = cls == e
            cE[e][k] = w[msk].sum()
            AE[e][k] = wa[msk].sum()
    ctot = cE[1] + cE[-1]
    X = sum(ctot[b] ** 2 for b in range(2, p) if chi[b] == 1)
    # Z term
    a = psi[supp] ** 2
    Z = 0.0
    for i, x in enumerate(supp):
        Z += a[i] * (a * g[(1 + x) * inv[(1 + supp) % p] % p]).sum()
    T0 = sum((cE[e] * AE[e]).sum() for e in (1, -1)) - Z
    c = sum(cE[e][1] ** 2 for e in (1, -1)) - (psi ** 4).sum()
    ks = np.arange(2, p)
    SA2 = sum((AE[e][ks] ** 2).sum() for e in (1, -1))
    one_minus = (1 - ks) % p
    third = (1 - inv[ks]) % p
    CPL = 0.0
    ICR = 0.0
    for e in (1, -1):
        c3 = np.where(chi[ks] == 1, cE[e][third], cE[-e][third])
        m3 = np.minimum(np.minimum(cE[e][ks], cE[e][one_minus]), c3)
        CPL += (cE[e][ks] * m3).sum()
        ICR += (cE[e][ks] * cE[e][one_minus]).sum()
    # Delta(l,0) = sum_x psi(x) psi(x') [c_{chi(x)}(x'/x) - psi(x)psi(x')], 1+x' = (1+x)/l
    D0 = 0.0
    arg = 1
    for l in range(2, p):
        xp = ((1 + supp) * inv[l] - 1) % p
        ok = psi[xp] > 0
        if not ok.any():
            continue
        xx = supp[ok]
        xq = xp[ok]
        kap = xq * inv[xx] % p
        cc = np.where(chi[xx] == 1, cE[1][kap], cE[-1][kap])
        val = (psi[xx] * psi[xq] * (cc - psi[xx] * psi[xq])).sum()
        if val > D0:
            D0, arg = val, l
    # T3
    T3 = 0.0
    gs = np.nonzero(g)[0]
    for x in gs:
        T3 += g[x] * (g[gs] * g[gs * inv[x] % p]).sum()
    G = g.sum()
    Gam = (g ** 2).sum()
    return dict(G=G, Gam=Gam, X=X, c=c, T0=T0, SA2=SA2, CPL=CPL, ICR=ICR, D0=D0, argD0=arg, T3=T3)


def laws(p, n, qelts, rng):
    m = max(2, round(n / math.sqrt(p)))
    out = {}
    out["rand"] = law_g(p, n, qelts, rng.choice(n, m, replace=False))
    out["interval"] = law_g(p, n, qelts, np.arange(m))
    half = rng.choice(2 * m, m, replace=False)
    out["halfint"] = law_g(p, n, qelts, half)
    # gp01: symmetric GP in Q of length ~ sqrt p
    L = int(round(math.sqrt(p) / 2))
    g = np.zeros(p)
    g[qelts[np.r_[0:L + 1, n - L:n]]] = 1.0
    out["gp01"] = g
    for d in range(int(math.sqrt(p) / 2), int(2 * math.sqrt(p)) + 1):
        if n % d == 0:
            g = np.zeros(p)
            g[qelts[:: n // d]] = 1.0
            out[f"subgroup{d}"] = g
            break
    return out


def main():
    primes = [int(a) for a in sys.argv[1:]] or [401, 809]
    print("model, p | G/sqrt p  Gam/sqrt p | X/p  c/p  (T0-c)/p  (T0-c)/(X-c) | SA2/p^(5/4)  CS=sqrt(SA2 X)/(T0-c) | CPL/(T0-c)  ICR/X | D0/sqrt p  T3/p")
    for p in primes:
        rng = np.random.default_rng(p)
        n, qelts, chi, inv = setup(p)
        for name, g in laws(p, n, qelts, rng).items():
            q = quantities(p, g, chi, inv)
            t0c = q["T0"] - q["c"]
            print(f"{name:12s} {p:5d} | {q['G'] / math.sqrt(p):6.3f} {q['Gam'] / math.sqrt(p):6.3f} | {q['X'] / p:6.3f} {q['c'] / p:6.3f} {t0c / p:7.4f} {t0c / max(q['X'] - q['c'], 1e-12):6.3f} | {q['SA2'] / p ** 1.25:7.4f} {math.sqrt(q['SA2'] * q['X']) / max(t0c, 1e-12):7.2f} | {q['CPL'] / max(t0c, 1e-12):6.2f} {q['ICR'] / q['X']:6.3f} | {q['D0'] / math.sqrt(p):6.3f} {q['T3'] / p:6.3f}", flush=True)


if __name__ == "__main__":
    main()
