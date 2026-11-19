"""Count signed shifted coset cells in prime and prime-square fields."""

from collections import defaultdict
from json import dumps
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from theta import prime_divisors, prime_field_generator


def square_operations(prime):
    nonsquare = next(x for x in range(2, prime)
                     if pow(x, (prime - 1) // 2, prime) == prime - 1)

    def multiply(left, right):
        a, c = left % prime, left // prime
        b, d = right % prime, right // prime
        return ((a*b + nonsquare*c*d) % prime
                + prime * ((a*d + b*c) % prime))

    def power(base, exponent):
        result = 1
        while exponent:
            if exponent & 1:
                result = multiply(result, base)
            base = multiply(base, base)
            exponent >>= 1
        return result

    order = prime * prime - 1
    factors = prime_divisors(order)
    generator = next(x for x in range(prime, prime * prime)
                     if all(power(x, order // factor) != 1 for factor in factors))

    def subtract_one(x):
        return ((x % prime - 1) % prime) + prime * (x // prime)

    return multiply, subtract_one, generator


def check(prime, b, square=False):
    q = prime * prime if square else prime
    index = (q - 1) // b
    assert b % 2 == 0 and index % 2 == 0 and b * index == q - 1
    if square:
        multiply, subtract_one, generator = square_operations(prime)
    else:
        generator = prime_field_generator(prime)

        def multiply(x, y):
            return (x*y) % prime

        def subtract_one(x):
            return x - 1

    values = [1]
    for _ in range(1, q - 1):
        values.append(multiply(values[-1], generator))
    logs = {x: j for j, x in enumerate(values)}
    assert len(logs) == q - 1 and multiply(values[-1], generator) == 1

    cells = defaultdict(lambda: [0, 0, 0, 0])
    twisted_sum = 0
    for j, x in enumerate(values[1:], start=1):
        k = logs[subtract_one(x)]
        if j % index == 0:
            twisted_sum += 1 - 2 * ((j // index + k) % 2)
        key = (j % index, k % index)
        orientation = 2 * ((j // index) % 2) + (k // index) % 2
        cells[key][orientation] += 1
    opposite = [(ends[0] + ends[3], ends[1] + ends[2])
                for (c, d), ends in cells.items() if (c + d) % 2]
    opposite_points = sum(a + c for a, c in opposite)
    signed_second = sum((a - c)**2 for a, c in opposite)
    total_signed_second = sum((a + d - b2 - c)**2 for a, b2, c, d in cells.values())
    odd_cells = sum((a + c) % 2 for a, c in opposite)
    unpaired_points = sum(a + c for a, c in opposite if (a, c) != (1, 1))
    same_pairs = sum(a*(a-1) + c*(c-1) for a, c in opposite)
    mismatches = (b - 1 - abs(twisted_sum)) // 2
    parity_errors = 0
    other_points = 0
    not_two_points = 0
    for (c, d), ends in cells.items():
        expected = 2 * (c % 2) + d % 2
        population = sum(ends)
        correct = sum(ends[i] * (ends[i ^ expected] - (expected == 0))
                      for i in range(4))
        parity_errors += population*(population-1) - correct
        if expected:
            other_points += population
            if population != 2:
                not_two_points += population
    assert opposite_points == (q - 1) // 2
    assert 2 * signed_second == q - twisted_sum**2
    assert total_signed_second == q - b
    assert odd_cells <= signed_second
    assert same_pairs <= b * mismatches
    assert unpaired_points <= signed_second + 2 * same_pairs
    assert other_points == 3*(q - 1) // 4
    assert not_two_points <= 3*unpaired_points // 2
    assert parity_errors <= 4*b*mismatches
    if square:
        assert b == prime + 1 and abs(twisted_sum) == prime
        assert unpaired_points == odd_cells == not_two_points == parity_errors == 0

    print(dumps(dict(q=q, subgroup_order=b, squared_field=square,
                     twisted_sum=twisted_sum, mismatches=mismatches,
                     opposite_points=opposite_points, odd_cells=odd_cells,
                     unpaired_points=unpaired_points, same_sign_pairs=same_pairs,
                     non_both_positive_points=other_points,
                     non_both_positive_non_two_points=not_two_points,
                     parity_errors=parity_errors,
                     opposite_signed_second=signed_second,
                     total_signed_second=total_signed_second), sort_keys=True))


if __name__ == "__main__":
    check(10193, 98)
    check(40801, 200)
    check(252001, 500)
    for r in (11, 31, 97):
        check(r, r + 1, square=True)
