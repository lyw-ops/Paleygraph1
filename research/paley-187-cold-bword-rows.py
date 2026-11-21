#!/usr/bin/env python3
"""Round 187 cold call `cold-prime-b-word-delocalization`: FLOATING physical rows (evidence only, label (c)).

Own implementation (no import of earlier scripts).  For each prime p = 1 (mod 4), n = (p-1)/2:

  * K = real symmetric circulant on Z/n with eigenvalues chi(1 - g^(2j)) (Rounds 96/180/186 convention);
    the physical row coordinate i is the square-subgroup character psi_i(g^(2j)) = e(ij/n).
  * Nine-centre start (Rounds 57-65 as recorded in astra-joint-65.md, astra-legendre-63.md, astra-joint-64.md,
    astra-ranknext-58.md, weighted-arithmetic-57.md), built from its physical fields:
        V_0 = S + alpha Y + beta W + gamma F_4 + delta G + z R + w Q + v (U + U'),
    with x = sqrt(n) K e_0, S = 2x, c = sqrt(q/n), C_1 = S/s_p,
        y = K(x^2),  Y = 2(y + x/sqrt n)/c^2,
        z' = K(x y), W = (2/c^3)(z' + y/sqrt n) - C_1/q,
        w' = K(x z'), F_4 = (2/c^4)(w' - y/(2n) + z'/sqrt n) + D_4 K e_0,  D_4 = n(1+q)/(2q^2)  [h_q dropped],
        G = -K(C_1 F_4)                                                     [bounded D_q K e_0 dropped],
        A_i, B_i = signed Legendre traces at the two lifts of psi_i (Mellin transform of u = l.(l*l), l(a) = chi(1-a),
                   on F_p^x, divided by q),  R = K(A B),  Q = K(A^2 + B^2 - 2) + (4n(q+1)/q^2) K e_0,
        U + U' = K(2 T_4(C_1)) - 2(1 - 8/q + 7/q^2) K e_0.
    Amplitudes at the real floor t = a = 2031/128: (alpha, beta, gamma, delta) from
    research/astra-primitive-62-check.py `coefficients()` (Arb, radius < 5e-13; midpoints used here),
    z = 1.701367523e-3 (Round 63), w = 8.50649424e-4 (Round 64), v = -9.00249249e-4 (Round 65).
    The two dropped exceptional constants change coordinates by O(n^(-1/2)) only.
  * Exact map V_{h+1} = K Phi_t(V_h), Phi_t(x) = sqrt(4t + x^2) principal branch, mark t_0 = n at i = 0.
    Increments R_h = V_{h+1} - V_h are propagated as (log scale, unit direction) with the stable secant
    Phi(V+R) - Phi(V) = R(2V+R)/(Phi(V+R)+Phi(V)); below double precision this is the tangent map.
  * At height 602: frozen L = K Phi'(V_602), L_S = K Phi'(S), B = L - L_S.
    Measured: ratio sup_good/RMS (good = i != 0) of
        R_{602+k} (= L^k r_602 up to relative O(||R_602||)), k < k_n = ceil((4/7) log2 n),
        the single-B words w_{a,b} = L^b B L_S^a r_602, a + b + 1 <= k_n,
        the B-generated part L^k r - L_S^k r, and the seed part L_S^k r,
    with normalized even moments and tail counts.  Controls: iid Gaussian vectors, the nine-centre fields,
    and growing-height words L_S^m S, L^m S.

Nothing here is a certified bound.  Usage:
  .venv/bin/python -B research/paley-187-cold-bword-rows.py OUT.jsonl p1 p2 ...   [--t a|corner] [--start nine|seed]
"""
import json
import sys
import time

import numpy as np
import scipy.fft as sf

WORKERS = 8
A_T = 2031 / 128
AMP = dict(alpha=0.243408316565, beta=0.082584064225, gamma=0.0279615357329, delta=-0.0094859449111,
           z=1.701367523e-3, w=8.50649424e-4, v=-9.00249249e-4)


def factor(m):
    f, d = [], 2
    while d * d <= m:
        if m % d == 0:
            f.append(d)
            while m % d == 0:
                m //= d
        d += 1
    if m > 1:
        f.append(m)
    return f


def prim_root(p):
    fac = factor(p - 1)
    g = 2
    while any(pow(g, (p - 1) // f, p) == 1 for f in fac):
        g += 1
    return g


def legendre_of_one_minus_powers(g, N, p, chunk=1 << 21):
    """ell[k] = chi(1 - g^k), k < N, as int8 (exact values -1, 0, 1), by Euler's criterion in int64."""
    out = np.empty(N, dtype=np.int8)
    B = 4096
    b = np.empty(B, dtype=np.int64)
    x = 1
    for j in range(B):
        b[j] = x
        x = x * g % p
    gB = pow(g, B, p)
    e_half = (p - 1) // 2
    for s in range(0, N, chunk):
        e = min(chunk, N - s)
        pw = np.empty(e, dtype=np.int64)
        blk = pow(g, s, p)
        for t0 in range(0, e, B):
            m = min(B, e - t0)
            pw[t0:t0 + m] = (b[:m] * blk) % p
            blk = blk * gB % p
        z = (1 - pw) % p
        del pw
        res = np.ones(e, dtype=np.int64)
        base = z.copy()
        ee = e_half
        while ee:
            if ee & 1:
                res = (res * base) % p
            base = (base * base) % p
            ee >>= 1
        o = np.where(res == 1, 1, -1).astype(np.int8)
        o[z == 0] = 0
        out[s:s + e] = o
        del z, res, base, o
    return out


class Phys:
    """Physical Paley operator on Z/n.  ell (int8, length 2n) is kept only until the Legendre traces are built."""

    def __init__(self, p):
        self.p = p
        self.n = n = (p - 1) // 2
        self.g = prim_root(p)
        self.ell = legendre_of_one_minus_powers(self.g, 2 * n, p)
        self.lam = self.ell[0::2].astype(np.float64)
        self.lam_r = self.lam[: n // 2 + 1].copy()

    def K(self, v):
        if np.iscomplexobj(v):
            return self.K(v.real) + 1j * self.K(v.imag)
        X = sf.rfft(v, workers=WORKERS)
        X *= self.lam_r
        return sf.irfft(X, self.n, workers=WORKERS, overwrite_x=True)

    def legendre_traces(self):
        """A_i, B_i: Mellin transform of u = ell.(ell*ell) on F_p^x (cyclic of order 2n, written in log
        coordinates k <-> g^k) at the two lifts m = i, i + n of the square-subgroup character psi_i, divided
        by q.  Computed with even/odd splitting so that every FFT has length n.  Returns (A, B, max |Im|)."""
        n, q = self.n, self.p
        e = self.ell[0::2].astype(np.float64)
        o = self.ell[1::2].astype(np.float64)
        E = sf.rfft(e, workers=WORKERS)
        O = sf.rfft(o, workers=WORKERS)
        ce = sf.irfft(E * E, n, workers=WORKERS)                      # (e*e)_j
        ce += np.roll(sf.irfft(O * O, n, workers=WORKERS), 1)          # + (o*o)_(j-1)
        co = sf.irfft(E * O, n, workers=WORKERS)                      # (e*o)_j
        co *= 2.0
        del E, O
        ce *= e                                                        # u at even k = 2j
        co *= o                                                        # u at odd k = 2j+1
        del e, o
        # F(m) = sum_k u_k e(mk/2n) = Ehat(m) + e(m/2n) Ohat(m),  Ehat(m) = sum_j u_2j e(mj/n)
        Ue = sf.rfft(ce, workers=WORKERS)
        del ce
        Uo = sf.rfft(co, workers=WORKERS)
        del co
        i = np.arange(n)
        jj = np.minimum(i, n - i)
        sgn = np.where(i <= n // 2, -1.0, 1.0)                          # Im Ehat(i) = sgn * Im rfft[jj]
        reE = Ue.real[jj]
        imE = sgn * Ue.imag[jj]
        del Ue
        reO = Uo.real[jj]
        imO = sgn * Uo.imag[jj]
        del Uo, jj, sgn
        ang = np.pi * i / n
        del i
        cs, sn = np.cos(ang), np.sin(ang)
        del ang
        tr = cs * reO - sn * imO                                       # Re(e(i/2n) Ohat)
        ti = sn * reO + cs * imO                                       # Im(e(i/2n) Ohat)
        del cs, sn, reO, imO
        A = (reE + tr) / q
        B = (reE - tr) / q
        imag = float(max(np.abs(imE + ti).max(), np.abs(imE - ti).max())) / q
        return A, B, imag


def stats(f, good, full=False, chunk=1 << 22):
    """sup over good coordinates / RMS over all coordinates; optional normalized even moments and tail counts.
    Chunked to keep the memory footprint at a few arrays of length chunk."""
    n = len(f)
    ss, sup, arg = 0.0, -1.0, -1
    for s0 in range(0, n, chunk):
        a = np.abs(f[s0:s0 + chunk])
        ss += float(np.dot(a, a))
        ag = np.where(good[s0:s0 + chunk], a, -1.0)
        j = int(np.argmax(ag))
        if ag[j] > sup:
            sup, arg = float(ag[j]), s0 + j
    rms = float(np.sqrt(ss / n))
    out = dict(ratio=sup / rms, rms=rms, sup=sup, arg=arg)
    if full:
        mom = np.zeros(9)
        ths = (2, 3, 4, 4.5, 5, 5.5, 6, 7)
        cnt = np.zeros(len(ths), dtype=np.int64)
        ng = 0
        for s0 in range(0, n, chunk):
            z = np.abs(f[s0:s0 + chunk])[good[s0:s0 + chunk]] / rms
            ng += len(z)
            z2 = z * z
            acc = np.ones_like(z2)
            for k in range(1, 9):
                acc *= z2
                mom[k] += float(acc.sum())
            for i, th in enumerate(ths):
                cnt[i] += int(np.count_nonzero(z > th))
        out['moments'] = {2 * k: mom[k] / ng for k in range(1, 9)}
        out['tail'] = {str(th): int(cnt[i]) for i, th in enumerate(ths)}
    return out


def gauss_max_median(n):
    """median of max_{i<n} |Z_i| for iid N(0,1): solve (2 Phi(x) - 1)^n = 1/2 (erfc form)."""
    from math import erfc, log, sqrt
    lo, hi = 0.0, 12.0
    for _ in range(200):
        mid = (lo + hi) / 2
        # log((1 - erfc(mid/sqrt2))^n)
        val = n * np.log1p(-erfc(mid / sqrt(2)))
        if val < log(0.5):
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def run(p, out, tmode='a', start='nine', height=602):
    T0 = time.time()
    P = Phys(p)
    n, q = P.n, p
    K = P.K
    rec = dict(p=p, n=n, g=P.g, tmode=tmode, start=start, height=height)
    if tmode == 'a':
        t = A_T
    else:
        sr, si = {'pp': (1, 1), 'pm': (1, -1), 'mp': (-1, 1), 'mm': (-1, -1)}[tmode]
        t = complex(A_T + sr * 2.0 ** -17, si * 2.0 ** -17)
    cplx = isinstance(t, complex)
    rec['t'] = str(t)
    e0 = np.zeros(n)
    e0[0] = 1.0
    Ke0 = K(e0)
    del e0
    S = 2 * np.sqrt(n) * Ke0
    c = np.sqrt(q / n)
    sp = 2 * c
    rec['sanity'] = dict(sum_lam=float(P.lam.sum()), sqrtn_S0=float(np.sqrt(n) * S[0]),
                         sumS2_over_4nm1=float(np.dot(S, S) / (4 * (n - 1))), maxS=float(np.abs(S).max()), s_p=sp)
    good = np.ones(n, dtype=bool)
    good[0] = False
    fields = {}
    V0 = S.copy()
    rsn = 1 / np.sqrt(n)

    def add(nm, f, amp):
        fields[nm] = stats(f, good, full=True)
        V0.__iadd__(amp * f)

    if start == 'nine':
        # Legendre centres first (they need the full-group row ell, then ell is dropped)
        A, Bv, imag = P.legendre_traces()
        P.ell = None
        rec['legendre_imag_max'] = imag
        rec['legendre_meanA2'] = float(np.mean(A[1:] ** 2))
        R = K(A * Bv)
        add('R', R, AMP['z'])
        del R
        A *= A
        Bv *= Bv
        A += Bv
        del Bv
        A -= 2.0
        Q = K(A)
        del A
        Q += (4 * n * (q + 1) / q ** 2) * Ke0
        add('Q', Q, AMP['w'])
        del Q
        C1 = S / sp
        T4 = 8 * C1 ** 4 - 8 * C1 ** 2 + 1
        UU = K(2 * T4)
        del T4
        UU -= 2 * (1 - 8 / q + 7 / q ** 2) * Ke0
        add('UU', UU, AMP['v'])
        del UU
        x = S / 2
        y = K(x * x)
        Y = 2 * (y + x * rsn) / c ** 2
        add('Y', Y, AMP['alpha'])
        del Y
        zz = K(x * y)
        W = (2 / c ** 3) * (zz + y * rsn) - C1 / q
        add('W', W, AMP['beta'])
        del W
        ww = K(x * zz)
        del x
        D4 = n * (1 + q) / (2 * q * q)
        F4 = (2 / c ** 4) * (ww - y / (2 * n) + zz * rsn) + D4 * Ke0
        del y, zz, ww
        add('F4', F4, AMP['gamma'])
        G = K(C1 * F4)
        del F4
        G *= -1.0
        add('G', G, AMP['delta'])
        del G, C1
        fields['S'] = stats(S, good, full=True)
    P.ell = None
    del Ke0
    rec['fields'] = fields
    dv = V0 - S
    rec['V0'] = dict(sup_minus_S=float(np.abs(dv)[good].max()), rms_minus_S=float(np.sqrt(np.mean(dv ** 2))))
    del dv
    four_t = 4 * t
    four_n = 4.0 * n

    def Phi(v):
        o = np.sqrt(four_t + v * v)
        o[0] = np.sqrt(four_n + v[0] * v[0])
        return o

    def dPhi(v):
        o = v / np.sqrt(four_t + v * v)
        o[0] = v[0] / np.sqrt(four_n + v[0] * v[0])
        return o

    if cplx:
        V0 = V0.astype(complex)
    # h = 0 increment, computed directly
    V = V0
    del V0
    r = K(Phi(V))
    r -= V
    sig = float(np.sqrt(np.vdot(r, r).real / n))
    logsig = np.log10(sig)
    r /= sig
    logs = {0: float(logsig)}
    rates = []
    Dfix = None
    for h in range(height):
        s = 10.0 ** logsig if logsig > -300 else 0.0
        if s * float(np.abs(r).max()) > 1e-17 * float(np.abs(V).max()):
            Vn = V + s * r
            d = Phi(Vn)
            d += Phi(V)
            np.divide(V + Vn, d, out=d)
            d *= r
            V = Vn
            del Vn
        else:
            # below double precision the secant equals the tangent at the (numerically fixed) row
            if Dfix is None:
                Dfix = dPhi(V)
            d = Dfix * r
        Rn = K(d)
        del d
        nr = float(np.sqrt(np.vdot(Rn, Rn).real / n))
        rates.append(nr)
        logsig += np.log10(nr)
        Rn /= nr
        r = Rn
        del Rn
        if (h + 1) in (1, 2, 5, 10, 20, 50, 100, 200, 300, 400, 500, 600, 602) or h + 1 == height:
            logs[h + 1] = float(logsig)
    del Dfix
    rec['log10_sigma'] = logs
    rec['rate_last100_geomean'] = float(np.exp(np.mean(np.log(rates[-100:]))))
    rec['rate_first10'] = [float(x_) for x_ in rates[:10]]
    # frozen operators at the final row; keep h = V - S, D = Phi'(V), DB = Phi'(V) - Phi'(S)
    D = dPhi(V)
    Sc = S.astype(complex) if cplx else S
    hvec = V - Sc
    del V
    rec['V602_minus_S'] = dict(sup=float(np.abs(hvec)[good].max()), rms=float(np.sqrt(np.mean(np.abs(hvec) ** 2))))
    DB = D - dPhi(Sc)
    rec['DB'] = dict(sup=float(np.abs(DB)[good].max()), rms=float(np.sqrt(np.mean(np.abs(DB) ** 2))))

    def L(f):
        return K(D * f)

    def LS(f):
        w_ = D * f
        w_ -= DB * f
        return K(w_)

    def Bop(f):
        return K(DB * f)

    kn = int(np.ceil((4 / 7) * np.log2(n)))
    rec['k_n'] = kn
    full_k = {0, 1, 2, 5, kn - 1}
    # R_{602+k} ~ L^k r and its seed / B parts
    Rk, seed_k, bpart_k = [], [], []
    f = r.copy()
    fs = r.copy()
    for k in range(kn):
        Rk.append(stats(f, good, full=(k in full_k)))
        seed_k.append(stats(fs, good))
        if k >= 1:
            diff = f - fs
            bpart_k.append(stats(diff, good, full=(k in full_k)))
            del diff
        f = L(f)
        fs = LS(fs)
    rec['R_602_plus_k'] = Rk
    rec['seed_part_k'] = seed_k
    rec['B_part_k'] = bpart_k
    rec['Lambda_gamma1'] = max(x_['ratio'] for x_ in Rk)
    del f, fs
    # single-B words w_{a,b} = L^b B L_S^a r
    words = {}
    fa = r.copy()
    for a in range(kn):
        g_ = Bop(fa)
        for b in range(kn - a):
            words[f'{a},{b}'] = stats(g_, good, full=(a in (0, 3) and b in (0, 3, kn - 1 - a)))
            if b < kn - a - 1:
                g_ = L(g_)
        fa = LS(fa)
    rec['words'] = words
    rec['words_max_ratio'] = max(v_['ratio'] for v_ in words.values())
    del fa, g_
    # controls
    rng = np.random.default_rng(p)
    gs = []
    for _ in range(3):
        gv = rng.standard_normal(n)
        gs.append(stats(gv, good)['ratio'])
        del gv
    rec['gauss_iid_ratio'] = gs
    rec['gauss_max_median'] = gauss_max_median(n - 1)
    grow = {'LS^m S': [], 'L^m S': [], 'L^m h': []}
    rec['h_stats'] = stats(hvec, good, full=True)
    for key, f1, op in (('LS^m S', Sc, LS), ('L^m S', Sc, L), ('L^m h', hvec, L)):
        f1 = f1.copy()
        for m in range(0, 25):
            grow[key].append(stats(f1, good)['ratio'])
            f1 = op(f1)
        del f1
    rec['height_growth'] = grow
    rec['seconds'] = time.time() - T0
    with open(out, 'a') as fh:
        fh.write(json.dumps(rec) + '\n')
    print(f'[float] p={p} n={n} t={tmode} start={start}: ratio(R602)={Rk[0]["ratio"]:.3f} '
          f'ratio(B r)={words["0,0"]["ratio"]:.3f} gauss_med={rec["gauss_max_median"]:.3f} '
          f'rate={rec["rate_last100_geomean"]:.4f} log10 sigma_end={logsig:.1f} ({rec["seconds"]:.0f}s)', flush=True)


if __name__ == '__main__':
    args = sys.argv[1:]
    tmode, start, height = 'a', 'nine', 602
    if '--t' in args:
        i = args.index('--t')
        tmode = args[i + 1]
        del args[i:i + 2]
    if '--start' in args:
        i = args.index('--start')
        start = args[i + 1]
        del args[i:i + 2]
    if '--height' in args:
        i = args.index('--height')
        height = int(args[i + 1])
        del args[i:i + 2]
    out = args[0]
    for p in map(int, args[1:]):
        run(p, out, tmode, start, height)
