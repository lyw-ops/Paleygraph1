"""Exact determinant-weight moment tables for the shifted rank-seven and eight factors."""

from collections import Counter
import json


def dominant_walks(rank, degree, is_dominant):
    """Track minuscule tensor multiplicities using the ±coordinate steps."""
    states = {(0,) * rank: 1}
    yield states
    for _ in range(degree):
        next_states = Counter()
        for highest_weight, multiplicity in states.items():
            for index in range(rank):
                for step in (-1, 1):
                    child = list(highest_weight)
                    child[index] += step
                    if is_dominant(child):
                        next_states[tuple(child)] += multiplicity
        states = next_states
        yield states


def orthogonal_chamber(weight):
    return weight[0] >= weight[1] >= weight[2] >= abs(weight[3])


def unitary_chamber(weight):
    return all(left >= right for left, right in zip(weight, weight[1:]))


def main():
    degree = 28
    orthogonal = [
        counts.get((0, 0, 0, 0), 0)
        for counts in dominant_walks(4, degree, orthogonal_chamber)
    ]
    assert orthogonal[:9] == [1, 0, 1, 0, 3, 0, 15, 0, 106]
    assert all(orthogonal[arity] == 0 for arity in range(1, degree + 1, 2))

    unitary = []
    for counts in dominant_walks(7, degree, unitary_chamber):
        # One-dimensional representations are det^e. Here det is (-m)^3.
        unitary.append({
            3 * weight[0]: -count if weight[0] % 2 else count
            for weight, count in counts.items()
            if weight[0] == weight[-1]
        })
    assert unitary[:8] == [
        {0: 1}, {}, {0: 2}, {}, {0: 12}, {}, {0: 120}, {-3: -1, 3: -1},
    ]
    assert all(row.get(-shift) == value for row in unitary for shift, value in row.items())
    print(json.dumps(dict(
        kind="independent_shifted_group_exact_character_moments",
        degree=degree,
        orthogonal_standard=orthogonal,
        unitary_standard_plus_dual_by_jacobi_shift=unitary,
    ), sort_keys=True))


if __name__ == "__main__":
    main()
