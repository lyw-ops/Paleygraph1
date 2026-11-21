"""Exact comparisons in the ordinary and cold Round 177 notes."""

from fractions import Fraction as Q


def check_collision_exponents():
    epsilon = Q(1, 1024)
    delta = 2 * epsilon
    alpha = Q(18, 13) + Q(4, 13) * max(49 * epsilon, 36 * epsilon + 9 * delta)
    cutoff = Q(63, 128)
    target = Q(37, 16) - Q(1, 4320) - delta
    assert alpha == Q(2331, 1664)
    assert Q(35, 16) - Q(1, 4320) + cutoff / 4 == target
    assert target - (2 * alpha - cutoff) == Q(737, 898560)
    assert Q(9, 4) < target
    epsilon, delta = Q(3, 418), Q(1, 418)
    assert Q(18, 13) + Q(4, 13) * max(49 * epsilon, 36 * epsilon + 9 * delta) == Q(3, 2) - epsilon


def check_cold_tube():
    n_min = 4 * (Q(2031, 128) - Q(1, 2**17))
    seed, radius = Q(2828428, 10**6), Q(3, 8)
    disk = Q(1963, 1000) + radius
    assert n_min - 2 * disk**2 > 0
    assert 2 * seed * disk * (n_min - 2 * disk**2) > 4 * disk**2 * (seed + disk)**2
    rate = Q(545, 1000)
    assert (seed + disk)**2 < rate**2 * (n_min + (seed + disk)**2)
    assert rate**8 < Q(1, 128)

    factor = Q(122, 100)
    x = (Q(4823, 1000) + radius)**2 / n_min
    assert 0 < x < 1
    assert 4 * (1 + x / 2)**2 < factor**2 * n_min * (1 - x)**5
    outgoing = Q(1272, 10**5)
    displacement = outgoing
    for bound in (2648, 4181, 5943, 8039, 10631, 13984, 18565, 25268, 35998):
        assert 0 <= displacement < radius
        next_bound = Q(bound, 10**5)
        assert outgoing + Q(1066, 1000) * displacement + factor * displacement**2 < next_bound
        displacement = next_bound
    assert displacement < radius
    assert (radius - Q(25268, 10**5)) * (1 - rate) == Q(556556, 10**7)


if __name__ == "__main__":
    check_collision_exponents()
    check_cold_tube()
    print("Round 177 exact comparisons passed.")
