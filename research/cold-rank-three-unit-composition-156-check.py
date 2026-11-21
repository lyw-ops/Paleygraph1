"""Price an exact rank-three unit merge on both omitted derivative comparisons."""

from contextlib import redirect_stdout
import io
import json
from pathlib import Path
import runpy


def main():
    directory = Path(__file__).parent
    with redirect_stdout(io.StringIO()):
        replay = runpy.run_path(str(directory / "cold-resummed-136-check.py"))
    compose = runpy.run_path(str(directory / "cold-three-center-composition-153-check.py"))
    legendre = runpy.run_path(str(directory / "cold-signed-legendre-omission-150-check.py"))
    arb, acb, t = (replay[key] for key in ("arb", "acb", "t"))
    kern, prev = (replay["fields"][key] for key in ("kern", "prev"))
    alpha, beta, groups, _ = kern["p3"]["coefficients"](t, acb(prev["da"]), acb(prev["db"]))
    gamma = arb(499)/500 * beta * groups[1, 1][0, 0]
    delta = -2*gamma*kern["linear_scalar"](groups, beta)
    beta_cap, delta_cap = (replay[key] for key in ("b", "d"))
    assert abs(beta) <= beta_cap and abs(delta) <= delta_cap

    coefficients = replay["coefficients"]
    powers = legendre["tensor_counts"](len(coefficients)-1)
    b, c = (legendre["signed_labels"](arity, coefficients, powers, alpha, acb)[0, 0, 0]
            for arity in (1, 3))
    direct = delta*b
    contracted = 3*delta*beta**2*c/4
    merged = abs(direct + contracted).upper()
    signed_saving = abs(direct) + abs(contracted) - merged
    credited = delta_cap*(abs(b).upper() + 3*beta_cap**2*abs(c).upper()/4)
    saved = (credited - merged).lower()
    assert signed_saving > arb("0.00000005") and saved > arb("0.00000005")

    (B, B_tail), ((E1, E1_tail), (E2, E2_tail)), ((A1, A1_tail), _) = compose["geometry"](directory, replay)
    # The removed part has the same folded weights as the single G field.
    G = [kern["G"][5+k]*(2 if k else 1) for k in range(6)]
    def adjusted(row):
        result = list(row)
        for k, mass in enumerate(G):
            result[k] -= saved*mass
        assert all(entry >= 0 for entry in result)
        return result

    retained = compose["block_rate"](((adjusted(E2), A1), (B, adjusted(E1))), replay)
    tail = (E2_tail*arb("1.048") + A1_tail*arb("0.4122")
            + B_tail*arb("0.4112") + E1_tail*arb("0.6931"))
    result = retained + tail
    assert result < arb("0.66379866")
    print(json.dumps({
        "kind": "rank_three_unit_direct_two_height_composition",
        "signed_G_coefficient_saving_lower": "5e-8",
        "outward_composed_upper": "0.66379866",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
