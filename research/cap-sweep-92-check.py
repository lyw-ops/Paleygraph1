"""Outward validation of the physical correction as three real caps vary."""

from fractions import Fraction
import json
from pathlib import Path
import runpy

from flint import acb, arb, arb_mat, ctx
import numpy as np


prior = runpy.run_path(str(Path(__file__).with_name("real-two-marks-91-check.py")))
ctx.prec = 192
kernel, size, s = (prior[key] for key in ("kernel", "size", "s"))
identity = arb_mat([[int(i == j) for j in range(2*size)] for i in range(2*size)])


def trial(cap):
    numeric_kernel = np.array([[float(kernel[i, j]) for j in range(size)]
                               for i in range(size)])
    mark = np.sqrt(complex(s))
    row = np.zeros(size, dtype=complex)
    for _ in range(1000):
        cost = (1+cap*cap) * (row.imag**2/cap**2 - row.real**2)/4
        side = np.where(row.imag >= 0, 1, -1)
        sums = np.where(cost <= 1, np.sqrt(4+row*row),
                        side*(row.imag/cap + 1j*cap*row.real))
        sums[0] = mark * np.sqrt(4+(row[0]/mark)**2)
        row = (row + numeric_kernel @ sums)/2
    return [acb(arb(float(z.real)), arb(float(z.imag))) for z in row]


def evaluate(row, cap):
    sums, partials, cap_partials = [], [], []
    charged = []
    for i, z in enumerate(row):
        cost = (1+cap*cap) * (z.imag**2/cap**2 - z.real**2)/4
        if i and cost > 1:
            assert z.imag > 0 or z.imag < 0
            side = 1 if z.imag > 0 else -1
            sums.append(side*acb(z.imag/cap, cap*z.real))
            partials.append((0, side/cap, side*cap, 0))
            cap_partials.append(side*acb(-z.imag/cap**2, z.real))
            charged.append((i, side, cost))
        else:
            if i:
                assert cost < 1
            sums.append((4+z*z).sqrt() if i else s.sqrt()*(4+z*z/s).sqrt())
            d = z / sums[-1]
            partials.append((d.real, -d.imag, d.imag, d.real))
            cap_partials.append(acb(0))

    def apply(values):
        return [sum((kernel[i,j]*values[j] for j in range(size)), acb(0))
                for i in range(size)]

    def real_column(values):
        return arb_mat(2*size, 1, [z.real for z in values] + [z.imag for z in values])

    residual = real_column([z-root for z,root in zip(row, apply(sums))])
    cap_source = real_column(apply(cap_partials))
    jacobian = arb_mat([[int(i == j) - kernel[i % size, j % size]
                         * partials[j % size][2*(i//size)+j//size]
                         for j in range(2*size)] for i in range(2*size)])
    for z, total in zip(row, sums):
        assert total.real > abs(z.real)
    return residual, jacobian, cap_source, charged


def check(capr):
    cap = arb(capr.numerator) / capr.denominator
    row = trial(float(capr))
    for _ in range(2):
        residual, jacobian, _, _ = evaluate(row, cap)
        step = jacobian.solve(residual)
        row = [acb((z.real-step[i,0]).mid(), (z.imag-step[i+size,0]).mid())
               for i,z in enumerate(row)]
    residual, jacobian, _, _ = evaluate(row, cap)
    inv = jacobian.solve(identity)
    pre = arb_mat([[inv[i,j].mid() for j in range(2*size)] for i in range(2*size)])
    radius = arb("1e-23")
    tube = [z + acb(arb(0, radius), arb(0, radius)) for z in row]
    _, jacobian, source, charged = evaluate(tube, cap)
    contraction = identity - pre*jacobian
    assert max(sum(abs(contraction[i,j]).upper() for j in range(2*size))
               for i in range(2*size)) < arb(1)/2
    defect = pre*residual
    assert max(abs(defect[i,0]).upper() for i in range(2*size)) < radius/2
    assert cap > abs(s.imag)/(2*s.real)
    record = dict(kind="canonical_cap_price", prime=173, real="1/50",
                  imag="13/1000", cap=str(capr), precision=ctx.prec,
                  positive_active_sites=[i for i, side, _ in charged if side > 0],
                  negative_active_sites=[i for i, side, _ in charged if side < 0])
    if charged:
        assert [(i, side) for i, side, _ in charged] == [(43, 1)]
        drow = jacobian.solve(source)
        i, _, cost = charged[0]
        z = tube[i]
        slope = (cap/2)*(z.imag**2/cap**2-z.real**2) + (1+cap**2)/2*(
            z.imag*drow[i+size,0]/cap**2-z.real*drow[i,0]-z.imag**2/cap**3)
        lower = (1-cap**2)/(cap*(1+cap**2))*cost
        assert -slope > lower > 0
        record.update(total_correction=(cost-1).str(16), derivative=slope.str(16),
                      one_sign_loss_lower=lower.str(16))
        return record, cost-1
    record.update(total_correction="0", derivative="0")
    return record, arb(0)


def main():
    tight, middle, wide = map(check, (Fraction(7,10), Fraction(707,1000), Fraction(143,200)))
    assert tight[1] > middle[1] > wide[1]
    assert wide[0]["positive_active_sites"] == wide[0]["negative_active_sites"] == []
    for record, _ in (tight, middle, wide):
        print(json.dumps(record, sort_keys=True))


if __name__ == "__main__":
    main()
