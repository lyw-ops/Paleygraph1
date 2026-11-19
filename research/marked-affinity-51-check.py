"""Enclose marked transfer bounds using exact positive Picard prefix rows."""
from fractions import Fraction
import json
from math import factorial
from pathlib import Path
import sys

from flint import acb, arb, ctx

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from square_control import square_field_sign
from theta import paley_sign


def verify(order, depth, square_root=None):
    sign = square_field_sign(square_root) if square_root else paley_sign(order)
    n = len(sign)
    w = [arb(1)] + [arb(1) / (2 * n)] * (n - 1)
    v = [arb(0)] * n
    for _ in range(depth + 1):
        u = [(value * value + 4 * weight).sqrt() for value, weight in zip(v, w)]
        coefficients = acb.dft([acb(value) for value in u])
        v_next = [value.real / n for value in acb.dft([
            int(label) * coefficient for label, coefficient in zip(sign, coefficients)
        ])]
        v = v_next

    assert all(level > abs(value) for level, value in zip(u, v_next))
    product = [(level * level - value * value) / 4
               for level, value in zip(u, v_next)]
    assert all(weight > 0 for weight in product)
    center = ((u[0] + v_next[0]) / (u[0] - v_next[0])).log() / 2
    total = sum(w)
    trial_total = sum(product)
    root = [(weight / total).sqrt() for weight in w]
    trial_root = [(weight / trial_total).sqrt() for weight in product]
    A = root[0] * trial_root[0]
    B = sum(x * y for x, y in zip(root[1:], trial_root[1:]))
    defects = [x - y for x, y in zip(root, trial_root)]
    D = sum(defect * defect for defect in defects) / 2
    assert (D - (1 - A - B)).contains(0)
    radius = 2 * (D * (1 - A + B) / (4 * A)).sqrt().asinh()
    old_defects = [weight.sqrt() - (trial / product[0]).sqrt()
                   for weight, trial in zip(w[1:], product[1:])]
    old_radius = sum(defect * defect for defect in old_defects).sqrt()
    lower = center - radius
    upper = center + radius
    assert radius < old_radius
    if order == 97:
        assert abs(center) + radius < arb(1469) / 100000
        assert abs(center) + old_radius > arb(22) / 1000
    elif order == 173:
        assert lower > arb(1375) / 100000 and upper < arb(1690) / 100000
        assert abs(center) + old_radius > arb(18) / 1000
    elif order == 401:
        assert upper < -arb(184) / 10000
        assert center + old_radius < -arb(184) / 10000
    elif order == 121:
        assert lower > arb(91) / 1000
        assert center - old_radius < arb(81) / 1000
    print(json.dumps(dict(order=order, square_root=square_root, a="1/2", depth=depth,
                          center=str(center), marked_radius=str(radius),
                          old_radius=str(old_radius), lower_mark=str(lower),
                          upper_mark=str(upper),
                          bulk_product_lower=str(min(weight.lower()
                                                     for weight in product[1:]))),
                     sort_keys=True))


def verify_square_stencil():
    anchor = 25
    degree = 93
    cold = Fraction(1, 2)
    assert anchor * anchor * Fraction(99, 100) > Fraction(197, 8) ** 2
    assert Fraction(1 + anchor) / (1 + cold) < sum(
        Fraction(3**power, factorial(power)) for power in range(6)
    )
    ratio = (anchor - cold) / (anchor + cold)
    assert 3 * ratio**degree < Fraction(74, 1000)
    assert Fraction(1, 7) > Fraction(14, 100)
    assert Fraction(14, 100) - Fraction(74, 1000) > Fraction(6, 100)
    print(json.dumps(dict(kind="exact_square_stencil_constants", anchor=anchor,
                          degree=degree, cold=str(cold), excess_lower="3/50"),
                     sort_keys=True))


if __name__ == "__main__":
    ctx.prec = 320
    for field, depth, root in [(97, 9, None), (173, 16, None), (401, 32, None), (121, 16, 11)]:
        verify(field, depth, root)
    verify_square_stencil()
