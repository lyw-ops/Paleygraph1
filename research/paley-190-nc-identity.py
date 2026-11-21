#!/usr/bin/env python3
r"""Round 190, call ordinary-nc-excludes-sector-laws: checks of Lemma 1 and models.

Part A (identity check, floating linear algebra at small p; the identity is proved
in the report for all p):
  Build, in character space Z/n (n = (p-1)/2), the matrices of Rounds 20/151/184
     K_{ij} = (1/n) sum_{x in Q} s(x) conj(psi^{i-j}(x)),  s(x) = chi(1-x),
     J = projection onto constants,  P = (I - J - rho K)/2   (Round 151: I - rho K = 2P + J),
     l = P e_0,  L = P - l l^T / l_0   (Round 20 / Round 151 definition of L_sigma),
  and check, for random b >= 0 with b_0 = 0, r = mean(b), f = sum_j nu_j psi^j, nu = b/sum b:
     ||L b||_{2,n}^2 / r^2  ==  V_{-rho} := sum_{x in T_{-rho}} |f(x) - mean_{T_{-rho}} f|^2,
  where ||v||_{2,n}^2 = (1/n) sum_j |v_j|^2 (normalized norm). Also checks K^2 = I - J,
  P^2 = P, and |sum_{T_{-rho}} f| <= (sqrt p + 1)/2.

Part B (models; floating; evidence only): diluted-interval laws D_theta, nu uniform on a
  random subset S of size round(m_0) of an interval J' of Z/n \ {0} of length m_0/theta.
  Printed: |S|/m_0, G/sqrt p, E(S)/|S|^3, max_{a!=0} r_S(a), Gamma_tot/sqrt p,
  K = floor(n/(2|J'|)) and min g on {gamma^{2k}: |k| <= K} (= I.I^{-1} for |I| = K+1),
  max fraction of S in one coset of a subgroup of Z/n of order <= 2 m_0,
  max relative g-mass on one coset of a multiplicative subgroup of order in [sqrt p/4, 4 sqrt p],
  and for each sign rho: G_{-rho}, V_{-rho}, number of points of the GP {|k|<=K} in T_{-rho}.

Usage:  .venv/bin/python -B research/paley-190-nc-identity.py --check
        .venv/bin/python -B research/paley-190-nc-identity.py P [P ...]
"""
import sys
import numpy as np


def is_prime(m):
    if m < 2:
        return False
    i = 2
    while i * i <= m:
        if m % i == 0:
            return False
        i += 1
    return True


def prim_root(p):
    fac, m, q = [], p - 1, 2
    while q * q <= m:
        if m % q == 0:
            fac.append(q)
            while m % q == 0:
                m //= q
        q += 1
    if m > 1:
        fac.append(m)
    for g in range(2, p):
        if all(pow(g, (p - 1) // q, p) != 1 for q in fac):
            return g
    raise ValueError


def setup(p):
    n = (p - 1) // 2
    gam = prim_root(p)
    g2 = gam * gam % p
    xs = np.empty(n, dtype=np.int64)
    x = 1
    for k in range(n):
        xs[k] = x
        x = x * g2 % p
    sq = np.zeros(p, dtype=np.int64)
    sq[(np.arange(1, p, dtype=np.int64) ** 2) % p] = 1
    chi = np.where(sq == 1, 1, -1)
    chi[0] = 0
    s = chi[(1 - xs) % p]          # s(x) = chi(1-x); s = 0 at k = 0 (x = 1)
    return n, gam, xs, s


def f_of_nu(nu):
    n = len(nu)
    return np.fft.ifft(nu) * n      # f(gamma^{2k}) = sum_j nu_j e(jk/n)


def part_a(primes, trials=5, seed=0):
    rng = np.random.default_rng(seed)
    worst = 0.0
    for p in primes:
        n, gam, xs, s = setup(p)
        k_idx = np.arange(n)
        # psi^d(x_k) = e(dk/n); K_{ij} = (1/n) sum_k s_k e(-(i-j)k/n)
        kd = np.array([np.sum(s * np.exp(-2j * np.pi * d * k_idx / n)) for d in range(n)]) / n
        K = np.empty((n, n), dtype=complex)
        for i in range(n):
            K[i] = kd[(i - np.arange(n)) % n]
        assert np.max(np.abs(K.imag)) < 1e-9, "k should be real"
        K = K.real
        I = np.eye(n)
        J = np.ones((n, n)) / n
        e1 = np.max(np.abs(K @ K - (I - J)))
        for rho in (1, -1):
            P = (I - J - rho * K) / 2
            e2 = np.max(np.abs(P @ P - P))
            l = P[:, 0].copy()
            L = P - np.outer(l, l) / l[0]
            Tm = (s == -rho)
            for _ in range(trials):
                b = rng.random(n) ** 3
                b[0] = 0.0
                r = b.mean()
                Lb = L @ b
                lhs = np.mean(Lb ** 2) / r ** 2
                nu = b / b.sum()
                f = f_of_nu(nu)
                fm = f[Tm].mean()
                V = np.sum(np.abs(f[Tm] - fm) ** 2)
                Gm = np.sum(np.abs(f[Tm]) ** 2)
                Psum = abs(f[Tm].sum())
                rel = abs(lhs - V) / max(V, 1e-300)
                worst = max(worst, rel)
                assert rel < 1e-8, (p, rho, lhs, V)
                assert Psum <= (np.sqrt(p) + 1) / 2 + 1e-9, (p, rho, Psum)
                assert Gm <= V + Psum ** 2 / Tm.sum() + 1e-9
            print(f"p={p} rho={rho:+d}: K^2=I-J err {e1:.1e}, P^2=P err {e2:.1e}, "
                  f"||Lb||^2/r^2 = V_(-rho) (rel err <= {worst:.1e}), |sum_T- f| <= (sqrt p+1)/2: OK")
    print("PART A: ALL IDENTITY CHECKS OK")


def part_b(p, thetas=(1.0, 0.75, 0.5, 0.25), seed=None):
    n, gam, xs, s = setup(p)
    m0 = n / np.sqrt(p)
    m = int(round(m0))
    rng = np.random.default_rng(p if seed is None else seed)
    rows = []
    divisors = [d for d in range(1, n + 1) if n % d == 0]
    for theta in thetas:
        Lp = int(round(m / theta))
        start = n // 3                       # interval J' = [start, start+Lp), away from 0
        Jp = np.arange(start, start + Lp)
        S = np.sort(rng.choice(Jp, size=m, replace=False))
        nu = np.zeros(n)
        nu[S] = 1.0 / m
        f = f_of_nu(nu)
        g = np.abs(f) ** 2
        G = g.sum()
        ind = np.zeros(n)
        ind[S] = 1.0
        F = np.fft.fft(ind)
        E = np.sum(np.abs(F) ** 4) / n
        auto = np.real(np.fft.ifft(np.abs(F) ** 2))
        auto[0] = 0
        rmax = auto.max() / m
        Gam = np.sum(g ** 2)
        K = n // (2 * Lp)
        ks = np.r_[0:K + 1, n - K:n]
        ming = g[ks].min()
        # coset fractions in Z/n for subgroups of order e <= 2 m0  (H = multiples of n/e)
        cf = 0.0
        for e in divisors:
            if e <= 2 * m0 and e > 1:
                step = n // e
                cnt = np.bincount(S % step, minlength=step)
                cf = max(cf, cnt.max() / m)
        # multiplicative cosets of order d in [sqrt p/4, 4 sqrt p]: log-index k = c mod n/d
        mc = 0.0
        for d in divisors:
            if np.sqrt(p) / 4 <= d <= 4 * np.sqrt(p):
                step = n // d
                sums = np.bincount(np.arange(n) % step, weights=g, minlength=step)
                mc = max(mc, sums.max() / G)
        sect = []
        for rho in (1, -1):
            Tm = (s == -rho)
            Gm = g[Tm].sum()
            V = np.sum(np.abs(f[Tm] - f[Tm].mean()) ** 2)
            bad = int(np.sum(s[ks] == -rho))
            sect.append((rho, Gm, V, bad))
        rows.append((theta, m / m0, G / np.sqrt(p), E / m ** 3, rmax, Gam / np.sqrt(p), K,
                     ming, cf, mc, sect))
    for (theta, sm, Gs, Er, rmax, Gt, K, ming, cf, mc, sect) in rows:
        sc = "; ".join(f"rho={r:+d}: G_-rho={Gm:.1f} V={V:.1f} bad={bad}/{2*K}" for (r, Gm, V, bad) in sect)
        print(f"p={p} theta={theta:.2f} |S|/m0={sm:.3f} G/sqrtp={Gs:.3f} E/|S|^3={Er:.3f} "
              f"max r_S={rmax:.3f} Gamma_tot/sqrtp={Gt:.3f} K={K} (K/sqrtp={K/np.sqrt(p):.3f}) "
              f"min g on GP={ming:.3f} cosetfrac(Z/n)={cf:.3f} cosetmass(Q)={mc:.3f} | {sc}")


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args or args[0] == "--check":
        part_a([13, 17, 29, 37, 41, 53, 61, 101, 109, 197])
    else:
        for a in args:
            p = int(a)
            assert is_prime(p) and p % 4 == 1
            part_b(p)
