"""Check an endpoint extension with a genuinely active nonnegativity constraint at p=97."""

from flint import arb, ctx, fmpq_poly, fmpz_poly

from theta import paley_sign


def solve(matrix, rhs, modulus):
    """Eliminate over the cyclotomic field, setting free coordinates to zero."""
    rows = [list(row) + [value] for row, value in zip(matrix, rhs)]
    columns = len(rows[0]) - 1
    pivots = []
    for column in range(columns):
        first = len(pivots)
        pivot = next((i for i in range(first, len(rows)) if rows[i][column]), None)
        if pivot is None:
            continue
        rows[first], rows[pivot] = rows[pivot], rows[first]
        gcd, inverse, _ = rows[first][column].xgcd(modulus)
        assert gcd == 1
        rows[first] = [(entry * inverse) % modulus for entry in rows[first]]
        for i, row in enumerate(rows):
            if i != first and row[column]:
                multiplier = row[column]
                rows[i] = [(a - multiplier * b) % modulus for a, b in zip(row, rows[first])]
        pivots.append(column)
    assert all(not row[-1] for row in rows[len(pivots):])
    solution = [fmpq_poly() for _ in range(columns)]
    for i, column in enumerate(pivots):
        solution[column] = rows[i][-1]
    return solution, len(pivots)


def main():
    ctx.prec = 160
    sign = paley_sign(97)
    n = len(sign)
    generator = fmpq_poly([0, 1])
    modulus = fmpq_poly(fmpz_poly.cyclotomic(n))
    powers = [generator**i % modulus for i in range(n)]
    cosine = [(2 * arb.pi() * i / n).cos() for i in range(n)]
    positives = {0, 2, 3, 5, 6, 7, 8, 11, 13, 14, 18, 19, 22}
    negatives = {0, 1, 4, 9, 12, 15, 16, 17, 20, 23, 24}

    def real_ball(poly):
        return sum(
            arb(c.numerator) / c.denominator * cosine[i] for i, c in enumerate(poly)
        )

    def equations(side, support):
        return [
            [sum(powers[(j * h) % n] for h in {i, (-i) % n}) for i in support]
            for j in range(1, n // 2 + 1) if sign[j] == -side
        ]

    def anchored_spectrum(side, support):
        support = sorted(support - {0})
        matrix = equations(side, support)
        values, rank = solve(matrix, [fmpq_poly([-1]) for _ in matrix], modulus)
        assert rank == len(support) and all(real_ball(value) > 0 for value in values)
        vector = {0: fmpq_poly([1])}
        for i, value in zip(support, values):
            vector[i] = vector[-i % n] = value
        return vector

    plus = anchored_spectrum(1, positives)
    minus = anchored_spectrum(-1, negatives)
    assert set(plus) & set(minus) == {0}
    plus_mass = sum(plus.values())
    assert (plus_mass * sum(minus.values())) % modulus == n

    allowed = sorted({0} | (set(range(n // 2 + 1)) - positives))
    allowed_matrix = equations(-1, allowed)
    _, rank = solve(allowed_matrix, [fmpq_poly() for _ in allowed_matrix], modulus)
    assert rank == len(allowed) - 1

    # The plus face has two free bulk coordinates. Test the derivatives of
    # the squared norm along the directions that increase them from zero.
    active_plus = sorted(positives - {0})
    active_matrix = equations(1, active_plus)
    shared_zeros = set(range(n // 2 + 1)) - positives - negatives
    assert shared_zeros == {10, 21}
    for index in sorted(shared_zeros):
        column = [row[0] for row in equations(1, [index])]
        direction, rank = solve(active_matrix, [-value for value in column], modulus)
        assert rank == len(active_plus)
        pairing = sum(2 * plus[i] * value for i, value in zip(active_plus, direction)) % modulus
        assert real_ball(pairing) > 0

    projector = [
        sum(powers[(j * h) % n] for j in range(n) if sign[j] == 1) / n
        for h in range(n)
    ]
    inverse = plus_mass.xgcd(modulus)[1]
    theta_plus = n * inverse
    support = sorted(minus)
    gram = [[projector[(i - j) % n] for j in support] for i in support]
    rhs = [(theta_plus if i == 0 else fmpq_poly()) - 1 for i in support]
    coefficients, _ = solve(gram, rhs, modulus)
    deficit = arb(0)
    free_energy = arb(0)
    for i in range(n):
        value = (1 + sum(projector[(i - j) % n] * x for j, x in zip(support, coefficients))) % modulus
        interval = real_ball(value)
        difference = (theta_plus * plus.get(i, fmpq_poly()) - value) % modulus
        free_energy += real_ball(difference)**2 / n
        if interval < 0:
            deficit += interval**2 / n
            print(i, interval)
    assert deficit > arb(1) / 100
    assert arb(17) / 100 < free_energy < arb(18) / 100
    print("Lower bound from the negative extension coordinates:", deficit)
    print("Actual opposite free energy:", free_energy)


if __name__ == "__main__":
    main()
