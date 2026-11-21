#!/usr/bin/env python3
r"""Round 188 (ordinary-prime-beyond-point-plane): identity checks and models.

Modes
  --check            exact integer checks at small primes (any g >= 0 on Q,
                     inversion-symmetric where stated), plus floating checks of
                     the character identities (tolerance stated).
  P [P ...]          floating-point flat-law models g = |f|^2 at the primes P
                     (p = 1 mod 4).  Evidence about models only.

Conventions (Rounds 169-187, counting norms).
  mu(r,b) = g(Y) g(D) on Y != D in F_p \ {0,1}, r = (Y-D)/(1-D),
  b = D(1-Y)/(Y(1-D)), square mask b in Q.  j_(r,b)(e) = r e + b.
  F_mu v(s) = sum_(r,b) mu(r,b) v((s-b)/r);  kernel K[s,x] = sum_r M[r, s-rx].
  Delta(lam,beta) = sum mu(r,b) mu(lam r, b + r beta)  (h: x -> lam x + beta).
  m(r) = row (slope) mass, m'(b) = horizontal (intercept) mass.
  h(z) = g(1-z), c_h(k) = sum_z h(z) h(k z), X = sum_r m(r)^2.
  h_t(e) = g(t/e) (e != 0), phi_t = h_t - G/p, w = g(1-g).
  T := sum_lam c_g(lam) Delta(lam,0)   (Theorem A quantity).
"""
import sys
import numpy as np


def prim_root(p):
    fac = []
    q, d = p - 1, 2
    while d * d <= q:
        if q % d == 0:
            fac.append(d)
            while q % d == 0:
                q //= d
        d += 1
    if q > 1:
        fac.append(q)
    for a in range(2, p):
        if all(pow(a, (p - 1) // f, p) != 1 for f in fac):
            return a
    raise ValueError


def setup(p):
    th = prim_root(p)
    pw = np.zeros(p - 1, dtype=np.int64)
    x = 1
    for m in range(p - 1):
        pw[m] = x
        x = x * th % p
    dlog = np.zeros(p, dtype=np.int64)
    dlog[pw] = np.arange(p - 1)
    inv = np.zeros(p, dtype=np.int64)
    for a in range(1, p):
        inv[a] = pow(a, p - 2, p)
    isq = np.zeros(p, dtype=bool)
    isq[pw[0::2]] = True
    return th, pw, dlog, inv, isq


def build_mu(p, g, inv, isq, dtype=float):
    """M[r-1, b] = sum of g(Y)g(D) over admissible pairs."""
    M = np.zeros((p - 1, p), dtype=dtype)
    supp = np.array([y for y in range(2, p) if g[y] != 0], dtype=np.int64)
    Y = np.repeat(supp, len(supp))
    D = np.tile(supp, len(supp))
    keep = Y != D
    Y, D = Y[keep], D[keep]
    r = (Y - D) % p * inv[(1 - D) % p] % p
    b = D * (1 - Y) % p * inv[Y * (1 - D) % p] % p
    keep = isq[b]
    Y, D, r, b = Y[keep], D[keep], r[keep], b[keep]
    np.add.at(M, (r - 1, b), (g[Y] * g[D]).astype(dtype))
    return M


def mult_corr(v, p, dlog, pw):
    """c_v(lam) = sum_x v(x) v(lam x) for lam in F_p^*, via FFT on the log group."""
    a = v[pw].astype(float)
    A = np.fft.fft(a)
    c = np.fft.ifft(np.conj(A) * A).real  # c[k] = sum_m a[m] a[m+k]
    out = np.zeros(p)
    out[pw] = c
    return out


def delta_table(M, p):
    """D[lam, beta] for lam in 1..p-1 (row lam), beta in 0..p-1 (floating, FFT)."""
    F = np.fft.fft(M, axis=1)
    rr = np.arange(1, p)
    beta = np.arange(p)
    idx = (rr[:, None] * beta[None, :]) % p
    out = np.zeros((p, p))
    for lam in range(1, p):
        perm = (lam * rr) % p - 1
        corr = np.fft.ifft(np.conj(F) * F[perm], axis=1).real
        out[lam] = corr[rr[:, None] - 1, idx].sum(axis=0)
    return out


def delta_table_exact(M, p):
    out = np.zeros((p, p), dtype=object)
    rr = np.arange(1, p)
    bb = np.arange(p)
    for lam in range(1, p):
        for beta in range(p):
            r2 = (lam * rr) % p - 1
            b2 = (bb[None, :] + rr[:, None] * beta) % p
            out[lam, beta] = int((M * M[r2[:, None], b2]).sum())
    return out


def kernel(M, p):
    K = np.zeros((p, p))
    s = np.arange(p)
    for r in range(1, p):
        row = M[r - 1]
        if not row.any():
            continue
        K += row[(s[:, None] - r * s[None, :]) % p]
    return K


# ---------------------------------------------------------------- exact checks
def exact_checks():
    ok = True
    rng = np.random.default_rng(188)
    for p in (13, 17, 29, 37):
        th, pw, dlog, inv, isq = setup(p)
        for trial in range(2):
            g = np.zeros(p, dtype=np.int64)
            for y in pw[0::2]:
                y = int(y)
                if g[y] == 0 and y != 1:
                    v = int(rng.integers(0, 4))
                    g[y] = v
                    g[inv[y]] = v  # inversion symmetry g(1/x) = g(x)
            g[1] = 3
            M = build_mu(p, g, inv, isq, dtype=np.int64)
            Dl = delta_table_exact(M, p)
            m = M.sum(axis=1)
            mprime = M.sum(axis=0)
            M1 = int(m.sum())
            c = int((M * M).sum())
            X = int((m * m).sum())
            Lam0 = int((mprime * mprime).sum())
            C = {lam: sum(int(m[r - 1]) * int(m[(lam * r) % p - 1]) for r in range(1, p))
                 for lam in range(1, p)}
            E = sum(int(Dl[l, b]) ** 2 for l in range(1, p) for b in range(p))
            # (I1) fibre sums
            i1 = all(sum(int(Dl[l, b]) for b in range(p)) == C[l] for l in range(1, p))
            # (I2) Delta <= c, E <= c X + sum_{lam != 1} C D
            maxD = max(int(Dl[l, b]) for l in range(1, p) for b in range(p))
            Dlam = {l: max(int(Dl[l, b]) for b in range(p)) for l in range(1, p)}
            bound = c * X + sum(C[l] * Dlam[l] for l in range(2, p))
            i2 = (maxD == c == int(Dl[1, 0])) and E <= bound and E <= c * M1 * M1
            # (I3) m'(b) = c_h(b) on Q\{1}, m(r) = c_h(1-r) on 1-r in Q\{1}, Lam0 = X
            h = np.zeros(p, dtype=np.int64)
            for z in range(1, p):
                h[z] = g[(1 - z) % p]
            ch = {k: sum(int(h[z]) * int(h[(k * z) % p]) for z in range(1, p)) for k in range(1, p)}
            i3a = all(int(mprime[b]) == (ch[b] if (isq[b] and b != 1) else 0) for b in range(1, p)) \
                and int(mprime[0]) == 0
            i3b = all(int(m[r - 1]) == (ch[(1 - r) % p] if (isq[(1 - r) % p] and r != 0) else 0)
                      for r in range(1, p) if (1 - r) % p != 0)
            i3 = i3a and i3b and Lam0 == X
            # trace identity p E = tr((K K^T)^2) - M1^4 + E^x(m)
            K = np.zeros((p, p), dtype=object)
            for r in range(1, p):
                for b in range(p):
                    if M[r - 1, b]:
                        for x in range(p):
                            K[(r * x + b) % p, x] += int(M[r - 1, b])
            KK = K.dot(K.T)
            tr2 = sum(KK[i, j] * KK[j, i] for i in range(p) for j in range(p))
            Exm = sum(v * v for v in C.values())
            i4 = (p * E == tr2 - M1 ** 4 + Exm)
            flag = i1 and i2 and i3 and i4
            ok &= flag
            print(f"p={p} trial={trial}: fibre sums {i1}; Delta<=c and E<=cX+sum C D {i2}; "
                  f"m'=c_h, m=c_h(1-.), Lam0=X {i3}; trace identity {i4}")
    # floating checks of the character identities on g = |f|^2 (tolerance 1e-8 relative)
    for p in (29, 37, 53):
        th, pw, dlog, inv, isq = setup(p)
        n = (p - 1) // 2
        rng2 = np.random.default_rng(p)
        nu = rng2.random(n)
        nu /= nu.sum()
        g = law_to_g(p, nu, pw)
        M = build_mu(p, g, inv, isq)
        K = kernel(M, p)
        m = M.sum(axis=1)
        # omega on characters of F_p^*: g(theta^k) = sum_a omega_a e(a k/(p-1))
        om = np.fft.fft(g[pw]) / (p - 1)
        err_om = np.abs(om.imag).max() + max(0.0, -om.real.min())
        om = om.real
        worst = 0.0
        # ||K chi||^2 = p S0(chi) - |m^(chi)|^2 for every nontrivial chi
        for a in range(1, p - 1):
            chi = np.zeros(p, dtype=complex)
            chi[pw] = np.exp(2j * np.pi * a * np.arange(p - 1) / (p - 1))
            lhs = np.linalg.norm(K @ chi) ** 2
            A = (M * np.conj(chi[1:])[:, None]).sum(axis=0)
            S0 = (np.abs(A) ** 2).sum()
            mh = (m * np.conj(chi[1:])).sum()
            rhs = p * S0 - abs(mh) ** 2
            worst = max(worst, abs(lhs - rhs) / max(1.0, abs(lhs)))
        # sum_t ||K phi_t||^2 = (p-1) sum_{a!=0} om_a^2 ||K chi_-a||^2 + (p-1) om_0^2 ||pi(d0-1/p)||^2
        G = g.sum()
        H0 = np.zeros((p, p - 1))
        for ti, t in enumerate(range(1, p)):
            H0[1:, ti] = g[(t * inv[1:]) % p]
        Phi = H0 - G / p
        lhs2 = (np.abs(K @ Phi) ** 2).sum()
        rhs2 = 0.0
        for a in range(1, p - 1):
            chi = np.zeros(p, dtype=complex)
            chi[pw] = np.exp(-2j * np.pi * a * np.arange(p - 1) / (p - 1))
            rhs2 += (p - 1) * om[a] ** 2 * np.linalg.norm(K @ chi) ** 2
        d0 = -np.full(p, 1.0 / p)
        d0[0] += 1.0
        rhs2 += (p - 1) * om[0] ** 2 * np.linalg.norm(K @ d0) ** 2
        rel2 = abs(lhs2 - rhs2) / lhs2
        # T = sum_lam c_g(lam) Delta(lam,0) and sum_t ||K phi_t||^2 <= p T
        cg = mult_corr(g, p, dlog, pw)
        D0 = np.array([0.0] + [(M * M[(lam * np.arange(1, p)) % p - 1]).sum() for lam in range(1, p)])
        T = (cg[1:] * D0[1:]).sum()
        # (p-1) sum_a om_a^2 S0(chi_-a) = T
        T2 = 0.0
        for a in range(0, p - 1):
            chi = np.zeros(p, dtype=complex)
            chi[pw] = np.exp(-2j * np.pi * a * np.arange(p - 1) / (p - 1))
            A = (M * np.conj(chi[1:])[:, None]).sum(axis=0)
            T2 += (p - 1) * om[a] ** 2 * (np.abs(A) ** 2).sum()
        relT = abs(T - T2) / T
        # uniform in t: ||K phi_t||^2 <= p T0, T0 = sum_lam g(lam) Delta(lam,0) <= X
        T0 = (g[1:] * D0[1:]).sum()
        Xv = (m * m).sum()
        flt = (np.abs(K @ Phi) ** 2).sum(axis=0)
        unif = flt.max() / (p * T0)
        flag = (worst < 1e-8 and rel2 < 1e-8 and relT < 1e-8 and lhs2 <= p * T * (1 + 1e-12)
                and err_om < 1e-12 and unif <= 1 + 1e-12 and T0 <= Xv * (1 + 1e-12))
        print(f"p={p} (float): max_t ||K phi_t||^2 / (p T0) = {unif:.4f}; T0/X = {T0 / Xv:.4f}")
        ok &= flag
        print(f"p={p} (float): omega real >= 0 (err {err_om:.1e}); ||K chi||^2 = p S0 - |m^|^2 (max rel err {worst:.1e}); "
              f"t-sum identity (rel err {rel2:.1e}); T two ways (rel err {relT:.1e}); "
              f"sum_t ||K phi_t||^2 / (p T) = {lhs2 / (p * T):.4f}")
    print("ALL CHECKS OK" if ok else "SOME CHECK FAILED")
    return ok


# ---------------------------------------------------------------- models
def law_to_g(p, nu, pw):
    n = (p - 1) // 2
    f = n * np.fft.ifft(nu)  # f(theta^(2i)) = sum_j nu_j e(j i / n)
    g = np.zeros(p)
    g[pw[0::2]] = np.abs(f) ** 2
    g[1] = 1.0
    return np.minimum(g, 1.0)


def sector_g(p, inv, isq, rng):
    """Not of the form |f|^2: g = 1/2 on a random inversion-closed subset B of the
    sector T_+ = {x in Q, x != 1, chi(1-x) = 1}, |B| ~ 2 sqrt p, g(1) = 1.  It has
    sector concentration (M_1 ~ G^2 ~ p) and w = 1/4 on B.  Theorem A applies to any
    0 <= g <= 1 on Q; Lam0 = X uses only g(1/x) = g(x)."""
    T = [x for x in range(2, p) if isq[x] and isq[(1 - x) % p] and x <= inv[x]]
    k = min(len(T), int(round(np.sqrt(p))))
    B = rng.choice(np.array(T), size=k, replace=False)
    g = np.zeros(p)
    g[B] = 0.5
    g[inv[B]] = 0.5
    g[1] = 1.0
    return g


def model_law(p, kind, rng):
    n = (p - 1) // 2
    m0 = max(2, int(round(n / np.sqrt(p))))
    if kind == "rand":
        S = rng.choice(n, size=m0, replace=False)
    elif kind == "interval":
        S = np.arange(m0)
    elif kind == "halfint":
        S = rng.choice(2 * m0, size=m0, replace=False)
    elif kind == "sumset":  # A + A for a random A of size ~ sqrt(m0): mid energy
        k = max(2, int(round(np.sqrt(m0))))
        A = rng.choice(n, size=k, replace=False)
        S = np.unique((A[:, None] + A[None, :]) % n)
    else:
        raise ValueError(kind)
    nu = np.zeros(n)
    nu[S] = 1.0
    return nu / nu.sum()


def run_model(p, kind, seed=0, full_delta=True):
    th, pw, dlog, inv, isq = setup(p)
    rng = np.random.default_rng(1000 * p + seed + sum(map(ord, kind)))
    if kind == "sector":
        g = sector_g(p, inv, isq, rng)
    else:
        nu = model_law(p, kind, rng)
        g = law_to_g(p, nu, pw)
    G = g.sum()
    Gam = (g ** 2).sum()
    w = g * (1 - g)
    M = build_mu(p, g, inv, isq)
    m = M.sum(axis=1)
    mprime = M.sum(axis=0)
    M1 = m.sum()
    c = (M * M).sum()
    X = (m * m).sum()
    Lam0 = (mprime * mprime).sum()
    h = np.zeros(p)
    h[1:] = g[(1 - np.arange(1, p)) % p]
    ch = mult_corr(h, p, dlog, pw)
    Exh = (ch[1:] ** 2).sum()
    cg = mult_corr(g, p, dlog, pw)
    Lstar = cg[2:].max()
    # slope autocorrelation C(lam) and E^x(m)
    mm = np.zeros(p)
    mm[1:] = m
    C = mult_corr(mm, p, dlog, pw)
    Exm = (C[1:] ** 2).sum()
    out = dict(p=p, kind=kind, G=G, Gam=Gam, W=w.sum(), M1=M1, c=c, X=X, Lam0=Lam0, Exh=Exh,
               Lstar=Lstar, supC=C[2:].max())
    D0 = np.array([0.0] + [(M * M[(lam * np.arange(1, p)) % p - 1]).sum() for lam in range(1, p)])
    out["T"] = (cg[1:] * D0[1:]).sum()
    out["T0"] = (g[1:] * D0[1:]).sum()
    if full_delta:
        Dl = delta_table(M, p)
        E = (Dl[1:] ** 2).sum()
        E1 = (Dl[1] ** 2).sum()
        Dlam = Dl[2:].max(axis=1)
        out.update(E=E, E1=E1, Eneq1=E - E1, maxD=Dlam.max(),
                   fibvar=E - Exm / p,
                   boundB=c * X + (C[2:] * Dlam).sum())
    K = kernel(M, p)
    KK = K @ K.T
    tr2 = (KK * KK).sum()
    out["E_trace"] = (tr2 - M1 ** 4 + Exm) / p
    P = np.eye(p) - 1.0 / p
    out["pi2"] = np.linalg.norm(P @ K @ P, 2) ** 2
    H0 = np.zeros((p, p - 1))
    tt = np.arange(1, p)
    for ti, t in enumerate(tt):
        H0[1:, ti] = g[(t * inv[1:]) % p]
    Phi = H0 - G / p
    fl = (np.abs(K @ Phi) ** 2).sum(axis=0)
    wt = w[tt]
    phin = (Phi ** 2).sum(axis=0)
    out["fluct_w"] = (wt * fl).sum()
    out["fluct_all"] = fl.sum()
    out["fluct_max"] = fl.max()
    out["mean_w"] = wt.sum() * M1 ** 2 * G ** 2 / p
    out["op_bound"] = out["pi2"] * (wt * phin).sum()
    out["E_bound"] = np.sqrt(p * out["E_trace"] - Exm) * (wt * phin).sum()
    out["ch_bound"] = 0.25 * p * out["T"]
    out["thA_bound"] = 0.25 * p * Gam * X
    return out


KINDS = ("rand", "halfint", "sumset", "interval", "sector")


def main(argv):
    if not argv or argv[0] == "--check":
        ok = exact_checks()
        return 0 if ok else 1
    full = "--nodelta" not in argv
    primes = [int(a) for a in argv if not a.startswith("--")]
    print("Floating-point models (flat laws on S in Z/n, |S| ~ n/sqrt p); evidence about models only.")
    for p in primes:
        for kind in KINDS:
            o = run_model(p, kind, full_delta=full)
            sp = np.sqrt(p)
            line = (f"p={p:5d} {kind:8s} G/sp={o['G']/sp:.3f} Gam/sp={o['Gam']/sp:.3f} W/sp={o['W']/sp:.3f} "
                    f"M1/p={o['M1']/p:.3f} c/p={o['c']/p:.3f} X/p={o['X']/p:.3f} Lam0/X={o['Lam0']/o['X']:.6f} "
                    f"Exh/p={o['Exh']/p:.3f} L*/Gam={o['Lstar']/o['Gam']:.3f} supC/p={o['supC']/p:.3f} "
                    f"E/p2={o['E_trace']/p**2:.3f}")
            if full:
                line += (f" E1/p2={o['E1']/p**2:.3f} Eneq1/p2={o['Eneq1']/p**2:.3f} maxD={o['maxD']:.2f} "
                         f"Bbound/E={o['boundB']/o['E']:.2f} |E-Etr|/E={abs(o['E']-o['E_trace'])/o['E']:.1e}")
            print(line)
            print(f"        pi2/p^1.5={o['pi2']/p**1.5:.3f} T/p^1.5={o['T']/p**1.5:.4f} T/(Gam X)={o['T']/(o['Gam']*o['X']):.3f} | "
                  f"weighted fluct/p^2.5={o['fluct_w']/p**2.5:.4f} mean/p^2.5={o['mean_w']/p**2.5:.4f} "
                  f"ratios to fluct: op={o['op_bound']/o['fluct_w']:.1f} E-op={o['E_bound']/o['fluct_w']:.1f} "
                  f"ch(pT/4)={o['ch_bound']/o['fluct_w']:.2f} thmA={o['thA_bound']/o['fluct_w']:.2f} "
                  f"all-t fluct/(pT)={o['fluct_all']/(p*o['T']):.3f} | max_t fluct/(p T0)={o['fluct_max']/(p*o['T0']):.3f} "
                  f"T0/X={o['T0']/o['X']:.3f} T0/c={o['T0']/o['c']:.3f} W*T0/(Gam X/4)={o['W']*o['T0']/(o['Gam']*o['X']/4):.3f}")
            sys.stdout.flush()
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
