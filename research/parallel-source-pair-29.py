"""Round 29: reciprocal Schur identities, stripped tails, and an exact model.

All records are floating-point diagnostics of identities proved in the note.
The constructed reflection is not a Paley kernel. No write occurs in Python.
"""

import argparse
import json
from math import sqrt
from pathlib import Path
import sys

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from poisson_weights import weighted_iterate
from smoothing import kernel_action
from square_control import square_field_sign
from theta import paley_sign
from importlib import import_module

old = import_module("parallel-reciprocal-28")
project, even_basis = old.project, old.even_basis


def emit(row):
    print(json.dumps(row, sort_keys=True), flush=True)


def analyze_paley(q, characteristic, tau, dense):
    sign = paley_sign(q) if q == characteristic else square_field_sign(characteristic)
    n = len(sign)
    c = tau / n
    weights = np.full(n, c)
    weights[0] = 1
    W = float(weights.sum())
    a = sqrt(W / n)
    rho = tau / W
    v, u, residual = weighted_iterate(sign, weights, tolerance=1e-12, rounds=64)
    if residual > 1e-9:
        raise RuntimeError((q, tau, residual))
    large = (u + np.abs(v)) / 2
    small = weights / large
    spectra = {1: np.where(v >= 0, large, small), -1: np.where(v >= 0, small, large)}
    mark = np.eye(1, n, 0).ravel()
    for side in (1, -1):
        A, B = spectra[side], spectra[-side]
        x = A - a
        b = (1 - c) / A[0]
        d = c / (a * A)
        e = project(sign, side, mark)
        Q = (1 - c) * (1 - a / A[0])
        row = {
            "kind": "paley", "q": q, "characteristic": characteristic,
            "tau": tau, "side": side, "n": n,
            "stationary_residual": float(residual), "energy": float(x @ x),
            "source_error": float(np.linalg.norm(project(sign, side, d * x) - b * e)),
            "bulk_product_error": float(np.max(np.abs(
                d[1:] * (c / (a * B[1:])) - rho))),
            "mark_product_error": float(abs(d[0] * c / (a * B[0]) - rho * c)),
            "dirichlet_error": float(abs(np.sum(d * x * x) - Q)),
        }
        if dense:
            plus = even_basis(sign, side)
            minus = even_basis(sign, -side)
            comp = np.column_stack((np.ones(n) / sqrt(n), minus))
            T = (plus.T * d) @ plus
            inv = np.linalg.inv(T)
            U = A / a
            Sm = (minus.T * U) @ minus
            C = (minus.T * U) @ plus
            xc = plus.T @ x
            schur = (plus.T * U) @ plus - C.T @ np.linalg.solve(Sm, C)
            schur -= np.outer(xc, xc) / (a * a * n)
            row["reciprocal_schur_relative_error"] = float(
                np.linalg.norm(schur - rho * inv) / max(1, np.linalg.norm(rho * inv)))
            row["complement_constant_coupling_error"] = float(
                np.linalg.norm(minus.T @ U) / sqrt(n))
            root = plus[0]
            values, vec = np.linalg.eigh(T)
            masses = b * b * (vec.T @ root) ** 2 / values
            f0 = float(root @ inv @ root)
        else:
            comp = None
        for delta in (0.002, 0.01, 0.05, 0.2):
            theta = delta / (d + delta)
            t = theta * x
            k = float(t[0])
            t[0] = 0
            mean = float(t.mean())
            leak = project(sign, -side, t)
            leakage = float(np.sum((d + delta) * leak * leak))
            spatial = float(delta * np.sum(d / (d + delta) * x * x))
            mark_cost = abs(k) * sqrt(d[0] + delta)
            mean_cost = abs(mean) * sqrt(float(np.sum(d + delta)))
            bound = spatial + (mark_cost + mean_cost + sqrt(leakage)) ** 2
            tail = {
                "delta": delta, "spatial": spatial, "opposite_leakage_squared": leakage,
                "mark_cost": mark_cost, "mean_cost": mean_cost,
                "decrement_upper": bound,
            }
            if dense:
                inverse_d = 1 / (d + delta)
                L = (comp.T * inverse_d) @ comp
                r = comp.T @ (theta * x)
                correction = float(r @ np.linalg.solve(L, r))
                fdelta = float(root @ np.linalg.solve(T + delta * np.eye(len(T)), root))
                decrement = b * b * (f0 - fdelta)
                low = float(masses[values <= delta].sum())
                error = abs(decrement - spatial - correction)
                tail.update({
                    "decrement": decrement, "complement_correction": correction,
                    "decomposition_error": error, "source_inverse_tail": low,
                    "decrement_bound_slack": bound - decrement,
                    "tail_bound_slack": 2 * bound - low,
                })
                if error > 1e-7 or bound < decrement - 1e-8 or low > 2 * bound + 1e-8:
                    raise AssertionError(tail)
            emit({**row, **tail})


def model(t, tau):
    """Seven-dimensional invariant block of an exact stationary reflection.

    Coordinates 0..5 are normalized indicators of groups of the stated sizes.
    Coordinate 6 is a balanced unit vector inside group 4. This avoids forming
    the full n-by-n matrix and makes all source calculations exact block ones.
    """
    n = 2 * t ** 8
    m = t ** 5
    M = (n - 2 - 2 * m) // 2
    H = float(t * t)
    c = tau / n
    W = 1 + (n - 1) * c
    a = sqrt(W / n)
    rho = tau / W
    sizes = np.array([1, 1, m, m, M, M], dtype=float)
    roots = np.sqrt(sizes)
    Lsum = (n * sqrt(W) - sqrt(n) - sqrt(tau) - m * (H + tau / H)) / M
    if Lsum <= 2 * sqrt(tau):
        raise ValueError("increase t")
    Lhi = (Lsum + sqrt(Lsum * Lsum - 4 * tau)) / 2
    Llo = tau / Lhi
    avals = np.array([1, sqrt(c), H / sqrt(n), tau / (H * sqrt(n)),
                      Lhi / sqrt(n), Llo / sqrt(n)])
    bvals = avals[[0, 1, 3, 2, 5, 4]]
    j = np.r_[roots / sqrt(n), 0.0]
    A = np.r_[avals * roots, 0.0]
    B = np.r_[bvals * roots, 0.0]
    x, y = A - a * sqrt(n) * j, B - a * sqrt(n) * j
    E = float(x @ x)
    g, h = x / sqrt(E), y / sqrt(E)
    e0 = np.eye(1, 7, 0).ravel()
    alpha = x[0] / sqrt(E)
    z = e0 - j / sqrt(n) - alpha * g - alpha * h
    z /= np.linalg.norm(z)
    w = np.eye(1, 7, 6).ravel()
    lp = .5 - 1 / n - alpha * alpha
    lm = .5 - alpha * alpha
    if lp <= 0:
        raise ValueError("increase t")
    p = (sqrt(lp) * z + sqrt(lm) * w) / sqrt(lp + lm)
    pos = np.column_stack((g, p))
    Pp = pos @ pos.T
    Pm = np.eye(7) - np.outer(j, j) - Pp
    K = 2 * Pp + np.outer(j, j) - np.eye(7)
    # Multiplication by a group-constant scalar acts on w by its group-4 value.
    dvals = c / (a * avals)
    d = np.r_[dvals, dvals[4]]
    dmvals = c / (a * bvals)
    dm = np.r_[dmvals, dmvals[4]]
    T = (pos.T * d) @ pos
    val, vec = np.linalg.eigh(T)
    b = 1 - c
    source = pos[0]
    inverse_mass = b * b * (vec.T @ source) ** 2 / val
    Q = (1 - c) * (1 - a)
    action_error = float(np.linalg.norm(T @ (pos.T @ x) - b * source))
    root_row = K @ e0
    root_entry_scaled = max(abs(root_row[i]) / roots[i] for i in range(1, 6)) * sqrt(n)
    # w is balanced on M-1 points; its root-row contribution is bounded this way.
    root_entry_scaled += abs(root_row[6]) * sqrt(n / (M - 1))
    rows = {
        "kind": "exact_reflection_model", "t": t, "n": n, "tau": tau,
        "m": m, "M": M, "H": H, "background_high": Lhi,
        "energy": E, "energy_over_t": E / t,
        "energy_over_sqrt_n": E / sqrt(n),
        "normalized_tail_first_mass": float(2 * m * H / n),
        "scaled_root_row_upper": root_entry_scaled,
        "mean_error": float(max(abs(A @ j - sqrt(W)), abs(B @ j - sqrt(W)))),
        "orthogonality_relative_error": float(abs(x @ y) / max(1, E)),
        "reflection_error": float(np.linalg.norm(K @ K - np.eye(7) + np.outer(j, j))),
        "stationary_error": float(np.linalg.norm(K @ (A + B) - (A - B))),
        "mark_diagonal_error": float(abs(K[0, 0] + 1 / n)),
        "positive_source_error": action_error,
        "opposite_positive_source_error": float(np.linalg.norm(Pm @ (dm * y) - b * Pm @ e0)),
        "coordinate_product_error": float(np.max(np.abs(
            avals * bvals - np.r_[1.0, np.full(5, c)]))),
        "diagonal_pair_bulk_error": float(np.max(np.abs(dvals[1:] * dmvals[1:] - rho))),
        "diagonal_pair_mark_error": float(abs(dvals[0] * dmvals[0] - rho * c)),
        "coordinate_cap_slack": float(1 - max(np.max(avals[1:]), np.max(bvals[1:]))),
        "inverse_energy_mass": float(inverse_mass.sum()),
        "inverse_energy_identity_error": float(abs(inverse_mass.sum() - Q)),
        "small_eigenvalue": float(val[0]), "large_eigenvalue": float(val[-1]),
        "low_inverse_energy_mass": float(inverse_mass[0]),
        "second_inverse_source_energy_error": float(abs(
            np.sum(b * b * (vec.T @ source) ** 2 / val ** 2) / E - 1)),
    }
    for delta in (0.01, 0.05, 0.2):
        theta = delta / (d + delta)
        tv = theta * x
        k = tv[0]
        tv[0] = 0
        leak = Pm @ tv
        meanpart = j @ tv
        leakage = float(np.sum((d + delta) * leak * leak))
        spatial = float(delta * np.sum(d / (d + delta) * x * x))
        mean_cost = abs(meanpart) * sqrt(float(sizes @ (dvals + delta)) / n)
        bound = spatial + (abs(k) * sqrt(d[0] + delta) + mean_cost + sqrt(leakage)) ** 2
        decrement = float(np.sum(inverse_mass * delta / (val + delta)))
        if decrement > bound + 1e-7:
            raise AssertionError((t, decrement, bound))
        emit({**rows, "delta": delta, "spatial": spatial,
              "opposite_leakage_squared": leakage, "decrement": decrement,
              "decrement_upper": bound})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model-only", action="store_true")
    args = parser.parse_args()
    for t in (3, 5, 10, 30, 100, 300, 1000):
        model(t, .05)
    if not args.model_only:
        for q, ch, dense in ((101, 101, True), (401, 401, True),
                             (289, 17, True), (961, 31, True),
                             (9413, 9413, False), (9409, 97, False)):
            analyze_paley(q, ch, .05, dense)


if __name__ == "__main__":
    main()
