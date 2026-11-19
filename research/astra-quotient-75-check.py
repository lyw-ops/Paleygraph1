"""Certify prime-quotient gaps on previously surviving prime masks."""

import argparse
import json
import sys
from fractions import Fraction
from functools import lru_cache
from math import isqrt
from pathlib import Path

from flint import arb, ctx, fmpq

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from theta import certify, optimize, paley_sign, prime_divisors


SCALE = 10**10


@lru_cache(None)
def cosine_boxes(order):
    lower, upper = [], []
    for j in range(order // 2 + 1):
        value = SCALE * arb.cos_pi_fmpq(fmpq(2 * j, order))
        lower.append(int(value.lower().floor().unique_fmpz()))
        upper.append(int(value.upper().ceil().unique_fmpz()))
    return lower, upper


def lower_theta(signs, side):
    row, _ = optimize(signs, side)
    return certify(signs, side, row, cosine_boxes(len(signs)), SCALE)


def run(limit):
    ctx.prec = 96
    for p in range(5, limit + 1, 4):
        if any(p % d == 0 for d in range(3, isqrt(p) + 1, 2)):
            continue
        n = (p - 1) // 2
        signs = paley_sign(p)
        for b in sorted(prime_divisors(n)):
            if b == n or b * b < 4 * n or b == 2:
                continue
            m = n // b
            for side in (1, -1):
                forbidden = (signs.reshape(b, m) == -side).sum(axis=0)
                if forbidden[0] >= min(forbidden[1:]):
                    continue
                upper = Fraction(b, 1) / lower_theta(signs[::m], -side)
                lower = lower_theta(signs[::m // 2], side)
                print(json.dumps(dict(p=p, b=b, side=side, period=m,
                                      quotient_upper=str(upper), doubled_lower=str(lower),
                                      strict=lower > upper)), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--limit', type=int, default=3000)
    run(parser.parse_args().limit)
