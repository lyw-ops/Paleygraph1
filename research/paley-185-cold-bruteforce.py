#!/usr/bin/env python3
"""Round 185 cold call: independent brute-force cross-check (does NOT import the other 185 scripts'
model layer for the weights; it only reads the object lists of the leaves script to compare).

  * objects as explicit sorted slot lists (one entry per slot), own line/shift/tensor/transport;
  * Fourier coefficients by FFT of the functions at t = a, s^2 = 8 (double precision);
  * checks: linear paths to depth 4 have pairwise distinct weight data and agree with the
    leaves script; the four depth-5 equal-weight pairs and their separation by pre-transport data;
    unsigned prices per depth and the nonlinear depth-2/3 prices (floating, compared with the
    certified balls of the leaves script).
Replay:  .venv/bin/python -B research/paley-185-cold-bruteforce.py
"""
import contextlib
import io
import itertools
import os
import runpy

import numpy as np

_here = os.path.dirname(os.path.abspath(__file__))


def line(k):
    return ([-k], [k])


def shift(O, k):
    return ([w - k for w in O[0]], [w + k for w in O[1]])


def tensor(O1, O2):
    return (sorted(a + b for a in O1[0] for b in O2[0]), sorted(a + b for a in O1[1] for b in O2[1]))


def transport(O):
    r2 = sum(abs(w) for w in O[0]) + sum(abs(w) for w in O[1])
    r = r2 // 2
    A = [w for w in O[0] if w < 0] + [w for w in O[1] if w > 0]
    B = [w for w in O[1] if w < 0] + [w for w in O[0] if w > 0]
    assert len(A) <= r and len(B) <= r
    return (sorted(A + [0] * (r - len(A))), sorted(B + [0] * (r - len(B))))


def key(O):
    return (tuple(sorted(O[0])), tuple(sorted(O[1])))


# Fourier coefficients by FFT at t = a = 2031/128, s^2 = 8
a = 2031 / 128
s = np.sqrt(8.0)
beta = 8 / (4 * a)
N = 1 << 14
th = 2 * np.pi * np.arange(N) / N


def four(vals, k):
    return float(np.real(np.fft.fft(vals)[k % N] / N))


c2 = np.cos(th) ** 2
F_half = (1 + beta * c2) ** 0.5
F_m32 = (1 + beta * c2) ** -1.5
G_m12 = np.cos(th) * (1 + beta * c2) ** -0.5
G_m52 = np.cos(th) * (1 + beta * c2) ** -2.5
bp = {k: four(F_half, k) for k in (2, -2, 4, -4, 6, -6)}
bh = {k: four(F_m32, k) for k in range(-6, 7, 2)}
gh = {k: four(G_m12, k) for k in (1, -1, 3, -3, 5, -5)}
ee = {k: four(G_m52, k) for k in (1, -1, 3, -3, 5, -5)}
TS = 2 * np.sqrt(a)
VAR = s / TS
ROOTS = (2, -2, 4, -4, 6, -6)
SEED = (1, -1, 3, -3, 5, -5)

# linear chain
obj = {(k,): transport(line(k)) for k in ROOTS}
pre = {(k,): line(k) for k in ROOTS}
coef = {(k,): TS * bp[k] for k in ROOTS}
front = list(obj)
for j in range(1, 6):
    new = []
    for p in front:
        for k in SEED:
            q = p + (k,)
            pre[q] = shift(obj[p], k)
            obj[q] = transport(pre[q])
            coef[q] = coef[p] * VAR * gh[k]
            new.append(q)
    front = new
paths4 = [p for p in obj if len(p) <= 5]
keys4 = [key(obj[p]) for p in paths4]
print(f"(1) linear paths to depth 4: {len(paths4)}; distinct weight data: {len(set(keys4))}  "
      f"(all distinct: {len(set(keys4)) == len(paths4)})")
paths5 = list(obj)
from collections import defaultdict
g5 = defaultdict(list)
for p in paths5:
    g5[key(obj[p])].append(p)
eq5 = [v for v in g5.values() if len(v) > 1]
print(f"    to depth 5: {len(paths5)} paths, {len(g5)} distinct weight data, equal-weight groups: {len(eq5)}")
for v in eq5:
    p, q = v
    print(f"      {p} vs {q}: pre-transport data equal? {key(pre[p]) == key(pre[q])}; "
          f"dims of pre {len(pre[p][0])}, {len(pre[q][0])}; coefficient signs {np.sign(coef[p]):+.0f}, {np.sign(coef[q]):+.0f}")
mono = all(len(obj[p][0]) >= len(obj[p[:-1]][0]) + 1 for p in paths5 if len(p) > 1)
print(f"    dimension strictly increases along every linear path (depth <= 5): {mono}")

# comparison with the leaves script
os.environ["P185_DEPTH"] = "5"
with contextlib.redirect_stdout(io.StringIO()):
    L = runpy.run_path(os.path.join(_here, "paley-185-cold-picard-leaves.py"))


def expand(Wt):
    return (tuple(sorted(w for w, c in Wt[0] for _ in range(c))), tuple(sorted(w for w, c in Wt[1] for _ in range(c))))


agree = all(expand(L["W"][p]) == key(obj[p]) for p in paths5)
print(f"(2) weight data agree with the leaves script for all {len(paths5)} paths: {agree}")
for j in range(6):
    ps = [p for p in paths5 if len(p) == j + 1]
    fl = sum(abs(coef[p]) * len(obj[p][0]) for p in ps)
    ball = sum(float(L["COEF"][p].real.mid()) * 0 + abs(float(L["COEF"][p].real.mid())) * len(obj[p][0]) for p in ps)
    print(f"    [float] depth {j}: unsigned price (FFT coefficients, t=a, s^2=8) {fl:.6f}; ball midpoints {ball:.6f}")

# nonlinear depth 2 and 3 (independent construction)
tot = defaultdict(float)
seen = {}
for i in range(-6, 7, 2):
    for k, l in itertools.product(ROOTS, ROOTS):
        O = transport(shift(tensor(obj[(k,)], obj[(l,)]), i))
        c = 0.5 / TS * bh[i] * coef[(k,)] * coef[(l,)]
        kk = ("Q", i, tuple(sorted((k, l))))
        seen[kk] = seen.get(kk, 0.0) + c
        seen[kk + ("dim",)] = len(O[0])
Qp = sum(abs(v) * seen[k + ("dim",)] for k, v in seen.items() if len(k) == 3)
tot["Q_1"] = Qp
LQ = 0.0
for k, v in list(seen.items()):
    if len(k) != 3:
        continue
    _, i, (k1, l1) = k
    O = transport(shift(tensor(obj[(k1,)], obj[(l1,)]), i))
    for c in SEED:
        LQ += abs(v * VAR * gh[c]) * len(transport(shift(O, c))[0])
tot["L_S Q_1"] = LQ
X = 0.0
for i in range(-6, 7, 2):
    for k in ROOTS:
        for l in ROOTS:
            for c in SEED:
                O = transport(shift(tensor(obj[(k,)], obj[(l, c)]), i))
                X += abs(1 / TS * bh[i] * coef[(k,)] * coef[(l, c)]) * len(O[0])
tot["X_1"] = X
C = 0.0
cub = {}
for c in SEED:
    for ks in itertools.product(ROOTS, repeat=3):
        kk = (c, tuple(sorted(ks)))
        v = (1 / 6) * (-3 * s / TS ** 3) * ee[c] * coef[(ks[0],)] * coef[(ks[1],)] * coef[(ks[2],)]
        cub[kk] = cub.get(kk, 0.0) + v
for (c, ks), v in cub.items():
    O = transport(shift(tensor(tensor(obj[(ks[0],)], obj[(ks[1],)]), obj[(ks[2],)]), c))
    C += abs(v) * len(O[0])
tot["C_1"] = C
print("(3) [float] nonlinear unsigned prices (independent): " +
      ", ".join(f"{k} {v:.6f}" for k, v in tot.items()) + f"; certified balls (leaves script): " +
      ", ".join(f"{k} <= {v:.6f}" for k, v in L["SUMMARY"]["NLP"].items()))
print("BRUTE FORCE DONE")
