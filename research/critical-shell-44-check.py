"""Arb brackets on the true rooted Picard critical slice."""

import json
from pathlib import Path
import sys

from flint import arb, arb_mat, ctx
import numpy as np
from scipy.optimize import linprog

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from square_control import square_field_sign
from theta import paley_sign


SCALE = 10**12


def rounded(values):
    return [arb(round(float(value)*SCALE))/SCALE for value in values]


def pad_rows(row):
    low = min(value.lower() for value in row)
    return (-low if low < 0 else arb(0)) + arb(1)/SCALE


def midpoint_array(rows):
    return np.array([[float(value.mid()) for value in row] for row in rows])


class Shell:
    def __init__(self, signs, tau):
        self.n = len(signs)
        self.tau = tau
        self.root_n = arb(self.n).sqrt()
        self.critical = (1+(1-arb(1)/self.n)*tau).sqrt()
        self.mass = self.critical/self.root_n
        cosines = [(arb(2*j)/self.n).cos_pi() for j in range(self.n)]
        self.basis = {}
        self.numeric_basis = {}
        self.reference = {}
        for sigma in (1, -1):
            positions = [j for j in range(1, self.n//2+1) if signs[j] == sigma]
            basis = [[cosines[(i*j) % self.n] for j in positions] for i in range(self.n)]
            self.basis[sigma] = basis
            self.numeric_basis[sigma] = midpoint_array(basis)
            result = linprog(-np.ones(len(positions)), A_ub=-self.numeric_basis[sigma],
                             b_ub=np.ones(self.n), bounds=(None, None), method="highs")
            assert result.success
            row = self.row(sigma, rounded(result.x))
            pad = pad_rows(row)
            row = [(entry+pad)/(1+pad) for entry in row]
            assert all(entry > 0 for entry in row)
            self.reference[sigma] = row
        column = [sum(int(s)*cosines[i*j % self.n] for j, s in enumerate(signs))/self.n
                  for i in range(self.n)]
        self.kernel = arb_mat([[column[(i-j) % self.n] for j in range(self.n)]
                               for i in range(self.n)])

    def row(self, sigma, coeffs):
        return [1+sum(x*y for x, y in zip(basis_row, coeffs))
                for basis_row in self.basis[sigma]]

    def apply(self, row):
        return list(self.kernel*arb_mat(self.n, 1, row))

    def orbit(self, times):
        state = [arb(0)]*self.n
        weights = [arb(1)] + [self.tau/self.n]*(self.n-1)
        deficits = mark_loss = arb(0)
        early = [[arb(int(i == 0)) for i in range(self.n)]]
        for t in range(1, max(times)+1):
            activation = [(v*v+4*w).sqrt() for v, w in zip(state, weights)]
            g = sum(activation)/(2*self.root_n)
            deficits += 2*(self.critical-g)
            bulk_root = (state[0]*state[0]+4*self.tau/self.n).sqrt()
            mark_loss += 2-activation[0]+bulk_root
            state = self.apply(activation)
            y = [self.root_n*v for v in state]
            if t <= 4:
                early.append(y)
            if t in times:
                yield t, y, early, deficits, mark_loss

    def primal_lower(self, sigma, score, interior):
        numeric = self.numeric_basis[sigma]
        coeff_cost = np.array([float(x.mid()) for x in score]) @ numeric
        result = linprog(-coeff_cost, A_ub=-numeric, b_ub=np.ones(self.n),
                         A_eq=np.ones((1, numeric.shape[1])),
                         b_eq=[float((self.root_n*self.critical-1).mid())],
                         bounds=(None, None), method="highs")
        assert result.success
        coeffs = rounded(result.x)
        coeffs[0] = self.root_n*self.critical-1-sum(coeffs[1:])
        candidate = self.row(sigma, coeffs)
        mix = arb(1)/SCALE
        repaired = [(1-mix)*v+mix*w for v, w in zip(candidate, interior)]
        while not all(value > 0 for value in repaired):
            mix *= 10
            assert mix <= 1
            repaired = [(1-mix)*v+mix*w for v, w in zip(candidate, interior)]
        return sum(x*y for x, y in zip(score, repaired))/self.n

    def certify_dual(self, score, basis):
        matrix = [[arb(1), arb(int(i == 0)), *row] for i, row in enumerate(basis)]
        result = linprog([1., float(self.mass.mid())]+[0.]*len(basis[0]),
                         A_ub=-midpoint_array(matrix),
                         b_ub=[-float(value.mid()) for value in score],
                         bounds=(None, None), method="highs")
        assert result.success
        coeffs = rounded(result.x)
        res = [sum(x*y for x, y in zip(row, coeffs))-score[i]
               for i, row in enumerate(matrix)]
        pad = pad_rows(res)
        assert all(value+pad > 0 for value in res)
        return coeffs[0]+pad+coeffs[1]*self.mass

    def restricted_basis(self, sigma, early, terminal):
        columns = []
        for vector in [*early, terminal]:
            average = sum(vector)/self.n
            kv = self.apply(vector)
            columns.append([(value-average-sigma*image)/2
                            for value, image in zip(vector, kv)])
        return list(zip(*columns))

    def certify_case(self, q, tau_label, times, saturated_root=None):
        available = {}
        for sigma in (1, -1):
            reference = self.reference[sigma]
            lower_mark = reference[0]/self.root_n
            upper_mark = self.root_n/self.reference[-sigma][0]
            if saturated_root is not None and sigma == 1:
                subfield_witness = [arb(saturated_root-1 if i % (saturated_root-1) == 0 else 0)
                                    for i in range(self.n)]
                assert (subfield_witness[0]/self.root_n-self.critical).contains(0)
                available[sigma] = (subfield_witness, self.critical, self.critical, True)
            elif upper_mark < self.critical:
                print(json.dumps(dict(kind="empty_critical_slice", q=q, tau=tau_label,
                                      sigma=sigma, critical=str(self.critical),
                                      mark_upper=str(upper_mark)), sort_keys=True))
            else:
                assert lower_mark > self.critical
                scale = (self.root_n*self.critical-1)/(reference[0]-1)
                assert 0 < scale < 1
                interior = [1+scale*(value-1) for value in reference]
                assert all(value > 0 for value in interior)
                available[sigma] = (interior, lower_mark, upper_mark, False)
        if not available:
            return
        for t, y, early, deficits, mark_loss in self.orbit(times):
            for sigma, (interior, mark_low, mark_high, saturated) in available.items():
                score = [sigma*value for value in y]
                lower = (sum(x*y for x, y in zip(score, interior))/self.n
                         if saturated else self.primal_lower(sigma, score, interior))
                upper = self.certify_dual(score, self.basis[-sigma])
                restricted = self.certify_dual(score, self.restricted_basis(sigma, early, y))
                assert lower < upper and upper-lower < arb("0.000001")
                assert lower < restricted
                reserve = self.critical*mark_loss
                residual = upper+reserve-deficits
                contrast = self.critical-1/self.root_n
                denom = 2*contrast*t-upper-reserve
                assert residual > 0
                dilution_upper = (
                    self.critical+contrast*residual/denom if denom > 0 else None
                )
                if dilution_upper is not None:
                    assert dilution_upper > mark_low
                finite_action = 3*(arb.pi()**2*self.tau**2*t/self.critical)**(arb(1)/3)
                print(json.dumps(dict(
                    kind="certified_critical_score", q=q, tau=tau_label, T=t, sigma=sigma,
                    saturated_square=saturated,
                    score_enclosure=str(lower.lower().union(upper.upper())),
                    prefix_shape_upper=str(restricted),
                    F=str(deficits), R=str(reserve),
                    action_leading_scale=str(finite_action), direct_mark_upper=str(mark_high),
                    dilution_mark_upper=str(dilution_upper) if dilution_upper is not None else None,
                ), sort_keys=True))


if __name__ == "__main__":
    ctx.prec = 256
    for q, square_root, floor, times in (
        (101, None, (1, 4), (7, 16, 32, 64)),
        (101, None, (1, 20), (7, 16, 32, 64)),
        (49, 7, (1, 4), (7, 16, 32, 64)),
        (121, 11, (1, 4), (7, 16, 32, 64)),
        (121, 11, (1, 1), (7,)),
        (173, None, (1, 20), (7, 16, 32)),
        (173, None, (1, 1000), (7, 16, 32, 64)),
        (401, None, (1, 20), (7, 16, 32)),
        (401, None, (1, 100), (7, 16, 32, 64)),
    ):
        signs = square_field_sign(square_root) if square_root else paley_sign(q)
        Shell(signs, arb(floor[0])/floor[1]).certify_case(
            q, f"{floor[0]}/{floor[1]}", times)
    for r in (7, 11):
        n = (r*r-1)//2
        # Solve W = (r-1)^2/n exactly at the boundary of the plus slice.
        num, den = (r-1)**2-n, n-1
        signs = square_field_sign(r)
        assert all(signs[j] == 1 for j in range(n//(r-1), n, n//(r-1)))
        Shell(signs, arb(num)/den).certify_case(
            r*r, f"{num}/{den}", (7, 16, 32, 64), saturated_root=r)
