#!/usr/bin/env python3
"""Round 183 audit: independent checks for the row-deleted report
(research/native-claude-ordinary-prime-row-deleted-one-match-183.md).

Written by the Round 183 auditor without reusing the report's code.

Exact part (Python integers; all operators scaled by p so that P = (pI - J)/p is integral):
  R1  Proposition 2.1/2.3: with Delta split by pair type I/S/P/G and
      A = R P F F^* P R (outputs s = 0, 1 deleted), Z = R pi(Delta_S+Delta_P+Delta_G) R:
        tr(A^3) == c^3 tr((RPR)^3) + 3c^2 tr((RPR)^2 Z) + 3c tr(RPR Z^2) + tr(Z^3);
      IXX >= 0 and IXX <= 3 c p (E(mu) - c^2); tr(Z^2) <= p (E(mu) - c^2).
  R2  Proposition 2.4: E(mu) <= 8c^2 + tr(A^3)/(p abar) + (4G^7 + E^x(m))/p with abar = tr(A)/(p-2),
      and the scalar inequality tr(A^3) >= c0 ||A - c0 I||_HS^2 - (p-2)c0^3 for c0 in {abar, c, 1}.
  R3  Trace identity k = 2: p E(mu) = tr((pi pi^*)^2) + E^x(m)  (Round 182, re-checked).
Floating part (numpy eigvalsh / eigh, labelled [float]):
  R4  Proposition 2.2: pi(Delta_I + Delta_S) is diagonal in the additive Fourier basis with
      entries sum_r |mu_r^(eta)|^2 <= X;  max_z L_z^2 <= ||pi(Delta_I+Delta_P)|| <= sum_z L_z^2;
      | ||A|| - ||R pi(Delta_G) R|| | <= X + sum_z L_z^2 + c.
  R5  Proposition 1.1 (Parseval): for a random probability nu on Z/n,
      f = sum nu_j j on Q, g = |f|^2:  sum g^2 = n E(nu)  and  G = n sum nu^2.

Replay: .venv/bin/python -B research/paley-183-audit-rowdel-check.py
"""
import cmath
import random

import numpy as np


def inv(a, p):
    return pow(a % p, p - 2, p)


def letters(p, g):
    """Round 171 chart: letters j = (r, b) with weight mu = g(Y) g(D) (integers)."""
    Q = {x * x % p for x in range(1, p)}
    mu = {}
    for Y in Q:
        for D in Q:
            if Y == 1 or D == 1 or Y == D:
                continue
            if g[Y] * g[D] == 0:
                continue
            b = D * (1 - Y) * inv(Y * (1 - D), p) % p
            if b not in Q:
                continue
            r = (Y - D) * inv(1 - D, p) % p
            mu[(r, b)] = mu.get((r, b), 0) + g[Y] * g[D]
    return Q, mu


def fix(j, p):
    r, b = j
    return b * inv(1 - r, p) % p


def quot(j, k, p):
    """j o k^{-1} for affine maps e -> r e + b."""
    r, b = j
    r2, b2 = k
    q = r * inv(r2, p) % p
    return (q, (b - q * b2) % p)


def perm(h, p):
    """integer matrix of U_h: U_h[s, e] = 1 iff s = h(e)."""
    r, b = h
    M = np.zeros((p, p), dtype=object)
    for e in range(p):
        M[(r * e + b) % p, e] = 1
    return M


def check_exact(p, seed):
    rng = random.Random(seed)
    Q = {x * x % p for x in range(1, p)}
    g = {x: 0 for x in range(p)}
    for x in Q:
        g[x] = rng.randint(0, 3)
    g[1] = 3  # integer weights; the identities are homogeneous
    Q, mu = letters(p, g)
    L = list(mu)
    Dl = {t: {} for t in "ISPG"}
    for j in L:
        for k in L:
            h = quot(j, k, p)
            if j == k:
                t = "I"
            elif j[0] == k[0]:
                t = "S"
            elif fix(j, p) == fix(k, p):
                t = "P"
            else:
                t = "G"
            Dl[t][h] = Dl[t].get(h, 0) + mu[j] * mu[k]
    Pp = np.array([[p * (s == e) - 1 for e in range(p)] for s in range(p)], dtype=object)  # pP

    def op(D):
        M = np.zeros((p, p), dtype=object)
        for h, v in D.items():
            M = M + v * perm(h, p)
        return M

    OP = {t: op(Dl[t]) for t in "ISPG"}
    full = OP["I"] + OP["S"] + OP["P"] + OP["G"]
    c = sum(mu[j] ** 2 for j in L)
    E = 0
    Dall = {}
    for t in "ISPG":
        for h, v in Dl[t].items():
            Dall[h] = Dall.get(h, 0) + v
    E = sum(v * v for v in Dall.values())
    assert Dall.get((1, 0), 0) == c
    # p^2 * compressed operators on outputs 2..p-1 (scaled by p^2 since P appears twice)
    def comp(M):
        return (Pp.dot(M).dot(Pp))[2:, 2:]
    A2 = comp(full)                  # p^2 A
    Z2 = comp(OP["S"] + OP["P"] + OP["G"])   # p^2 Z
    RPR2 = (p * Pp)[2:, 2:]          # p^2 RPR
    tr = lambda M: sum(M[i, i] for i in range(M.shape[0]))
    tA3 = tr(A2.dot(A2).dot(A2))     # p^6 tr(A^3)
    III = c ** 3 * tr(RPR2.dot(RPR2).dot(RPR2))
    IIX = 3 * c ** 2 * tr(RPR2.dot(RPR2).dot(Z2))
    IXX = 3 * c * tr(RPR2.dot(Z2).dot(Z2))
    XXX = tr(Z2.dot(Z2).dot(Z2))
    assert tA3 == III + IIX + IXX + XXX
    assert IXX >= 0 and IXX <= 3 * c * p * (E - c * c) * p ** 6
    assert tr(Z2.dot(Z2)) <= p * (E - c * c) * p ** 4
    # R3: trace identity k=2 with masses m(r)
    m = {}
    for (r, b), v in mu.items():
        m[r] = m.get(r, 0) + v
    Ex = 0
    for a in m:
        for b2 in m:
            for c2 in m:
                d = a * b2 * inv(c2, p) % p
                if d in m:
                    Ex += m[a] * m[b2] * m[c2] * m[d]
    PFFP = Pp.dot(full).dot(Pp)  # p^2 * (P F F^* P)
    tr2 = tr(PFFP.dot(PFFP))      # p^4 tr((pi pi^*)^2)
    assert p * E * p ** 4 == tr2 + Ex * p ** 4
    # R2
    from fractions import Fraction as Fr
    trA = Fr(tr(A2), p ** 2)
    abar = trA / (p - 2)
    G = sum(g[x] for x in Q)
    trA3 = Fr(tA3, p ** 6)
    assert Fr(E) <= 8 * c * c + trA3 / (p * abar) + Fr(4 * G ** 7 + Ex, p)
    A = np.array([[Fr(x, p ** 2) for x in row] for row in A2], dtype=object)
    for c0 in (abar, Fr(c), Fr(1)):
        Bm = A - c0 * np.identity(p - 2, dtype=object)
        hs = sum(Bm[i, k] ** 2 for i in range(p - 2) for k in range(p - 2))
        assert trA3 >= c0 * hs - (p - 2) * c0 ** 3
    return dict(p=p, c=c, E=E, IXX=Fr(IXX, p ** 6), tA3=trA3, mu=mu, Dl=Dl, g=g, Q=Q)


def check_float(d):
    p, mu, Dl, c = d["p"], d["mu"], d["Dl"], d["c"]
    Pm = np.eye(p) - np.ones((p, p)) / p

    def opf(D):
        M = np.zeros((p, p))
        for (r, b), v in D.items():
            for e in range(p):
                M[(r * e + b) % p, e] += v
        return Pm @ M @ Pm

    DIS = dict(Dl["S"])
    for h, v in Dl["I"].items():
        DIS[h] = DIS.get(h, 0) + v
    DIP = dict(Dl["P"])
    for h, v in Dl["I"].items():
        DIP[h] = DIP.get(h, 0) + v
    MIS, MIP, MG = opf(DIS), opf(DIP), opf(Dl["G"])
    # additive Fourier basis
    ws = np.array([[cmath.exp(2j * cmath.pi * eta * s / p) for s in range(p)] for eta in range(p)]) / np.sqrt(p)
    T = ws.conj() @ MIS @ ws.T
    off = np.abs(T - np.diag(np.diag(T)))
    off[0, :] = 0
    off[:, 0] = 0
    assert off.max() < 1e-8 * max(1, np.abs(T).max())
    m = {}
    byr = {}
    for (r, b), v in mu.items():
        m[r] = m.get(r, 0) + v
        byr.setdefault(r, []).append((b, v))
    X = sum(v * v for v in m.values())
    for eta in range(1, p):
        ent = sum(abs(sum(v * cmath.exp(-2j * cmath.pi * eta * b / p) for b, v in L)) ** 2 for L in byr.values())
        assert abs(ent - T[eta, eta].real) < 1e-6 * max(1, ent)
        assert ent <= X + 1e-9
    Lz = {}
    for (r, b), v in mu.items():
        z = fix((r, b), p)
        Lz[z] = Lz.get(z, 0) + v
    nIP = np.linalg.eigvalsh((MIP + MIP.T) / 2).max()
    assert max(Lz.values()) ** 2 <= nIP + 1e-6 and nIP <= sum(v * v for v in Lz.values()) + 1e-6
    full = MIS + MIP - opf(Dl["I"]) + MG
    A = full[2:, 2:]
    nA = np.linalg.eigvalsh((A + A.T) / 2).max()
    RG = MG[2:, 2:]
    nG = np.abs(np.linalg.eigvalsh((RG + RG.T) / 2)).max()
    assert abs(nA - nG) <= X + sum(v * v for v in Lz.values()) + c + 1e-6
    print(f"   [float] p={p}: pi(D_I+D_S) diagonal, entries <= X={X}; max L_z^2={max(Lz.values())**2} <= "
          f"||pi(D_I+D_P)||={nIP:.1f} <= sum L_z^2={sum(v*v for v in Lz.values())}; "
          f"| ||A||-||R pi(D_G) R|| | = {abs(nA-nG):.1f} <= {X + sum(v*v for v in Lz.values()) + c}")


def parseval(p, seed):
    rng = random.Random(seed)
    n = (p - 1) // 2
    nu = np.array([rng.random() ** 3 for _ in range(n)])
    nu /= nu.sum()
    primes = [q for q in range(2, p) if (p - 1) % q == 0 and all(q % e for e in range(2, int(q ** .5) + 1))]
    th = next(t for t in range(2, p) if all(pow(t, (p - 1) // q, p) != 1 for q in primes))
    gen = th * th % p
    logs = {pow(gen, k, p): k for k in range(n)}
    gs = []
    for y, k in logs.items():
        f = sum(nu[j] * cmath.exp(2j * cmath.pi * j * k / n) for j in range(n))
        gs.append(abs(f) ** 2)
    gs = np.array(gs)
    lam = np.array([sum(nu[j] * nu[(j - d) % n] for j in range(n)) for d in range(n)])
    En = (lam ** 2).sum()
    assert abs((gs ** 2).sum() - n * En) < 1e-9 * n * En
    assert abs(gs.sum() - n * (nu ** 2).sum()) < 1e-9 * gs.sum()
    print(f"   [float] p={p}: sum g^2 = {(gs**2).sum():.6f} = n E(nu) = {n*En:.6f};  G = {gs.sum():.6f} = n sum nu^2")


if __name__ == "__main__":
    for p, s in ((29, 1), (37, 2), (41, 3), (53, 4)):
        d = check_exact(p, s)
        print(f"R1-R3 p={p}: tr(A^3) = III+IIX+IXX+XXX exactly; 0 <= IXX <= 3cp(E-c^2); Prop 2.4 inequality; "
              f"k=2 trace identity  OK  (tr A^3 = {float(d['tA3']):.4g}, IXX share {float(d['IXX']/d['tA3']):.3f})")
        check_float(d)
    for p in (101, 197):
        parseval(p, p)
    print("ALL ROWDEL AUDIT CHECKS OK")
