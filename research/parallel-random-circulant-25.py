"""Compare the first Paley feedback fields with Gaussian tree normalization."""

import argparse
import json
from math import asinh, log, sqrt
from pathlib import Path
import sys

import numpy as np


sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from smoothing import kernel_action, smoothing
from square_control import square_field_sign
from theta import optimize, paley_sign


def moment_record(order, sign, square_root):
    n = len(sign)
    leaf = np.fft.fft(sign).real / sqrt(n)
    centered_square = leaf**2 - 1
    graft = kernel_action(sign, centered_square)
    leaf_second = float(np.mean(leaf**2))
    leaf_fourth = float(np.mean(leaf**4))
    graft_second = float(np.mean(graft**2))
    graft_fourth = float(np.mean(graft**4))
    norm_error = abs(graft_second - float(np.var(centered_square)))
    if abs(leaf_second - (n - 1)/n) > 2e-12 or norm_error > 2e-12:
        raise RuntimeError("a deterministic Fourier identity failed")
    record = dict(
        kind="moments",
        order=order,
        square_root=square_root,
        leaf_second=leaf_second,
        leaf_fourth=leaf_fourth,
        leaf_fourth_cumulant=leaf_fourth - 3*leaf_second**2,
        first_graft_second=graft_second,
        first_graft_fourth=graft_fourth,
        first_graft_fourth_cumulant=graft_fourth - 3*graft_second**2,
        first_graft_isometry_error=norm_error,
    )
    if square_root is not None:
        h = (square_root + 1)//2
        record["subfield_kernel_l2_over_l1"] = 1/sqrt(h)
        record["subfield_kernel_ratio_times_sqrt_n"] = sqrt(n/h)
    return record


def residual_record(order, sign, side, tau):
    multiplier = side*sign
    n = len(sign)
    reference, metrics = smoothing(multiplier, tau, 1e-12, 20000)
    if metrics[-2] > 1e-12:
        raise RuntimeError("the numerical stationary reference did not converge")
    weights = np.full(n, tau/n)
    weights[0] = 1
    total_weight = float(weights.sum())
    root = np.zeros(n)
    root[0] = 1
    trial = 2*kernel_action(multiplier, root)
    activation = np.sqrt(trial**2 + 4*weights)
    residual = trial - kernel_action(multiplier, activation)
    reference_activation = np.sqrt(reference**2 + 4*weights)
    positive_reference = (reference_activation + reference)/2
    positive_trial = (activation + trial)/2
    ratio = positive_trial/positive_reference
    discrepancy = float(np.sum(weights*(ratio + 1/ratio - 2)))
    expression = (
        sqrt(total_weight/n)*float(activation.sum())
        - 2*total_weight - .5*float(residual @ reference)
    )
    discrepancy_upper = (
        np.linalg.norm(trial) + .5*np.linalg.norm(reference)
    )*np.linalg.norm(residual)
    _, spectrum = optimize(sign, side)
    log_error = abs(log(spectrum[0]/sqrt(n)) - asinh(trial[0]/2))
    log_upper = .5*log(total_weight) + sqrt(max(discrepancy, 0))
    if abs(discrepancy - expression) > 2e-10:
        raise RuntimeError("the relative-discrepancy identity failed")
    if discrepancy > discrepancy_upper + 2e-10 or log_error > log_upper + 2e-10:
        raise RuntimeError("a deterministic residual comparison failed")
    return dict(
        kind="residual_smoke",
        order=order,
        side=side,
        tau=tau,
        stationary_residual=metrics[-2],
        relative_discrepancy=discrepancy,
        discrepancy_identity_error=abs(discrepancy - expression),
        discrepancy_upper=float(discrepancy_upper),
        log_error=float(log_error),
        log_upper=float(log_upper),
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--primes", type=int, nargs="+", default=[9413, 151337, 1000033])
    parser.add_argument("--square-roots", type=int, nargs="+", default=[97, 193, 389])
    args = parser.parse_args()
    for prime in args.primes:
        print(json.dumps(moment_record(prime, paley_sign(prime), None)))
    for prime in args.square_roots:
        print(json.dumps(moment_record(prime*prime, square_field_sign(prime), prime)))
    for order, sign in ((61, paley_sign(61)), (97, paley_sign(97)),
                        (49, square_field_sign(7)), (121, square_field_sign(11))):
        for side in (-1, 1):
            print(json.dumps(residual_record(order, sign, side, .05)))


if __name__ == "__main__":
    main()
