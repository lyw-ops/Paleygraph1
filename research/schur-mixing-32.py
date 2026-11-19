"""Round 32: exact Schur spectra and actual marked first-moment diagnostics.

Integer convolution checks are exact; stationary and conjugation rows are
floating diagnostics, not interval certificates or asymptotic proofs.
"""

import argparse
import json
from math import sqrt
from pathlib import Path
import sys

import numpy as np
from flint import fmpz_poly

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from poisson_weights import weighted_iterate
from smoothing import kernel_action
from square_control import square_field_sign
from theta import paley_sign, prime_field_generator


def cyclic_integer(left, right):
    n = len(left)
    modulus = fmpz_poly([-1] + [0] * (n - 1) + [1])
    result = [int(x) for x in ((fmpz_poly(left) * fmpz_poly(right)) % modulus).coeffs()]
    return result + [0] * (n - len(result))


def exact_spectrum(q, characteristic):
    sign = paley_sign(q) if q == characteristic else square_field_sign(characteristic)
    n = len(sign)
    s = [int(x) for x in sign]
    positive, negative = [int(x == 1) for x in s], [int(x == -1) for x in s]
    cross = cyclic_integer(positive, negative)
    double = cyclic_integer(s, s)
    assert cross[0] == 0 and double[0] == n - 1
    assert all(4 * cross[i] == n - 2 - double[i] for i in range(1, n))
    legendre = [2 * double[i] + 2 for i in range(1, n)]
    assert all(value * value <= 4 * q for value in legendre)
    direct_legendre = q == characteristic
    if direct_legendre:
        generator = pow(prime_field_generator(q), 2, q)
        chi = [0] + [1 if pow(x, (q - 1) // 2, q) == 1 else -1 for x in range(1, q)]
        for i in range(1, n):
            a = pow(generator, i, q)
            value = sum(chi[v * (v - 1) * (v - a) % q] for v in range(q))
            assert value == legendre[i - 1]
    k = kernel_action(sign, np.eye(1, n, 0).ravel())
    gram_spectrum = np.fft.fft(k * k).real
    exact_gram = np.array(double, dtype=float) / n
    numerical_error = float(np.max(np.abs(gram_spectrum - exact_gram)))
    assert numerical_error < 2e-12
    return {
        "kind": "exact_integer_schur_spectrum", "q": q, "n": n,
        "characteristic": characteristic, "nonzero_modes_checked": n - 1,
        "cross_count_min": min(cross[1:]), "cross_count_max": max(cross[1:]),
        "schur_gap_exact": f"{min(cross[1:])}/{n}",
        "schur_top_exact": f"{max(cross[1:])}/{n}",
        "legendre_min": min(legendre), "legendre_max": max(legendre),
        "direct_prime_legendre_check": direct_legendre,
        "integer_convolution_and_hasse_checks": True,
        "auxiliary_fft_error": numerical_error,
    }


def stationary(q, characteristic, tau):
    sign = paley_sign(q) if q == characteristic else square_field_sign(characteristic)
    n = len(sign)
    c = tau / n
    weights = np.full(n, c)
    weights[0] = 1
    W = float(weights.sum())
    a = sqrt(W / n)
    v, u, residual = weighted_iterate(sign, weights, tolerance=1e-11, rounds=64)
    assert residual < 2e-9
    large = (u + np.abs(v)) / 2
    small = weights / large
    A = np.where(v >= 0, large, small)
    B = weights / A
    root = np.eye(1, n, 0).ravel()
    k = kernel_action(sign, root)
    for side, spectrum, opposite in ((1, A, B), (-1, B, A)):
        e = (root - 1 / n + side * k) / 2
        p = float(e[0])
        diagonal = c / (a * spectrum)
        b = (1 - c) / spectrum[0]
        Q = (1 - c) * (1 - a / spectrum[0])
        moment = float(np.dot(diagonal, e * e))
        correlation = float(np.dot(opposite - a, k * k) / (4 * a))
        coefficient = 1 / (2 * n) - (1 + side) / (2 * n * n) + c * p * p
        formula = .25 - .5 / n + opposite[0] / a * coefficient + correlation
        error = abs(moment - formula)
        assert error < 2e-9
        yield {
            "kind": "floating_actual_stationary_first_moment", "q": q,
            "characteristic": characteristic, "n": n, "tau": tau,
            "side": side, "stationary_residual": float(residual),
            "root": float(spectrum[0]), "source_first_inverse_mass": float(Q),
            "marked_spectral_first_moment": moment,
            "seed_square_opposite_correlation": correlation,
            "exact_formula_error": error,
            "ordered_retained_inverse_mass_lower": b * b * p * p / moment,
            "max_escaping_inverse_mass_allowed_by_this_bound": max(0., Q - b * b * p * p / moment),
            "scope": "finite floating diagnostic; no prime-uniform tightness claim",
        }


def conjugation(prime):
    sign = paley_sign(prime)
    n = len(sign)
    k = kernel_action(sign, np.eye(1, n, 0).ravel())
    indices = np.arange(n)
    base = k[(indices[:, None] - indices[None, :]) % n]
    rng = np.random.default_rng(320032 + prime)
    direction = rng.choice([-1., 1.], n)
    direction[0] = 0
    direction[1:] -= direction[1:].mean()
    direction /= np.linalg.norm(direction)
    U = np.eye(n) - 2 * np.outer(direction, direction)
    changed = U @ base @ U
    difference = changed - base
    square_difference = changed * changed - base * base
    norm = float(np.max(np.abs(np.linalg.eigvalsh(square_difference))))
    bound = float(np.max(np.abs(changed + base)) * np.linalg.norm(difference))
    coherence_bound = float((np.max(np.abs(changed)) + np.max(np.abs(base))) * np.linalg.norm(difference))
    P = np.eye(n) - np.ones((n, n)) / n
    H = (P + changed) * (P - changed) / 4
    eig = np.linalg.eigvalsh(H)
    gap = float(eig[1])
    # The trivial cross-count is zero; take the nonconstant Fourier modes.
    counts = cyclic_integer([int(x == 1) for x in sign], [int(x == -1) for x in sign])
    base_gap = min(counts[1:]) / n
    assert norm <= bound + 1e-11 and bound <= coherence_bound + 1e-11
    assert gap >= base_gap - bound / 4 - 1e-11
    assert abs(eig[0]) < 1e-11
    reflection_error = float(np.linalg.norm(changed @ changed - P))
    assert reflection_error < 2e-10
    return {
        "kind": "floating_finite_rank_schur_stability", "q": prime, "n": n,
        "kernel_difference_rank_upper": 2,
        "kernel_difference_frobenius": float(np.linalg.norm(difference)),
        "schur_square_difference_operator": norm,
        "entrywise_frobenius_upper": bound,
        "coherence_frobenius_upper": coherence_bound,
        "base_cross_projector_gap": base_gap,
        "changed_cross_projector_gap": gap,
        "weyl_gap_lower": base_gap - bound / 4,
        "reflection_error": reflection_error,
        "scope": "auxiliary rank-two conjugation; not the stationary UI counterfamily",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--small-only", action="store_true")
    args = parser.parse_args()
    for q, p in ((13, 13), (41, 41), (101, 101), (401, 401), (121, 11), (361, 19)):
        print(json.dumps(exact_spectrum(q, p), sort_keys=True), flush=True)
    fields = [(401, 401), (9413, 9413), (9409, 97)]
    if not args.small_only:
        fields += [(153649, 153649), (151321, 389), (1000033, 1000033)]
    for q, p in fields:
        for row in stationary(q, p, .05):
            print(json.dumps(row, sort_keys=True), flush=True)
    for prime in (101, 401):
        print(json.dumps(conjugation(prime), sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
