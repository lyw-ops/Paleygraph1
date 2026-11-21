#!/usr/bin/env python3
r"""Round 182 (call ordinary-prime-one-match-operator-norm): exact identity checks.

Everything here is exact integer arithmetic on the ACTUAL one-match affine chart
of Round 171, with random nonnegative integer weights g supported on the squares Q
(the identities are linear/multilinear in g, so integer weights test them exactly).

Chart (Round 171): for Y, D in F_p \ {0,1}, Y != D, g(Y)g(D) != 0 (so Y, D in Q),
    r = (Y-D)/(1-D),  b = D(1-Y)/(Y(1-D)),   mask: b in Q,
    mu(r,b) = g(Y) g(D),   j_{Y,D}(e) = r e + b.
U_j f(s) = f(j^{-1} s); F_mu = sum_j mu(j) U_j; K(y,x) = sum_{j: j x = y} mu(j).
h_t(e) = g(t/e) for e != 0, h_t(0) = 0;  G = sum g;  M1 = sum mu;  m(r) = sum_b mu(r,b).

Checks (all exact):
 (C1) chart: (Y,D) -> (r,b) injective, r,b not in {0,1}; fixed point of j_{Y,D} is D/Y.
 (C2) splitting, every t != 0:  p*||F h_t||^2 = M1^2 G^2 + p*||F h_t - (M1 G/p) 1||^2
      (scaled by p^2), and F h_t - (M1 G/p)1 = F(h_t - G/p) (mean-zero part).
 (C3) trace identity, k = 1,2,3:  tr((K K^T)^k) - M1^(2k) = p T_k(mu) - T_k^x(m),
      T_k(mu) = (mu * mu~)^{*k}(id) on Aff(F_p), T_k^x(m) = (m * m~)^{*k}(1) on F_p^*.
      (k=1 is the Hilbert-Schmidt identity ||pi(mu)||_HS^2 = p sum mu^2 - sum m^2.)
 (C4) the s = 1 row:  K(1,x) = g(1/x) n(1/x) for x != 0, where
      n(Y) = sum_{D in F_p\{0,1,Y}, chi(1-D) = chi(1-Y)} g(D); and K(1,0) = 0.
 (C5) conic degeneracy: for x != 0, the fibre {(Y,D): j_{Y,D}(x) = y} lies on the conic
      D(1-(1+x-y)Y) = Y(y - xY); its determinant equals (x-y)(1-y)/4 up to sign,
      checked as: the conic is a product of two lines exactly when y in {1, x}.
      (verified by brute force: the zero set over F_p contains a full line iff y in {1,x}).
 (C6) entry bound: every entry K(y,x) <= gmax*G (for y != 1 each Y has at most one D on the
      fibre; for y = 1 only Y = 1/x occurs), hence every row and column of K has squared
      norm <= gmax*G*M1 (row and column sums equal M1).
Primes 13, 17, 29 (several seeds) for C1-C4; C3 is checked for k = 1, 2, 3 at every prime.
Replay:  python3 research/paley-182-opnorm-identities.py
"""
import random


def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def chart(p, g):
    """Return dict mu[(r,b)] for the actual masked chart, plus the pair list."""
    inv = lambda z: pow(z, p - 2, p)
    mu = {}
    pairs = []
    for Y in range(2, p):
        if g[Y] == 0:
            continue
        for D in range(2, p):
            if D == Y or g[D] == 0:
                continue
            r = (Y - D) * inv(1 - D) % p
            b = D * (1 - Y) * inv(Y * (1 - D) % p) % p
            if legendre(b, p) != 1:
                continue
            assert r not in (0, 1) and b not in (0, 1)
            assert (r, b) not in mu, 'chart not injective'
            # fixed point of e -> r e + b is b/(1-r) = D/Y
            assert b * inv(1 - r) % p == D * inv(Y) % p
            mu[(r, b)] = g[Y] * g[D]
            pairs.append((Y, D, r, b))
    return mu, pairs


def kernel(p, mu):
    K = [[0] * p for _ in range(p)]
    for (r, b), w in mu.items():
        for x in range(p):
            K[(r * x + b) % p][x] += w
    return K


def matmul(A, B):
    p = len(A)
    Bt = list(zip(*B))
    return [[sum(a * b for a, b in zip(row, col)) for col in Bt] for row in A]


def group_conv(f1, f2, p):
    out = {}
    for (r1, b1), w1 in f1.items():
        for (r2, b2), w2 in f2.items():
            k = (r1 * r2 % p, (r1 * b2 + b1) % p)
            out[k] = out.get(k, 0) + w1 * w2
    return out


def check(p, seed, kmax):
    rng = random.Random(seed)
    g = [0] * p
    for x in range(1, p):
        if legendre(x, p) == 1 and rng.random() < 0.7:
            g[x] = rng.randint(1, 3)
    G = sum(g)
    mu, pairs = chart(p, g)
    M1 = sum(mu.values())
    K = kernel(p, mu)
    inv = lambda z: pow(z, p - 2, p)
    # (C2) splitting
    for t in range(1, p):
        h = [0] + [g[t * inv(e) % p] for e in range(1, p)]
        assert sum(h) == G
        Fh = [sum(K[y][x] * h[x] for x in range(p)) for y in range(p)]
        lhs = sum(v * v for v in Fh)
        # p*(F h - M1 G/p) = p*Fh - M1*G ; and F(p h - G) = p Fh - G*M1
        h0 = [p * v - G for v in h]
        Fh0 = [sum(K[y][x] * h0[x] for x in range(p)) for y in range(p)]
        assert Fh0 == [p * v - M1 * G for v in Fh]
        assert p * p * lhs == p * M1 * M1 * G * G + sum(v * v for v in Fh0)
    # (C3) trace identity
    m = {}
    for (r, b), w in mu.items():
        m[r] = m.get(r, 0) + w
    mut = {(inv(r), (-b * inv(r)) % p): w for (r, b), w in mu.items()}
    nu = group_conv(mu, mut, p)
    mt = {inv(r): w for r, w in m.items()}
    nux = {}
    for r1, w1 in m.items():
        for r2, w2 in mt.items():
            k = r1 * r2 % p
            nux[k] = nux.get(k, 0) + w1 * w2
    KKt = matmul(K, [list(c) for c in zip(*K)])
    P = [row[:] for row in KKt]
    nuk = dict(nu)
    nuxk = dict(nux)
    for k in range(1, kmax + 1):
        if k > 1:
            P = matmul(P, KKt)
            nuk = group_conv(nuk, nu, p)
            new = {}
            for r1, w1 in nuxk.items():
                for r2, w2 in nux.items():
                    kk = r1 * r2 % p
                    new[kk] = new.get(kk, 0) + w1 * w2
            nuxk = new
        tr = sum(P[i][i] for i in range(p))
        Tk = nuk.get((1, 0), 0)
        Tkx = nuxk.get(1, 0)
        assert tr - M1 ** (2 * k) == p * Tk - Tkx, (p, seed, k)
        if k == 1:
            assert Tk == sum(w * w for w in mu.values())
            assert Tkx == sum(w * w for w in m.values())
    # (C6) entry, row and column bounds
    gmax = max(g)
    for y in range(p):
        assert sum(K[y]) == M1
        assert max(K[y]) <= gmax * G
        assert sum(v * v for v in K[y]) <= gmax * G * M1
    for x in range(p):
        col = [K[y][x] for y in range(p)]
        assert sum(col) == M1 and sum(v * v for v in col) <= gmax * G * M1
    # (C4) s = 1 row
    assert K[1][0] == 0
    for x in range(1, p):
        Y = inv(x)
        n = sum(g[D] for D in range(2, p)
                if D != Y and legendre(1 - D, p) == legendre(1 - Y, p))
        exp = g[Y] * n if Y != 1 else 0
        assert K[1][x] == exp, (p, seed, x)
    return M1, G


def check_conics(p):
    """(C5): zero set of D(1-(1+x-y)Y) - Y(y-xY) on F_p^2 contains a full affine line
    iff y in {1, x} (x != 0)."""
    for x in range(1, p):
        for y in range(p):
            Z = {(Y, D) for Y in range(p) for D in range(p)
                 if (D * (1 - (1 + x - y) * Y) - Y * (y - x * Y)) % p == 0}
            has_line = False
            # lines D = aY + c, and vertical lines Y = c
            for a in range(p):
                for c in range(p):
                    if all((Y, (a * Y + c) % p) in Z for Y in range(p)):
                        has_line = True
            for c in range(p):
                if all((c, D) in Z for D in range(p)):
                    has_line = True
            assert has_line == (y in (1 % p, x)), (p, x, y)


if __name__ == '__main__':
    for p in (13, 17, 29):
        for seed in range(2):
            kmax = 3
            M1, G = check(p, seed, kmax)
            print(f"p={p} seed={seed}: C1-C4, C6 exact OK (k<= {kmax}); M1={M1}, G={G}")
    for p in (7, 11, 13):
        check_conics(p)
        print(f"p={p}: C5 degenerate fibres exactly y in {{1, x}}")
    print("all exact checks passed")
