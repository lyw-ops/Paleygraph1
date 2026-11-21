#!/usr/bin/env python3
"""Round 192, call ordinary-nc-vertex-tightness: search for sharp-spectrum sets.

EVIDENCE ONLY (field-free; no Paley input).  Tests the statement (SS) of the
report, section 3: a set S in Z/N whose normalised spectrum
g_S(xi) = |sum_{s in S} e(s xi/N)|^2/|S|^2 carries (1-o(1)) of its nonzero
mass sum_{xi != 0} g_S at levels >= a should be close to a bounded signed
combination of cosets, so its mass should sit on boundedly many subgroups of
the dual of order ~ N/|S|.

Objective (low-mass fraction):  L_a(S) = sum_{xi != 0, g_S < a} g_S / sum_{xi != 0} g_S.
Scale as in the near-critical support: |S| = round(sqrt(N/2)) (n/|S| = sqrt(2n) = sqrt p).

Part E  exhaustive minimum of L_a over all S with |S| = m in Z/N, N prime
        (affine normalisation: 0, 1 in S, valid since x -> cx + t preserves L_a),
        and composite controls with a subgroup of order m.
Part S  simulated annealing at larger N (prime N: no subgroups at all;
        composite N with a subgroup of order ~ m as a control), several seeds:
        random, interval, half of an interval, rank-2 Bohr set.
        Also reports, for the best set, the largest share of nonzero mass on
        one subgroup of the dual of order in [N/(4m), 4N/m] (zero for prime N).

Run:
  .venv/bin/python -B research/paley-192-vertex-sharp-search.py E
  .venv/bin/python -B research/paley-192-vertex-sharp-search.py S 20000      # steps per run
"""
import sys
from itertools import combinations
from math import sqrt

import numpy as np

A_LEVELS = (0.2, 0.1, 0.05)


def spectrum(ind):
    F = np.fft.fft(ind)
    m = ind.sum()
    return (F.real ** 2 + F.imag ** 2) / (m * m)


def low_frac(g, a):
    h = g[1:]
    return h[h < a].sum() / h.sum()


def subgroup_share(g, N, m):
    """Largest share of sum_{xi != 0} g on (H^perp minus 0) over subgroups H^perp of
    Z/N of order N/h in [N/(4m), 4N/m]; H^perp = multiples of h."""
    best = 0.0
    tot = g[1:].sum()
    for h in range(2, N):
        if N % h:
            continue
        order = N // h
        if not (N / (4 * m) <= order <= 4 * N / m):
            continue
        best = max(best, g[h::h].sum() / tot)
    return best


# ----------------------------------------------------------------- Part E
def exhaustive(N, m, levels=A_LEVELS, batch=200000):
    rest = np.arange(2, N)
    best = {a: (2.0, None) for a in levels}
    combos = combinations(rest, m - 2)
    while True:
        chunk = []
        for _ in range(batch):
            try:
                chunk.append(next(combos))
            except StopIteration:
                break
        if not chunk:
            break
        arr = np.array(chunk, dtype=np.int64).reshape(len(chunk), m - 2)
        ind = np.zeros((len(chunk), N))
        ind[:, 0] = 1
        ind[:, 1] = 1
        rows = np.arange(len(chunk))[:, None]
        ind[rows, arr] = 1
        F = np.fft.fft(ind, axis=1)
        g = (F.real ** 2 + F.imag ** 2)[:, 1:] / (m * m)
        tot = g.sum(axis=1)
        for a in levels:
            lf = np.where(g < a, g, 0).sum(axis=1) / tot
            i = int(np.argmin(lf))
            if lf[i] < best[a][0]:
                best[a] = (float(lf[i]), (0, 1) + tuple(int(x) for x in arr[i]))
        if len(chunk) < batch:
            break
    return best


def part_e():
    print("PART E: exhaustive minimum of L_a over |S| = m (prime N: affine-normalised 0,1 in S)")
    for N, m in ((31, 4), (41, 5), (53, 5), (61, 6), (73, 6), (83, 6)):
        best = exhaustive(N, m)
        print(f"  N={N:3d} (prime) m={m}: " + "  ".join(
            f"min L_{a}={best[a][0]:.4f} at S={best[a][1]}" for a in A_LEVELS))
    # composite controls: N = m * k with a subgroup of order m (S = subgroup gives L = 0)
    for N, m in ((32, 4), (50, 5), (60, 6)):
        ind = np.zeros(N)
        ind[:: N // m] = 1
        g = spectrum(ind)
        print(f"  control N={N} (subgroup of order {m}): L_a = "
              + ", ".join(f"{low_frac(g, a):.4f}" for a in A_LEVELS))


# ----------------------------------------------------------------- Part S
def seeds(N, m, rng):
    out = {}
    out["random"] = rng.choice(N, size=m, replace=False)
    out["interval"] = np.arange(m)
    out["half-interval"] = rng.choice(2 * m, size=m, replace=False)
    # rank-2 Bohr set {x : ||x a/N|| < d1, ||x b/N|| < d2}, trimmed/padded to m points
    a, b = int(rng.integers(1, N)), int(rng.integers(1, N))
    x = np.arange(N)
    ta = np.abs(((x * a) % N) / N - np.round(((x * a) % N) / N))
    tb = np.abs(((x * b) % N) / N - np.round(((x * b) % N) / N))
    score = np.maximum(ta, tb)
    out["bohr2"] = np.argsort(score)[:m]
    return out


def anneal(N, m, start, a, steps, rng, T0=0.05, T1=1e-4):
    ind = np.zeros(N)
    ind[start] = 1
    cur = low_frac(spectrum(ind), a)
    best, best_ind = cur, ind.copy()
    for t in range(steps):
        T = T0 * (T1 / T0) ** (t / max(1, steps - 1))
        inS = np.flatnonzero(ind)
        u = int(inS[rng.integers(len(inS))])
        if rng.random() < 0.5:      # local move: shift one element by a small step
            v = (u + int(rng.choice([-3, -2, -1, 1, 2, 3]))) % N
        else:                        # global move: to a uniformly random site
            v = int(rng.integers(N))
        if ind[v] == 1:
            continue
        ind[u], ind[v] = 0, 1
        new = low_frac(spectrum(ind), a)
        if new <= cur or rng.random() < np.exp((cur - new) / T):
            cur = new
            if cur < best:
                best, best_ind = cur, ind.copy()
        else:
            ind[u], ind[v] = 1, 0
    return best, best_ind


def part_s(steps):
    print(f"PART S: simulated annealing of L_a, {steps} steps per run (best of each seed)")
    cases = [(2003, "prime"), (5003, "prime"), (10007, "prime"), (20011, "prime"),
             (2048, "2^11 (subgroups of every power-of-2 order)"), (5000, "composite, subgroup of order 50"),
             (10082, "2*71^2, subgroup of order 71")]
    for N, label in cases:
        m = int(round(sqrt(N / 2)))
        rng = np.random.default_rng(N)
        for a in (0.1,):
            res = []
            for name, st in seeds(N, m, rng).items():
                ind0 = np.zeros(N)
                ind0[st] = 1
                l0 = low_frac(spectrum(ind0), a)
                b, bi = anneal(N, m, st, a, steps, rng)
                g = spectrum(bi)
                res.append((name, l0, b, subgroup_share(g, N, m),
                            float(((g ** 2).sum()) / g.sum())))
            print(f"  N={N} ({label}), m={m}, a={a}:")
            for name, l0, b, share, e in res:
                print(f"     seed {name:13s} start L={l0:.4f} -> best L={b:.4f}; "
                      f"max subgroup share={share:.4f}; sum g^2/sum g={e:.4f}")
        # control value: exact subgroup when it exists
        for h in range(m - 3, m + 4):
            if h > 1 and N % h == 0:
                ind = np.zeros(N)
                ind[:: N // h] = 1
                g = spectrum(ind)
                print(f"     control: subgroup of order {h}: L_0.1 = {low_frac(g, 0.1):.4f}")
                break


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "E"
    if mode == "E":
        part_e()
    elif mode == "S":
        part_s(int(sys.argv[2]) if len(sys.argv) > 2 else 20000)
