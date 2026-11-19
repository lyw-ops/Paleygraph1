"""Minimal independent checks for the regularization and averaged-mark bridge.

Exact rational stationary data at p13; Arb zero-Picard prefixes at p13/q25;
and an exact marked-value obstruction for one saved square proposal.
Only stdout is written. No stationary optimizer or large Fourier solve.
"""

from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from flint import acb, arb, ctx
from square_control import square_field_sign
from theta import paley_sign


def emit(row):
    print(json.dumps(row, sort_keys=True), flush=True)


def dot(x, y):
    return sum((a*b for a, b in zip(x, y)), F(0))


def mv(A, x):
    return [dot(row, x) for row in A]


def solve(A, b):
    n = len(b)
    rows = [list(a)+[z] for a, z in zip(A, b)]
    for i in range(n):
        pivot = next(j for j in range(i, n) if rows[j][i])
        rows[i], rows[pivot] = rows[pivot], rows[i]
        scale = rows[i][i]
        rows[i] = [x/scale for x in rows[i]]
        for j in range(n):
            if j != i:
                scale = rows[j][i]
                rows[j] = [x-scale*y for x, y in zip(rows[j], rows[i])]
    return [row[-1] for row in rows]


def rational_source_checks():
    n, tau, W, a2 = 6, F(30, 19), F(44, 19), F(22, 57)
    c, rho = tau/n, tau/W
    u = [F(3, 2), F(5, 4), F(3, 4), F(1, 2), F(3, 4), F(5, 4)]
    h = [x-1 for x in u]
    v = [(n/W if i == 0 else rho)/x for i, x in enumerate(u)]
    assert sum(u) == sum(v) == n
    k = [F(x, 6) for x in [-1, 3, -1, -3, -1, 3]]
    P = [[(F(i == j)-F(1, n)+k[(i-j) % n])/2
          for j in range(n)] for i in range(n)]
    e = [row[0] for row in P]
    assert all(x > 0 for x in u+v)
    assert mv(P, h) == h and mv(P, [x-1 for x in v]) == [0]*n
    d = [rho/x for x in u]
    T = [[sum(P[i][k]*d[k]*P[k][j] for k in range(n))
          for j in range(n)] for i in range(n)]
    S = [[sum(P[i][k]*v[k]*P[k][j] for k in range(n))
          for j in range(n)] for i in range(n)]
    Th = mv(T, h)
    assert Th == [F(14, 11)*x for x in e]
    assert mv(S, h) == [F(21, 11)*x for x in e]
    Q = a2*dot(h, Th)
    w = [F(1)]+[c]*(n-1)
    for delta in [F(1), F(1, 4), F(1, 16), F(1, 64)]:
        matrix = [[T[i][j]+delta*F(i == j) for j in range(n)] for i in range(n)]
        hd = solve(matrix, Th)
        decrement = Q-a2*dot(Th, hd)
        error = [x-y for x, y in zip(h, hd)]
        energy_error = a2*dot(error, mv(T, error))
        mean_l1 = sum(abs(x) for x in error)/n
        assert energy_error <= decrement
        assert mean_l1**2 <= decrement/tau
        assert delta*a2*dot(hd, hd) <= Q
        assert error[0] == decrement/(a2*F(14, 11))
        # One-sided exact source-dependent regularization.
        wd = [x+delta*a2*y for x, y in zip(w, u)]
        vd = [(x+delta)/(1+delta) for x in v]
        assert sum(wd) == (1+delta)*W
        assert all(a2*(1+delta)*x*y == z for x, y, z in zip(u, vd, wd))
        # Symmetric regularization leaves the physical centered rows unchanged.
        ws = [x+delta*a2*(y+z)+delta**2*a2 for x, y, z in zip(w, u, v)]
        assert sum(ws) == (1+delta)**2*W
        assert all(a2*(x+delta)*(y+delta) == z for x, y, z in zip(u, v, ws))
        shifted_source = [(x+delta*y)/(1+delta) for x, y in zip(mv(S, h), h)]
        shifted_operator = [[(S[i][j]+delta*P[i][j])/(1+delta)
                             for j in range(n)] for i in range(n)]
        assert mv(shifted_operator, h) == shifted_source
        emit({"kind": "exact_regularized_source_check", "q": 13, "tau": str(tau),
              "delta": str(delta), "Q": str(Q),
              "source_inverse_decrement": str(decrement),
              "normalized_L1_error": str(mean_l1),
              "energy_error": str(energy_error),
              "L1_bound_squared": str(decrement/tau),
              "one_sided_and_symmetric_pair_identities": True,
              "shifted_inverse_retains_unknown_source_term": True})


def K(sign, x):
    n = len(sign)
    transformed = acb.dft(x)
    out = acb.dft([int(s)*z for s, z in zip(sign, transformed)])
    assert all(z.imag.contains(0) for z in out)
    return [z.real/n for z in out]


def project(sign, side, x):
    mean = sum(x)/len(x)
    return [(z-mean+side*y)/2 for z, y in zip(x, K(sign, x))]


def averaged_checks(q, root):
    sign = square_field_sign(root) if root else paley_sign(q)
    n = len(sign); tau = arb(1)/20
    w = [arb(1)]+[tau/n]*(n-1)
    W = sum(w)
    vec = [[arb(0)]*n]
    phi, mu, energy = [], [], []
    for t in range(10):
        energy.append(sum(x*x for x in vec[t]))
        phi.append([(x*x+4*y).sqrt() for x, y in zip(vec[t], w)])
        mu.append(sum(phi[t])/(2*n))
        vec.append(K(sign, phi[t]))
    for T in [2, 8]:
        mean = sum(mu[1:T+1])/T
        rows = {}
        for side in [1, -1]:
            pieces = []
            for t in range(1, T+1):
                raw = [(x+side*y)/2 for x, y in zip(phi[t], vec[t])]
                pieces.append(project(sign, side, raw))
            rows[side] = [mean+sum(x[i] for x in pieces)/T for i in range(n)]
            assert (sum(rows[side])/n-mean).contains(0)
        differences = []
        for t in range(1, T+1):
            differences.append(energy[t+1]-energy[t]-4*W+4*n*mu[t]**2)
        assert all(x.contains(0) for x in differences)
        jensen_slack = sum(mu[t]**2 for t in range(1,T+1))/T-mean**2
        assert jensen_slack.lower() > 0
        budget = W+(energy[1]-energy[T+1])/(4*T)
        assert (budget-n*sum(mu[t]**2 for t in range(1,T+1))/T).contains(0)
        assert (n*mean**2-budget).upper() < 0
        difference = sum((vec[t][0]+vec[t+1][0])/2 for t in range(1,T+1))/T
        total = sum(mu[t]-mu[t-1]+(phi[t][0]+phi[t-1][0])/2
                    for t in range(1,T+1))/T
        assert (rows[1][0]-rows[-1][0]-difference).contains(0)
        assert (rows[1][0]+rows[-1][0]-total).contains(0)
        emit({"kind": "arb_actual_zero_Picard_average_check", "q": q, "T": T,
              "tau": "1/20", "mean_scaled_interval": str(mean*arb(n).sqrt()),
              "plus_mark_interval": str(rows[1][0]),
              "minus_mark_interval": str(rows[-1][0]),
              "energy_budget_upper": str(budget.upper()),
              "energy_and_mark_identities_enclose_zero": True,
              "scope": "finite normalization checks; no completion positivity asserted"})


def square_mark_obstruction():
    path = Path(__file__).parent/"astra-conic-primal-34-q151321-t48-tau1_20-k1_1000-input.json.gz"
    data = gzip.decompress(path.read_bytes())
    payload = json.loads(data)
    root, q, n = 389, 151321, 75660
    assert payload["order"] == q and payload["square_root"] == root and payload["steps"] == 48
    sign = square_field_sign(root)
    coeff, scale = payload["minus"], payload["scale"]
    assert len(coeff) == n and coeff[0] == scale and coeff[1:] == coeff[:0:-1]
    assert all(x == 0 for j, x in enumerate(coeff) if j and sign[j] != -1)
    value = F(sum(coeff), scale)
    theta_minus = F(root+1, 2)
    assert theta_minus == 195 and value > theta_minus
    emit({"kind": "exact_fixed_mark_completion_obstruction", "q": q,
          "input_file": path.name, "uncompressed_input_sha256": hashlib.sha256(data).hexdigest(),
          "input_minus_mark": str(value), "theta_minus": str(theta_minus),
          "strict_mark_excess": str(value-theta_minus),
          "mean_one_and_exact_minus_support_checked": True,
          "no_nonnegative_mean_and_mark_preserving_completion": True,
          "scope": "this one saved affine input; not general conic infeasibility"})


def main():
    ctx.prec = 192
    rational_source_checks()
    averaged_checks(13, None)
    averaged_checks(25, 5)
    square_mark_obstruction()
    emit({"kind": "all_checks_passed", "arithmetic": "Fraction exact and Arb192"})


if __name__ == "__main__":
    main()
