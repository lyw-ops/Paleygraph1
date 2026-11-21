#!/usr/bin/env python3
"""Round 185 cold call `cold-prime-picard-leaf-inequivalence`: tails of the depth expansion
(own implementation; uses paley-185-cold-model.py and re-runs paley-185-cold-picard-leaves.py
silently at depth 3 for its object lists).

  (T1) Fourier-truncation terms omitted from the explicit enumeration (roots |k'| >= 8, seed lines
       |k| >= 7, bhat |2i| >= 8, e_c |c| >= 7) at linear depth <= 5 and nonlinear depth <= 3:
       certified unsigned upper bounds (outward balls).  Per-simple dimension bounds are the
       Prop. A bound of Round 184: dim K(J^c (x) F_1 (x) ... (x) F_m) <= (m + |c|) prod dim F_i.
  (T2) linear depth >= 6: certified, by the accepted Round 184 Prop. B/C value
       g_S = sum_m G_m(L_S) <= 2.467879 and the Prop. C word expansion with the omitted seed
       lines (per-step ratio tau): sum_{m>=1} ||L_S,full^m|| <= g_S/(1 - tau g_S) - 1.
  (T3) nonlinear depth 4: exact enumeration (evidence for the uncertified nonlinear tail):
       unsigned price, and the price of objects that could contain (pre-transport multiset
       containment) a linear simple of depth 1..3 or a root with OPPOSITE sign.
Replay:  .venv/bin/python -B research/paley-185-cold-tails.py
"""
import contextlib
import importlib.util
import io
import os
import runpy
import time

import numpy as np
from flint import acb, arb

T0 = time.time()
_here = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("m185", os.path.join(_here, "paley-185-cold-model.py"))
M = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(M)
os.environ["P185_DEPTH"] = os.environ.get("P185_TAIL_DEPTH", "3")
with contextlib.redirect_stdout(io.StringIO()):
    G = runpy.run_path(os.path.join(_here, "paley-185-cold-picard-leaves.py"))
LIN, W, PRE, COEF, NL, sgn_ref = G["LIN"], G["W"], G["PRE"], G["COEF"], G["NL"], G["sgn_ref"]
SUM = G["SUMMARY"]
ROOTS, SEED, IH, EC = G["ROOTS"], G["SEED"], G["IH"], G["EC"]
TS, S = G["TS"], G["S"]


def up(z):
    """upper bound (float) of a real arb or of |acb|"""
    if isinstance(z, acb):
        return M.upper_abs(z)
    return float(z.upper()) * (1 + 1e-12) + 1e-300


TSU = up(TS)                      # |2 sqrt t| <=
TSL = M.lower_abs(TS)             # |2 sqrt t| >=
SU = up(S)
VARU = up(M.VARPI)
KMAX = 60                         # explicit index range for the omitted-term sums; beyond: geometric


def cabs(kind, k):
    """uniform upper bound of |coefficient of J^k|"""
    fn = {"bp": M.bprime, "bh": M.bhat, "g": M.ghat, "e": M.ecoef}[kind]
    if abs(k) <= 14:
        return up(fn(k))
    return M.coef_abs_up_tail(kind, k)


# ------------------------------------------------------------------ T1. Fourier truncation
print("== T1. Fourier-truncation terms omitted from the enumeration (certified unsigned upper bounds) ==")
roots_all = [k for k in range(-KMAX, KMAX + 1, 2) if k != 0]
seed_all = [k for k in range(-KMAX - 1, KMAX + 2, 2)]
ih_all = list(range(-KMAX, KMAX + 1, 2))
geo = 1e-25                       # remainder of every sum beyond |index| = KMAX: |beta|^30 < 1e-27
# P(h_1) pieces: 2|sqrt t| |b'_k| |k|
R_all = sum(TSU * cabs("bp", k) * abs(k) for k in roots_all) + geo
R_in = sum(TSU * cabs("bp", k) * abs(k) for k in ROOTS)
R_out = R_all - sum(M.lower_abs(TS * M.bprime(k)) * abs(k) for k in ROOTS)
rho_in = sum(VARU * cabs("g", k) * (1 + abs(k)) for k in SEED)
rho_out = sum(VARU * cabs("g", k) * (1 + abs(k)) for k in seed_all if abs(k) >= 7) + geo
rho_all = rho_in + rho_out
print(f"   roots: P(h_1) over all k' <= {M.cl(R_all)}; omitted |k'| >= 8: <= {M.ce(R_out)}")
print(f"   seed per-step ratio (1+|k|) varpi |ghat_k|: kept <= {M.cl(rho_in)}, omitted |k| >= 7: tau <= {M.ce(rho_out)}")
# linear depth j: omitted paths have an omitted root or an omitted step
om_lin = {}
for j in range(0, 6):
    om_lin[j] = R_out * rho_all ** j + R_all * (rho_all ** j - rho_in ** j)
OM_LIN_15 = sum(om_lin[j] for j in range(1, 6))
OM_LIN_13 = sum(om_lin[j] for j in range(1, 4))
print("   omitted linear paths, depth j = 0..5: " + ", ".join(M.ce(om_lin[j], 2) for j in range(6)))
# nonlinear depth <= 3: B_all - B_kept with the Prop. A per-simple bound
bh_w_all = sum(cabs("bh", i) * (2 + abs(i)) for i in ih_all) + geo
bh_w_in = sum(cabs("bh", i) * (2 + abs(i)) for i in IH)
P1_all, P1_in = R_all, R_in
# P(L_S h_1) bound per (l, c): |s ghat_c b'_l| (1+|c|)|l|
L1_all = sum(SU * cabs("g", c) * cabs("bp", l) * (1 + abs(c)) * abs(l) for c in seed_all for l in roots_all) + geo
L1_in = sum(SU * cabs("g", c) * cabs("bp", l) * (1 + abs(c)) * abs(l) for c in SEED for l in ROOTS)
q_fac = 0.5 / TSL
OM_Q = q_fac * (bh_w_all * P1_all ** 2 - bh_w_in * P1_in ** 2)
PQ_all = q_fac * bh_w_all * P1_all ** 2
OM_LQ = PQ_all * rho_all - (q_fac * bh_w_in * P1_in ** 2) * rho_in
OM_X = (1 / TSL) * (bh_w_all * P1_all * L1_all - bh_w_in * P1_in * L1_in)
e_w_all = sum(cabs("e", c) * (3 + abs(c)) for c in seed_all) + geo
e_w_in = sum(cabs("e", c) * (3 + abs(c)) for c in EC)
c_fac = (1 / 6) * 3 * SU / TSL ** 3
OM_C = c_fac * (e_w_all * P1_all ** 3 - e_w_in * P1_in ** 3)
OM_NL = OM_Q + OM_LQ + OM_X + OM_C
print(f"   omitted nonlinear (depth <= 3): Q_1 {M.ce(OM_Q, 2)}, L_S Q_1 {M.ce(OM_LQ, 2)}, X_1 {M.ce(OM_X, 2)}, C_1 {M.ce(OM_C, 2)}; "
      f"total <= {M.ce(OM_NL)}")
T_OMIT_13 = OM_LIN_13 + OM_NL
T_OMIT_15 = OM_LIN_15 + OM_NL

# ------------------------------------------------------------------ T2. linear depth >= 4 and >= 6
print("\n== T2. linear chain beyond the enumeration (certified) ==")
G_S = 2.467879          # Round 184 Prop. B/C (accepted): sum_{m>=0} G_m(L_S) <= 2.467879, uniform on Q
gfull = G_S / (1 - rho_out * G_S)
P3 = sum(M.upper_abs(COEF[p]) * M.dim(W[p]) for p in LIN if len(p) == 4) + om_lin[3]
# depth-5 path sum from the depth-5 run of the leaves script (printed there): recomputed here
os.environ["P185_DEPTH"] = "5"
with contextlib.redirect_stdout(io.StringIO()):
    G5 = runpy.run_path(os.path.join(_here, "paley-185-cold-picard-leaves.py"))
P5 = sum(M.upper_abs(G5["COEF"][p]) * M.dim(G5["W"][p]) for p in G5["LIN"] if len(p) == 6) + om_lin[5]
T_LIN_GE4 = (gfull - 1) * P3
T_LIN_GE6 = (gfull - 1) * P5
print(f"   g_S (Round 184) <= {G_S}; with omitted seed lines: sum_(m>=1) ||L_S,full^m|| <= {M.cl(gfull - 1)}")
print(f"   P(L_S^3 h_1) <= {M.cl(P3)}  =>  sum_(j>=4) P(L_S^j h_1) <= {M.cl(T_LIN_GE4)}")
print(f"   P(L_S^5 h_1) <= {M.cl(P5)}  =>  sum_(j>=6) P(L_S^j h_1) <= {M.cl(T_LIN_GE6)}")
print(f"   (depth 4 and 5 linear simples are proved inequivalent to every depth <= 3 simple: leaves script, depth 5 run)")

# ------------------------------------------------------------------ T3. nonlinear depth 4 (exact enumeration)
print("\n== T3. nonlinear pieces of depth 4 (exact enumeration; evidence for the nonlinear tail) ==")
t1 = time.time()
INV_TS = 1 / TS
PHI3 = -3 * S / (TS * TS * TS)
PHI4 = 3 / (TS * TS * TS)
N4 = {}


def add4(key, pre, coef, kind):
    if key in N4:
        N4[key]["coef"] += coef
        return
    N4[key] = dict(pre=pre, W=M.transport(pre), coef=coef, kind=kind)


lin1 = [p for p in LIN if len(p) == 2]
lin2 = [p for p in LIN if len(p) == 3]
nl3 = [k for k, v in NL.items() if v["depth"] == 3]
qk = [k for k, v in NL.items() if v["kind"] == "Q_1"]
# (a) L_S of the depth-3 nonlinear pieces
for k in nl3:
    for c in SEED:
        add4(("L3", c, k), M.shift(NL[k]["W"], c), M.VARPI * M.ghat(c) * NL[k]["coef"], "L_S(L_S Q_1 + X_1 + C_1)")
# (b) K(Phi'' h_1 h^(2)), h^(2) = L_S^2 h_1 + Q_1
for i in IH:
    for k in ROOTS:
        for p in lin2:
            add4(("Xb", i, k, p), M.shift(M.tensor(W[(k,)], W[p]), i), INV_TS * M.bhat(i) * COEF[(k,)] * COEF[p],
                 "K(Phi'' h_1 L_S^2 h_1)")
        for q in qk:
            add4(("Xq", i, k, q), M.shift(M.tensor(W[(k,)], NL[q]["W"]), i),
                 INV_TS * M.bhat(i) * COEF[(k,)] * NL[q]["coef"], "K(Phi'' h_1 Q_1)")
# (c) (1/2) K(Phi'' (L_S h_1)^2)
for i in IH:
    for a_ in range(len(lin1)):
        for b_ in range(a_, len(lin1)):
            pa, pb = lin1[a_], lin1[b_]
            mult = 1 if a_ == b_ else 2
            add4(("Y", i, pa, pb), M.shift(M.tensor(W[pa], W[pb]), i),
                 acb(0.5 * mult) * INV_TS * M.bhat(i) * COEF[pa] * COEF[pb], "(1/2)K(Phi'' (L_S h_1)^2)")
# (d) (1/2) K(Phi''' h_1^2 L_S h_1)   [ (1/6) * 3 ]
for c in EC:
    for k1 in ROOTS:
        for k2 in ROOTS:
            for p in lin1:
                key = ("C2", c, tuple(sorted((k1, k2))), p)
                pre = M.shift(M.tensor(M.tensor(W[(k1,)], W[(k2,)]), W[p]), c)
                add4(key, pre, acb(0.5) * PHI3 * M.ecoef(c) * COEF[(k1,)] * COEF[(k2,)] * COEF[p],
                     "(1/2)K(Phi''' h_1^2 L_S h_1)")
# (e) (1/24) K(Phi'''' h_1^4)
for c in IH:
    for ks in __import__("itertools").product(ROOTS, repeat=4):
        key = ("Q4", c, tuple(sorted(ks)))
        if key in N4:
            N4[key]["coef"] += acb(1) / 24 * PHI4 * M.fcoef(c) * COEF[(ks[0],)] * COEF[(ks[1],)] * COEF[(ks[2],)] * COEF[(ks[3],)]
            continue
        pre = M.shift(M.tensor(M.tensor(M.tensor(W[(ks[0],)], W[(ks[1],)]), W[(ks[2],)]), W[(ks[3],)]), c)
        add4(key, pre, acb(1) / 24 * PHI4 * M.fcoef(c) * COEF[(ks[0],)] * COEF[(ks[1],)] * COEF[(ks[2],)] * COEF[(ks[3],)],
             "(1/24)K(Phi'''' h_1^4)")
assert all(M.valid(v["W"]) for v in N4.values())
print(f"   {len(N4)} objects ({time.time() - t1:.1f} s)")
kinds = []
for v in N4.values():
    if v["kind"] not in kinds:
        kinds.append(v["kind"])
P4NL = 0.0
for kd in kinds:
    vs = [v for v in N4.values() if v["kind"] == kd]
    pr = sum(M.upper_abs(v["coef"]) * M.dim(v["W"]) for v in vs)
    P4NL += pr
    print(f"   {kd:28s}: {len(vs):6d} objects, unsigned price <= {M.cl(pr)}")
print(f"   all nonlinear depth 4: unsigned <= {M.cl(P4NL)}   (depth 2: {M.cl(SUM['NLP']['Q_1'])}; depth 3: "
      f"{M.cl(SUM['NL_UP'] - SUM['NLP']['Q_1'])})")

# containment of linear depth 0..3 pre-data in the depth-4 nonlinear pre-data (numpy, exact integers)
S_lin = [p for p in LIN if len(p) <= 4]
allw = set()
for p in S_lin:
    for f in (0, 1):
        allw.update(w for w, _ in PRE[p][f])
for v in N4.values():
    for f in (0, 1):
        allw.update(w for w, _ in v["pre"][f])
wl = sorted(allw)
idx = {w: n for n, w in enumerate(wl)}
nw = len(wl)


def vec(Wx):
    x = np.zeros(2 * nw, dtype=np.int64)
    for f in (0, 1):
        for w, c in Wx[f]:
            x[f * nw + idx[w]] = c
    return x


Lmat = np.stack([vec(PRE[p]) for p in S_lin])
Lsgn = np.array([sgn_ref(COEF[p]) for p in S_lin])
Ldep = np.array([len(p) - 1 for p in S_lin])
t1 = time.time()
opp13 = opp0 = any13 = 0.0
for v in N4.values():
    x = vec(v["pre"])
    hit = np.all(Lmat <= x, axis=1)
    if not hit.any():
        continue
    sN = sgn_ref(v["coef"])
    pr = M.upper_abs(v["coef"]) * M.dim(v["W"])
    h13 = hit & (Ldep >= 1)
    h0 = hit & (Ldep == 0)
    if h13.any():
        any13 += pr
        if (Lsgn[h13] * sN < 0).any():
            opp13 += pr
    if h0.any() and (Lsgn[h0] * sN < 0).any():
        opp0 += pr
print(f"   containment scan ({time.time() - t1:.1f} s): depth-4 nonlinear objects that could contain a linear "
      f"depth 1-3 simple: price <= {M.cl(any13)}; with OPPOSITE sign: <= {M.cl(opp13)}; an opposite-sign root: <= {M.cl(opp0)}")

# ------------------------------------------------------------------ summary
print("\n== summary: model A_X-price of h - h_1 and of h ==")
# For the opposite-sign refinement a same-sign overlap only increases |Re(c_M + delta_M)| >= |Re c_M|,
# so the linear part is priced here by certified lower bounds of |Re c_M| (coefficients are complex on Q).


def re_lower(paths):
    return sum(max(0.0, float(abs(COEF[p].real).lower()) * (1 - 1e-12)) * M.dim(W[p]) for p in paths)


L13 = re_lower([p for p in LIN if 2 <= len(p) <= 4])
L03 = re_lower([p for p in LIN if len(p) <= 4])
print(f"   linear depth 1-3 priced by |Re c|: >= {M.fl(L13)} (by |c|: {M.fl(SUM['L13'])}); depth 0-3: >= {M.fl(L03)}")
# depth <= 3 nonlinear objects with an opposite-sign possible overlap (from the leaves script, Section 6)
nso = {}
for lab, cond in (("13", lambda p: 2 <= len(p) <= 4), ("03", lambda p: len(p) <= 4)):
    tot = 0.0
    for k, v in NL.items():
        hs = [p for p in G["touch"][k] if cond(p)]
        if hs and any(sgn_ref(v["coef"]) * sgn_ref(COEF[p]) < 0 for p in hs):
            tot += M.upper_abs(v["coef"]) * M.dim(v["W"])
    nso[lab] = tot
print(f"   depth <= 3 truncation, h - h_1: >= {M.fl(SUM['L13'] - SUM['T_13'])} (all touching subtracted), "
      f">= {M.fl(L13 - nso['13'])} (opposite-sign touching subtracted);  <= {M.cl(SUM['U13'] + SUM['NL_UP'])}")
print(f"   depth <= 3 truncation, h    : >= {M.fl(SUM['L03'] - SUM['T_03'])} (all touching), >= {M.fl(L03 - nso['03'])} (opposite-sign);"
      f"  <= {M.cl(SUM['U03'] + SUM['NL_UP'])}")
full13 = L13 - nso["13"] - opp13 - T_LIN_GE6 - T_OMIT_15
full03 = L03 - nso["03"] - opp13 - opp0 - T_LIN_GE6 - T_OMIT_15 - om_lin[0]
print(f"   full model, conditional on the nonlinear depth >= 5 overlap N5 (uncertified):")
print(f"      A_X(h - h_1) >= {M.fl(full13)} - N5   [= {M.fl(L13)} - {M.cl(nso['13'])} (depth<=3 opp.) - {M.cl(opp13)} (depth 4 opp.)"
      f" - {M.cl(T_LIN_GE6)} (linear j>=6) - {M.ce(T_OMIT_15)} (Fourier)]")
print("      N5 := opposite-sign overlap mass of the nonlinear pieces of depth >= 5 and of the Fourier-omitted"
      " depth-4 nonlinear terms")
print(f"      A_X(h)       >= {M.fl(full03)} - N5")
print(f"   route survives in the model only if N5 >= {M.fl(full13 - 0.3411, 4)} (h - h_1) or >= {M.fl(full03 - 0.7499, 4)} (h)")
print(f"\n({time.time() - T0:.1f} s)")
