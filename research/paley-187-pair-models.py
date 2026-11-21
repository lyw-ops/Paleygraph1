#!/usr/bin/env python3
r"""Round 187, call ordinary-prime-level-pair-energy: floating-point models (EVIDENCE ONLY).

For a prime p = 1 mod 4 (default about 10^7) and tailored laws nu on the character group of Q
(cap n max nu <= sqrt p), compute g = |f|^2 on Q and, at heights a = p^{-e} with e visibly
positive (up to 1/6), the following quantities, all by FFT over Z/(p-1) in discrete-log
coordinates (floating point; not certificates):

  * |S_a|, K(S_a) = |S_a|^3 / E^x(S_a)  and the Lemma S1 bound  K <= n max nu / (a^2 |S_a|);
  * the (HC') ratio  E(S_a;S_a') (a a')^2 / p^{4/3}  for all pairs of heights;
  * the Lemma M' ingredients for R = S_a (popular-quotient class F, P, |B|, the guaranteed
    |B| >= m/(4 L0 sqrt K)) and the ratio  E(S_a';B) / T1  with
    T1 = alpha^{4/3}|B|^{2/3}K^{2/3}m^{1/3}alpha^{1/3}  (constant and logs dropped);
  * E^x(h) for h(z) = g(1-z), normalised by p and by p^{4/3}.

Laws (all satisfy n max nu <= sqrt p):
  dir      nu uniform on an interval [0, Lw) of characters (level sets are log-intervals);
  dir2d    nu uniform on a 2-dimensional progression l1 + T l2 (Bohr-type level sets);
  blocksR  nu uniform on R random translates of an interval of length Lw/R (default R = 8)
           (g is about |P|^2/... with a random R-term polynomial P on a log-interval of length
           about R sqrt p: level sets at height about 1/R have the extremal size sqrt p / a);
  dirmix   1/2 dir + 1/2 uniform on a random set of size Lw.

Usage: .venv/bin/python -B research/paley-187-pair-models.py [p] [law ...]
       .venv/bin/python -B research/paley-187-pair-models.py --adversarial [p ...]
         (Lemma M' against an adversarial partner: R a log-interval, 1-A a log-interval
          of the same ratio, so that E(A;B) is as large as the multiplicative structure allows)
"""
import math
import sys
import time

import numpy as np


def is_prime(n):
    if n < 2:
        return False
    for q in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % q == 0:
            return n == q
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def factor(n):
    fs, d = [], 2
    while d * d <= n:
        if n % d == 0:
            fs.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        fs.append(n)
    return fs


def setup(p):
    fs = factor(p - 1)
    g0 = next(g for g in range(2, p) if all(pow(g, (p - 1) // q, p) != 1 for q in fs))
    # powers g0^k, k = 0..p-2, vectorised in blocks
    B = 1 << 12
    first = np.empty(B, dtype=np.int64)
    x = 1
    for i in range(B):
        first[i] = x
        x = x * g0 % p
    step = x  # g0^B
    pw = np.empty(p - 1, dtype=np.int64)
    cur = first.copy()
    for start in range(0, p - 1, B):
        end = min(start + B, p - 1)
        pw[start:end] = cur[: end - start]
        cur = cur * step % p
    dlog = np.empty(p, dtype=np.int64)
    dlog[pw] = np.arange(p - 1, dtype=np.int64)
    dlog[0] = -1
    return g0, pw, dlog


def law(name, n, p, rng):
    Lw = int(math.ceil(n / math.sqrt(p)))
    nu = np.zeros(n)
    if name == "dir":
        nu[:Lw] = 1.0
    elif name == "dir2d":
        L1 = int(math.ceil(math.sqrt(Lw)))
        L2 = int(math.ceil(Lw / L1))
        T = int(rng.integers(n // 7, n // 3))
        idx = (np.arange(L1)[:, None] + T * np.arange(L2)[None, :]).ravel() % n
        nu[np.unique(idx)] = 1.0
    elif name.startswith("blocks"):
        r = int(name[6:] or 8)
        Lb = int(math.ceil(Lw / r))
        for s in rng.integers(0, n, size=r):
            nu[(s + np.arange(Lb)) % n] = 1.0
    elif name == "dirmix":
        nu[:Lw] += 1.0 / Lw
        idx = rng.choice(n, size=Lw, replace=False)
        nu[idx] += 1.0 / Lw
        nu /= nu.sum()
        return nu
    else:
        raise ValueError(name)
    nu /= nu.sum()
    return nu


def corr_energy(ind1, ind2):
    """sum_k (1_{L1} star 1_{L2})(k)^2 over Z/(p-1): mixed (additive) energy of exponent sets."""
    f1 = np.fft.rfft(ind1)
    f2 = np.fft.rfft(ind2)
    N = len(ind1)
    c = np.fft.irfft(f1 * np.conj(f2), n=N)
    return float(np.dot(c, c)), c


def lemma_terms(A_ks, R_ks, Lsh, N, p):
    """Lemma M' quantities for exponent sets A_ks (the set A as dlogs) and R_ks (R as dlogs)."""
    m = len(R_ks)
    ind = np.zeros(N)
    ind[R_ks] = 1.0
    Emult, rcorr = corr_energy(ind, ind)
    K = m ** 3 / Emult
    r = np.rint(rcorr).astype(np.int64)
    L0 = int(m).bit_length()
    pos = r > 0
    j = np.zeros_like(r)
    j[pos] = np.floor(np.log2(r[pos])).astype(np.int64)
    best, bestS = None, -1.0
    for jj in np.unique(j[pos]):
        sel = pos & (j == jj)
        S = float((r[sel].astype(np.float64) ** 2).sum())
        if S > bestS:
            best, bestS = jj, S
    Fsel = pos & (j == best)
    P = float(r[Fsel].sum())
    dconv = np.fft.irfft(np.fft.rfft(ind) * np.fft.rfft(Fsel.astype(np.float64)), n=N)
    d = np.rint(dconv[R_ks]).astype(np.int64)
    Bks = R_ks[2 * m * d >= P]
    nb = len(Bks)
    shA = np.zeros(N)
    shA[Lsh[A_ks]] = 1.0
    shB = np.zeros(N)
    shB[Lsh[Bks]] = 1.0
    EAB, _ = corr_energy(shA, shB)
    alpha = len(A_ks)
    T1 = alpha ** (5 / 3) * nb ** (2 / 3) * K ** (2 / 3) * m ** (1 / 3)
    T2 = K * alpha * nb
    T3 = alpha ** 2 * nb * math.sqrt(K * m / p)
    return dict(m=m, K=K, B=nb, EAB=EAB, ratio=EAB / (T1 + T2 + T3), triv=EAB / (alpha * nb * min(alpha, nb)))


def adversarial(p):
    """R a log-interval (K small); A with 1-A a log-interval of the same ratio (adversarial partner)."""
    while not (is_prime(p) and p % 4 == 1):
        p += 1
    g0, pw, dlog = setup(p)
    N = p - 1
    oneminus = (1 - pw) % p
    Lsh = dlog[oneminus]
    print(f"\n== adversarial Lemma M' test, p = {p} (EVIDENCE ONLY) ==")
    for th in (0.5, 0.55, 0.6, 0.65):
        m = int(p ** th)
        R_ks = np.arange(1, m + 1, dtype=np.int64)            # R = {g0^k : 1 <= k <= m}
        # A = {x : 1 - x = g0^k, 1 <= k <= m}, i.e. dlog(x) for x = 1 - g0^k
        xs = (1 - pw[1:m + 1]) % p
        A_ks = dlog[xs]
        A_ks = A_ks[(A_ks > 0)]                                # drop x = 1 (cannot occur) and x = 0
        for name, Aset in (("A=R", R_ks), ("1-A=log-interval", A_ks)):
            t = lemma_terms(Aset, R_ks, Lsh, N, p)
            print(f"   m=p^{th:.2f}={t['m']:7d} {name:17s} K={t['K']:.3f} |B|/m={t['B'] / t['m']:.3f} "
                  f"E(A;B)={t['EAB']:.4g}  E/(T1+T2+T3)={t['ratio']:.3e}  E/(|A||B|min)={t['triv']:.3e}")


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--adversarial":
        for p in [int(a) for a in sys.argv[2:]] or [100049, 1000033, 10000189]:
            adversarial(p)
        return
    p = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 10000189
    laws = [a for a in sys.argv[1:] if not a.isdigit()] or ["dir", "dir2d", "blocks4", "blocks8", "blocks16", "dirmix"]
    while not (is_prime(p) and p % 4 == 1):
        p += 1
    t0 = time.time()
    g0, pw, dlog = setup(p)
    n = (p - 1) // 2
    N = p - 1
    print(f"p = {p}, n = {n}, g0 = {g0}, setup {time.time() - t0:.1f}s")
    rng = np.random.default_rng(187)
    es = [0.02, 0.05, 0.08, 0.11, 0.14, 1 / 6]
    for name in laws:
        nu = law(name, n, p, rng)
        capratio = n * nu.max() / math.sqrt(p)
        f = np.fft.ifft(nu) * n          # f(j) = sum_l nu_l e(l j / n), on x = g0^{2j}
        gQ = np.abs(f) ** 2
        G = gQ.sum()
        # g on F_p^x in exponent coordinates k (x = g0^k): g = gQ[k/2] for even k
        gexp = np.zeros(N)
        gexp[0::2] = gQ
        gexp[0] = 0.0                    # exclude x = 1 from level sets / h (h(0) not defined)
        # level sets S_a = {x != 1 : g(x) >= a}, as exponent indicators and as residues
        print(f"\n== law {name}: n max nu / sqrt p = {capratio:.3f}, G/sqrt p = {G / math.sqrt(p):.3f}, "
              f"g(1) = {gQ[0]:.3f}")
        # shifted exponent map: x -> log(1-x)
        oneminus = (1 - pw) % p                       # 1 - g0^k
        Lsh = dlog[oneminus]                          # -1 where 1-x = 0 (k=0)
        sets = {}
        for e in es:
            a = p ** (-e)
            ks = np.nonzero(gexp >= a)[0]
            if len(ks) == 0:
                continue
            sets[e] = (a, ks)
        # h(z) = g(1-z): in exponent coordinates of z, H[l] = g(1 - g0^l)
        H = np.zeros(N)
        valid = Lsh >= 0
        H[Lsh[valid]] = gexp[np.nonzero(valid)[0]]
        Eh, _ = corr_energy(H, H)
        print(f"   E^x(h) = {Eh:.4g} = {Eh / p:.3f} p = {Eh / p ** (4 / 3):.4f} p^(4/3)")
        rows = []
        for e, (a, ks) in sets.items():
            ind = np.zeros(N)
            ind[ks] = 1.0
            m = len(ks)
            Emult, rcorr = corr_energy(ind, ind)       # E^x(S_a) and r(w) (w in exponent coords)
            K = m ** 3 / Emult
            Kbound = n * nu.max() / (a * a * m)
            # shifted indicator 1_{1-S_a} in exponent coordinates
            sh = np.zeros(N)
            sh[Lsh[ks]] = 1.0
            sets[e] = (a, ks, ind, sh, K, rcorr)
            rows.append((e, a, m, K, Kbound))
        for e, a, m, K, Kb in rows:
            print(f"   e={e:.4f} a={a:.4f} |S_a|={m:7d} (|S_a| a/sqrt p = {m * a / math.sqrt(p):.3f})"
                  f"  K={K:8.3f}  S1 bound {Kb:9.3f}")
        print("   (HC') ratios E(S_a;S_a') (a a')^2 / p^(4/3):")
        keys = sorted(sets)
        worst = 0.0
        for i, e1 in enumerate(keys):
            for e2 in keys[i:]:
                a1, _, _, sh1, _, _ = sets[e1]
                a2, _, _, sh2, _, _ = sets[e2]
                Epair, _ = corr_energy(sh1, sh2)
                ratio = Epair * (a1 * a2) ** 2 / p ** (4 / 3)
                worst = max(worst, ratio)
                print(f"      e=({e1:.3f},{e2:.3f})  E={Epair:.4g}  E/(|U||U'|)={Epair / (sh1.sum() * sh2.sum()):.3f}"
                      f"  ratio={ratio:.5f}")
        print(f"   max (HC') ratio = {worst:.5f}")
        print("   Lemma M' ingredients (R = S_a; partner A = S_a' with the largest set):")
        eA = max(keys)
        aA, ksA, indA, shA, _, _ = sets[eA]
        alpha = len(ksA)
        for e in keys:
            a, ks, ind, sh, K, rcorr = sets[e]
            m = len(ks)
            r = np.rint(rcorr).astype(np.int64)
            E = float((r.astype(np.float64) ** 2).sum())
            L0 = int(m).bit_length()
            pos = r > 0
            j = np.zeros_like(r)
            j[pos] = np.floor(np.log2(r[pos])).astype(np.int64)
            best, bestS = None, -1.0
            for jj in np.unique(j[pos]):
                sel = pos & (j == jj)
                S = float((r[sel].astype(np.float64) ** 2).sum())
                if S > bestS:
                    best, bestS = jj, S
            Fsel = pos & (j == best)
            Fsize = int(Fsel.sum())
            P = float(r[Fsel].sum())
            # d(y) = #{y' in R : y - y' in F} (exponent coordinates) = (1_R * 1_F)(y)
            dconv = np.fft.irfft(np.fft.rfft(ind) * np.fft.rfft(Fsel.astype(np.float64)), n=N)
            d = np.rint(dconv[ks]).astype(np.int64)
            Bmask = 2 * m * d >= P
            Bks = ks[Bmask]
            nb = len(Bks)
            guaranteed = m / (4 * L0 * math.sqrt(K))
            shB = np.zeros(N)
            shB[Lsh[Bks]] = 1.0
            EAB, _ = corr_energy(shA, shB)
            T1 = alpha ** (5 / 3) * nb ** (2 / 3) * K ** (2 / 3) * m ** (1 / 3)
            print(f"      e={e:.3f}: m={m} K={K:.2f} rho=2^{best} |F|={Fsize} (|F|/(K m)={Fsize / (K * m):.3f})"
                  f" eta=P/m^2={P / m / m:.3f} |B|/m={nb / m:.3f} (guaranteed {guaranteed / m:.4f})"
                  f"  E(A;B)/T1={EAB / T1:.3e}")
    print(f"\nEVIDENCE ONLY (floating point). total {time.time() - t0:.1f}s")


if __name__ == "__main__":
    main()
