"""Measure the theta certificate's response to the marked smoothing weight."""

import argparse
import csv
from math import isfinite
import sys

import numpy as np
from scipy.sparse.linalg import LinearOperator, cg, minres

from smoothing import kernel_action, smoothing
from square_control import square_field_sign
from theta import paley_sign


def linearized_operator(sign, activation_derivative):
    # On the mean-zero subspace H = K - P diag(v/Phi(v)) P, where P = I - J.
    # Add J on the constant subspace so MINRES sees an invertible operator.
    def apply(values):
        mean = values.mean()
        weighted = activation_derivative * (values - mean)
        return kernel_action(sign, values) - weighted + weighted.mean() + mean

    n = len(sign)
    return LinearOperator((n, n), matvec=apply, dtype=np.float64)


def marked_system(sign, tau, vector):
    n = len(sign)
    weights = np.full(n, tau / n)
    weights[0] = 1
    total = np.hypot(vector, 2 * np.sqrt(weights))
    activation_derivative = vector / total
    operator = linearized_operator(sign, activation_derivative)
    rhs = np.full(n, -1 / n)
    rhs[0] += 1
    return operator, rhs, total, activation_derivative


def marked_response(sign, tau, vector, tolerance, max_steps):
    operator, rhs, total, activation_derivative = marked_system(sign, tau, vector)
    response, info = minres(operator, rhs, rtol=tolerance, maxiter=max_steps)
    residual = np.linalg.norm(operator @ response - rhs)
    if info < 0:
        raise RuntimeError(f"MINRES failed with status {info}")
    difference = 4 * response[0] / total[0] ** 2 - activation_derivative[0]
    bulk_sum = tau * (1 - 1 / len(sign))
    leverage_sum = bulk_sum / (1 + bulk_sum)
    return (
        difference, (leverage_sum + difference) / 2, (leverage_sum - difference) / 2,
        response, np.max(np.abs(activation_derivative[1:])), residual, info,
    )


def regularized_solve(operator, rhs, width, tolerance, max_steps):
    def apply(values):
        return operator @ (operator @ values) + width ** 2 * values

    system = LinearOperator(operator.shape, matvec=apply, dtype=np.float64)
    solution, info = cg(system, rhs, rtol=tolerance, maxiter=max_steps)
    if info < 0:
        raise RuntimeError(f"CG failed with status {info}")
    residual = np.linalg.norm(system @ solution - rhs)
    return solution, residual, info


def regularized_response(operator, rhs, width, tolerance, max_steps):
    solution, residual, info = regularized_solve(operator, rhs, width, tolerance, max_steps)
    signed_response = np.dot(rhs, operator @ solution)
    filtered_mass = width ** 2 * np.dot(rhs, solution)
    return signed_response, filtered_mass, residual, info


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primes", nargs="*", type=int)
    parser.add_argument("--square-characteristics", nargs="*", type=int, default=[])
    parser.add_argument("--tau", nargs="+", type=float, default=[0.05, 0.2, 0.5, 1, 2, 4, 16])
    parser.add_argument("--max-steps", type=int, default=20000)
    parser.add_argument("--tolerance", type=float, default=1e-9)
    parser.add_argument("--widths", nargs="+", type=float, default=[], help="resolvent regularization widths")
    args = parser.parse_args()
    if not args.primes and not args.square_characteristics:
        parser.error("provide at least one prime or square characteristic")
    if any(not isfinite(value) or value <= 0 for value in [*args.tau, args.tolerance, *args.widths]):
        parser.error("tau, tolerance and regularization widths must be positive and finite")
    if args.max_steps < 3:
        parser.error("max-steps must be at least 3")

    writer = csv.writer(sys.stdout, lineterminator="\n")
    fields = [
        "field_order", "characteristic", "tau", "log_marked_mass", "leverage_difference",
        "leverage_plus", "leverage_minus", "inverse_marker_l2", "subfield_response_energy_share",
        "max_bulk_abs_derivative", "smoothing_residual_l2", "response_residual_l2", "minres_status",
    ]
    if args.widths:
        fields += [
            "marked_inverse_entry", "width", "regularized_inverse_entry",
            "filtered_spectral_mass", "regularized_response_residual_l2", "cg_status",
        ]
    writer.writerow(fields)
    cases = [(p, p) for p in args.primes] + [(p * p, p) for p in args.square_characteristics]
    for order, prime in sorted(cases):
        square = order != prime
        sign = square_field_sign(prime) if square else paley_sign(prime)
        for tau in args.tau:
            vector, metrics = smoothing(sign, tau, args.tolerance, args.max_steps)
            difference, plus, minus, response, max_bulk, residual, info = marked_response(
                sign, tau, vector, args.tolerance / 10, args.max_steps,
            )
            norm = np.linalg.norm(response)
            share = (np.linalg.norm(response[prime - 1::prime - 1]) / norm) ** 2 if square else ""
            row = (
                order, prime, tau, np.arcsinh(vector[0] / 2), difference, plus, minus,
                norm, share, max_bulk, metrics[-2], residual, info,
            )
            if args.widths:
                operator, rhs, _, _ = marked_system(sign, tau, vector)
                for width in args.widths:
                    result = regularized_response(operator, rhs, width, args.tolerance / 10, args.max_steps)
                    writer.writerow((*row, np.dot(rhs, response), width, *result))
            else:
                writer.writerow(row)


if __name__ == "__main__":
    main()
