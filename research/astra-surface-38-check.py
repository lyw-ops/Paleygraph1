"""Replay the root-directed recurrence on an exact nonconstant physical row."""

import json

from flint import fmpq as Q, fmpq_poly as Poly


def record(kind, **values):
    print(json.dumps({"kind": kind, **values}, sort_keys=True))


def actual_rank_one_check():
    # Accepted prime-13 cosine basis and cubic, research/complex-floor-33.md.
    basis = [Q(x, 2) for x in (2, 1, -1, -2, -1, 1)]
    center_coordinate = Q(1, 2)
    row = [1 + center_coordinate * entry for entry in basis]
    direction = [entry / value for entry, value in zip(basis, row)]
    floor = -6 * direction[0] / sum(direction[1:])
    weights = [Q(1)] + [floor / 6] * 5
    assert floor > 0 and min(row) > 0
    assert sum(w * d for w, d in zip(weights, direction)) == 0
    hessian = sum(w * d**2 for w, d in zip(weights, direction))
    assert hessian > 0

    order = 12
    position = [center_coordinate]
    inverse = [[Q(1)] for _ in row]
    for j in range(1, order + 1):
        # [z^j]1/(1+h), initially omitting the unknown coefficient of h.
        truncated = [
            -sum(d * position[s] * history[j - s] for s in range(1, j))
            for d, history in zip(direction, inverse)
        ]
        projected = sum(w * d * val for w, d, val in zip(weights, direction, truncated))
        next_position = (projected - direction[0] * inverse[0][j - 1]) / hessian
        position.append(next_position)
        for d, val, history in zip(direction, truncated, inverse):
            history.append(val - d * next_position)

    X = Poly(position)
    zm = Poly([1, -1])
    residual = ((6 * zm + 5 * floor) * X**3
                + (floor - 6 * zm) * X**2
                - (24 * zm + 8 * floor) * X
                + 24 * zm - 4 * floor)
    assert all(residual[j] == 0 for j in range(order + 1))
    assert (3 * (6 + 5 * floor) * center_coordinate**2
            + 2 * (floor - 6) * center_coordinate - (24 + 8 * floor)) != 0
    record("exact_actual_stationary_direction", prime=13, floor=str(floor),
           center_coordinate=str(center_coordinate), hessian=str(hessian),
           first_marked_relative_jet=str(direction[0] * position[1]),
           last_marked_relative_jet=str(direction[0] * position[-1]),
           cubic_residual_zero_through=order)


def analytic_constants():
    h_bound = Q(1, 31)
    residual_bound = h_bound**2 / (1 - h_bound) + h_bound + Q(1, 32) / (1 - h_bound)
    derivative_bound = (1 + Q(1, 64)) / (1 - Q(1, 8))**2 - 1
    assert residual_bound < 1 and derivative_bound < Q(1, 2)
    assert h_bound + Q(1, 16) < Q(1, 8)
    record("directional_repair_constants", weighted_residual_over_sqrt_W=str(residual_bound),
           contraction_upper_bound=str(derivative_bound))


if __name__ == "__main__":
    actual_rank_one_check()
    analytic_constants()
