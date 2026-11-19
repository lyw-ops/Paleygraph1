"""Compare signed resolvent windows and the mixed stationary tail at the mark."""

import argparse
import csv
from math import isfinite, sqrt
import sys

import numpy as np
from scipy.sparse.linalg import LinearOperator, minres

from sensitivity import marked_response, marked_system, regularized_solve
from smoothing import kernel_action, smoothing
from square_control import square_field_sign
from theta import paley_sign


def window_statistics(operator, rhs, total, diagonal, width, tolerance, max_steps):
    n = len(rhs)
    solution, residual, status = regularized_solve(operator, rhs, width, tolerance, max_steps)
    if status:
        raise RuntimeError(f"regularized solve failed with status {status}")
    real_propagator = operator @ solution
    imaginary_propagator = width * solution
    marked_resolvent = complex(np.dot(rhs, real_propagator), np.dot(rhs, imaginary_propagator))
    filtered_mass = width * marked_resolvent.imag
    mixed_tail = width * np.dot(total, imaginary_propagator)
    mixed_difference = width * np.dot(diagonal * total, imaginary_propagator)

    # The defect of the compressed diagonal includes both the bulk and the mean direction.
    defect = 1 - diagonal**2
    bulk_norm_squared = np.dot(defect[1:], real_propagator[1:]**2 + imaginary_propagator[1:]**2)
    mean_direction = (diagonal - diagonal.mean()) / sqrt(n)
    mean_response = complex(np.dot(mean_direction, real_propagator), np.dot(mean_direction, imaginary_propagator))
    budget = (
        defect[0] * abs(marked_resolvent - diagonal[0] / defect[0])**2
        + bulk_norm_squared + abs(mean_response + 1 / sqrt(n))**2 + filtered_mass
    )

    absolute_lower = (np.dot(rhs, rhs) - filtered_mass) / 2
    positive_lower = max(0.0, (absolute_lower + marked_resolvent.real) / 2)
    negative_lower = max(0.0, (absolute_lower - marked_resolvent.real) / 2)
    bulk_source_response = np.dot(defect[1:] * total[1:], real_propagator[1:])
    source_error = abs(
        diagonal[0] * total[0] - 4 * marked_resolvent.real / total[0]
        - mixed_difference - bulk_source_response
    )
    return (
        marked_resolvent.real, filtered_mass, mixed_tail, positive_lower, negative_lower,
        abs(budget - 1 / defect[0]), residual, mixed_difference, bulk_source_response, source_error,
    )


def damping_statistics(sign, operator, rhs, total, diagonal, tau, width, tolerance, max_steps):
    n = len(rhs)
    damping = 1 - width

    def apply(values):
        return damping * (operator @ values) + width * (kernel_action(sign, values) + values.mean())

    system = LinearOperator(operator.shape, matvec=apply, dtype=np.float64)
    response, status = minres(system, rhs, rtol=tolerance, maxiter=max_steps)
    if status:
        raise RuntimeError(f"damped solve failed with status {status}")
    residual = np.linalg.norm(system @ response - rhs)
    inverse = response[0]
    signed = diagonal * total
    total_load = width * np.dot(total, response)
    signed_load = width * np.dot(signed, response)
    bulk_response = np.dot((1 - diagonal[1:] ** 2) * total[1:], response[1:])
    source_error = abs(signed[0] - 4 * damping * inverse / total[0] - total_load - damping * bulk_response)
    defect = 1 - (damping * diagonal) ** 2
    mean_response = (damping * np.dot(diagonal - diagonal.mean(), response) + 1) / sqrt(n)
    budget = (
        defect[0] * (inverse - damping * diagonal[0] / defect[0]) ** 2
        + np.dot(defect[1:], response[1:] ** 2) + mean_response**2
    )
    total_weight = 1 + tau * (n - 1) / n
    mean_error = abs(2 * sqrt(total_weight) * mean_response - total[0] + signed_load)
    return (
        inverse, total_load, signed_load, bulk_response, source_error,
        abs(budget - 1 / defect[0]), mean_error, residual,
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primes", nargs="*", type=int)
    parser.add_argument("--square-characteristics", nargs="*", type=int, default=[])
    parser.add_argument("--tau", nargs="+", type=float, default=[0.05, 0.5])
    parser.add_argument("--widths", nargs="+", type=float, default=[0.05, 0.25, 0.5])
    parser.add_argument("--scaled-widths", nargs="+", type=float, default=[1, 4])
    parser.add_argument("--diagonal-damping", action="store_true", help="use H_t with t=1-width instead of H-i*width")
    parser.add_argument("--tolerance", type=float, default=1e-9)
    parser.add_argument("--max-steps", type=int, default=10000)
    args = parser.parse_args()
    if not args.primes and not args.square_characteristics:
        parser.error("provide at least one prime or square characteristic")
    if any(not isfinite(value) or value <= 0 for value in [*args.tau, *args.widths, *args.scaled_widths, args.tolerance]):
        parser.error("weights, widths and tolerance must be positive and finite")
    if args.max_steps < 3:
        parser.error("max-steps must be at least 3")

    writer = csv.writer(sys.stdout, lineterminator="\n")
    columns = (
        "field_order", "characteristic", "tau", "width", "marked_inverse_entry", "regularized_inverse_entry",
        "filtered_marked_mass", "mixed_u_tail", "positive_part_lower", "negative_part_lower",
        "sum_rule_error", "cg_residual_l2", "mixed_v_tail", "bulk_source_response", "stationary_source_error",
        "smoothing_residual_l2", "inverse_residual_l2",
    )
    if args.diagonal_damping:
        columns = (
            "field_order", "characteristic", "tau", "width", "marked_inverse_entry", "damped_inverse_entry",
            "total_damping_load", "signed_damping_load", "bulk_source_response", "stationary_source_error",
            "sum_rule_error", "stationary_mean_error", "damped_residual_l2",
            "smoothing_residual_l2", "inverse_residual_l2",
        )
    writer.writerow(columns)
    orders = [(p, p) for p in args.primes] + [(r * r, r) for r in args.square_characteristics]
    for order, characteristic in sorted(orders):
        sign = paley_sign(characteristic) if order == characteristic else square_field_sign(characteristic)
        widths = sorted(set(args.widths) | {value / sqrt(order) for value in args.scaled_widths})
        if args.diagonal_damping and widths[-1] > 1:
            parser.error(f"diagonal damping requires widths at most one, got {widths[-1]} at {order}")
        for tau in args.tau:
            vector, metrics = smoothing(sign, tau, args.tolerance, args.max_steps)
            _, _, _, response, _, inverse_residual, _ = marked_response(
                sign, tau, vector, args.tolerance / 10, args.max_steps,
            )
            operator, rhs, total, diagonal = marked_system(sign, tau, vector)
            marked_inverse = np.dot(rhs, response)
            for width in widths:
                if args.diagonal_damping:
                    result = damping_statistics(
                        sign, operator, rhs, total, diagonal, tau, width, args.tolerance / 10, args.max_steps,
                    )
                else:
                    result = window_statistics(operator, rhs, total, diagonal, width, args.tolerance / 10, args.max_steps)
                writer.writerow((order, characteristic, tau, width, marked_inverse, *result, metrics[-2], inverse_residual))


if __name__ == "__main__":
    main()
