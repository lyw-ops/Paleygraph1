#!/usr/bin/env python3
r"""Round 187, call ordinary-prime-level-pair-energy: exact exponent ledger.

Exact rational arithmetic (fractions.Fraction), standard library only.  Optional float LP
cross-check with --lp (numpy + scipy).

Checks the exponent algebra of research/native-claude-ordinary-prime-level-pair-energy-187.md :

  * Lemma M' per-piece bound -> per-component pair price, for its three terms
      T1  (form I)  alpha^{4/3}|B|^{2/3}K^{2/3}m^{1/3}alpha^{1/3}
      T2            K alpha |B|
      T3            alpha |B| (alpha K m alpha)^{1/2} p^{-1/2}
    summed over the pieces of one phase component (sum |B|^{1/3}, sum |B|^{1/2} via min|B|),
    with the heights a_s a_g, as linear forms in (e_s, mu_s, e_g, mu_g);
  * the three excess identities over 2/3 and their nonpositivity whenever
    u_s <= u_g, mu_i >= -e_i, e_s <= 1/6   (exact, by nonnegative-coefficient rewriting
    and by exact vertex enumeration of the polytope);
  * the light part (Young) at tau0 = p^{-1/6};
  * the corollaries: E^x(h), sup C, X, sum W^{3/2}, E(mu), one-match covariance;
  * comparison with Round 186 (Theorem B, Prop. X) and the BSG-shape ceiling.

Every exponent is "exponent of p".  Linear forms are dicts {var: Fraction}, key 1 = constant.
Prints ALL OK at the end if every assertion holds.
"""
import itertools
import random
import sys
from fractions import Fraction as F

ok = True


def check(cond, msg):
    global ok
    print(("ok   " if cond else "FAIL ") + msg)
    ok = ok and bool(cond)


def L(*pairs, c=0):
    d = {1: F(c)}
    for k, v in pairs:
        d[k] = d.get(k, F(0)) + F(v)
    return d


def add(*forms):
    out = {}
    for f in forms:
        for k, v in f.items():
            out[k] = out.get(k, F(0)) + F(v)
    return {k: v for k, v in out.items() if v != 0 or k == 1}


def scale(s, f):
    return {k: F(s) * v for k, v in f.items()}


def sub(f, g):
    return add(f, scale(-1, g))


def same(f, g):
    d = sub(f, g)
    return all(v == 0 for v in d.values())


def show(f):
    parts = [str(f.get(1, F(0)))]
    for k, v in sorted(((k, v) for k, v in f.items() if k != 1), key=lambda kv: str(kv[0])):
        parts.append(f"{'+' if v >= 0 else '-'} {abs(v)}*{k}")
    return " ".join(parts)


def ev(f, val):
    return sum(v * (val[k] if k != 1 else 1) for k, v in f.items())


half = F(1, 2)
TWO3 = F(2, 3)

# ------------------------------------------------------------------ building blocks
# structured component s: height a_s = p^{-e_s}; remainders m in [M, 2M), M = p^{1/2 - mu_s};
# K <= p^{2 e_s + mu_s} = p^{u_s};  pieces |B| >= M / (4 L0 sqrt K);  sum |B| <= 2M.
# partner g: |X_g| <= 2 p^{1/2 - mu_g} (alpha), height a_g = p^{-e_g}.
es, ms, eg, mg = "e_s", "mu_s", "e_g", "mu_g"
logM = L((ms, -1), c=half)
logK = L((es, 2), (ms, 1))
u_s = logK
u_g = L((eg, 2), (mg, 1))
logalpha = L((mg, -1), c=half)
logminB = sub(logM, scale(half, logK))
heights = L((es, -1), (eg, -1))

print("== Lemma M' terms summed over the pieces of a component ==")
# T1 per piece: E^{1/2} <= alpha^{5/6} |B|^{1/3} K^{1/3} m^{1/6}; sum |B|^{1/3} <= 2M (min|B|)^{-2/3}
sum_B13 = add(logM, scale(F(-2, 3), logminB))
T1 = add(heights, scale(F(5, 6), logalpha), scale(F(1, 3), logK), scale(F(1, 6), logM), sum_B13)
# T1 form II: min <= 4 L0^2 K m :  E^{1/2} <= alpha^{2/3}|B|^{1/3} K^{1/2} m^{1/3}
T1b = add(heights, scale(F(2, 3), logalpha), scale(F(1, 2), logK), scale(F(1, 3), logM), sum_B13)
# T2 per piece: (K alpha |B|)^{1/2}; sum |B|^{1/2} <= 2M (min|B|)^{-1/2}
sum_B12 = add(logM, scale(F(-1, 2), logminB))
T2 = add(heights, scale(half, logK), scale(half, logalpha), sum_B12)
# T3 per piece: alpha |B|^{1/2} (K m)^{1/4} p^{-1/4}
T3 = add(heights, logalpha, sum_B12, scale(F(1, 4), logK), scale(F(1, 4), logM), L(c=F(-1, 4)))

for name, T in (("T1 (form I)", T1), ("T1 (form II)", T1b), ("T2", T2), ("T3", T3)):
    print(f"   {name}: pair exponent = {show(T)}")

ex1 = sub(T1, L(c=TWO3))
ex2 = sub(T2, L(c=TWO3))
ex3 = sub(T3, L(c=TWO3))
# claimed identities
check(same(ex1, add(scale(F(1, 6), sub(u_s, u_g)), scale(F(-2, 3), L((eg, 1), (mg, 1))))),
      "T1 excess = (u_s - u_g)/6 - (2/3)(e_g + mu_g)")
check(same(ex1, add(scale(F(1, 6), u_s), scale(-1, L((eg, 1), (mg, F(5, 6)))))),
      "T1 excess = u_s/6 - (e_g + 5 mu_g/6)")
check(same(ex2, add(L(c=F(-1, 6)), scale(F(1, 4), u_s), scale(F(-1, 2), u_g))),
      "T2 excess = -1/6 + u_s/4 - u_g/2")
check(same(ex3, L((eg, -1), (mg, -1), (ms, F(-1, 4)), c=F(-1, 24))),
      "T3 excess = -1/24 - (e_g + mu_g) - mu_s/4")

# nonnegative rewriting: d = u_g - u_s >= 0, w_i = e_i + mu_i >= 0, z = 1/6 - e_s >= 0
# substitute mu_i = w_i - e_i, e_g from d:  u_g = 2 e_g + mu_g = e_g + w_g, u_s = e_s + w_s
# so e_g = d + e_s + w_s - w_g, and e_s = 1/6 - z.
def rewrite(f):
    # variables -> (d, w_s, w_g, z)
    out = {1: F(0), "d": F(0), "w_s": F(0), "w_g": F(0), "z": F(0)}
    c = f.get(1, F(0))
    a_es = f.get(es, F(0)); a_ms = f.get(ms, F(0)); a_eg = f.get(eg, F(0)); a_mg = f.get(mg, F(0))
    # mu_s = w_s - e_s ; mu_g = w_g - e_g
    a_es2 = a_es - a_ms; a_ws = a_ms
    a_eg2 = a_eg - a_mg; a_wg = a_mg
    # e_g = d + e_s + w_s - w_g
    a_d = a_eg2; a_es2 += a_eg2; a_ws += a_eg2; a_wg -= a_eg2
    # e_s = 1/6 - z
    c += a_es2 * F(1, 6); a_z = -a_es2
    out[1] = c; out["d"] = a_d; out["w_s"] = a_ws; out["w_g"] = a_wg; out["z"] = a_z
    return out


for name, ex in (("T1", ex1), ("T2", ex2), ("T3", ex3)):
    r = rewrite(ex)
    # d, w_s, w_g >= 0 unbounded above; 0 <= z <= 1/6
    worst = r[1] + max(F(0), r["z"]) * F(1, 6)
    nonpos = worst <= 0 and all(r[k] <= 0 for k in ("d", "w_s", "w_g"))
    check(nonpos, f"{name} excess = {show(r)}  (<= {worst} for d,w_s,w_g >= 0, 0 <= z <= 1/6)")

print("== exact vertex enumeration of the excess polytope ==")
# variables x = (e_s, mu_s, e_g, mu_g); constraints A x <= b
VARS = (es, ms, eg, mg)
cons = []  # (coeff dict, rhs): sum coeff*x <= rhs
cons.append(({es: -1}, F(0)))            # e_s >= 0
cons.append(({eg: -1}, F(0)))            # e_g >= 0
cons.append(({es: 1}, F(1, 6)))          # e_s <= 1/6 (heights >= p^{-1/6})
cons.append(({eg: 1}, F(1, 6)))          # e_g <= 1/6
cons.append(({es: -1, ms: -1}, F(0)))    # mu_s >= -e_s
cons.append(({eg: -1, mg: -1}, F(0)))    # mu_g >= -e_g
cons.append(({ms: 1}, half))             # M >= 1
cons.append(({mg: 1}, half))
cons.append(({es: 2, ms: 1, eg: -2, mg: -1}, F(0)))   # u_s <= u_g


def solve(rows, rhs):
    n = len(rows)
    Mx = [list(r) + [b] for r, b in zip(rows, rhs)]
    for c in range(n):
        piv = next((i for i in range(c, n) if Mx[i][c] != 0), None)
        if piv is None:
            return None
        Mx[c], Mx[piv] = Mx[piv], Mx[c]
        for i in range(n):
            if i != c and Mx[i][c] != 0:
                fct = Mx[i][c] / Mx[c][c]
                Mx[i] = [a - fct * b for a, b in zip(Mx[i], Mx[c])]
    return [Mx[i][n] / Mx[i][i] for i in range(n)]


verts = []
for combo in itertools.combinations(range(len(cons)), 4):
    rows = [[F(cons[i][0].get(v, 0)) for v in VARS] for i in combo]
    rhs = [cons[i][1] for i in combo]
    x = solve(rows, rhs)
    if x is None:
        continue
    val = dict(zip(VARS, x))
    if all(sum(F(c) * val[k] for k, c in cd.items()) <= b for cd, b in cons):
        verts.append(val)
check(len(verts) > 0, f"polytope has {len(verts)} vertices (with repetition)")
for name, ex in (("T1", ex1), ("T1 form II", sub(T1b, L(c=TWO3))), ("T2", ex2), ("T3", ex3)):
    mx = max(ev(ex, v) for v in verts)
    arg = max(verts, key=lambda v: ev(ex, v))
    print(f"   max {name} excess over the polytope = {mx} at {dict((k, str(x)) for k, x in arg.items())}")
    if name != "T1 form II":
        check(mx <= 0, f"{name} excess <= 0 on the whole polytope")
print("   (form II is not needed; its maximum is reported only.)")

print("== whole level sets: Lemma M' T1 is exactly the (HC') price at u_s = u_g ==")
for e in (F(0), F(1, 74), F(1, 37), F(1, 15), F(1, 12), F(1, 10), F(1, 6)):
    val = {es: e, ms: -e, eg: e, mg: -e}
    check(ev(ex1, val) == 0 and ev(ex2, val) < 0 and ev(ex3, val) <= 0,
          f"e = {e}: T1,T2,T3 excess = {ev(ex1, val)}, {ev(ex2, val)}, {ev(ex3, val)}")

print("== comparison with Round 186 Prop. P (Reiher-Schoen) ==")
# Round 186 form I pair exponent: 2/3 + 13/6 e_s + 13/12 mu_s - e_g - 5/6 mu_g
R186 = L((es, F(13, 6)), (ms, F(13, 12)), (eg, -1), (mg, F(-5, 6)), c=TWO3)
diff = sub(R186, T1)
check(same(diff, scale(F(11, 12), u_s)), f"R186 minus Lemma M' (T1) = (11/12) u_s : {show(diff)}")

print("== chunked Stevens-de Zeeuw: the middle term s b^{1/2} n p^{-1/2} ==")
# chunks of n0 = c0 p^2 / s lines: sum over n/n0 + 1 chunks of s^{3/4} b^{1/2} n_j^{3/4}
# <= s^{3/4} b^{1/2} n^{3/4} (n/n0 + 1)^{1/4} <= s^{3/4}b^{1/2}n^{3/4} + s^{3/4} b^{1/2} n n0^{-1/4}
s_, b_, n_ = "s", "b", "n"
mid = add(L((s_, F(3, 4)), (b_, F(1, 2)), (n_, 1)), scale(F(-1, 4), L((s_, -1), c=2)))
check(same(mid, L((s_, 1), (b_, half), (n_, 1), c=F(-1, 2))), "s^{3/4} b^{1/2} n (p^2/s)^{-1/4} = s b^{1/2} n p^{-1/2}")

print("== light part and the energy of h ==")
G = half                     # G <= C sqrt p
tau0 = F(-1, 6)              # tau0 = c p^{-1/6}
young_LL = 2 * G + (tau0 + G)          # ||h_<||_1^2 ||h_<||_2^2
young_LH = (tau0 + G) / 2 + G          # ||h_<||_2 ||h_>=||_1
check(young_LL == F(4, 3), f"light-light Young: E <= G^2 tau0 G = p^{young_LL}")
check(young_LH == TWO3, f"light-heavy Young: ||c|| <= ||h_<||_2 ||h_>=||_1 = p^{young_LH}")
Eh = F(4, 3)
check(Eh == 2 * TWO3, "E^x(h) << p^{4/3} (log p)^{32/3}")

print("== corollaries ==")
T = F(11, 8)
supC = Eh
check(supC == T - F(1, 24), f"sup C exponent 4/3 = 11/8 - 1/24 (delta_C = 1/24, scheme floor)")
X31 = F(31, 21)
check(Eh < X31 and Eh < F(34, 23), f"X <= E^x(h): 4/3 < 31/21 (Round 186 Prop. X) < 34/23")
EXm = max(2 * Eh, supC + 2)           # E^x(m) <= X^2 + sup C M_1^2, M_1 <= G^2
check(EXm == F(10, 3), f"E^x(m) exponent {EXm}")
W32 = 1 + EXm / 2
check(W32 == F(8, 3) and W32 == F(43, 16) - F(1, 48), f"sum W^(3/2), E(mu): {W32} = 43/16 - 1/48")
# E(mu) << sum (W^2/p + W^{3/2} + G log p W):  W^2/p -> EXm - 1 ; G W -> 1/2 + 2
check(max(EXm - 1, W32, half + 2) == W32, "R178: E(mu) dominated by sum W^(3/2)")
cov = F(9, 8) + W32 / 4
check(cov == F(43, 24) and cov == F(115, 64) - F(1, 192), f"one-match covariance {cov} = 115/64 - 1/192")
old = F(2125, 1184)
check(cov < old, f"43/24 = {float(cov):.6f} < 2125/1184 = {float(old):.6f}")
check(F(115, 64) - cov == F(1, 192) and F(115, 64) - old == F(5, 2368), "gains over 115/64: 1/192 vs 5/2368")
# mission formula delta_C(kappa) = (1/24)/(1 + 8 kappa/5): kappa = 0 gives the floor
dC = lambda k: F(1, 24) / (1 + F(8, 5) * k)
check(dC(F(0)) == F(1, 24) and dC(F(11, 12)) == F(5, 296), "delta_C(0) = 1/24, delta_C(11/12) = 5/296")
check(F(1, 24) > F(2386, 100000), "1/24 exceeds the Reiher-Schoen-shape BSG ceiling ~0.02386")

print("== random rational spot checks of the excess bounds ==")
rng = random.Random(187)
for _ in range(20000):
    e1 = F(rng.randint(0, 600), 3600); e2 = F(rng.randint(0, 600), 3600)
    m1 = F(rng.randint(-int(e1 * 3600), 1800), 3600); m2 = F(rng.randint(-int(e2 * 3600), 1800), 3600)
    val = {es: e1, ms: m1, eg: e2, mg: m2}
    if ev(u_s, val) > ev(u_g, val):
        val = {es: e2, ms: m2, eg: e1, mg: m1}
    if max(ev(ex1, val), ev(ex2, val), ev(ex3, val)) > 0:
        check(False, f"positive excess at {val}")
        break
else:
    check(True, "20000 random admissible points: max(T1,T2,T3) <= 2/3 with s = argmin u")

if "--lp" in sys.argv:
    print("== float LP cross-check (scipy) ==")
    import numpy as np
    from scipy.optimize import linprog
    A = np.array([[float(cd.get(v, 0)) for v in VARS] for cd, b in cons])
    bb = np.array([float(b) for cd, b in cons])
    for name, ex in (("T1", ex1), ("T2", ex2), ("T3", ex3)):
        c = -np.array([float(ex.get(v, 0)) for v in VARS])
        res = linprog(c, A_ub=A, b_ub=bb, bounds=[(None, None)] * 4)
        mx = -res.fun + float(ex.get(1, 0))
        print(f"   LP max {name} excess = {mx:.12f}")
        check(mx <= 1e-12, f"LP: {name} excess <= 0")

print("ALL OK" if ok else "SOME CHECKS FAILED")
sys.exit(0 if ok else 1)
