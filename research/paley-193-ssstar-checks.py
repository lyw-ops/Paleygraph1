#!/usr/bin/env python3
"""Round 193, call ordinary-ss-star-literature: finite checks (evidence only).

Floating-point diagnostics on small explicit sets in Z/N.  Nothing here is a
proof; the report's statements are proved by hand.  The script checks, on
examples, the normalisations used to compare (SS*) with published theorems:

  g(xi) = |1_S^(xi)|^2/|S|^2, M = N/|S| - 1, alpha = |S|/N,
  Lambda = {xi : g(xi) >= a},  h = projection of 1_S onto Lambda,
  ||h||_A = (1/N) sum_{Lambda} |1_S^| <= a^(-1/2)          (Lemma 2(i)),
  E|1_S - h|^2 = alpha^2 * sum_{xi not in Lambda} g          (Lemma 2(ii)),
  #{x : |1_S(x) - h(x)| >= 1/4} <= 16 N E|1_S - h|^2           (Lemma 2(iii)),
  GOSSW Thm 3.4 translation: mu^2 = 4 alpha^2 sum_{not Lambda} g versus
  the required mu <= 1/(20 s^2), s = |Lambda|.

Usage: python3 research/paley-193-ssstar-checks.py
Prints a table and 'ALL OK' if every asserted inequality holds.
"""
import cmath
import math
import random


def dft_abs2(S, N):
    """Return |1_S^(xi)|^2 for xi in Z/N (unnormalised transform)."""
    w = [cmath.exp(-2j * math.pi * k / N) for k in range(N)]
    out = []
    for xi in range(N):
        z = 0j
        for x in S:
            z += w[(x * xi) % N]
        out.append(z)
    return out


def analyse(name, S, N, a):
    S = sorted(set(x % N for x in S))
    s = len(S)
    F = dft_abs2(S, N)
    g = [abs(z) ** 2 / s ** 2 for z in F]
    M = N / s - 1
    alpha = s / N
    low = sum(g[xi] for xi in range(1, N) if g[xi] < a)
    Lam = [xi for xi in range(N) if g[xi] >= a]
    normA_S = sum(abs(z) for z in F) / N
    normA_h = sum(abs(F[xi]) for xi in Lam) / N
    # h(x) = (1/N) sum_{xi in Lam} F(xi) e(x xi / N)
    winv = [cmath.exp(2j * math.pi * k / N) for k in range(N)]
    Sset = set(S)
    err2 = 0.0
    exc = 0
    for x in range(N):
        hx = sum(F[xi] * winv[(x * xi) % N] for xi in Lam) / N
        d = (1.0 if x in Sset else 0.0) - hx.real
        err2 += d * d
        if abs(d) >= 0.25:
            exc += 1
    err2 /= N
    lowmass = sum(g[xi] for xi in range(N) if g[xi] < a)  # includes nothing at 0
    ok = True
    ok &= normA_h <= a ** -0.5 + 1e-9                                # Lemma 2(i)
    ok &= abs(err2 - alpha ** 2 * lowmass) <= 1e-9 * max(1, err2)   # Lemma 2(ii)
    ok &= exc <= 16 * N * err2 + 1e-9                                # Lemma 2(iii)
    mu2 = 4 * alpha ** 2 * lowmass
    need = (1.0 / (20 * len(Lam) ** 2)) ** 2
    print(f"{name:34s} N={N:5d} |S|={s:3d} a={a:.4f} low/M={low / M:.3f} "
          f"||1_S||_A={normA_S:6.3f} ||h||_A={normA_h:5.3f}<= {a ** -0.5:5.3f} "
          f"E|1_S-h|^2/alpha={err2 / alpha:.3f} exc={exc:3d}<= {16 * N * err2:7.2f} "
          f"|Lam|={len(Lam):4d} mu^2={mu2:.2e} GOSSW-need={need:.2e}")
    return ok


def main():
    allok = True
    a = 0.25
    # (1) subgroup of order m = sqrt(N/2) in Z/N, N = 2 m^2: exactly sharp.
    m = 30
    N = 2 * m * m
    H = [60 * j for j in range(m)]
    allok &= analyse("subgroup", H, N, a)
    # (2) subgroup plus r extra points (Lemma 1: sharp up to O(r/|S|)).
    rng = random.Random(193)
    for r in (2, 5):
        extra = rng.sample([x for x in range(N) if x % 60], r)
        allok &= analyse(f"subgroup + {r} random points", H + extra, N, a)
    # (3) two cosets of different subgroups (Prop. D / Hosseini-Lovett Ex. 1.1 type).
    N2 = 1920
    h1, h2 = 15, 16
    S2 = [1 + (N2 // h1) * j for j in range(h1)] + [2 + (N2 // h2) * j for j in range(h2)]
    allok &= analyse("1+H_15 u 2+H_16", S2, N2, a / 4)
    # (4) interval of length ~ sqrt(N/2): not sharp (Fejer tail).
    allok &= analyse("interval", list(range(m)), N, a)
    # (5) Parameter translations at density alpha = N^(-1/2) (floating).
    print()
    for N in (10 ** 6, 10 ** 12, 10 ** 24):
        alpha = N ** -0.5
        # Croot-Sisask Cor. 1.2: |T| >= (beta/2)^(9/eps^2) |G|, beta = alpha.
        for eps in (0.5, 0.9):
            lg = (9 / eps ** 2) * math.log(alpha / 2) + math.log(N)
            print(f"N=1e{round(math.log10(N)):2d} Croot-Sisask eps={eps}: log|T| >= {lg:9.1f}"
                  f"  (nontrivial iff > 0: {lg > 0})")
            allok &= lg < 0
        # Chang: dim Spec_rho <= C rho^-2 log(1/alpha); at rho^2 = a = 1/4: 4 log(1/alpha) / log N.
        print(f"N=1e{round(math.log10(N)):2d} Chang dimension bound / log N at a=1/4 (C=1): "
              f"{4 * math.log(1 / alpha) / math.log(N):.2f}")
        # Konyagin-Shkredov Thm 3 range: exp((log p/loglog p)^(1/3)) <= |A| <= p/3.
        lo = math.exp((math.log(N) / math.log(math.log(N))) ** (1 / 3))
        s = math.sqrt(N / 2)
        print(f"N=1e{round(math.log10(N)):2d} Konyagin-Shkredov range lower end {lo:9.2f} <= |S|={s:.3e}: {lo <= s}"
              f"; bound (log(N/|S|))^(1/3) = {(math.log(N / s)) ** (1 / 3):.2f}")
        allok &= lo <= s <= N / 3
    print("ALL OK" if allok else "FAILED")


if __name__ == "__main__":
    main()
