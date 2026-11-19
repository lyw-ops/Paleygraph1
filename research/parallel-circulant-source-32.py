"""Round 32: actual Paley clipping, cyclic identities and triangle reductions.

Only stdout is written. Every numerical result is floating point, not an
interval certificate. The Markdown note proves the exact finite identities.
Run with python -B so that importing existing project helpers writes no pyc.
"""

import argparse
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


def projection(sign, side, vector):
    return (vector - vector.mean() + side * kernel_action(sign, vector)) / 2


def triangle_check(sign, side, B, a, h, z, d, b):
    """Small independent all-pairs check of the actual Paley induced graph.

    beta=DFT(B/a)/n, r=DFT(h)/n restricted to opposite vertices. For
    vertices g^(2k),g^(2l) in Q, the multiplier on their ratio is
    chi(g^(2k)-g^(2l)); this is the actual induced Paley adjacency.
    """
    n = len(sign)
    vertices = np.flatnonzero(sign == -side)
    beta = np.fft.fft(B / a) / n
    r = np.fft.fft(h) / n
    rr = r[vertices]
    differences = (vertices[:, None] - vertices[None, :]) % n
    adjacency = sign[differences] == -side
    tri = n * np.vdot(rr, (beta[differences] * adjacency) @ rr).real
    absolute_tri = n * float(np.abs(rr) @ (np.abs(beta[differences]) * adjacency) @ np.abs(rr))
    base = n * float(np.vdot(rr, rr).real)
    predicted = base + tri - b / a * z[0] ** 2
    direct = float(np.dot(d, z * z))
    return {"triangle_direct_error": abs(predicted - direct),
            "triangle_parseval_error": abs(base - float(z @ z)),
            "triangle_signed_term": float(tri),
            "triangle_absolute_majorant": absolute_tri,
            "triangle_diagonal_term": base,
            "triangle_mark_subtraction": float(b / a * z[0] ** 2),
            "triangle_vertices": len(vertices)}


def analyze(q, characteristic, tau, args):
    started = time.monotonic()
    sign = paley_sign(q) if q == characteristic else square_field_sign(characteristic)
    n = len(sign)
    c = tau / n
    w = np.full(n, c)
    w[0] = 1.
    W = float(w.sum())
    a = sqrt(W / n)
    rho = tau / W
    v, phi, residual = weighted_iterate(sign, w, tolerance=args.tolerance,
                                      rounds=args.rounds)
    if residual > args.accept_residual:
        raise RuntimeError((q, tau, "stationary solve not accepted", residual))
    high = (phi + np.abs(v)) / 2
    low = w / high
    spectra = {1: np.where(v >= 0, high, low),
               -1: np.where(v >= 0, low, high)}
    mark = np.eye(1, n, 0).ravel()
    # Integer checks concern actual signs; the stationary solve remains floating.
    assert sign[0] == 0 and int(sign.sum()) == -1
    assert np.all(np.abs(sign[1:]) == 1)
    assert np.array_equal(sign, sign[(-np.arange(n)) % n])
    for side in (1, -1):
        A, B = spectra[side], spectra[-side]
        u, opposite = A / a, B / a
        x = A - a
        d = c / (a * A)
        b = (1 - c) / A[0]
        e = projection(sign, -side, mark)
        en = float(np.dot(d, e * e))
        cross = np.fft.irfft(np.fft.rfft(A).conj() * np.fft.rfft(B), n)
        ratios = np.fft.irfft(np.fft.rfft(1 / A).conj() * np.fft.rfft(A), n)
        expected_ratios = n + (1 - c) / c * (1 - A / A[0])
        cepstrum_error = np.max(np.abs(np.fft.fft(np.log(A) + np.log(B)
                                                   - np.log(w)))) / n
        common = {"q": q, "characteristic": characteristic, "n": n,
                  "tau": tau, "side": side,
                  "stationary_residual": float(residual)}
        source = sqrt(n) * (A + B - 2 * np.sqrt(w))
        identities = {
            "kind": "cyclic_pair", **common,
            "mean_error": max(abs(A.mean() - a), abs(B.mean() - a)),
            "sector_error": float(np.linalg.norm(projection(sign, -side, A))),
            "cross_correlation_error": float(np.max(np.abs(cross - W))),
            "shift_ratio_relative_error": float(np.max(np.abs(ratios - expected_ratios))) / n,
            "cepstrum_reciprocity_error": float(cepstrum_error),
            "coordinate_product_error": float(np.max(np.abs(A * B - w))),
            "root_A": float(A[0]), "root_B": float(B[0]),
            "energy": float(x @ x), "bulk_u_max": float(np.max(u[1:])),
            "bulk_source_max": float(np.max(source[1:])),
            "root_projection_D_energy": en,
        }
        shifts = sorted(set([1, n // 7, n // 3, int(1 + np.argmax(A[1:]))]))
        kl_errors, budget_errors = [], []
        for shift in shifts:
            logratio = np.log(A) - np.log(np.roll(A, -shift))
            pi_to_q = float(w @ logratio)
            kl_errors.append(abs(pi_to_q - (1 - c) * np.log(A[0] / A[shift])))
            ratio = A[shift] / A[0]
            lr = np.log(A) - np.log(np.roll(A, -shift))
            lr[[0, (n - shift) % n]] = 0
            bulk_cost = 2 * c * float(np.sum(np.sinh(lr / 2) ** 2))
            budget_errors.append(abs(bulk_cost - (1 - ratio) * (1 - c / ratio)))
        identities["translation_KL_error"] = max(kl_errors)
        identities["bulk_log_shift_budget_error"] = max(budget_errors)
        emit(identities)

        for R in args.thresholds:
            tail = a * np.maximum(u - R, 0)
            tail[0] = 0
            excess = float(tail.sum() / (n * a))
            first = float(np.sum(u[1:] * (u[1:] > R)) / n)
            z = projection(sign, -side, tail)
            hinge_D = float(np.dot(d, z * z))
            direct_D = float(np.dot(d, tail * tail))
            diagonal = float(z @ z)
            signed_triangle = float(np.dot(opposite - 1, z * z))
            mark_subtraction = float(b / a * z[0] ** 2)
            row = {"kind": "hard_hinge", **common, "R": R,
                   "bulk_excess_mass": excess, "bulk_tail_first_mass": first,
                   "hinge_D_energy": hinge_D,
                   "hinge_D_over_excess": hinge_D / excess if excess > 1e-25 else None,
                   "hinge_unweighted_energy": diagonal,
                   "hinge_direct_D_energy": direct_D,
                   "hinge_weighted_projection_amplification": hinge_D / direct_D if direct_D > 1e-25 else None,
                   "cyclic_diagonal_term": diagonal,
                   "cyclic_signed_triangle_term": signed_triangle,
                   "cyclic_mark_subtraction": mark_subtraction,
                   "cyclic_triangle_identity_error": abs(diagonal + signed_triangle - mark_subtraction - hinge_D),
                   "source_tail_first_mass": float(np.sum(source[1:] * (source[1:] > R)) / n)}
            if direct_D > tau * excess + 1e-8:
                raise AssertionError(("direct hinge bound", row))
            if n <= args.dense_max:
                row.update(triangle_check(sign, side, B, a, tail, z, d, b))
                if row["triangle_direct_error"] > 1e-7:
                    raise AssertionError(row)
            emit(row)

        if n <= args.dense_max:
            # On each interval between bulk u-values, z_R is affine and
            # eta_R is positive affine. A quadratic divided by a positive
            # affine function is convex, so its maximum is at an endpoint.
            knots = np.unique(np.r_[0., u[1:]])
            max_ratio, maximizing_R = 0., 0.
            for R in knots[:-1]:
                hh = a * np.maximum(u - R, 0)
                hh[0] = 0
                eta = float(hh.sum() / (n * a))
                if eta <= 1e-25:
                    continue
                zz = projection(sign, -side, hh)
                ratio = float(np.dot(d, zz * zz)) / eta
                if ratio > max_ratio:
                    max_ratio, maximizing_R = ratio, float(R)
            emit({"kind": "all_threshold_scan", **common,
                  "knots": len(knots), "max_hinge_D_over_excess": max_ratio,
                  "maximizing_threshold": maximizing_R,
                  "candidate_C1_observed": max_ratio <= 1.})

        for delta in args.deltas:
            theta = delta / (d + delta)
            t = theta * x
            removed_mark = float(t[0])
            t[0] = 0
            z = projection(sign, -side, t)
            Dz = float(np.dot(d, z * z))
            unweighted = float(delta * (z @ z))
            # Complementary-sector identity used in the new UI proof.
            fullcap = rho * (u - 1) / (rho + delta * u)
            full_complement = -a * projection(sign, -side, fullcap) - removed_mark * e
            error = float(np.linalg.norm(z - full_complement))
            spatial = float(np.dot(delta * d / (d + delta), x * x))
            mean_cost = abs(float(t.mean())) * sqrt(float(np.sum(d + delta)))
            mark_cost = abs(removed_mark) * sqrt(d[0] + delta)
            row = {"kind": "soft_clip", **common, "delta": delta,
                   "leakage_D_energy": Dz, "leakage_delta_energy": unweighted,
                   "leakage_squared": Dz + unweighted,
                   "spatial": spatial, "mean_cost": mean_cost,
                   "mark_cost": mark_cost,
                   "decrement_upper": spatial + (mark_cost + mean_cost + sqrt(Dz + unweighted)) ** 2,
                   "actual_soft_cap_identity_error": error,
                   "direct_bulk_D_energy": float(np.dot(d, t * t)),
                   "projected_over_direct_D": Dz / float(np.dot(d, t * t)) if np.any(t) else None}
            if n <= args.dense_max:
                row.update(triangle_check(sign, side, B, a, t, z, d, b))
                # Positive divided-difference remainder, checked by a dense matrix.
                kernel = np.fft.irfft(sign[:n // 2 + 1], n)
                indices = np.arange(n)
                pij = (np.eye(n) - 1 / n - side * kernel[(indices[:, None] - indices[None, :]) % n]) / 2
                diff = u[None, :] - u[:, None]
                remainder = (delta * rho * (rho + delta) * diff ** 2 /
                             ((rho + delta * u[:, None]) ** 2 * (rho + delta * u[None, :])))
                curvature = a * np.sum(pij * remainder, axis=1) - removed_mark * e
                row["positive_curvature_identity_error"] = float(np.linalg.norm(curvature - z))
                absolute_curvature = a * np.sum(np.abs(pij) * remainder, axis=1) + abs(removed_mark) * np.abs(e)
                row["positive_curvature_absolute_D_bound"] = float(np.dot(d, absolute_curvature ** 2))
                if max(row["triangle_direct_error"], row["positive_curvature_identity_error"]) > 1e-7:
                    raise AssertionError(row)
                if delta == args.deltas[0] and n <= 200:
                    from scipy.integrate import quad_vec
                    def integrand(R):
                        hh = a * np.maximum(u - R, 0)
                        hh[0] = 0
                        return (2 * delta * rho * (rho + delta) /
                                (rho + delta * R) ** 3 * projection(sign, -side, hh))
                    integral, quadrature_error = quad_vec(
                        integrand, 0, float(np.max(u[1:])),
                        points=np.unique(u[1:]), epsabs=1e-11, epsrel=1e-11)
                    integrated = delta / rho * A[0] * e + integral
                    row["hinge_superposition_error"] = float(np.linalg.norm(z - integrated))
                    row["hinge_quadrature_reported_error"] = float(quadrature_error)
                    if row["hinge_superposition_error"] > 1e-7:
                        raise AssertionError(row)
            if error > 1e-7:
                raise AssertionError(row)
            emit(row)

        # Source UI is already enough for the delta times unweighted component.
        for delta in args.deltas:
            R = max(2., sqrt(rho / delta))
            excess_first = float(np.sum(u * (u > R)) / n)
            # This finite bound keeps the full marked first mass. It is harmless
            # in the field-first limit and avoids an unjustified deleted term.
            cap_bound = (2 * delta * (R + 1) + rho / 4 * excess_first)
            mark_term = delta / (d[0] + delta) * x[0]
            predicted = 2 * W * cap_bound + 2 * delta * mark_term ** 2 * float(e @ e)
            this_t = delta / (d + delta) * x
            this_t[0] = 0
            this_z = projection(sign, -side, this_t)
            value = float(delta * np.dot(this_z, this_z))
            if value > predicted + 1e-8:
                raise AssertionError(("UI delta bound", q, side, delta, value, predicted))
            emit({"kind": "UI_delta_bound", **common, "delta": delta, "R": R,
                  "full_u_tail_first_mass": excess_first,
                  "delta_leakage": value, "UI_delta_upper": predicted})
    emit({"kind": "runtime", "q": q, "tau": tau,
          "seconds": time.monotonic() - started})


def audit_files(paths):
    """Read back replay files; write a compact floating-consistency audit."""
    from collections import Counter
    from math import isfinite

    total = 0
    for path in paths:
        rows = [json.loads(line) for line in Path(path).read_text().splitlines()]
        counts = Counter(row["kind"] for row in rows)
        maxima = {}
        ui = {}
        for row in rows:
            for key, value in row.items():
                if isinstance(value, (int, float)):
                    if not isfinite(value):
                        raise AssertionError((path, key, value))
                    if key.endswith("error") or key.endswith("residual"):
                        maxima[key] = max(maxima.get(key, 0.), abs(value))
            if row["kind"] == "hard_hinge":
                assert row["hinge_D_energy"] >= -1e-12
                assert row["hinge_direct_D_energy"] <= row["tau"] * row["bulk_excess_mass"] + 1e-8
                ratio = row["hinge_D_over_excess"]
                assert ratio is None or ratio <= 1.
            if row["kind"] == "all_threshold_scan":
                assert row["candidate_C1_observed"]
            if row["kind"] == "UI_delta_bound":
                assert row["delta_leakage"] <= row["UI_delta_upper"] + 1e-8
                key = (row["q"], row["tau"], row["side"], row["delta"])
                ui[key] = row["delta_leakage"]
        for row in rows:
            if row["kind"] == "soft_clip":
                key = (row["q"], row["tau"], row["side"], row["delta"])
                assert abs(ui[key] - row["leakage_delta_energy"]) < 1e-10
        assert max(maxima.values(), default=0.) < 1e-7
        assert counts["cyclic_pair"] == 2 * counts["runtime"]
        total += len(rows)
        emit({"kind": "floating_consistency_audit", "file": str(path),
              "records": len(rows), "kinds": dict(counts),
              "max_errors": maxima, "status": "passed",
              "scope": "finite floating records; no interval or uniform-prime certificate"})
    emit({"kind": "audit_total", "records": total, "files": len(paths),
          "status": "passed"})


def existing31_check(taus):
    """Reuse the old exact eight-dimensional family, without a new model."""
    import importlib.util

    old_path = Path(__file__).with_name("parallel-coherent-source-31.py")
    spec = importlib.util.spec_from_file_location("existing_round31", old_path)
    old = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(old)
    for tau in taus:
        Fstar = old.limiting_row(tau)["F_limit"]
        emit({"kind": "existing31_algebraic_limit", "tau": tau,
              "F_limit": Fstar, "hinge_D_limit": Fstar / 4,
              "ratio_over_t_limit": sqrt(1 + tau) * Fstar,
              "scope": "same prior noncirculant family; no new counterexample"})
        for t in (8, 32, 128, 512, 4096):
            block = old.build_block(2 * t ** 8, t ** 4, float(t ** 3), tau=tau)
            n, a, s = block["n"], block["a"], block["s"]
            R = block["H"] / (2 * s)
            hh = np.maximum(block["avals"] - a * R, 0) * block["roots"]
            hh[0] = 0
            assert np.count_nonzero(hh) == 1 and hh[2] > 0
            eta = float(hh @ block["roots"] / (n * a))
            z = block["Pm"] @ hh
            energy = float(z @ (block["dvals"] * z))
            expected_eta = 1 / (4 * s * t)
            emit({"kind": "existing31_hardtail", "tau": tau, "t": t,
                  "n": n, "R": R, "bulk_excess_mass": eta,
                  "hinge_D_energy": energy, "hinge_D_over_excess": energy / eta,
                  "ratio_over_t": energy / eta / t,
                  "eta_identity_error": abs(eta - expected_eta),
                  "hinge_D_limit": Fstar / 4,
                  "same_prior_noncirculant_family": True})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--primes", type=int, nargs="*", default=[101, 401, 9413, 153649, 1000033])
    parser.add_argument("--square-roots", type=int, nargs="*", default=[19, 97, 389])
    parser.add_argument("--tau", type=float, nargs="+", default=[.05])
    parser.add_argument("--thresholds", type=float, nargs="+", default=[0, 1, 2, 3, 4, 5, 6, 8, 16, 32, 64, 128])
    parser.add_argument("--deltas", type=float, nargs="+", default=[.2, .05, .01, .002, .0002])
    parser.add_argument("--dense-max", type=int, default=300)
    parser.add_argument("--rounds", type=int, default=96)
    parser.add_argument("--tolerance", type=float, default=2e-12)
    parser.add_argument("--accept-residual", type=float, default=1e-8)
    parser.add_argument("--audit-files", nargs="+", default=None)
    parser.add_argument("--existing31-check", action="store_true")
    args = parser.parse_args()
    if args.audit_files is not None:
        audit_files(args.audit_files)
        return
    if args.existing31_check:
        existing31_check(args.tau)
        return
    for tau in args.tau:
        for q, ch in [(p, p) for p in args.primes] + [(p * p, p) for p in args.square_roots]:
            analyze(q, ch, tau, args)


if __name__ == "__main__":
    main()
