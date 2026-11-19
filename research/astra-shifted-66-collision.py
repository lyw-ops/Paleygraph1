"""Fieldwise Newton comparison for the putative rank-six exterior square."""
from math import gcd
from pathlib import Path
import json
import runpy

from flint import fmpz_poly

old = runpy.run_path(str(Path(__file__).with_name("rank-four-arithmetic-56-check.py")))


def compare(p, d):
    q = p**d
    order = q-1
    ring = fmpz_poly.cyclotomic(order)
    base, ell, _, _ = old["data"](p, d)
    conv = old["cycconv"]
    legendre = [l*x for l, x in zip(ell, conv(ell, ell))]
    dual_source = [l*(x+2*(q+1)) for l, x in zip(ell, conv(legendre, legendre))]
    ell_inverse = [(-1)**i*l for i, l in enumerate(ell)]
    negative_shift = [l*(-x+1+(-1)**i)
                      for i, (l, x) in enumerate(zip(ell, conv(ell_inverse, dual_source)))]
    _, a1, _ = old["rank_four_rows"](p, d)
    extension, extension_a, _ = old["rank_four_rows"](p, 2*d)
    norm = extension.g**((q*q-1)//order)
    embedded = extension.embed(base, base.g)
    norm_log = next(i for i in range(order) if embedded**i == norm)
    assert gcd(norm_log, order) == 1
    a2 = [0]*order
    for i, value in enumerate(extension_a):
        a2[i*norm_log % order] += value

    different_from_negative = 0
    for k in range(1, order):
        if k == order//2:
            continue

        def value(row):
            return old["reduce_at_character"](row, k, ring, order)

        lhs = (2*q*q*value(negative_shift)) % ring
        rhs = (-value(ell_inverse)*(value(a1)**2-value(a2))) % ring
        assert lhs == rhs
        different_from_negative += int(lhs != -rhs)
    return dict(field=q, good_characters=q-3, nonzero=different_from_negative,
                norm_generator_log=norm_log)


if __name__ == "__main__":
    fields = ((5, 1), (3, 2), (13, 1), (17, 1), (5, 2), (7, 2), (97, 1))
    print(json.dumps(dict(kind="fieldwise_rank_six_exterior_square_comparison",
                     equality="Z_minus_D = L^-1 exterior^2 A on tested good characters",
                     fields=[compare(p, d) for p, d in fields]), sort_keys=True))
