#!/usr/bin/env python3
r"""Round 183 (call ordinary-prime-row-deleted-one-match): exact row-deleted cubic trace by word type.

Objects (Rounds 169/171/178/182, counting norms):
  g >= 0 on the squares Q (here: 0/1 integer model weights, optionally divided by an integer k),
  chart  r=(Y-D)/(1-D), b=D(1-Y)/(Y(1-D)), Y,D in F_p\{0,1}, Y != D, mask b in Q,
  mu(r,b)=g(Y)g(D),  j_{Y,D}(e)=r e+b,  fixed point fix(j)=D/Y,
  K(y,x)=sum_{j x=y} mu(j),  F F^* = K K^T = sum_h Delta(h) U_h,  Delta(h)=sum_{j j'^{-1}=h} mu(j)mu(j').
  pi = F restricted to 1^perp;  A_R = R pi pi^* R  (R deletes outputs s=0,1),
  A_full = pi pi^*.   tr(A_full^3) = p T_3 - T_3^x(m)  (Round 182, accepted).

Two-letter quotient types (each factor j j'^{-1} of the six-word j1 j2^-1 j3 j4^-1 j5 j6^-1):
  I : j = j'                       (coinciding letters)
  S : slope(j)=slope(j'), j != j'  (common slope: the quotient is a nonzero translation)
  P : fix(j)=fix(j'),   j != j'    (common fixed point D/Y: the quotient fixes it)
  G : otherwise                    (generic: distinct slopes and distinct fixed points)
(S and P are disjoint: slope and fixed point determine j.)  Delta = Delta_I+Delta_S+Delta_P+Delta_G and
pi(Delta) = sum_tau pi(Delta_tau), where pi(Delta_tau) = P M_tau P with M_tau = sum_h Delta_tau(h) U_h
(each M_tau has constant row/column sums r_tau, so pi(Delta_tau) = M_tau - (r_tau/p) J on 1^perp).
Hence, exactly,
  tr(A^3) = sum_{a,b,c in {I,S,P,G}} tr( R N_a R N_b R N_c ) / p^3,   N_tau = p M_tau - r_tau J (integer).
For the full operator (no R) term (a,b,c) equals sum over words whose three quotients have types a,b,c of
  (p*[h1h2h3 = id] - [slope(h1h2h3)=1]) * weight,
i.e. the type-split translation discrepancy of slope-closed six-words.  The row-deleted version is the
same sum with the three intermediate points restricted to s not in {0,1}.

All traces are exact integers (int64 matrix products with digit-split exact trace reductions); the
spectral norms printed are floating (numpy eigvalsh), labelled as such.

Usage:  .venv/bin/python -B research/paley-183-rowdel-trace.py [--check] [p ...]
  --check : exactness checks at p=29,37,41 against the Round 182 group-convolution identity
            (imports research/paley-182-opnorm-identities.py) and sum_tau M_tau = K K^T.
"""
import sys
import math
import random
import importlib.util
from fractions import Fraction
import numpy as np

TYPES = 'ISPG'


def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def primroot(p):
    fac = []
    n = p - 1
    d = 2
    while d * d <= n:
        if n % d == 0:
            fac.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        fac.append(n)
    for g in range(2, p):
        if all(pow(g, (p - 1) // q, p) != 1 for q in fac):
            return g


# ----------------------------------------------------------------------------- models
def sector(p, rho):
    """T_rho = {x in Q \\ {1}: chi(1-x) = rho}."""
    return [x for x in range(2, p) if legendre(x, p) == 1 and legendre(1 - x, p) == rho]


def model(p, kind, rho, seed=0):
    """Return (g as int list, k) with actual weights g/k.  Sector models live in T_rho."""
    rng = random.Random(1000 * p + 17 * seed + (0 if rho == 1 else 7) + sum(map(ord, kind)))
    q = int(round(math.sqrt(p)))
    T = sector(p, rho)
    Tset = set(T)
    g = [0] * p
    k = 1
    if kind == 'rand':
        B = rng.sample(T, q)
    elif kind == 'spread4':
        B = rng.sample(T, min(4 * q, (3 * len(T)) // 4))
        k = 4
    elif kind == 'interval':
        B = [x for x in range(2, p) if x in Tset][:q]
    elif kind == 'logint':
        th = primroot(p)
        B = []
        x = 1
        for _ in range(p):
            x = x * th * th % p
            if x in Tset:
                B.append(x)
            if len(B) >= q:
                break
    elif kind == 'coset':
        n = (p - 1) // 2
        th = primroot(p)
        divs = [d for d in range(2, n + 1) if n % d == 0]
        d = min(divs, key=lambda d: abs(d - q))
        gen = pow(th, 2 * (n // d), p)          # generator of the order-d subgroup H of Q
        H = [pow(gen, i, p) for i in range(d)]
        reps = list(range(n // d))
        rng.shuffle(reps)
        B = []
        for c in reps:
            a = pow(th, 2 * c, p)
            B += [a * h % p for h in H if a * h % p in Tset]
            if len(B) >= q:
                break
    elif kind == 'randQ':                        # balanced control (not sector-concentrated)
        Q = [x for x in range(2, p) if legendre(x, p) == 1]
        B = rng.sample(Q, q)
    else:
        raise ValueError(kind)
    for x in B:
        g[x] = 1
    return g, k


# ----------------------------------------------------------------------------- chart
def chart(p, g):
    inv = lambda z: pow(z, p - 2, p)
    letters = []   # (r, b, fix, weight)
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
            letters.append((r, b, D * inv(Y) % p, g[Y] * g[D]))
    return letters


def deltas(p, letters):
    """Delta_tau(h) for h = j j'^{-1} = (r/r', b - r b'/r'), split by quotient type."""
    inv = [0] + [pow(z, p - 2, p) for z in range(1, p)]
    D = {t: {} for t in TYPES}
    for (r, b, z, w) in letters:
        for (r2, b2, z2, w2) in letters:
            if (r, b) == (r2, b2):
                t = 'I'
            elif r == r2:
                t = 'S'
            elif z == z2:
                t = 'P'
            else:
                t = 'G'
            a = r * inv[r2] % p
            c = (b - r * b2 * inv[r2]) % p
            d = D[t]
            d[(a, c)] = d.get((a, c), 0) + w * w2
    return D


def dense(p, dct):
    """M = sum_h w_h U_h as p x p int64 matrix; (U_h f)(s) = f(h^{-1}s), entry M[h s', s'] += w."""
    M = np.zeros((p, p), dtype=np.int64)
    ar = np.arange(p)
    for (a, c), w in dct.items():
        M[(a * ar + c) % p, ar] += w
    return M


def kernel(p, letters):
    K = np.zeros((p, p), dtype=np.int64)
    ar = np.arange(p)
    for (r, b, z, w) in letters:
        K[(r * ar + b) % p, ar] += w
    return K


def exact_trace(X, Z):
    """sum_{i,j} X_ij Z_ji exactly (X int64 up to ~2^62, |Z| < 2^31)."""
    Zt = Z.T
    B = 1 << 21
    tot = 0
    rem = X.copy()
    shift = 0
    for _ in range(3):
        dgt = rem % B           # in [0, B)
        rem = (rem - dgt) // B
        tot += int(np.einsum('ij,ij->i', dgt, Zt).astype(object).sum()) << shift
        shift += 21
    # remaining high part
    tot += int(np.einsum('ij,ij->i', rem, Zt).astype(object).sum()) << shift
    return tot


def analyse(p, g, k=1, verbose=True, want_eigs=True):
    letters = chart(p, g)
    Dl = deltas(p, letters)
    Ms = {t: dense(p, Dl[t]) for t in TYPES}
    rs = {t: int(sum(Dl[t].values())) for t in TYPES}
    M1 = sum(w for (_, _, _, w) in letters)
    assert sum(rs.values()) == M1 * M1
    Ns = {t: p * Ms[t] - rs[t] for t in TYPES}   # integer, = p * pi(Delta_tau) on 1^perp
    out = {}
    for label, sl in (('R', slice(2, p)), ('full', slice(0, p))):
        Nt = {t: np.ascontiguousarray(Ns[t][sl, sl]) for t in TYPES}
        assert max(int(np.abs(v).max()) for v in Nt.values()) < (1 << 31)
        prod = {(a, b): Nt[a] @ Nt[b] for a in TYPES for b in TYPES}
        tri = {}
        for a in TYPES:
            for b in TYPES:
                for c in TYPES:
                    tri[(a, b, c)] = exact_trace(prod[(a, b)], Nt[c])
        tot = sum(tri.values())
        # tr(A), tr(A^2) exactly
        Ntot = sum(Nt.values())
        t1 = int(sum(int(v) for v in np.diag(Ntot)))
        t2 = exact_trace(Ntot, Ntot)
        den = k ** 4
        out[label] = dict(tri=tri, tr3=Fraction(tot, p ** 3 * den ** 3), tr2=Fraction(t2, p ** 2 * den ** 2),
                          tr1=Fraction(t1, p * den))
        nd = Ntot.shape[0]
        out[label]['var'] = out[label]['tr2'] - out[label]['tr1'] ** 2 / nd   # sum (a_i - mean)^2, exact
        if want_eigs:
            fl = lambda X: X.astype(np.float64) / (p * den)
            ev = np.linalg.eigvalsh(fl(Ntot))
            out[label]['norm'] = math.sqrt(max(ev.max(), 0.0))
            # floating class norms: generic class, common-slope (+I) class, common-fixed-point (+I) class
            out[label]['nG'] = float(np.abs(np.linalg.eigvalsh(fl(Nt['G']))).max())
            out[label]['nIS'] = float(np.abs(np.linalg.eigvalsh(fl(Nt['I'] + Nt['S']))).max())
            out[label]['nIP'] = float(np.abs(np.linalg.eigvalsh(fl(Nt['I'] + Nt['P']))).max())
    # exact scalar inputs: affine energy E(mu)=sum_h Delta(h)^2, slope-row mass sum_r m(r)^2,
    # fixed-point-class mass sum_z L_z^2
    allh = {}
    for t in TYPES:
        for h, w in Dl[t].items():
            allh[h] = allh.get(h, 0) + w
    mr, Lz = {}, {}
    for (r, b, z, w) in letters:
        mr[r] = mr.get(r, 0) + w
        Lz[z] = Lz.get(z, 0) + w
    out['Emu'] = Fraction(sum(w * w for w in allh.values()), k ** 8)
    out['Sm2'] = Fraction(sum(w * w for w in mr.values()), k ** 4)
    out['SL2'] = Fraction(sum(w * w for w in Lz.values()), k ** 4)
    G = Fraction(sum(g), k)
    S2 = Fraction(sum(x * x for x in g), k * k)
    out['G'] = G
    out['S2'] = S2
    out['M1'] = Fraction(M1, k * k)
    out['mu2'] = Fraction(sum(w * w for (_, _, _, w) in letters), k ** 4)
    out['rs'] = {t: Fraction(rs[t], k ** 4) for t in TYPES}
    out['den'] = k ** 4
    return out, letters, Ms


def classes(tri):
    """Group ordered type patterns (a,b,c) by multiset."""
    agg = {}
    for key, v in tri.items():
        m = ''.join(sorted(key, key=TYPES.index))
        agg[m] = agg.get(m, 0) + v
    return agg


def run_check():
    spec = importlib.util.spec_from_file_location('r182', 'research/paley-182-opnorm-identities.py')
    r182 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(r182)
    for p in (29, 37, 41):
        for seed in (0, 1):
            rng = random.Random(seed)
            g = [0] * p
            for x in range(2, p):
                if legendre(x, p) == 1 and rng.random() < 0.6:
                    g[x] = rng.randint(1, 3)
            out, letters, Ms = analyse(p, g, want_eigs=False)
            K = kernel(p, letters)
            assert (sum(Ms.values()) == K @ K.T).all(), 'sum_tau M_tau != K K^T'
            # independent: p T_3 - T_3^x via Round 182 group convolutions
            mu, _ = r182.chart(p, g)
            inv = lambda z: pow(z, p - 2, p)
            mut = {(inv(r), (-b * inv(r)) % p): w for (r, b), w in mu.items()}
            nu1 = r182.group_conv(mu, mut, p)
            nu3 = r182.group_conv(r182.group_conv(nu1, nu1, p), nu1, p)
            T3 = nu3.get((1, 0), 0)
            T3x = sum(w for (a, c), w in nu3.items() if a == 1)
            assert out['full']['tr3'] == p * T3 - T3x, (p, seed)
            # the full type split: (a,b,c) term = sum over typed words of (p[id]-[slope 1]) weight
            Dl = deltas(p, letters)
            for (a, b, c), v in list(out['full']['tri'].items())[::7]:
                w3 = r182.group_conv(r182.group_conv(Dl[a], Dl[b], p), Dl[c], p)
                val = p * w3.get((1, 0), 0) - sum(w for (aa, cc), w in w3.items() if aa == 1)
                assert Fraction(v, p ** 3) == val, (p, seed, a, b, c)
            # R-deleted vs dense direct computation
            Kf = K.astype(object)
            FF = Kf.dot(Kf.T)
            A = [[Fraction(int(FF[i][j])) - Fraction(out['M1'] ** 2, p) for j in range(2, p)] for i in range(2, p)]
            n = p - 2
            A2 = [[sum(A[i][l] * A[l][j] for l in range(n)) for j in range(n)] for i in range(n)]
            tr3 = sum(A2[i][l] * A[l][i] for i in range(n) for l in range(n))
            assert tr3 == out['R']['tr3'], (p, seed)
            print(f'p={p} seed={seed}: type split sums to K K^T; full tr3 = pT3 - T3x; R tr3 = direct: OK')
    print('all exact checks passed')


def main(argv):
    if '--check' in argv:
        run_check()
        return
    ps = [int(a) for a in argv if a.isdigit()] or [101, 197, 401, 577, 677]
    kinds = [a[7:] for a in argv if a.startswith('--kind=')]
    kinds = kinds[0].split(',') if kinds else ['rand', 'coset', 'logint', 'interval', 'spread4', 'randQ']
    rhos = (1, -1)
    for p in ps:
        for kind in kinds:
            for rho in (rhos if kind != 'randQ' else (0,)):
                g, k = model(p, kind, rho if rho else 1)
                out, letters, _ = analyse(p, g, k)
                R, F = out['R'], out['full']
                s = lambda x: float(x)
                print(f'p={p} model={kind} rho={rho:+d} |B|={sum(1 for x in g if x)} k={k} '
                      f'G={s(out["G"]):.2f} S2={s(out["S2"]):.2f} M1/p={s(out["M1"]) / p:.4f} '
                      f'mu2={s(out["mu2"]):.1f}')
                print(f'   tr3_R/p^4.5={s(R["tr3"]) / p ** 4.5:.5f}  tr3_R/p^4={s(R["tr3"]) / p ** 4:.4f}  '
                      f'tr3_full/p^4.5={s(F["tr3"]) / p ** 4.5:.5f}  '
                      f'HS_R/p^2={s(R["tr1"]) / p ** 2:.4f}  tr2_R/p^3={s(R["tr2"]) / p ** 3:.4f}  '
                      f'[float] sigR/sqrtp={R["norm"] / math.sqrt(p):.3f} sig1/p^.75={F["norm"] / p ** 0.75:.3f}')
                print(f'   exact: E(mu)/p^2={s(out["Emu"]) / p ** 2:.4f}  sum m^2/p={s(out["Sm2"]) / p:.4f}  '
                      f'sum L_z^2/p^1.5={s(out["SL2"]) / p ** 1.5:.4f}  mu2/p={s(out["mu2"]) / p:.4f}  '
                      f'var_R/p^3.5={s(R["var"]) / p ** 3.5:.4f}  '
                      f'[float] ||R pi(D_G) R||/p^1.5={R["nG"] / p ** 1.5:.4f}  ||pi(D_G)||/p^1.5={F["nG"] / p ** 1.5:.4f}  '
                      f'||pi(D_IS)||/p={F["nIS"] / p:.4f}  ||pi(D_IP)||/p={F["nIP"] / p:.4f}')
                for label, D in (('R', R), ('full', F)):
                    agg = classes(D['tri'])
                    den = p ** 3 * out['den'] ** 3
                    items = sorted(agg.items(), key=lambda kv: -abs(kv[1]))
                    txt = '  '.join(f'{m}:{agg[m] / den / p ** 4.5:+.4f}' for m, _ in items[:10])
                    print(f'   [{label}] class/p^4.5  {txt}')
                sys.stdout.flush()


if __name__ == '__main__':
    main(sys.argv[1:])
