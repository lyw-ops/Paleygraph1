"""Verify the twisted coset transform and rational terms over prime fields."""

from json import dumps
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from theta import prime_field_generator


def transform(values, root, prime):
    powers = [pow(root, i, prime) for i in range(len(values))]
    return [sum(value * powers[(freq * j) % len(values)]
                for j, value in enumerate(values)) % prime
            for freq in range(len(values))]


def check(prime, b):
    assert b % 2 == 0 and (prime - 1) % (2*b) == 0
    m = (prime - 1) // (2*b)
    g = prime_field_generator(prime)
    xi = pow(g, b // 2, prime)
    chi = [-1] * prime
    chi[0] = 0
    for x in range(1, (prime + 1) // 2):
        chi[x*x % prime] = 1
    subgroup = [pow(g, 2*m*k, prime) for k in range(b)]
    f = [sum((1 - 2*(k % 2)) * chi[(1 - pow(g, j, prime)*x) % prime]
             for k, x in enumerate(subgroup))
         for j in range(2*m)]
    assert sum(value**2 for value in f) == prime
    f = f + [-value for value in f]
    assert all(f[(-j) % len(f)] == (1 - 2*(j % 2))*value
               for j, value in enumerate(f))

    full = transform(f, xi, prime)
    lower_odds = range(1, 2*m, 2)
    assert all(full[t] == 0 for t in lower_odds)
    assert full[::2] == [0]*(2*m)
    centers = [0] + ([m] if m % 2 else [])
    coset_terms = 0
    modular_fibers = 0
    for center in centers:
        u = [f[(center + 2*h) % len(f)] for h in range(2*m)]
        assert all(u[h] == u[-h % (2*m)] for h in range(2*m))
        even_transform = transform(u, xi*xi % prime, prime)
        js = list(range(1 - center % 2, 4*m, 2))
        zs = [pow(xi, (center - j) % (4*m), prime) for j in js]
        for j, z in zip(js, zs):
            assert pow(z, 2*m, prime) == prime - 1
            recovered = sum(even_transform[t] * pow(z, t, prime) for t in lower_odds)
            assert recovered % prime == -2*m*f[j] % prime
            peak = sum(2*u[0]*pow(z, t, prime) for t in lower_odds) % prime
            assert peak == 4*u[0]*z*pow((1 - z*z) % prime, -1, prime) % prime
        modular_fibers += len(js)

        for size in range(1, 2*m + 1):
            if (2*m) % size:
                continue
            for offset in sorted({0, 1, m, 2*m - 1}):
                indicator = [int((h - offset) % (2*m // size) == 0)
                             for h in range(2*m)]
                support = range(size, 2*m, 2*size) if size % 2 else ()
                coeffs = {t: sum(indicator[h] * pow(xi, 2*t*h, prime)
                                 for h in range(2*m)) % prime
                          for t in lower_odds}
                assert all(coeffs[t] == (size * pow(xi, 2*offset*t, prime) % prime
                                         if t in support else 0)
                           for t in lower_odds)
                for z in zs:
                    direct = sum(coeffs[t] * pow(z, t, prime) for t in support) % prime
                    if size % 2:
                        w = pow(pow(xi, 2*offset, prime)*z, size, prime)
                        expected = 2*size*w*pow((1 - w*w) % prime, -1, prime) % prime
                    else:
                        expected = 0
                    assert direct == expected
                    coset_terms += 1

    print(dumps(dict(kind="exact_twisted_modular_reconstruction", prime=prime,
                     subgroup_order=b, half_index=m, centers=centers,
                     centered_coset_sums=[f[center] for center in centers],
                     opposite_parity_points=modular_fibers,
                     verified_coset_terms=coset_terms), sort_keys=True))


def check_cross_gain(prime, b):
    """Compare the flat cross-pair sum with its four positional sums."""
    n = (prime - 1) // 2
    m = n // b
    g = prime_field_generator(prime)
    omega = g*g % prime
    signs = []
    positional = 1
    for _ in range(n):
        sign = pow((1 - positional) % prime, n, prime)
        signs.append(-1 if sign == prime - 1 else sign)
        positional = positional*omega % prime
    sums = transform(signs, omega, prime)
    offset = b // 2
    left = [i + b*j for i in (0, 1) for j in range(m)]
    right = [(k + offset) % n for k in left]
    direct = sum(sums[(k - i) % n] for i in left for k in right) % prime
    blocks = [sum(signs[m*j] * pow(omega, m*j*(r - l) % n, prime)
                  for j in range(b)) % prime
              for l in (0, 1) for r in (offset, offset + 1)]
    assert direct == m*m*sum(blocks) % prime
    assert blocks[0] == blocks[3] == sum(
        signs[m*j] * (1 - 2*(j % 2)) for j in range(b)) % prime
    print(dumps(dict(kind="exact_two_coset_cross_sum", prime=prime,
                     subgroup_order=b, matched_displacement=offset,
                     size=len(left), direct=direct, positional_sums=blocks),
                sort_keys=True))


if __name__ == "__main__":
    for p, size in [(61, 6), (101, 10), (10193, 98), (40801, 200)]:
        check(p, size)
    check_cross_gain(61, 6)
    check_cross_gain(101, 10)
