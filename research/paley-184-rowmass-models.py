#!/usr/bin/env python3
r"""Round 184, call ordinary-prime-near-critical-slope-row-mass: prime models.

Floating evidence only (numpy float64). Every model is a FLAT law: nu uniform on
a set S of characters of Q (identified with Z/n, 0 not in S, |S| ~ m_0 = n/sqrt p),
f = sum_{j in S} nu_j j on Q, g = |f|^2, h(z) = g(1-z). So (H1), (H2), (H4) hold,
m_eff = |S|, and the only near-critical requirement left is sector concentration
rho * sum_x g(x) chi(1-x) ~ sqrt p (Round 183, Proposition 1.2). For flat laws

    sum_{x in Q} g(x) chi(1-x) = (sqrt p / |S|^2) * sum_{i,j in S} k(i-j),
    k(d) = p^{-1/2} sum_{x in Q} chi(1-x) conj(d(x))   (real, |k| <= 1),

so sector concentration means: the average of rho*k over S x S tends to 1.
Models (S chosen in Z/n \ {0}):
  rand    random S;
  opt     local search maximizing rho * sum_{S x S} k (greedy + swaps, restarts);
  apbest  the arithmetic progression a*{1..m} maximizing rho * sum k over all a
          (physically a Fejer kernel on a geometric progression: log-interval type);
  aphalf  a random half of the best progression of length 2m (energy ~ |S|^3/3,
          admissible for the Round 20 gap, unlike a full progression, energy 2/3);
  ap+rand S = A + B, A the best progression of length m/b, B random of size b
          (an intermediate-height configuration: a log-interval lobe of length
          about b*sqrt p carrying the mass of g at heights about 1/b);
  coset   S = nonzero part of a subgroup of Z/n of order near m (coset model,
          excluded on (NC) by Round 151 and by the Round 20 gap; control only).
Printed per model: |S|/m_0, sector tightness s = rho sum g chi(1-x)/sqrt p,
G/sqrt p, G_{-rho}, E(S)/|S|^3, Gamma_2 = sum_{x!=1} g^2 (/sqrt p), X/p,
max_xi W_xi / p, sup_{lambda!=1} C(lambda)/p, the Young ratio X/((G-1)^2 Gamma_2),
the floor ratio X/(M_1^2/(n-1)), and the largest slope fibre max c_h.

Usage: .venv/bin/python -B research/paley-184-rowmass-models.py P [P ...]
"""
import sys
import numpy as np


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
        if all(pow(g, (p - 1) // f, p) != 1 for f in fac):
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
    # Q = theta^(2i); chi(1 - theta^(2i))
    xs = exp[0::2]  # x_i = theta^(2i), i = 0..n-1
    chi1 = leg[(1 - xs) % p]
    # k(d) = p^{-1/2} sum_i chi1[i] e(-d i / n)
    kd = np.fft.fft(chi1) / np.sqrt(p)
    assert np.max(np.abs(kd.imag)) < 1e-6 * np.sqrt(n)
    k = kd.real
    assert np.max(np.abs(k)) <= 1 + 1e-9
    return dict(p=p, N=N, n=n, exp=exp, log=log, leg=leg, xs=xs, chi1=chi1, k=k)


def mconv(a, b):
    return np.fft.irfft(np.fft.rfft(a) * np.fft.rfft(b), len(a))


def mcorr(a, b):
    return np.fft.irfft(np.conj(np.fft.rfft(a)) * np.fft.rfft(b), len(a))


def phi(k, S, rho):
    S = np.asarray(S)
    d = (S[:, None] - S[None, :]) % len(k)
    return rho * k[d].sum()


def local_search(k, m, rho, rng, restarts=3, maxit=None):
    n = len(k)
    rk = rho * k
    best = None
    for _ in range(restarts):
        # greedy build from a random seed
        s0 = int(rng.integers(1, n))
        inS = np.zeros(n, dtype=bool)
        inS[s0] = True
        score = np.roll(rk, s0)  # score[x] = sum_{j in S} rk[x - j]
        score_ok = score.copy()
        S = [s0]
        while len(S) < m:
            cand = np.where(inS, -np.inf, score)
            cand[0] = -np.inf
            # random tie-breaking among the top few
            top = np.argpartition(-cand, 5)[:5]
            x = int(top[rng.integers(0, 5)]) if len(S) < m // 3 else int(np.argmax(cand))
            inS[x] = True
            S.append(x)
            score += np.roll(rk, x)
        # swap improvement
        it = 0
        lim = maxit or 20 * m
        while it < lim:
            it += 1
            Sarr = np.nonzero(inS)[0]
            ys = Sarr[np.argsort(score[Sarr])[:8]]
            cand = np.where(inS, -np.inf, score)
            cand[0] = -np.inf
            xs = np.argpartition(-cand, 8)[:8]
            bestgain, pair = 0.0, None
            for y in ys:
                for x in xs:
                    gain = 2 * (score[x] - rk[(x - y) % n]) - 2 * score[y] + 2 * rk[0]
                    if gain > bestgain + 1e-12:
                        bestgain, pair = gain, (int(x), int(y))
            if pair is None:
                break
            x, y = pair
            inS[y] = False
            score -= np.roll(rk, y)
            inS[x] = True
            score += np.roll(rk, x)
        S = np.nonzero(inS)[0]
        val = phi(k, S, rho)
        if best is None or val > best[0]:
            best = (val, S)
    return best[1]


def best_ap(k, m, rho, n):
    # Phi(a*{1..m}) = sum_{|d|<m} (m-|d|) rho k(a d); evaluate for all a coprime to n
    from math import gcd
    ds = np.arange(-(m - 1), m)
    wts = (m - np.abs(ds)).astype(float)
    best = (-np.inf, None)
    for a in range(1, n):
        if gcd(a, n) != 1:
            continue
        v = rho * np.dot(wts, k[(a * ds) % n])
        if v > best[0]:
            best = (v, a)
    return best[1]


def measure(env, S, rho):
    p, N, n = env['p'], env['N'], env['n']
    S = np.asarray(sorted(set(int(s) % n for s in S)))
    assert 0 not in S
    m = len(S)
    ind = np.zeros(n)
    ind[S] = 1.0
    # f(x_i) = (1/m) sum_{j in S} e(j i / n)
    f = np.fft.ifft(ind) * n / m
    gQ = np.abs(f) ** 2
    assert abs(gQ[0] - 1) < 1e-9
    # g on F_p (index by element)
    g = np.zeros(p)
    g[env['xs']] = gQ
    G = g.sum()
    m0 = n / np.sqrt(p)
    chi1 = env['chi1']
    sgc = float(np.dot(gQ, chi1))
    Gm = float(gQ[chi1 == -rho].sum())
    # additive energy of S in Z/n
    Fh = np.fft.fft(ind)
    ES = float(np.sum(np.abs(Fh) ** 4) / n)
    Gam2 = float((gQ[1:] ** 2).sum())
    # h(z) = g(1-z) on F_p^*, by log index
    exp, log = env['exp'], env['log']
    hz = g[(1 - exp) % p]
    c = mcorr(hz, hz)  # c[t] = c_h(theta^t)
    tt = np.arange(N)
    selQ = (tt % 2 == 0) & (tt != 0)
    X = float(np.sum(c[selQ] ** 2))
    M1 = float(np.sum(c[selQ]))
    # m(r) = c_h(1-r) for 1-r in Q\{1}; r = theta^t
    one_minus_r = (1 - exp) % p
    lu = log[one_minus_r]
    okr = (lu >= 0) & (lu % 2 == 0) & (lu != 0)
    mr = np.zeros(N)
    mr[okr] = c[lu[okr]]
    W = mconv(mr, mr)
    C = mcorr(mr, mr)
    maxW = float(W.max())
    supC = float(C[1:].max())
    assert abs(C[0] - X) < 1e-6 * max(1, X)
    young = (G - 1) ** 2 * Gam2
    return dict(m=m, m_m0=m / m0, s=rho * sgc / np.sqrt(p), G=G / np.sqrt(p), Gm=Gm,
                ES=ES / m ** 3, Gam2=Gam2 / np.sqrt(p), Xp=X / p, Wp=maxW / p, Cp=supC / p,
                young=X / young, floor=X / (M1 ** 2 / (n - 1)), maxc=float(c[selQ].max()))


def run(p, seed=0):
    env = setup(p)
    n, k = env['n'], env['k']
    m0 = n / np.sqrt(p)
    m = int(round(m0))
    rng = np.random.default_rng(seed + p)
    rows = []
    for rho in (1, -1):
        rows.append(('rand', rho, rng.choice(np.arange(1, n), m, replace=False)))
        rows.append(('opt', rho, local_search(k, m, rho, rng)))
        a = best_ap(k, m, rho, n)
        rows.append((f'apbest a={a}', rho, (a * np.arange(1, m + 1)) % n))
        a2 = best_ap(k, 2 * m, rho, n)
        full = (a2 * np.arange(1, 2 * m + 1)) % n
        rows.append((f'aphalf a={a2}', rho, rng.choice(full, m, replace=False)))
        # progression (+) random: S = A + B, A = best AP of length m/b, B random of size b;
        # physically a log-interval lobe of length ~ b*sqrt(p) at heights ~ 1/b
        for b in (4, 16):
            la = max(2, m // b)
            a3 = best_ap(k, la, rho, n)
            A = (a3 * np.arange(1, la + 1)) % n
            for _ in range(50):
                B = rng.choice(np.arange(n), b, replace=False)
                Ssum = (A[:, None] + B[None, :]).ravel() % n
                if len(set(Ssum.tolist())) == la * b and 0 not in set(Ssum.tolist()):
                    break
            rows.append((f'ap+rand b={b}', rho, Ssum))
    # coset control: subgroup of Z/n with order d closest to m (d | n), only if 1/2 <= d/m <= 2
    divs = [d for d in range(2, n) if n % d == 0 and 0.5 <= d / m <= 2]
    if divs:
        d = min(divs, key=lambda d: abs(d - m))
        sub = np.arange(n // d, n, n // d)
        rows.append((f'coset d={d}', 0, sub))
    out = []
    for name, rho, S in rows:
        r = measure(env, S, rho if rho != 0 else 1)
        out.append((name, rho, r))
    return out


def main():
    ps = [int(a) for a in sys.argv[1:]] or [1009, 4001]
    print("flat-law models; floating evidence only")
    print(f"{'p':>7} {'model':>16} {'rho':>3} {'|S|/m0':>6} {'s':>6} {'G/rp':>5} {'G_-r':>6} "
          f"{'E(S)/S3':>7} {'Gam2/rp':>7} {'X/p':>7} {'maxW/p':>7} {'supC/p':>7} "
          f"{'X/Young':>7} {'X/floor':>7} {'maxc':>6}")
    for p in ps:
        for name, rho, r in run(p):
            print(f"{p:7d} {name:>16} {rho:3d} {r['m_m0']:6.3f} {r['s']:6.3f} {r['G']:5.3f} "
                  f"{r['Gm']:6.1f} {r['ES']:7.4f} {r['Gam2']:7.4f} {r['Xp']:7.3f} {r['Wp']:7.3f} "
                  f"{r['Cp']:7.3f} {r['young']:7.4f} {r['floor']:7.3f} {r['maxc']:6.2f}")
        sys.stdout.flush()


if __name__ == "__main__":
    main()
