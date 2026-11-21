#!/usr/bin/env python3
"""Round 184 audit: independent finite checks of the two ordinary reports.

Written by the Round 184 auditor; shares no code with paley-184-rowmass-*.py or paley-184-energy-*.py.
Float64 (identities are checked to 1e-9 relative); exact integers where noted.  Evidence only.

  SE1  Proposition 1: g^(a) = n lambda_a, sum g^2 / G = sum_a lambda_a q_a  (random laws).
  SE0  Lemma 0 identity: <e, rho K e> = 1 - (2 G_{-rho} + 1)/G for every law.
  SE2  Theorem 2, finite form of its proof: for every flat S, sign rho and shift a,
         m^2[(1-r)(2r-1) - d_rho(S)] <= m0 <1_{S\\U}, rho K 1_U> <= m0 m sqrt(1-r) ||rho K u_S - u_S||.
  SE4  Proposition 4.2 identity: sum_{y in B} g(y) = b sum_D nu(D)^2, B = H^perp.
  SRM-Y  Lemma Y chain X <= R_* M_1 <= Gamma_2 M_1 <= (G-1)^2 Gamma_2, Gamma_2 = n E(nu) - 1,
         and the Cauchy-Schwarz floors of Proposition 2 (without the (NC) value of M_1).
  SRM-4  Proposition 4 (evidence): E^x(1_Y)/(p log p) for Y = (1-B)\\{0}, B a subgroup of order ~ sqrt p.
  SRM-5  Proposition 5: square control in F_{r^2} rebuilt from the Fourier sum (exact integers for X etc.).
Replay:  .venv/bin/python -B research/paley-184-audit-ordinary-check.py   (about 1-2 min)
"""
import math
import numpy as np

rng = np.random.default_rng(18401)


def prim_root(p):
    fac, m, d = [], p - 1, 2
    while d * d <= m:
        if m % d == 0:
            fac.append(d)
            while m % d == 0:
                m //= d
        d += 1
    if m > 1:
        fac.append(m)
    for gg in range(2, p):
        if all(pow(gg, (p - 1) // q, p) != 1 for q in fac):
            return gg


class Field:
    """F_p, p = 1 mod 4: Q = <w^2> = {w^(2t)}, characters psi^j(w^(2t)) = e(jt/n)."""

    def __init__(self, p):
        self.p, self.n = p, (p - 1) // 2
        w = prim_root(p)
        self.log = np.zeros(p, dtype=np.int64)
        x = 1
        for e in range(p - 1):
            self.log[x] = e
            x = x * w % p
        self.Qel = np.array([pow(w, 2 * t, p) for t in range(self.n)])     # index t -> element
        self.chi = np.zeros(p, dtype=np.int64)
        self.chi[1:] = np.where(self.log[1:] % 2 == 0, 1, -1)
        # s(t) = chi(1 - x_t) on Q, k(d) = p^(-1/2) sum_t s(t) e(d t / n)
        self.s = self.chi[(1 - self.Qel) % p]
        self.k = np.real(np.fft.fft(self.s)) / math.sqrt(p)   # sum_t s(t) e(-d t/n); s symmetric so real
        self.m0 = self.n / math.sqrt(p)

    def g_of_law(self, nu):
        f = np.fft.ifft(nu) * self.n          # f(t) = sum_j nu_j e(jt/n)
        return np.abs(f) ** 2


def check_se(p):
    F = Field(p)
    n = F.n
    ok = True
    for trial in range(3):
        b = rng.random(n) * (rng.random(n) < 0.2)
        b[0] = 0
        nu = b / b.sum()
        g = F.g_of_law(nu)
        G = g.sum()
        lam = np.real(np.fft.ifft(np.abs(np.fft.fft(nu)) ** 2))     # lambda_a = sum_j nu_j nu_{j+a}
        ghat = np.real(np.fft.fft(g))                                 # sum_t g(t) e(-a t/n)
        q = lam / lam[0]
        ok &= np.allclose(ghat, n * lam, rtol=1e-9, atol=1e-9)
        ok &= abs((g ** 2).sum() / G - (lam * q).sum()) <= 1e-9 * G
        ok &= abs(q.sum() - 1 / (nu ** 2).sum()) <= 1e-8 * q.sum()
        # Lemma 0 identity for both signs
        e = nu / np.linalg.norm(nu)
        Ke = np.real(np.fft.ifft(np.fft.fft(e) * np.fft.fft(F.k))) / F.m0      # (K e)_i = sum_j k(i-j) e_j / m0
        for rho in (1, -1):
            Gm = g[F.s == -rho].sum()
            ok &= abs(rho * e @ Ke - (1 - (2 * Gm + 1) / G)) <= 1e-9
        # Prop 4.2 identity, a subgroup H of Z/n of order h | n, B = H^perp = {t : t*(n/h)... }
        for h in [d for d in range(2, 60) if n % d == 0][:3]:
            H = np.arange(0, n, n // h)                   # subgroup of order h in Z/n
            Bt = np.arange(0, n, h)                       # t with e(j t/n) = 1 for all j in H: t in (n/(n/h)) Z... = h Z
            assert np.allclose(np.exp(2j * np.pi * np.outer(H, Bt) / n), 1)
            cos_mass = np.array([nu[(c + H) % n].sum() for c in range(n // h)])
            ok &= abs(g[Bt].sum() - len(Bt) * (cos_mass ** 2).sum()) <= 1e-9 * G
    # Theorem 2, finite form, on flat sets
    worst = -math.inf
    for trial in range(6):
        m = int(round(F.m0)) + rng.integers(-2, 3)
        if trial % 2 == 0:
            S = rng.choice(n, size=m, replace=False)
        else:   # half of a coset-like / progression set, to get large overlaps
            step = int(rng.integers(1, n))
            S = np.unique((step * np.arange(2 * m)) % n)[rng.permutation(2 * m)[:m]]
            S = np.unique(np.concatenate([S, (S + n // 2) % n]))[:m]
        S = np.unique(S)
        m = len(S)
        one = np.zeros(n); one[S] = 1
        for rho in (1, -1):
            uS = one / math.sqrt(m)
            KuS = np.real(np.fft.ifft(np.fft.fft(uS) * np.fft.fft(F.k))) / F.m0
            err = np.linalg.norm(rho * KuS - uS)
            dd = (1 - rho * F.k[(S[:, None] - S[None, :]) % n]).sum() / m ** 2
            for a in range(n):
                U = (S + a) % n
                oneU = np.zeros(n); oneU[U] = 1
                r = (one * oneU).sum() / m
                KoneU = np.real(np.fft.ifft(np.fft.fft(oneU) * np.fft.fft(F.k))) / F.m0
                mid = F.m0 * ((one * (1 - oneU)) @ (rho * KoneU))
                lo = m ** 2 * ((1 - r) * (2 * r - 1) - dd)
                hi = F.m0 * m * math.sqrt(max(1 - r, 0)) * err
                worst = max(worst, lo - mid, mid - hi)
    ok &= worst <= 1e-7 * F.m0 ** 2
    return ok, worst


for p in (101, 197, 389):
    ok, w = check_se(p)
    print(f"SE1/SE0/SE4/SE2 p={p}: identities and the finite Theorem 2 chain hold: {ok} (max violation {w:.2e})")


# ---------------------------------------------------------------- SRM Lemma Y and floors
def slope_rows(F, g_on_Q):
    p, n = F.p, F.n
    gF = np.zeros(p)
    gF[F.Qel] = g_on_Q                        # g on F_p, zero off Q (and at 0)
    z = np.arange(1, p)
    hz = gF[(1 - z) % p]                      # h(z) = g(1-z), z != 0
    hfull = np.zeros(p); hfull[1:] = hz
    # c_h(kappa) = sum_z h(z) h(kappa z), via multiplicative convolution on logs
    hl = np.zeros(p - 1); hl[F.log[1:]] = hz
    corr = np.real(np.fft.ifft(np.conj(np.fft.fft(hl)) * np.fft.fft(hl)))   # sum_e h(w^e) h(w^(e+d))
    c_h = np.zeros(p)
    elt = np.array([pow(prim_root(p), d, p) for d in range(p - 1)])
    c_h[elt] = corr
    # m(r) = c_h(1-r) for 1-r in Q \ {1}
    mrow = np.zeros(p)
    for kap in F.Qel:
        if kap != 1:
            mrow[(1 - kap) % p] = c_h[kap]
    return hfull, c_h, mrow, elt


def check_srm(p):
    F = Field(p)
    n = F.n
    ok = True
    for trial in range(3):
        b = rng.random(n) * (rng.random(n) < 0.15); b[0] = 0
        nu = b / b.sum()
        g = F.g_of_law(nu)
        G = g.sum()
        hfull, c_h, mrow, elt = slope_rows(F, g)
        Gam2 = (hfull ** 2).sum()
        ok &= abs(Gam2 - (n * (np.abs(np.fft.fft(nu)) ** 4).sum() / n - 1)) <= 1e-8 * max(1, Gam2)   # n E(nu) - 1
        ok &= abs(c_h[1] - Gam2) <= 1e-8 * Gam2
        M1, X = mrow.sum(), (mrow ** 2).sum()
        Qm1 = [k for k in F.Qel if k != 1]
        Rst = max(c_h[k] for k in Qm1)
        ok &= X <= Rst * M1 * (1 + 1e-12) and Rst <= Gam2 * (1 + 1e-12) and M1 <= (G - 1) ** 2 * (1 + 1e-12)
        # W_xi, C(lambda) via multiplicative correlations of m
        ml = np.zeros(p - 1); ml[F.log[1:]] = mrow[1:]
        fm = np.fft.fft(ml)
        W = np.real(np.fft.ifft(fm * fm))                 # sum m(r) m(xi/r): convolution on logs
        C = np.real(np.fft.ifft(np.conj(fm) * fm))        # sum m(r) m(lambda r)
        ok &= abs(W.sum() - M1 ** 2) <= 1e-8 * M1 ** 2 and abs(C[0] - X) <= 1e-8 * X
        ok &= X >= M1 ** 2 / (n - 1) * (1 - 1e-12)
        ok &= W.max() >= M1 ** 2 / (p - 1) * (1 - 1e-12)
        ok &= C[1:].max() >= (M1 ** 2 - X) / (p - 2) * (1 - 1e-12)
        ok &= W.max() <= X * (1 + 1e-12)
    return ok


for p in (101, 197, 293):
    print(f"SRM-Y p={p}: Lemma Y chain, Gamma_2 = n E(nu) - 1, sum W = M_1^2, C(1) = X, CS floors, max W <= X: {check_srm(p)}")


# ---------------------------------------------------------------- SRM Prop 4 (evidence)
def shifted_subgroup_energy(p, b):
    w = prim_root(p)
    gen = pow(w, (p - 1) // b, p)
    B = [pow(gen, t, p) for t in range(b)]
    Y = [(1 - x) % p for x in B if x != 1]
    log = {}
    x = 1
    for e in range(p - 1):
        log[x] = e
        x = x * w % p
    ly = np.array([log[y] for y in Y])
    diffs = (ly[:, None] - ly[None, :]) % (p - 1)
    cnt = np.bincount(diffs.ravel(), minlength=p - 1)
    return int((cnt.astype(np.int64) ** 2).sum()), len(Y)


print("SRM-4 (evidence) E^x((1-B)\\{0}) / (p log p) for subgroups B of order b ~ c sqrt p:")
def isprime(x):
    return x > 1 and all(x % d for d in range(2, int(x ** 0.5) + 1))


chosen = []
for target in (10 ** 4, 4 * 10 ** 4, 1.6 * 10 ** 5, 6.4 * 10 ** 5):
    p = int(target) + 1
    while not (isprime(p) and p % 4 == 1 and any((p - 1) % d == 0 for d in range(int(0.7 * math.sqrt(p)), int(1.5 * math.sqrt(p))))):
        p += 4 if p % 4 == 1 else 1
    chosen.append(p)
for p in chosen:
    divs = [d for d in range(int(0.5 * math.sqrt(p)), int(2 * math.sqrt(p)) + 1) if (p - 1) % d == 0 and ((p - 1) // d) % 2 == 0]
    row = []
    for b in divs[:3]:
        E, y = shifted_subgroup_energy(p, b)
        row.append(f"b={b} ({b/math.sqrt(p):.2f}sqrt p): E/(p log p)={E/(p*math.log(p)):.3f}, E/|Y|^2={E/y**2:.2f}")
    print(f"   p={p}: " + "; ".join(row))


# ---------------------------------------------------------------- SRM Prop 5 square control
def square_control(r):
    # F_{r^2} = F_r[i]/(i^2 - c), c a non-residue mod r
    c = next(a for a in range(2, r) if pow(a, (r - 1) // 2, r) == r - 1)
    q = r * r

    def mul(x, y):
        return ((x[0] * y[0] + c * x[1] * y[1]) % r, (x[0] * y[1] + x[1] * y[0]) % r)

    def pw(x, e):
        out, base = (1, 0), x
        while e:
            if e & 1:
                out = mul(out, base)
            base = mul(base, base)
            e >>= 1
        return out
    N = q - 1
    fac = [d for d in range(2, N + 1) if N % d == 0 and all(d % e for e in range(2, int(d ** 0.5) + 1))]
    gen = next((a, b) for a in range(r) for b in range(1, r) if all(pw((a, b), N // f) != (1, 0) for f in fac))
    els = [pw(gen, e) for e in range(N)]
    enc = lambda x: x[0] * r + x[1]
    log = np.zeros(q, dtype=np.int64)
    for e, x in enumerate(els):
        log[enc(x)] = e
    n = N // 2
    # Fourier sum: nu uniform on I \ {0}, I = {j : j (r+1)/2 = 0 mod n} = (r-1) Z/n
    I = [j for j in range(n) if (j * ((r + 1) // 2)) % n == 0]
    assert len(I) == (r + 1) // 2
    nu = np.zeros(n); nu[[j for j in I if j != 0]] = 1 / (len(I) - 1)
    f = np.fft.ifft(nu) * n
    g = np.abs(f) ** 2                                   # g on Q indexed by t: element w^(2t)
    gF = np.zeros(q)
    for t in range(n):
        gF[enc(els[2 * t])] = g[t]
    Fr_star = [enc((a, 0)) for a in range(1, r)]
    beta = 4 / (r - 1) ** 2
    ok = np.allclose(gF[Fr_star], 1) and np.allclose([gF[enc(els[2 * t])] for t in range(n) if (2 * t) % (r + 1) != 0], beta)
    G = gF.sum()
    # chi on F_q^*: (-1)^log
    one_minus = lambda x: ((1 - x[0]) % r, (-x[1]) % r)
    chi1m = np.array([0 if one_minus(els[2 * t]) == (0, 0) else (1 if log[enc(one_minus(els[2 * t]))] % 2 == 0 else -1)
                      for t in range(n)])
    Gm = g[chi1m == -1].sum()
    sgchi = (g * chi1m).sum()
    # slope rows: h(z) = g(1-z) on F_q^*, c_h(kappa) = sum_z h(z) h(kappa z)
    hl = np.zeros(N)
    for e, x in enumerate(els):
        hl[e] = gF[enc(one_minus(x))]
    corr = np.real(np.fft.ifft(np.conj(np.fft.fft(hl)) * np.fft.fft(hl)))   # c_h(w^d)
    mrow = np.zeros(N)                                   # indexed by log of r'
    for t in range(1, n):
        kap = els[2 * t]                                 # kappa in Q \ {1}
        rr = one_minus(kap)
        if rr != (0, 0):
            mrow[log[enc(rr)]] = corr[2 * t]
    X = (mrow ** 2).sum()
    fm = np.fft.fft(mrow)
    W = np.real(np.fft.ifft(fm * fm))
    C = np.real(np.fft.ifft(np.conj(fm) * fm))
    X0 = (r - 2) * (r - 3) ** 2
    return ok, G, Gm, sgchi / r, X / r ** 3, W.max() / r ** 3, C[1:].max() / r ** 3, X >= X0 - 1e-6, W.max() >= X0 - 1e-6, C[1:].max() >= (r - 3) ** 3 - 1e-6


print("SRM-5 square control in F_{r^2} (rebuilt from the Fourier sum):")
print("    r   g closed form   G (=r+1)   G_-     sum g chi(1-x)/sqrt q   X/q^1.5  maxW/q^1.5  supC/q^1.5  lower bounds hold")
for r in (5, 7, 11, 13, 17):
    ok, G, Gm, sg, Xn, Wn, Cn, b1, b2, b3 = square_control(r)
    print(f"   {r:2d}   {ok}            {G:8.4f}   {Gm:.3f}   {sg:.4f}                 {Xn:.4f}   {Wn:.4f}      {Cn:.4f}      {b1 and b2 and b3}")
print("AUDIT ORDINARY CHECK DONE (finite evidence; identities to float precision)")
