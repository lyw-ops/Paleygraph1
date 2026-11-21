#!/usr/bin/env python3
"""Round 193 review: independent exact checks (integers / Fractions only).

Part M: Lemma M' (Round 187) Steps 1-3, re-implemented from the statement,
        not from research/paley-187-pair-lemma-check.py.
Part A: Theorem A (Round 188), Lemmas A1-A2 consequences, on laws g = |f|^2
        with f = sum_i c_i 1_{K_i} (K_i subgroups of Q, c_i >= 0 rational,
        sum c_i = 1). Such f equals sum_eta nu_eta eta with nu >= 0 a
        probability on Q^ (nu = sum_i c_i * uniform(annihilator of K_i)),
        so omega >= 0 and (H3) hold and every value is rational.
        Also random rational (H3)-symmetric g on Q (omega not controlled):
        identities only.

Everything is exact. No floating point is used for any assertion.
Usage: python3 -B research/paley-193-review-checks.py
"""
from fractions import Fraction as Fr
import random
import sys

random.seed(193)


def prim_root(p):
    fac, x, d = [], p - 1, 2
    while d * d <= x:
        if x % d == 0:
            fac.append(d)
            while x % d == 0:
                x //= d
        d += 1
    if x > 1:
        fac.append(x)
    for g in range(2, p):
        if all(pow(g, (p - 1) // q, p) != 1 for q in fac):
            return g


# ---------------------------------------------------------------- Part M
def lemma_mprime_case(p, A, R):
    inv = lambda x: pow(x, p - 2, p)
    m = len(R)
    r = {}
    for y1 in R:
        for y2 in R:
            w = y2 * inv(y1) % p  # w = y/y' with y' = y1, y = y2
            r[w] = r.get(w, 0) + 1
    assert sum(r.values()) == m * m
    E = sum(v * v for v in r.values())
    # brute-force multiplicative energy
    prod = {}
    for a in R:
        for b in R:
            prod[a * b % p] = prod.get(a * b % p, 0) + 1
    assert E == sum(v * v for v in prod.values())
    L0 = m.bit_length()  # floor(log2 m) + 1
    K = Fr(m ** 3, E)
    assert 1 <= K <= m
    classes = {}
    for w, v in r.items():
        classes.setdefault(v.bit_length() - 1, []).append(w)
    assert len(classes) <= L0
    good = [j for j, ws in classes.items() if L0 * sum(r[w] ** 2 for w in ws) >= E]
    assert good, "pigeonhole failed"
    checked = 0
    for j in good:  # every admissible popular class, not only the first
        F = set(classes[j])
        rho = 2 ** j
        SF2 = sum(r[w] ** 2 for w in F)
        P = sum(r[w] for w in F)
        assert len(F) * rho * rho <= E
        assert 2 * rho * P >= SF2 and 2 * rho * L0 * P >= E
        eta = Fr(P, m * m)
        assert eta <= 1 and 1 / eta <= 2 * L0 * K
        assert len(F) <= 4 * L0 * L0 * K * eta * eta * m  # (2.1)
        V = [inv(y) for y in R]
        d = {y: sum(1 for v in V if v * y % p in F) for y in R}
        assert sum(d.values()) == P
        assert all(d[y] <= min(m, len(F)) for y in R)
        B = [y for y in R if 2 * m * d[y] >= P]
        assert B and 2 * sum(d[y] for y in B) >= P
        assert 16 * L0 * L0 * m * len(B) ** 2 >= E  # |B|^2 >= m^2/(16 L0^2 K)
        # Step 3: lines l_{u,v}: Z = v(uX + 1 - u); incidences with A x F
        Bs = set(B)
        mrow = {}
        for x in A:
            for y in B:
                u = (1 - y) * inv(1 - x) % p
                mrow[u] = mrow.get(u, 0) + 1
        lines = {}
        for u in range(1, p):
            for v in V:
                key = (v * u % p, v * (1 - u) % p)
                assert key not in lines
                lines[key] = (u, v)
        for h in sorted(set(mrow.values())):
            T = [u for u, c in mrow.items() if c >= h]
            I = 0
            for u in T:
                for v in V:
                    sl, ic = v * u % p, v * (1 - u) % p
                    for x in A:
                        if (sl * x + ic) % p in F:
                            I += 1
            assert 2 * m * I >= h * len(T) * P, (p, h)
        checked += 1
    return checked


def part_m():
    cases = 0
    for p in [13, 17, 19, 23, 29, 31, 37, 41]:
        pool = list(range(2, p))
        g0 = prim_root(p)
        for kind in range(5):
            mR = random.randint(2, p - 2)
            if kind == 0:
                R = random.sample(pool, mR)
            elif kind == 1:  # geometric progression avoiding 1
                R = sorted({pow(g0, k, p) for k in range(1, random.randint(3, p - 2))} - {1})
            elif kind == 2:  # Q minus 1
                R = sorted({x * x % p for x in range(1, p)} - {1})
            elif kind == 3:  # GP plus junk
                gp = {pow(g0, 2 * k, p) for k in range(1, (p - 1) // 4)} - {1}
                R = sorted(gp | set(random.sample(pool, 3)))
            else:  # coset of a small subgroup
                d = next(q for q in range(3, p) if (p - 1) % q == 0)
                R = sorted({g0 * pow(g0, (p - 1) // d * k, p) % p for k in range(d)} - {1})
            A = random.sample(pool, random.randint(1, p - 2))
            cases += lemma_mprime_case(p, A, R)
    print(f"Part M: Lemma M' Steps 1-3 exact on {cases} (case, popular class) pairs: OK")


# ---------------------------------------------------------------- Part A
def theorem_a_case(p, g, omega_nonneg):
    """g: dict x -> Fraction on F_p^x, supported on Q, g(1) = 1, g(1/x) = g(x)."""
    inv = lambda x: pow(x, p - 2, p) if x % p else 0
    Q = {x * x % p for x in range(1, p)}
    gg = [g.get(x, Fr(0)) for x in range(p)]  # gg[0] = 0
    # integer scaling
    N = 1
    for v in gg:
        N = N * v.denominator // __import__("math").gcd(N, v.denominator)
    gi = [int(v * N) for v in gg]
    # chart
    mu = {}
    for Y in range(2, p):
        for D in range(2, p):
            if Y == D or gi[Y] == 0 or gi[D] == 0:
                continue
            r = (Y - D) * inv(1 - D) % p
            b = D * (1 - Y) * inv(Y * (1 - D)) % p
            if b not in Q:
                continue
            assert (r, b) not in mu  # chart injective
            mu[(r, b)] = gi[Y] * gi[D]
    M1 = sum(mu.values())
    m = [0] * p
    mp = [0] * p
    for (r, b), v in mu.items():
        m[r] += v
        mp[b] += v
    X = sum(v * v for v in m)
    Lam0 = sum(v * v for v in mp)
    # h(z) = g(1 - z), c_h(k) = sum_z h(z) h(kz)
    hi = [0] + [gi[(1 - z) % p] for z in range(1, p)]
    ch = [0] * p
    for k in range(1, p):
        ch[k] = sum(hi[z] * hi[k * z % p] for z in range(1, p))
    for b in range(p):
        assert mp[b] == (ch[b] if (b in Q and b != 1) else 0), "Lemma A1"
    for r in range(p):
        k = (1 - r) % p
        assert m[r] == (ch[k] if (k in Q and k != 1) else 0), "R183-A"
    assert Lam0 == X
    Delta0 = [0] * p
    for (r, b), v in mu.items():
        for lam in range(1, p):
            w = mu.get((lam * r % p, b))
            if w:
                Delta0[lam] += v * w
    assert sum(Delta0) == Lam0  # S0(1) = Lambda_0
    cg = [0] * p
    for lam in range(1, p):
        cg[lam] = sum(gi[x] * gi[lam * x % p] for x in range(1, p))
    Gam_tot = cg[1]
    assert all(cg[l] <= Gam_tot for l in range(1, p))
    C = [0] * p
    for lam in range(1, p):
        C[lam] = sum(m[r] * m[lam * r % p] for r in range(1, p))
    T0 = sum(gi[l] * Delta0[l] for l in range(1, p))          # scale N^5
    Tcal = sum(cg[l] * Delta0[l] for l in range(1, p))        # scale N^6
    Gi = sum(gi)                                              # scale N
    # scales: mu ~ N^2, X, Lam0, Delta ~ N^4, C ~ N^4, cg ~ N^2
    # pN^3 F_mu phi_t(s) = p * F_mu h_t(s) [N^3] - G M1 [N * N^2]
    sum_t = 0
    max_ratio = Fr(0)
    for t in range(1, p):
        ht = [0] + [gi[t * inv(e) % p] for e in range(1, p)]
        Fh = [0] * p
        for (r, b), v in mu.items():
            ir = inv(r)
            for s in range(p):
                Fh[s] += v * ht[(s - b) * ir % p]
        # splitting: ||F h_t||^2 = M1^2 G^2/p + ||F phi_t||^2
        nphi = sum((p * f - Gi * M1) ** 2 for f in Fh)        # = p^2 N^6 ||F phi_t||^2
        assert p * p * sum(f * f for f in Fh) == p * M1 * M1 * Gi * Gi + nphi
        sum_t += nphi
        # (i): ||F phi_t||^2 <= p T0 <= p X   (T0 at scale N^5, X at N^4)
        lhs = Fr(nphi, p * p * N ** 6)
        if omega_nonneg:
            assert lhs <= p * Fr(T0, N ** 5), ("Theorem A (i) fails", p, t)
        if T0:
            max_ratio = max(max_ratio, lhs / (p * Fr(T0, N ** 5)))
    assert Fr(T0, N ** 5) <= Fr(X, N ** 4)
    # (ii) exact identity and bound
    lhs2 = Fr(sum_t, p * p * N ** 6)
    ident = (p * Fr(Tcal, N ** 6) - Fr(Gi * Gi * Lam0, N ** 6)
             - Fr(sum(cg[l] * C[l] for l in range(1, p)), N ** 6)
             + Fr(Gi * Gi * M1 * M1, p * N ** 6))
    assert lhs2 == ident, "t-sum identity"
    assert lhs2 <= p * Fr(Tcal, N ** 6) - Fr(Gi * Gi * X, N ** 6)
    assert Fr(Tcal, N ** 6) <= Fr(Gam_tot * X, N ** 6)
    STATS["mu"] += len(mu)
    STATS["laws"] += 1
    return max_ratio


STATS = {"mu": 0, "laws": 0}


def subgroup_law(p, rng):
    g0 = prim_root(p)
    n = (p - 1) // 2
    divs = [d for d in range(3, n + 1) if n % d == 0]
    k = rng.randint(1, 3)
    ds = rng.sample(divs, min(k, len(divs)))
    if max(ds) < n // 3 and n // 3 in divs:
        ds.append(n // 3)
    cs = [Fr(rng.randint(1, 6)) for _ in ds]
    tot = sum(cs)
    cs = [c / tot for c in cs]
    f = {}
    for d, c in zip(ds, cs):
        # subgroup of Q of order d: generated by g0^(2n/d)
        gen = pow(g0, 2 * n // d, p)
        x = 1
        for _ in range(d):
            f[x] = f.get(x, Fr(0)) + c
            x = x * gen % p
    return {x: v * v for x, v in f.items()}


def random_h3_law(p, rng):
    Q = sorted({x * x % p for x in range(1, p)})
    g = {}
    for x in Q:
        if x in g:
            continue
        v = Fr(1) if x == 1 else Fr(rng.randint(0, 4), 4)
        g[x] = v
        g[pow(x, p - 2, p)] = v
    return g


def part_a():
    rng = random.Random(1930)
    n_cases = 0
    worst = Fr(0)
    for p in [13, 17, 29, 37, 41, 53, 61, 73]:
        for _ in range(3):
            worst = max(worst, theorem_a_case(p, subgroup_law(p, rng), True))
            n_cases += 1
        for _ in range(2):
            theorem_a_case(p, random_h3_law(p, rng), False)
            n_cases += 1
    print(f"Part A: Theorem A exact on {n_cases} laws (p = 13..73): A1, R183-A, splitting, "
          f"(i) on omega>=0 laws, (ii) identity and bounds: OK; "
          f"max_t ||pi phi_t||^2/(p T0) = {worst} ({float(worst):.4f}); "
          f"{STATS['mu']} chart entries in total")


if __name__ == "__main__":
    part_m()
    part_a()
    print("ALL EXACT CHECKS OK")
