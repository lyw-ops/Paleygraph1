#!/usr/bin/env python3
"""Round 184 (near-critical support energy): floating evidence only.

For a prime p = 1 mod 4, Q = squares, n = (p-1)/2, m0 = n/sqrt(p), and
k(d) = p^{-1/2} sum_{x in Q} chi(1-x) psi^d(x)  (real, |k| <= 1; Round 20 notation),
search for flat sets S in Z/n of size m = round(m0) maximising the signed pair
average  avg_sigma(S) = |S|^{-2} sum_{s,s' in S} sigma k(s-s').
Near-criticality (NC) of a flat law on S is exactly avg_sigma(S) -> 1 with |S| ~ m0
(Round 19 section 3 / Round 20 flattening).  For the best sets found we report
E(S)/|S|^3 and the overlap profile q(a) = |S cap (S+a)|/|S|.

This is a heuristic search: it gives lower bounds for the best pair average over
flat sets at finite p, not the maximum, and says nothing asymptotic.
Usage: .venv/bin/python -B research/paley-184-energy-search.py [p ...] [--restarts R]
"""
import sys
import numpy as np


def primitive_root(p):
    phi = p - 1
    fac, m, d = [], phi, 2
    while d * d <= m:
        if m % d == 0:
            fac.append(d)
            while m % d == 0:
                m //= d
        d += 1
    if m > 1:
        fac.append(m)
    for g in range(2, p):
        if all(pow(g, phi // q, p) != 1 for q in fac):
            return g


def kernel(p):
    n = (p - 1) // 2
    th = primitive_root(p)
    th2 = th * th % p
    x = np.empty(n, dtype=np.int64)
    v = 1
    for i in range(n):
        x[i] = v
        v = v * th2 % p
    # chi(1-x) via Euler criterion, vectorised by pow on python ints (n small enough)
    s = np.array([0 if int(xi) == 1 else (1 if pow(int(1 - xi) % p, n, p) == 1 else -1) for xi in x],
                 dtype=float)
    # k(d) = p^{-1/2} sum_i s_i e(d i / n); s even => real
    k = np.fft.fft(s).conj().real / np.sqrt(p)  # sum_i s_i e^{+2 pi i d i/n}
    return n, k, s


def energy_profile(S, n):
    ind = np.zeros(n)
    ind[list(S)] = 1.0
    F = np.fft.fft(ind)
    r = np.fft.ifft(np.abs(F) ** 2).real  # r(a) = |S cap (S+a)|
    r = np.rint(r)
    m = len(S)
    E = float((r ** 2).sum())
    q = r / m
    q_off = np.delete(q, 0)
    return E / m ** 3, float(q_off.max()), q


def local_search(kk, n, m, rng, start=None, iters=20000, allowed=None):
    """kk = sigma*k.  Maximise F(S)=sum_{s,s'} kk(s-s') at fixed |S|=m."""
    if start is None:
        S = list(rng.choice(n, size=m, replace=False))
    else:
        S = list(start)
    inS = np.zeros(n, dtype=bool)
    inS[S] = True
    ind = inS.astype(float)
    # c(j) = sum_{s in S} kk(j-s)  (circular convolution)
    c = np.fft.ifft(np.fft.fft(kk) * np.fft.fft(ind)).real
    k0 = kk[0]
    stall = 0
    for _ in range(iters):
        Sarr = np.flatnonzero(inS)
        o = Sarr[np.argmin(c[Sarr])]
        cc = np.where(inS, -np.inf, c)
        if allowed is not None:
            cc = np.where(allowed, cc, -np.inf)
        # consider top candidates for i
        top = np.argpartition(-cc, 8)[:8]
        best, bi = 0.0, -1
        for i in top:
            d = 2 * c[i] - 2 * c[o] - 2 * kk[(i - o) % n] + 2 * k0
            if d > best + 1e-12:
                best, bi = d, i
        if bi < 0:
            # random perturbation: swap a random member with a random good outsider
            stall += 1
            if stall > 30:
                break
            o = rng.choice(Sarr)
            bi = top[rng.integers(len(top))]
        else:
            stall = 0
        inS[o] = False
        inS[bi] = True
        c += np.roll(kk, bi) - np.roll(kk, o)
    S = np.flatnonzero(inS)
    Fval = float(c[S].sum())
    return S, Fval / m ** 2


def greedy_build(kk, n, m, seed_pt=0):
    inS = np.zeros(n, dtype=bool)
    inS[seed_pt] = True
    c = np.roll(kk, seed_pt).copy()
    for _ in range(m - 1):
        cc = np.where(inS, -np.inf, c)
        i = int(np.argmax(cc))
        inS[i] = True
        c += np.roll(kk, i)
    return np.flatnonzero(inS)


def main():
    args = sys.argv[1:]
    R = 6
    if '--restarts' in args:
        j = args.index('--restarts')
        R = int(args[j + 1])
        del args[j:j + 2]
    primes = [int(a) for a in args] or [1009, 4001, 10009, 40009]
    print("p n m0 m sigma | start | avg_sigma(S) | E(S)/|S|^3 | max_{a!=0} q(a) | #{a!=0: q>=0.4}")
    for p in primes:
        assert p % 4 == 1
        n, k, s = kernel(p)
        m0 = n / np.sqrt(p)
        m = int(round(m0))
        rng = np.random.default_rng(p)
        for sigma in (+1, -1):
            kk = sigma * k
            rows = []
            for t in range(R):
                S, avg = local_search(kk, n, m, rng)
                rows.append(("rand%d" % t, S, avg))
            Sg = greedy_build(kk, n, m)
            S, avg = local_search(kk, n, m, rng, start=Sg)
            rows.append(("greedy", S, avg))
            # subgroup-subset starts: H = subgroup of Z/n of order h, m <= h <= 4m
            for h in range(m, 4 * m + 1):
                if n % h:
                    continue
                allowed = np.zeros(n, dtype=bool)
                allowed[::n // h] = True
                start = list(rng.choice(np.flatnonzero(allowed), size=m, replace=False))
                SH, avgH = local_search(kk, n, m, rng, start=start, allowed=allowed)
                rows.append(("inH%d" % h, SH, avgH))
                S2, avg2 = local_search(kk, n, m, rng, start=SH)
                rows.append(("fromH%d" % h, S2, avg2))
            for name, S, avg in rows:
                e, qmax, q = energy_profile(S, n)
                big = int((np.delete(q, 0) >= 0.4).sum())
                print(f"{p} {n} {m0:.2f} {m} {sigma:+d} | {name} | {avg:.4f} | {e:.4f} | {qmax:.3f} | {big}")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
