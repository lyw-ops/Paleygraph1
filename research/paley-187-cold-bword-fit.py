#!/usr/bin/env python3
"""Round 187 cold call `cold-prime-b-word-delocalization`: analysis of the FLOATING rows (evidence only, label (c)).

Reads the JSON lines written by research/paley-187-cold-bword-rows.py and prints:
  A. per-prime table: sup/RMS of R_602, of the first B-word B r_602, word mean / max, Lambda_n(gamma = 1),
     B-part mean, Gaussian controls and the Gaussian-max reference E_G(n) (expected max of n iid |N(0,1)|);
  B. growth-law fits over primes: bounded (X = c), X = a + b sqrt(2 ln n), X = E_G(n) + d, X = k E_G(n),
     with a bootstrap over primes for the slope b and the Gaussian reference slope b_G of E_G on sqrt(2 ln n);
  C. tail counts above thresholds against n P(|Z| > th) (Poisson z-scores), and normalized even moments;
  D. fixed-height fields (Y, W, F4, G, R, Q, U+U') and the height-growth curves L_S^m S;
  E. counting rates (seed part against the exact compact value l_S = 0.2400606, full increments);
  F. sensitivity to the start row and to the corners of Q (optional second file).
Usage: .venv/bin/python -B research/paley-187-cold-bword-fit.py MAIN.jsonl [SENS.jsonl]
"""
import json
import sys
from math import erfc, log, sqrt

import numpy as np
from scipy import integrate, special

L_S = 0.2400606


def load(path):
    out = []
    with open(path) as fh:
        for line in fh:
            out.append(json.loads(line))
    return out


def gauss_expected_max(n):
    """E max_{i<n} |Z_i| = int_0^inf (1 - erf(x/sqrt2)^n) dx."""
    f = lambda x: -np.expm1(n * np.log1p(-special.erfc(x / np.sqrt(2))))
    v, _ = integrate.quad(f, 0, 15, limit=400, points=[sqrt(2 * log(n))])
    return v


def gauss_sd_max(n):
    f2 = lambda x: 2 * x * (-np.expm1(n * np.log1p(-special.erfc(x / np.sqrt(2)))))
    m2, _ = integrate.quad(f2, 0, 15, limit=400, points=[sqrt(2 * log(n))])
    m = gauss_expected_max(n)
    return sqrt(max(m2 - m * m, 0.0))


def summarize(rows):
    tab = []
    for d in rows:
        n = d['n']
        ng = n - 1
        w = np.array([v['ratio'] for v in d['words'].values()])
        Rk = np.array([x['ratio'] for x in d['R_602_plus_k']])
        Bp = np.array([x['ratio'] for x in d['B_part_k']])
        # real rows are even (f_i = f_(n-i)): n/2 distinct good values; the iid control has n - 1
        tab.append(dict(p=d['p'], n=n, EG=gauss_expected_max(n // 2), SDG=gauss_sd_max(n // 2),
                        EGc=gauss_expected_max(ng), SDGc=gauss_sd_max(ng),
                        R0=Rk[0], Rmean=Rk.mean(), Lam=Rk.max(), Br=d['words']['0,0']['ratio'],
                        wmean=w.mean(), wmax=w.max(), wsd=w.std(ddof=1), nw=len(w), Bmean=Bp.mean(),
                        gauss=np.mean(d['gauss_iid_ratio']), kn=d['k_n']))
    return tab


def fit_all(x, y, sig):
    """weighted least squares for the four models; returns dict of (params, chi2, dof)."""
    s2 = np.sqrt(2 * np.log(x['n']))
    EG = x['EG']
    W = 1 / sig ** 2
    res = {}
    # bounded
    c = np.sum(W * y) / np.sum(W)
    res['bounded c'] = ((c,), float(np.sum(W * (y - c) ** 2)), len(y) - 1)
    # linear in sqrt(2 ln n)
    A = np.vstack([np.ones_like(s2), s2]).T
    Aw = A * np.sqrt(W)[:, None]
    coef, *_ = np.linalg.lstsq(Aw, y * np.sqrt(W), rcond=None)
    res['a + b sqrt(2ln n)'] = (tuple(coef), float(np.sum(W * (y - A @ coef) ** 2)), len(y) - 2)
    # Gaussian law + shift
    dsh = np.sum(W * (y - EG)) / np.sum(W)
    res['E_G(n) + d'] = ((dsh,), float(np.sum(W * (y - EG - dsh) ** 2)), len(y) - 1)
    # Gaussian law scaled
    kk = np.sum(W * y * EG) / np.sum(W * EG * EG)
    res['k E_G(n)'] = ((kk,), float(np.sum(W * (y - kk * EG) ** 2)), len(y) - 1)
    return res


def slope_boot(n, y, B=4000, seed=1):
    rng = np.random.default_rng(seed)
    s2 = np.sqrt(2 * np.log(n))
    bs = []
    for _ in range(B):
        idx = rng.integers(0, len(n), len(n))
        if np.ptp(s2[idx]) < 0.3:
            continue
        b = np.polyfit(s2[idx], y[idx], 1)[0]
        bs.append(b)
    bs = np.array(bs)
    return float(np.polyfit(s2, y, 1)[0]), float(np.percentile(bs, 2.5)), float(np.percentile(bs, 97.5))


def main():
    rows = [d for d in load(sys.argv[1]) if d['tmode'] == 'a' and d['start'] == 'nine']
    rows.sort(key=lambda d: d['n'])
    tab = summarize(rows)
    print('[float] A. per-prime table (t = a, nine-centre start, principal branch); ratio = sup_good / RMS')
    print('     p          n   k_n E_G(n/2) sd_G   R602   Br602  word-mean  word-max  Lambda(g=1)  Bpart-mean  gauss-ctl E_G(n-1)')
    for r in tab:
        print(f"{r['p']:>10d} {r['n']:>10d} {r['kn']:>4d} {r['EG']:7.3f} {r['SDG']:5.3f} {r['R0']:6.3f} {r['Br']:7.3f}"
              f" {r['wmean']:9.3f} {r['wmax']:9.3f} {r['Lam']:11.3f} {r['Bmean']:11.3f} {r['gauss']:9.3f} {r['EGc']:8.3f}")
    n = np.array([r['n'] for r in tab], dtype=float)
    X = dict(n=n, EG=np.array([r['EG'] for r in tab]))
    sdg = np.array([r['SDG'] for r in tab])
    print('\n[float] B. growth-law fits over primes (weights 1/sigma^2)')
    s2 = np.sqrt(2 * np.log(n))
    bG = np.polyfit(s2, X['EG'], 1)[0]
    print('  reference E_G = expected max of n/2 iid |N(0,1)| (the real rows are even: f_i = f_(n-i));'
          ' the iid control uses n - 1')
    print(f'  Gaussian reference: slope of E_G(n/2) on sqrt(2 ln n) over this n-range: b_G = {bG:.3f}')
    for key, sig_scale, label in (('R0', 1.0, 'R_602 (single vector)'),
                                  ('Br', 1.0, 'B r_602 (single vector)'),
                                  ('wmean', None, 'mean over all single-B words'),
                                  ('Rmean', None, 'mean over R_602+k, k < k_n'),
                                  ('Bmean', None, 'mean over B-parts of R_602+k'),
                                  ('gauss', 1 / sqrt(3), 'iid Gaussian control (mean of 3)')):
        y = np.array([r[key] for r in tab])
        Xc = X if key != 'gauss' else dict(n=n, EG=np.array([r['EGc'] for r in tab]))
        if key == 'gauss':
            sdg_ = np.array([r['SDGc'] for r in tab])
        else:
            sdg_ = sdg
        if sig_scale is None:
            # averages of correlated vectors: use the across-prime residual scatter about E_G as sigma (floor sd_G/4)
            resid = y - Xc['EG']
            sig = np.full_like(y, max(np.std(resid - np.mean(resid), ddof=1), 1e-3))
        else:
            sig = sdg_ * sig_scale
        fits = fit_all(Xc, y, sig)
        b, lo, hi = slope_boot(n, y)
        print(f'  {label}:')
        for k_, (par, chi2, dof) in fits.items():
            print(f'     {k_:<18s} params {", ".join(f"{v:.3f}" for v in par):<16s} chi2/dof = {chi2:.1f}/{dof} = {chi2 / dof:.2f}')
        print(f'     OLS slope b on sqrt(2 ln n) = {b:.3f}, bootstrap 95% [{lo:.3f}, {hi:.3f}]  (bounded: 0; Gaussian law: {bG:.3f})')
    # decade means of excess over E_G
    print('\n  excess over the Gaussian law, word means, by n-range:')
    for lo_, hi_ in ((1e3, 1e4), (1e4, 1e5), (1e5, 1e6), (1e6, 1e7), (1e7, 1e8)):
        sel = [r for r in tab if lo_ <= r['n'] < hi_]
        if sel:
            ex = np.array([r['wmean'] - r['EG'] for r in sel])
            ex0 = np.array([r['R0'] - r['EG'] for r in sel])
            print(f'    n in [{lo_:.0e},{hi_:.0e}): {len(sel)} primes; word-mean - E_G = {ex.mean():+.3f};'
                  f' R602 - E_G = {ex0.mean():+.3f}; E_G = {np.mean([r["EG"] for r in sel]):.3f}')

    print('\n[float] C. tails above thresholds (good coordinates, normalized by RMS) against n P(|Z| > th);'
          ' z-scores use the n/2 distinct values (counts are even)')
    for d in rows:
        if d['n'] < 4e5:
            continue
        n_ = d['n'] - 1
        for lab, st in (('R602', d['R_602_plus_k'][0]), ('R602+1', d['R_602_plus_k'][1]),
                        ('Bpart k=1', d['B_part_k'][0]), ('w(0,0)', d['words']['0,0']),
                        (f'w(0,{d["k_n"] - 1})', d['words'][f'0,{d["k_n"] - 1}'])):
            if 'tail' not in st:
                continue
            parts = []
            for th, c in st['tail'].items():
                # coordinates come in pairs i, n - i: compare c/2 with (n/2) P(|Z| > th)
                e = n_ * erfc(float(th) / sqrt(2))
                z = (c / 2 - e / 2) / sqrt(max(e / 2, 1e-12))
                if e > 0.05 or c > 0:
                    parts.append(f'{th}:{c}/{e:.1f}({z:+.1f})')
            print(f"  p={d['p']:>10d} {lab:<9s} " + ' '.join(parts))
    print('\n  normalized even moments M_2m / (2m-1)!! (good coordinates), R_602:')
    df = [1, 1, 3, 15, 105, 945, 10395, 135135, 2027025]
    for d in rows:
        if d['n'] < 4e5 and d['n'] > 3e3:
            continue
        mo = d['R_602_plus_k'][0]['moments']
        print(f"  p={d['p']:>10d} " + ' '.join(f"{2 * m}:{mo[str(2 * m)] / df[m]:.3f}" for m in range(2, 9)))

    print('\n[float] D. fixed-height fields of the nine-centre start: sup/RMS against E_G(n)')
    names = ['Y', 'W', 'F4', 'G', 'R', 'Q', 'UU', 'S']
    print('         n  E_G   ' + ''.join(f'{nm:>7s}' for nm in names) + '   h=V602-S')
    for d in rows:
        f = d['fields']
        print(f"  {d['n']:>9d} {gauss_expected_max(d['n'] // 2):5.2f} " + ''.join(f"{f[nm]['ratio']:7.3f}" for nm in names)
              + f"   {d['h_stats']['ratio']:.3f}")
    print('\n  M_4 / 3 of the fixed-height fields (Gaussian = 1; bounded symmetric laws < 1):')
    for d in rows:
        if d['n'] in (min(r['n'] for r in rows), max(r['n'] for r in rows)) or abs(np.log10(d['n']) - 6) < 0.01:
            f = d['fields']
            print(f"  {d['n']:>9d} " + ''.join(f"{nm}:{f[nm]['moments']['4'] / 3:.3f} " for nm in names))
    print('\n  height growth: sup/RMS of L_S^m S, m = 0..24 (seed iterates; height m above S)')
    for d in rows[::max(1, len(rows) // 8)] + [rows[-1]]:
        g = d['height_growth']['LS^m S']
        print(f"  n={d['n']:>9d} " + ' '.join(f'{v:.2f}' for v in g[:12]) + ' ... mean(m>=4) ' + f'{np.mean(g[4:]):.2f}')

    print('\n[float] E. counting rates')
    for d in rows[::max(1, len(rows) // 6)] + [rows[-1]]:
        sk = d['seed_part_k']
        rs = [sk[k + 1]['rms'] / sk[k]['rms'] for k in range(len(sk) - 1)]
        rk = d['R_602_plus_k']
        rr = [rk[k + 1]['rms'] / rk[k]['rms'] for k in range(len(rk) - 1)]
        print(f"  n={d['n']:>9d}: seed-part per-step RMS rate mean {np.mean(rs):.5f} (compact exact l_S = {L_S});"
              f" full L^k r rate mean {np.mean(rr):.5f}; increment rate (h 502-602) {d['rate_last100_geomean']:.5f};"
              f" log10 ||R_602||_2,n (float) {d['log10_sigma']['602']:.1f}")

    if len(sys.argv) > 2:
        print('\n[float] F. sensitivity: start row and corners of Q (same primes)')
        sens = load(sys.argv[2])
        allrows = rows + sens
        for p in sorted({d['p'] for d in sens}):
            for d in [x for x in allrows if x['p'] == p]:
                w = np.array([v['ratio'] for v in d['words'].values()])
                Rk = np.array([x['ratio'] for x in d['R_602_plus_k']])
                print(f"  p={p:>8d} t={d['tmode']:<2s} start={d['start']:<5s}: R602 {Rk[0]:.3f}, R-mean {Rk.mean():.3f},"
                      f" word-mean {w.mean():.3f}, word-max {w.max():.3f}, rate {d['rate_last100_geomean']:.5f},"
                      f" sup|V602-S| {d['V602_minus_S']['sup']:.4f}")


if __name__ == '__main__':
    main()
