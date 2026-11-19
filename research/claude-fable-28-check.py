"""Replay for research/claude-fable-28.md (floating point; diagnostics, not certificates).

Sections:
  identities  direct O(n^2) checks of Propositions 1-3 at small orders
  witness     sign / l1 / l2 of the stationary positional witnesses (table B1)
  pairing     l-infinity/l1 positional pairing bound along Picard prefixes (table B2)
  highset     fixed-depth averaged iterates: subfield-annihilator values at squares
              versus upper tails at primes (section C probe)
  possup      positional sup norm max_{x != 1} |sum_k z_T(k) eta_k(x)| of the averaged
              iterates, and the pairing <z_T, v*> it controls through (6)

Run from the repository root:
  OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
      research/claude-fable-28-check.py > research/claude-fable-28-check.jsonl
"""

import argparse
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from theta import paley_sign  # noqa: E402
from square_control import square_field_sign  # noqa: E402


def apply_k(sign, vec):
    n = len(sign)
    return np.fft.irfft(sign[: n // 2 + 1] * np.fft.rfft(vec), n)


def weights(n, tau):
    w = np.full(n, tau / n)
    w[0] = 1.0
    return w


def stationary(sign, tau, tol=1e-13, max_steps=400000):
    n = len(sign)
    w4 = 4 * weights(n, tau)
    v = np.zeros(n)
    res = np.inf
    for step in range(max_steps):
        nv = apply_k(sign, np.sqrt(v * v + w4))
        res = float(np.linalg.norm(nv - v))
        v = nv
        if res < tol:
            break
    return v, res, step + 1


def pair(sign, tau):
    n = len(sign)
    w = weights(n, tau)
    W = w.sum()
    m = np.sqrt(W / n)
    v, res, steps = stationary(sign, tau)
    phi = np.sqrt(v * v + 4 * w)
    up, um = (phi + v) / 2, (phi - v) / 2
    fp = np.fft.ifft(up).real / m
    fm = np.fft.ifft(um).real / m
    return dict(n=n, w=w, W=W, m=m, v=v, phi=phi, up=up, um=um, fp=fp, fm=fm, res=res, steps=steps)


def emit(record):
    def clean(x):
        if isinstance(x, (np.floating, float)):
            return float(f"{float(x):.10g}")
        if isinstance(x, (np.integer,)):
            return int(x)
        if isinstance(x, (list, tuple)):
            return [clean(y) for y in x]
        return x

    print(json.dumps({k: clean(x) for k, x in record.items()}), flush=True)


def conv(a, b):
    """Direct cyclic convolution (no FFT): (a*b)[j] = sum_i a[i] b[j-i]."""
    n = len(a)
    idx = (np.arange(n)[:, None] - np.arange(n)[None, :]) % n
    return (a[None, :] * b[idx]).sum(axis=1)


def identities(label, sign, tau, rng):
    P = pair(sign, tau)
    n, W, m, fp, fm = P["n"], P["W"], P["m"], P["fp"], P["fm"]
    gamma = (1 - tau / n) / W
    dplus, dminus = sign == 1, sign == -1
    delta = np.zeros(n)
    delta[0] = 1
    phip, phim = fp - delta, fm - delta
    A, B = phip.sum(), phim.sum()
    c1 = conv(fp, fm)
    err1 = np.abs(c1 - (gamma + (1 - gamma) * delta)).max()
    c2 = conv(phip, phim)
    err2 = np.abs((phip + phim + c2)[1:] - gamma).max()
    inv = (fm - gamma / (1 + A)) / (1 - gamma)
    err3 = np.abs(conv(fp, inv) - delta).max()
    const_dev = np.abs(inv[dplus] + gamma / ((1 - gamma) * (1 + A))).max()
    # Proposition 2 and 3 at a random trial point and at Picard points
    out = []
    w = P["w"]
    trials = [rng.normal(size=n) / np.sqrt(n)]
    v = np.zeros(n)
    for _ in range(6):
        v = apply_k(sign, np.sqrt(v * v + 4 * w))
        trials.append(v.copy())
    for t in trials:
        t = (t + np.roll(t[::-1], 1)) / 2  # even
        t = t - t.mean()
        r = t - apply_k(sign, np.sqrt(t * t + 4 * w))
        g = np.arcsinh(t / (2 * np.sqrt(w)))
        gs = np.arcsinh(P["v"] / (2 * np.sqrt(w)))
        lhs = float((w * (np.cosh(g - gs) - 1)).sum())
        rhs = float(r @ (t - P["v"])) / 4 - float(r @ r) / 8
        R = np.fft.fft(r).real
        lhs5 = float(r @ P["v"])
        rhs5 = float(m * ((phip - phim)[1:] * R[1:]).sum())
        bound6 = float(np.abs(R[1:]).max() * m * (np.abs(phip[1:]).sum() + np.abs(phim[1:]).sum()))
        out.append((lhs, rhs, lhs <= rhs + 1e-12, abs(lhs5 - rhs5), abs(lhs5) <= bound6 + 1e-12))
    N = float(np.clip(-(phip + phim)[1:], 0, None).sum())
    l1 = float(m * (np.abs(phip[1:]).sum() + np.abs(phim[1:]).sum()))
    emit(dict(section="identities", label=label, n=n, tau=tau, stationary_residual=P["res"],
              f_plus_at_1=fp[0], f_minus_at_1=fm[0],
              leak_plus_on_Dminus=np.abs(fp[dminus]).max(), leak_minus_on_Dplus=np.abs(fm[dplus]).max(),
              min_spectrum=min(P["up"].min(), P["um"].min()),
              err_factorization_1=err1, err_quadratic_2=err2, err_inverse_3=err3,
              inverse_constancy_dev_on_Dplus=const_dev,
              err_sum_identity=abs((1 + A) * (1 + B) - n / W),
              prop2_all_hold=all(o[2] for o in out), prop2_min_slack=min(o[1] - o[0] for o in out),
              prop3_identity_max_err=max(o[3] for o in out), prop3_bound_all_hold=all(o[4] for o in out),
              eq7_err=abs(l1 - (P["phi"][0] - 2 * m + 2 * m * N))))


def witness(label, sign, tau):
    P = pair(sign, tau)
    n, m, fp, fm = P["n"], P["m"], P["fp"], P["fm"]
    dplus, dminus = sign == 1, sign == -1
    rt = np.sqrt(n)
    emit(dict(section="witness", label=label, n=n, tau=tau, stationary_residual=P["res"], steps=P["steps"],
              v0=P["v"][0], norm_v=np.linalg.norm(P["v"]), Phi0=P["phi"][0],
              neg_fraction_plus=(fp[dplus] < 0).mean(), neg_fraction_minus=(fm[dminus] < 0).mean(),
              l1_plus_over_sqrt_n=np.abs(fp[dplus]).sum() / rt, sum_plus_over_sqrt_n=fp[dplus].sum() / rt,
              l1_minus_over_sqrt_n=np.abs(fm[dminus]).sum() / rt, sum_minus_over_sqrt_n=fm[dminus].sum() / rt,
              l2sq_plus=(fp[dplus] ** 2).sum(), l2sq_minus=(fm[dminus] ** 2).sum(),
              min_sqrt_n_f_plus=rt * fp[dplus].min(), max_sqrt_n_f_plus=rt * fp[dplus].max(),
              m_l1_total=m * (np.abs(fp[1:]).sum() + np.abs(fm[1:]).sum()),
              max_bulk_U_plus=P["up"][1:].max() / m, max_bulk_U_minus=P["um"][1:].max() / m))


def pairing(label, sign, tau, depths, subfield_step=None):
    P = pair(sign, tau)
    n, m, w = P["n"], P["m"], P["w"]
    l1 = m * (np.abs(P["fp"][1:]).sum() + np.abs(P["fm"][1:]).sum())
    v = np.zeros(n)
    for T in range(max(depths) + 1):
        nv = apply_k(sign, np.sqrt(v * v + 4 * w))
        if T in depths:
            r = v - nv
            R = np.fft.fft(r).real
            arg = int(np.abs(R[1:]).argmax()) + 1
            rec = dict(section="pairing", label=label, n=n, tau=tau, T=T, norm_r=np.linalg.norm(r),
                       rho=np.abs(R[1:]).max(), pairing=float(r @ P["v"]),
                       bound_linf_l1=np.abs(R[1:]).max() * l1, bound_l2_l2=np.linalg.norm(r) * np.linalg.norm(P["v"]),
                       norm_vstar=np.linalg.norm(P["v"]), m_l1_total=l1, mark=v[0])
            if subfield_step:
                inside = np.abs(R[subfield_step::subfield_step])
                outside_mask = np.ones(n, bool)
                outside_mask[::subfield_step] = False
                rec.update(argmax_in_subfield=(arg % subfield_step == 0),
                           subfield_min_abs_R=inside.min(), subfield_mean_R=R[subfield_step::subfield_step].mean(),
                           outside_max_abs_R=np.abs(R[outside_mask]).max())
            emit(rec)
        v = nv


def highset(label, sign, tau, depths, annihilator_step=None, thresholds=(0.5, 0.75, 0.9)):
    """Averaged iterates z_{t+1} = (z_t + K Phi(z_t))/2 from zero, scaled by sqrt(n)."""
    n = len(sign)
    w = weights(n, tau)
    z = np.zeros(n)
    refs = {}
    for T in range(1, max(depths) + 1):
        z = (z + apply_k(sign, np.sqrt(z * z + 4 * w))) / 2
        if T in depths:
            sc = np.sqrt(n) * z[1:]
            rec = dict(section="highset", label=label, n=n, tau=tau, T=T, mark=z[0],
                       rms=np.sqrt((sc ** 2).mean()), max_scaled=sc.max(), min_scaled=sc.min(),
                       q999=np.quantile(sc, 0.999), q9999=np.quantile(sc, 0.9999))
            if annihilator_step:
                a = np.sqrt(n) * z[annihilator_step::annihilator_step]
                mask = np.ones(n, bool)
                mask[::annihilator_step] = False
                bulk = np.sqrt(n) * z[mask]
                rec.update(annihilator_mean=a.mean(), annihilator_min=a.min(), annihilator_max=a.max(),
                           bulk_max_scaled=bulk.max(), bulk_q9999=np.quantile(bulk, 0.9999),
                           bulk_fraction_above=[float((bulk >= c * a.mean()).mean()) for c in thresholds])
                refs[T] = float(a.mean())
            emit(rec)
    return refs


def highset_compare(label, sign, tau, depths, refs, thresholds=(0.5, 0.75, 0.9)):
    n = len(sign)
    w = weights(n, tau)
    z = np.zeros(n)
    for T in range(1, max(depths) + 1):
        z = (z + apply_k(sign, np.sqrt(z * z + 4 * w))) / 2
        if T in depths and T in refs:
            sc = np.sqrt(n) * z[1:]
            emit(dict(section="highset_compare", label=label, n=n, tau=tau, T=T, square_reference=refs[T],
                      max_scaled=sc.max(), ratio_max_to_reference=sc.max() / refs[T],
                      count_above=[int((sc >= c * refs[T]).sum()) for c in thresholds],
                      fraction_above=[float((sc >= c * refs[T]).mean()) for c in thresholds]))


def possup(label, sign, tau, depths, subfield_step=None):
    P = pair(sign, tau)
    n, m, w = P["n"], P["m"], P["w"]
    l1 = m * (np.abs(P["fp"][1:]).sum() + np.abs(P["fm"][1:]).sum())
    z = np.zeros(n)
    for T in range(1, max(depths) + 1):
        z = (z + apply_k(sign, np.sqrt(z * z + 4 * w))) / 2
        if T in depths:
            Z = np.fft.fft(z).real
            rec = dict(section="possup", label=label, n=n, tau=tau, T=T,
                       positional_sup=np.abs(Z[1:]).max(), positional_rms=np.sqrt((Z[1:] ** 2).mean()),
                       frequency_sup_scaled=np.sqrt(n) * np.abs(z[1:]).max(),
                       pairing_with_vstar=float(z @ P["v"]), bound_linf_l1=np.abs(Z[1:]).max() * l1,
                       norm_z=np.linalg.norm(z), norm_vstar=np.linalg.norm(P["v"]))
            if subfield_step:
                rec.update(subfield_mean=Z[subfield_step::subfield_step].mean(),
                           argmax_in_subfield=((int(np.abs(Z[1:]).argmax()) + 1) % subfield_step == 0))
            emit(rec)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--quick", action="store_true", help="skip the million-order prime")
    args = parser.parse_args()
    rng = np.random.default_rng(28)

    for p in (101, 401):
        for tau in (0.05, 0.01):
            identities(f"p={p}", paley_sign(p), tau, rng)
    for r in (11, 19):
        identities(f"q={r}^2", square_field_sign(r), 0.05, rng)

    for p in (401, 1997, 9413, 37253, 153649):
        s = paley_sign(p)
        for tau in (0.05, 0.01):
            witness(f"p={p}", s, tau)
    for r in (19, 43, 97, 193):
        witness(f"q={r}^2", square_field_sign(r), 0.05)

    depths = (1, 2, 4, 8, 16, 32, 64, 128)
    for p in (9413, 153649):
        pairing(f"p={p}", paley_sign(p), 0.05, depths)
    for r in (97, 193):
        pairing(f"q={r}^2", square_field_sign(r), 0.05, depths, subfield_step=(r + 1) // 2)

    pd = (1, 2, 4, 8, 16, 32, 64, 128, 256)
    for p in (9413, 153649):
        possup(f"p={p}", paley_sign(p), 0.05, pd)
    for r in (97, 193):
        possup(f"q={r}^2", square_field_sign(r), 0.05, pd, subfield_step=(r + 1) // 2)

    hd = (1, 2, 3, 4, 6, 8, 12, 16, 24, 32, 64, 128)
    refs = {}
    for r in (97, 193, 389):
        refs = highset(f"q={r}^2", square_field_sign(r), 0.05, hd, annihilator_step=r - 1)
    primes = (9413, 37253, 153649) + (() if args.quick else (1000033,))
    for p in primes:
        s = paley_sign(p)
        highset(f"p={p}", s, 0.05, hd)
        highset_compare(f"p={p}", s, 0.05, hd, refs)


if __name__ == "__main__":
    main()
