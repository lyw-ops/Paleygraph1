"""Check the signed stationary action against the independent prime-13 cubic."""

import json

from flint import fmpq as Q, fmpq_poly as Poly


def log_one_plus(series, order):
    """Return the Taylor polynomial from (1+h) l' = h'."""
    assert series[0] == 0
    coeff = [Q(0)]
    for degree in range(1, order + 1):
        product = sum(series[j] * (degree - j) * coeff[degree - j]
                      for j in range(1, degree))
        coeff.append(series[degree] - Q(product) / degree)
    return Poly(coeff)


def main():
    # In x=1/2, (1+x cos(pi i/3)) is strictly positive, and the first
    # order condition fixes the floor 30/19.  The cubic uses z=1-floor/t.
    basis = [Q(num, 2) for num in (2, 1, -1, -2, -1, 1)]
    center, floor = Q(1, 2), Q(30, 19)
    relative_basis = [v / (1 + v * center) for v in basis]
    weights = [Q(1)] + [floor / 6] * 5
    assert sum(w * b for w, b in zip(weights, relative_basis)) == 0
    hessian = sum(w * b**2 for w, b in zip(weights, relative_basis))
    assert hessian > 0
    z = Poly([0, 1])

    def cubic(position):
        return ((6 * (1 - z) + 5 * floor) * position**3
                + (floor - 6 * (1 - z)) * position**2
                - (24 * (1 - z) + 8 * floor) * position
                + 24 * (1 - z) - 4 * floor)

    max_depth = 6
    order = 2 * max_depth + 2
    position = Poly([center])
    linear = 3 * (6 + 5 * floor) * center**2 + 2 * (floor - 6) * center - (24 + 8 * floor)
    assert cubic(position)[0] == 0 and linear != 0
    for degree in range(1, order + 1):
        position -= z**degree * (cubic(position)[degree] / linear)
    assert all(cubic(position)[j] == 0 for j in range(order + 1))
    row = [(position - center) * b for b in relative_basis]
    mark = log_one_plus(row[0], order)
    for depth in range(max_depth + 1):
        logs = [log_one_plus(Poly([h[j] for j in range(depth + 1)]), order)
                for h in row]
        action = sum(w * value for w, value in zip(weights, logs)) - z * logs[0]
        defect = mark + action.derivative()
        assert all(defect[j] == 0 for j in range(2 * depth + 1))
        next_norm = sum(w * h[depth + 1]**2 for w, h in zip(weights, row))
        assert next_norm > 0
        assert defect[2 * depth + 1] == -(depth + 1) * next_norm
    print(json.dumps(dict(test="actual_variational_jets", prime=13, floor=str(floor),
                          depths=list(range(max_depth + 1)), highest_mark_order=2 * max_depth + 1,
                          last_verified_defect=str(defect[2 * max_depth + 1])), sort_keys=True))

    column = [b * relative_basis[0] / hessian for b in relative_basis]
    square = [v**2 for v in column]
    moment3 = sum(w * v**3 for w, v in zip(weights, column))
    projection_coeff = sum(w * b * v for w, b, v in zip(weights, relative_basis, square)) / hessian
    reflected = sum(w * v * (v - 2 * b * projection_coeff)
                    for w, v, b in zip(weights, square, relative_basis))
    c0 = column[0]
    predictions = [-c0, moment3 - Q(3, 2) * c0**2,
                   reflected + 4 * c0 * moment3 - Q(10, 3) * c0**3]
    assert all(mark[j] == prediction for j, prediction in enumerate(predictions, 1))
    print(json.dumps(dict(test="actual_signed_cubic_contraction", prime=13,
                          coefficients=list(map(str, predictions)),
                          reflection_quadratic_form=str(reflected)), sort_keys=True))


if __name__ == "__main__":
    main()
