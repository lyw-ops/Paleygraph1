"""Measure the largest signed additive Paley eigenvalue on common neighbors."""

import argparse
import csv
from math import isfinite, isqrt, sqrt
import sys

import numpy as np
from scipy import fft
from scipy.sparse.linalg import LinearOperator, eigsh


def quadratic_character(prime):
    if prime < 3 or prime % 2 == 0 or any(
        prime % divisor == 0 for divisor in range(3, isqrt(prime) + 1, 2)
    ):
        raise ValueError(f"expected an odd prime, got {prime}")
    numbers = np.arange(1, (prime + 1) // 2, dtype=np.int64)
    character = np.full(prime, -1, dtype=np.int8)
    character[0] = 0
    character[numbers**2 % prime] = 1
    return character


def field_characters(prime, square):
    character = quadratic_character(prime)
    if square:
        nonsquare = np.flatnonzero(character == -1)[0]
        coordinates_squared = np.arange(prime, dtype=np.int64)**2
        norms = (coordinates_squared[:, None] - nonsquare * coordinates_squared[None, :]) % prime
        character = character[norms]
    elif prime % 4 != 1:
        raise ValueError(f"expected a prime congruent to 1 mod 4, got {prime}")
    return character, np.roll(character, 1, axis=0)


def additive_paley(character):
    order = character.size
    if character.ndim == 2:
        multiplier = fft.rfftn(character.astype(float)).real / sqrt(order)

        def apply(values):
            spectrum = fft.rfftn(values.reshape(character.shape))
            return fft.irfftn(multiplier * spectrum, s=character.shape, axes=(0, 1)).ravel()

        return apply

    length = fft.next_fast_len(2 * order - 1, real=True)
    multiplier = fft.rfft(character.astype(float), length) / sqrt(order)

    def apply(values):
        convolution = fft.irfft(multiplier * fft.rfft(values, length), length)
        convolution[:order - 1] += convolution[order:2 * order - 1]
        return convolution[:order]

    return apply


def compression(prime, square, sign, tolerance):
    character, shifted = field_characters(prime, square)
    common = np.flatnonzero((character == 1) & (shifted == sign))
    order = character.size
    size = len(common)
    if size == 0:
        return size, None, None, None, None, None
    if size == 1:
        return size, 0., 0., 0., 0., 0.
    paley = additive_paley(character)

    def multiply(values):
        full = np.zeros(order)
        full[common] = values
        return sign * paley(full)[common]

    operator = LinearOperator((size, size), matvec=multiply, dtype=np.float64)
    constant_image = multiply(np.full(size, 1 / sqrt(size)))
    constant_mean = constant_image.sum() / sqrt(size)
    constant_norm = np.linalg.norm(constant_image)
    dense_error = ""
    if order <= 853:
        if square:
            a, b = np.unravel_index(common, character.shape)
            dense = character[(a[:, None] - a) % prime, (b[:, None] - b) % prime]
        else:
            dense = character[(common[:, None] - common) % prime]
        exact_dense = np.linalg.eigvalsh(sign * dense / sqrt(order))[-1]
    start = np.random.default_rng(26).normal(size=size)
    values, vectors = eigsh(operator, k=1, which="LA", v0=start, tol=tolerance)
    eigenvalue = values[0]
    vector = vectors[:, 0]
    residual = np.linalg.norm(multiply(vector) - eigenvalue * vector)
    if order <= 853:
        dense_error = abs(exact_dense - eigenvalue)
    return size, eigenvalue, residual, dense_error, constant_mean, constant_norm


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--primes", nargs="*", type=int, default=[])
    parser.add_argument("--square-bases", nargs="*", type=int, default=[])
    parser.add_argument("--tolerance", type=float, default=1e-9)
    args = parser.parse_args()
    if not args.primes and not args.square_bases:
        parser.error("specify at least one field order")
    if not isfinite(args.tolerance) or args.tolerance <= 0:
        parser.error("tolerance must be positive and finite")

    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow((
        "characteristic", "field_order", "square", "sign", "size", "beta", "gap", "residual",
        "dense_error", "constant_mean", "constant_norm",
    ))
    orders = [(prime, prime, False) for prime in args.primes]
    orders += [(prime**2, prime, True) for prime in args.square_bases]
    for order, prime, square in sorted(orders):
        for sign in (1, -1):
            size, beta, residual, dense_error, mean, norm = compression(prime, square, sign, args.tolerance)
            gap = 1 - beta if beta is not None else None
            writer.writerow((prime, order, int(square), sign, size, beta, gap, residual, dense_error, mean, norm))
            sys.stdout.flush()


if __name__ == "__main__":
    main()
