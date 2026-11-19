"""Round 31: an exact stationary coherent-reflection counterfamily.

The proof, including the uniform coherence of the full completion, is in the
matching Markdown note. Large examples use their exact invariant 8D block.
Two small examples, seeded by Walsh and actual prime Paley matrices, construct
and check every entry of completed reflections. Their helpers use a deterministic
seeded numerical nullspace construction, not
the sparse cube-vertex existence construction used in the asymptotic proof.
All output is floating-point replay, not interval certification. No file writes.
"""

import argparse
import json
from math import isqrt, sqrt

import numpy as np


def emit(row):
    print(json.dumps(row, sort_keys=True), flush=True)


def build_block(n, m, H, tau=0.05, dfrac=0.6):
    """Normalized group indicators: root, neutral, tails +/-, backgrounds 1..4."""
    neutral = 2 * m - 1
    M = n // 4 - m
    assert n % 4 == 0 and M > 0
    sizes = np.array([1, neutral, m, m, M, M, M, M], dtype=float)
    roots = np.sqrt(sizes)
    c = tau / n
    W = 1 + (n - 1) * c
    s, a = sqrt(W), sqrt(W / n)
    d = dfrac * (sqrt(1 + tau) - sqrt(tau))
    S = (n * s - sqrt(n) - neutral * sqrt(tau) - m * (H + tau / H)) / (4 * M)
    levels = np.array([S + d, S - d])
    if min(levels) <= sqrt(tau):
        raise ValueError("background levels not positive: increase n / reduce H")
    odd_levels = np.sqrt(levels * levels - tau)
    avals = np.array([
        1, sqrt(c), H / sqrt(n), tau / (H * sqrt(n)),
        (levels[0] + odd_levels[0]) / sqrt(n),
        (levels[0] - odd_levels[0]) / sqrt(n),
        (levels[1] + odd_levels[1]) / sqrt(n),
        (levels[1] - odd_levels[1]) / sqrt(n),
    ])
    # Use reciprocal division for the small background values.
    avals[5] = c / avals[4]
    avals[7] = c / avals[6]
    bvals = avals[[0, 1, 3, 2, 5, 4, 7, 6]]
    j = roots / sqrt(n)
    A, B = avals * roots, bvals * roots
    x, y = A - a * roots, B - a * roots
    E = float(x @ x)
    k = 1 - a
    s_neutral = (sqrt(tau) - s) / sqrt(n)
    s_background = (S - s) / sqrt(n)
    qvals = np.zeros(8)
    qvals[0] = -1 / n
    qvals[1] = (k - s_background) / (n * neutral * (s_neutral - s_background))
    qvals[4:] = (1 / n - neutral * qvals[1]) / (4 * M)
    q = qvals * roots
    beta = 2 * M / n
    R2 = 1 - 1 / n - float(q @ q)
    odd_norm2 = float(odd_levels @ odd_levels)
    extra = R2 / beta - k * k / (beta * beta * odd_norm2)
    if extra <= 0:
        raise ValueError("root row not feasible: increase t / reduce H")
    # The minus branch gives a larger nonzero limiting inverse leakage.
    coeff = k * odd_levels / (beta * odd_norm2)
    coeff -= sqrt(extra) * np.array([-odd_levels[1], odd_levels[0]]) / sqrt(odd_norm2)
    r = q.copy()
    r[4:] += np.array([coeff[0], -coeff[0], coeff[1], -coeff[1]]) * sqrt(M / n)
    root = np.eye(1, 8, 0).ravel()
    ep = (root - j / sqrt(n) + r) / 2
    em = (root - j / sqrt(n) - r) / 2
    lp, lm = 0.5 - 1 / n, 0.5
    up, um = ep / sqrt(lp), em / sqrt(lm)
    X = x - (k / lp) * ep
    Y = y - (k / lm) * em
    EX = float(X @ X)
    if EX <= 0:
        raise ValueError("empty positive residual")
    g = X / sqrt(EX)
    plus = np.column_stack([up, g])
    Pp = plus @ plus.T
    Pm = np.eye(8) - np.outer(j, j) - Pp
    dvals = c / (a * avals)
    dmvals = c / (a * bvals)
    T = (plus.T * dvals) @ plus
    values, vec = np.linalg.eigh(T)
    b = 1 - c
    source = np.array([sqrt(lp), 0.0])
    invmass = b * b * (vec.T @ source) ** 2 / values
    Q = b * k
    F = float(X @ (dvals * X))
    root_coherence = float(np.max(np.abs(r / roots)) * sqrt(n))
    first_source_moment = float(ep @ (dvals * ep))
    coherent_moment_bound = lp * lp * dvals[0] + (root_coherence + 1 / sqrt(n)) ** 2 / 4
    retained_checks = []
    for epsilon in (0.001, 0.01, 0.1):
        lower = b * b / coherent_moment_bound * max(0., lp - epsilon * Q / (b * b)) ** 2
        actual = float(invmass[values > epsilon].sum())
        assert actual >= lower - 1e-8
        retained_checks.append({"epsilon": epsilon, "retained_inverse_mass": actual,
                                "coherent_lower_bound": lower})
    assert first_source_moment <= coherent_moment_bound + 1e-8
    exact_T = np.array([
        [lp * (Q + F) / (k * k), -sqrt(lp) * F / (k * sqrt(EX))],
        [-sqrt(lp) * F / (k * sqrt(EX)), F / EX],
    ])
    errors = {
        "mass_error": max(abs(A @ j - s), abs(B @ j - s)),
        "pair_product_error": float(np.max(np.abs(avals * bvals - np.r_[1., np.full(7, c)]))),
        "center_orthogonality_error": float(abs(x @ y)),
        "root_row_mean_error": float(abs(j @ r)),
        "root_row_norm_error": abs(float(r @ r) - (1 - 1 / n)),
        "root_row_diagonal_error": abs(r[0] + 1 / n),
        "root_row_pairing_error": max(abs(r @ x - k), abs(r @ y + k)),
        "plus_orthogonality_error": float(np.linalg.norm(plus.T @ plus - np.eye(2))),
        "source_equation_error": float(np.linalg.norm(T @ (plus.T @ x) - b * source)),
        "minus_source_equation_error": float(np.linalg.norm(Pm @ (dmvals * y) - b * em)),
        "source_matrix_formula_error": float(np.linalg.norm(T - exact_T)),
        "inverse_first_identity_error": abs(float(invmass.sum()) - Q),
        "inverse_second_relative_error": abs(float(np.sum(invmass / values)) / E - 1),
        "bulk_diagonal_product_error": float(np.max(np.abs(dvals[1:] * dmvals[1:] - tau / W))),
        "marked_diagonal_product_error": abs(float(dvals[0] * dmvals[0]) - tau * c / W),
    }
    for key, error in errors.items():
        # Absolute cancellation of orthogonality at huge energy is not used.
        scale = max(1., E) if key == "center_orthogonality_error" else 1.
        if error / scale > 2e-8:
            raise AssertionError((key, error, scale))
    row = {
        "kind": "invariant_exact_stationary_block", "n": n, "m": m,
        "H": H, "tau": tau, "background_offset": d, "background_mean": S,
        "energy_plus": E, "energy_minus": float(y @ y),
        "energy_over_sqrt_n": E / sqrt(n),
        "tail_source_first_mass": 2 * m / n * (H + tau / H - 2 * sqrt(tau)),
        "root_row_scaled_max": root_coherence,
        "root_marker": 0., "weighted_residual_energy_F": F,
        "first_source_moment": first_source_moment,
        "coherent_first_source_moment_upper": coherent_moment_bound,
        "retained_mass_checks": retained_checks,
        "small_eigenvalue": float(values[0]), "large_eigenvalue": float(values[1]),
        "small_inverse_first_mass": float(invmass[0]),
        "large_inverse_first_mass": float(invmass[1]), "total_inverse_first_mass": float(invmass.sum()),
        "coordinate_cap_slack": float(1 - max(np.max(avals[1:]), np.max(bvals[1:]))),
        **{key: float(value) for key, value in errors.items()},
    }
    tails = []
    for delta in (0.001, 0.01, 0.1):
        theta = delta / (dvals + delta)
        truncated = theta * x
        mark = truncated[0]
        truncated[0] = 0
        leak = Pm @ truncated
        ell2 = float(np.sum((dvals + delta) * leak * leak))
        spatial = float(np.sum(delta * dvals / (dvals + delta) * x * x))
        mean = float(j @ truncated) / sqrt(n)
        mean_cost = abs(mean) * sqrt(float(sizes @ (dvals + delta)))
        mark_cost = abs(mark) * sqrt(dvals[0] + delta)
        decrement = float(np.sum(invmass * delta / (values + delta)))
        certificate = spatial + (mark_cost + mean_cost + sqrt(ell2)) ** 2
        if decrement > certificate + 1e-8:
            raise AssertionError((delta, decrement, certificate))
        tails.append({"delta": delta, "opposite_leakage_squared": ell2,
                      "spatial": spatial, "mark_cost": mark_cost,
                      "mean_cost": mean_cost, "decrement": decrement,
                      "decrement_upper": certificate})
    row["tail_certificates"] = tails
    return locals()


def limiting_row(tau=0.05, dfrac=0.6):
    s = sqrt(1 + tau)
    d = dfrac * (s - sqrt(tau))
    levels = np.array([s + d, s - d])
    D = np.sqrt(levels * levels - tau)
    norm2 = float(D @ D)
    coeff = 2 * D / norm2 - sqrt(2 - 4 / norm2) * np.array([-D[1], D[0]]) / sqrt(norm2)
    offsets = np.array([d, -d])
    odd_residual = D - coeff
    F = float(np.sum(levels * (offsets ** 2 + odd_residual ** 2)
                        - 2 * D * offsets * odd_residual) / (2 * s))
    assert F > 0
    return {"kind": "algebraic_limit", "tau": tau, "background_offset": d,
            "root_background_coefficients": coeff.tolist(), "F_limit": F,
            "small_inverse_first_mass_limit": F / (1 + F),
            "large_inverse_first_mass_limit": 1 / (1 + F),
            "small_eigenvalue_times_energy_limit": F / (1 + F)}


def fwht(vector):
    out = np.asarray(vector, dtype=float).copy()
    step = 1
    while step < len(out):
        blocks = out.reshape(-1, 2 * step)
        left, right = blocks[:, :step].copy(), blocks[:, step:].copy()
        blocks[:, :step], blocks[:, step:] = left + right, left - right
        step *= 2
    return out


def prime_paley_multiplier(prime):
    """Exact integer Legendre signs; no numerical stationary solve or imports."""
    assert prime % 8 == 1
    assert all(prime % divisor for divisor in range(2, isqrt(prime) + 1))
    factors = []
    remaining = prime - 1
    for divisor in range(2, isqrt(remaining) + 1):
        if remaining % divisor == 0:
            factors.append(divisor)
            while remaining % divisor == 0:
                remaining //= divisor
    if remaining > 1:
        factors.append(remaining)
    generator = next(base for base in range(2, prime)
                     if all(pow(base, (prime - 1) // factor, prime) != 1 for factor in factors))
    character = np.full(prime, -1, dtype=np.int8)
    character[0] = 0
    character[[value * value % prime for value in range(1, (prime + 1) // 2)]] = 1
    multiplier = np.array([character[(1 - pow(generator, 2 * index, prime)) % prime]
                           for index in range((prime - 1) // 2)])
    assert multiplier.sum() == -1 and multiplier[0] == 0
    return multiplier


def full_replay(seed_kind="walsh"):
    """Small auxiliary members; asymptotic family uses H=t^3, not this H=4."""
    prime = 1033 if seed_kind == "prime_paley" else None
    n, m, H = (prime - 1) // 2 if prime else 512, 16, 4.
    model = build_block(n, m, H)
    indices = np.arange(n)
    if prime:
        multiplier = prime_paley_multiplier(prime)
        transform = np.fft.ifft(multiplier)
        assert np.max(np.abs(transform.imag)) < 1e-12
        kernel = transform.real
        K0 = kernel[(indices[:, None] - indices[None, :]) % n]
        cosets = [indices[indices % 4 == k] for k in range(4)]
    else:
        # f(u,z)=(-1)^(u+z1*z2+z3*z4+...). At n=512 there are four pairs.
        parity = indices & 1
        for bit in range(1, 9, 2):
            parity ^= ((indices >> bit) & 1) * ((indices >> (bit + 1)) & 1)
        multiplier = 1. - 2. * parity
        multiplier[0] = 0
        kernel = fwht(multiplier) / n
        K0 = kernel[np.bitwise_xor.outer(indices, indices)]
        cosets = [indices[((indices >> 1) & 3) == k] for k in range(4)]
    # Index-four cosets, with exactly m removed from each, in either group.
    removed = np.sort(np.concatenate([group[:m] for group in cosets]))
    assert removed[0] == 0
    groups = [np.array([0]), removed[2 * m + 1:],
              removed[1:m + 1], removed[m + 1:2 * m + 1]]
    groups += [group[m:] for group in cosets]
    indicators = np.zeros((n, 8))
    for col, group in enumerate(groups):
        indicators[group, col] = 1 / sqrt(len(group))
    assert np.linalg.norm(indicators.T @ indicators - np.eye(8)) < 1e-12
    assert np.array_equal(np.array([len(group) for group in groups]), model["sizes"])
    r = indicators @ model["r"]
    r0 = K0[:, 0]
    w0 = (r0 - r) / np.linalg.norm(r0 - r)
    U0 = np.eye(n) - 2 * np.outer(w0, w0)
    K1 = U0 @ K0 @ U0
    # Orthonormal basis of F intersect span{j,e0,r}^perp, starting with g.
    root_basis = indicators @ np.column_stack([model["j"], model["up"], model["um"]])
    seeds = [indicators @ model["g"], indicators @ model["Y"]]
    seeds += [indicators[:, i] for i in range(8)]
    zlist = []
    for seed in seeds:
        z = seed - root_basis @ (root_basis.T @ seed)
        for old in zlist:
            z -= old * (old @ z)
        if np.linalg.norm(z) > 1e-9:
            zlist.append(z / np.linalg.norm(z))
    assert len(zlist) == 5
    signs = [1, -1, -1, -1, -1]
    rng = np.random.default_rng(310031)
    plist = []
    helper_errors = []
    P = np.eye(n) - np.ones((n, n)) / n
    for z, sign in zip(zlist, signs):
        sector = (P + sign * K1) / 2
        forbidden = [sector @ indicators]
        forbidden += [old[:, None] for old, old_sign in zip(plist, signs) if old_sign == sign]
        forbidden = np.column_stack(forbidden)
        left, values, _ = np.linalg.svd(forbidden, full_matrices=False)
        basis = left[:, values > 1e-10]
        p = sector @ rng.normal(size=n)
        p -= basis @ (basis.T @ p)
        p /= np.linalg.norm(p)
        plist.append(p)
        helper_errors.append(max(float(np.linalg.norm(K1 @ p - sign * p)),
                                 float(np.linalg.norm(indicators.T @ p))))
    rotate = np.column_stack([(z - p) / sqrt(2) for z, p in zip(zlist, plist)])
    U = np.eye(n) - 2 * rotate @ rotate.T
    K = U @ K1 @ U
    A, B = indicators @ model["A"], indicators @ model["B"]
    x, y = indicators @ model["x"], indicators @ model["y"]
    j = np.ones(n) / sqrt(n)
    e0 = np.eye(1, n, 0).ravel()
    positive = (P + K) / 2
    fullplus = indicators @ model["plus"]
    weights = np.full(n, model["c"])
    weights[0] = 1
    activation = np.sqrt((A - B) ** 2 + 4 * weights)
    dvals = model["c"] / (model["a"] * A)
    common_character = np.exp(2j * np.pi * indices / 4) if prime else 1. - 2. * ((indices >> 2) & 1)
    error = {
        "symmetry_error": np.linalg.norm(K - K.T),
        "reflection_error": np.linalg.norm(K @ K - P),
        "constant_error": np.linalg.norm(K @ j),
        "root_row_error": np.linalg.norm(K[:, 0] - r),
        "plus_vector_error": np.linalg.norm(K @ x - x),
        "minus_vector_error": np.linalg.norm(K @ y + y),
        "stationary_error": np.linalg.norm(K @ activation - (A - B)),
        "block_invariance_error": np.linalg.norm(K @ indicators - indicators @ (indicators.T @ K @ indicators)),
        "full_source_error": np.linalg.norm(positive @ (dvals * x) - (1 - model["c"]) * (positive @ e0)),
        "full_source_block_error": np.linalg.norm(positive @ (dvals[:, None] * fullplus) - fullplus @ model["T"]),
        "helpers_error": max(helper_errors),
    }
    assert max(error.values()) < 1e-8, error
    eigenvalues = np.linalg.eigvalsh(K)
    plus_dim, minus_dim = int(np.sum(eigenvalues > .5)), int(np.sum(eigenvalues < -.5))
    assert (plus_dim, minus_dim) == ((n - 2) // 2, n // 2)
    V = U @ U0
    conjugation_error = float(np.linalg.norm(K - V @ K0 @ V.T))
    rank_rotation = int(np.linalg.matrix_rank(V - np.eye(n), tol=1e-8))
    difference_singular_values = np.linalg.svd(K - K0, compute_uv=False)
    rank_difference = int(np.sum(difference_singular_values > 1e-8))
    assert rank_rotation <= 6 and rank_difference <= 12 and conjugation_error < 1e-8
    common_A, common_B = common_character @ A / sqrt(n), common_character @ B / sqrt(n)
    translation_defect = np.linalg.norm(K - np.roll(K, (1, 1), axis=(0, 1))) if prime else np.linalg.norm(K - K[np.ix_(indices ^ 1, indices ^ 1)])
    assert translation_defect > .01
    emit({"kind": "full_matrix_stationary_replay", "seed_kind": seed_kind,
          "seed_prime": prime, "n": n, "m": m, "H": H,
          "note": "finite auxiliary parameters; no asymptotic inference from this row",
          "helper_method": "seeded projected numerical nullspace; proof uses sparse cube vertices",
          "every_entry_checked": n * n,
          "base_coherence_constant": float(np.max(np.abs(K0)) * sqrt(n)),
          "after_root_rotation_coherence_constant": float(np.max(np.abs(K1)) * sqrt(n)),
          "full_coherence_constant": float(np.max(np.abs(K)) * sqrt(n)),
          "root_row_coherence_constant": float(np.max(np.abs(K[:, 0])) * sqrt(n)),
          "plus_dimension": plus_dim, "minus_dimension": minus_dim,
          "root_diagonal": float(K[0, 0]),
          "root_plus_projector": float(positive[0, 0]),
          "centered_energy": model["E"],
          "small_inverse_first_mass": float(model["invmass"][0]),
          "common_character_A": [float(np.real(common_A)), float(np.imag(common_A))],
          "common_character_B": [float(np.real(common_B)), float(np.imag(common_B))],
          "conjugation_error": conjugation_error,
          "rank_rotation_minus_identity": rank_rotation,
          "rank_kernel_difference": rank_difference,
          "kernel_difference_operator_norm": float(difference_singular_values[0]),
          "root_row_difference_norm": float(np.linalg.norm(r - r0)),
          "translation_commutator_frobenius": float(translation_defect),
          "diagonal_nonconstancy": float(np.ptp(np.diag(K))),
          "full_helper_scaled_infinity_max": max(float(np.max(np.abs(p))) * n ** .25 for p in plist),
          **{key: float(value) for key, value in error.items()}})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--block-only", action="store_true")
    args = parser.parse_args()
    emit(limiting_row())
    for t in (8, 16, 32, 64, 256, 1024, 4096):
        model = build_block(2 * t ** 8, t ** 4, float(t ** 3))
        emit({"t": t, **model["row"]})
    if not args.block_only:
        full_replay()
        full_replay("prime_paley")


if __name__ == "__main__":
    main()
