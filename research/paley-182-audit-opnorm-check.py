#!/usr/bin/env python3
"""Round 182 independent audit (session/r182-audit): one-match operator-norm report.

Independent of research/paley-182-opnorm-*.py.  Needs numpy (on this machine:
/usr/bin/python3).  Floating point; every check is an inequality or identity
with a stated tolerance, used as an audit cross-check, not as a certificate.

For p in {29, 37, 53, 61} (p = 1 mod 4) and g = |f|^2 with f the Fourier row of a
random probability nu on the characters of Q (so 0 <= g <= 1, g(1) = 1, supp g = Q):
 O1  chart of Round 171 with mask b in Q; mu(r,b) = g(Y)g(D); kernel K(y,x).
 O2  spectral check of Prop. 2: sum_i sigma_i(pi)^(2k) = p T_k(mu) - T_k^x(m), k=1,2,3,
     with T_k computed by convolution on Aff(F_p) (not via traces of K).
 O3  Prop. 4 lower bound sigma_1^2 >= (sum_Y g^2 n^2 - M1^2/p)/(1-1/p) and the
     row-one formula K(1,x) = g(1/x) n(1/x).
 O4  Prop. 5: sigma_3 <= sigma_R <= sigma_1, |sigma_R - ||R K_irr||| <= max_x K(x,x) <= G,
     and sum_{s != 0,1, t} w(t) |F h_t(s)|^2 <= 2G^7/p + 2 sigma_R^2 G sum g^2.
 O5  Prop. 1 splitting for every t.
 O6  Prop. 3(v): the symmetric-matrix determinant of the fibre conic equals
     -(x-y)(1-y)/4 (exact Fractions, random rational x, y).
 O7  exponent arithmetic of Props. 5-6 and the next-test threshold (exact).

Replay: /usr/bin/python3 -B research/paley-182-audit-opnorm-check.py
"""
import random
from fractions import Fraction as F

import numpy as np


def legendre(a, p):
    a %= p
    return 0 if a == 0 else (1 if pow(a, (p - 1) // 2, p) == 1 else -1)


def prim_root(p):
    m = p - 1
    fs = [q for q in range(2, m + 1) if m % q == 0 and all(q % r for r in range(2, int(q ** .5) + 1))]
    return next(c for c in range(2, p) if all(pow(c, m // q, p) != 1 for q in fs))


def make_g(p, rng):
    n = (p - 1) // 2
    gq = prim_root(p)
    nu = rng.random(n) ** 3
    nu /= nu.sum()
    g = np.zeros(p)
    for j in range(n):
        x = pow(gq, 2 * j, p)
        f = np.sum(nu * np.exp(2j * np.pi * np.arange(n) * j / n))
        g[x] = abs(f) ** 2
    return g


def run(p, seed):
    rng = np.random.default_rng(seed)
    g = make_g(p, rng)
    inv = lambda z: pow(z % p, p - 2, p)
    G = g.sum()
    mu = {}
    for Y in range(2, p):
        for D in range(2, p):
            if Y == D or g[Y] == 0 or g[D] == 0:
                continue
            r = (Y - D) * inv(1 - D) % p
            b = D * (1 - Y) * inv(Y * (1 - D)) % p
            if legendre(b, p) != 1:
                continue
            mu[(r, b)] = mu.get((r, b), 0.0) + g[Y] * g[D]
            assert mu[(r, b)] == g[Y] * g[D], "chart not injective"
    M1 = sum(mu.values())
    K = np.zeros((p, p))
    for (r, b), w in mu.items():
        for x in range(p):
            K[(r * x + b) % p, x] += w
    # orthonormal basis of 1-perp
    Bm = np.linalg.qr(np.hstack([np.ones((p, 1)), np.eye(p)[:, : p - 1]]))[0][:, 1:]
    Pi = K @ Bm
    sv = np.linalg.svd(Pi, compute_uv=False)
    # O2: T_k by convolution on Aff(F_p): word j1 j2^-1 j3 j4^-1 ...
    def conv(a, b):
        out = {}
        for (r1, b1), w1 in a.items():
            for (r2, b2), w2 in b.items():
                k = (r1 * r2 % p, (r1 * b2 + b1) % p)
                out[k] = out.get(k, 0.0) + w1 * w2
        return out
    muinv = {(inv(r), (-b * inv(r)) % p): w for (r, b), w in mu.items()}
    step = conv(mu, muinv)
    m = {}
    for (r, b), w in mu.items():
        m[r] = m.get(r, 0.0) + w
    mstep = {}
    for r1, w1 in m.items():
        for r2, w2 in m.items():
            k = r1 * inv(r2) % p
            mstep[k] = mstep.get(k, 0.0) + w1 * w2
    cur, mcur = dict(step), dict(mstep)
    for k in (1, 2, 3):
        if k > 1:
            cur = conv(cur, step)
            new = {}
            for r1, w1 in mcur.items():
                for r2, w2 in mstep.items():
                    kk = r1 * r2 % p
                    new[kk] = new.get(kk, 0.0) + w1 * w2
            mcur = new
        lhs = float(np.sum(sv ** (2 * k)))
        rhs = p * cur.get((1, 0), 0.0) - mcur.get(1, 0.0)
        assert abs(lhs - rhs) <= 1e-8 * max(1.0, abs(lhs)), (p, k, lhs, rhs)
    # O3 row one
    nY = {}
    for Y in range(2, p):
        nY[Y] = sum(g[D] for D in range(2, p) if D != Y and legendre(1 - D, p) == legendre(1 - Y, p))
    for x in range(1, p):
        Y = inv(x)
        exp = g[Y] * nY[Y] if Y != 1 else 0.0
        assert abs(K[1, x] - exp) < 1e-12
    assert K[1, 0] == 0
    lb = (sum(g[Y] ** 2 * nY[Y] ** 2 for Y in range(2, p)) - M1 ** 2 / p) / (1 - 1 / p)
    assert sv[0] ** 2 >= lb - 1e-9
    # O4
    R = np.eye(p)[2:, :]
    sR = np.linalg.norm(R @ Pi, 2)
    assert sv[2] - 1e-9 <= sR <= sv[0] + 1e-9
    Kirr = K.copy()
    Kirr[1, :] = 0
    np.fill_diagonal(Kirr, 0)
    sIrr = np.linalg.norm(R @ Kirr @ Bm, 2)
    dmax = max(K[x, x] for x in range(p))
    assert abs(sR - sIrr) <= dmax + 1e-9 and dmax <= G + 1e-9
    w = g * (1 - g)
    sg2 = float(np.sum(g ** 2))
    lhs5 = 0.0
    for t in range(1, p):
        h = np.array([0.0] + [g[t * inv(e) % p] for e in range(1, p)])
        Fh = K @ h
        # O5 splitting
        hc = h - h.sum() / p
        Khc = K @ hc
        # macOS Accelerate matmul can emit spurious FP warnings; values are checked finite
        assert np.all(np.isfinite(Fh)) and np.all(np.isfinite(Khc))
        assert abs(Fh @ Fh - (M1 ** 2 * G ** 2 / p + np.sum(Khc ** 2))) < 1e-8 * (Fh @ Fh)
        lhs5 += w[t] * float(np.sum(Fh[2:] ** 2))
    rhs5 = 2 * G ** 7 / p + 2 * sR ** 2 * G * sg2
    assert lhs5 <= rhs5
    print(f"p={p} seed={seed}: G={G:.3f} M1={M1:.3f} sum g^2={sg2:.3f} | s1={sv[0]:.3f} "
          f"rowone-lb^(1/2)={max(lb,0)**.5:.3f} s3={sv[2]:.3f} sR={sR:.3f} |sR-sIrr|={abs(sR-sIrr):.3f}<=maxdiag={dmax:.3f} | "
          f"Prop5 lhs/rhs={lhs5/rhs5:.4f}  O2-O5 OK")


def o6():
    rnd = random.Random(5)
    for _ in range(200):
        x = F(rnd.randint(-50, 50), rnd.randint(1, 30))
        y = F(rnd.randint(-50, 50), rnd.randint(1, 30))
        # conic in (Y, D, Z): x Y^2 - (1+x-y) Y D + D Z - y Y Z
        M = [[x, -(1 + x - y) / 2, -y / 2], [-(1 + x - y) / 2, 0, F(1, 2)], [-y / 2, F(1, 2), 0]]
        det = (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
               - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
               + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))
        assert det == -(x - y) * (1 - y) / 4
    print("O6 conic determinant = -(x-y)(1-y)/4 exactly (200 random rational pairs): OK")


def o7():
    # k=2: tr <= p E(mu) = p^(1+43/16); ||pi|| <= p^(59/64); weighted p^(1+59/32) -> covariance -1
    assert F(1) + F(43, 16) == F(59, 16) and F(59, 16) / 4 == F(59, 64)
    assert 2 * F(59, 64) + 1 == F(91, 32) and F(91, 32) - 1 == F(118, 64) > F(115, 64)
    assert F(59, 16) * F(3, 2) == F(177, 32) and F(9, 2) == F(144, 32)
    # next test: tr_3 = p^(9/2+eta) -> sigma_R <= p^(3/4+eta/6) -> covariance 3/2+eta/3 < 115/64 iff eta < 57/64
    eta = F(57, 64)
    assert F(3, 2) + eta / 3 == F(115, 64)
    # (a7) R178 Rudnev-Shkredov route with E=p^2, |U|=p^(1/2), M1=p: |U|^(5/8) E^(1/8) M1^(1/2)
    e = F(5, 8) * F(1, 2) + F(1, 8) * 2 + F(1, 2)
    assert e == F(17, 16) and 2 * e == F(17, 8) and 2 * e + F(1, 2) - 1 == F(13, 8)
    print("O7 exponents: 59/64, 118/64 > 115/64, 177/32 vs 144/32, eta < 57/64, R178 route 13/8: OK")


if __name__ == "__main__":
    np.seterr(all="ignore")
    for p, seed in ((29, 1), (37, 2), (53, 3), (61, 4)):
        run(p, seed)
    o6()
    o7()
    print("ALL AUDIT CHECKS OK")
