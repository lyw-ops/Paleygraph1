"""Measure the exterior signs and localized eigenspaces at random weights."""

import argparse
import csv
import sys

import numpy as np
from scipy.linalg import lstsq

from face_ranks import spectrum_basis, spectrum_vertices
from square_control import square_field_sign
from theta import paley_sign


def positive_optimum(weights, spectrum, basis):
    """Optimize the log objective in the positive affine Fourier space."""
    if basis.shape[1] == 0:
        return spectrum, 0.0

    root_weights = np.sqrt(weights)
    for _ in range(120):
        reciprocal = weights / spectrum
        residual = len(weights) * np.max(np.abs(basis.T @ reciprocal))
        if residual < 1e-8:
            return spectrum, residual

        weighted_basis = basis * (root_weights / spectrum)[:, None]
        coefficients = lstsq(weighted_basis, root_weights, lapack_driver="gelsy")[0]
        relative_direction = (basis @ coefficients) / spectrum
        negative = relative_direction < 0
        step = min(1, np.min(-0.99 / relative_direction[negative], initial=np.inf))
        increase = weights @ relative_direction
        while weights @ np.log1p(step * relative_direction) < 0.1 * step * increase - 1e-16:
            step /= 2
            if step < 1e-8:
                raise RuntimeError(f"line search stalled at residual {residual:.3g}")
        spectrum = spectrum * (1 + step * relative_direction)
    raise RuntimeError(f"log solve stalled at residual {residual:.3g}")


def floored_pair(weights, basis):
    outside = weights == 0
    floor_masses = (1e-2, 1e-4, 1e-6, 1e-8) if np.any(outside) else (0.0,)
    floor_profile = outside / max(1, np.count_nonzero(outside))
    plus = np.ones(len(weights))
    for floor_mass in floor_masses:
        floored_weights = (weights + floor_mass * floor_profile) / (1 + floor_mass)
        plus, residual = positive_optimum(floored_weights, plus, basis)
        minus = len(weights) * floored_weights / plus
        if floor_mass == 1e-6:
            previous_positive = plus[outside] > minus[outside]

    contrast = (plus[outside] - minus[outside]) / (plus[outside] + minus[outside])
    resolved = len(contrast) == 0 or (
        np.array_equal(previous_positive, contrast > 0) and np.min(np.abs(contrast)) > 0.9
    )
    return plus, minus, residual, resolved


def localized_dimension(kernel, support, side):
    """Count eigenvalues at the signed endpoint, using a numerical tolerance."""
    compression = side * kernel[np.ix_(support, support)]
    return np.count_nonzero(np.linalg.eigvalsh(compression) > 1 - 1e-9)


def exposed_rank(vertices, support, normal, score_tolerance):
    points = vertices[:, support]
    values = points @ normal
    face = points[values > np.max(values) - score_tolerance]
    return np.linalg.matrix_rank(face - face[0], tol=1e-7)


def check_ranks(vertices, weights, plus, minus, basis, ranks):
    support = weights > 0

    def matches(spectra, tolerance):
        measured = [exposed_rank(polytope, support, weights[support] / spectrum[support], tolerance)
                    for polytope, spectrum in zip(vertices, spectra)]
        return measured == ranks

    if matches((plus, minus), 1e-6):
        return False, True
    if support.all():
        return False, False

    # A finite floor perturbs the exposing normal, especially near a change of face.
    extra_floor = 1e-10
    floored_weights = (weights + extra_floor * ~support / np.count_nonzero(~support)) / (1 + extra_floor)
    refined_plus, _ = positive_optimum(floored_weights, plus, basis)
    refined_minus = len(weights) * floored_weights / refined_plus
    return True, matches((refined_plus, refined_minus), 1e-7)


def sample_weights(n, count, rng):
    labels = rng.integers(n, size=count)
    masses = rng.exponential(size=count)
    return np.bincount(labels, weights=masses, minlength=n) / masses.sum()


def probe(sign, sample_counts, samples, seed):
    n = len(sign)
    rng = np.random.default_rng(seed)
    basis = spectrum_basis(sign, 1)
    coordinates = np.arange(n)
    kernel = (np.fft.fft(sign).real / n)[(coordinates[:, None] - coordinates[None, :]) % n]
    vertices = [spectrum_vertices(sign, side) for side in (1, -1)] if n <= 20 else []

    for count in sample_counts:
        objectives = []
        missed = []
        partitions = []
        ranks_checked = 0
        refinements = 0
        disagreements = 0
        max_residual = 0.0
        for _ in range(samples):
            weights = sample_weights(n, count, rng)
            plus, minus, residual, resolved = floored_pair(weights, basis)
            max_residual = max(max_residual, residual)
            support = weights > 0
            objectives.append(weights[support] @ (np.log(plus[support]) - np.log(minus[support])))
            ell_plus_missed = localized_dimension(kernel, ~support, 1)
            ell_minus_missed = localized_dimension(kernel, ~support, -1)
            missed.append((np.count_nonzero(~support), ell_plus_missed, ell_minus_missed))
            if not resolved:
                continue

            plus_only = ~support & (plus > minus)
            minus_only = ~support & (minus > plus)
            sign_count = np.count_nonzero(plus_only) - np.count_nonzero(minus_only)
            ell_plus = localized_dimension(kernel, plus_only, 1)
            ell_minus = localized_dimension(kernel, minus_only, -1)
            plus_rank = basis.shape[1] - np.count_nonzero(minus_only) + ell_minus - ell_plus
            minus_rank = np.count_nonzero(support) - 1 - plus_rank
            partitions.append((sign_count, ell_plus, ell_minus, plus_rank - minus_rank))
            if vertices:
                ranks_checked += 1
                refined, matched = check_ranks(vertices, weights, plus, minus, basis, [plus_rank, minus_rank])
                refinements += refined
                disagreements += not matched

        averaged_partitions = tuple(np.mean(partitions, axis=0)) if partitions else ("",) * 4
        yield (
            count, samples, len(partitions), *np.mean(missed, axis=0), *averaged_partitions,
            np.mean(objectives), np.std(objectives, ddof=1) / np.sqrt(samples),
            ranks_checked, refinements, disagreements, max_residual,
        )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primes", type=int, nargs="*")
    parser.add_argument("--square-characteristics", type=int, nargs="*", default=[])
    parser.add_argument("--labels", type=int, nargs="+", default=[1, 2, 4, 8, 16, 32, 64, 128, 256])
    parser.add_argument("--samples", type=int, default=24)
    parser.add_argument("--seed", type=int, default=26)
    args = parser.parse_args()
    orders = [(prime, "prime", paley_sign) for prime in args.primes]
    orders += [(prime, "prime-square", square_field_sign) for prime in args.square_characteristics]
    if not orders or args.samples < 2 or min(args.labels) < 1:
        parser.error("provide field orders, at least two samples, and positive label counts")

    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow((
        "q", "kind", "n", "labels", "samples", "resolved_partitions", "missed_mean",
        "missed_plus_dim_mean", "missed_minus_dim_mean", "exterior_sign_count_mean",
        "exterior_plus_dim_mean", "exterior_minus_dim_mean", "rank_difference_mean",
        "log_optimum_difference_mean", "log_optimum_difference_se", "vertex_rank_checks",
        "vertex_rank_refinements", "vertex_rank_disagreements", "max_stationary_residual",
    ))
    for prime, kind, field_sign in orders:
        sign = field_sign(prime)
        n = len(sign)
        for result in probe(sign, args.labels, args.samples, args.seed):
            writer.writerow((2 * n + 1, kind, n, *result))


if __name__ == "__main__":
    main()
