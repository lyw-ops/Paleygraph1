"""Floating diagnostics for the actual reciprocal stationary source (Round 28).

All writes are made by shell redirection to the requested Round-28 prefix.
This script imports existing field construction and stationary solving only.
It does not claim interval certification or an asymptotic prime estimate.
"""

import argparse
import json
from math import sqrt
from pathlib import Path
import sys

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from poisson_weights import weighted_iterate
from smoothing import kernel_action
from square_control import square_field_sign
from theta import paley_sign


def project(sign, side, vector):
    coefficients = np.fft.rfft(vector)
    coefficients[0] = 0
    coefficients[1:] *= sign[1:len(coefficients)] == side
    return np.fft.irfft(coefficients, len(vector))


def even_basis(sign, side):
    """Orthonormal real, even basis of the nonconstant sector."""
    n = len(sign)
    modes = np.flatnonzero(sign[1:n // 2 + 1] == side) + 1
    columns = np.cos(2 * np.pi * np.outer(np.arange(n), modes) / n)
    columns *= sqrt(2 / n)
    if n % 2 == 0 and len(modes) and modes[-1] == n // 2:
        columns[:, -1] /= sqrt(2)
    return columns


def krylov_tests(matrix, source, max_steps):
    """Exhibit h with <source,h>=1 and small ||T h|| in source Krylov spaces.

    Full reorthogonalization is used. SVD on T times the basis avoids squaring
    the conditioning of the small least-squares problem.
    """
    columns = []
    vector = source / np.linalg.norm(source)
    records = []
    depths = {1, 4, 8, 16, 32, max_steps}
    for step in range(1, min(max_steps, len(source)) + 1):
        columns.append(vector)
        basis = np.column_stack(columns)
        if step in depths:
            transformed = matrix @ basis
            left, singular, right = np.linalg.svd(transformed, full_matrices=False)
            contrast = basis.T @ source
            rotated = right @ contrast
            keep = singular > 1e-13 * singular[0]
            inverse = np.zeros_like(singular)
            inverse[keep] = rotated[keep] / singular[keep] ** 2
            coefficients = right.T @ inverse
            denominator = contrast @ coefficients
            test = basis @ coefficients / denominator
            records.append({
                "depth": step,
                "test_norm": float(np.linalg.norm(matrix @ test)),
                "contrast_error": float(abs(source @ test - 1)),
                "h_norm": float(np.linalg.norm(test)),
            })
        vector = matrix @ vector
        for _ in range(2):
            vector -= basis @ (basis.T @ vector)
        norm = np.linalg.norm(vector)
        if norm < 1e-13:
            break
        vector /= norm
    return records


def analyze(order, characteristic, sign, tau, dense_max, krylov_steps):
    n = len(sign)
    weights = np.full(n, tau / n)
    weights[0] = 1
    c, total_weight = tau / n, float(weights.sum())
    a = sqrt(total_weight / n)
    v, u, residual = weighted_iterate(sign, weights, tolerance=2e-12, rounds=64)
    large = (u + np.abs(v)) / 2
    small = weights / large
    spectra = {
        1: np.where(v >= 0, large, small),
        -1: np.where(v >= 0, small, large),
    }
    if residual > 2e-9:
        raise RuntimeError(f"stationary solve unresolved: q={order}, tau={tau}, r={residual}")

    for side in (1, -1):
        spectrum = spectra[side]
        opposite = spectra[-side]
        root = float(spectrum[0])
        x = spectrum - a
        energy = float(x @ x)
        norm_squared = float(spectrum @ spectrum)
        b = (1 - c) / root
        diagonal = c / (a * spectrum)
        e = project(sign, side, np.eye(1, n, 0).ravel())
        source = b * e

        def action(z):
            return project(sign, side, diagonal * project(sign, side, z))

        source_error = float(np.linalg.norm(action(x) - source))
        dirichlet = float(x @ action(x))
        expected_dirichlet = (1 - c) * (1 - a / root)

        convolution = np.fft.irfft(np.fft.rfft(spectrum) ** 2, n)
        witness = convolution / norm_squared
        mass = float(witness.sum() / sqrt(n))
        witness_energy = float(witness[1:] @ witness[1:] / sqrt(n))
        expected_mass = sqrt(n) * total_weight / norm_squared
        positive_defect = max(0.0, 1 - 1.01 * mass)
        defect_lower = positive_defect ** 2 / witness_energy

        row = {
            "q": order, "characteristic": characteristic, "tau": tau, "side": side,
            "n": n, "stationary_residual": residual,
            "root": root, "centered_energy": energy,
            "centered_energy_over_sqrt_n": energy / sqrt(n),
            "exact_source_test_min": 1 / sqrt(energy),
            "source_error": source_error,
            "sector_error": float(np.linalg.norm(project(sign, side, x) - x)),
            "reciprocal_error": float(np.max(np.abs(spectrum * opposite - weights))),
            "mean_error": float(abs(spectrum.mean() - a)),
            "diagonal_pair_bulk_error": float(np.max(np.abs(
                diagonal[1:] * (c / (a * opposite[1:])) - tau / total_weight))),
            "dirichlet_error": abs(dirichlet - expected_dirichlet),
            "dirichlet": dirichlet,
            "autocorrelation_mass": mass,
            "autocorrelation_energy": witness_energy,
            "autocorrelation_mass_error": abs(mass - expected_mass),
            "autocorrelation_mark_error": abs(float(witness[0]) - 1),
            "autocorrelation_sector_error": float(np.linalg.norm(
                project(sign, side, witness) + witness.mean() - witness)),
            "autocorrelation_min": float(witness.min()),
            "autocorrelation_young_slack": mass - 1 / sqrt(n) - witness_energy,
            "ordinary_relaxed_defect_lower_mean_1p01": defect_lower,
        }
        if n <= dense_max:
            basis = even_basis(sign, side)
            matrix = (basis.T * diagonal) @ basis
            values, vectors = np.linalg.eigh(matrix)
            root_source = basis[0]
            spectral_source = vectors.T @ root_source
            spectral_x = b * spectral_source / values
            inverse_first = float(np.sum(spectral_source ** 2 / values))
            inverse_second = float(np.sum((spectral_source / values) ** 2))
            h_coordinates = vectors @ (b * spectral_source / values ** 2) / energy
            contrast = float(b * root_source @ h_coordinates)
            h_coordinates /= contrast
            h = basis @ h_coordinates
            transformed = diagonal * h
            signed_correlation = side * float(transformed @ kernel_action(sign, transformed))
            centered_transformed = transformed - transformed.mean()
            test_norm_squared = float(np.linalg.norm(action(h)) ** 2)
            cutoff = 2 * expected_dirichlet / energy
            slow_energy_fraction = float(np.sum(spectral_x[values <= cutoff] ** 2) / energy)
            cumulative = np.cumsum(spectral_x ** 2)
            median_index = min(np.searchsorted(cumulative, energy / 2), len(values) - 1)
            row.update({
                "sector_dimension_even": basis.shape[1],
                "smallest_eigenvalue": float(values[0]),
                "source_energy_median_eigenvalue": float(values[median_index]),
                "source_energy_cutoff": cutoff,
                "source_energy_fraction_below_cutoff": slow_energy_fraction,
                "first_inverse_moment_error": abs(inverse_first - root * (root - a) / (1 - c)),
                "second_inverse_moment_relative_error": abs(inverse_second * b * b / energy - 1),
                "explicit_test_norm": sqrt(test_norm_squared),
                "explicit_test_root_error": abs(float(h[0]) - root / (1 - c)),
                "explicit_test_norm_relative_error": abs(test_norm_squared * energy - 1),
                "signed_test_identity_error": abs(
                    2 * test_norm_squared - centered_transformed @ centered_transformed - signed_correlation),
                "signed_test_correlation": signed_correlation,
                "signed_test_centered_norm_squared": float(centered_transformed @ centered_transformed),
                "source_krylov_tests": krylov_tests(matrix, b * root_source, krylov_steps),
            })
        identity_keys = [
            "reciprocal_error", "mean_error", "diagonal_pair_bulk_error",
            "dirichlet_error", "autocorrelation_mass_error", "autocorrelation_mark_error",
        ]
        if max(row[key] for key in identity_keys) > 2e-8 or source_error > 2e-8:
            raise RuntimeError(f"failed identity at q={order}, side={side}: {row}")
        if row["autocorrelation_young_slack"] < -2e-8:
            raise RuntimeError("Young bound failed")
        if "source_energy_fraction_below_cutoff" in row and row["source_energy_fraction_below_cutoff"] < .5 - 2e-8:
            raise RuntimeError("source-window extraction failed")
        yield row


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--primes", nargs="+", type=int, default=[1009, 4001, 9413])
    parser.add_argument("--square-roots", nargs="+", type=int, default=[31, 61, 97])
    parser.add_argument("--tau", nargs="+", type=float, default=[.05, .005])
    parser.add_argument("--inverse-n-floor", action="store_true")
    parser.add_argument("--dense-max", type=int, default=2000)
    parser.add_argument("--krylov-steps", type=int, default=32)
    args = parser.parse_args()
    fields = [(p, p) for p in args.primes] + [(r * r, r) for r in args.square_roots]
    for order, characteristic in sorted(fields):
        sign = paley_sign(order) if order == characteristic else square_field_sign(characteristic)
        floors = list(args.tau) + ([1 / len(sign)] if args.inverse_n_floor else [])
        for tau in floors:
            for row in analyze(order, characteristic, sign, tau, args.dense_max, args.krylov_steps):
                print(json.dumps(row, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
