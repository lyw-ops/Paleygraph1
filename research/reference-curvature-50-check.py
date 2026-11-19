"""Independently enclose the regression and the two flat tangent norms."""
import json
from math import isqrt

from flint import acb, arb, ctx


def verify(prime):
    assert prime % 4 == 1
    assert all(prime % divisor for divisor in range(2, isqrt(prime) + 1))
    n = (prime - 1) // 2
    squares = {value * value % prime for value in range(1, n + 1)}
    generator = next(value for value in sorted(squares)
                     if len({pow(value, k, prime) for k in range(n)}) == n)
    mask = [0]
    for k in range(1, n):
        mask.append(1 if (1 - pow(generator, k, prime)) % prime in squares else -1)
    assert mask[1:] == mask[:0:-1]

    root_n = arb(n).sqrt()
    z = [value.real / root_n for value in acb.dft([acb(side) for side in mask])]
    bulk = z[1:]
    mean = sum(bulk) / (n - 1)
    squares_bulk = [value ** 2 for value in bulk]
    square_mean = sum(squares_bulk) / (n - 1)
    variance = sum((value - mean) ** 2 for value in bulk)
    slope = sum((value - mean) * (square - square_mean)
                for value, square in zip(bulk, squares_bulk)) / variance
    residual = sum((square - square_mean - slope * (value - mean)) ** 2
                   for value, square in zip(bulk, squares_bulk)) / n
    assert residual > 0

    transform = acb.dft([acb(0)] + [acb(value) for value in squares_bulk])
    projected_norms = []
    for side in (1, -1):
        projection = [value.real / n for value in acb.dft([
            coefficient if label == side else acb(0)
            for label, coefficient in zip(mask, transform)
        ])]
        tangent = [value.real / n for value in acb.dft([
            acb(int(label == side)) for label in mask
        ])]
        correction = projection[0] / tangent[0]
        projected_norms.append(sum(
            (component - correction * direction) ** 2
            for component, direction in zip(projection[1:], tangent[1:])
        ) / n)
    assert (residual - sum(projected_norms)).contains(0)
    print(json.dumps(dict(prime=prime, n=n, scaled_curvature=str(residual / 64),
                          projected_norms=list(map(str, projected_norms))),
                     sort_keys=True))


if __name__ == "__main__":
    ctx.prec = 192
    for p in (97, 173, 401):
        verify(p)
