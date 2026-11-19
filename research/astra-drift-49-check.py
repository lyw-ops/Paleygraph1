"""Verify a common antipodal coupling on actual cold histories and optimal rows."""
import importlib.util
import json
from pathlib import Path
import sys

import numpy as np
from scipy.optimize import linear_sum_assignment
from flint import arb, ctx

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root))
from theta import paley_sign
from square_control import square_field_sign

spec = importlib.util.spec_from_file_location("endpoint", root / "research/endpoint-direction-45-check.py")
endpoint = importlib.util.module_from_spec(spec)
spec.loader.exec_module(endpoint)
ctx.prec = 224


def rms(values):
    return (sum(x*x for x in values)/len(values)).sqrt()


def verify(q, depth, square_root=0):
    if square_root:
        sign = square_field_sign(square_root)
        n = len(sign)
        side = 1
        rho = [arb(square_root-1 if i % (square_root-1) == 0 else 0) for i in range(n)]
    else:
        sign = paley_sign(q)
        n = len(sign)
        pairs, error = endpoint.solve_prime_pair(sign)
        assert error is None
        side = 1 if pairs[1][0] > pairs[-1][0] else -1
        assert pairs[side][0] > pairs[-side][0]
        rho = [arb(n).sqrt()*a for a in pairs[side]]
    state = [arb(0)]*n
    histories = []
    A = H = B = arb(0)
    for _ in range(depth):
        signal = [abs(x) for x in state]
        signal[0] = (4+state[0]**2).sqrt()
        B += 2-signal[0]+abs(state[0])
        A += (1-sum(signal)/(2*arb(n).sqrt()))**2
        H += sum(x*(abs(v)-side*v) for x,v in zip(rho,state))/arb(n).sqrt()
        state = endpoint.apply_multiplier(signal,sign)
        histories.append([arb(n).sqrt()*x for x in state])
    approx = np.array([[float(x) for x in row] for row in histories]).T
    cost = np.max(abs(approx[:,None,:]+approx[None,:,:]),axis=2)**2
    # Round only the proposed assignment costs to remove platform-sensitive ties.
    _, permutation = linear_sum_assignment(np.rint(1e8*cost).astype(np.int64))
    perm = [int(j) for j in permutation]
    assert sorted(perm) == list(range(n))
    squared = [max(abs(row[i]+row[j]).upper() for row in histories)**2 for i,j in enumerate(perm)]
    error_upper = (sum(squared)/n).sqrt().upper()
    for start in (0, depth//2):
        diff = [side*(histories[-1][i]-(histories[start-1][i] if start else 0)) for i in range(n)]
        drift = sum(x*z for x,z in zip(rho,diff))/n
        anti = sum((rho[i]-rho[j])*(diff[i]-diff[j]) for i,j in enumerate(perm))/(4*n)
        even = sum((rho[i]+rho[j])*(diff[i]+diff[j]) for i,j in enumerate(perm))/(4*n)
        assert (drift-anti-even).contains(0)
        imbalance = rms([rho[i]-rho[j] for i,j in enumerate(perm)])
        norm = rms(rho)
        bound = imbalance*rms(diff)/2 + (1 if start else arb(1)/2)*norm*error_upper
        assert abs(drift) < bound
        # Every exactly endpoint-weight-preserving permutation must pay this much
        # RMS antipodal error in the full history, by weighted Cauchy-Schwarz.
        min_preserving = abs(drift)/(norm*(1 if start else arb(1)/2))
        active = [i for i,x in enumerate(rho) if x > 0]
        inactive = [i for i,x in enumerate(rho) if x == 0]
        assert len(active)+len(inactive) == n
        # A partition-preserving coupling retains the conditional drift of each cell.
        conditional_sq = sum(sum(diff[i] for i in indices)**2/len(indices) for indices in
                             (active,inactive) if indices)/n
        support_lower = conditional_sq.sqrt()/(1 if start else arb(1)/2)
        mass = arb(len(active))/n
        sd = (mass*(1-mass)).sqrt()
        # This lower bound holds for every coupling below the displayed cost.
        gap = abs(2*sum(diff[i] for i in active)/n) - sd*(2 if start else 1)*error_upper
        crossing_lower = (max(arb(0), gap.lower())/rms(diff))**2
        inverse_certificate = {}
        if not start:
            alpha = rho[0]/arb(n).sqrt()
            energy_root = rms(diff)
            assert (drift+alpha*B-energy_root**2/4-2*depth*(alpha-1)-A-H).contains(0)
            terminal_error = rms([diff[i]+diff[j] for i,j in enumerate(perm)])
            inverse_slack = (imbalance**2+2*norm*terminal_error-8*depth*(alpha-1)
                             -(imbalance-energy_root)**2-4*(A+H)+4*alpha*B)
            assert inverse_slack > 0
            inverse_certificate["inverse_inequality_slack"] = str(inverse_slack)
            assert support_lower > error_upper and crossing_lower > 0
        print(json.dumps(dict(**inverse_certificate, order=q, sign=side, depth=depth, start=start,
                              mark=str(rho[0]/arb(n).sqrt()), history_rms_upper=str(error_upper),
                              actual_secant=str(drift), odd_part=str(anti), even_error=str(even),
                              density_rms=str(norm), imbalance_rms=str(imbalance),
                              secant_abs_cap=str(bound), preserving_rms_lower=str(min_preserving), support_preserving_lower=str(support_lower), crossing_probability_lower=str(crossing_lower)),
                         sort_keys=True))


if __name__ == "__main__":
    for order, root_value in [(101,0), (173,0), (121,11), (961,31)]:
        verify(order,6,root_value)
