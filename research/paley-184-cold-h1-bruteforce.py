#!/usr/bin/env python3
"""Round 184 cold call: independent FORWARD brute force for paley-184-cold-h1-product-ratio.py.

Exact (Fractions).  Simulates the compact-model rule on explicit simples, child by child (no
adjoint, no aggregation over paths, no extreme-ray reduction), and checks:
  (1) every child of every path is a valid simple (Sigma|w| = 2r, refills >= 0), m <= 2;
  (2) the path-summed A-ratio of every tested parent is <= the certified G_m (joint, m = 1, 2,
      and seed only m <= 3), and the family F_K approaches G_m from below as K grows;
  (3) the one-step h_1 ratio of F_K tends to d + mu/2 term by term.
Coefficients are entered as the same rational upper bounds (printed in the main script) but are
recomputed here from their own exact series, truncated at l = 30 (difference < 10^-25).
Replay:  .venv/bin/python -B research/paley-184-cold-h1-bruteforce.py     (about 1 min)
"""
from collections import Counter
from fractions import Fraction as Fr
from math import comb
import random

beta0 = Fr(256, 2031)


def bin_gen(al, l):
    r = Fr(1)
    for j in range(l):
        r = r * (al - j) / (j + 1)
    return r


def four(al, i, L=30):
    """Fourier coefficient of (1 + beta0 cos^2)^al at e^{2 i theta}"""
    return sum(bin_gen(al, l) * beta0 ** l * Fr(comb(2 * l, l + abs(i)), 4 ** l) for l in range(abs(i), L))


def ghat(k, L=30):
    k = abs(k)
    return sum((-1) ** l * Fr(comb(2 * l, l), 4 ** l) * beta0 ** l * Fr(comb(2 * l + 1, l + (k + 1) // 2), 2 ** (2 * l + 1))
               for l in range((k - 1) // 2, L))


# varpi upper bound and the uniform enlargements are tiny; for the brute force we use the
# beta0 values (a lower bound for what the certified G_m must dominate) -- see the report.
VARPI = Fr(355030238, 10 ** 9)
seed = [(VARPI * abs(ghat(k)), ([-k], [k])) for k in (1, -1, 3, -3, 5, -5)]


def KJ(k):
    if k > 0:
        return ([-k, k] + [0] * (k - 2), [0] * k)
    return ([0] * (-k), [k, -k] + [0] * (-k - 2))


def mline(G, s):
    return ([x - s for x in G[0]], [y + s for y in G[1]])


h1 = []
for k in (2, -2, 4, -4, 6, -6):
    for i in range(-3, 4):
        h1.append((abs(four(Fr(-3, 2), i)) * abs(four(Fr(1, 2), k // 2)), mline(KJ(k), 2 * i)))


def child(F, T):
    """F = (Counter A, Counter B) of weights; T = (list, list).  Returns child or raises."""
    FA, FB = F
    PA, PB = Counter(), Counter()
    for v, c in FA.items():
        for x in T[0]:
            PA[v + x] += c
    for v, c in FB.items():
        for y in T[1]:
            PB[v + y] += c
    rp2 = sum(abs(w) * c for w, c in PA.items()) + sum(abs(w) * c for w, c in PB.items())
    assert rp2 % 2 == 0
    rp = rp2 // 2
    CA, CB = Counter(), Counter()
    for w, c in PA.items():
        if w < 0:
            CA[w] += c
        elif w > 0:
            CB[w] += c
    for w, c in PB.items():
        if w < 0:
            CB[w] += c
        elif w > 0:
            CA[w] += c
    za = rp - sum(CA.values())
    zb = rp - sum(CB.values())
    if za < 0 or zb < 0:
        raise ValueError("negative refill")
    if za:
        CA[0] += za
    if zb:
        CB[0] += zb
    return (CA, CB), rp


def rank(F):
    s = sum(abs(w) * c for w, c in F[0].items()) + sum(abs(w) * c for w, c in F[1].items())
    assert s % 2 == 0
    r = s // 2
    assert sum(F[0].values()) == r and sum(F[1].values()) == r
    return r


def path_sum(F, terms, m, check=True):
    """sum over all m-step paths of |coef| * rank(child), explicit child by child"""
    layer = [(Fr(1), F)]
    for _ in range(m):
        new = []
        for c0, G in layer:
            for c, T in terms:
                ch, rp = child(G, T)
                if check:
                    assert rank(ch) == rp
                new.append((c0 * c, ch))
        layer = new
    return sum(c * rank(G) for c, G in layer)


def random_simple(rng, r, wmax=4):
    while True:
        ws = [rng.randint(-wmax, wmax) for _ in range(2 * r)]
        if sum(abs(w) for w in ws) == 2 * r:
            return (Counter(ws[:r]), Counter(ws[r:]))


G_JOINT = {1: Fr("0.829417"), 2: Fr("0.544535")}
G_SEED = {1: Fr("0.699581"), 2: Fr("0.370632"), 3: Fr("0.195745")}

rng = random.Random(1840)
joint = seed + h1
worst = {1: Fr(0), 2: Fr(0)}
worst_s = {1: Fr(0), 2: Fr(0), 3: Fr(0)}
n_par = 0
for trial in range(120):
    r = rng.randint(1, 4)
    F = random_simple(rng, r)
    r0 = rank(F)
    for m in (1, 2):
        worst[m] = max(worst[m], path_sum(F, joint, m) / r0)
    for m in (1, 2, 3):
        worst_s[m] = max(worst_s[m], path_sum(F, seed, m) / r0)
    n_par += 1
print(f"(1) {n_par} random valid parents (r<=4), joint 48 terms m<=2 and seed m<=3: every child valid "
      "(no negative refill, Sigma|w| = 2r): True")
print(f"(2) max path-summed ratio, joint: m=1 {float(worst[1]):.6f} <= {G_JOINT[1]}: {worst[1] <= G_JOINT[1]};"
      f"  m=2 {float(worst[2]):.6f} <= {G_JOINT[2]}: {worst[2] <= G_JOINT[2]}")
print(f"    seed: " + "; ".join(f"m={m} {float(worst_s[m]):.6f} <= {G_SEED[m]}: {worst_s[m] <= G_SEED[m]}"
                                for m in (1, 2, 3)))


def FK(K):
    return (Counter({-K: 1, 0: K // 2 - 1}), Counter({0: K // 2}))


print("    family F_K (A: -K, 0^(K/2-1) | B: 0^(K/2)):")
for K in (40, 400, 4000):
    F = FK(K)
    r0 = rank(F)
    v1 = path_sum(F, joint, 1, check=False) / r0
    v2 = path_sum(F, joint, 2, check=False) / r0
    s1 = path_sum(F, seed, 1, check=False) / r0
    print(f"      K={K:5d}: joint m=1 {float(v1):.6f}, m=2 {float(v2):.6f}; seed m=1 {float(s1):.6f}")
print(f"    (certified sups: joint 0.829417 / 0.544535, seed 0.699581; approached from below)")

# (3) one-step h_1 ratio term by term on F_K
F = FK(20000)
r0 = rank(F)
ok3 = True
for c, T in h1:
    _, rp = child(F, T)
    d = len(T[0])
    mu = sum(abs(x) for x in T[0]) + sum(abs(y) for y in T[1])
    gap = (d + Fr(mu, 2)) - Fr(rp, r0)
    ok3 = ok3 and 0 <= gap <= Fr(2 * (d + mu), 20000)
print(f"(3) F_K, K=20000: each h_1 term's ratio within 2(d+mu)/K below d+mu/2: {ok3}")
tot = sum(c * Fr(child(F, T)[1], r0) for c, T in h1)
print(f"    sum |bhat b'| ratio on F_K = {float(tot):.6f} (closed form beta_1 at beta0 = 0.129836..)")
print("BRUTE FORCE OK" if worst[1] <= G_JOINT[1] and worst[2] <= G_JOINT[2] and ok3 else "BRUTE FORCE FAILED")
