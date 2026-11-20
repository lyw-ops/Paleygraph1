"""Round 182 (call ordinary-prime-shifted-level-energy): exact exponent ledger.

All arithmetic is with Fractions.  It checks the exponent bookkeeping of the
report's Proposition 3 (layer-cake BSG extraction) for a per-piece lemma of the
form
    E^x(1-B)^(1/4) <= C K_j^c |B|^(beta/4)   (B a BSG piece of a level set,
                                              K_j the BSG energy parameter),
with BSG size |B| >> m K_j^(-1/2), K_j << Q0/m, Q0 = p^(1/2) t^(-2) at level t.
Writing a = c + (1 - beta/4)/2 (price per point Q0^a m^(beta/4 - 1 - a)):
  phase 1 (m = sqrt p) at level t : p^(beta/8) t^(-1-2a)
  layer cake over t in [tau,1]    : p^(beta/8 + 2 a eps)          (tau = p^-eps)
  light part (Young)              : fourth-root exponent 3/8 - eps/4
  leftover (size p^(1/2-delta))   : fourth-root exponent 3/8 - 3 delta/4
  phase 2                          : p^(beta/8) t^(-2a) p^(delta max(0, a-beta/4))
The optimum eps solves beta/8 + 2 a eps = 3/8 - eps/4, and E^x(h) = O(p^(3/2-eps)).

Rows: Round 177 lemma (36/13, K^(16/13) in quotient constant), Lemma SE of this
report (8/3, K^(2/3)), and two hypothetical lemmas showing the cap of the route.
Also checks: 8/3 < 36/13, 52/35 and 34/23 values, the trivial-frequency
exponent 1/2 + (3/2 - eps) - 1, and the dyadic algebra of Lemma SE.

Replay: python3 -B research/paley-182-shifted-energy-exponents.py
"""
from fractions import Fraction as F


def route(beta4, c, delta_mode="balance"):
    """beta4 = beta/4, c = K_j exponent in E^(1/4). Returns (a, eps, delta, Eexp)."""
    a = c + (1 - beta4) / 2
    beta8 = beta4 / 2
    eps = (F(3, 8) - beta8) / (2 * a + F(1, 4))
    delta = eps / 3  # leftover equals light part: 3/8 - 3 delta/4 = 3/8 - eps/4
    lead = beta8 + 2 * a * eps
    assert lead == F(3, 8) - eps / 4 == F(3, 8) - 3 * delta / 4
    # phase 2 fourth-root exponent
    extra = delta * max(F(0), a - beta4)
    if 2 * a > 1:
        ph2 = beta8 + (2 * a - 1) * eps + extra
    else:
        ph2 = beta8 + extra
    assert ph2 <= lead, (ph2, lead)
    return a, eps, delta, 4 * lead


def main():
    # Round 177 lemma: E <= (K')^(16/13) N^(36/13), K' <= K_j^4  -> E^(1/4) <= K_j^(16/13) N^(9/13)
    rows = [
        ("Round 177 lemma, single level (as in R177)", None, None),
        ("Round 177 lemma + layer cake", F(9, 13), F(16, 13)),
        ("Lemma SE (8/3) + layer cake", F(2, 3), F(2, 3)),
        ("hypothetical sharp lemma N^2, K-free", F(1, 2), F(0)),
        ("hypothetical: no BSG loss (a=0), beta=2", None, "a0"),
    ]
    # single-level Round 177 accounting (as published): structured exponent
    # 18/13 + (4/13) max(49 eps, 36 eps + 9 delta); light 3/2 - eps; leftover 3/2 - 3 delta
    eps, delta = F(3, 418), F(1, 418)
    s177 = F(18, 13) + F(4, 13) * max(49 * eps, 36 * eps + 9 * delta)
    assert s177 == F(3, 2) - F(3, 418) == F(3, 2) - eps == F(3, 2) - 3 * delta
    print(f"{rows[0][0]:45s}: E^x(h) = O(p^({s177})) = p^(3/2 - 3/418)")
    # single-level with Lemma SE: 4/3 + 4 max(8 eps/3, 5 eps/3 + delta/6), balanced
    eps, delta = F(1, 70), F(1, 210)
    s_se = F(4, 3) + 4 * max(F(8, 3) * eps, F(5, 3) * eps + delta / 6)
    assert s_se == F(3, 2) - eps == F(3, 2) - 3 * delta == F(52, 35)
    print(f"{'Lemma SE, single level':45s}: E^x(h) = O(p^({s_se})) = p^(3/2 - 1/70)")
    for name, beta4, c in rows[1:4]:
        a, eps, delta, Eexp = route(beta4, c)
        print(f"{name:45s}: a={a}, eps={eps}, delta={delta}, E^x(h)=O(p^({Eexp}))"
              f" = p^(3/2 - {F(3, 2) - Eexp})")
    # no BSG loss: per level E(1-S_t)^(1/4) <= |S_t|^(1/2) with |S_t| <= sqrt(p)/t:
    # integral over t >= tau of p^(1/4) t^(-1/2) is O(p^(1/4)); light part 3/8 - eps/4
    # with tau = p^(-1/2) gives 1/4: E^x(h) = O(p) (log factors aside)
    print(f"{rows[4][0]:45s}: E^x(h) = O(p^(1)) up to logs (the conditional route)")
    # comparisons
    assert F(8, 3) < F(36, 13)
    a, eps, delta, Eexp = route(F(2, 3), F(2, 3))
    assert Eexp == F(34, 23) == F(3, 2) - F(1, 46)
    triv = F(1, 2) + Eexp - 1
    assert triv == F(45, 46)
    print(f"trivial multiplicative frequency of w: O(p^({triv}))  [Round 181 claimed 1-3/418]")
    assert F(34, 23) > F(11, 8)
    _, _, _, cap = route(F(1, 2), F(0))
    assert cap == F(4, 3) and cap < F(11, 8)
    print(f"route cap with a sharp K-free lemma: p^({cap}) < p^(11/8); target p^(1+1/1280) needs a=0")
    # Lemma SE dyadic algebra: H = K^(2/3) N^(2/3) balances H N^2 with K^2 N^4 / H^2
    # symbolic check with exponents (K^x N^y as pairs):
    HN2 = (F(2, 3), F(2, 3) + 2)
    tail = (2 - 2 * F(2, 3), 4 - 2 * F(2, 3))
    assert HN2 == tail == (F(2, 3), F(8, 3))
    # SdZ rich-line step: h N t <= C K^(1/2) N^2 t^(3/4)  =>  t <= C' K^2 N^4 / h^4
    lhs_t_exp = F(1) - F(3, 4)
    assert 1 / lhs_t_exp == 4  # t^(1/4) <= C K^(1/2) N / h
    # SdZ hypotheses: a = N <= b = K N; a b^2 <= n^3 with n = t N  <=>  K^2 <= t^3;
    # a n = N^2 t <= N^4 / h <= p^2 / h for N <= sqrt p
    print("Lemma SE exponent algebra OK; SdZ hypothesis translation recorded")
    print("ALL OK")


if __name__ == "__main__":
    main()
