#!/usr/bin/env python3
"""Round 181 exact identity checks (integer arithmetic, random integer weights).

For a nonnegative integer weight mu on Aff(F_p) = {(r,b): r!=0}, acting by
j(e) = r e + b, and an integer function f on F_p, check exactly:
 (I1) sum_s |F_mu f(s)|^2 = sum_h Delta(h) m_f(h),
      F_mu f(s) = sum_j mu(j) f(j^{-1} s), Delta(h) = sum_j mu(j) mu(j h),
      m_f(h) = sum_e f(e) f(h^{-1} e), (j h)(e) = j(h(e)), h=(a,c): e -> a e + c.
 (I2) p * sum_s |F_mu f|^2 = M1^2 (sum f)^2 + p * ||F_mu f0||^2 , f0 = f - mean
      (checked as p^2-scaled integers).
 (I3) Hilbert-Schmidt: ||K||_HS^2 = p sum mu^2 + M1^2 - sum_r m(r)^2, where
      K(y,e) = sum_{j: j e = y} mu(j); hence ||K0||_HS^2 = p sum mu^2 - sum_r m(r)^2.
 (I4) the inequality p^2||F_mu f0||^2 <= ||K0||_HS^2 * p^2 ||f0||^2 (scaled).
 (I5) fibre sums: sum_c Delta(a,c) = sum_r m(r) m(a r).
Primes: 13, 17, 29, 37 (several random seeds). Exact integers throughout.
"""
import random


def check(p, seed):
    rng = random.Random(seed)
    inv = [0] + [pow(x, p - 2, p) for x in range(1, p)]
    # sparse random weight
    mu = {}
    for r in range(1, p):
        for b in range(p):
            if rng.random() < 0.3:
                mu[(r, b)] = rng.randint(1, 5)
    f = [rng.randint(0, 4) for _ in range(p)]
    M1 = sum(mu.values())
    # F_mu f
    F = [0] * p
    for (r, b), w in mu.items():
        for e in range(p):
            F[(r * e + b) % p] += w * f[e]
    lhs = sum(x * x for x in F)
    # Delta and m_f
    Delta = {}
    items = list(mu.items())
    for (r, b), w in items:
        for (r2, b2), w2 in items:
            # j' = j h : r2 = r a, b2 = b + c r
            a = r2 * inv[r] % p
            c = (b2 - b) * inv[r] % p
            Delta[(a, c)] = Delta.get((a, c), 0) + w * w2
    def m_f(a, c):
        # sum_e f(e) f(h^{-1} e), h^{-1}(e) = (e - c)/a
        ia = inv[a]
        return sum(f[e] * f[((e - c) * ia) % p] for e in range(p))
    rhs = sum(D * m_f(a, c) for (a, c), D in Delta.items())
    assert lhs == rhs, (p, seed, 'I1')
    # I2: f0 = f - S/p ; p*F0 = p*F - M1*S
    S = sum(f)
    F0p = [p * x - M1 * S for x in F]  # = p * F_mu f0
    assert p * p * lhs == p * M1 * M1 * S * S + sum(x * x for x in F0p), (p, seed, 'I2')
    # I3: HS
    K = [[0] * p for _ in range(p)]
    for (r, b), w in mu.items():
        for e in range(p):
            K[(r * e + b) % p][e] += w
    HS = sum(x * x for row in K for x in row)
    m = [0] * p
    for (r, b), w in mu.items():
        m[r] += w
    smu2 = sum(w * w for w in mu.values())
    sm2 = sum(x * x for x in m)
    assert HS == p * smu2 + M1 * M1 - sm2, (p, seed, 'I3')
    HS0 = p * smu2 - sm2
    # I4: p^2 ||F f0||^2 <= HS0 * p^2 ||f0||^2 ; p^2||f0||^2 = sum (p f - S)^2
    f0n = sum((p * x - S) ** 2 for x in f)
    assert sum(x * x for x in F0p) <= HS0 * f0n, (p, seed, 'I4')
    # I5 fibre sums
    for a in range(1, p):
        Ca = sum(Delta.get((a, c), 0) for c in range(p))
        assert Ca == sum(m[r] * m[(a * r) % p] for r in range(1, p)), (p, seed, 'I5')
    ratio = sum(x * x for x in F0p) / (HS0 * f0n)
    return ratio


if __name__ == '__main__':
    for p in (13, 17, 29, 37):
        rs = [check(p, s) for s in range(3)]
        print(f"p={p}: identities I1-I5 exact OK; ||F f0||^2/(HS0 ||f0||^2) = "
              + ", ".join(f"{x:.4f}" for x in rs))
