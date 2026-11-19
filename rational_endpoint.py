"""Test rational rooted Paley spectra using exact primitive-layer resultants."""

import argparse
import csv
from fractions import Fraction
from math import gcd, lcm, sqrt
import sys

from flint import arb, ctx, fmpz_poly
import numpy as np

from quadratic_theta import damped_trials
from square_control import square_field_sign
from theta import paley_sign, prime_divisors


def order_layers(n):
    layers = {}
    for position in range(1, n):
        order = n // gcd(position, n)
        layers.setdefault(order, []).append(position)
    return layers


def rational_period(sign, side, layers):
    period, dimension = 1, 1
    for order, positions in layers.items():
        if np.all(sign[positions] == side):
            period = lcm(period, order)
            dimension += len(positions)
    return period, dimension


def resultant_energy_lower(n, ell, allowed, forbidden, polynomial, total, energy_scale):
    norm = abs(fmpz_poly.cyclotomic(ell).resultant(fmpz_poly(polynomial)))
    if norm == 0:
        return norm, Fraction(0), Fraction(0)
    fraction = arb(allowed) / forbidden
    scale = arb(forbidden) / (n * energy_scale)
    base = scale * (arb(allowed) / total)**fraction
    scale_out = 10**14

    def outward(value):
        lower = (value * scale_out).lower().floor().unique_fmpz()
        return Fraction(int(lower), scale_out)

    return norm, outward(base), outward(base * arb(norm)**(arb(2) / forbidden))


def trial_energy(sign, side, primitive, vector):
    squared = np.abs(np.fft.fft(vector))**2 / len(sign)
    primitive_forbidden = [index for index in primitive if sign[index] == -side]
    return float(squared[sign == -side].sum()), float(squared[primitive_forbidden].sum())


def prime_rows(p, denominator, one_fraction):
    sign = paley_sign(p)
    n = len(sign)
    ell = max(prime_divisors(n))
    layers = order_layers(n)
    for order, positions in layers.items():
        bias = int(sign[positions].sum())
        assert bias**2 <= p * 4**len(prime_divisors(order))
    primitive = layers[ell]
    k = max(1, int(.97 * sqrt(n)))
    _, _, plus, minus, residual = next(damped_trials(sign, [p**(-1 / 6)], 2e-10, 72))
    for side, opposite_reference in ((1, minus), (-1, plus)):
        period, dimension = rational_period(sign, side, layers)
        allowed = int(np.sum(sign[primitive] == side))
        forbidden = len(primitive) - allowed
        if min(allowed, forbidden) == 0:
            continue
        raw = np.fft.ifft((sign != side) * np.fft.fft(opposite_reference)).real
        ordered = np.argsort(raw[1:], kind='stable') + 1
        adverse = ordered[:k - 1]
        for label, positions in (('interval', np.arange(1, k)), ('reference_defect', adverse)):
            weights = np.zeros(n, dtype=int)
            weights[0] = denominator
            weights[positions] = denominator - np.arange(len(positions)) % denominator
            counts = [int(weights[index::ell].sum()) for index in range(ell)]
            if sum(counts) >= ell:
                continue
            total = ell * sum(value**2 for value in counts) - sum(counts)**2
            norm, unit_lower, norm_lower = resultant_energy_lower(
                n, ell, allowed, forbidden, counts, total, denominator**2,
            )
            assert norm > 0 and norm_lower >= unit_lower
            energy, energy_layer = trial_energy(sign, side, primitive, weights / denominator)
            assert float(norm_lower) <= energy_layer + 1e-9 <= energy + 2e-9
            yield (p, p, side, label, ell, n // ell, period, dimension, allowed, forbidden,
                   denominator, Fraction(sum(counts), denominator), int(norm).bit_length(), energy,
                   energy_layer, unit_lower, norm_lower, residual)
        if one_fraction:
            extra = int(ordered[k - 1])
            folded_determinant = [0] * ell
            for position in (0, *map(int, adverse)):
                folded_determinant[(extra - position) % ell] += 1
                folded_determinant[(position - extra) % ell] -= 1
            total = 4 * n * (k + 1)
            norm, unit_lower, norm_lower = resultant_energy_lower(
                n, ell, allowed, forbidden, folded_determinant, total, 4,
            )
            vector = np.zeros(n)
            vector[0] = 1
            vector[adverse] = 1
            vector[extra] = .97 * sqrt(n) - k
            energy, energy_layer = trial_energy(sign, side, primitive, vector)
            assert float(norm_lower) <= energy_layer + 1e-9 <= energy + 2e-9
            yield (p, p, side, 'fractional_defect', ell, n // ell, period, dimension, allowed, forbidden,
                   '', vector.sum(), int(norm).bit_length(), energy, energy_layer,
                   unit_lower, norm_lower, residual)


def square_row(h):
    sign = square_field_sign(h)
    n = len(sign)
    k = (h + 1) // 2
    assert len(sign[k::k]) == h - 2
    assert np.all(sign[k::k] == 1)
    period, dimension = rational_period(sign, 1, order_layers(n))
    assert period % (h - 1) == 0
    return (h*h, h, 1, 'subfield', '', '', period, dimension, '', '', 1, k, '', 0, '', '', '', '')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('primes', nargs='*', type=int)
    parser.add_argument('--square-characteristics', nargs='*', type=int, default=[])
    parser.add_argument('--denominator', type=int, default=1)
    parser.add_argument('--one-fraction', action='store_true')
    args = parser.parse_args()
    if args.denominator < 1 or not (args.primes or args.square_characteristics):
        parser.error('provide field orders and a positive denominator')
    ctx.prec = 192
    writer = csv.writer(sys.stdout, lineterminator='\n')
    writer.writerow(('order', 'characteristic', 'sign', 'trial', 'large_factor', 'cofactor',
                     'rational_period_bound', 'rational_sector_dimension', 'allowed_on_layer',
                     'forbidden_on_layer', 'denominator', 'mass', 'cyclotomic_norm_bits',
                     'numerical_forbidden_energy', 'numerical_layer_energy', 'unit_norm_lower',
                     'exact_norm_lower', 'reference_residual'))
    for p in args.primes:
        for row in prime_rows(p, args.denominator, args.one_fraction):
            writer.writerow(row)
            sys.stdout.flush()
    for h in args.square_characteristics:
        writer.writerow(square_row(h))


if __name__ == '__main__':
    main()
