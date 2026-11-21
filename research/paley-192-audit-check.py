#!/usr/bin/env python3
"""Round 192 audit (session/r192-audit): independent checks of
research/native-claude-ordinary-nc-vertex-tightness-192.md.

Written by the auditor; it imports nothing from the report's scripts.
Exact parts use fractions.Fraction / integers; numerical parts use numpy
(floating point, evidence for finite p only).

Parts
  X  exact arithmetic: Prop. C constants, Prop. D (A6) thresholds including
     the range delta >= 350/256 not covered by the report's 3/4 bound,
     n/lcm -> 8d, F_{r^2} control m_<a exactly 2, loss exponents.
  J  Lemma J for EVERY subgroup Gamma of F_p^* (not only of Q), both signs,
     p <= 241; the Jacobi-sum identity sum_{y in Gamma} chi(1-y)
     = (1/k) sum_{psi^k=1} J(psi,chi) with complex characters (p <= 61);
     and the comparison with Vinogradov's bound (|sum| <= sqrt p) for Gamma <= Q.
  T  Prop. A(2) level transfer: random nonnegative g, g' and 0<a<b.
  A  Prop. A(1),(3) and the Theorem E chain on perturbed flat laws:
     sum|f-f_S|^2 = n ||nu - 1_S/|S|||^2 (Parseval), Delta bound,
     m^Q_{<a/2}(g_S) <= m^Q_{<a}(g) + 2 Delta, m_<a(T_rho) sandwich.
  D  Prop. D two-subgroup family at the report's three tabulated primes:
     levels, max coset share for each delta in a grid over (0,2) against
     (1-delta/2)^(1/4), q_a dichotomy, t_B, Lemma J and G_{-rho}.
  F  Prop. F: the F_{r^2} control built in F_r[i] (r = 3 mod 4), independent
     field arithmetic: g levels, V_- = 0, G_- -> 1, Lemma 0 identity,
     d_rho(S), m_<a on T_+, energy ratio, t_B for B = F_r^*.
  B  Prop. B: random flat law (Bernoulli p^-1/2) and Bernoulli D_theta,
     both signs: G_eps, m_<a(T_eps), sup g, energy, coset counts.

Run:  .venv/bin/python -B research/paley-192-audit-check.py [X J T A D F B]
"""
import sys
from fractions import Fraction as Fr
from math import gcd, isqrt, sqrt

import numpy as np

RESULTS = []


def check(name, cond):
    RESULTS.append((name, bool(cond)))
    print(("ok   " if cond else "FAIL ") + name)


# ------------------------------------------------------------------ helpers
def is_prime(m):
    if m < 2:
        return False
    if m % 2 == 0:
        return m == 2
    r = isqrt(m)
    f = 3
    while f <= r:
        if m % f == 0:
            return False
        f += 2
    return True


def prime_factors(m):
    out, d = [], 2
    while d * d <= m:
        if m % d == 0:
            out.append(d)
            while m % d == 0:
                m //= d
        d += 1
    if m > 1:
        out.append(m)
    return out


def divisors(m):
    small = [d for d in range(1, isqrt(m) + 1) if m % d == 0]
    return sorted(set(small + [m // d for d in small]))


def prim_root(p):
    fs = prime_factors(p - 1)
    g = 2
    while any(pow(g, (p - 1) // q, p) == 1 for q in fs):
        g += 1
    return g


def legendre_vec(vals, p):
    vals = np.asarray(vals, dtype=np.int64) % p
    out = np.zeros(len(vals), dtype=np.int64)
    # Euler's criterion, vectorised by repeated squaring
    e = (p - 1) // 2
    base = vals.copy()
    acc = np.ones(len(vals), dtype=np.int64)
    while e:
        if e & 1:
            acc = (acc * base) % p
        base = (base * base) % p
        e >>= 1
    out[acc == 1] = 1
    out[acc == p - 1] = -1
    out[vals == 0] = 0
    return out


def paley_s(p):
    """n and s[k] = chi(1 - w^(2k)) for a primitive root w (s[0] = 0)."""
    n = (p - 1) // 2
    w = prim_root(p)
    w2 = w * w % p
    pw = np.empty(n, dtype=np.int64)
    pw[0] = 1
    for k in range(1, n):
        pw[k] = pw[k - 1] * w2 % p
    return n, legendre_vec(1 - pw, p)


def f_of(nu):
    """f(x_k) = sum_j nu_j e(jk/n), computed as n * ifft."""
    n = len(nu)
    return n * np.fft.ifft(nu)


# ------------------------------------------------------------------ Part X
def part_x():
    print("PART X: exact arithmetic")
    # Prop C: (sum_Lambda g)^2 <= |Lambda| sum g^2 with sum_Lambda g -> 1, sum g^2 <= 1/2 (units sqrt p)
    check("Prop C: |Lambda_a|/sqrt p >= 1^2/(1/2) = 2", Fr(1) / Fr(1, 2) == 2)
    check("Prop C: |S||Lambda|/n >= 2 since |S| sqrt p / n -> 1", Fr(2) * 1 == 2)
    check("Prop C: 2 <= 1/a iff a <= 1/2", all((2 <= 1 / Fr(a)) == (Fr(a) <= Fr(1, 2))
                                               for a in [Fr(1, 3), Fr(1, 2), Fr(51, 100), Fr(9, 10)]))
    # Prop D (A6). Report: share <= beta_i + beta_j/2 -> 3/4, enough iff (3/4)^4 < 1 - delta/2.
    thr = 2 * (1 - Fr(3, 4) ** 4)
    check(f"Prop D: report threshold 2(1-(3/4)^4) = {thr} = 350/256", thr == Fr(350, 256))
    # Refined: if K (order <= (2-delta) m0 < 2 h_i) contains H_i then K = H_i or |K| = t h_i with
    # t <= 2(2-delta) and |K cap H_j| <= t d = O(1); otherwise |K cap H_i| <= h_i/2 for both i.
    # So the share is <= 1/2 + o(1); enough iff (1/2)^4 <= 1 - delta/2 iff delta <= 15/8.
    thr2 = 2 * (1 - Fr(1, 2) ** 4)
    check(f"Prop D refined: share 1/2 suffices for delta <= {thr2} = 15/8", thr2 == Fr(15, 8))
    # delta in (15/8, 2): |K| <= (2-delta) m0 < m0/8 < h_i, share <= 2|K|/m0 <= 2u (u = 2-delta);
    # need 2u <= (u/2)^(1/4) iff 32 u^3 <= 1; true for u <= 1/8 since 32/512 < 1.
    check("Prop D refined: for u = 2 - delta <= 1/8, (2u)^4 <= u/2", all(
        (2 * Fr(u)) ** 4 <= Fr(u) / 2 for u in [Fr(1, 8), Fr(1, 10), Fr(1, 100), Fr(1, 10**6)]))
    # n/lcm with h_i ~ m0/2, m0 ~ sqrt p / 2, n ~ p/2: n d/(h1 h2) -> (1/2) d / (1/16) = 8 d
    check("Prop D: n/lcm -> 8d", Fr(1, 2) / (Fr(1, 4) * Fr(1, 4)) == 8)
    # Prop D energy beta1^3 + beta2^3 at beta = 1/2
    check("Prop D: beta1^3+beta2^3 = 1/4", 2 * Fr(1, 8) == Fr(1, 4))
    # Prop F: beta = 4/(r-1)^2 on Q minus F_r^*, |Q| - (r-1) = (r-1)^2/2, so m_<a = 2 exactly
    for r in [7, 11, 19, 23, 43, 10007]:
        beta = Fr(4, (r - 1) ** 2)
        rest = Fr(r * r - 1, 2) - (r - 1)
        check(f"Prop F r={r}: m^Q_<a = beta(|Q|-(r-1)) = 2 exactly (report bound 2(r+1)/(r-1))",
              beta * rest == 2 and 2 <= Fr(2 * (r + 1), r - 1))
        check(f"Prop F r={r}: G = (r-1) + 2 = r+1; G_- = |T_-| beta = (r+1)/(r-1)",
              (r - 1) + beta * rest == r + 1 and Fr((r * r - 1), 4) * beta == Fr(r + 1, r - 1))
    # Prop B(ii): heavier sign 1/2 - theta; Bernoulli both signs (1-theta)/2 - theta = (1-3 theta)/2
    for th in [Fr(1, 10), Fr(1, 5), Fr(3, 10)]:
        check(f"Prop B: theta={th}: (1-theta)/2 - theta = (1-3theta)/2 = {(1 - 3 * th) / 2} > 0",
              (1 - th) / 2 - th == (1 - 3 * th) / 2 and (1 - 3 * th) / 2 > 0)
    # D_theta: high set size: |D_L'(k)| <= n/(2L'|k|) >= sqrt(a)/2 forces |k| <= n/(L' sqrt a);
    # n/L' = theta sqrt p (1+o(1)), so the count is O(sqrt p / sqrt a), better than O(sqrt p / a).
    # Bernoulli D_theta off-diagonal: Var <= 2 theta^2 sum_{j != j' in J'} |c|^2 / m^4,
    # sum <= L'^2 (p/4) (|c(d)| <= (sqrt p+1)/2), L' = m/theta, m = sqrt p/2 (leading orders):
    # 2 theta^2 (m/theta)^2 (p/4) / m^4 = p / (2 m^2) = 2 -> standard deviation O(1).
    m2 = Fr(1, 4)  # m^2 / p
    check("Prop B(ii-2): off-diagonal variance <= 2 theta^2 L'^2 (p/4)/m^4 = p/(2m^2) = 2 (O(1))",
          Fr(1, 2) / m2 == 2)
    # Loss exponents
    check("loss vs O(p): 3/2 - 1 = 1/2", Fr(3, 2) - 1 == Fr(1, 2))
    check("loss vs o(pD), D <= p^(1/4): 3/2 - 5/4 = 1/4", Fr(3, 2) - Fr(5, 4) == Fr(1, 4))
    check("Prop A: Delta = o(p^(1/4)) O(p^(1/4)) = o(p^(1/2))", Fr(1, 4) + Fr(1, 4) == Fr(1, 2))


# ------------------------------------------------------------------ Part J
def part_j():
    print("PART J: Lemma J for every subgroup of F_p^*, and the Jacobi identity")
    total = 0
    worst = 10.0
    for p in [q for q in range(13, 242) if q % 4 == 1 and is_prime(q)]:
        w = prim_root(p)
        chi = {x: (1 if pow(x, (p - 1) // 2, p) == 1 else -1) for x in range(1, p)}
        chi[0] = 0
        sp = sqrt(p)
        for k in divisors(p - 1):
            h = (p - 1) // k
            gam = [pow(w, k * t, p) for t in range(h)]
            ssum = sum(chi[(1 - y) % p] for y in gam)
            bound = (1 + (k - 1) * sp) / k
            ok = abs(ssum) <= bound + 1e-9 and abs(ssum) < sp
            for rho in (1, -1):
                bad = sum(1 for y in gam if y != 1 and chi[(1 - y) % p] == -rho)
                ok &= bad >= (h - 1 - sp) / 2 - 1e-9
                if h - 1 > sp:
                    worst = min(worst, bad / ((h - 1 - sp) / 2))
            total += 1
            if not ok:
                check(f"Lemma J p={p} k={k}", False)
    check(f"Lemma J: {total} (p, Gamma) pairs, p <= 241, every subgroup of F_p^*, both signs", True)
    print(f"     smallest ratio bad / ((|Gamma|-1-sqrt p)/2) where positive: {worst:.3f}")
    # Jacobi identity with complex characters
    ok = True
    for p in [13, 17, 29, 37, 41, 53, 61]:
        w = prim_root(p)
        ind = {}
        x = 1
        for e in range(p - 1):
            ind[x] = e
            x = x * w % p

        def charv(a, u):  # character psi_a(u) = e(a ind(u)/(p-1)), psi(0) = 0
            return 0 if u % p == 0 else np.exp(2j * np.pi * a * ind[u % p] / (p - 1))
        chi_a = (p - 1) // 2
        for k in divisors(p - 1):
            h = (p - 1) // k
            lhs = sum(charv(chi_a, 1 - pow(w, k * t, p)) for t in range(h))
            rhs = 0
            for t in range(k):          # psi^k = 1  <=>  psi = psi_{a}, a multiple of (p-1)/k
                a = t * (p - 1) // k
                J = sum(charv(a, u) * charv(chi_a, 1 - u) for u in range(1, p))
                rhs += J
            rhs /= k
            ok &= abs(lhs - rhs) < 1e-8
    check("Lemma J: sum_{Gamma} chi(1-y) = (1/k) sum_{psi^k=1} J(psi,chi) (p <= 61, all k)", ok)
    # Vinogradov comparison for Gamma <= Q: sum_{x,x' in Gamma} chi(x-x') = |Gamma| sum_y chi(1-y)
    ok = True
    for p in [29, 37, 41, 53, 61, 73, 89, 97, 101]:
        w = prim_root(p)
        for k in divisors(p - 1):
            if k % 2:
                continue  # Gamma <= Q iff k even
            gam = [pow(w, k * t, p) for t in range(1, (p - 1) // k + 1)]
            leg = lambda z: 0 if z % p == 0 else (1 if pow(z, (p - 1) // 2, p) == 1 else -1)
            dbl = sum(leg(x - y) for x in gam for y in gam)
            sgl = sum(leg(1 - y) for y in gam)
            ok &= dbl == len(gam) * sgl and abs(dbl) <= sqrt(p) * len(gam) + 1e-9
    check("Lemma J = Vinogradov with A = Gamma, B = -Gamma for Gamma <= Q (p <= 101)", ok)


# ------------------------------------------------------------------ Part T
def part_t():
    print("PART T: Prop. A(2) level transfer on random data")
    rng = np.random.default_rng(192)
    ok = True
    worst = -1.0
    for _ in range(20000):
        N = int(rng.integers(2, 60))
        g = rng.random(N) ** rng.uniform(0.3, 3)
        gp = np.clip(g + rng.normal(0, rng.uniform(0, 0.5), N), 0, None)
        a = rng.uniform(0.01, 0.9)
        b = rng.uniform(a + 1e-3, 1.0)
        D = np.abs(g - gp).sum()
        lhs = g[g < a].sum()
        rhs = gp[gp < b].sum() + D * b / (b - a)
        ok &= lhs <= rhs + 1e-12
        worst = max(worst, lhs - (gp[gp < b].sum() + D))
    check("Prop A(2): sum_{g<a} g <= sum_{g'<b} g' + Delta b/(b-a), 20000 random cases", ok)


# ------------------------------------------------------------------ Part A
def part_a():
    print("PART A: Prop. A and the Theorem E transfer on perturbed flat laws (finite p)")
    rng = np.random.default_rng(7)
    for p in [10009, 40009]:
        n, s = paley_s(p)
        m0 = n / sqrt(p)
        m = int(round(m0))
        # random flat support S, perturbed by eps in l^1
        for eps in [0.0, 0.05, 0.2]:
            S = rng.choice(np.arange(1, n), size=m, replace=False)
            nuS = np.zeros(n)
            nuS[S] = 1.0 / m
            pert = np.abs(rng.normal(0, 1, n))
            pert[0] = 0
            pert /= pert.sum()
            nu = (1 - eps) * nuS + eps * pert
            fS, f = f_of(nuS), f_of(nu)
            gS, g = np.abs(fS) ** 2, np.abs(f) ** 2
            lhs = np.sum(np.abs(f - fS) ** 2)
            pars = n * np.sum((nu - nuS) ** 2)
            D = np.abs(g - gS).sum()
            G, GS = g.sum(), gS.sum()
            dbound = sqrt(lhs) * sqrt(2 * G + 2 * GS)
            ok1 = abs(lhs - pars) <= 1e-8 * max(1, pars) and D <= dbound + 1e-9
            ok2 = True
            for a in [0.05, 0.1, 0.2, 0.4]:
                mq = lambda h, lev: h[1:][h[1:] < lev].sum()
                ok2 &= mq(gS, a / 2) <= mq(g, a) + 2 * D + 1e-9
                for rho in (1, -1):
                    mT = g[(s == rho) & (g < a)].sum()
                    Gm = g[s == -rho].sum()
                    ok2 &= (mq(g, a) - Gm - 1e-9 <= mT <= mq(g, a) + 1e-9)
            check(f"Prop A p={p} eps={eps}: Parseval, Delta <= CS bound, transfer chain, sandwich", ok1 and ok2)


# ------------------------------------------------------------------ Part D
def part_d():
    print("PART D: two-subgroup family (independent construction)")
    for p, h1, h2 in [(3997297, 487, 513), (3998809, 484, 486), (3999001, 500, 516)]:
        assert is_prime(p) and p % 4 == 1
        n, s = paley_s(p)
        assert n % h1 == 0 and n % h2 == 0
        m0 = n / sqrt(p)
        nu = np.zeros(n)
        nu[(1 + (n // h1) * np.arange(h1)) % n] += 1
        nu[(2 + (n // h2) * np.arange(h2)) % n] += 1
        overlap = nu.max()
        nu /= nu.sum()
        g = np.abs(f_of(nu)) ** 2
        k = np.arange(n)
        in1, in2 = (k % h1 == 0), (k % h2 == 0)
        b1, b2 = h1 / (h1 + h2), h2 / (h1 + h2)
        lev = max(abs(g[in1 & ~in2] - b1 ** 2).max(), abs(g[in2 & ~in1] - b2 ** 2).max())
        tB = g[~(in1 | in2)].sum() / g.sum()
        G = g.sum()
        # coset shares for subgroups of order e <= 2 m0, recorded per order
        shares = {}
        for e in divisors(n):
            if e == n or e > 2 * m0:
                continue
            step = n // e
            shares[e] = np.bincount(np.arange(n) % step, weights=nu, minlength=step).max()
        okA6 = True
        for delta in np.linspace(0.01, 1.99, 199):
            lim = (2 - delta) * m0
            mx = max([v for e, v in shares.items() if e <= lim], default=0.0)
            okA6 &= mx <= (1 - delta / 2) ** 0.25 + 0.03  # o(1) slack at finite p
        mx_all = max(shares.values())
        lam = np.fft.fft(g).real / n
        q = lam / lam[0]
        dich = np.max((1 - q) * (2 * q - 1))
        nl = n // (h1 * h2 // gcd(h1, h2))
        rows = []
        okJ = True
        for rho in (1, -1):
            for h, ind in ((h1, in1), (h2, in2)):
                bad = int(np.count_nonzero(ind & (s == -rho)))
                okJ &= bad >= (n / h - 1 - sqrt(p)) / 2
            Gm = g[s == -rho].sum()
            mlow = [g[(s == rho) & (g < a)].sum() for a in (0.2, 0.05)]
            rows.append(f"rho={rho:+d} G_-rho={Gm:.1f} m_<.2={mlow[0]:.3f} m_<.05={mlow[1]:.3f}")
        check(f"Prop D p={p}: disjoint cosets (max multiplicity {int(overlap)}), level dev {lev:.1e}, "
              f"t_B={tB:.1e}, |Gamma'|={nl}, max coset share={mx_all:.4f}, (A6)(b) for every delta "
              f"in grid, dichotomy {dich:.3f}, Lemma J bad counts; " + "; ".join(rows),
              overlap == 1 and lev < 1e-12 and tB < 1e-20 and okA6 and okJ and dich < 0.03
              and max(float(r.split('m_<.2=')[1].split()[0]) for r in rows) <= nl)


# ------------------------------------------------------------------ Part F
def part_f():
    print("PART F: F_{r^2} control in F_r[i] (independent field arithmetic)")
    for r in [7, 11, 19, 23, 31, 43]:
        assert r % 4 == 3 and is_prime(r)
        q = r * r

        def mul(x, y):
            return ((x[0] * y[0] - x[1] * y[1]) % r, (x[0] * y[1] + x[1] * y[0]) % r)

        def pw(x, e):
            out, b = (1, 0), x
            while e:
                if e & 1:
                    out = mul(out, b)
                b = mul(b, b)
                e >>= 1
            return out
        fs = prime_factors(q - 1)
        gen = None
        for a in range(r):
            for b in range(1, r):
                x = (a, b)
                if all(pw(x, (q - 1) // t) != (1, 0) for t in fs):
                    gen = x
                    break
            if gen:
                break
        n = (q - 1) // 2
        g2 = mul(gen, gen)
        elems = [(1, 0)]
        for _ in range(n - 1):
            elems.append(mul(elems[-1], g2))
        sq = set(elems)

        def chi(x):
            if x == (0, 0):
                return 0
            return 1 if x in sq else -1
        s = np.array([chi(((1 - x[0]) % r, (-x[1]) % r)) for x in elems])
        s[0] = 0
        I = np.arange(0, n, r - 1)            # annihilator of F_r^*, order (r+1)/2
        nu = np.zeros(n)
        nu[I[1:]] = 1.0
        nu /= nu.sum()
        f = f_of(nu)
        g = np.abs(f) ** 2
        inFr = np.array([x[1] == 0 for x in elems])
        beta = 4 / (r - 1) ** 2
        lev_ok = np.allclose(g[inFr], 1) and np.allclose(g[~inFr], beta)
        sector_ok = np.all(s[inFr & (np.arange(n) > 0)] == 1)
        Tm = s == -1
        V = np.sum(np.abs(f[Tm] - f[Tm].mean()) ** 2)
        Gm = g[Tm].sum()
        G = g.sum()
        # Lemma 0: <e, rho K e> = (G_rho - G_-rho)/G, with K = multiplication by s
        lem0 = abs(((g * s).sum()) / G - (1 - (2 * Gm + 1) / G)) < 1e-9
        mlowQ = g[1:][g[1:] < 0.5].sum()
        mlowT = g[(s == 1) & (g < 0.5)].sum()
        S = I[1:]
        energy = sum(np.count_nonzero(np.isin((S + a) % n, S)) ** 2 for a in range(n)) / len(S) ** 3
        tB = g[~inFr].sum() / G
        check(f"Prop F r={r}: levels 1/beta, F_r^*\\1 in T_+, V_-={V:.1e}, G_-={Gm:.4f} "
              f"(=(r+1)/(r-1)={(r + 1) / (r - 1):.4f}), Lemma 0, m^Q_<.5={mlowQ:.4f}, m_<.5(T_+)={mlowT:.4f}, "
              f"E/|S|^3={energy:.3f} (subgroup minus a point, -> 1), t_B(F_r^*)={tB:.3f}, G={G:.3f}",
              lev_ok and sector_ok and V < 1e-18 and abs(Gm - (r + 1) / (r - 1)) < 1e-9 and lem0
              and abs(mlowQ - 2) < 1e-9 and abs(G - (r + 1)) < 1e-9 and 1 - 2 / len(S) <= energy <= 1)


# ------------------------------------------------------------------ Part B
def part_b():
    print("PART B: Prop. B families (Bernoulli; floating point; finite p)")
    for p in [160001, 640009]:
        n, s = paley_s(p)
        rp = sqrt(p)
        m0 = n / rp
        rng = np.random.default_rng(p + 1)
        xi = rng.random(n) < 1 / rp
        xi[0] = False
        S = np.flatnonzero(xi)
        nu = xi / xi.sum()
        g = np.abs(f_of(nu)) ** 2
        sup = g[1:].max()
        Gp, Gm = g[s == 1].sum() / rp, g[s == -1].sum() / rp
        E2 = (g ** 2).sum() / rp
        cnt = 0
        for e in divisors(n):
            if e > 2 * m0:
                continue
            step = n // e
            cnt = max(cnt, np.bincount(S % step, minlength=step).max())
        ov = (np.fft.ifft(np.abs(np.fft.fft(xi.astype(float))) ** 2).real)
        maxov = np.max(np.round(ov[1:]))
        print(f"     random flat p={p}: |S|/m0={len(S) / m0:.3f} sup g={sup:.4f} (C log p/m0 scale "
              f"{np.log(p) / m0:.4f}) G_+={Gp:.3f} G_-={Gm:.3f} sum g^2/sqrt p={E2:.4f} "
              f"max coset count={cnt} max overlap={int(maxov)} log p={np.log(p):.1f}")
        check(f"Prop B(i) p={p}: G_eps in [0.45,0.55] sqrt p both signs, sup g < 0.1",
              0.45 < Gp < 0.55 and 0.45 < Gm < 0.55 and sup < 0.1)
        for th in (0.2, 0.3):
            L = int(round(m0 / th))
            a0 = int(rng.integers(1, n - L - 1))
            xi2 = np.zeros(n, dtype=bool)
            xi2[a0:a0 + L] = rng.random(L) < th
            nu2 = xi2 / xi2.sum()
            g2 = np.abs(f_of(nu2)) ** 2
            out = []
            okb = True
            for eps in (1, -1):
                Ge = g2[s == eps].sum() / rp
                ml = g2[(s == eps) & (g2 < 0.05)].sum() / rp
                okb &= ml >= (1 - 3 * th) / 2 - 0.05 and Ge >= (1 - th) / 2 - 0.05
                out.append(f"eps={eps:+d} G={Ge:.3f} m_<.05={ml:.3f}")
            check(f"Prop B(ii-2) p={p} theta={th}: both signs above ((1-theta)/2, (1-3theta)/2) "
                  f"= ({(1 - th) / 2:.3f}, {(1 - 3 * th) / 2:.3f}) up to 0.05: " + "; ".join(out), okb)


if __name__ == "__main__":
    parts = sys.argv[1:] or ["X", "J", "T", "A", "D", "F", "B"]
    table = {"X": part_x, "J": part_j, "T": part_t, "A": part_a, "D": part_d, "F": part_f, "B": part_b}
    for P in parts:
        table[P]()
    bad = [nm for nm, ok in RESULTS if not ok]
    print()
    print(f"{len(RESULTS)} checks, {len(bad)} failures")
    print("ALL AUDIT CHECKS OK" if not bad else "FAILURES:\n  " + "\n  ".join(bad))
