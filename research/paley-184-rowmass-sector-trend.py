#!/usr/bin/env python3
r"""Round 184, call ordinary-prime-near-critical-slope-row-mass: sector trend.

Floating evidence only. At a fixed prime p, anneal a flat law (nu uniform on
S, |S| = round(m_0), 0 not in S) towards sector concentration, i.e. maximize
Phi(S) = rho * sum_{i,j in S} k(i-j) (see paley-184-rowmass-models.py). Along the
path, record snapshots and measure the slope-row quantities. The question is
whether X, max W and sup C move off their floors as the model approaches the
near-critical branch (s = rho sum g chi(1-x)/sqrt p -> 1). Floors:
    X >= M_1^2/(n-1),  max_xi W_xi >= M_1^2/(p-1),  sup_{lambda != 1} C >= (M_1^2 - X)/(p-2).

Usage: .venv/bin/python -B research/paley-184-rowmass-sector-trend.py P [steps] [seed]
"""
import importlib.util
import os
import sys
import numpy as np

_here = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("rm", os.path.join(_here, "paley-184-rowmass-models.py"))
rm = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rm)


def floors(env, S, rho):
    r = rm.measure(env, S, rho)
    return r


def anneal(env, rho, steps, seed):
    k, n, p = env['k'], env['n'], env['p']
    m = int(round(n / np.sqrt(p)))
    rng = np.random.default_rng(seed)
    rk = rho * k
    S = list(rng.choice(np.arange(1, n), m, replace=False))
    inS = np.zeros(n, dtype=bool)
    inS[S] = True
    score = np.zeros(n)
    for s in S:
        score += np.roll(rk, s)
    val = float(sum(score[s] for s in S))
    snaps = []
    targets = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    ti = 0
    T0 = 2.0
    best = (val, np.nonzero(inS)[0].copy())
    for it in range(steps):
        T = T0 * (1 - it / steps) + 1e-3
        Sarr = np.nonzero(inS)[0]
        y = int(Sarr[rng.integers(0, m)])
        # propose x among good outsiders (biased) or random
        if rng.random() < 0.7:
            cand = np.where(inS, -np.inf, score)
            cand[0] = -np.inf
            top = np.argpartition(-cand, 32)[:32]
            x = int(top[rng.integers(0, 32)])
        else:
            x = int(rng.integers(1, n))
            if inS[x]:
                continue
        gain = 2 * (score[x] - rk[(x - y) % n]) - 2 * score[y] + 2 * rk[0]
        if gain >= 0 or rng.random() < np.exp(gain / T):
            inS[y] = False
            score -= np.roll(rk, y)
            inS[x] = True
            score += np.roll(rk, x)
            val += gain
            if val > best[0]:
                best = (val, np.nonzero(inS)[0].copy())
            # sector tightness s = (sqrt p / m^2) * Phi / sqrt p = Phi / m^2
            s_now = val / m ** 2
            while ti < len(targets) and s_now >= targets[ti]:
                snaps.append((targets[ti], np.nonzero(inS)[0].copy()))
                ti += 1
    snaps.append(('best', best[1]))
    return snaps


def main():
    p = int(sys.argv[1]) if len(sys.argv) > 1 else 4001
    steps = int(sys.argv[2]) if len(sys.argv) > 2 else 200000
    seed = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    env = rm.setup(p)
    print(f"p={p}, m={int(round(env['n']/np.sqrt(p)))}, steps={steps}, seed={seed}; floating evidence only")
    print(f"{'rho':>3} {'snap':>5} {'s':>6} {'G_-r':>6} {'E(S)/S3':>7} {'Gam2/rp':>7} {'X/p':>6} "
          f"{'X/floor':>7} {'maxW/flW':>8} {'supC/flC':>8} {'maxc':>6}")
    for rho in (1, -1):
        for tag, S in anneal(env, rho, steps, seed):
            r = rm.measure(env, S, rho)
            # floors from M_1: recompute via X/floor ratio: floor_X = M1^2/(n-1)
            n = env['n']
            M1sq = r['Xp'] * p / r['floor'] * (n - 1)
            flW = M1sq / (p - 1)
            flC = (M1sq - r['Xp'] * p) / (p - 2)
            print(f"{rho:3d} {str(tag):>5} {r['s']:6.3f} {r['Gm']:6.1f} {r['ES']:7.4f} {r['Gam2']:7.4f} "
                  f"{r['Xp']:6.3f} {r['floor']:7.3f} {r['Wp'] * p / flW:8.3f} {r['Cp'] * p / flC:8.3f} {r['maxc']:6.2f}")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
