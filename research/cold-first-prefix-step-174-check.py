"""Check the rational inequalities in the first three cold-prefix steps."""

from fractions import Fraction as Q


def check():
    center = Q(2031, 128)
    n_min = 4 * (center - Q(1, 2**17))
    for majorant, increment, remainder in (
        (Q(4823, 1000), Q(12, 1000), Q(140, 10**6)),
        (Q(4873, 1000), Q(1), Q(1)),
    ):
        x = majorant**2 / n_min
        assert 0 < x < 1
        assert 4 * increment**4 * (1 + x / 2)**2 < remainder**2 * n_min * (1 - x)**5

    upper_t = 4 * (center + Q(1, 2**16))
    curvature = Q(255, 1000)
    assert upper_t**2 < curvature**2 * (n_min - Q(4841, 1000)**2)**3
    assert Q(518, 1000) + Q(5, 100) * curvature < Q(535, 1000)
    assert Q(535, 1000)**8 < Q(1, 128)

    outgoing = Q(1272, 10**5)
    assert Q(1048, 1000) * Q(12, 1000) + Q(140, 10**6) < outgoing
    displacement = outgoing
    for next_bound in (Q(2645, 10**5), Q(4162, 10**5)):
        assert outgoing + Q(1066, 1000) * displacement + displacement**2 < next_bound
        displacement = next_bound


if __name__ == "__main__":
    check()
    print("Round 174 cold-prefix rational inequalities passed.")
