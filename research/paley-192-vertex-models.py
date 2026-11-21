#!/usr/bin/env python3
"""Round 192, call ordinary-nc-vertex-tightness: model evidence (floating point).

EVIDENCE ONLY.  None of these laws is near-critical in the sense of (NC); the
point of each part is stated in the report
research/native-claude-ordinary-nc-vertex-tightness-192.md, section 5.

Part A  sector-free families (random flat law, diluted intervals D_theta):
        vertex mass below fixed levels on T_rho for both signs, sup g,
        sum g^2, the uncertainty product |S||Lambda_a|/n.
Part B  the two-subgroup sharp family (Proposition D): search for primes
        p = 1 mod 4 with divisors h1, h2 of n = (p-1)/2, h1 + h2 ~ m_0,
        h1/h2 ~ 1, gcd small; then the exact level structure, the sector-free
        (NC) diagnostics (flatness, energy, overlap dichotomy, single-coset mass,
        coset mass t_B) and the sector diagnostics (G_{-rho}, bad points of
        Gamma_i versus Lemma J) with the actual Legendre symbol.

Conventions: Q = <gamma^2>, x = gamma^(2k) <-> k in Z/n; psi^j(x) = e(jk/n);
f(x) = sum_j nu_j psi^j(x) (computed as n*ifft(nu)), g = |f|^2;
T_eps = {x in Q\\{1}: chi(1-x) = eps}; m_<a(T_rho) = sum_{T_rho, g<a} g.

Run:
  .venv/bin/python -B research/paley-192-vertex-models.py A 10009 40009 160001 640009
  .venv/bin/python -B research/paley-192-vertex-models.py B 20000 3000000
  .venv/bin/python -B research/paley-192-vertex-models.py check
"""
import sys
from math import gcd, isqrt, sqrt

import numpy as np

LEVELS = (0.5, 0.2, 0.1, 0.05, 0.01)


# ---------------------------------------------------------------- arithmetic
def is_prime(m):
    if m < 2:
        return False
    for q in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if m % q == 0:
            return m == q
    d, s = m - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, m)
        if x in (1, m - 1):
            continue
        for _ in range(s - 1):
            x = x * x % m
            if x == m - 1:
                break
        else:
            return False
    return True


def factor(m):
    fs = {}
    d = 2
    while d * d <= m:
        while m % d == 0:
            fs[d] = fs.get(d, 0) + 1
            m //= d
        d += 1 if d == 2 else 2
    if m > 1:
        fs[m] = fs.get(m, 0) + 1
    return fs


def divisors(m):
    divs = [1]
    for q, e in factor(m).items():
        divs = [d * q ** k for d in divs for k in range(e + 1)]
    return sorted(divs)


def primitive_root(p):
    qs = list(factor(p - 1))
    for g in range(2, p):
        if all(pow(g, (p - 1) // q, p) != 1 for q in qs):
            return g
    raise ValueError


def paley_tables(p):
    """Return n, and s[k] = chi(1 - gamma^(2k)) (s[0] = 0) as int8 array."""
    n = (p - 1) // 2
    gam = primitive_root(p)
    g2 = gam * gam % p
    # powers of gamma^2 by repeated squaring blocks (vectorised doubling)
    pw = np.empty(n, dtype=np.int64)
    pw[0] = 1
    filled = 1
    cur = g2  # gamma^(2*filled)
    while filled < n:
        take = min(filled, n - filled)
        pw[filled:filled + take] = (pw[:take] * cur) % p
        filled += take
        cur = pow(g2, filled, p)
    # Legendre table on F_p
    leg = -np.ones(p, dtype=np.int8)
    sq = (np.arange(1, (p - 1) // 2 + 1, dtype=np.int64) ** 2) % p
    leg[sq] = 1
    leg[0] = 0
    s = leg[(1 - pw) % p]
    return n, s


def fourier_g(nu):
    n = len(nu)
    f = n * np.fft.ifft(nu)
    return (f.real ** 2 + f.imag ** 2)


# ---------------------------------------------------------------- statistics
def vertex_stats(g, s, rho, levels=LEVELS):
    T = (s == rho)
    out = {"G_rho": g[T].sum()}
    for a in levels:
        out[a] = g[T & (g < a)].sum()
    return out


def lambda_size(g, a):
    return int(np.count_nonzero(g[1:] >= a)) + (1 if g[0] >= a else 0)


# ---------------------------------------------------------------- Part A
def law_flat(n, m, rng):
    S = rng.choice(np.arange(1, n), size=m, replace=False)
    nu = np.zeros(n)
    nu[S] = 1.0 / m
    return nu, S


def law_dtheta(n, m, theta, rng):
    L = int(round(m / theta))
    a0 = 1 + int(rng.integers(0, n - L - 1))
    S = a0 + rng.choice(np.arange(L), size=m, replace=False)
    nu = np.zeros(n)
    nu[S] = 1.0 / m
    return nu, S


def part_a(primes):
    print("PART A: sector-free families (evidence; not near-critical)")
    print("columns: law, p, rho, G_rho/sqrt p, m_<a(T_rho)/sqrt p for a in", LEVELS,
          "| sup_{x!=1} g, sum g^2/sqrt p, |Lambda_0.05|/sqrt p, |S||Lambda_0.05|/n")
    for p in primes:
        assert p % 4 == 1 and is_prime(p)
        n, s = paley_tables(p)
        m = int(round(n / sqrt(p)))
        rng = np.random.default_rng(p)
        for name, (nu, S) in (("flat", law_flat(n, m, rng)),
                              ("D_0.25", law_dtheta(n, m, 0.25, rng)),
                              ("D_0.10", law_dtheta(n, m, 0.10, rng))):
            g = fourier_g(nu)
            rp = sqrt(p)
            supg = g[1:].max()
            e2 = (g ** 2).sum() / rp
            lam = lambda_size(g, 0.05)
            for rho in (1, -1):
                st = vertex_stats(g, s, rho)
                row = " ".join(f"{st[a] / rp:6.3f}" for a in LEVELS)
                print(f"{name:7s} {p:7d} {rho:+d}  G_rho {st['G_rho'] / rp:5.3f} | m_<a {row} | "
                      f"sup {supg:6.4f} sumg2 {e2:5.3f} Lam {lam / rp:5.2f} prod {len(S) * lam / n:5.2f}")


# ---------------------------------------------------------------- Part B
def search_two_subgroup(pmin, pmax, tol_sum=0.03, tol_ratio=1.10, dmax=4, limit=None):
    found = []
    p = pmin + ((1 - pmin) % 4)
    while p <= pmax:
        if is_prime(p):
            n = (p - 1) // 2
            m0 = n / sqrt(p)
            ds = [d for d in divisors(n) if 0.35 * m0 <= d <= 0.65 * m0]
            best = None
            for i, h1 in enumerate(ds):
                for h2 in ds[i + 1:]:
                    if abs(h1 + h2 - m0) <= tol_sum * m0 and h2 / h1 <= tol_ratio and gcd(h1, h2) <= dmax:
                        key = (gcd(h1, h2), abs(h1 + h2 - m0))
                        if best is None or key < best[0]:
                            best = (key, h1, h2)
            if best is not None:
                found.append((p, best[1], best[2]))
                if limit and len(found) >= limit:
                    break
        p += 4
    return found


def two_subgroup_law(n, h1, h2):
    """nu = (1_{x1+H1} + 1_{x2+H2})/(h1+h2), H_i = multiples of n/h_i; x1 = 1, x2 = 2."""
    nu = np.zeros(n)
    s1, s2 = n // h1, n // h2
    nu[(1 + s1 * np.arange(h1)) % n] += 1.0
    nu[(2 + s2 * np.arange(h2)) % n] += 1.0
    nu /= (h1 + h2)
    assert nu[0] == 0
    return nu


def part_b(pmin, pmax, show=8):
    print(f"PART B: two-subgroup sharp family, primes p = 1 mod 4 in [{pmin}, {pmax}]")
    found = search_two_subgroup(pmin, pmax)
    print(f"  primes found: {len(found)}")
    for p, h1, h2 in found[:3] + found[-show:]:
        n = (p - 1) // 2
        print(f"  p={p} n={n} h1={h1} h2={h2} gcd={gcd(h1, h2)} n/lcm={n * gcd(h1, h2) // (h1 * h2)}")
    print("  diagnostics for the largest examples:")
    for p, h1, h2 in found[-show:]:
        diagnose_two_subgroup(p, h1, h2)
    return found


def diagnose_two_subgroup(p, h1, h2):
    n, s = paley_tables(p)
    rp = sqrt(p)
    m0 = n / rp
    nu = two_subgroup_law(n, h1, h2)
    g = fourier_g(nu)
    G = g.sum()
    meff = 1.0 / (nu ** 2).sum()
    # level structure: Gamma_i = annihilator of H_i = multiples of h_i in Z/n (k-index)
    k = np.arange(n)
    in1 = (k % h1 == 0)
    in2 = (k % h2 == 0)
    b1, b2 = h1 / (h1 + h2), h2 / (h1 + h2)
    only1 = in1 & ~in2
    only2 = in2 & ~in1
    lev_err = max(np.abs(g[only1] - b1 ** 2).max(), np.abs(g[only2] - b2 ** 2).max())
    off = ~(in1 | in2)
    t_B = g[off].sum() / G
    e2 = (g ** 2).sum()
    # overlap q_a = ghat(a)/G with ghat(a) = sum_x g(x) psi^a(x)-bar = n lambda_a
    lam = np.fft.fft(g).real / n  # lambda_a (up to the conjugation convention; g real even)
    q = lam / lam[0]
    dich = np.max((1 - q) * (2 * q - 1))
    Hstar = np.count_nonzero(q > 0.75)
    q_off = np.max(q[q <= 0.75])
    # (A6): max law mass of a coset of a subgroup of order e <= 2 m0  (cosets = classes mod n/e)
    best_c = 0.0
    for e in divisors(n):
        if e > 2 * m0 or e == n:
            continue
        step = n // e
        cls = np.bincount(np.arange(n) % step, weights=nu, minlength=step)
        best_c = max(best_c, cls.max())
    # sector diagnostics
    rows = []
    for rho in (1, -1):
        Gm = g[s == -rho].sum()
        bad1 = int(np.count_nonzero(in1 & (s == -rho)))
        bad2 = int(np.count_nonzero(in2 & (s == -rho)))
        st = vertex_stats(g, s, rho)
        rows.append((rho, Gm, bad1, bad2, st))
    lamsz = lambda_size(g, 0.2)
    nS = int(np.count_nonzero(nu))
    print(f"  p={p} h1={h1} h2={h2}: G/sqrt p={G / rp:.4f} m_eff/m0={meff / m0:.4f} "
          f"levels b1^2={b1 ** 2:.4f} b2^2={b2 ** 2:.4f} (max dev {lev_err:.1e}) "
          f"t_B={t_B:.1e} sumg2/G={e2 / G:.4f} dichotomy max={dich:.2e} |H*|={Hstar} "
          f"max q off H*={q_off:.4f} max coset mass={best_c:.4f} |S||Lam_0.2|/n={nS * lamsz / n:.3f}")
    J = (n / h1 - 1 - rp) / 2, (n / h2 - 1 - rp) / 2
    for rho, Gm, bad1, bad2, st in rows:
        mm = " ".join(f"{st[a]:8.3f}" for a in (0.2, 0.1, 0.05))
        print(f"     rho={rho:+d}: G_(-rho)={Gm:9.3f} (sqrt p={rp:.1f}); bad points in Gamma_1, Gamma_2: "
              f"{bad1}, {bad2} (Lemma J lower bounds {J[0]:.1f}, {J[1]:.1f}); m_<a(T_rho) a=.2,.1,.05: {mm}")


# ---------------------------------------------------------------- self-check
def self_check():
    ok = True
    # Legendre/primitive-root tables against direct computation at small primes
    for p in (13, 17, 29, 37, 41, 53, 61, 101):
        n, s = paley_tables(p)
        gam = primitive_root(p)
        for k in range(n):
            x = pow(gam, 2 * k, p)
            y = (1 - x) % p
            want = 0 if y == 0 else (1 if pow(y, (p - 1) // 2, p) == 1 else -1)
            ok &= (s[k] == want)
        # |T_+| = (p-5)/4, |T_-| = (p-1)/4  (R190 setup)
        ok &= (np.count_nonzero(s == 1) == (p - 5) // 4) and (np.count_nonzero(s == -1) == (p - 1) // 4)
        # g via fft equals the direct character sum for a random law
        rng = np.random.default_rng(p)
        nu = rng.random(n)
        nu[0] = 0
        nu /= nu.sum()
        g = fourier_g(nu)
        kk = np.arange(n)
        fd = np.array([np.sum(nu * np.exp(2j * np.pi * np.arange(n) * t / n)) for t in kk])
        ok &= np.allclose(g, np.abs(fd) ** 2)
        ok &= abs(g.sum() - n * (nu ** 2).sum()) < 1e-9   # G = n ||nu||^2
    # Lemma J at small primes, every subgroup Gamma of Q and both signs
    for p in (13, 17, 29, 37, 41, 53, 61, 73, 89, 97, 101, 109, 113):
        n, s = paley_tables(p)
        for e in divisors(n):          # Gamma of order e: k multiples of n/e
            idx = np.arange(0, n, n // e)
            for rho in (1, -1):
                bad = np.count_nonzero(s[idx] == -rho)
                ok &= bad >= (e - 1 - sqrt(p)) / 2 - 1e-12
    # two-subgroup closed form at a small example
    for p, h1, h2 in search_two_subgroup(1000, 60000, tol_sum=0.2, tol_ratio=1.5, dmax=6, limit=4):
        n = (p - 1) // 2
        nu = two_subgroup_law(n, h1, h2)
        g = fourier_g(nu)
        k = np.arange(n)
        in1, in2 = (k % h1 == 0), (k % h2 == 0)
        b1, b2 = h1 / (h1 + h2), h2 / (h1 + h2)
        ok &= np.allclose(g[in1 & ~in2], b1 ** 2) and np.allclose(g[in2 & ~in1], b2 ** 2)
        ok &= np.allclose(g[~(in1 | in2)], 0, atol=1e-18 * n * n + 1e-20)
    print("SELF-CHECK OK" if ok else "SELF-CHECK FAILED")
    return ok


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] == "check":
        sys.exit(0 if self_check() else 1)
    if sys.argv[1] == "A":
        part_a([int(x) for x in sys.argv[2:]] or [10009, 40009, 160001])
    elif sys.argv[1] == "B":
        a = sys.argv[2:]
        part_b(int(a[0]) if a else 20000, int(a[1]) if len(a) > 1 else 1000000)
