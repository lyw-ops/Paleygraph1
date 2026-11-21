#!/usr/bin/env python3
"""Round 185 cold call `cold-prime-picard-leaf-inequivalence`: identification of the transported
simples of the Picard pieces and the exact signed model A_X-price to depth 3 (own implementation).

Depth of a term = (number of transports K in its expression tree) - 1.  The depth-graded pieces:
    h^(0) = h_1 = 2 sqrt t sum_{k'} b'_{k'} K(J^{k'})                         (roots)
    h^(1) = L_S h_1
    h^(2) = L_S^2 h_1 + Q_1,                Q_1 = (1/2) K(Phi''(S) h_1^2)
    h^(3) = L_S^3 h_1 + L_S Q_1 + X_1 + C_1, X_1 = K(Phi''(S) h_1 L_S h_1),
                                             C_1 = (1/6) K(Phi'''(S) h_1^3)
from h = h_1 + L_S h + sum_{m>=2} K(Phi^(m)(S) h^m)/m!  (frozen-base fixed point, mark removed).
Ranges kept exactly: roots |k'| <= 6, seed lines |k| <= 5, bhat |2i| <= 6, e_c |c| <= 5;
everything else is bounded (unsigned) in paley-185-cold-tails.py.

Identification criterion (report Section 2):
  (C1) different weight data  =>  inequivalent  (weight data is an isomorphism invariant);
  (C2) Round 80: K and J^c are injective on isomorphism classes, so
       K(J^a X) ~ K(J^b Y)  <=>  J^a X ~ J^b Y  <=>  X ~ J^(b-a) Y.
  Peeling stops at a pair X ~ J^c Y with c != 0 (twist outside K); there only (C1) is used.
  Pairs not separated are "possibly equal"; blocks = connected components.  Merging can only
  lower sum_B dim_B |sum_{p in B} c_p|, so the block price is a certified LOWER bound of the
  model price of the linear chain (each linear path object is a single simple, Round 80).

Every printed coefficient bound is an outward ball (acb) containing all values on
Q x {p >= 10^6}; no floating number enters a certified statement except as an outward-rounded
endpoint of such a ball.
Replay:  .venv/bin/python -B research/paley-185-cold-picard-leaves.py
"""
import importlib.util
import itertools
import os
import sys
import time
from collections import defaultdict

from flint import acb, arb

_here = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("m185", os.path.join(_here, "paley-185-cold-model.py"))
M = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(M)

T0 = time.time()
ROOTS = (2, -2, 4, -4, 6, -6)
SEED = (1, -1, 3, -3, 5, -5)
IH = (0, 2, -2, 4, -4, 6, -6)
EC = (1, -1, 3, -3, 5, -5)
DEPTH = int(os.environ.get("P185_DEPTH", "5"))

S = acb(M.S_BALL)
TS = M.TWO_SQT

# ------------------------------------------------------------------ 1. linear chain L_S^j h_1
# path p = (k', k_1, ..., k_j);  object O(p) = K(J^{k_j} O(p')),  O((k',)) = K(J^{k'})
# coefficient c_p = 2 sqrt t (s/(2 sqrt t))^j b'_{k'} prod ghat_{k_i}
W = {}
PRE = {}
COEF = {}
for kp in ROOTS:
    p = (kp,)
    PRE[p] = M.line(kp)
    W[p] = M.transport(PRE[p])
    COEF[p] = TS * M.bprime(kp)
frontier = [(kp,) for kp in ROOTS]
for j in range(1, DEPTH + 1):
    new = []
    for p in frontier:
        for k in SEED:
            q = p + (k,)
            PRE[q] = M.shift(W[p], k)
            W[q] = M.transport(PRE[q])
            COEF[q] = COEF[p] * M.VARPI * M.ghat(k)
            new.append(q)
    frontier = new
LIN = list(W.keys())
assert all(M.valid(W[p]) for p in LIN)
print(f"== 1. linear chain to depth {DEPTH}: {len(LIN)} path objects; all valid simples (refill >= 0, "
      f"sum|w| = 2r): True")
for j in range(DEPTH + 1):
    ps = [p for p in LIN if len(p) == j + 1]
    up = sum(M.upper_abs(COEF[p]) * M.dim(W[p]) for p in ps)
    lo = sum(M.lower_abs(COEF[p]) * M.dim(W[p]) for p in ps)
    dims = sorted(set(M.dim(W[p]) for p in ps))
    print(f"   depth {j}: {len(ps):5d} paths, unsigned path-summed price in [{M.fl(lo)}, {M.cl(up)}], "
          f"dims {dims[:8]}{' ...' if len(dims) > 8 else ''} (max {dims[-1]})")


# ------------------------------------------------------------------ 2. identification
def sep_reason(p, q):
    """None if O(p), O(q) are possibly equal; otherwise the reason they are proved inequivalent."""
    if p == q:
        return None
    if W[p] != W[q]:
        return "C1"
    if PRE[p] != PRE[q]:
        return "C2:pre"            # K injective, and the pre-transport data differ
    if len(p) == 1 or len(q) == 1:
        # both roots with equal pre data are equal paths; a root vs a non-root has a line
        # pre-object vs a dim >= 2 pre-object, which PRE already separated
        return None if p == q else "C2:root"
    a, b = p[-1], q[-1]
    if a == b:
        return sep_reason(p[:-1], q[:-1])
    c = b - a
    if W[p[:-1]] != M.shift(W[q[:-1]], c):
        return "C2+C1:twist"
    return None                     # X ~ J^c Y not excluded: possibly equal (twin pair)


groups = defaultdict(list)
for p in LIN:
    groups[W[p]].append(p)
multi = {w: ps for w, ps in groups.items() if len(ps) > 1}
npairs = sum(len(ps) * (len(ps) - 1) // 2 for ps in multi.values())
reasons = defaultdict(int)
undecided = []
for w, ps in multi.items():
    for p, q in itertools.combinations(ps, 2):
        r = sep_reason(p, q)
        if r is None:
            undecided.append((p, q))
        else:
            reasons[r] += 1
print(f"\n== 2. identification of the {len(LIN)} linear path simples ==")
print(f"distinct weight data: {len(groups)}; weight-data classes with >1 path: {len(multi)} "
      f"({npairs} pairs)")
print(f"pairs separated by peeling: " + ", ".join(f"{k}: {v}" for k, v in sorted(reasons.items())))
print(f"pairs NOT separated (possibly equal; twist X ~ J^c Y with equal weight data): {len(undecided)}")

# union-find blocks
parent = {p: p for p in LIN}


def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


for p, q in undecided:
    parent[find(p)] = find(q)
blocks = defaultdict(list)
for p in LIN:
    blocks[find(p)].append(p)
BL = [ps for ps in blocks.values()]
nb = [ps for ps in BL if len(ps) > 1]
print(f"blocks: {len(BL)}; blocks with >1 member: {len(nb)}")


def sgn_ref(z):
    """sign of the real part if the ball excludes 0 on the real axis, else 0"""
    re = z.real
    if re > 0:
        return 1
    if re < 0:
        return -1
    return 0


opp = []
for ps in nb:
    sg = set(sgn_ref(COEF[p]) for p in ps)
    if 0 in sg:
        print("  WARNING: undetermined sign in block", ps)
    if 1 in sg and -1 in sg:
        opp.append(ps)
print(f"blocks with members of opposite sign: {len(opp)}")
for ps in sorted(nb, key=lambda ps: -max(M.upper_abs(COEF[p]) for p in ps))[:40]:
    d = M.dim(W[ps[0]])
    tot = acb(0)
    for p in ps:
        tot += COEF[p]
    mem = "; ".join(f"{p} c={float(COEF[p].real.mid()):+.3e}" for p in ps)
    print(f"  block dim {d}: |sum c| dim in [{M.lower_abs(tot) * d:.3e}, {M.upper_abs(tot) * d:.3e}]"
          f"  unsigned {sum(M.upper_abs(COEF[p]) for p in ps) * d:.3e} :: {mem}")

# signed prices of the linear chain, per depth and cumulative
print("\n== 3. signed block price of the linear chain (certified lower / upper; uniform on Q x {p>=10^6}) ==")


def block_price(paths):
    """sum over blocks (restricted to the given paths) of dim |sum c|: (lower, upper, unsigned_up)"""
    pset = set(paths)
    lo = up = uns = 0.0
    for ps in BL:
        mem = [p for p in ps if p in pset]
        if not mem:
            continue
        d = M.dim(W[mem[0]])
        tot = acb(0)
        for p in mem:
            tot += COEF[p]
            uns += M.upper_abs(COEF[p]) * d
        lo += M.lower_abs(tot) * d
        up += M.upper_abs(tot) * d
    return lo, up, uns


for j in range(DEPTH + 1):
    ps = [p for p in LIN if len(p) == j + 1]
    lo, up, uns = block_price(ps)
    print(f"   depth {j} alone: signed in [{M.fl(lo)}, {M.cl(up)}]  (unsigned <= {M.cl(uns)})")
ps_rest = [p for p in LIN if 2 <= len(p)]
lo_r, up_r, uns_r = block_price(ps_rest)
lo_h, up_h, uns_h = block_price(LIN)
print(f"   depths 1..{DEPTH} (linear part of h - h_1): signed in [{M.fl(lo_r)}, {M.cl(up_r)}]  (unsigned <= {M.cl(uns_r)})")
print(f"   depths 0..{DEPTH} (linear part of h):       signed in [{M.fl(lo_h)}, {M.cl(up_h)}]  (unsigned <= {M.cl(uns_h)})")

# mirror symmetry (other lift)
mir_ok = all(M.mirror(W[p]) == W[tuple(-x for x in p)] for p in LIN)
coef_ok = all(COEF[p].overlaps(COEF[tuple(-x for x in p)])
              for p in LIN)
print(f"\nlift symmetry: W(-p) = fibre exchange of W(p) for all paths: {mir_ok}; c(-p) = c(p) (balls overlap): {coef_ok}")

# ------------------------------------------------------------------ 4. nonlinear pieces to depth 3
# Q_1 = (1/2) K(Phi2 h_1^2), L_S Q_1, X_1 = K(Phi2 h_1 L_S h_1), C_1 = (1/6) K(Phi3 h_1^3),
# Phi2 = Phi_t''(S), Phi3 = Phi_t'''(S).
# A nonlinear object N = K(P_N) with P_N = J^c (x) F_1 (x) ... may be reducible.  It can contribute
# to the coordinate of a linear simple M = K(P_M) only if P_M is isomorphic to a constituent of P_N
# (K additive, injective on non-punctual simples; P_N semisimple), which forces the multiset
# containment W(P_M) <= W(P_N) at both fibres (weight data of a direct sum = union).
INV_TS = 1 / TS
NL = {}          # key -> dict(pre, W, coef, depth, kind)


def add_nl(key, pre, coef, depth, kind):
    if key in NL:
        NL[key]["coef"] += coef
        return
    NL[key] = dict(pre=pre, W=M.transport(pre), coef=coef, depth=depth, kind=kind)


for i in IH:
    for k in ROOTS:
        for l in ROOTS:
            key = ("Q", i, tuple(sorted((k, l))))
            pre = M.shift(M.tensor(W[(k,)], W[(l,)]), i)
            add_nl(key, pre, acb(0.5) * INV_TS * M.bhat(i) * COEF[(k,)] * COEF[(l,)], 2, "Q_1")
QKEYS = [k for k in NL if k[0] == "Q"]
for qk in QKEYS:
    for c in SEED:
        pre = M.shift(NL[qk]["W"], c)
        add_nl(("LQ", c, qk), pre, M.VARPI * M.ghat(c) * NL[qk]["coef"], 3, "L_S Q_1")
for i in IH:
    for k in ROOTS:
        for l in ROOTS:
            for c in SEED:
                key = ("X", i, k, (l, c))
                pre = M.shift(M.tensor(W[(k,)], W[(l, c)]), i)
                add_nl(key, pre, INV_TS * M.bhat(i) * COEF[(k,)] * COEF[(l, c)], 3, "X_1")
PHI3 = -3 * S / (TS * TS * TS)
for c in EC:
    for k1 in ROOTS:
        for k2 in ROOTS:
            for k3 in ROOTS:
                key = ("C", c, tuple(sorted((k1, k2, k3))))
                pre = M.shift(M.tensor(M.tensor(W[(k1,)], W[(k2,)]), W[(k3,)]), c)
                add_nl(key, pre, acb(1) / 6 * PHI3 * M.ecoef(c) * COEF[(k1,)] * COEF[(k2,)] * COEF[(k3,)],
                       3, "C_1")
assert all(M.valid(v["W"]) for v in NL.values())
print(f"\n== 4. nonlinear pieces to depth 3 ({len(NL)} objects after merging tensor permutations) ==")
NLP = {}
for kind in ("Q_1", "L_S Q_1", "X_1", "C_1"):
    vs = [v for v in NL.values() if v["kind"] == kind]
    up = sum(M.upper_abs(v["coef"]) * M.dim(v["W"]) for v in vs)
    lo = sum(M.lower_abs(v["coef"]) * M.dim(v["W"]) for v in vs)
    NLP[kind] = up
    print(f"   {kind:8s}: {len(vs):5d} objects, unsigned price in [{M.fl(lo)}, {M.cl(up)}], "
          f"max dim {max(M.dim(v['W']) for v in vs)}")
NL_UP = sum(NLP.values())
print(f"   all nonlinear to depth 3: unsigned <= {M.cl(NL_UP)}")

# containment against linear simples (pre-transport level)
lin_by_dim = defaultdict(list)
for p in LIN:
    lin_by_dim[M.dim(PRE[p])].append(p)
lin_dims = sorted(lin_by_dim)


def ext(Wx):
    return [(min(w for w, _ in Wx[f]), max(w for w, _ in Wx[f])) for f in (0, 1)]


LEXT = {p: ext(PRE[p]) for p in LIN}
touch = {}
t1 = time.time()
for key, v in NL.items():
    P = v["pre"]
    dP = M.dim(P)
    eP = ext(P)
    hits = []
    for d in lin_dims:
        if d > dP:
            break
        for p in lin_by_dim[d]:
            e = LEXT[p]
            if e[0][0] < eP[0][0] or e[0][1] > eP[0][1] or e[1][0] < eP[1][0] or e[1][1] > eP[1][1]:
                continue
            if M.contains(PRE[p], P):
                hits.append(p)
    touch[key] = hits
print(f"   containment scan done ({time.time() - t1:.1f} s)")
for kind in ("Q_1", "L_S Q_1", "X_1", "C_1"):
    vs = [(k, v) for k, v in NL.items() if v["kind"] == kind]
    for lab, cond in (("roots (h_1)", lambda p: len(p) == 1),
                      ("linear depth 1-3", lambda p: 2 <= len(p) <= 4),
                      (f"linear depth 4-{DEPTH}", lambda p: len(p) >= 5)):
        tk = [(k, v) for k, v in vs if any(cond(p) for p in touch[k])]
        pr = sum(M.upper_abs(v["coef"]) * M.dim(v["W"]) for k, v in tk)
        print(f"   {kind:8s} objects that could contain a {lab:18s}: {len(tk):5d}, unsigned price <= {M.cl(pr)}")


def nl_touch_price(cond):
    return sum(M.upper_abs(v["coef"]) * M.dim(v["W"]) for k, v in NL.items() if any(cond(p) for p in touch[k]))


T_13 = nl_touch_price(lambda p: 2 <= len(p) <= 4)
T_15 = nl_touch_price(lambda p: 2 <= len(p))
T_05 = nl_touch_price(lambda p: True)
T_03 = nl_touch_price(lambda p: len(p) <= 4)

# full weight-data coincidences (as if every nonlinear object were simple)
allW = defaultdict(list)
for p in LIN:
    allW[W[p]].append(("L", p))
for k, v in NL.items():
    allW[v["W"]].append(("N", k))
coll = {w: m for w, m in allW.items() if len(m) > 1}
ln = [m for m in coll.values() if any(x[0] == "L" for x in m) and any(x[0] == "N" for x in m)]
nn = [m for m in coll.values() if all(x[0] == "N" for x in m)]


def cf(x):
    return COEF[x[1]] if x[0] == "L" else NL[x[1]]["coef"]


nn_opp = [m for m in nn if len(set(sgn_ref(cf(x)) for x in m)) > 1]
print(f"   equal full weight data: linear-vs-nonlinear classes {len(ln)}; nonlinear-only classes {len(nn)} "
      f"(with opposite signs: {len(nn_opp)})")
for m in ln[:10]:
    print("     L/N class:", [(x[0], x[1], f"{float(cf(x).real.mid()):+.2e}") for x in m])
nn_opp_price = 0.0
for m in nn_opp:
    d = M.dim(NL[m[0][1]]["W"])
    tot = acb(0)
    for x in m:
        tot += cf(x)
    uns = sum(M.upper_abs(cf(x)) for x in m)
    nn_opp_price += (uns - M.lower_abs(tot)) * d
print(f"   loss if all equal-weight nonlinear objects were identified (signed vs unsigned): <= {M.ce(nn_opp_price)}")

# ------------------------------------------------------------------ 5. depth-3 signed model price
lin13 = [p for p in LIN if 2 <= len(p) <= 4]
lin03 = [p for p in LIN if len(p) <= 4]
lin15 = [p for p in LIN if 2 <= len(p)]
lin05 = list(LIN)
L13, U13, _ = block_price(lin13)
L03, U03, _ = block_price(lin03)
L15, U15, _ = block_price(lin15)
L05, U05, _ = block_price(lin05)
print("\n== 5. model A_X-price of the depth-<=3 truncation (certified, uniform on Q x {p>=10^6}, both lifts) ==")
print(f"   (h - h_1)_<=3: lower >= {M.fl(L13 - T_13)}  [= linear {M.fl(L13)} - nonlinear objects touching it {M.cl(T_13)}];"
      f"  upper <= {M.cl(U13 + NL_UP)}  [= linear {M.cl(U13)} + nonlinear {M.cl(NL_UP)}]")
print(f"   h_<=3        : lower >= {M.fl(L03 - T_03)}  [= linear {M.fl(L03)} - touching {M.cl(T_03)}];"
      f"  upper <= {M.cl(U03 + NL_UP)}")
print(f"   allowances: A_X(h - h_1) < 0.3411 (joint, Duhamel);  A_X(h) < 0.7499 (seed only)")
print(f"   linear part to depth {DEPTH} (all separated): h - h_1 >= {M.fl(L15)}, h >= {M.fl(L05)}; "
      f"nonlinear depth<=3 objects touching these: {M.cl(T_15)} / {M.cl(T_05)}")
SUMMARY = dict(L13=L13, U13=U13, L03=L03, U03=U03, L15=L15, L05=L05, T_13=T_13, T_03=T_03, T_15=T_15,
               T_05=T_05, NL_UP=NL_UP, NLP=NLP)
print(f"\n({time.time() - T0:.1f} s)")

# ------------------------------------------------------------------ 6. sign structure of the possible overlaps
print("\n== 6. possible constituent overlaps (containment) and their signs ==")


def overlap_sign_price(cond):
    same = opp = 0.0
    nso = nss = 0
    for k, v in NL.items():
        hs = [p for p in touch[k] if cond(p)]
        if not hs:
            continue
        sN = sgn_ref(v["coef"])
        sg = set(sN * sgn_ref(COEF[p]) for p in hs)
        pr = M.upper_abs(v["coef"]) * M.dim(v["W"])
        if -1 in sg:
            opp += pr
            nso += 1
        else:
            same += pr
            nss += 1
    return nso, opp, nss, same


for lab, cond in (("roots (h_1)", lambda p: len(p) == 1), ("linear depth 1-3", lambda p: 2 <= len(p) <= 4),
                  (f"linear depth 1-{DEPTH}", lambda p: 2 <= len(p))):
    nso, opp, nss, same = overlap_sign_price(cond)
    print(f"   nonlinear objects possibly containing a {lab:17s} of OPPOSITE sign: {nso:4d} (price <= {M.cl(opp)});"
          f" only same sign: {nss:4d} (price <= {M.cl(same)})")
# the depth-5 linear pairs with equal final weight data
for w, ps in multi.items():
    p, q = ps[0], ps[1]
    print(f"   equal final weight data, dim {M.dim(w)}: {p} vs {q}; separated by {sep_reason(p, q)}; "
          f"signs {sgn_ref(COEF[p])}, {sgn_ref(COEF[q])}")
# examples of Q_1 objects that could contain a root: K(J^2i (x) K(J^k) (x) K(J^l)) containing J^k'
ex = [(k, touch[k]) for k in NL if k[0] == "Q" and any(len(p) == 1 for p in touch[k])][:6]
for k, hs in ex:
    print(f"   Q_1 object {k} could contain roots {[p for p in hs if len(p) == 1]}; coef {float(NL[k]['coef'].real.mid()):+.3e}")
print(f"\n({time.time() - T0:.1f} s)")
