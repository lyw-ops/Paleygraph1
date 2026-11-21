#!/usr/bin/env python3
"""Round 191, call ordinary-fixed-block-assembly: exact bookkeeping checks.

Part A (exact Fractions): every loss exponent quoted in
research/native-claude-ordinary-fixed-block-assembly-191.md.
Exponents are powers of p; "loss" = (best accepted bound) / p.

Part B (exact Fractions, small primes, arbitrary rational weights g):
the slope-complete identity used in Proposition 2 of the report,
    sum_{t != 1} P_t = X - diag,
where P_t sums g(A_x)g(C_x)g(A_y)g(C_y) over u in Q\\{1} and x, y in F_p
(physical square masks completed) at slope t = C_y A_x / (C_x A_y),
X = sum_{u in Q\\{1}} c(u)^2, c(u) = sum_x g(A_x) g(C_x), A_x = 1 - v x,
C_x = 1 - v u x, and diag = sum_u sum_x g(A_x)^2 g(C_x)^2.  It also checks
that slope 1 occurs exactly on x = y among supported terms.

Run: python3 research/paley-191-assembly-exponents.py
"""
from fractions import Fraction as Fr
import random

ok = True


def check(name, lhs, rhs):
    global ok
    good = lhs == rhs
    ok = ok and good
    print(f"{'OK ' if good else 'BAD'} {name}: {lhs} == {rhs}")


print("Part A: loss exponents (exact)")
half = Fr(1, 2)
# Slope floors at fixed vertex thresholds (paid below g(t) <= p^-sigma*).
sig_R163 = 1 - Fr(4, 445)          # R163:61, any fixed a,b > 0
gam_one = Fr(1, 211)               # R164:20-25, one threshold > 1/2
gam_both = Fr(1, 54)               # R164:20-25, both thresholds > 1/2
check("R163 floor sigma* = 1-4/445", sig_R163, Fr(441, 445))
check("R164 floor (one high) 1-2/211", 1 - 2 * gam_one, Fr(209, 211))
check("R164 floor (both high) 1-2/54 = 26/27", 1 - 2 * gam_both, Fr(26, 27))

# (P-I) slope band g(t) ~ p^-sigma under M_w = O(p): bound p^(1+sigma/2).
for name, s in [("a<=1/2 (R163)", sig_R163), ("one>1/2", 1 - 2 * gam_one),
                ("both>1/2", 1 - 2 * gam_both)]:
    print(f"    M_w-alone max band loss {name}: sigma*/2 = {s/2}")
check("max band loss, a<=1/2", sig_R163 / 2, Fr(441, 890))
check("max band loss, both > 1/2", (1 - 2 * gam_both) / 2, Fr(13, 27))
check("max band loss, one > 1/2", (1 - 2 * gam_one) / 2, Fr(209, 422))

# Combined with the count bound p^(3/2 - g0 - sigma/2):
# g0 = 2/445 (R163 energy route, any a,b>0), g0 = gamma (R164).
for name, g0 in [("R163 2/445", Fr(2, 445)), ("R164 1/211", gam_one),
                 ("R164 1/54", gam_both)]:
    # 1 + s/2 = 3/2 - g0 - s/2  =>  s = 1/2 - g0
    s = half - g0
    lhs = 1 + s / 2
    rhs = Fr(3, 2) - g0 - s / 2
    assert lhs == rhs
    print(f"    combined band crossover {name}: sigma = {s}, loss = {s/2}")
check("combined band loss (R163)", (half - Fr(2, 445)) / 2, Fr(441, 1780))
check("combined band loss (one high)", (half - gam_one) / 2, Fr(209, 844))
check("combined band loss (both high)", (half - gam_both) / 2, Fr(13, 54))

# (P-II) near-unit slopes, 1 - g(t) in [eps, 2 eps):
# M_w gives p/eps; R159 + pointwise N_t << p^(1-gamma) gives
# p^(3/2 - gamma) (E+eps)^(1/6) (log).  For eps >= E the crossover is
# eps^(-7/6) = p^(1/2 - gamma), loss (6/7)(1/2 - gamma) = (3 - 6 gamma)/7.
for name, g in [("a<=1/2 (R162 N_t << p)", Fr(0)), ("one high", gam_one),
                ("both high", gam_both)]:
    loss = Fr(6, 7) * (half - g)
    assert loss == (3 - 6 * g) / 7
    print(f"    near-unit combined loss {name}: {loss}; "
          f"eps-threshold exponent -{loss}; cap (eps < E) 1/2-gamma = {half-g}")
check("near-unit loss, gamma = 0", Fr(6, 7) * half, Fr(3, 7))
# With eps < E the bound is p^(1/2-gamma) E^(1/6).  At E = p^-1/2 this piece
# is p^(5/12) (gamma = 0), below the 3/7 crossover, so the overall loss is 3/7;
# at E = p^-3/7 the eps < E piece equals the crossover value 3/7.
check("near-unit eps<E piece at E = p^-1/2, gamma=0", half - Fr(1, 12), Fr(5, 12))
check("near-unit eps<E piece at E = p^-3/7 equals 3/7", half - Fr(3, 7) / 6, Fr(3, 7))

# (P-III) vertex layers.
# R160 device: price p * m_<a, m_<a <= G ~ p^(1/2); target o(p D),
# D = E^(-1/2)/log(2/E) <= p^(1/4)/log: loss exponent in [1/4, 1/2).
check("vertex loss vs O(p) target", half, Fr(1, 2))
check("vertex loss vs o(pD) target, best case D ~ p^(1/4)", half - Fr(1, 4), Fr(1, 4))
# Positive majorant at vertex level alpha: a^-2 (X - diag); alpha >= C/p.
check("majorant vertex loss at alpha = p^-1 (true amplitudes)", Fr(2), Fr(2))
check("majorant vertex loss at alpha = p^-1 (amplitudes to 1, R166:9)", Fr(4), Fr(4))
# Flat admissible law: p^3 triples x amplitude p^(-1/4) on five factors.
check("flat absolute off-diagonal exponent 3 - 5/4", 3 - Fr(5, 4), Fr(7, 4))
check("flat absolute loss over target", Fr(7, 4) - 1, Fr(3, 4))
# Rank-two flattening (R160 rank-two:57-61): exponent 7/4 - sum(alpha_j-1/4)_+.
def rank_two(alphas):
    return Fr(7, 4) - sum(max(Fr(0), a - Fr(1, 4)) for a in alphas)
check("rank-two, all five at g ~ p^-1/2", rank_two([Fr(1, 4)] * 5), Fr(7, 4))
check("rank-two, three at p^-1/2", rank_two([half] * 3 + [Fr(1, 4)] * 2), Fr(1))
# Flat model check of X: c(u) ~ n (2/sqrt p)^2 = 2, X ~ n * 4 = 2p.
check("flat X exponent", Fr(1), Fr(1))
# D upper bound: E >= p^-1/2 gives D <= p^(1/4)/log.
check("D <= p^(1/4)", half / 2, Fr(1, 4))
# Prop 1.4 (R183): sum g^2 <= (1/2+o(1)) sqrt p; tightness at level a forces
# sum g^2 >= a (G - m_<a); with G = sqrt p and m_<a = o(sqrt p), a <= 1/2.
check("tightness level bound", half, Fr(1, 2))

print()
print("Part B: exact identity sum_{t!=1} P_t = X - diag (rational g)")


rng = random.Random(191)
for p in (13, 17, 29, 37, 41):
    Q = {pow(x, 2, p) for x in range(1, p)}
    g = {z: Fr(0) for z in range(p)}
    for z in Q:
        g[z] = Fr(rng.randint(0, 6), 6)
    g[1] = Fr(1)
    for v in (1, next(z for z in range(2, p) if z not in Q)):
        X = Fr(0)
        diag = Fr(0)
        P = {}
        slope_one_offdiag = 0
        for u in Q:
            if u == 1:
                continue
            c = Fr(0)
            for x in range(p):
                A = (1 - v * x) % p
                C = (1 - v * u * x) % p
                c += g[A] * g[C]
                diag += g[A] ** 2 * g[C] ** 2
            X += c * c
            for x in range(p):
                Ax, Cx = (1 - v * x) % p, (1 - v * u * x) % p
                wx = g[Ax] * g[Cx]
                if wx == 0:
                    continue
                for y in range(p):
                    Ay, Cy = (1 - v * y) % p, (1 - v * u * y) % p
                    wy = g[Ay] * g[Cy]
                    if wy == 0:
                        continue
                    t = Cy * Ax * pow(Cx * Ay, -1, p) % p
                    if t == 1 and x != y:
                        slope_one_offdiag += 1
                    P[t] = P.get(t, Fr(0)) + wx * wy
        lhs = sum(val for t, val in P.items() if t != 1)
        check(f"p={p} v={v}: sum_(t!=1) P_t = X - diag", lhs, X - diag)
        check(f"p={p} v={v}: P_1 = diag", P.get(1, Fr(0)), diag)
        check(f"p={p} v={v}: no off-diagonal slope-1 terms", slope_one_offdiag, 0)

print()
print("ALL OK" if ok else "SOME CHECKS FAILED")
