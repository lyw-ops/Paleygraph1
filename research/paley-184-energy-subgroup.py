#!/usr/bin/env python3
"""Round 184 (near-critical support energy): exact integer evidence for (Sub).

(Sub): for subgroups B <= Q of order b with b asymp sqrt(p), the shifted-subgroup
quadratic-character sum  A(B) = sum_{y in B, y != 1} chi(1-y)  is <= (1-c)(b-1)
in absolute value.  The report shows that the subgroup model of energy 1/2 needs
|A(B)| = (1-o(1)) b for some B of order about sqrt(p)/C.

For every prime p = 1 mod 4 in [lo, hi] and every divisor b of n=(p-1)/2 with
sqrt(p)/4 <= b <= 2 sqrt(p), compute A(B)/(b-1) exactly (integer sums, floats
only for the ratio).  Prints per-range maxima and the extreme cases.
This is finite evidence; it proves nothing asymptotic.
Usage: .venv/bin/python -B research/paley-184-energy-subgroup.py LO HI
"""
import sys
import math


def is_prime(m):
    if m < 2:
        return False
    if m % 2 == 0:
        return m == 2
    r = int(math.isqrt(m))
    f = 3
    while f <= r:
        if m % f == 0:
            return False
        f += 2
    return True


def primitive_root(p):
    phi = p - 1
    fac, m, d = [], phi, 2
    while d * d <= m:
        if m % d == 0:
            fac.append(d)
            while m % d == 0:
                m //= d
        d += 1
    if m > 1:
        fac.append(m)
    for g in range(2, p):
        if all(pow(g, phi // q, p) != 1 for q in fac):
            return g


def main():
    lo, hi = int(sys.argv[1]), int(sys.argv[2])
    worst = []  # (ratio, p, b, A)
    count = 0
    for p in range(lo | 1, hi + 1, 2):
        if p % 4 != 1 or not is_prime(p):
            continue
        n = (p - 1) // 2
        sq = math.sqrt(p)
        bs = [b for b in range(max(3, int(sq / 4)), int(2 * sq) + 1) if n % b == 0]
        if not bs:
            continue
        th = primitive_root(p)
        for b in bs:
            gen = pow(th, (p - 1) // b, p)  # order b, inside Q since b | n
            y, A = gen, 0
            for _ in range(b - 1):
                A += 1 if pow((1 - y) % p, n, p) == 1 else -1
                y = y * gen % p
            count += 1
            worst.append((abs(A) / (b - 1), p, b, A))
    worst.sort(reverse=True)
    print(f"primes in [{lo},{hi}], subgroups with sqrt(p)/4 <= b <= 2 sqrt(p): {count}")
    print("largest |A(B)|/(b-1):  ratio  p  b  b/sqrt(p)  A")
    for r, p, b, A in worst[:12]:
        print(f"  {r:.4f}  {p}  {b}  {b / math.sqrt(p):.3f}  {A}")
    # max ratio by b/sqrt(p) band, restricted to b >= 30 to suppress tiny-b noise
    bands = [(0.25, 0.5), (0.5, 1.0), (1.0, 2.0)]
    for a1, a2 in bands:
        sel = [w for w in worst if a1 <= w[2] / math.sqrt(w[1]) < a2 and w[2] >= 30]
        if sel:
            r, p, b, A = max(sel)
            mean = sum(w[0] for w in sel) / len(sel)
            print(f"band b/sqrt(p) in [{a1},{a2}), b>=30: N={len(sel)} max={r:.4f} (p={p}, b={b}) mean={mean:.4f}")


if __name__ == "__main__":
    main()
