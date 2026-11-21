#!/usr/bin/env python3
"""Round 185 cold call: FLOATING evidence for the nonlinear tail at depth 5 (label (c)).

Weight data are exact integers; coefficients are the midpoints of the certified balls, converted to
double precision, so every printed price here is a [float] diagnostic, not a bound.
Depth-5 nonlinear pieces of h (depth = number of transports - 1):
  (a) L_S N^(4)                                (N^(d) = nonlinear part of h^(d))
  (b) K(Phi'' h^(0) h^(3)),  h^(3) = L_S^3 h_1 + N^(3)
  (c) K(Phi'' h^(1) h^(2)),  h^(2) = L_S^2 h_1 + Q_1
  (d) (1/2) K(Phi''' h_0^2 h^(2)) + (1/2) K(Phi''' h_0 (h^(1))^2)
  (e) (1/6) K(Phi'''' h_0^3 h^(1))
  (f) (1/120) K(Phi^(5) h_0^5): bounded by the Prop. A dimension bound (it is below 1e-6).
For each object: unsigned price |c| dim, and whether its pre-transport weight data contain the
pre-transport data of a linear simple of depth 1..3 (or a root) of opposite sign.
Replay:  .venv/bin/python -B research/paley-185-cold-depth5-evidence.py      (a few minutes)
"""
import contextlib
import io
import itertools
import os
import runpy
import time
from collections import Counter, defaultdict

import numpy as np

T0 = time.time()
_here = os.path.dirname(os.path.abspath(__file__))
with contextlib.redirect_stdout(io.StringIO()):
    T = runpy.run_path(os.path.join(_here, "paley-185-cold-tails.py"))
M = T["M"]
LIN, W, PRE, COEF, NL, N4 = T["LIN"], T["W"], T["PRE"], T["COEF"], T["NL"], T["N4"]
ROOTS, SEED, IH, EC = T["ROOTS"], T["SEED"], T["IH"], T["EC"]
sgn_ref = T["sgn_ref"]
print(f"[setup {time.time() - T0:.1f} s]")


def f(z):
    return float(z.real.mid())


TS = f(T["TS"])
S = f(T["S"])
VAR = f(M.VARPI)
gh = {k: f(M.ghat(k)) for k in SEED}
bh = {i: f(M.bhat(i)) for i in IH}
ec = {c: f(M.ecoef(c)) for c in EC}
fc = {c: f(M.fcoef(c)) for c in IH}
PHI2 = 1 / TS
PHI3 = -3 * S / TS ** 3
PHI4 = 3 / TS ** 3

# factor objects: (W, coef) lists
h0 = [(W[p], f(COEF[p])) for p in LIN if len(p) == 1]
h1 = [(W[p], f(COEF[p])) for p in LIN if len(p) == 2]
h2 = [(W[p], f(COEF[p])) for p in LIN if len(p) == 3] + \
     [(v["W"], f(v["coef"])) for v in NL.values() if v["kind"] == "Q_1"]
h3 = [(W[p], f(COEF[p])) for p in LIN if len(p) == 4] + \
     [(v["W"], f(v["coef"])) for v in NL.values() if v["depth"] == 3]
n4 = [(v["W"], f(v["coef"])) for v in N4.values()]

# S13 + roots, sparse containment structure
S_lin = [p for p in LIN if len(p) <= 4]
lsgn = np.array([1 if f(COEF[p]) > 0 else -1 for p in S_lin])
ldep = np.array([len(p) - 1 for p in S_lin])
cols, cnts, rows = [], [], []
WIDX = {}


def col(fib, w):
    key = (fib, w)
    if key not in WIDX:
        WIDX[key] = len(WIDX)
    return WIDX[key]


for r, p in enumerate(S_lin):
    for fib in (0, 1):
        for w, c in PRE[p][fib]:
            cols.append(col(fib, w))
            cnts.append(c)
            rows.append(r)
cols = np.array(cols)
cnts = np.array(cnts)
rows = np.array(rows)
order = np.argsort(rows, kind="stable")
cols, cnts, rows = cols[order], cnts[order], rows[order]
starts = np.searchsorted(rows, np.arange(len(S_lin)))
NCOL = len(WIDX)

stats = defaultdict(lambda: [0, 0.0, 0.0, 0.0, 0.0])   # n, price, any13, opp13, opp_root


def record(kind, pre, coef):
    """pre: exact pre-transport weight data (tuple form); coef: float"""
    r2 = sum(abs(w) * c for w, c in pre[0]) + sum(abs(w) * c for w, c in pre[1])
    d = r2 // 2
    pr = abs(coef) * d
    st = stats[kind]
    st[0] += 1
    st[1] += pr
    x = np.zeros(NCOL + 1, dtype=np.int64)
    for fib in (0, 1):
        for w, c in pre[fib]:
            k = WIDX.get((fib, w))
            if k is not None:
                x[k] = c
    ok = (x[cols] >= cnts).astype(np.int8)
    hit = np.minimum.reduceat(ok, starts).astype(bool)
    if not hit.any():
        return
    sN = 1 if coef > 0 else -1
    h13 = hit & (ldep >= 1)
    if h13.any():
        st[2] += pr
        if (lsgn[h13] * sN < 0).any():
            st[3] += pr
    h0m = hit & (ldep == 0)
    if h0m.any() and (lsgn[h0m] * sN < 0).any():
        st[4] += pr


# (a) L_S N^(4)
for Wn, c in n4:
    for k in SEED:
        record("(a) L_S N4", M.shift(Wn, k), c * VAR * gh[k])
print(f"[(a) done {time.time() - T0:.0f} s]")
# (b) K(Phi'' h0 h3)
for i in IH:
    for W0, c0 in h0:
        for W3, c3 in h3:
            record("(b) K(Phi'' h0 h3)", M.shift(M.tensor(W0, W3), i), PHI2 * bh[i] * c0 * c3)
print(f"[(b) done {time.time() - T0:.0f} s]")
# (c) K(Phi'' h1 h2)
for i in IH:
    for W1, c1 in h1:
        for W2, c2 in h2:
            record("(c) K(Phi'' h1 h2)", M.shift(M.tensor(W1, W2), i), PHI2 * bh[i] * c1 * c2)
print(f"[(c) done {time.time() - T0:.0f} s]")
# (d) cubic: (1/2) K(Phi''' h0 h0 h2) + (1/2) K(Phi''' h0 h1 h1); merge permutations by keys
acc = {}
for cc in EC:
    for (a_, (Wa, ca)), (b_, (Wb, cb)) in itertools.product(enumerate(h0), repeat=2):
        for n2, (W2, c2) in enumerate(h2):
            key = ("d1", cc, tuple(sorted((a_, b_))), n2)
            v = 0.5 * PHI3 * ec[cc] * ca * cb * c2
            if key in acc:
                acc[key][1] += v
            else:
                acc[key] = [M.shift(M.tensor(M.tensor(Wa, Wb), W2), cc), v]
    for a_, (Wa, ca) in enumerate(h0):
        for (b_, (Wb, cb)), (e_, (We, ce)) in itertools.product(enumerate(h1), repeat=2):
            key = ("d2", cc, a_, tuple(sorted((b_, e_))))
            v = 0.5 * PHI3 * ec[cc] * ca * cb * ce
            if key in acc:
                acc[key][1] += v
            else:
                acc[key] = [M.shift(M.tensor(M.tensor(Wa, Wb), We), cc), v]
for key, (pre, v) in acc.items():
    record("(d) cubic", pre, v)
print(f"[(d) done {time.time() - T0:.0f} s]")
# (e) quartic (1/6) K(Phi'''' h0^3 h1)
acc = {}
for cc in IH:
    for tri in itertools.product(range(len(h0)), repeat=3):
        st_ = tuple(sorted(tri))
        for n1, (W1, c1) in enumerate(h1):
            key = (cc, st_, n1)
            v = PHI4 / 6 * fc[cc] * h0[tri[0]][1] * h0[tri[1]][1] * h0[tri[2]][1] * c1
            if key in acc:
                acc[key][1] += v
            else:
                pre = M.shift(M.tensor(M.tensor(M.tensor(h0[tri[0]][0], h0[tri[1]][0]), h0[tri[2]][0]), W1), cc)
                acc[key] = [pre, v]
for key, (pre, v) in acc.items():
    record("(e) quartic", pre, v)
print(f"[(e) done {time.time() - T0:.0f} s]")
# (f) quintic: Prop. A bound (1/120) |Phi^(5) coef| (5 + |c|) P(h_1)^5 with |Phi^(5)| <= 15 s/(2 sqrt t)^5 * 7
P1 = sum(abs(c) * M.dim(Wx) for Wx, c in h0)
quint = 15 * S / TS ** 5 * 7 * (5 + 10) * P1 ** 5 / 120
print(f"[float] (f) quintic K(Phi^(5) h_1^5)/120: price <= about {quint:.1e} (crude)")

print("\n[float] depth-5 nonlinear pieces: unsigned price; part that could contain a linear depth 1-3 simple; "
      "part with an OPPOSITE-sign possible overlap (depth 1-3 / roots)")
tot = [0.0, 0.0, 0.0, 0.0]
for kind in sorted(stats):
    n, pr, a13, o13, o0 = stats[kind]
    tot = [tot[0] + pr, tot[1] + a13, tot[2] + o13, tot[3] + o0]
    print(f"[float]   {kind:22s}: {n:7d} objects, price {pr:.6f}, could-contain {a13:.6f}, opposite {o13:.6f} / roots {o0:.6f}")
print(f"[float]   total depth 5: price {tot[0]:.6f}, could-contain (depth 1-3) {tot[1]:.6f}, "
      f"opposite-sign {tot[2]:.6f}, opposite-sign roots {tot[3]:.6f}")
print(f"[float] depth 2/3/4/5 nonlinear unsigned: {T['SUM']['NLP']['Q_1']:.4f} / "
      f"{T['SUM']['NL_UP'] - T['SUM']['NLP']['Q_1']:.4f} / {T['P4NL']:.4f} / {tot[0]:.4f}")
print(f"\n({time.time() - T0:.0f} s)")
