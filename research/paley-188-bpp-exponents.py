#!/usr/bin/env python3
"""Round 188 (ordinary-prime-beyond-point-plane): exact exponent bookkeeping.

All arithmetic uses fractions.Fraction.  Exponents are powers of p, with
G ~ p^(1/2), M_1 ~ p (the near-critical normalisation; upper bounds hold with
G <= C sqrt p, M_1 <= G^2 in general), Gamma_tot = sum_x g(x)^2 = p^gamma,
X = E_Q(h) = p^eX, E(mu) = p^eE.  Logarithms are dropped (p^{o(1)}).

Routes (covariance = (1/p) * sum_{s,t} w |H|^2, plus the paid p^{3/2}):
  RS  (Round 178 Rudnev-Shkredov second norm):  9/8 + eE/4
  OP  (Round 182 Prop. 5 + Plancherel, ||pi||^4 <= pE): gamma + eE/2
  CH  (this report, Theorem A):                  gamma + eX
each maxed with 3/2.
"""
from fractions import Fraction as F


def mx(*a):
    return max(a)


def rs(eE):
    return mx(F(3, 2), F(9, 8) + eE / 4)


def op(gamma, eE):
    return mx(F(3, 2), gamma + eE / 2)


def ch(gamma, eX):
    return mx(F(3, 2), gamma + eX)


def main():
    ok = True

    def check(name, got, want):
        nonlocal ok
        flag = (got == want)
        ok &= flag
        print(f"{'OK ' if flag else 'BAD'} {name}: {got} (expected {want})")

    half = F(1, 2)
    # accepted inputs (Round 187): E(mu) << p^(8/3), X, E^x(h) << p^(4/3)
    eE187, eX187 = F(8, 3), F(4, 3)
    check("RS with R187 E(mu)", rs(eE187), F(43, 24))
    check("43/24 = 115/64 - 1/192", F(115, 64) - F(1, 192), F(43, 24))
    check("OP with R187 E(mu), gamma=1/2", op(half, eE187), F(11, 6))
    check("CH with R187 X, gamma=1/2", ch(half, eX187), F(11, 6))
    # Proposition B: E(mu) <= c M_1^2 <= Gamma_2^2 M_1^2  -> eE <= 2 gamma + 2
    check("OP with Prop. B at gamma", op(F(1, 4), 2 * F(1, 4) + 2), F(3, 2))
    # floors of each route (method statements)
    check("RS floor at E = M_1^4/p^2 (eE=2)", rs(F(2)), F(13, 8))
    check("RS floor at point-plane eE=5/2", rs(F(5, 2)), F(7, 4))
    check("OP at eE=5/2, gamma=1/2", op(half, F(5, 2)), F(7, 4))
    check("OP at eE=2 (CS floor), gamma=1/2", op(half, F(2)), F(3, 2))
    check("CH at X floor eX=1, gamma=1/2", ch(half, F(1)), F(3, 2))
    # thresholds in eX for CH at gamma = 1/2
    check("CH < 7/4 iff eX < 5/4", ch(half, F(5, 4)), F(7, 4))
    check("CH < 43/24 iff eX < 31/24", ch(half, F(31, 24)), F(43, 24))
    # crossover with Round 184 Prop 1(ii): max W <= X = p^(1+eps) gives 7/4 + eps/8
    eps = F(2, 7)
    check("crossover CH (3/2+eps) = R184 (7/4+eps/8) at eps=2/7",
          F(3, 2) + eps, F(7, 4) + eps / 8)
    # thresholds in gamma (Gamma_tot = p^gamma), using min(OP via Prop B, OP/CH via R187)
    def best(gamma):
        return min(op(gamma, 2 * gamma + 2), op(gamma, eE187), ch(gamma, eX187), rs(eE187))
    check("gamma=1/4 gives target", best(F(1, 4)), F(3, 2))
    check("gamma=3/8: min(1+2gamma, gamma+4/3)", best(F(3, 8)), F(41, 24))
    check("gamma=1/3: both branches equal 5/3", best(F(1, 3)), F(5, 3))
    check("gamma=5/12: gamma+4/3 = 7/4", best(F(5, 12)), F(7, 4))
    check("gamma=11/24: gamma+4/3 = 43/24", best(F(11, 24)), F(43, 24))
    check("gamma=1/2 (worst): 43/24", best(half), F(43, 24))
    # Round 184 Corollary Y comparison: 7/4 + gamma/8 for gamma < 3/8
    g = F(1, 3)
    print("compare at gamma=1/3: new", best(g), " Round 184 Cor. Y", F(7, 4) + g / 8)
    ok &= best(g) < F(7, 4) + g / 8
    # translation fibre: E_1 <= c X <= (p/4) p^(4/3): OP contribution at gamma=1/2
    check("translation fibre E_1 <= cX: OP exponent", op(half, 1 + eX187), F(5, 3))
    # Theorem A with first-mass target X = p^(1+1/1280)
    check("CH at X target 1+1/1280", ch(half, 1 + F(1, 1280)), F(3, 2) + F(1, 1280))
    # dilation-fibre requirement for < 7/4 through OP at gamma=1/2: E_{!=1} < p^(5/2)
    check("sup D(lambda) <= p^(1/2-d) => E_!=1 <= p^(5/2-d): OP", op(half, F(5, 2) - F(1, 10)),
          F(7, 4) - F(1, 20))
    print("ALL OK" if ok else "SOME CHECK FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
