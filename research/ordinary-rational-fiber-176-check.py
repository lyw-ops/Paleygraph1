"""Exact finite diagnostics and exponent checks for the Round 176 fibers."""

from collections import Counter
from fractions import Fraction
from itertools import product


def projective(matrix, p):
    first = next(entry % p for entry in matrix if entry % p)
    scale = pow(first, -1, p)
    return tuple(scale * entry % p for entry in matrix)


def check_relative_fiber(p, coefficients):
    a, b, c, d = coefficients
    units = range(1, p)
    maps = {}
    for u, v in product(units, repeat=2):
        matrix = (u * (a*d*v - b*c), u*b*d*(v-1), -a*c*(v-1), a*d-b*c*v)
        key = projective(matrix, p)
        assert key not in maps
        maps[key] = (u, v)

    fibers = Counter()
    for u, previous_u, w in product(units, repeat=3):
        matrix = (
            u * pow(previous_u, -1, p) * (a*d*w-b*c),
            u*b*d*(w-1), -a*c*(w-1)*pow(previous_u, -1, p), a*d-b*c*w,
        )
        key = projective(matrix, p)
        if key[1] and key[2] and (key[0] or key[3]):
            fibers[key] += 1
    assert max(fibers.values(), default=0) <= 2


def check_shifted_quadratic(p):
    for d in range(1, p):
        domain = [x for x in range(1, p) if (x+d) % p]
        for x, y, z in product(domain, repeat=3):
            u = z * pow(y, -1, p) % p
            v = y * (y + d) * pow(x * (x+d) % p, -1, p) % p
            slope = pow(u*u*v, -1, p)
            intercept = d * pow(u*v, -1, p)
            assert (x*(x+d)*pow(z, -1, p) - slope*z - intercept) % p == 0
            assert intercept * pow(d*slope % p, -1, p) % p == u


def check_exponents():
    for degree, eps, margin in (
        (17, Fraction(1, 840), Fraction(1, 2856)),
        (22, Fraction(1, 1080), Fraction(1, 4752)),
    ):
        delta = 2 * eps
        bsg_size = Fraction(1, 2) - Fraction(5, 2)*eps - Fraction(9, 4)*delta
        assert bsg_size/degree - (12*eps + 6*delta) == margin
    assert Fraction(255, 22) < 15


if __name__ == "__main__":
    check_exponents()
    for p in (5, 13, 17):
        for matrix in ((1, 1, 1, -1), (1, 2, 3, 4), (2, 1, 1, 1)):
            check_relative_fiber(p, matrix)
        check_shifted_quadratic(p)
        print(f"p={p}: relative-transform and quadratic incidences verified")
