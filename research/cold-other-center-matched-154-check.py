"""Check two genuine selected omitted-center pairs on the cold square."""

from contextlib import redirect_stdout
import io
import json
from pathlib import Path
import runpy


def main():
    directory = Path(__file__).parent
    with redirect_stdout(io.StringIO()):
        replay = runpy.run_path(str(directory / "cold-resummed-136-check.py"))
    cosines = runpy.run_path(str(directory / "cold-W-all-order-return-152-check.py"))["cosines"]
    multiply = runpy.run_path(str(directory / "cold-leading-W-square-151-check.py"))["multiply"]
    arb, acb, t, price = (replay[key] for key in ("arb", "acb", "t", "price"))
    kern, prev = (replay["fields"][key] for key in ("kern", "prev"))
    alpha, beta, groups, _ = kern["p3"]["coefficients"](t, acb(prev["da"]), acb(prev["db"]))
    gamma = arb(499) / 500 * beta * groups[1, 1][0, 0]
    delta = -2 * gamma * kern["linear_scalar"](groups, beta)

    pairs = ((alpha * delta, -beta * gamma), (beta * delta, -(gamma**2)))
    slope = arb("0.000005")
    for z in (z for pair in pairs for z in pair):
        assert z.real < 0 and abs(z.imag) < -slope * z.real
    assert 1 / (1 + slope**2).sqrt() > 1 - arb("1.25e-11")

    root = 2 * t.sqrt()
    unit = replay["seed"] / root
    assert abs(unit) < arb("0.356") and abs(1 / root) < 1 / arb("7.96")
    _, derivative = cosines(unit, arb, acb)
    a = arb("0.356")**2
    orders = 14
    tail = a**orders * ((2*orders + 1)/(1-a) + 2*a/(1-a)**2) / arb("7.96")
    error = acb(arb(0, tail.upper()), arb(0, tail.upper()))
    b0, b2 = (derivative[j] / root + error for j in (0, 2))
    factor = b0 * (b0 + b2/2)
    assert abs(factor) > 0

    W = {0: arb(1), -1: arb(3)/4, 1: arb(3)/4, -3: arb(1)/4, 3: arb(1)/4}
    F = {k: kern["F"][4+k] for k in range(-4, 5)}
    G = {k: kern["G"][5+k] for k in range(-5, 6)}
    weights = [multiply(row, G, arb) for row in (W, F)]
    row_prices = [sum(mass*price(k) for k, mass in row.items() if k) for row in weights]
    combined_price = abs(factor)*sum(abs(left+right)*cost for (left, right), cost in zip(pairs, row_prices))

    relative_upper = "0.86"
    price_upper = "0.014"
    assert abs(4*t*factor) < arb(relative_upper)
    assert combined_price < arb(price_upper)
    print(json.dumps({
        "kind": "selected_actual_omitted_center_pairs_on_C1",
        "signed_summand_angular_slope_upper": "5e-6",
        "relative_merge_saving_upper": "1.25e-11",
        "all_order_factor_relative_to_leading_upper": relative_upper,
        "eventual_selected_packet_price_upper": price_upper,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
