"""Outward enclosure of the two real endpoint problems at a clipped prime row."""

import json
from pathlib import Path
import runpy

from flint import acb, arb, arb_mat, ctx
import numpy as np


base = runpy.run_path(str(Path(__file__).with_name("astra-cold-37.py")))
ctx.prec = 192
prime = 173
sign = base["paley_sign"](prime)
n = len(sign)
kernel = base["even_kernel"](sign)
size = kernel.nrows()
multiplicities = [1, *([2] * (size - 2)), 1]
a = 1 / arb(2).sqrt()
c = (1 + a*a) / 4
s = n / acb(arb(1)/50, arb(13)/1000)


def midpoint_row():
    numeric_kernel = np.array([[float(kernel[i, j]) for j in range(size)]
                               for i in range(size)])
    root_mark = np.sqrt(complex(s))
    row = np.zeros(size, dtype=complex)
    for _ in range(4500):
        sign_im = np.where(row.imag >= 0, 1, -1)
        cost = 0.75 * row.imag**2 - 0.375 * row.real**2
        total = np.where(cost <= 1, np.sqrt(4+row*row),
                         np.sqrt(2)*abs(row.imag) + 1j*sign_im*row.real/np.sqrt(2))
        total[0] = root_mark * np.sqrt(4 + (row[0]/root_mark)**2)
        row = (row + numeric_kernel @ total) / 2
    return [acb(arb(float(z.real)), arb(float(z.imag))) for z in row]


def evaluate(row):
    total, partials, capped = [], [], set()
    for i, z in enumerate(row):
        cost = 3*z.imag**2/4 - 3*z.real**2/8
        if i and cost > 1:
            assert z.imag > 0 or z.imag < 0
            side = 1 if z.imag > 0 else -1
            total.append(acb(side*z.imag/a, side*a*z.real))
            partials.append((0, side/a, side*a, 0))
            capped.add(i)
        else:
            if i:
                assert cost < 1
            total.append((4+z*z).sqrt() if i else s.sqrt()*(4+z*z/s).sqrt())
            d = z / total[-1]
            partials.append((d.real, -d.imag, d.imag, d.real))
    jacobian = arb_mat([[int(i == j) - kernel[i % size, j % size]
                         * partials[j % size][2*(i//size)+j//size]
                         for j in range(2*size)] for i in range(2*size)])
    residual = [z - sum((kernel[i,j]*total[j] for j in range(size)), acb(0))
                for i,z in enumerate(row)]
    vector = arb_mat(2*size, 1, [z.real for z in residual] + [z.imag for z in residual])
    return total, jacobian, vector, capped


def main():
    center = midpoint_row()
    for _ in range(2):
        _, jacobian, residual, _ = evaluate(center)
        step = jacobian.solve(residual)
        center = [acb((z.real-step[i,0]).mid(), (z.imag-step[i+size,0]).mid())
                  for i,z in enumerate(center)]
    _, jacobian, residual, _ = evaluate(center)
    identity = arb_mat([[int(i == j) for j in range(2*size)] for i in range(2*size)])
    inv = jacobian.solve(identity)
    preconditioner = arb_mat([[inv[i,j].mid() for j in range(2*size)] for i in range(2*size)])
    radius = arb("1e-23")
    tube = [z + acb(arb(0, radius), arb(0, radius)) for z in center]
    total, interval_jac, _, capped = evaluate(tube)
    contraction = identity - preconditioner * interval_jac
    assert max(sum(abs(contraction[i,j]).upper() for j in range(2*size))
               for i in range(2*size)) < arb(1)/2
    displacement = preconditioner * residual
    assert max(abs(displacement[i,0]).upper() for i in range(2*size)) < radius/2
    assert capped == {43}
    A, B = [(u+z)/2 for u,z in zip(total,tube)], [(u-z)/2 for u,z in zip(total,tube)]
    P_plus = [z.real+z.imag/a for z in A]
    P_minus = [z.real-z.imag/a for z in A]
    Q_plus = [z.real+z.imag/a for z in B]
    Q_minus = [z.real-z.imag/a for z in B]
    assert all(P_plus[i] > 0 and Q_plus[i] > 0 and P_minus[i] > 0 and Q_minus[i] > 0
               for i in range(size) if i != 43)
    assert P_minus[43].contains(0) and Q_plus[43].contains(0)
    assert P_plus[43] > 0 and Q_minus[43] > 0
    tau_plus, tau_minus = P_plus[0]*Q_plus[0], P_minus[0]*Q_minus[0]
    h, d = (tau_plus+tau_minus)/2, s.imag/a
    delta_mark = (P_plus[0]-P_minus[0])*(Q_minus[0]-Q_plus[0])
    assert s.real > abs(d)
    assert (h + c*delta_mark - s.real).contains(0)
    assert (tau_plus-tau_minus-2*d).contains(0)
    assert h-s.real > 0 and h-s.real < c*(tau_plus.sqrt()-tau_minus.sqrt())**2
    defect = c*P_plus[43]*Q_minus[43] - 1
    assert defect > 0
    mean_plus = sum(m*z for m,z in zip(multiplicities,P_plus))/n
    mean_minus = sum(m*z for m,z in zip(multiplicities,P_minus))/n
    weights_plus = [p*q for p,q in zip(P_plus,Q_plus)]
    weights_minus = [p*q for p,q in zip(P_minus,Q_minus)]
    gap_minus = arb(0)
    gap_plus = arb(0)
    bregman_minus = arb(0)
    bregman_plus = arb(0)
    for i in range(size):
        if i == 43:
            continue
        ratio = P_plus[i]*mean_minus/(P_minus[i]*mean_plus)
        weight_minus = multiplicities[i]*weights_minus[i]
        weight_plus = multiplicities[i]*weights_plus[i]
        gap_minus -= weight_minus*ratio.log()
        gap_plus += weight_plus*ratio.log()
        bregman_minus += weight_minus*(ratio-1-ratio.log())
        bregman_plus += weight_plus*(1/ratio-1+ratio.log())
    switch_price = mean_minus/mean_plus*P_plus[43]*Q_minus[43]
    assert (gap_minus-switch_price-bregman_minus).contains(0)
    assert (gap_plus-bregman_plus).contains(0)
    assert gap_minus > switch_price > 0
    assert gap_plus > 0
    print(json.dumps(dict(
        kind="two_real_stationary_endpoint_switch",
        prime=prime, real="1/50", imag="13/1000", kappa=2, precision=ctx.prec,
        zero_weight_orbits=[43], cap_correction=defect.str(15),
        real_mark_weights=[tau_plus.str(15), tau_minus.str(15)],
        plus_phase_switch_price=switch_price.str(15),
        endpoint_objective_gaps=[gap_plus.str(15), gap_minus.str(15)],
    ), sort_keys=True))


if __name__ == "__main__":
    main()
