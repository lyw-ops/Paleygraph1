"""Round 33: positive-pair fidelity certificates for the actual Paley source.

All writes use the parallel-prime-ui-33 prefix. Float diagnostics and Arb
certificates are different record classes. A replay uses only exact integer
Fourier coefficients, exact Paley signs, and Arb interval arithmetic; it does
not trust the proposed stationary solve.
"""

import argparse
from fractions import Fraction
import gzip
import hashlib
import json
from math import sqrt
from pathlib import Path
import sys
import time

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from poisson_weights import weighted_iterate
from smoothing import kernel_action
from square_control import square_field_sign
from theta import paley_sign


def emit(row):
    print(json.dumps(row, sort_keys=True), flush=True)


def signs(q, root):
    return square_field_sign(root) if root else paley_sign(q)


def project(sign, side, x):
    return (x + x.mean() + side * kernel_action(sign, x)) / 2


def positive_pair(sign, vector, w, kappa):
    """Project raw positive spectra, then add a constant to impose min >= kappa.

    The floating output is a proposal only. The certified mode rounds the
    Fourier coefficients and checks positivity independently with Arb.
    """
    phi = np.hypot(vector, 2 * np.sqrt(w))
    high = (phi + np.abs(vector)) / 2
    raw = np.where(vector >= 0, high, w / high)
    other = np.where(vector >= 0, w / high, high)
    out, repairs = [], []
    for side, spectrum in ((1, raw), (-1, other)):
        p = project(sign, side, spectrum)
        mean = float(p.mean())
        shift = max(0., (kappa * mean - float(p.min())) / (1 - kappa))
        out.append((p + shift) / (mean + shift))
        repairs.append(shift / mean)
    return out[0], out[1], repairs


def actual_pair(vector, w):
    phi = np.hypot(vector, 2 * np.sqrt(w))
    high = (phi + np.abs(vector)) / 2
    return (np.where(vector >= 0, high, w / high),
            np.where(vector >= 0, w / high, high))


def pair_row(sign, p, q, m, u, v, kappa, common, thresholds):
    n = len(p)
    gap = float(np.mean((np.sqrt(m) - np.sqrt(p * q)) ** 2))
    error = (np.sqrt(u * q) - np.sqrt(v * p)) ** 2
    r = np.sqrt(m * p / q)
    t = np.sqrt(m * q / p)
    minimum = min(float(p[1:].min()), float(q[1:].min()))
    rho = float(m[1])
    row = {"kind": "floating_feasible_pair", **common, "kappa": kappa,
           "trial_fidelity_gap": gap, "trial_gap_over_kappa": gap / kappa,
           "bulk_minimum": minimum,
           "bulk_rebalanced_max": max(float(r[1:].max()), float(t[1:].max())),
           "pair_mean_error": max(abs(float(p.mean())-1), abs(float(q.mean())-1)),
           "pair_product_mean_error": abs(float(np.mean(p*q))-1),
           "unknown_source_error_identity_error": abs(float(error.mean())-gap),
           "source_cross_error": max(abs(float(np.mean(u*q))-1), abs(float(np.mean(v*p))-1)),
           "bulk_source_u_max": float(u[1:].max()),
           "bulk_source_v_max": float(v[1:].max())}
    if abs(float(error.mean()) - gap) > 1e-7:
        raise AssertionError(row)
    emit(row)
    for R in thresholds:
        if not R > sqrt(rho):
            raise ValueError("joint-tail thresholds must exceed sqrt(rho)")
        tails = float((np.sum(u[1:] * (u[1:] > R)) +
                       np.sum(v[1:] * (v[1:] > R))) / n)
        bound = (sqrt(gap) + sqrt(2 * rho / R)) ** 2 / minimum
        if tails > bound + 1e-7:
            raise AssertionError(("joint tail bound", tails, bound))
        emit({"kind": "floating_tail_bound", **common, "kappa": kappa,
              "R": R, "actual_joint_tail": tails, "finite_tail_upper": bound})


def exact_input(sign, p, q, order, root, tau, bits, kappa, proposal):
    n, scale = len(sign), 2 ** bits
    spectra = []
    for side, spectrum in ((1, p), (-1, q)):
        f = np.fft.fft(spectrum).real / n
        half = [scale]
        for j in range(1, n // 2 + 1):
            half.append(round(float(f[j]) * scale) if sign[j] == side else 0)
        coefficients = half + (half[-2:0:-1] if n % 2 == 0 else half[:0:-1])
        assert len(coefficients) == n
        spectra.append(coefficients)
    return {"schema": "prime-ui-33-positive-Fourier-pair-v1", "q": order,
            "square_root": root, "tau": str(tau), "n": n, "scale": scale,
            "target_kappa": str(kappa), "proposal": proposal,
            "plus": spectra[0], "minus": spectra[1]}


def prefix_path(path):
    path = Path(path)
    if not path.name.startswith("parallel-prime-ui-33"):
        raise ValueError("all outputs must have the authorized prefix")
    return path


def save_input(payload, path):
    path = prefix_path(path)
    data = (json.dumps(payload, separators=(",", ":")) + "\n").encode()
    with path.open("wb") as file:
        with gzip.GzipFile(filename="", mode="wb", fileobj=file, mtime=0) as zipped:
            zipped.write(data)
    return hashlib.sha256(data).hexdigest()


def replay(path, precision, thresholds):
    from flint import acb, arb, ctx
    ctx.prec = precision
    path = Path(path)
    data = gzip.decompress(path.read_bytes())
    payload = json.loads(data)
    assert payload["schema"] == "prime-ui-33-positive-Fourier-pair-v1"
    sign = signs(payload["q"], payload["square_root"])
    n = len(sign)
    assert payload["n"] == n and payload["q"] == 2*n+1
    scale = payload["scale"]
    assert isinstance(scale, int) and scale > 0
    pairs = []
    for side, key in ((1, "plus"), (-1, "minus")):
        coefficients = payload[key]
        assert len(coefficients) == n and all(isinstance(x, int) for x in coefficients)
        assert coefficients[0] == scale
        assert coefficients[1:] == coefficients[:0:-1]
        assert all(x == 0 for j, x in enumerate(coefficients) if j and sign[j] != side)
        transformed = acb.dft(coefficients)
        assert all(x.imag.contains(0) for x in transformed)
        spectrum = [x.real / scale for x in transformed]
        assert all(x > 0 for x in spectrum), "strict positivity not certified"
        pairs.append(spectrum)
    p, q = pairs
    tau = Fraction(payload["tau"])
    assert tau > 0
    tau_ball = arb(tau.numerator) / tau.denominator
    W = 1 + (n-1)*tau_ball/n
    rho, m0 = tau_ball/W, n/W
    assert all(arb(R) > rho.sqrt() for R in thresholds), "joint-tail thresholds must exceed sqrt(rho)"
    gap = arb(0)
    for i, (pp, qq) in enumerate(zip(p, q)):
        mm = m0 if i == 0 else rho
        gap += (mm.sqrt() - (pp*qq).sqrt()) ** 2
    gap /= n
    # Use a nonnegative outward upper endpoint, never a rounded midpoint.
    gap_upper = max(arb(0), gap.upper())
    bulk_min = min(x.lower() for x in p[1:] + q[1:])
    assert bulk_min > 0
    rmax, umax, source_max = arb(0), arb(0), arb(0)
    u_tail = {R: arb(0) for R in thresholds}
    g_tail = {R: arb(0) for R in thresholds}
    u_tail_lower = {R: arb(0) for R in thresholds}
    g_tail_lower = {R: arb(0) for R in thresholds}
    for i in range(1, n):
        r, t = (rho*p[i]/q[i]).sqrt(), (rho*q[i]/p[i]).sqrt()
        rmax = max(rmax, r.upper(), t.upper())
        # e_i <= n*S, and e_i=q_i*(u_i-r_i)^2/u_i.
        def enclose(center, lower_weight):
            z = n*gap_upper/lower_weight
            upper = (center + z/2 + (z*center + z*z/4).sqrt()).upper()
            low_center = center.lower()
            lower = (low_center**2 / (low_center + z/2 +
                       (z*low_center + z*z/4).sqrt())).lower()
            return lower, upper
        ulow, uu = enclose(r, q[i].lower())
        vlow, vv = enclose(t, p[i].lower())
        umax = max(umax, uu, vv)
        gg = (W.sqrt()*(uu+vv)-2*tau_ball.sqrt()).upper()
        glow = max(arb(0), (W.sqrt()*(ulow+vlow)-2*tau_ball.sqrt()).lower())
        source_max = max(source_max, gg)
        for R in thresholds:
            if not uu <= R:
                u_tail[R] += uu
            if not vv <= R:
                u_tail[R] += vv
            if not gg <= R:
                g_tail[R] += gg
            if ulow > R:
                u_tail_lower[R] += ulow
            if vlow > R:
                u_tail_lower[R] += vlow
            if glow > R:
                g_tail_lower[R] += glow
    result = {"kind": "arb_positive_pair_certificate", "q": payload["q"],
              "square_root": payload["square_root"], "n": n,
              "tau": str(tau), "precision_bits": precision,
              "exact_fourier_input": path.name,
              "uncompressed_input_sha256": hashlib.sha256(data).hexdigest(),
              "proposal": payload["proposal"],
              "strict_positivity_proved": True, "exact_sector_support_proved": True,
              "fidelity_gap_upper": str(gap_upper), "bulk_floor_lower": str(bulk_min),
              "bulk_rebalanced_max_upper": str(rmax),
              "actual_stationary_bulk_normalized_max_upper": str(umax),
              "actual_stationary_bulk_G_max_upper": str(source_max)}
    emit(result)
    for R in thresholds:
        joint_bound = ((gap_upper.sqrt()+(2*rho/R).sqrt())**2/bulk_min).upper()
        emit({"kind": "arb_stationary_tail_certificate", "q": payload["q"],
              "square_root": payload["square_root"], "tau": str(tau), "R": R,
              "joint_normalized_tail_lower": str((u_tail_lower[R]/n).lower()),
              "joint_normalized_tail_upper": str((u_tail[R]/n).upper()),
              "G_tail_lower": str((g_tail_lower[R]/n).lower()),
              "G_tail_upper": str((g_tail[R]/n).upper()),
              "dimension_free_joint_tail_upper": str(joint_bound)})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--primes", nargs="*", type=int, default=[])
    parser.add_argument("--square-roots", nargs="*", type=int, default=[])
    parser.add_argument("--tau", default="1/20")
    parser.add_argument("--kappa", nargs="+", type=float, default=[.001, .01, .05, .1])
    parser.add_argument("--thresholds", nargs="+", type=float, default=[2, 4, 8, 16, 32, 64, 128])
    parser.add_argument("--steps", nargs="*", type=int, default=[])
    parser.add_argument("--stationary", action="store_true")
    parser.add_argument("--certify-prefix", type=Path)
    parser.add_argument("--coefficient-bits", type=int, default=90)
    parser.add_argument("--precision", type=int, default=160)
    parser.add_argument("--replay", type=Path)
    args = parser.parse_args()
    if args.replay:
        replay(args.replay, args.precision, args.thresholds)
        return
    tau = Fraction(args.tau)
    if not tau > 0 or not all(0 < x < 1 for x in args.kappa):
        parser.error("positive tau, kappa in (0,1) required")
    if args.certify_prefix:
        prefix_path(args.certify_prefix)
    for order, root in ([(x, None) for x in args.primes] +
                        [(x*x, x) for x in args.square_roots]):
        started = time.monotonic()
        sign = signs(order, root)
        n = len(sign)
        w = np.full(n, float(tau)/n)
        w[0] = 1
        W = 1+(n-1)*float(tau)/n
        a, m = sqrt(W/n), w*n/W
        stationary, _, residual = weighted_iterate(sign, w, tolerance=1e-12, rounds=96)
        if residual > 1e-9:
            raise RuntimeError((order, "stationary proposal not accepted", residual))
        A, B = actual_pair(stationary, w)
        u, v = A/a, B/a
        proposals = []
        if args.steps:
            vector = np.zeros(n)
            for step in range(1, max(args.steps)+1):
                vector = kernel_action(sign, np.hypot(vector, 2*np.sqrt(w)))
                if step in args.steps:
                    proposals.append((f"Picard-{step}", vector.copy()))
        if args.stationary or not proposals:
            proposals.append(("safeguarded-Newton-proposal", stationary))
        for name, vector in proposals:
            for kappa in args.kappa:
                p, q, repairs = positive_pair(sign, vector, w, kappa)
                common = {"q": order, "square_root": root, "n": n,
                          "tau": str(tau), "proposal": name,
                          "stationary_float_residual": float(residual),
                          "relative_constant_repairs": repairs}
                pair_row(sign, p, q, m, u, v, kappa, common, args.thresholds)
                if args.certify_prefix:
                    stem = str(args.certify_prefix)
                    path = Path(f"{stem}-q{order}-tau{tau.numerator}_{tau.denominator}-{name}-k{kappa:g}-input.json.gz")
                    payload = exact_input(sign, p, q, order, root, tau,
                                          args.coefficient_bits, kappa, name)
                    digest = save_input(payload, path)
                    emit({"kind": "exact_fourier_input_saved", "path": str(path),
                          "uncompressed_sha256": digest})
                    replay(path, args.precision, args.thresholds)
        emit({"kind": "runtime", "q": order, "seconds": time.monotonic()-started})


if __name__ == "__main__":
    main()
