"""Outward scalar margins for the rotated, erased Newton first hit."""

import json

from flint import arb, ctx


def main():
    ctx.prec = 192
    half = arb(2)**-17
    floor = arb(2031)/128-half
    markup = 2*arb("1e-4")/arb(3).sqrt()-arb("7.1e-5")
    g_angle, u_angle = arb("2.03e-5"), (arb("1e-4")/arb(3).sqrt()).asin()
    assert half*(21/floor.sqrt()+arb("4.768")/(2*floor**arb("1.5")))/2 < g_angle.sin()
    assert 21*half/(2*arb("1e30").sqrt()) < g_angle.sin()
    assert half/(2*floor) < u_angle
    assert ((u_angle+g_angle)/2).tan()+g_angle.tan() < arb("6.1e-5")
    assert half*(arb("15.811")/floor.sqrt()+arb("0.075")/(2*floor**arb("1.5"))) < arb("3.04e-5")
    assert arb("0.075")/floor.sqrt() < arb("0.019")
    assert 1/(1-arb("0.51358")) < arb("2.057")

    entry, entry_imag, erasure = arb(178), arb("0.283"), 2000
    secant_gap = arb("1.514")
    crude_rate = entry*secant_gap/10**7
    assert markup-crude_rate/(1-crude_rate)*arb("0.019") > arb("4.39e-5")
    rate = entry*secant_gap/erasure
    im_gain = (entry_imag*secant_gap+entry*arb("6.1e-5"))/erasure/(1-rate)**2
    nominal_debit = rate/(1-rate)*arb("3.04e-5")+im_gain*arb("0.019")
    assert nominal_debit < arb("1.031e-5")
    signed = markup-nominal_debit
    assert signed > arb("3.41e-5")
    source_lower = signed*(1-rate)/entry
    assert source_lower > arb("1.65e-7")

    real_change = entry*rate/(1-rate)
    imaginary_change = entry_imag*rate/(1-rate)+entry*im_gain
    assert real_change < arb("27.72") and imaginary_change < arb("0.097")
    assert entry+real_change < 206 and entry_imag+imaginary_change < arb("0.380")
    ordinary_debit = arb("0.025")**2*(
        arb("27.72")*(arb("0.000055")+arb("0.09834")*arb("0.00624"))
        +arb("0.097")*arb("0.04919"))
    ordinary_lower = arb("3.41e-5")-ordinary_debit
    assert ordinary_lower > arb("1.94e-5")
    mixed_lower = ordinary_lower-arb("0.015")*arb("0.025")**2
    assert mixed_lower > arb("1e-5")
    print(json.dumps(dict(
        kind="physical_newton_erasure_rotated_arithmetic",
        precision_bits=ctx.prec, maximum_erased_sites="floor(sqrt(n)/2000)",
        compensated_signed_exterior_lower=signed.str(18),
        surviving_l1_over_sqrt_n_lower=source_lower.str(18),
        scaled_real_entry_change_upper=real_change.str(18),
        scaled_imaginary_entry_change_upper=imaginary_change.str(18),
        ordinary_exterior_lower_if_quarter_scaled_envelope_at_most_0p025=ordinary_lower.str(18),
        mixed_exterior_lower_in_same_regime=mixed_lower.str(18),
    ), sort_keys=True))


if __name__ == "__main__":
    main()
