"""Enclose the actual marked curvature of the positive balanced prime-173 row."""

import json
from pathlib import Path
import runpy

from flint import acb, acb_mat, arb, arb_mat, ctx


center = runpy.run_path(str(Path(__file__).with_name("astra-center-94-check.py")))
ctx.prec = 256
kernel, size, multiplicities, n, s, a = (
    center[key] for key in ("K", "size", "mult", "n", "s", "a")
)
upper, lower = 43, 29
active_sites = (upper, lower)


def enclose_balanced_row():
    joint = center["joint"]
    row = center["propose"](0.1413)
    for _ in range(4):
        residual, jacobian, *_ = joint(row)
        step = jacobian.solve(residual)
        row = [(value-step[i, 0]).mid() for i, value in enumerate(row)]
    residual, jacobian, *_ = joint(row)
    dimension = len(row)
    identity = arb_mat([[int(i == j) for j in range(dimension)] for i in range(dimension)])
    inverse = jacobian.solve(identity).mid()
    radius = arb("1e-24")
    tube = [value + arb(0, radius) for value in row]
    _, patch, charges, difference, total = joint(tube)
    norm = center["row_norm"]
    assert norm(identity-inverse*patch) < arb(1)/2
    assert norm(inverse*residual) < radius/2
    assert {i: sign for i, (sign, _) in charges.items()} == {upper: 1, lower: -1}
    assert abs(tube[-1]) < a
    excess = charges[upper][1] - 1
    assert (excess - 2*(charges[lower][1]-1)).contains(0)
    assert excess > arb("0.4150") and excess < arb("0.4151")
    return tube[-1], patch, charges, difference, total


def main():
    turn, patch, charges, difference, total = enclose_balanced_row()
    weights = [acb(1) for _ in range(size)]
    weights[0] = s
    for i in active_sites:
        weights[i] = acb(charges[i][1])
    scaled_kernel = acb_mat([[acb(kernel[i, j], -turn*multiplicities[j]/n)
                             for j in range(size)] for i in range(size)])
    holomorphic = acb_mat([[int(i == j)-scaled_kernel[i, j]*difference[j]/total[j]
                           for j in range(size)] for i in range(size)])

    def log_response(delta, delta_weight, i):
        return (delta-difference[i]*delta_weight/(2*weights[i]))/total[i]

    def source(i, delta_weight):
        return [scaled_kernel[j, i]*2*delta_weight/total[i] for j in range(size)]

    sites = (0, *active_sites)
    normalizer = {i: arb(multiplicities[i]).sqrt() for i in sites}
    complex_derivatives = {}
    for j in sites:
        rhs = acb_mat([[value] for value in source(j, 1)])
        response = holomorphic.solve(rhs)
        for i in sites:
            complex_derivatives[i, j] = (
                log_response(response[i, 0], int(i == j), i)*normalizer[i]/normalizer[j]
            )
    for i in sites:
        for j in sites:
            assert (complex_derivatives[i, j]-complex_derivatives[j, i]).contains(0)
    c = acb_mat([[complex_derivatives[i, 0]] for i in active_sites])
    H = arb_mat([[complex_derivatives[i, j].imag for j in active_sites] for i in active_sites])
    assert H[0, 0] < 0 < H[1, 1]
    upper_charge = abs(c[0, 0])**2 / (-H[0, 0])
    lower_charge = abs(c[1, 0])**2 / H[1, 1]
    c_real = arb_mat([[c[i, 0].real] for i in range(2)])
    c_imag = arb_mat([[c[i, 0].imag] for i in range(2)])
    curvature = -(c_real.transpose()*H.solve(c_real) + c_imag.transpose()*H.solve(c_imag))[0, 0]
    assert -lower_charge < curvature < upper_charge

    # The last row and column of the joint solve are balance and cap center.
    # Differentiate the clipped system with the certified center held fixed.
    fixed_cap = arb_mat([[patch[i, j] for j in range(2*size)] for i in range(2*size)])

    def clipped_response(delta_weight):
        column = source(0, delta_weight)
        rhs = arb_mat(2*size, 1, [z.real for z in column] + [z.imag for z in column])
        response = fixed_cap.solve(rhs)
        return log_response(acb(response[0, 0], response[size, 0]), delta_weight, 0)

    nonholomorphic = (clipped_response(1) + acb(0, 1)*clipped_response(acb(0, 1)))/2
    assert nonholomorphic.real.contains(0)
    assert (2*nonholomorphic.imag-curvature).contains(0)
    assert arb("7.11921e-7") < curvature < arb("7.11923e-7")
    print(json.dumps(dict(
        kind="positive_balanced_pair_at_fixed_center_has_nonzero_marked_curvature", p=173,
        precision=ctx.prec, t_real="1/50", t_imag="17/1000", upper_orbit=upper,
        lower_orbit=lower, center=turn.atan().str(16), excess=(charges[upper][1]-1).str(16),
        active_matrix=[[H[i, j].str(16) for j in range(2)] for i in range(2)],
        upper_charge=upper_charge.str(16), lower_charge=lower_charge.str(16),
        curvature=curvature.str(16), clipped_wirtinger_imag=nonholomorphic.imag.str(16),
    ), sort_keys=True))


if __name__ == "__main__":
    main()
