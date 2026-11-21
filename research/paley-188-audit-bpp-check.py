#!/usr/bin/env python3
"""Round 188 audit (session/r188-audit): independent replay of the ordinary report
`native-claude-ordinary-prime-beyond-point-plane-188.md` (BPP).

Own implementation; imports no report script.

Part A (exact integers): Proposition B (fibre sums, Delta <= c, E <= cX + sum_{l!=1} C D <= c M_1^2) and
  Lemma A1 (m'(b) = c_h(b), m(r) = c_h(1-r), Lambda_0 = X) for random integer weights on Q that are
  inversion symmetric (H3); and the failure of Lambda_0 = X without (H3) (shows (H3) is load-bearing).
Part B (floating, double precision, tolerances stated): the actual g = |f|^2 of a probability nu on the
  characters of Q, at p = 13 .. 61, several laws (random, sparse, flat interval, point mass, two-point):
  (H3) g(1/x) = g(x); omega >= 0, omega = lambda_nu/2 on both lifts, sum omega = 1, G = (p-1) omega(1);
  Lemma A2 for every nontrivial chi (Gauss sum identity); the splitting; Theorem A (i) for every t
  (||pi phi_t||^2 <= p T_0 <= p X); Theorem A (ii) (t-orthogonality identity and <= p T - G^2 X <= p Gamma X);
  the weighted consequence over s != 0, 1; the physical form of T_0 - c.
  Also the auditor's remarks (not in BPP): T0 - c <= (T3 G E^x(h))^(1/2), T3 = (p-1)^2 sum omega^3;
  T0 <= c + (Gamma_2 D0* X)^(1/2) with D0* = max_(l!=1) Delta(l,0) <= (Gamma_tot E^x(h))^(1/2).
Part C (floating): negative control.  A nonnegative inversion-symmetric weight on Q that is NOT of the
  form |f|^2 (its multiplicative Fourier coefficients have negative entries): does Theorem A (i) fail?
Part D (exact Fractions): every exponent of BPP re-derived from the route formulas.
Replay: .venv/bin/python -B research/paley-188-audit-bpp-check.py   (about 1 min)
"""
import cmath
import math
import random
from fractions import Fraction as F

import numpy as np

OK = True


def check(name, cond):
    global OK
    OK &= bool(cond)
    print(f'  [{"OK" if cond else "FAIL"}] {name}')


def prim_root(p):
    fac = []
    m = p - 1
    d = 2
    while d * d <= m:
        if m % d == 0:
            fac.append(d)
            while m % d == 0:
                m //= d
        d += 1
    if m > 1:
        fac.append(m)
    for g0 in range(2, p):
        if all(pow(g0, (p - 1) // q, p) != 1 for q in fac):
            return g0


def setup(p):
    gam = prim_root(p)
    log = [None] * p
    x = 1
    for i in range(p - 1):
        log[x] = i
        x = x * gam % p
    inv = [0] + [pow(x, p - 2, p) for x in range(1, p)]
    Q = [x for x in range(1, p) if log[x] % 2 == 0]
    return gam, log, inv, Q


def chart(p, g, inv, Qset):
    """mu(r, b) = g(Y) g(D) on Y != D in F_p minus {0,1}, mask b in Q (Round 171 chart).  Returns dict."""
    mu = {}
    for Y in range(2, p):
        if g[Y] == 0:
            continue
        for D in range(2, p):
            if D == Y or g[D] == 0:
                continue
            r = (Y - D) * inv[(1 - D) % p] % p
            b = D * (1 - Y) % p * inv[Y * (1 - D) % p] % p
            if b not in Qset:
                continue
            key = (r, b)
            assert key not in mu, 'chart not injective'
            mu[key] = g[Y] * g[D]
    return mu


def marginals(p, mu):
    m = [0] * p
    mp = [0] * p
    for (r, b), v in mu.items():
        m[r] += v
        mp[b] += v
    return m, mp


def c_h(p, g, kap):
    # h(z) = g(1 - z), z in F_p^x
    return sum(g[(1 - z) % p] * g[(1 - kap * z) % p] for z in range(1, p))


def delta_table(p, mu):
    """Delta(lam, beta) = sum mu(r,b) mu(lam r, b + r beta)."""
    D = {}
    items = list(mu.items())
    for lam in range(1, p):
        for beta in range(p):
            s = 0
            for (r, b), v in items:
                w = mu.get((lam * r % p, (b + r * beta) % p))
                if w:
                    s += v * w
            if s:
                D[(lam, beta)] = s
    return D


# ---------------------------------------------------------------- Part A
print('== Part A: exact integer checks of Proposition B and Lemma A1 ==')
rng = random.Random(18801)
for p in (13, 17, 29, 37, 41):
    gam, log, inv, Q = setup(p)
    Qset = set(Q)
    for trial in range(3):
        # random integer weight on Q, inversion symmetric, g(1) arbitrary
        g = [0] * p
        for x in Q:
            if g[x] == 0 or x <= inv[x]:
                v = rng.choice((0, 0, 1, 2, 3, 5))
                g[x] = v
                g[inv[x]] = v
        g[1] = rng.choice((1, 2, 4))
        mu = chart(p, g, inv, Qset)
        m, mp = marginals(p, mu)
        M1 = sum(mu.values())
        c = sum(v * v for v in mu.values())
        X = sum(v * v for v in m)
        L0 = sum(v * v for v in mp)
        Dt = delta_table(p, mu)
        C = [0] * p
        for lam in range(1, p):
            C[lam] = sum(m[r] * m[lam * r % p] for r in range(1, p))
        fib = all(sum(Dt.get((lam, be), 0) for be in range(p)) == C[lam] for lam in range(1, p))
        Dmax = [0] * p
        for (lam, be), v in Dt.items():
            Dmax[lam] = max(Dmax[lam], v)
        E = sum(v * v for v in Dt.values())
        rhs = c * X + sum(C[l] * Dmax[l] for l in range(2, p))
        ok_B = fib and Dmax[1] == c and max(Dt.values()) <= c and E <= rhs <= c * M1 * M1 and Dt.get((1, 0)) == c
        # Lemma A1
        a1 = all(mp[b] == (c_h(p, g, b) if (b in Qset and b != 1) else 0) for b in range(p))
        a1r = all(m[r] == (c_h(p, g, (1 - r) % p) if ((1 - r) % p in Qset and (1 - r) % p != 1) else 0)
                  for r in range(p))
        # sum_lam Delta(lam, 0) = Lambda_0
        l0 = sum(Dt.get((lam, 0), 0) for lam in range(1, p)) == L0
        check(f'p={p} t{trial}: Prop B (i)-(iii) exact [E={E}, cX+sumCD={rhs}, cM1^2={c*M1*M1}]; '
              f'A1 m\'=c_h, m=c_h(1-.), Lambda_0=X={X}; sum Delta(l,0)=Lambda_0', ok_B and a1 and a1r and L0 == X and l0)
# (H3) is load-bearing for A1
p = 29
gam, log, inv, Q = setup(p)
Qset = set(Q)
fails = 0
for trial in range(5):
    g = [0] * p
    for x in Q:
        g[x] = rng.choice((0, 1, 2, 3))
    g[1] = 1
    if all(g[x] == g[inv[x]] for x in Q):
        continue
    mu = chart(p, g, inv, Qset)
    m, mp = marginals(p, mu)
    if sum(v * v for v in m) != sum(v * v for v in mp):
        fails += 1
check(f'without (H3) Lambda_0 != X occurs (p=29, {fails} of 5 asymmetric weights): (H3) is load-bearing in A1', fails > 0)

# ---------------------------------------------------------------- Part B
print('\n== Part B: actual g = |f|^2 (floating, double precision) ==')


def actual_g(p, log, nu):
    n = (p - 1) // 2
    g = np.zeros(p)
    f = np.zeros(p, dtype=complex)
    for x in range(1, p):
        if log[x] % 2 == 0:
            i = log[x] // 2
            f[x] = sum(nu[j] * cmath.exp(2j * math.pi * j * i / n) for j in range(n) if nu[j])
            g[x] = abs(f[x]) ** 2
    return g, f


def laws(p, rng):
    n = (p - 1) // 2
    out = {}
    v = np.array([rng.random() for _ in range(n)])
    out['random'] = v / v.sum()
    v = np.zeros(n)
    for j in rng.sample(range(n), max(2, int(round(math.sqrt(n))))):
        v[j] = rng.random() + 0.2
    out['sparse'] = v / v.sum()
    k = max(2, int(round(n / math.sqrt(p))))
    s0 = rng.randrange(n)
    v = np.zeros(n)
    for j in range(k):
        v[(s0 + j) % n] = 1
    out['interval'] = v / v.sum()
    v = np.zeros(n)
    v[rng.randrange(n)] = 1
    out['point'] = v
    v = np.zeros(n)
    i1, i2 = rng.sample(range(n), 2)
    v[i1], v[i2] = 0.7, 0.3
    out['two-point'] = v
    return out


def kernel(p, mu):
    K = np.zeros((p, p))
    for (r, b), v in mu.items():
        for x in range(p):
            K[(r * x + b) % p, x] += v
    return K


worst_i = 0.0
worst_ii = 0.0
for p in (13, 17, 29, 37, 41, 53, 61):
    gam, log, inv, Q = setup(p)
    Qset = set(Q)
    n = (p - 1) // 2
    for name, nu in laws(p, rng).items():
        g, f = actual_g(p, log, nu)
        tol = 1e-9 * max(1.0, g.sum())
        h3 = max(abs(g[x] - g[inv[x]]) for x in range(1, p))
        # omega(alpha_k) = (1/(p-1)) sum_x g(x) conj(alpha_k(x))
        chars = np.zeros((p - 1, p), dtype=complex)  # chars[k, x] = alpha_k(x), alpha_k(0) = 0
        for k in range(p - 1):
            for x in range(1, p):
                chars[k, x] = cmath.exp(2j * math.pi * k * log[x] / (p - 1))
        omega = (chars.conj() @ g) / (p - 1)
        lam_nu = np.array([sum(nu[j] * nu[(j - kk) % n] for j in range(n)) for kk in range(n)])
        om_ok = (np.max(np.abs(omega.imag)) < 1e-12 and omega.real.min() > -1e-12
                 and np.allclose(omega.real[:n], lam_nu / 2, atol=1e-12)
                 and np.allclose(omega.real[n:], lam_nu / 2, atol=1e-12)
                 and abs(omega.real.sum() - 1) < 1e-12)
        om = omega.real
        G = g.sum()
        Gam = (g ** 2).sum()
        W = (g * (1 - g)).sum()
        om_ok &= abs(G - (p - 1) * om[0]) < 1e-9 and abs(Gam - (p - 1) * (om ** 2).sum()) < 1e-9
        mu = chart(p, list(g), inv, Qset)
        if not mu:
            continue
        m = np.zeros(p)
        mp = np.zeros(p)
        for (r, b), v in mu.items():
            m[r] += v
            mp[b] += v
        M1 = sum(mu.values())
        c = sum(v * v for v in mu.values())
        X = (m ** 2).sum()
        L0 = (mp ** 2).sum()
        D0 = np.zeros(p)
        for (r, b), v in mu.items():
            for lam in range(1, p):
                w = mu.get((lam * r % p, b))
                if w:
                    D0[lam] += v * w
        T0 = float((g * D0).sum())
        cg = np.array([0.0] + [sum(g[x] * g[l * x % p] for x in range(1, p)) for l in range(1, p)])
        Tcal = float((cg * D0).sum())
        K = kernel(p, mu)
        # Lemma A2
        a2 = 0.0
        s0max = 0.0
        for k in range(1, p - 1):
            chi = chars[k]
            lhs = np.linalg.norm(K @ chi) ** 2
            A = np.array([sum(v * np.conj(chi[r]) for (r, bb), v in mu.items() if bb == b) for b in range(p)])
            S0 = (np.abs(A) ** 2).sum()
            S0b = (chi * D0).sum()
            mhat = sum(m[r] * np.conj(chi[r]) for r in range(1, p))
            rhs = p * S0 - abs(mhat) ** 2
            a2 = max(a2, abs(lhs - rhs) / max(1, lhs), abs(S0 - S0b) / max(1, S0))
            s0max = max(s0max, S0 / L0)
        # Theorem A
        ri = 0.0
        tot = 0.0
        wsum = 0.0
        split = 0.0
        for t in range(1, p):
            ht = np.zeros(p)
            for e in range(1, p):
                ht[e] = g[t * inv[e] % p]
            phi = ht - G / p
            v = K @ phi
            nv = (v ** 2).sum()
            ri = max(ri, nv / (p * T0))
            tot += nv
            Kh = K @ ht
            split = max(split, abs((Kh ** 2).sum() - (M1 ** 2 * G ** 2 / p + nv)) / (Kh ** 2).sum())
            wt = g[t] * (1 - g[t])
            wsum += wt * sum(Kh[s] ** 2 for s in range(2, p))
        # t-orthogonality identity
        alph = 0.0
        for k in range(p - 1):
            ab = np.conj(chars[k]).copy()
            if k == 0:
                ab = ab - (p - 1) / p
            alph += om[k] ** 2 * np.linalg.norm(K @ ab) ** 2
        alph *= (p - 1)
        ii_id = abs(tot - alph) / tot
        weighted_rhs = W * M1 ** 2 * G ** 2 / p + p * min(W * T0, Tcal / 4)
        ok_all = (h3 < 1e-12 and om_ok and a2 < 1e-9 and s0max <= 1 + 1e-9 and L0 > 0 and abs(L0 - X) < tol
                  and ri <= 1 + 1e-9 and T0 <= X + tol and T0 >= c - tol and ii_id < 1e-9
                  and tot <= p * Tcal - G ** 2 * X + tol * p and Tcal <= Gam * X + tol and split < 1e-9
                  and wsum <= weighted_rhs + tol * p)
        worst_i = max(worst_i, ri)
        worst_ii = max(worst_ii, tot / (p * Tcal - G ** 2 * X))
        check(f'p={p:2d} {name:9s}: H3 err {h3:.0e}; omega>=0 = lambda/2; A2 rel err {a2:.0e}; '
              f'max_t ||pi phi_t||^2/(pT0) = {ri:.3f}; T0/X = {T0 / X:.3f}; '
              f'sum_t/(pT - G^2X) = {tot / (p * Tcal - G ** 2 * X):.3f}; weighted/rhs = '
              f'{(wsum / weighted_rhs) if weighted_rhs > 0 else 0.0:.3f}', ok_all)
print(f'  worst ratio in (i): {worst_i:.3f};  worst ratio in (ii): {worst_ii:.3f}')

# physical form of T0 - c at one prime
p = 37
gam, log, inv, Q = setup(p)
Qset = set(Q)
nu = laws(p, random.Random(5))['interval']
g, f = actual_g(p, log, nu)
mu = chart(p, list(g), inv, Qset)
D0 = np.zeros(p)
for (r, b), v in mu.items():
    for lam in range(1, p):
        w = mu.get((lam * r % p, b))
        if w:
            D0[lam] += v * w
c = sum(v * v for v in mu.values())
T0 = float((g * D0).sum())
direct = 0.0
upper = 0.0
for Y in range(2, p):
    for Y2 in range(2, p):
        if Y2 == Y or g[Y] * g[Y2] == 0:
            continue
        wgt = g[Y] * g[Y2] * g[Y2 * inv[Y] % p]
        if wgt == 0:
            continue
        s = 0.0
        for b in Q:
            # D/(1-D) = b Y/(1-Y)  => D = z/(1+z), z = bY/(1-Y)
            out = []
            for YY in (Y, Y2):
                z = b * YY % p * inv[(1 - YY) % p] % p
                if (1 + z) % p == 0:
                    out.append(None)
                    continue
                D = z * inv[(1 + z) % p] % p
                out.append(D)
            if None in out or out[0] in (0, 1, Y) or out[1] in (0, 1, Y2) or b == 1:
                continue
            s += g[out[0]] * g[out[1]]
        direct += wgt * s
        phiY = Y * inv[(1 - Y) % p] % p
        phiY2 = Y2 * inv[(1 - Y2) % p] % p
        upper += wgt * c_h(p, list(g), phiY * inv[phiY2] % p)
check(f'physical form at p=37 (interval law): T0 - c = {T0 - c:.6f}, triangle sum = {direct:.6f}, c_h upper = {upper:.6f}',
      T0 - c > 1e-3 and abs((T0 - c) - direct) < 1e-9 * max(1, T0) and direct <= upper + 1e-9)

# auditor's remark: T0 - c <= (T3(g) * G * E^x(h))^(1/2), T3(g) = sum_{x,y} g(x) g(y) g(y/x) = (p-1)^2 sum omega^3
print('  auditor remarks: T0 - c <= (T3 G E^x(h))^(1/2), T3 = sum g(x)g(y)g(y/x) = (p-1)^2 sum omega^3;'
      ' T0 <= c + (Gamma_2 D0* X)^(1/2); D0* <= (Gamma_tot E^x(h))^(1/2)')
for p in (29, 37, 53):
    gam, log, inv, Q = setup(p)
    Qset = set(Q)
    for name, nu in laws(p, random.Random(77 + p)).items():
        if name == 'point':
            continue
        g, f = actual_g(p, log, nu)
        mu = chart(p, list(g), inv, Qset)
        D0 = np.zeros(p)
        for (r, b), v in mu.items():
            for lam in range(1, p):
                w = mu.get((lam * r % p, b))
                if w:
                    D0[lam] += v * w
        c = sum(v * v for v in mu.values())
        T0 = float((g * D0).sum())
        T3 = sum(g[x] * g[y] * g[y * inv[x] % p] for x in range(1, p) for y in range(1, p))
        chars = np.array([[cmath.exp(2j * math.pi * k * log[x] / (p - 1)) if x else 0 for x in range(p)]
                          for k in range(p - 1)])
        om = ((chars.conj() @ g) / (p - 1)).real
        Eh = sum(c_h(p, list(g), k) ** 2 for k in range(1, p))
        G = g.sum()
        bound = math.sqrt(T3 * G * Eh)
        X = sum(v * v for v in marginals(p, mu)[0])
        Gam2 = (g ** 2).sum() - 1
        D0s = max(D0[2:])
        b2 = c + math.sqrt(Gam2 * D0s * X)
        b3 = math.sqrt((g ** 2).sum() * Eh)
        check(f'p={p} {name:9s}: T0 = {T0:.4f} <= c + (Gamma_2 D0* X)^(1/2) = {b2:.4f}; '
              f'D0* = max_(l!=1) Delta(l,0) = {D0s:.4f} <= (Gamma_tot E^x(h))^(1/2) = {b3:.4f}',
              T0 <= b2 + 1e-9 and D0s <= b3 + 1e-9)
        check(f'p={p} {name:9s}: T0 - c = {T0 - c:.4f} <= (T3 G Eh)^(1/2) = {bound:.4f}; T3 = (p-1)^2 sum omega^3 '
              f'({T3:.4f} vs {(p - 1) ** 2 * (om ** 3).sum():.4f}); T3/(G Gamma) = {T3 / (G * (g ** 2).sum()):.3f}',
              T0 - c <= bound + 1e-9 and abs(T3 - (p - 1) ** 2 * (om ** 3).sum()) < 1e-8 * max(1, T3)
              and T3 <= G * (g ** 2).sum() + 1e-9)

# ---------------------------------------------------------------- Part C
print('\n== Part C: negative control (omega with negative entries) ==')
viol = 0
maxr = 0.0
for p in (29, 37, 41, 53):
    gam, log, inv, Q = setup(p)
    Qset = set(Q)
    for trial in range(6):
        rr = random.Random(1000 * p + trial)
        g = np.zeros(p)
        # sparse 0/1 inversion-symmetric weight on Q with g(1) = 1 (not of the form |f|^2 in general)
        sel = rr.sample([x for x in Q if x != 1], max(2, int(math.sqrt(p))))
        for x in sel:
            g[x] = 1.0
            g[inv[x]] = 1.0
        g[1] = 1.0
        chars = np.array([[cmath.exp(2j * math.pi * k * log[x] / (p - 1)) if x else 0 for x in range(p)]
                          for k in range(p - 1)])
        om = ((chars.conj() @ g) / (p - 1)).real
        mu = chart(p, list(g), inv, Qset)
        D0 = np.zeros(p)
        for (r, b), v in mu.items():
            for lam in range(1, p):
                w = mu.get((lam * r % p, b))
                if w:
                    D0[lam] += v * w
        T0 = float((g * D0).sum())
        K = kernel(p, mu)
        G = g.sum()
        r_ = 0.0
        for t in range(1, p):
            ht = np.array([0.0] + [g[t * inv[e] % p] for e in range(1, p)])
            v = K @ (ht - G / p)
            r_ = max(r_, (v ** 2).sum() / (p * T0))
        maxr = max(maxr, r_)
        if r_ > 1 + 1e-9:
            viol += 1
print(f'  sparse inversion-symmetric 0/1 weights (min omega < 0 in general): max_t ||pi phi_t||^2/(p T0) = {maxr:.3f};'
      f' violations of (i): {viol} of 24')
print('  (evidence only: whether (i) survives without omega >= 0 is not claimed by BPP and not needed)')

# ---------------------------------------------------------------- Part D
print('\n== Part D: exponents (exact Fractions) ==')
h = F(1, 2)            # G, W, Gamma_tot <= p^(1/2)
eX187 = F(4, 3)        # Round 187 Cor. 4 (plus o(1))
eE187 = F(8, 3)
cov_RS = lambda eE: F(9, 8) + eE / 4
cov_OP = lambda gam, eE: gam + eE / 2
cov_CH = lambda w, eX: w + eX           # min(W, Gamma/4) X with W ~ p^w
check('RS at E = p^(8/3): 43/24', cov_RS(eE187) == F(43, 24))
check('43/24 = 115/64 - 1/192', F(43, 24) == F(115, 64) - F(1, 192))
check('CH unconditional: 1/2 + 4/3 = 11/6, worse than 43/24 by 1/24', cov_CH(h, eX187) == F(11, 6)
      and F(11, 6) - F(43, 24) == F(1, 24))
check('OP at gamma = 1/2, E = p^(8/3): 11/6', cov_OP(h, eE187) == F(11, 6))
check('RS floor at E >= M1^4/p^2 = p^2: 13/8', cov_RS(F(2)) == F(13, 8))
check('point-plane floor E >= p^(5/2): RS 7/4 and OP(gamma=1/2) 7/4', cov_RS(F(5, 2)) == F(7, 4) == cov_OP(h, F(5, 2)))
check('X = p^(1+eps): 3/2 + eps; < 7/4 iff eps < 1/4; < 43/24 iff eps < 7/24',
      cov_CH(h, 1 + F(1, 4)) == F(7, 4) and cov_CH(h, 1 + F(7, 24)) == F(43, 24))
check('vs Round 184 Prop 1(ii) 7/4 + eps/8: crossover eps = 2/7', F(3, 2) + F(2, 7) == F(7, 4) + F(2, 7) / 8)
check('X at the first-mass target 1 + 1/1280: covariance 3/2 + 1/1280', cov_CH(h, 1 + F(1, 1280)) == F(3, 2) + F(1, 1280))
# Corollary B1: min(1 + 2 gamma, gamma + 4/3, 43/24)
cb1 = lambda gm: min(1 + 2 * gm, gm + F(4, 3), F(43, 24))
check('B1 thresholds: gamma = 1/4 -> 3/2; < 7/4 iff gamma < 5/12; < 43/24 iff gamma < 11/24',
      cb1(F(1, 4)) == F(3, 2) and cb1(F(5, 12)) == F(7, 4) and cb1(F(5, 12) - F(1, 1000)) < F(7, 4)
      and cb1(F(11, 24)) == F(43, 24) and cb1(F(11, 24) - F(1, 1000)) < F(43, 24))
check('B1 branch 1 + 2 gamma below 7/4 only for gamma < 3/8; at gamma = 3/8 min = 41/24; at 1/3 both = 5/3',
      cb1(F(3, 8)) == F(41, 24) and 1 + 2 * F(1, 3) == F(1, 3) + F(4, 3) == F(5, 3))
check('translation fibre: Gamma_tot (c X)^(1/2) with c <= p: 1/2 + (1 + 4/3)/2 = 5/3', h + (1 + eX187) / 2 == F(5, 3))
check('E_(!=1) <= p^(5/2 - d) -> 7/4 - d/2 (gamma = 1/2)', cov_OP(h, F(5, 2) - F(1, 10)) == F(7, 4) - F(1, 20))
check('uniform second norm: ||H(.,t)||^2 <= p^2 + p X -> p^(7/3), norm 7/6; RS value (1/2)(1/2 + 43/24 + 1) ... = 55/48',
      max(F(2), 1 + eX187) / 2 == F(7, 6) and (F(43, 24) + 1 - h) / 2 == F(55, 48))
check('Young barrier: tau_0 G^3 <= p^(5/4) iff tau_0 <= p^(-1/4); height-1 N^(5/2) at N = p^(1/2) is p^(5/4)',
      -F(1, 4) + 3 * h == F(5, 4) and F(5, 2) * h == F(5, 4) and F(8, 3) * h == F(4, 3))
check('flat-law support energy: n E(nu) = p^(1/4), |S| = p^(1/2): E(S) = p^(1/4) |S|^4 / p = |S|^(5/2)',
      F(1, 4) + 4 * h - 1 == F(5, 2) * h)

# auditor remarks (Theorem A uniform branch with T0 <= c + (Gamma_2 D0* X)^(1/2), W, Gamma_2 <= p^(1/2))
rem = lambda eX, d: h + (h + d + eX) / 2
check('remark: covariance <= p^(1/2 + (1/2 + d + e_X)/2); at e_X = 4/3: 17/12 + d/2; = 7/4 at d = 2/3, = 43/24 at d = 3/4',
      rem(eX187, F(2, 3)) == F(7, 4) and rem(eX187, F(3, 4)) == F(43, 24) and rem(eX187, F(0)) == F(17, 12))
check('remark: D0* <= (Gamma_tot E^x(h))^(1/2) gives d = 11/12 now and d = 3/4 at the floor E^x(h) = p',
      (h + eX187) / 2 == F(11, 12) and (h + 1) / 2 == F(3, 4))
check('remark: T3 route T0 - c <= (T3 G E^x(h))^(1/2): covariance 1/2 + (t3 + 1/2 + 4/3)/2 < 7/4 iff t3 < 2/3',
      h + (F(2, 3) + h + eX187) / 2 == F(7, 4))

print('\nALL AUDIT CHECKS OK' if OK else '\nSOME AUDIT CHECK FAILED')
