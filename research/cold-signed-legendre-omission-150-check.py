"""Price the actual omission after signed Jacobi and Legendre label collection."""

from collections import Counter
from contextlib import redirect_stdout
import io
import json
from math import comb
from pathlib import Path
import runpy


def tensor_counts(max_degree):
    powers = [Counter({(0, 0): 1})]
    for _ in range(max_degree):
        row = Counter()
        for (a, b), count in powers[-1].items():
            row[a + 1, b] += count
            row[a, b + 1] += count
            if a:
                row[a - 1, b] += count
            if b:
                row[a, b - 1] += count
        powers.append(row)
    return powers


def signed_labels(omitted_degree, seed_coefficients, legendre_powers, alpha, acb):
    labels = {}
    for j in range(omitted_degree, len(seed_coefficients)):
        r = j - omitted_degree
        scale = comb(j, omitted_degree) * (alpha / 2)**r
        for k, coefficient in enumerate(seed_coefficients[j]):
            if coefficient.is_zero():
                continue
            for (a, b), count in legendre_powers[r].items():
                key = k, a, b
                labels[key] = labels.get(key, acb(0)) + scale * count * coefficient
    return labels


def folded_label_row(labels, width, arb):
    weights = [arb(0)] * (width + 1)
    for (k, a, b), coefficient in labels.items():
        cost = abs(coefficient).upper() * (b + 1)
        for shift in ((-k, k) if k else (0,)):
            for legendre_weight in range(-2 * a, 2 * a + 1, 4):
                weights[abs(shift + legendre_weight)] += cost
    return weights


def main():
    source = Path(__file__).with_name("cold-resummed-136-check.py")
    with redirect_stdout(io.StringIO()):
        replay = runpy.run_path(str(source))
    old = replay["inherited"]
    arb, acb, arb_poly = replay["arb"], replay["acb"], replay["arb_poly"]
    symmetric, folded, tilted = replay["symmetric"], replay["folded"], replay["tilted"]
    radius, cut_weight, eps = replay["radius"], replay["cut_weight"], replay["eps"]
    seed_coefficients = replay["coefficients"]
    max_degree = len(seed_coefficients) - 1
    fields = replay["fields"]
    kern, prev = fields["kern"], fields["prev"]
    alpha = kern["p3"]["coefficients"](replay["t"], acb(prev["da"]), acb(prev["db"]))[0]
    assert abs(alpha) < arb("0.244")

    legendre_powers = tensor_counts(max_degree - 1)
    for r in range((max_degree - 1) // 2 + 1):
        catalan = comb(2 * r, r) // (r + 1)
        next_catalan = comb(2 * r + 2, r + 1) // (r + 2)
        assert legendre_powers[2 * r][0, 0] == catalan * next_catalan
    rows = []
    for j in range(1, max_degree + 1):
        signed = signed_labels(j, seed_coefficients, legendre_powers, alpha, acb)
        width = 2 * (max_degree - j)
        weights = folded_label_row(signed, width, arb)
        rows.append((symmetric(weights, width), width, tilted(weights)))

    fixed_other = list(replay["center"])
    fixed_other[0] -= replay["a"]
    fixed_other[2] -= replay["a"]
    assert all(x >= 0 for x in fixed_other)
    for height, envelope in ((601, old["h"]), (602, replay["h"])):
        residual, _ = old["residual"](envelope)
        other_row = [value + folded(residual, radius, k)
                     for k, value in enumerate(fixed_other)]
        other = symmetric(other_row, radius)
        other_tilt = tilted(other_row)
        other_power = arb_poly([1])
        retained = [arb(0)] * (cut_weight + 1)
        loss = arb(0)
        for j, (multiplier, width, multiplier_tilt) in enumerate(rows, 1):
            other_power *= other
            comparison = multiplier * other_power
            midpoint = width + j * radius
            for k in range(cut_weight + 1):
                retained[k] += folded(comparison, midpoint, k)
            loss += sum(folded(comparison, midpoint, k) * (arb(k) / 5).cosh()
                        for k in range(cut_weight + 1, midpoint + 1))
            loss += multiplier_tilt * j * eps * (other_tilt + eps)**(j - 1)
        rate = replay["price_rate"](retained) + 10 * loss + replay["old_tail_price"]
        assert rate < arb("0.540")
        print(json.dumps({
            "kind": "actual_signed_jacobi_legendre_omission",
            "height": height,
            "eventual_total_upper": "0.540",
            "taylor_orders": 14,
            "max_omitted_degree": max_degree,
        }, sort_keys=True))


if __name__ == "__main__":
    main()
