#!/usr/bin/env python3
"""Round 191 (literature call ordinary-gp-sector-constancy-literature): finite sanity checks.

Evidence only (exact integer arithmetic, small fields); not a proof and not a certificate.

Part V  (prime fields).  For p = 1 mod 4 prime, zeta in Q (the squares), and the symmetric
progression P = {zeta^h : |h| <= M} with 2M < ord(zeta), let E_rho = #{0 < |h| <= M :
chi(1 - zeta^h) = -rho}.  Vinogradov's bilinear bound |sum_{a in A, b in B} chi(a+b)| <=
sqrt(p|A||B|), applied to A = {zeta^j : 0 <= j <= M}, B = -A, gives E_rho >= (M - sqrt p)/2
(see the report, section 3.1).  The script checks this inequality exhaustively for small p and
reports the minimum of E_rho over zeta, rho, for each M.

Part F  (the F_{r^2} control).  In F_{r^2} every element of F_r is a square, so a generator
zeta of F_r^* (order r - 1 = sqrt(q) - 1) has chi(1 - zeta^k) = +1 for 1 <= k <= r - 2: the
sector-constancy statement (GP-Sub_c) fails in F_{r^2} for every c < 1.  The script verifies
this by explicit F_{r^2} arithmetic.

Part X  (exponent bookkeeping, exact Fractions).

Usage:
  python3 -B research/paley-191-gpsub-checks.py            # all parts, small ranges (< 10 s)
  python3 -B research/paley-191-gpsub-checks.py --pmax 1000
"""
import argparse
import math
from fractions import Fraction


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    r = int(math.isqrt(n))
    for d in range(3, r + 1, 2):
        if n % d == 0:
            return False
    return True


def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def mult_order(z, p):
    k, x = 1, z % p
    while x != 1:
        x = x * z % p
        k += 1
    return k


def part_v(pmax):
    worst_margin = None
    checked = 0
    for p in range(13, pmax + 1, 4):
        if not is_prime(p):
            continue
        chi = [legendre(a, p) for a in range(p)]
        squares = sorted({x * x % p for x in range(1, p)})
        for z in squares:
            if z == 1:
                continue
            o = mult_order(z, p)
            # s[h] = chi(1 - z^h) for 1 <= h < o
            s = [0] * o
            x = 1
            for h in range(1, o):
                x = x * z % p
                s[h] = chi[(1 - x) % p]
            for M in range(1, (o - 1) // 2 + 1):  # 2M < o
                # symmetric: chi(1 - z^-h) = chi(1 - z^h) because -1 and z are squares
                plus = sum(1 for h in range(1, M + 1) if s[h] == 1)
                minus = M - plus
                for E in (2 * plus, 2 * minus):  # counts over 0 < |h| <= M
                    bound = (M - math.sqrt(p)) / 2
                    margin = E - bound
                    checked += 1
                    if margin < -1e-9:
                        raise SystemExit(f"VIOLATION p={p} z={z} M={M} E={E} bound={bound}")
                    if worst_margin is None or margin < worst_margin[0]:
                        worst_margin = (margin, p, z, M, E)
    print(f"Part V: inequality E >= (M - sqrt p)/2 held in all {checked} (p, zeta, M, sign) cases, "
          f"p <= {pmax}; smallest margin {worst_margin[0]:.3f} at p={worst_margin[1]}, "
          f"zeta={worst_margin[2]}, M={worst_margin[3]}, E={worst_margin[4]}")


def part_f():
    # F_{r^2} = F_r[t]/(t^2 - n), n a nonsquare mod r; elements (a, b) = a + b t.
    for r in (7, 11, 19, 23, 31, 43):
        n = next(c for c in range(2, r) if legendre(c, r) == -1)
        q = r * r

        def mul(u, v):
            return ((u[0] * v[0] + n * u[1] * v[1]) % r, (u[0] * v[1] + u[1] * v[0]) % r)

        def power(u, e):
            res, base = (1, 0), u
            while e:
                if e & 1:
                    res = mul(res, base)
                base = mul(base, base)
                e >>= 1
            return res

        def chi(u):  # quadratic character of F_{r^2}
            if u == (0, 0):
                return 0
            return 1 if power(u, (q - 1) // 2) == (1, 0) else -1

        g = next(a for a in range(2, r) if mult_order(a, r) == r - 1)
        zeta = (g, 0)
        assert chi(zeta) == 1
        run = 0
        x = (1, 0)
        for k in range(1, r - 1):
            x = mul(x, zeta)
            if chi(((1 - x[0]) % r, (-x[1]) % r)) == 1:
                run += 1
            else:
                break
        print(f"Part F: q = {r}^2: generator zeta of F_r^* has order {r-1}, "
              f"run R(zeta) = {run} = r - 2 = sqrt(q) - 2 (chi(1 - zeta^k) = +1 throughout)")
        assert run == r - 2


def part_x():
    ok = True
    # Hanson-Petridis: R+1 <= (sqrt(2p-1)+1)/2  =>  R/sqrt p -> 1/sqrt 2.
    # Needed range: c ~ theta/2 < 1/4 for D_theta (theta < 1/2).
    ok &= Fraction(1, 4) ** 2 < Fraction(1, 2)          # 1/4 < 1/sqrt 2
    # Vinogradov version of (GP-Sub_kappa): E >= (c0 - 1) sqrt p / 2 > 0 iff c0 > 1.
    ok &= Fraction(1, 4) < 1
    # Kim-Yip-Yoo product-set route: s(R - s + 1) <= (p-1)/2 with s ~ R/2 gives R <~ sqrt(2p).
    ok &= Fraction(2) > Fraction(1, 2)                  # sqrt 2 > 1/sqrt 2 (compare squares)
    # Criterion 5.2 (Round 190, audit form): delta < 5 kappa; Vinogradov-type kappa < 1/2.
    ok &= 5 * Fraction(1, 2) > Fraction(1, 52)
    # Kerr additive bound p^(1/8) N^(71/96) < N iff N > p^(12/25); 12/25 < 1/2.
    ok &= Fraction(1, 8) / (1 - Fraction(71, 96)) == Fraction(12, 25)
    ok &= Fraction(12, 25) < Fraction(1, 2)
    print("Part X:", "ALL OK" if ok else "FAILED")
    if not ok:
        raise SystemExit(1)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--pmax", type=int, default=400)
    args = ap.parse_args()
    part_v(args.pmax)
    part_f()
    part_x()
