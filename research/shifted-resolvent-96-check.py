"""Check the translated-column rate and interpolation arithmetic against R82."""

import json
from pathlib import Path

from flint import arb, ctx


def main():
    ctx.prec = 192
    inherited = Path(__file__).with_name("astra-adjoint-82-checks.jsonl")
    records = map(json.loads, inherited.read_text().splitlines())
    rates = {record["height"]: arb(record["rate_upper"])
             for record in records if record["kind"] == "physical_packet_operator"}
    upper_100 = arb("0.984138")
    upper_250, upper_600 = arb("0.996682"), arb("1.046434")
    assert rates[100] < upper_100 and rates[250] < upper_250 and rates[600] < upper_600
    factor_250 = upper_250*(1+arb(2)/1000)
    factor_600 = upper_600*(1+arb(2)/5000)
    assert factor_250 < arb("0.999") and factor_600 < arb("1.048")

    rate_price, rate_euclidean = arb("1.048"), arb("0.514")
    exponent = -(rate_euclidean.log())/(2*(rate_price/rate_euclidean).log())
    assert exponent > arb("0.467")
    marked_100 = arb(2).sqrt()/(1-upper_100)
    all_100 = arb(2).sqrt()*(2/(1-upper_100)-1)
    assert marked_100 < 90 and all_100 < 178
    exterior_first_norm = arb("7.648e-5")/178
    assert exterior_first_norm > arb("4.296e-7")
    print(json.dumps(dict(
        kind="translated_physical_resolvent_rate_comparison", precision_bits=ctx.prec,
        geometric_price_factor_250=factor_250.str(16),
        geometric_price_factor_600=factor_600.str(16),
        eventual_geometric_margin_250=(arb("0.999")-factor_250).str(16),
        eventual_geometric_margin_600=(rate_price-factor_600).str(16),
        resolvent_coordinate_exponent_600=exponent.str(16),
        height_100_marked_column_limsup=marked_100.str(16),
        height_100_max_entry_limsup=all_100.str(16),
        first_hit_exterior_first_norm_over_sqrt_n_lower=exterior_first_norm.str(16),
        scopes=["strict packet contraction at 250", "packet and Euclidean interpolation at 600"],
    ), sort_keys=True))


if __name__ == "__main__":
    main()
