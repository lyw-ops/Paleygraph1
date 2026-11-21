#!/usr/bin/env python3
"""Round 191, call ordinary-fixed-block-assembly: floating model evidence.

EVIDENCE ONLY.  The laws below are admissible test laws (probability nu on
the dual of Q, cap n max nu = O(sqrt p), b_0 = 0); none of them is on the
hypothetical critical branch, and nothing here bounds the actual law.

Laws (m = round(n / sqrt p), the critical effective size m_0):
  flat     nu uniform on a random m-subset of Z/n minus {0};
  dtheta   R190 D_theta with theta = 1/4: nu uniform on a random m-subset of
           an interval of length m/theta (R190 NC note, line 199);
  interval nu uniform on the interval {1, ..., m}.

Part A (FFT, large p): vertex mass below fixed levels and X / p.
  m_<a = sum of g(A) over vertex values A in Q with chi(1-A) = rho (v = 1,
  rho = +1) and g(A) < a.  X = E_Q(h), h(z) = g(1-z) (R183 note, lines 47-49).
Part B (small p, O(n^2 log n)): the moment M_nu(F) (R152:58-69), the
  absolute off-diagonal majorant  Abs = sum_{u != 1} sum_{x != y}
  |F(ux)F(x)F(uy)F(y)| |f(t)|, the completed slope masses P_t (R166:9),
  X_c - diag = sum_{t != 1} P_t, M_w, M_sqrt = sum_{t != 1} sqrt(g(t)) P_t,
  where X_c includes the physical zero x = 0 completed in R166:11, so
  X_c = X + O(p) (Part A's X follows R183 and omits z = 0),
  and the assembly inequality of Proposition 1 at a fixed cut level a:
    sqrt M(F) <= sqrt M(F_>=a) + 2 sqrt(n max nu) ||F|| ||F - F_>=a||   (R160)
    M(F_>=a)  <= ||F_>=a||^4 + a^-2 (X - diag).

Run: .venv/bin/python -B research/paley-191-assembly-models.py   (needs numpy)
"""
import numpy as np

rng = np.random.default_rng(191)


def is_prime(q):
    if q < 2:
        return False
    i = 2
    while i * i <= q:
        if q % i == 0:
            return False
        i += 1
    return True


def primitive_root(p):
    fac = set()
    m, d = p - 1, 2
    while d * d <= m:
        while m % d == 0:
            fac.add(d)
            m //= d
        d += 1
    if m > 1:
        fac.add(m)
    for c in range(2, p):
        if all(pow(c, (p - 1) // q, p) != 1 for q in fac):
            return c


def setup(p):
    gam = primitive_root(p)
    ind = np.full(p, -1, dtype=np.int64)
    pw = np.empty(p - 1, dtype=np.int64)
    z = 1
    for i in range(p - 1):
        ind[z] = i
        pw[i] = z
        z = z * gam % p
    return ind, pw


def law(kind, n, m):
    nu = np.zeros(n)
    if kind == "flat":
        S = rng.choice(np.arange(1, n), size=m, replace=False)
    elif kind == "dtheta":
        L = int(round(m / 0.25))
        S = 1 + rng.choice(np.arange(L), size=m, replace=False)
    elif kind == "interval":
        S = np.arange(1, m + 1)
    nu[S] = 1.0 / m
    return nu


def g_on_field(p, ind, nu):
    n = (p - 1) // 2
    fQ = n * np.fft.ifft(nu)              # f(gamma^(2k)) = sum_j nu_j e(jk/n)
    fF = np.zeros(p, dtype=complex)
    for z in range(1, p):
        if ind[z] % 2 == 0:
            fF[z] = fQ[ind[z] // 2]
    return fQ, fF


def partA(p, kind, levels):
    n = (p - 1) // 2
    ind, pw = setup(p)
    m = int(round(n / np.sqrt(p)))
    nu = law(kind, n, m)
    fQ, fF = g_on_field(p, ind, nu)
    gF = np.abs(fF) ** 2
    G = gF.sum()
    sq = np.sqrt(p)
    z = np.arange(1, p)
    A = z
    vert = (ind[A] % 2 == 0) & (ind[(1 - A) % p] % 2 == 0) & ((1 - A) % p != 0)
    Gv = gF[A][vert].sum()
    out = {"G/sqrtp": G / sq, "Gvert/sqrtp": Gv / sq,
           "sumg2/sqrtp": (gF ** 2).sum() / sq}
    for a in levels:
        mass = gF[A][vert & (gF[A] < a)].sum()
        out[f"m<{a}/sqrtp"] = mass / sq
    # X = sum_{kappa in Q\{1}} c_h(kappa)^2 via cyclic correlation on F_p^x.
    H = np.array([gF[(1 - pw[i]) % p] for i in range(p - 1)])
    FH = np.fft.fft(H)
    c = np.real(np.fft.ifft(np.conj(FH) * FH))     # c[d] = sum_i H[i] H[i+d]
    X = sum(c[d] ** 2 for d in range(2, p - 1, 2))
    out["X/p"] = X / p
    return out


def moment_parts(p, ind, nu, fQ, fF, v, cut):
    """Return M_nu(F_cut), Abs, P (completed, by slope index), norms."""
    n = (p - 1) // 2
    inv = np.zeros(p, dtype=np.int64)
    for z in range(1, p):
        inv[z] = pow(z, -1, p)
    Qel = np.array([z for z in range(1, p) if ind[z] % 2 == 0])
    allx = np.arange(p)
    gF = np.abs(fF) ** 2
    Fphys = np.zeros(p, dtype=complex)          # F(x) = f(1 - v x), x in Q
    Fphys[Qel] = fF[(1 - v * Qel) % p]
    keep = np.zeros(p, dtype=bool)
    keep[Qel] = gF[(1 - v * Qel) % p] >= cut
    Fc = np.where(keep, Fphys, 0)
    M = 0.0
    Abs = 0.0
    P = np.zeros(n)
    absf = np.abs(fQ)
    for u in Qel:
        if u == 1:
            continue
        # physical row
        ux = u * Qel % p
        a_u = Fc[ux] * np.conj(Fc[Qel])
        Ax = (1 - v * Qel) % p
        Cx = (1 - v * ux) % p
        nz = (a_u != 0)
        B = np.zeros(n, dtype=complex)
        if nz.any():
            r = Cx[nz] * inv[Ax[nz]] % p
            k = ind[r] // 2
            assert len(np.unique(k)) == len(k)      # r_u injective (R152:50)
            B[k] = a_u[nz]
        FB = np.fft.fft(B)                           # C_a(u) for every anchor a
        M += np.dot(nu, np.abs(FB) ** 2)
        aB = np.abs(B)
        FA = np.fft.fft(aB)
        R = np.real(np.fft.ifft(np.conj(FA) * FA))   # R[d] = sum_k |B_k||B_k+d|
        Abs += np.dot(absf[1:], R[1:])
        # completed g-majorant (all x in F_p, square masks completed)
        A2 = (1 - v * allx) % p
        C2 = (1 - v * u * allx) % p
        wgt = gF[A2] * gF[C2]
        ok = wgt > 0
        Bg = np.zeros(n)
        if ok.any():
            r2 = C2[ok] * inv[A2[ok]] % p
            k2 = ind[r2] // 2
            np.add.at(Bg, k2, wgt[ok])
        FG = np.fft.fft(Bg)
        P += np.real(np.fft.ifft(np.conj(FG) * FG))
    normF2 = np.sum(np.abs(Fc) ** 2)
    return M, Abs, P, normF2


def partB(p, kind, cut):
    n = (p - 1) // 2
    ind, pw = setup(p)
    m = int(round(n / np.sqrt(p)))
    nu = law(kind, n, m)
    fQ, fF = g_on_field(p, ind, nu)
    gQ = np.abs(fQ) ** 2
    v = 1
    M, Abs, P, nF2 = moment_parts(p, ind, nu, fQ, fF, v, 0.0)
    Mc, _, Pc, nG2 = moment_parts(p, ind, nu, fQ, fF, v, cut)
    Xm = P[1:].sum()                                  # X - diag
    Mw = np.dot(gQ[1:] * (1 - gQ[1:]), P[1:])
    Ms = np.dot(np.sqrt(gQ[1:]), P[1:])
    Xc = Pc[1:].sum()                                  # level-restricted X - diag
    E2 = nF2 - nG2                                     # hard cut: ||F - F_>=a||^2
    lhs1 = np.sqrt(M)
    rhs1 = np.sqrt(Mc) + 2 * np.sqrt(n * nu.max()) * np.sqrt(nF2) * np.sqrt(E2)
    rhs2 = nG2 ** 2 + Xc / cut ** 2
    return {"M/p": M / p, "Abs/p": Abs / p, "Abs/p^1.75": Abs / p ** 1.75,
            "(X-diag)/p": Xm / p, "Mw/p": Mw / p, "Msqrt/p": Ms / p,
            "M(F>=a)/p": Mc / p, "m<a": E2, "||F||^2/sqrtp": nF2 / np.sqrt(p),
            "R160 ok": bool(lhs1 <= rhs1 + 1e-9), "Prop1 ok": bool(Mc <= rhs2 + 1e-9)}


if __name__ == "__main__":
    levels = [0.5, 0.2, 0.05, 0.01]
    print("Part A: vertex mass below fixed levels (fractions of sqrt p) and X/p")
    for p in [10009, 40009, 160001]:
        assert is_prime(p) and p % 4 == 1
        for kind in ["flat", "dtheta", "interval"]:
            out = partA(p, kind, levels)
            print(f"p={p:7d} {kind:8s} " +
                  " ".join(f"{k}={v:.3f}" for k, v in out.items()))
    print()
    print("Part B: moment, absolute majorant, slope masses; cut level a = 0.1")
    for p in [401, 797, 1601, 3209]:
        assert is_prime(p) and p % 4 == 1
        for kind in ["flat", "dtheta", "interval"]:
            out = partB(p, kind, 0.1)
            print(f"p={p:5d} {kind:8s} " +
                  " ".join(f"{k}={v:.3f}" if isinstance(v, float) else f"{k}={v}"
                           for k, v in out.items()))
