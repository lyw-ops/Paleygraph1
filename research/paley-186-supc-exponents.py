#!/usr/bin/env python3
r"""Round 186, call ordinary-prime-sup-c-heavy-price: exact exponent ledger.

Exact rational arithmetic (fractions.Fraction), standard library only, except the
optional float LP cross-check (--lp, needs numpy + scipy).

Checks the exponent algebra of
research/native-claude-ordinary-prime-sup-c-heavy-price-186.md :

  * reproduction of Round 185 Theorem 2 (11/8 - 1/664);
  * Lemma M (mixed shifted energy) exponent bookkeeping and its Stevens-de Zeeuw
    hypothesis at the scales used;
  * piece parameters (Phase 1 / Phase 2 of the Round 182 extraction) as linear forms
    in the height exponent e and the Phase-2 size exponent mu;
  * pair prices (Hoelder (a), mixed forms I and II) as linear forms;
  * the key inequality  c_pair <= (24/5) gain_pair  in every component case;
  * Theorem A: sup C exponent 11/8 - 5/696, with delta = 1/87, light term 19/14;
  * the binding configuration (0,0,1/87,1/87) attains it (bookkeeping is sharp);
  * Corollary: covariance 625/348 etc.;
  * Proposition X (side result): E^x(h) exponent 31/21;
  * cap / conditional criteria and sensitivity to BSG exponents.

Every exponent is "exponent of p".  Linear forms are dicts {var: Fraction}, key 1 = constant.
Prints ALL OK at the end if every assertion holds.
"""
import sys
from fractions import Fraction as F

ok = True


def check(cond, msg):
    global ok
    print(("ok   " if cond else "FAIL ") + msg)
    ok = ok and bool(cond)


# ---------------------------------------------------------------- linear forms
def L(*pairs, c=0):
    d = {1: F(c)}
    for k, v in pairs:
        d[k] = d.get(k, F(0)) + F(v)
    return d


def add(*forms):
    out = {}
    for f in forms:
        for k, v in f.items():
            out[k] = out.get(k, F(0)) + v
    return {k: v for k, v in out.items() if v != 0 or k == 1}


def scale(s, f):
    return {k: F(s) * v for k, v in f.items()}


def sub(f, g):
    return add(f, scale(-1, g))


def show(f):
    parts = [str(f.get(1, F(0)))]
    for k, v in sorted(((k, v) for k, v in f.items() if k != 1), key=lambda kv: kv[0]):
        parts.append(f"{'+' if v >= 0 else '-'} {abs(v)}*{k}")
    return " ".join(parts)


def nonneg_on_orthant(f):
    """f >= 0 for all nonnegative values of its variables iff all coefficients >= 0."""
    return all(v >= 0 for v in f.values())


T = F(11, 8)
half = F(1, 2)

print("== Round 185 Theorem 2 reproduced ==")
eps, d = F(1, 166), F(1, 415)
r185 = max(T - eps / 4, F(4, 3) + F(20, 3) * eps, F(4, 3) + F(8, 3) * eps + F(2, 3) * d,
           T - F(5, 8) * d, F(19, 14))
check(r185 == T - F(1, 664), "Round 185: max(band, Phase 1, Phase 2, leftover, light) = 11/8 - 1/664")

print("== Lemma M (mixed shifted energy): exponent algebra ==")
# sizes: alpha = |A|, N = |B| = |V|, K' = |VB|/N; s = min(alpha, K'N), b' = max.
# SdZ: h t N <= I << s^{3/4} b'^{1/2} (tN)^{3/4}  =>  t << s^3 b'^2 / (N h^4)
# s^3 b'^2 <= alpha^2 (K'N)^2 min(alpha, K'N);  E <= H alpha N + alpha^2 K'^2 N min / H^2
# H^3 = alpha K'^2 min  =>  E << alpha^{4/3} N K'^{2/3} min^{1/3}
for (A, Nn, Kp) in [(F(1, 2), F(1, 2), F(0)), (F(9, 14), F(1, 2), F(1, 3)), (F(1, 2) + F(1, 87), F(1, 2) - F(1, 87), F(8, 87)),
                    (F(3, 10), F(1, 2), F(1, 5)), (F(7, 10), F(2, 5), F(1, 50))]:
    mn = min(A, Kp + Nn)
    # case split of s^3 b'^2
    s, b = sorted([A, Kp + Nn])
    lhs = 3 * s + 2 * b
    rhs = 2 * A + 2 * (Kp + Nn) + mn
    check(lhs <= rhs, f"s^3 b'^2 <= alpha^2 (K'N)^2 min at (A,N,K')=({A},{Nn},{Kp})")
    H = (A + 2 * Kp + mn) / 3
    E1 = H + A + Nn
    E2 = 2 * A + 2 * Kp + Nn + mn - 2 * H
    check(E1 == E2 == F(4, 3) * A + Nn + F(2, 3) * Kp + mn / 3, "  balance H^3 = alpha K'^2 min gives alpha^{4/3} N K'^{2/3} min^{1/3}")
    # SdZ hypothesis: a n <= min * alpha N^2 / H <= alpha^{4/3} N^2
    an = mn + A + 2 * Nn - H
    check(an <= F(4, 3) * A + 2 * Nn, "  SdZ hypothesis a*n <= alpha^{4/3} N^2 at h >= H")
    # H grows (so h >= H0 constant is automatic for large p)
    check(H > 0, "  H is a positive power of p")
# sizes used: alpha <= 2G/tau0 = p^{1/2+1/7}, N <= p^{1/2}
check(F(4, 3) * (half + F(1, 7)) + 2 * half == F(13, 7) and F(13, 7) < 2,
      "Lemma M hypothesis at the scales used: alpha^{4/3} N^2 <= p^{13/7} = o(p^2)")
# Lemma SE as the case A = B (K' = |VB|/N, alpha = N <= K'N): N^{8/3} K'^{2/3}
check(F(4, 3) + 1 + F(1, 3) == F(8, 3), "Lemma M with A = B, alpha = N: exponent 8/3 in N (Lemma SE)")

print("== Piece parameters (Round 182 extraction at level t = a/2, a = p^-e) ==")
e, es, eg, mu, mus, mug = "e", "e_s", "e_g", "mu", "mu_s", "mu_g"


def pieces(kind, ev, muv):
    """return dict of linear forms: logK, logK' (=4 logK), log total size, log min piece size."""
    if kind == "P1":   # blocks m = sqrt p, K <= C sqrt p/(t^2 m) = C a^-2
        K = L((ev, 2))
        tot = L((ev, 1), c=half)                 # |U| <= 2G/a
        mn = add(L(c=half), scale(-half, K))     # |B| >= m K^{-1/2}
    else:              # Phase 2 at remainder size M = p^{1/2-mu}: K <= C sqrt p/(a^2 M)
        K = L((ev, 2), (muv, 1))
        tot = L((muv, -1), c=half)               # pieces of this phase: total <= 2M
        mn = add(L((muv, -1), c=half), scale(-half, K))
    return dict(K=K, Kp=scale(4, K), tot=tot, mn=mn)


P1 = pieces("P1", es, mus)
P2 = pieces("P2", es, mus)
check(show(P1["mn"]) == show(L((es, -1), c=half)), "P1: |B| >= sqrt p * a")
check(show(P2["mn"]) == show(L((es, -1), (mus, F(-3, 2)), c=half)), "P2: |B| >= p^{1/2-3mu/2} a")


def hol(kind, ev, muv):
    """(a): a * sum_j N(1-B_j) <= a * K'^{1/6} * total * min^{-1/3}  (Lemma SE per piece)"""
    P = pieces(kind, ev, muv)
    return add(L((ev, -1)), scale(F(1, 6), P["Kp"]), P["tot"], scale(F(-1, 3), P["mn"]))


check(show(hol("P1", e, mu)) == show(L((e, F(5, 3)), c=F(1, 3))), "Hoelder slot price P1: 1/3 + 5e/3 (Round 182 Phase 1)")
check(show(hol("P2", e, mu)) == show(L((e, F(2, 3)), (mu, F(1, 6)), c=F(1, 3))), "Hoelder slot price P2: 1/3 + 2e/3 + mu/6 (Round 182 Phase 2)")


def mixed(kind_s, form, A_g, e_s, mu_s, e_g):
    """pair price with structured side kind_s (pieces), generic side of size p^{A_g} at height p^{-e_g}.
    form I : sum_j (alpha^{5/3} |B_j| K'^{2/3})^{1/2}
    form II: sum_j (alpha^{4/3} |B_j|^{4/3} K')^{1/2}"""
    P = pieces(kind_s, e_s, mu_s)
    if form == "I":
        core = add(scale(F(5, 6), A_g), scale(F(1, 3), P["Kp"]), P["tot"], scale(F(-1, 2), P["mn"]))
    else:
        core = add(scale(F(2, 3), A_g), scale(F(1, 2), P["Kp"]), P["tot"], scale(F(-1, 3), P["mn"]))
    return add(core, L((e_s, -1), (e_g, -1)))


A_P1 = L((eg, 1), c=half)      # generic P1 component: size <= 2G/a_g
A_P2 = L((mug, -1), c=half)    # generic P2 component: size <= 2M
fI_11 = mixed("P1", "I", A_P1, es, mus, eg)
check(show(fI_11) == show(L((es, F(19, 6)), (eg, F(-1, 6)), c=F(2, 3))), "form I, P1 structured vs P1 generic: 2/3 + 19e_s/6 - e_g/6")
fII_11 = mixed("P1", "II", A_P1, es, mus, eg)
check(show(fII_11) == show(L((es, F(13, 3)), (eg, F(-1, 3)), c=F(2, 3))), "form II, P1 vs P1: 2/3 + 13e_s/3 - e_g/3")
fI_2x = mixed("P2", "I", L((1, 0)), es, mus, eg)   # generic size left symbolic below
fI_21 = mixed("P2", "I", A_P1, es, mus, eg)
check(show(fI_21) == show(L((es, F(13, 6)), (mus, F(13, 12)), (eg, F(-1, 6)), c=F(2, 3))), "form I, P2 structured vs P1 generic: 2/3 + 13e_s/6 + 13mu_s/12 - e_g/6")
fI_22 = mixed("P2", "I", A_P2, es, mus, eg)
check(show(fI_22) == show(L((es, F(13, 6)), (mus, F(13, 12)), (eg, -1), (mug, F(-5, 6)), c=F(2, 3))), "form I, P2 vs P2 generic: 2/3 + 13e_s/6 + 13mu_s/12 - e_g - 5mu_g/6")
fI_12 = mixed("P1", "I", A_P2, es, mus, eg)
check(show(fI_12) == show(L((es, F(19, 6)), (eg, -1), (mug, F(-5, 6)), c=F(2, 3))), "form I, P1 structured vs P2 generic: 2/3 + 19e_s/6 - e_g - 5mu_g/6")

print("== SdZ gains per slot (Lemma 4 form, sizes of components) ==")
th = {"pt": F(5, 8), "ln": F(3, 4)}


def gain(kind, role, ev, muv):
    if kind == "P1":
        return L((ev, 1 - th[role]))          # a (2G/a)^theta  vs  G^theta
    return L((ev, 1), (muv, th[role]))        # a (2M)^theta, M = p^{1/2-mu}


R = F(24, 5)
print("== Key inequality c_pair <= (24/5) gain_pair in every component case ==")
# P1-P1, with e_i <= e_j written e_j = e_i + w (w >= 0); structured side = lower slot
for (ri, rj) in (("pt", "ln"), ("ln", "pt")):
    # structured slot i at height e_i, generic slot j at e_j = e_i + w
    c = add(L((es, F(19, 6)), c=F(0)), scale(F(-1, 6), L((es, 1), ("w", 1))))     # 19e_i/6 - e_j/6
    g = add(gain("P1", ri, es, mus), {k: v for k, v in add(L((es, 1 - th[rj]), ("w", 1 - th[rj]))).items()})
    diff = sub(scale(R, g), c)
    check(nonneg_on_orthant(diff), f"P1-P1, lower slot role {ri}: (24/5)gain - c = {show(diff)} >= 0")
# P2 structured (slot i) with P1 or P2 generic (slot j): drop -gamma_j <= 0, keep gain of slot i only
for ri in ("pt", "ln"):
    c = L((es, F(13, 6)), (mus, F(13, 12)))
    g = gain("P2", ri, es, mus)
    diff = sub(scale(R, g), c)
    check(nonneg_on_orthant(diff), f"P2 slot (role {ri}) structured: (24/5)gain - c = {show(diff)} >= 0")
# P1-P1 bound c <= 3 min(e_i, e_j), gain >= (5/8) min
check(F(19, 6) - F(1, 6) == 3 and R * F(5, 8) == 3, "P1-P1 at equal heights: c = 3e = (24/5)(5e/8): the binding case")

print("== Theorem A ==")
Gs = F(1, 24) / (1 + R)
check(Gs == F(5, 696), "min(11/8 - G, 4/3 + (24/5)G) is maximal at G = 5/696")
top = T - Gs
check(top == F(4, 3) + R * Gs, "  both sides equal 11/8 - 5/696")
dlt = F(1, 87)
check(F(5, 8) * dlt == Gs, "leftover (Round 182 stop at p^{1/2-delta}, delta = 1/87): 11/8 - 5 delta/8 = 11/8 - 5/696")
check(F(19, 14) < top, "light term tau_0 G^3 = p^{19/14} is below")
check(F(5, 696) > F(1, 664), "5/696 > 1/664 (Round 185)")
check(F(5, 696) / F(1, 664) == F(830, 174), f"improvement factor 5/696 : 1/664 = {float(F(5,696)/F(1,664)):.4f}")
# binding configuration (0,0,e,e) with P1 components, e = 1/87
eb = F(1, 87)
sdz = T - F(3, 8) * eb - F(1, 4) * eb
hold = F(2, 3) + F(2, 3) + F(19, 6) * eb - F(1, 6) * eb
check(sdz == hold == top, "binding configuration e = (0,0,1/87,1/87): SdZ = pair-Hoelder = 11/8 - 5/696")
# all four at the same height e': 11/8 - 5e'/4 vs 4/3 + 6e'
e4 = F(1, 24) / (F(5, 4) + 6)
check(T - F(5, 4) * e4 == top and e4 == F(1, 174), "all four slots at height p^{-1/174}: also 11/8 - 5/696 (second binding family)")

print("== Theorem B (uncapped extraction: blocks = whole remainder) ==")
# component (e, mu): remainder size M = p^{1/2-mu}, -e <= mu <= delta (up to O(1/log p));
# K <= C sqrt p/(a^2 M) = p^{2e+mu}; |B| >= M K^{-1/2}; K' = K^4; pieces of the phase: total <= 2M.
ph = pieces("P2", es, mus)            # same formulas, now with mu allowed down to -e
fI = mixed("P2", "I", L((mug, -1), c=half), es, mus, eg)
check(show(fI) == show(L((es, F(13, 6)), (mus, F(13, 12)), (eg, -1), (mug, F(-5, 6)), c=F(2, 3))),
      "form I, phase component vs phase component: 2/3 + 13e_s/6 + 13mu_s/12 - e_g - 5mu_g/6")
# whole level set (mu = -e): K <= p^e
at_whole = {k: v for k, v in fI.items()}
sub_mu = add(at_whole, scale(at_whole.get(mus, 0), L((es, -1), (mus, -1))), scale(at_whole.get(mug, 0), L((eg, -1), (mug, -1))))
sub_mu = {k: v for k, v in sub_mu.items() if k not in (mus, mug) or v != 0}
check(show(sub_mu) == show(L((es, F(13, 12)), (eg, F(-1, 6)), c=F(2, 3))), "  at mu = -e (whole level sets): 2/3 + 13e_s/12 - e_g/6")
# in u = 2e + mu:  c <= (13/12) u_s - u_g/6, since e_g + 5mu_g/6 - u_g/6 = (2/3)(e_g + mu_g) >= 0
us, ug = "u_s", "u_g"
# (13/12)u_s expressed: 13/12 (2e_s + mu_s) = 13e_s/6 + 13 mu_s/12  -- identical to the structured part
check(F(13, 12) * 2 == F(13, 6), "  structured part = (13/12)(2e_s + mu_s) = (13/12) u_s")
check(F(1) - F(1, 6) * 2 == F(2, 3) and F(5, 6) - F(1, 6) == F(2, 3), "  generic part: e_g + 5mu_g/6 = u_g/6 + (2/3)(e_g + mu_g)")
# gain per slot e + theta mu = theta u - (2 theta - 1) e >= (1 - theta) u  (as e <= u)
for role in ("pt", "ln"):
    t_ = th[role]
    check(t_ - (2 * t_ - 1) == 1 - t_, f"  gain (role {role}) = theta u - (2theta-1) e >= (1-theta) u, 1-theta = {1-t_}")
RB = (F(13, 12) - F(1, 6)) / (F(3, 8) + F(1, 4))
check(RB == F(22, 15), "c <= (11/12) min(u) and gain >= (5/8) min(u): ratio 22/15")
GB = F(1, 24) / (1 + RB)
check(GB == F(5, 296), "Theorem B: sup C exponent 11/8 - 5/296")
dB = GB * F(8, 5)
check(dB == F(1, 37), "  leftover stop delta = 1/37")
check(F(19, 14) < T - GB, "  light term 19/14 below")
# binding families
e1 = F(1, 37)
check(T - F(5, 8) * e1 == F(4, 3) + F(11, 12) * e1 == T - GB, "  binding (0,0,e,e), whole level sets, e = 1/37")
e2 = F(1, 74)
check(T - F(5, 4) * e2 == F(4, 3) + 2 * F(11, 12) * e2 == T - GB, "  binding (e,e,e,e), whole level sets, e = 1/74")
# Lemma M hypothesis: sizes <= p^{1/2+e}; alpha^{4/3} N^2 <= p^{(10/3)(1/2+e)} < p^2 for e <= 1/12
check(F(10, 3) * (half + F(1, 12)) == F(35, 18) and F(35, 18) < 2, "  Lemma M hypothesis holds when all heights e <= 1/12")
check(F(1, 4) * F(1, 12) > GB, "  if some e > 1/12 the SdZ gain (1-theta)e >= 1/48 > 5/296 alone suffices")
check(GB > F(5, 696) > F(1, 664), "5/296 > 5/696 (sqrt p-capped blocks) > 1/664 (Round 185)")
print(f"   5/296 = {float(GB):.6f}, 5/696 = {float(F(5,696)):.6f}, 1/664 = {float(F(1,664)):.6f};  ratio to R185: {float(GB/F(1,664)):.3f}")
# MPRRS Lemma 33 (remark): structured piece with |BB| <= M|B|, generic D: E << M^{3/2} N |D|^{3/2};
# at height 1 (M = O(1)), N = |D| = sqrt p: pair exponent (1/2 + 3/4)/2 = 5/8, floor 5/4
check((half + F(3, 4) * 1) / 2 == F(5, 8) and 2 * F(5, 8) == F(5, 4), "remark: MPRRS Lemma 33 prices a height-1 pair at p^{5/8}; height-1 floor p^{5/4}")
# family (e,e,e,e) is unaffected (MPRRS pair cost 5/8 + 11e/2 there, K-loss M <= K'^2 = K^8)
check(F(5, 8) + F(11, 2) * e2 > F(2, 3) + F(11, 12) * e2, "  at (e,e,e,e), e = 1/74, Lemma M is cheaper than MPRRS: delta_C unchanged")
print("   sensitivity of Theorem B to the BSG doubling exponent c (size loss K^{-1/2}):")
for c in (F(4), F(3), F(8, 3)):
    exc = c / 3 - F(5, 12)          # c e/3 (K'^{1/3}) + 3e/4 (pieces) - e (height) - e/6 (generic)
    dd = F(1, 24) / (1 + exc / F(5, 8))
    print(f"     c = {c}: pair excess {exc} e, delta_C = {dd} ({float(dd):.6f})")
    if c == 4:
        check(dd == F(5, 296), "  c = 4 reproduces 5/296")

print("== Corollary (propagation, Round 184 Prop. 1(iii) / Round 180 chain) ==")
for dC, tagC in ((F(5, 296), "Theorem B"), (F(5, 696), "Theorem A")):
    supC = T - dC
    check(2 * F(31, 21) < supC + 2, f"{tagC}: X^2 below sup C * M_1^2")
    Em = supC + 2
    W32 = 1 + Em / 2
    cov = F(9, 8) + W32 / 4
    print(f"   {tagC}: sum W^(3/2), E(mu) = p^(43/16 - {dC/2}); covariance p^{cov} = p^(115/64 - {dC/8})"
          f"; ||H||_2 = p^(147/128 - {dC/16}); sum w|H|^2 = p^(179/64 - {dC/8})")
    if dC == F(5, 296):
        check(W32 == F(43, 16) - F(5, 592), "  sum W^{3/2}, E(mu) = p^{43/16 - 5/592}")
        check(cov == F(115, 64) - F(5, 2368) == F(2125, 1184), "  one-match covariance p^{2125/1184} = p^{115/64 - 5/2368}")
    else:
        check(cov == F(625, 348), "  (Theorem A) covariance p^{625/348}")
check(F(2125, 1184) < F(625, 348) < F(1193, 664), "2125/1184 < 625/348 < 1193/664")
print(f"   2125/1184 = {float(F(2125,1184)):.6f}; 625/348 = {float(F(625,348)):.6f}; 1193/664 = {float(F(1193,664)):.6f}; 43/24 = {43/24:.6f}")

print("== Proposition X (side result): E^x(h) ==")
# light-light Young 3/4 - eps/2 ; heavy P1-P1 pair 2/3 + 3 min(e) <= 2/3 + 3 eps
ex = F(1, 12) / (F(1, 2) + 3)
check(ex == F(1, 42), "balance 3/4 - eps/2 = 2/3 + 3 eps at eps = 1/42")
pairmax = F(3, 4) - ex / 2
check(2 * pairmax == F(31, 21) and F(31, 21) < F(34, 23), "E^x(h) = p^{31/21} < p^{34/23} (Round 182)")
dX = F(1, 126)
cases = {
    "LO-LO trivial 3/4 - 3delta/2": F(3, 4) - F(3, 2) * dX,
    "LO x light Young 3/4 - 3delta/4 - eps/4": F(3, 4) - F(3, 4) * dX - ex / 4,
    "P1 structured x LO generic: 2/3 + 19eps/6 - 5delta/6": F(2, 3) + F(19, 6) * ex - F(5, 6) * dX,
    "P2 structured x any: 2/3 + 13eps/6 + 13delta/12": F(2, 3) + F(13, 6) * ex + F(13, 12) * dX,
    "P1 structured x light (layer cake): 2/3 - eps/6 + 19eps/6": F(2, 3) - ex / 6 + F(19, 6) * ex,
    "P2 structured x light: 2/3 - eps/6 + 13eps/6 + 13delta/12": F(2, 3) - ex / 6 + F(13, 6) * ex + F(13, 12) * dX,
    "light below p^-1/4 vs any piece (trivial): 5/8": F(5, 8),
}
for k, v in cases.items():
    check(v <= pairmax, f"  {k} = {v} <= 31/42")
check(F(3, 4) - F(3, 2) * dX == pairmax, "  delta = 1/126 makes LO-LO exactly 31/42")
# SdZ hypothesis for the light layer cake in Lemma M: alpha = G/s <= C p^{3/4}: alpha^{4/3} N^2 <= C p^2
check(F(4, 3) * F(3, 4) + 1 == 2, "light layer cake: Lemma M usable down to s = C' p^{-1/4} (alpha^{4/3} N^2 = c p^2)")

print("== Cap and criteria ==")
check(F(4, 3) == T - F(1, 24), "scheme floor p^{4/3}: all four slots at height 1, Lemma SE N^{8/3} per pair")
check(T - F(5, 8) * F(1, 15) == F(4, 3), "SdZ reaches 4/3 for a pair at height p^{-e} only when e >= 1/15")
check(T - F(1, 4) * F(1, 6) == F(4, 3), "single band line role reaches 4/3 only at e >= 1/6")
# (HC) trivial at the bottom height t = p^{-1/6}: |U|^3 = p^{3/2+3/6} <= p^{4/3 + 4/6}
check(F(3, 2) + 3 * F(1, 6) == F(4, 3) + 4 * F(1, 6), "(HC) E(1-U,1-U') <= p^{4/3}(aa')^{-2} is the trivial bound at a = p^{-1/6}")
check(F(115, 64) - F(1, 24) / 8 == F(43, 24), "cap sup C = p^{4/3} gives covariance p^{43/24}")
# sensitivity: BSG doubling K^c, size loss K^{-sigma}, Lemma S1 K = a^{-kappa}
print("   sensitivity of delta_C to BSG doubling exponent c (size loss K^{-1/2}, K = a^{-2}):")
for c in (F(4), F(3), F(2), F(1)):
    excess = c * 2 / 3 + F(1, 2) * 2 / 2 - F(1, 6)
    Rr = excess / F(5, 8)
    dd = F(1, 24) / (1 + Rr)
    print(f"     c = {c}: pair excess {excess} e, ratio {Rr}, delta_C = {dd} ({float(dd):.6f})")
    if c == 4:
        check(dd == F(5, 696), "  c = 4 reproduces 5/696")

if "--lp" in sys.argv:
    print("== Float LP cross-check (scipy) ==")
    import itertools
    import numpy as np
    from scipy.optimize import linprog
    TH = [5 / 8, 3 / 4, 5 / 8, 3 / 4]

    def solve(types, delta, mixed_on=True, emax=1 / 7):
        nv = 11
        Z, Y, E, M = 0, [1, 2], [3, 4, 5, 6], [7, 8, 9, 10]
        A, b = [], []

        def le(co, const):
            row = np.zeros(nv)
            for k, v in co.items():
                row[k] += v
            A.append(row)
            b.append(const)

        def size(i):
            return ({E[i]: 1.0}, 0.5) if types[i] == 'P1' else ({M[i]: -1.0}, 0.5)
        co = {Z: 1.0}
        for i in range(4):
            if types[i] == 'P1':
                co[E[i]] = co.get(E[i], 0) + (1 - TH[i])
            else:
                co[E[i]] = co.get(E[i], 0) + 1
                co[M[i]] = co.get(M[i], 0) + TH[i]
        le(co, 11 / 8)
        le({Z: 1, Y[0]: -1, Y[1]: -1}, 0)

        def holf(i):
            return ({E[i]: 5 / 3}, 1 / 3) if types[i] == 'P1' else ({E[i]: 2 / 3, M[i]: 1 / 6}, 1 / 3)
        for pi, (i, j) in enumerate([(0, 1), (2, 3)]):
            y = Y[pi]
            ci, ki = holf(i)
            cj, kj = holf(j)
            co = {y: 1.0}
            for dd in (ci, cj):
                for k, v in dd.items():
                    co[k] = co.get(k, 0) - v
            le(co, ki + kj)
            if mixed_on:
                for s, g in [(i, j), (j, i)]:
                    sc, sk = size(g)
                    forms = ([(5 / 6, 1 / 4, {E[s]: 19 / 6}), (2 / 3, 1 / 3, {E[s]: 13 / 3})] if types[s] == 'P1'
                             else [(5 / 6, 1 / 4, {E[s]: 13 / 6, M[s]: 13 / 12}), (2 / 3, 1 / 3, {E[s]: 10 / 3, M[s]: 3 / 2})])
                    for (wa, c0, ex2) in forms:
                        co = {y: 1.0}
                        for k, v in sc.items():
                            co[k] = co.get(k, 0) - wa * v
                        for k, v in ex2.items():
                            co[k] = co.get(k, 0) - v
                        co[E[g]] = co.get(E[g], 0) + 1.0
                        le(co, wa * sk + c0)
        bounds = [(None, None)] * 3 + [(0, emax)] * 4 + [(0, (delta if types[i] == 'P2' else 0)) for i in range(4)]
        c = np.zeros(nv)
        c[Z] = -1
        r = linprog(c, A_ub=np.array(A), b_ub=np.array(b), bounds=bounds, method='highs')
        return -r.fun
    for mixed_on in (False, True):
        worst = max(solve(t, 1 / 87, mixed_on) for t in itertools.product(['P1', 'P2'], repeat=4))
        tag = "with Lemma M" if mixed_on else "Hoelder (a) only"
        print(f"   {tag}: LP max over configurations = 11/8 - {11/8 - worst:.7f}")
        if mixed_on:
            check(abs((11 / 8 - worst) - 5 / 696) < 1e-9, "LP (float) agrees: 11/8 - 5/696")
        else:
            check(abs((11 / 8 - worst) - 1 / 184) < 1e-9, "without Lemma M the per-height split gives 11/8 - 1/184")

    def solveB(delta, emax=1 / 12, mprrs=False):
        """Theorem B: components (e_i, mu_i), -e_i <= mu_i <= delta; Lemma M forms I/II, trivial pair bound."""
        nv = 11
        Z, Y, E, M = 0, [1, 2], [3, 4, 5, 6], [7, 8, 9, 10]
        A, b = [], []

        def le(co, const):
            row = np.zeros(nv)
            for k, v in co.items():
                row[k] += v
            A.append(row)
            b.append(const)
        co = {Z: 1.0}
        for i in range(4):
            co[E[i]] = 1.0
            co[M[i]] = TH[i]
        le(co, 11 / 8)
        le({Z: 1, Y[0]: -1, Y[1]: -1}, 0)
        for i in range(4):
            le({M[i]: -1, E[i]: -1}, 0)
        for pi, (i, j) in enumerate([(0, 1), (2, 3)]):
            y = Y[pi]
            for s, g in [(i, j), (j, i)]:
                le({y: 1, E[s]: -13 / 6, M[s]: -13 / 12, E[g]: 1, M[g]: 5 / 6}, 2 / 3)
                le({y: 1, E[s]: -10 / 3, M[s]: -3 / 2, E[g]: 1, M[g]: 2 / 3}, 2 / 3)
                if mprrs:
                    le({y: 1, M[g]: 3 / 4, E[s]: -23 / 2, M[s]: -23 / 4, E[g]: 1}, 5 / 8)
            for mn in (i, j):
                co = {y: 1, E[i]: 1, E[j]: 1}
                for k in (i, j, mn):
                    co[M[k]] = co.get(M[k], 0) + 0.5
                le(co, 0.75)
        bounds = [(None, None)] * 3 + [(0, emax)] * 4 + [(None, delta)] * 4
        c = np.zeros(nv)
        c[Z] = -1
        r = linprog(c, A_ub=np.array(A), b_ub=np.array(b), bounds=bounds, method='highs')
        return -r.fun
    vB = solveB(1 / 37)
    print(f"   Theorem B LP (heights <= 1/12): 11/8 - {11/8 - vB:.7f}")
    check(abs((11 / 8 - vB) - 5 / 296) < 1e-9, "LP (float) agrees with Theorem B: 11/8 - 5/296")
    vBm = solveB(1 / 37, mprrs=True)
    print(f"   Theorem B LP + MPRRS Lemma 33 everywhere (optimistic): 11/8 - {11/8 - vBm:.7f}")
    check(abs((11 / 8 - vBm) - 5 / 296) < 1e-9, "adding MPRRS Lemma 33 does not move delta_C")

print("ALL OK" if ok else "SOME CHECK FAILED")
