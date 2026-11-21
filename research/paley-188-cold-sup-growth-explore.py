#!/usr/bin/env python3
"""Round 188 cold call `cold-prime-compact-sup-growth`: exact consistency checks and FLOATING orientation.

Label (c) unless stated.  Nothing here is used as a certificate; the certified numbers are in
research/paley-188-cold-sup-growth-certify.py.

Part 1 (exact integers/Fractions; a check of a reduction, not of a rate):
  The per-fibre Round 80 / Round 182 rule for one factor J^e (e odd, any size): fibre A shifts by -e,
  fibre B by +e; generic rank r' = (1/2) sum |w'|; transport keeps negative weights in their fibre,
  moves positive weights to the other fibre, drops shifted zeros and fills each fibre with zeros up to r'.
  Claim checked: summed over the two children e = +m, -m, the pooled |w|-histogram of the children is
  P_m(histogram of the parent), where P_m sends a slot of size a >= 1 to sizes |a-m| (dropped if 0) and a+m,
  a zero slot to two slots of size m, and then adds sum_{b>=1}(b-1) n'_b zeros.  The fibre labels drop out.
  We also record how often a per-fibre fill would be negative (hypothesis (b4) of Round 182).
Part 2 (floating): Fourier coefficients beta_m of Phi_a'(sqrt8 cos theta) by the trapezoid rule, the
  Perron root of the truncated histogram operator sum_m (|beta_m|/2) P_m (dimension-price rate), the same
  with signed coefficients (value at a point where every leaf character equals its dimension), and the
  seed-linear and m = 1 variants.  Also the normalized Perron eigenvector (slot-size law of the leaves).
Replay: .venv/bin/python -B research/paley-188-cold-sup-growth-explore.py   (about 4 s)
"""
import math
import random
from collections import Counter
from fractions import Fraction

import numpy as np

A, B = 0, 1


def child(fibres, e):
    """fibres = (Counter A, Counter B) of slot values (zeros included). Returns child fibres and the fills."""
    shifted = []
    for fb, cnt in enumerate(fibres):
        for v, c in cnt.items():
            w = v - e if fb == A else v + e
            shifted.append((fb, w, c))
    r2 = sum(abs(w) * c for fb, w, c in shifted)
    assert r2 % 2 == 0
    r1 = r2 // 2
    out = (Counter(), Counter())
    for fb, w, c in shifted:
        if w < 0:
            out[fb][w] += c
        elif w > 0:
            out[1 - fb][w] += c
    fills = []
    for fb in (A, B):
        nz = sum(out[fb].values())
        fills.append(r1 - nz)
        if r1 - nz > 0:
            out[fb][0] += r1 - nz
    return out, fills, r1


def hist(fibres):
    h = Counter()
    for cnt in fibres:
        for v, c in cnt.items():
            h[abs(v)] += c
    return h


def P_m(h, m):
    out = Counter()
    for a, c in h.items():
        if a == 0:
            out[m] += 2 * c
        else:
            if a != m:
                out[abs(a - m)] += c
            out[a + m] += c
    z = sum((b - 1) * c for b, c in out.items() if b >= 1)
    out = Counter({b: c for b, c in out.items() if b != 0})
    if z:
        out[0] += z
    return out


def random_simple(rng, r):
    """random valid simple: two fibres of r slots, sum |w| = 2r, nonzero count per fibre <= r."""
    while True:
        tot = 2 * r
        vals = []
        while tot > 0:
            v = rng.randint(1, min(tot, 6))
            vals.append(v)
            tot -= v
        fib = [Counter(), Counter()]
        ok = True
        for v in vals:
            fb = rng.randint(0, 1)
            fib[fb][v * rng.choice((-1, 1))] += 1
        for fb in (A, B):
            nz = sum(fib[fb].values())
            if nz > r:
                ok = False
            elif nz < r:
                fib[fb][0] += r - nz
        if ok:
            return tuple(fib)


print('== Part 1: exact check of the fibre-free histogram reduction (one step, both signs) ==')
rng = random.Random(188)
neg_fill = 0
tests = 0
for trial in range(4000):
    r = rng.randint(2, 14)
    M = random_simple(rng, r)
    h = hist(M)
    assert sum(h.values()) == 2 * r and sum(a * c for a, c in h.items()) == 2 * r
    for m in (1, 3, 5, 7):
        tot = Counter()
        for e in (m, -m):
            ch, fills, r1 = child(M, e)
            tests += 1
            if min(fills) < 0:
                neg_fill += 1
                # complete the child formally (negative zero count) for the linear identity
                for fb in (A, B):
                    if fills[fb] < 0:
                        ch[fb][0] += fills[fb]
            tot += Counter({k: v for k, v in hist(ch).items()})
            # hist() above drops nonpositive counts in Counter addition; redo exactly:
        tot = Counter()
        for e in (m, -m):
            ch, fills, r1 = child(M, e)
            hh = hist(ch)
            for fb in (A, B):
                if fills[fb] < 0:
                    hh[0] = hh.get(0, 0) + fills[fb]
            for k, v in hh.items():
                tot[k] = tot.get(k, 0) + v
        ref = P_m(h, m)
        keys = set(tot) | set(ref)
        assert all(tot.get(k, 0) == ref.get(k, 0) for k in keys), (M, m, tot, ref)
print(f'  {tests} children of 4000 random valid simples (m = 1, 3, 5, 7, both signs): histogram identity holds exactly')
print(f'  children with a negative per-fibre fill (rule (b4) would fail on them): {neg_fill} of {tests}')

# fills along actual trees from the transported square K(J^2): A = {-2, 2}, B = {0, 0}
root = (Counter({-2: 1, 2: 1}), Counter({0: 2}))
layer = [root]
bad = 0
seen = 0
for depth in range(1, 8):
    nxt = []
    for M in layer:
        for e in (1, -1, 3, -3):
            ch, fills, r1 = child(M, e)
            seen += 1
            if min(fills) < 0:
                bad += 1
            if depth < 7 and abs(e) == 1 or depth < 4:
                nxt.append(ch)
    layer = nxt
print(f'  tree from K(J^2) (all +-1 paths to depth 7, +-3 to depth 3): {seen} children, negative fills: {bad}')

# exhaustive (exact): per-fibre fills are nonnegative for every formal configuration with r <= 5, slot
# values in [-2r, 2r], and every shift e in {+-1, +-3, +-5} (Lemma F of the report proves it for all r, e).
from itertools import combinations_with_replacement as cwr
cases = negs = 0
for r in range(1, 6):
    fibs = list(cwr(range(-2 * r, 2 * r + 1), r))
    for FA in fibs:
        sa = sum(abs(v) for v in FA)
        if sa > 2 * r:
            continue
        for FB in fibs:
            if sa + sum(abs(v) for v in FB) != 2 * r:
                continue
            for e in (1, -1, 3, -3, 5, -5):
                ch, fills, r1 = child((Counter(FA), Counter(FB)), e)
                cases += 1
                negs += min(fills) < 0
print(f'  exhaustive r <= 5, |e| <= 5: {cases} children, negative per-fibre fills: {negs}')

# cross-check against Round 182's independent fibre-resolved computation (exact):
# G_up(m) = sup over atoms (one slot of size b plus b-1 zeros) of mass(P_1^m atom)/mass(atom), incl. b -> infinity
r182 = [4, 12, 36, 104, 300, 856, 2440, 6928]
mine = []
for m in range(1, 9):
    V = m + 8
    vals = {}
    for b in range(1, V + 1):
        h = Counter({b: 1})
        if b > 1:
            h[0] = b - 1
        for _ in range(m):
            h = P_m(h, 1)
        vals[b] = sum(k * c for k, c in h.items())
    mine.append(max(max(Fraction(vals[b], b) for b in vals), Fraction(vals[V] - vals[V - 1])))
print('  Round 182 G_up(m), m = 1..8, recomputed from the histogram operator:', [int(g) for g in mine],
      '(matches Round 182:', mine == r182, ')')

# (exact) how far can the weight-list Goursat test of Rounds 55-68 separate the leaves?  Leaves of the
# J^{+-1} tree from K(J^2), grouped by their two-fibre weight data modulo a uniform shift (rank-one twist)
# and negation (duality).  A class of size > 2 cannot be separated by weight lists alone.
def canon(fibres):
    best = None
    for sg in (1, -1):
        g = [sorted((sg * v, c) for v, c in cnt.items() if c) for cnt in fibres]
        mn = min(v for fib in g for v, c in fib)
        g = tuple(tuple((v - mn, c) for v, c in fib) for fib in g)
        best = g if best is None or g < best else best
    return best


layer = [(Counter({-2: 1, 2: 1}), Counter({0: 2}))]
for depth in range(1, 13):
    layer = [child(M, e)[0] for M in layer for e in (1, -1)]
    if depth in (4, 8, 9, 10, 12):
        cl = Counter(canon(M) for M in layer)
        print(f'  depth {depth}: {len(layer)} leaves, {len(cl)} weight-data classes (mod shift, negation), largest class {max(cl.values())}')

print('\n== Part 2 (floating, orientation only) ==')
a = 2031 / 128
th = np.linspace(0, np.pi, 400001)
f = math.sqrt(8) * np.cos(th) / np.sqrt(4 * a + 8 * np.cos(th) ** 2)
beta = {m: 2 / np.pi * np.trapezoid(f * np.cos(m * th), th) for m in range(1, 26, 2)}
for m in range(1, 16, 2):
    print(f'  beta_{m:<2d} = {beta[m]: .12e}')
lS = math.sqrt(1 - math.sqrt(4 * a / (4 * a + 8)))
print(f'  l_S = {lS:.10f}; sqrt(sum beta_m^2 / 2) = {math.sqrt(sum(b * b for b in beta.values()) / 2):.10f}')


def build(Bmax, w):
    P = np.zeros((Bmax, Bmax))
    for m, wm in w.items():
        for a_ in range(Bmax):
            outs = [m, m] if a_ == 0 else ([abs(a_ - m)] if a_ != m else []) + [a_ + m]
            for o in outs:
                if o < Bmax:
                    P[o, a_] += wm
                    P[0, a_] += wm * (o - 1)
    return P


lin = math.sqrt(2 / a) / 2
for name, w in (('seed-linear only (Round 182: J^{+-1} with s/(4 sqrt a))', {1: lin}),
                ('exact J^{+-1} term only', {1: abs(beta[1]) / 2}),
                ('full Phi_a\'(S), |beta_m|/2 (dimension price)', {m: abs(b) / 2 for m, b in beta.items()}),
                ('full Phi_a\'(S), signed beta_m/2 (all leaves at +dimension)', {m: b / 2 for m, b in beta.items()})):
    for Bmax in (300, 1200):
        P = build(Bmax, w)
        ev, V = np.linalg.eig(P)
        i = int(np.argmax(ev.real))
        lam = ev[i].real
        print(f'  {name}; B = {Bmax}: rate = {lam:.10f}, rate/l_S = {lam / lS:.6f}')
    v = np.abs(V[:, i].real)
    v = v / v.sum()
    if 'dimension price' in name:
        print('    Perron slot-size law n_0..n_8 (fractions of slots):', ' '.join(f'{x:.4f}' for x in v[:9]))
        print(f'    mean slot size = {sum(k * v[k] for k in range(len(v))):.6f} (valid simples: exactly 1)')
print('  thresholds: 1/q_rho * l_S = 1.94363 * l_S =', f'{1 / 0.5145 * lS:.5f};',
      ' angular 2.1610 * l_S =', f'{2.1610 * lS:.5f}')

# growth from concrete roots: mass of P^k hist(root), floating
P = build(1200, {m: abs(b) / 2 for m, b in beta.items()})
for name, h in (('K(J^2), r = 2', {2: 2, 0: 2}), ('all slots |w| = 1, r = 6', {1: 12}),
                ('{0, 6}-type, r = 6', {6: 2, 0: 10})):
    x = np.zeros(1200)
    for k_, c in h.items():
        x[k_] = c
    masses = []
    for k in range(0, 61):
        masses.append((np.arange(1200) * x).sum() / 2)
        x = P @ x
    rates = [masses[k + 1] / masses[k] for k in (0, 1, 2, 5, 10, 20, 40, 59)]
    print(f'  A(L_S^k chi_M) step ratios, root {name}: ' + ' '.join(f'{q:.5f}' for q in rates))

# complex corners of Q (floating): coefficients of Phi_t'(sqrt8 cos th) at t = a + 2^-17 (+-1 +- i)
for cr in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
    t = a + 2 ** -17 * complex(*cr)
    fc = math.sqrt(8) * np.cos(th) / np.sqrt(4 * t + 8 * np.cos(th) ** 2 + 0j)
    bc = {m: 2 / np.pi * np.trapezoid(fc * np.cos(m * th), th) for m in range(1, 26, 2)}
    P = build(600, {m: abs(b) / 2 for m, b in bc.items()})
    lam = max(np.linalg.eigvals(P).real)
    l2 = math.sqrt(sum(abs(b) ** 2 for b in bc.values()) / 2)
    print(f'  corner t = a + 2^-17 ({cr[0]:+d}{cr[1]:+d}i): |beta|-rate = {lam:.9f}, sqrt(sum|beta|^2/2) = {l2:.9f},'
          f' ratio = {lam / l2:.6f}')
