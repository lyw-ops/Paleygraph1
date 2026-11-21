"""Outward validation of the genuine rotated cap at one small complex floor."""

from fractions import Fraction
import json
from pathlib import Path
import runpy

from flint import acb, arb, arb_mat, ctx


sweep = runpy.run_path(str(Path(__file__).with_name("cap-sweep-92-check.py")))
ctx.prec = 192
kernel, size, s, identity = (sweep[key] for key in ("kernel", "size", "s", "identity"))
multiplicities = sweep["prior"]["multiplicities"]
n = sum(multiplicities)
a = 1 / arb(2).sqrt()


def apply(values, turn):
    average = sum((m*z for m, z in zip(multiplicities, values)), acb(0)) / n
    rotation = acb(0, -turn) * average
    return [sum((kernel[i,j]*values[j] for j in range(size)), rotation)
            for i in range(size)]


def column(values):
    return arb_mat(2*size, 1, [z.real for z in values] + [z.imag for z in values])


def evaluate(row, turn):
    sums, d_x, d_y, d_a, active = [], [], [], [], []
    for i, z in enumerate(row):
        q = (1+a*a)/4 * (z.imag**2/a**2 - z.real**2)
        if i and q > 1:
            assert z.imag > 0 or z.imag < 0
            sign = 1 if z.imag > 0 else -1
            sums.append(sign*acb(z.imag/a, a*z.real))
            d_x.append(acb(0, sign*a))
            d_y.append(acb(sign/a))
            d_a.append(sign*acb(-z.imag/a**2, z.real))
            active.append((i, sign, q))
        else:
            if i:
                assert q < 1
            sums.append((4+z*z).sqrt() if i else s.sqrt()*(4+z*z/s).sqrt())
            d_x.append(z/sums[-1])
            d_y.append(acb(0, 1)*d_x[-1])
            d_a.append(acb(0))
    derivatives = d_x + d_y
    jacobian_entries = [[], []]
    for i in range(size):
        row_entries = [acb(int(i == j)) for j in range(size)] + [
            acb(0, int(i == j)) for j in range(size)
        ]
        for j, derivative in enumerate(derivatives):
            weight = acb(kernel[i,j % size], -turn*multiplicities[j % size]/n)
            row_entries[j] -= weight*derivative
        jacobian_entries[0].append([z.real for z in row_entries])
        jacobian_entries[1].append([z.imag for z in row_entries])
    jacobian = arb_mat(jacobian_entries[0]+jacobian_entries[1])
    residual = column([z-w for z,w in zip(row, apply(sums, turn))])
    for value, total in zip(row, sums):
        assert total.real > abs(value.real)
    mark_relative = (row[0]/(2*s.sqrt())).asinh().imag
    assert abs(mark_relative) < a.atan()
    assert abs((sums[0]+row[0]).arg()) < a.atan()
    assert abs((sums[0]-row[0]).arg()) < a.atan()
    average = sum((m*z for m,z in zip(multiplicities, sums)), acb(0))/n
    center_source = [acb(0, -(1+turn**2))*average]*size
    return residual, jacobian, active, column(center_source), column(apply(d_a, turn))


def slope(z, q, direction, i, da):
    # Active product q=(1+a²)[(Im U)²/a²−(Re U)²]/4.
    x, y = z.real, z.imag
    dx, dy = direction[i,0], direction[i+size,0]
    return (2*a*q/(1+a*a) - (1+a*a)*y*y/(2*a**3))*da + (
        (1+a*a)/2)*(y*dy/a**2-x*dx)


def check(center):
    b = arb(center.numerator)/center.denominator
    turn = b.tan()
    assert abs(turn) < a
    row = sweep["trial"](float(1/2**0.5))
    for _ in range(5):
        residual, jacobian, _, _, _ = evaluate(row, turn)
        step = jacobian.solve(residual)
        row = [acb((z.real-step[i,0]).mid(), (z.imag-step[i+size,0]).mid())
               for i,z in enumerate(row)]
    residual, jacobian, _, _, _ = evaluate(row, turn)
    inv = jacobian.solve(identity)
    pre = arb_mat([[inv[i,j].mid() for j in range(2*size)] for i in range(2*size)])
    radius = arb("1e-22")
    tube = [z+acb(arb(0,radius),arb(0,radius)) for z in row]
    _, patch, active, source_b, source_a = evaluate(tube, turn)
    contraction = identity-pre*patch
    assert max(sum(abs(contraction[i,j]).upper() for j in range(2*size))
               for i in range(2*size)) < arb(1)/2
    displacement = pre*residual
    assert max(abs(displacement[i,0]).upper() for i in range(2*size)) < radius/2
    record = dict(kind="rotated_physical_cap", prime=173, floor_real="1/50",
                  floor_imag="13/1000", tan_half_width="1/sqrt(2)",
                  center=str(center), precision=ctx.prec,
                  active_orbits=[(i, sign) for i, sign, _ in active])
    excess = sum((multiplicities[i]*(q-1) for i,_,q in active), arb(0))
    record["total_correction"] = excess.str(15) if active else "0"
    if center == 0:
        assert [(i, sign) for i, sign, _ in active] == [(43,1)]
        i, _, q = active[0]
        db = slope(tube[i], q, patch.solve(source_b), i, 0)
        dtheta = slope(tube[i], q, patch.solve(source_a*(1+a*a)), i, 1+a*a)
        loss = q*(1-a*a)/a
        assert (db-dtheta).contains(0)
        assert db < -loss and dtheta < -loss
        assert db > -16 and db < -15 and dtheta > -16 and dtheta < -15
        record.update(center_imbalance_derivative=db.str(15),
                      opening_total_derivative=dtheta.str(15),
                      loss_lower=loss.str(15))
    return record, excess


def main():
    left, midpoint, right = map(check, (Fraction(-1,250), Fraction(0), Fraction(1,250)))
    assert left[1] > midpoint[1] > 0 and right[1].is_zero()
    assert right[0]["active_orbits"] == []
    for record, _ in (left, midpoint, right):
        print(json.dumps(record, sort_keys=True))


if __name__ == "__main__":
    main()
