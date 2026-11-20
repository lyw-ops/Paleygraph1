"""Outward comparison of the genuine clipped and holomorphic product derivatives."""

import json
from pathlib import Path
import runpy

from flint import acb, acb_mat, arb, arb_mat, ctx


rotated = runpy.run_path(str(Path(__file__).with_name("rotated-cap-93-check.py")))
ctx.prec = 192
a, identity, kernel, s, size = (
    rotated[key] for key in ("a", "identity", "kernel", "s", "size")
)
marked_site = 0
active_site = 43


def enclose():
    row = rotated["sweep"]["trial"](float(1/2**0.5))
    evaluate = rotated["evaluate"]
    turn = arb(0)
    for _ in range(3):
        residual, jacobian, _, _, _ = evaluate(row, turn)
        step = jacobian.solve(residual)
        row = [acb((z.real-step[i,0]).mid(), (z.imag-step[i+size,0]).mid())
               for i,z in enumerate(row)]
    residual, jacobian, _, _, _ = evaluate(row, turn)
    inverse = jacobian.solve(identity)
    pre = arb_mat([[inverse[i,j].mid() for j in range(2*size)] for i in range(2*size)])
    radius = arb("1e-23")
    tube = [z+acb(arb(0,radius),arb(0,radius)) for z in row]
    _, jacobian, active, _, _ = evaluate(tube, turn)
    contraction = identity-pre*jacobian
    assert max(sum(abs(contraction[i,j]).upper() for j in range(2*size))
               for i in range(2*size)) < arb(1)/2
    displacement = pre*residual
    assert max(abs(displacement[i,0]).upper() for i in range(2*size)) < radius/2
    assert [(i, sign) for i,sign,_ in active] == [(active_site, 1)]
    return tube, jacobian, active[0][2]


def column_at(source_site, scale):
    return [kernel[i, source_site]*scale for i in range(size)]


def main():
    row, clipped, price = enclose()
    weights = [acb(1) for _ in row]
    weights[marked_site] = s
    weights[active_site] = acb(price)
    total = [(z*z+4*w).sqrt() for z,w in zip(row,weights)]
    # The positive-real-part square root is the clipped sum at these products.
    assert all(z.real > 0 for z in total)
    physical = acb_mat([[int(i == j) - kernel[i,j]*row[j]/total[j]
                         for j in range(size)] for i in range(size)])

    def log_response(delta, delta_w, test_site):
        return (delta - row[test_site]*delta_w/(2*weights[test_site]))/total[test_site]

    def product_derivative(source_site):
        rhs = acb_mat([[z] for z in column_at(source_site,2/total[source_site])])
        response = physical.solve(rhs)
        return [log_response(response[i,0],int(i==source_site),i) for i in range(size)]

    fixed_q_mark = product_derivative(marked_site)
    fixed_s_active = product_derivative(active_site)
    c = fixed_q_mark[active_site]
    assert (c - fixed_s_active[marked_site]).contains(0)
    hessian = fixed_s_active[active_site].imag
    assert hessian < -arb("0.064") and hessian > -arb("0.066")
    curvature = -(abs(c)**2)/hessian
    angular_lower = (1-a*a)/a * price * abs(c)**2
    assert curvature > angular_lower > 0

    def real_clipped_response(delta_s):
        rhs = column_at(marked_site,2*delta_s/total[marked_site])
        response = clipped.solve(rotated["column"](rhs))
        du = acb(response[marked_site,0],response[marked_site+size,0])
        return log_response(du,delta_s,marked_site)

    derivative_u = real_clipped_response(acb(1))
    derivative_v = real_clipped_response(acb(0,1))
    nonholomorphic = (derivative_u+acb(0,1)*derivative_v)/2
    assert nonholomorphic.real.contains(0)
    assert (2*nonholomorphic.imag-curvature).contains(0)
    assert nonholomorphic.imag > 0
    print(json.dumps(dict(
        kind="genuine_clipped_mark_curvature", precision=ctx.prec, prime=173,
        t_real="1/50", t_imag="13/1000", angular_cap="atan(1/sqrt(2))",
        active_site=active_site, active_sign=1, corrected_product=price.str(16),
        hessian=hessian.str(16), marked_site_response=[c.real.str(16),c.imag.str(16)],
        potential_laplacian=curvature.str(16), angular_lower=angular_lower.str(16),
        clipped_wirtinger_imag=nonholomorphic.imag.str(16),
        complex_reciprocity_and_clipped_response_overlap=True,
    ),sort_keys=True))


if __name__ == "__main__":
    main()
