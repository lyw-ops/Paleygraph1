"""Outward arithmetic for the height-100 nominal same-floor reflection."""

import json
from math import comb
from pathlib import Path
import runpy

from flint import acb, arb, ctx


def main():
    base = Path(__file__).resolve().parent
    fields = runpy.run_path(str(base / "astra-joint-65-check.py"))
    ctx.prec = 192
    joint, kernel, old, prior = (fields[key] for key in ("joint", "kern", "old", "prev"))
    rank_three = kernel["p3"]
    center, h, radius = arb(2031)/128, arb(2)**-17, arb(1)/4
    floor = center-h
    box = acb(arb(center, radius), arb(0, radius))
    alpha, beta, groups, amended = rank_three["coefficients"](
        box, acb(prior["da"]), acb(prior["db"]))
    gamma = arb(499)/500*beta*groups[1, 1][0, 0]
    delta = -2*gamma*kernel["linear_scalar"](groups, beta)
    z = old["prefix"](box)[0]
    w = joint["coefficient"](box, 0, 2, 0)

    # Only evaluate the amplitude. The inherited sign and packet tests
    # concern the smaller box used for the actual prefix.
    def scalar(arity, exponent):
        if abs(exponent) > 5:
            return acb(0)
        value = acb(0)
        for degree, terms in enumerate(rank_three["rank_powers"](4)):
            for (*labels, shift), multiplicity in terms.items():
                mode = abs(exponent-shift)
                if any(labels) or mode > 9:
                    continue
                row = (amended[mode] if arity+degree == 0 and mode in amended
                       else groups[arity+degree, mode])
                value += (row.get((0, 0), 0)*comb(arity+degree, arity)
                          *(beta/4)**degree*multiplicity/(2 if mode else 1))
        return value

    v = (scalar(0, 4) + gamma**2*scalar(2, 4)/8
         + gamma**4*(196*scalar(4, 4)+2*scalar(4, 2)+2*scalar(4, 6))/4096)
    mass = (2*abs(alpha)+3*abs(beta)+4*abs(gamma)+arb(23)/4*abs(delta)
            +8*(abs(z)+abs(w)+abs(v)))
    assert mass < arb("1.1")
    initial = 2*arb("1.1")/(radius-h)
    assert initial < 9

    old_rates = (base / "astra-adjoint-82-checks.jsonl").read_text().splitlines()
    q = arb("0.984138")
    logged = next(item for item in map(json.loads, old_rates) if item.get("height") == 100)
    assert arb(logged["rate_upper"]) < q
    eta = arb("4.8")**2/(4*floor)
    source = 2*eta/(floor.sqrt()*(1-eta)**arb("1.5"))
    assert source < arb("0.360")
    derivative = 9*q**100+arb("0.36")*(1-q**100)/(1-q)
    assert derivative < 21

    scale, difference = arb("0.61"), arb("2.1e-5")
    assert arb("4.8")/(2*floor.sqrt()) < scale
    assert h*(21/(2*floor.sqrt())+arb("4.8")/(4*floor**arb("1.5"))) < difference
    root = (1-scale**2).sqrt()
    log_mass, log_weight = scale.asin(), scale/root
    log_difference = difference/root
    log_weight_difference = log_difference+difference*scale**2/root**3
    secant_squared = 1/log_mass.cos()**2
    change_mass = secant_squared*log_difference
    change_weight = secant_squared*(log_weight_difference
                       +2*log_mass.tan()*log_weight*log_difference)
    rate = q+2*(change_mass+change_weight)
    assert 2*(change_mass+change_weight) < arb("0.00032") and rate < arb("0.9845")

    marked = arb(2).sqrt()/(1-arb("0.9845"))
    all_coordinates = arb(2).sqrt()*(2/(1-arb("0.9845"))-1)
    assert marked < 92 and all_coordinates < 182
    assert arb("4.768")/(4*floor+arb("4.768")**2).sqrt() < arb("0.514")

    residual = arb("0.169724")*arb("0.51358")**100
    secant_loss = 2*(arb(462).sqrt()+462*arb("0.001180"))
    assert residual < arb("3e-30") and secant_loss < 45
    assert (4*45/(8*floor)).sqrt() < arb("1.2")
    impulse = arb(3).sqrt()*h/(2*floor**arb("1.5"))
    signed = (1-arb("0.515")**2).sqrt()*arb("1e-4")-92*impulse*(16*residual).exp()
    assert signed > arb("7.55e-5")
    assert signed/182 > arb("4.14e-7")
    assert arb("4.14e-7")/(2*impulse+arb("2e-4")*residual) > arb("1.9")
    erase_rate = 182*arb("1.514")/500
    retained_angle = (1-arb("0.514")**2).sqrt()
    compensated = arb("1e-4")-92*impulse*(16*residual).exp()/(1-erase_rate)
    return_norm = 182*arb("1.514")/((1-erase_rate)*arb(500).sqrt())
    erased_source_lower = (retained_angle*compensated-arb("5e-5"))/return_norm
    quarter_residual = arb("0.0029")
    assert erased_source_lower > arb("6e-7")
    assert arb("2e-4")*quarter_residual*(1+501*quarter_residual**2).sqrt() < arb("6e-7")
    print(json.dumps(dict(
        kind="same_floor_real_reference_from_actual_complex_prefix", precision_bits=ctx.prec,
        center_feedback_mass_upper=mass.upper().str(14), time_source=source.str(14),
        predictor_time_derivative_upper=derivative.str(14), geometric_rate=rate.str(14),
        marked_limsup_bound=marked.str(14), all_source_limsup_bound=all_coordinates.str(14),
        complex_residual_upper=residual.str(14), signed_exterior_lower=signed.str(14),
        counting_residual_scale_lower="1.9", trimmed_source_lower=erased_source_lower.str(14),
        fourth_root_residual_scale_lower=quarter_residual.str(6),
    ), sort_keys=True))


if __name__ == "__main__":
    main()
