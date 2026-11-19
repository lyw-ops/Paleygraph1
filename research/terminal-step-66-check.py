"""Outward comparisons for the two-activation terminal budget."""

import json

from flint import arb, ctx


def main():
    ctx.prec = 160
    r = arb(2).sqrt()
    m = 2*r/arb.pi()
    delta = 1-m
    variance = 1-m*m
    fourth = 3*variance**2-(2*m/3)**4/8
    second_mean_lower = arb(9436066882988)/10**13
    crossing_lower = (variance*variance.sqrt()-9*fourth/(32*r))/(6*arb.pi()*r)
    step_square_cap = variance-(second_mean_lower-m)**2-4*crossing_lower
    assert second_mean_lower > m and crossing_lower > 0
    assert 0 < step_square_cap < arb(177914)/10**6

    variance_floor = arb(85)/10**5
    lower_mean = (1-(variance*variance_floor).sqrt())/m
    energy_gap = lower_mean**2-1-step_square_cap-2*(step_square_cap*variance_floor).sqrt()
    assert lower_mean > 0 and energy_gap > arb(8)/10**5

    epsilon = arb(1)/1000
    extra = arb(25)/10**7
    slope = 2*delta+epsilon*m
    cutoff = epsilon/slope
    density_cap = arb(451)/1000
    assert density_cap > 2/(arb.pi()*(r*r-cutoff*cutoff).sqrt())
    gap = (epsilon*(variance-(variance*step_square_cap).sqrt()-(variance*extra).sqrt())
           - density_cap*epsilon**2/slope-epsilon**2*variance/4-extra)
    assert gap > arb(36)/10**8
    assert arb(13037)/10**6+delta**2+extra > arb(22976)/10**6
    print(json.dumps(dict(
        kind="uniform_two_activation_terminal_budget_constants",
        precision=ctx.prec,
        early_crossing_lower=str(crossing_lower.lower()),
        squared_step_upper=str(step_square_cap.upper()),
        terminal_variance_floor="0.00085",
        variance_floor_strict_margin_lower=str(energy_gap.lower()),
        surplus_over_terminal_scalar_bound="0.0000025",
        surplus_strict_margin_lower=str(gap.lower()),
        full_explicit_budget_lower="0.022976",
    ), sort_keys=True))


if __name__ == "__main__":
    main()
