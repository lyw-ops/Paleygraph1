"""Compare Paley Fourier trials built from paths and mixed graph shapes."""

import argparse
import json
from math import sqrt
from pathlib import Path
import sys

import numpy as np
from numpy.polynomial.chebyshev import chebvander
from scipy.optimize import linprog


sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from smoothing import certify_spectrum
from square_control import square_field_sign
from theta import paley_sign


def shape_bases(sign, order):
    n = len(sign)
    x = np.fft.rfft(sign).real/sqrt(order)

    def inverse(values):
        return np.fft.irfft(values, n)

    def mask_operator(values):
        return np.fft.rfft(sign*inverse(values)).real

    triangle = mask_operator(2*x*x-1)
    corrected_product = mask_operator(x*triangle)
    paths = [
        np.full(n, 1/sqrt(n)),
        np.roll(sign, n//2)/sqrt(n),
        *np.fft.irfft(chebvander(x, 8)[:, 2:], n=n, axis=0).T,
    ]
    products = [
        x*triangle,
        triangle**2,
        x*x*triangle,
        x*triangle**2,
        triangle**3,
        x*corrected_product,
        triangle*corrected_product,
        corrected_product**2,
    ]
    absolute_values = [np.abs(x+d*triangle) for d in (-2., -.5, 0., .5, 2.)]
    mixed = paths + [inverse(value) for value in products]
    yield 'paths', paths
    yield 'mixed', mixed
    yield 'absolute', mixed + [inverse(value) for value in absolute_values]


def masked_spectrum(sign, side, features):
    columns = np.column_stack(features)*(sign == side)[:, None]
    return np.fft.rfft(columns, axis=0).real


def fit(spectrum):
    result = linprog(
        -spectrum[0],
        A_ub=-spectrum[1:],
        b_ub=np.ones(len(spectrum)-1),
        bounds=(None, None),
        method='highs',
        options={'primal_feasibility_tolerance': 1e-9, 'dual_feasibility_tolerance': 1e-9},
    )
    if not result.success:
        raise RuntimeError(result.message)
    return result.x


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('primes', type=int, nargs='*')
    parser.add_argument('--square-roots', type=int, nargs='+', default=[])
    parser.add_argument('--certify-max-order', type=int, default=0)
    parser.add_argument('--train-order', type=int, help='fit on one prime and reuse those coefficients')
    args = parser.parse_args()
    trained = {}
    if args.train_order is not None:
        train_sign = paley_sign(args.train_order)
        for family, features in shape_bases(train_sign, args.train_order):
            for side in (1, -1):
                trained[family, side] = fit(masked_spectrum(train_sign, side, features))
    cases = [(p, None, paley_sign) for p in args.primes]
    cases += [(h*h, h, square_field_sign) for h in args.square_roots]
    for order, square_root, make_sign in sorted(cases):
        sign = make_sign(order if square_root is None else square_root)
        root_n = sqrt(len(sign))
        for family, features in shape_bases(sign, order):
            for side in (1, -1):
                spectrum = masked_spectrum(sign, side, features)
                coefficients = trained[family, side] if trained else fit(spectrum)
                half = 1 + spectrum @ coefficients
                if not trained and half.min() < -2e-8:
                    raise RuntimeError('the numerical trial violated a Fourier constraint')
                mass = np.r_[half, half[-2:0:-1]]
                record = dict(order=order, square_root=square_root, side=side, family=family,
                              columns=len(features), numerical_ratio=float(mass[0]/root_n),
                              numerical_minimum=float(mass.min()))
                if trained:
                    record['train_order'] = args.train_order
                if order <= args.certify_max_order:
                    value = certify_spectrum(sign, side, mass)
                    if square_root is not None:
                        exact_theta = square_root-1 if side == 1 else (square_root+1)//2
                        if value > exact_theta:
                            raise RuntimeError('the certificate exceeded exact square theta')
                    record['certified_theta_lower'] = str(value)
                    record['certified_ratio_approx'] = float(value)/root_n
                print(json.dumps(record), flush=True)


if __name__ == '__main__':
    main()
