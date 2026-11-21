#!/usr/bin/env python3
"""Round 193 audit: floating-point diagnostics for call ordinary-ss-star-literature.

Evidence only, not proof. For explicit sets S in Z/N and a level a it prints
  low/M         = sum_{xi != 0, g < a} g / (N/|S| - 1),
  Lemma1 bound  = (N r/|S|^2)(1 + 16 a/(1 - sqrt a)^2) / M  (for S = H u E, r = |E|),
  sup d(h,Z)    = max_x dist(h(x), Z), h = projection of 1_S onto {g >= a},
  #exc          = #{x : |1_S(x) - h(x)| >= 1/4}.
The audit's point: Lemma 1's examples have many exceptional points for
1_S - h, yet h itself stays uniformly close to an integer-valued function, so
Lemma 1 does not show that the sup-norm hypothesis d(h, Z) small (Green-Sanders
Lemma 3.1 applied to h) is out of reach.
Usage: python3 -B research/paley-193-audit-ssstar.py
"""
import cmath
import math
import random


def analyse(name, S, N, a, r=None):
    S = sorted(set(x % N for x in S))
    s = len(S)
    w = [cmath.exp(-2j * math.pi * k / N) for k in range(N)]
    F = [sum(w[(x * xi) % N] for x in S) for xi in range(N)]
    g = [abs(z) ** 2 / s ** 2 for z in F]
    M = N / s - 1
    low = sum(g[xi] for xi in range(1, N) if g[xi] < a)
    Lam = [xi for xi in range(N) if g[xi] >= a]
    winv = [cmath.exp(2j * math.pi * k / N) for k in range(N)]
    Sset = set(S)
    supd = 0.0
    exc = 0
    for x in range(N):
        hx = (sum(F[xi] * winv[(x * xi) % N] for xi in Lam) / N).real
        supd = max(supd, abs(hx - round(hx)))
        if abs((1.0 if x in Sset else 0.0) - hx) >= 0.25:
            exc += 1
    line = (f"{name:30s} N={N:5d} |S|={s:3d} a={a:.4f} low/M={low / M:.3f} "
            f"sup d(h,Z)={supd:.3f} #exc={exc:3d}")
    ok = True
    if r is not None:
        bound = (N * r / s ** 2) * (1 + 16 * a / (1 - math.sqrt(a)) ** 2) / M
        line += f" Lemma1 bound/M={bound:.3f}"
        ok = low <= bound * M + 1e-9
    print(line)
    return ok


def main():
    ok = True
    rng = random.Random(1931)
    m = 30
    N = 2 * m * m
    H = [60 * j for j in range(m)]
    ok &= analyse("subgroup", H, N, 0.25, r=0)
    for r in (2, 5, 7):
        extra = rng.sample([x for x in range(N) if x % 60], r)
        ok &= analyse(f"subgroup + {r} random points", H + extra, N, 0.25, r=r)
    # removed points: a subgroup minus a coset of a subgroup K of H (|K| = 3)
    K = [600 * j for j in range(3)]
    ok &= analyse("subgroup minus 3-coset", [x for x in H if x not in K], N, 0.25)
    N2 = 1920
    S2 = [1 + 128 * j for j in range(15)] + [2 + 120 * j for j in range(16)]
    ok &= analyse("1+H_15 u 2+H_16", S2, N2, 1 / 16)
    ok &= analyse("1+H_15 u 2+H_16 + 3 pts", S2 + rng.sample(range(N2), 3), N2, 1 / 16)
    ok &= analyse("interval", list(range(m)), N, 0.25)
    print("ALL OK" if ok else "FAILED")


if __name__ == "__main__":
    main()
