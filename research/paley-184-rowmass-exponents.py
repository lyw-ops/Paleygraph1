#!/usr/bin/env python3
r"""Round 184, call ordinary-prime-near-critical-slope-row-mass: exponent bookkeeping.

Exact Fractions. All exponents are powers of p, with G = Theta(sqrt p) and
M_1 = Theta(p) (true on (NC) by Round 183 Proposition 1.2).

1. One-match covariance as a function of the affine energy E(mu) = p^e.
   (a) Rounds 178/180 route (Rudnev-Shkredov second norm, accepted):
       ||H_alpha||_2 << G^(5/8) E^(1/8) M_1^(1/2) + M_1(1 + G/sqrt p),
       sum_t w(t)|H_alpha|^2 << G ||H_alpha||_2^2, covariance = that / p,
       i.e. covariance exponent c(e) = 9/8 + e/4 (for e >= 3/2).
   (b) Round 182 operator route (accepted): covariance = ||pi||^2 <= (p E)^(1/2),
       exponent c_op(e) = (1 + e)/2.
2. E(mu) from the slope products (Round 178 point-plane, accepted):
       E << sum W^2/p + sum W^(3/2) + G log p sum W,
   with max W = p^(1+eps): e = max(2+eps, 5/2+eps/2, 5/2) = 5/2 + eps/2 (0<=eps<=1);
   with sup_{lambda!=1} C = p^(1+eps): E^x(m) <= X^2 + sup C M_1^2, X <= p^(34/23).
3. Lemma Y thresholds: X <= (G-1)^2 Gamma_2 = p^(1+gamma) if Gamma_2 = p^gamma.
4. Light-band criterion: Round 182 heavy part with split tau = p^(-eps):
       N(h_heavy) << p^(1/3+5eps/3) + p^(1/3+2eps/3+delta/6) + p^(3/8-3delta/4),
   optimized in delta; one-match improvement needs 4*eta(eps) < 11/8.
"""
from fractions import Fraction as F


def c_rs(e):
    # second norm exponent: G^(5/8) E^(1/8) M_1^(1/2) with G=p^(1/2), M_1=p
    norm = F(5, 16) + e / 8 + F(1, 2)
    assert norm >= 1  # the M_1(1+G/sqrt p) = O(p) term is not larger
    total = 2 * norm + F(1, 2)  # sum_t w(t) |H|^2 <= G * norm^2
    return total - 1, norm, total


def c_op(e):
    return (1 + e) / 2


def main():
    ok = True
    # 1. reproduce the accepted table entries
    e178 = F(11, 4) - F(3, 836)
    c, norm, tot = c_rs(e178)
    assert norm == F(37, 32) - F(3, 6688) and tot == F(45, 16) - F(3, 3344) and c == F(29, 16) - F(3, 3344)
    e180 = F(43, 16)
    c, norm, tot = c_rs(e180)
    assert (norm, tot, c) == (F(147, 128), F(179, 64), F(115, 64))
    assert c_op(e180) == F(118, 64)  # Round 182 accepted: covariance 118/64
    print("R178 row: E=11/4-3/836 -> second norm 37/32-3/6688, sum w|H|^2 45/16-3/3344, covariance 29/16-3/3344  OK")
    print("R180 row: E=43/16 -> second norm 147/128, sum w|H|^2 179/64, covariance 115/64 (RS route)  OK")
    print("R182 operator route at E=43/16: covariance 118/64  OK")
    # comparison of the two routes: c_op - c_rs = e/4 - 5/8 >= 0 iff e >= 5/2
    for e in (F(5, 2), F(21, 8), F(43, 16), F(11, 4)):
        d = c_op(e) - c_rs(e)[0]
        assert d == e / 4 - F(5, 8) and d >= 0
    print("c_op(e) - c_rs(e) = e/4 - 5/8 >= 0 for every e >= 5/2 (the RS route is never worse)  OK")
    # 2. max W = p^(1+eps)
    def e_of_maxW(eps):
        return max(2 + eps, F(5, 2) + eps / 2, F(5, 2))
    for eps in (F(0), F(1, 16), F(3, 16), F(1, 4), F(3, 8), F(1, 2), F(11, 23)):
        e = e_of_maxW(eps)
        assert e == F(5, 2) + eps / 2
        assert c_rs(e)[0] == F(7, 4) + eps / 8
        assert c_op(e) == F(7, 4) + eps / 4
    thr_rs = (F(115, 64) - F(7, 4)) * 8
    thr_op = (F(115, 64) - F(7, 4)) * 4
    assert (thr_rs, thr_op) == (F(3, 8), F(3, 16))
    print(f"max W = p^(1+eps): E = p^(5/2+eps/2), covariance p^(7/4+eps/8) (RS) vs p^(7/4+eps/4) (operator);")
    print(f"   improvement over 115/64 iff eps < {thr_rs} (RS route); the operator route needs eps < {thr_op}")
    # current status of max W: max W <= X <= p^(34/23)
    epsX = F(34, 23) - 1
    print(f"   current max W <= X = O(p^(34/23)): eps = {epsX} = {float(epsX):.4f} > 3/8: no improvement from X today")
    # sup C version
    for eps in (F(0), F(1, 8), F(3, 8)):
        Em = max(2 * F(34, 23), 3 + eps)  # E^x(m) <= X^2 + sup C * M_1^2
        assert Em == 3 + eps
        sumW32 = 1 + Em / 2  # sum W^(3/2) <= M_1 E^x(m)^(1/2)
        sumW2p = Em - 1
        e = max(sumW2p, sumW32, F(5, 2))
        assert e == F(5, 2) + eps / 2
    assert 2 * F(34, 23) < 3
    print("sup_{lambda!=1} C = p^(1+eps): E^x(m) = O(p^(3+eps)) since X^2 <= p^(68/23) < p^3; same E and threshold eps < 3/8")
    print("   (Round 180: eps = 3/8 exactly, giving 43/16 and 115/64)")
    # 3. Lemma Y: X <= (G-1)^2 Gamma_2
    g_onematch = thr_rs
    g_X = F(1, 1280)
    g_firstmass_G2 = F(1, 4) + F(1, 2560)  # Round 183 (G2): M_w <= (G-1) Gamma_2^2
    assert F(1, 2) + 2 * g_firstmass_G2 == 1 + F(1, 1280)
    print(f"Lemma Y: Gamma_2 = O(p^gamma) gives X = O(p^(1+gamma)); one-match improves iff gamma < {g_onematch};")
    print(f"   X-target needs gamma <= {g_X}; the first mass directly needs gamma <= {g_firstmass_G2} (Round 183 G2)")
    # 4. light-band criterion
    def eta(eps):
        # optimize delta in max(1/3+2eps/3+delta/6, 3/8-3delta/4), delta >= 0
        delta = (F(1, 24) - F(2, 3) * eps) / F(11, 12)
        assert delta >= 0
        a = F(1, 3) + F(2, 3) * eps + delta / 6
        b = F(3, 8) - F(3, 4) * delta
        assert a == b
        return max(F(1, 3) + F(5, 3) * eps, a), delta
    e0, d0 = eta(F(0))
    assert e0 == F(15, 44) and d0 == F(1, 22)
    print(f"heavy part with tau constant: N << p^(15/44), i.e. E^x(h_heavy) = O(p^(15/11)), 15/11 = {float(F(15,11)):.4f} < 11/8")
    epsb = F(1, 192)
    eb, _ = eta(epsb)
    assert eb == F(11, 32)
    assert F(1, 3) + F(5, 3) * epsb < F(11, 32)
    for eps in (F(1, 200), F(1, 1000)):
        assert 4 * eta(eps)[0] < F(11, 8)
    assert 4 * eta(F(1, 190))[0] > F(11, 8)
    print("light-band criterion: with tau = p^(-eps), eps < 1/192, the heavy part is O(p^(11/8 - c(eps))), c > 0;")
    print("   so sum_{x != 1, g(x) < p^(-1/192)} g(x)^2 = O(p^(3/8 - delta)) implies X = O(p^(11/8 - delta')) and")
    print("   a one-match exponent below 115/64. Boundary eps = 1/192 gives exactly 11/32.  OK")
    # Round 182 ledger reproduction at eps = 1/46
    e46, d46 = F(1, 46), F(1, 138)
    assert F(1, 3) + F(5, 3) * e46 == F(3, 8) - e46 / 4 == F(17, 46)
    print("Round 182 balance at eps=1/46 reproduced (17/46 -> 34/23)  OK")
    print("ALL OK" if ok else "FAIL")


if __name__ == "__main__":
    main()
