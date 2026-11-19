"""Direct theta bounds from preserved marks and an averaged Picard budget.

No optimizer or new large transform is run. Derived prime bounds depend on
the accepted exact-input positivity certificates of round 34. The square
obstruction uses its exact saved Fourier mark and the exact square theta.
"""

from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path
import sys

from flint import arb, ctx

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent))
from theta import paley_sign


def emit(row):
    print(json.dumps(row, sort_keys=True), flush=True)


def ball(value):
    value = Fraction(value)
    return arb(value.numerator) / value.denominator


def small_kernel():
    n = 6
    signs = [int(s) for s in paley_sign(13)]
    cosine = list(map(Fraction, [1, Fraction(1, 2), Fraction(-1, 2),
                                 -1, Fraction(-1, 2), Fraction(1, 2)]))
    first = [sum(signs[j]*cosine[i*j % n] for j in range(n))/n
             for i in range(n)]
    K = [[first[(i-j) % n] for j in range(n)] for i in range(n)]

    def mv(matrix, vector):
        return [sum((ball(a)*b if isinstance(a, Fraction) and isinstance(b, arb)
                     else a*b) for a, b in zip(row, vector)) for row in matrix]

    def project(vector, side):
        mean = sum(vector)/n
        return [(x-mean+side*y)/2 for x, y in zip(vector, mv(K, vector))]

    for j in range(n):
        vector = [Fraction(i == j) for i in range(n)]
        assert mv(K, mv(K, vector)) == [x-Fraction(1, n) for x in vector]
        assert project(project(vector, 1), -1) == [0]*n
    previous = [Fraction(3+i, 2) for i in range(n)]
    current = [Fraction(7+i, 3) for i in range(n)]
    v, next_v = mv(K, previous), mv(K, current)
    mu, old_mu = sum(current)/(2*n), sum(previous)/(2*n)
    plus = [(p+x)/2 for p, x in zip(current, v)]
    minus = [(p-x)/2 for p, x in zip(current, v)]
    X = [[mu+y for y in project(row, side)]
         for row, side in [(plus, 1), (minus, -1)]]
    assert [x-y for x, y in zip(*X)] == [(x+y)/2 for x, y in zip(v, next_v)]
    assert [x+y for x, y in zip(*X)] == [
        mu-old_mu+(x+y)/2 for x, y in zip(current, previous)]
    # An arbitrary exact activation pair also checks the energy algebra.
    activation = [abs(x)+2 for x in v]
    weights = [(p*p-x*x)/4 for p, x in zip(activation, v)]
    assert all(w > 0 for w in weights)
    next_v = mv(K, activation)
    energy_difference = sum(x*x for x in next_v)-sum(x*x for x in v)
    assert energy_difference == 4*sum(weights)-sum(activation)**2/n
    emit(dict(kind="exact_actual_projector_and_mark_identities", q=13,
              counting_norms=True, complementary_projections=True,
              exact_vector_mark_sum_and_difference=True,
              exact_energy_algebra=True))
    return K, mv, project


def budget_checks(K, mv, project):
    n, tau = len(K), Fraction(1, 20)
    weights = [arb(1)]+[ball(tau)/n]*(n-1)
    W = sum(weights)
    v = [arb(0)]*n
    means, energies, phis, vectors = [], [arb(0)], [], [v]
    for t in range(17):
        phi = [(x*x+4*w).sqrt() for x, w in zip(v, weights)]
        mu = sum(phi)/(2*n)
        next_v = mv([[ball(x) for x in row] for row in K], phi)
        E, next_E = sum(x*x for x in v), sum(x*x for x in next_v)
        assert (next_E-E-4*W+4*n*mu*mu).contains(0)
        means.append(mu)
        phis.append(phi)
        energies.append(next_E)
        vectors.append(next_v)
        v = next_v
    for T in (1, 2, 4, 8, 16):
        M = sum(means[1:T+1])/T
        gap = W+energies[1]/(4*T)-n*M*M
        assert gap > 0
        X = [[M]*n for _ in (1, -1)]
        for t in range(1, T+1):
            for i, side in enumerate((1, -1)):
                raw = [(p+side*x)/2 for p, x in zip(phis[t], vectors[t])]
                projected = project(raw, side)
                X[i] = [x+y/T for x, y in zip(X[i], projected)]
        expected_difference = sum((vectors[t][0]+vectors[t+1][0])/2
                                  for t in range(1, T+1))/T
        expected_sum = ((means[T]-means[0])/T
                        +sum((phis[t][0]+phis[t-1][0])/2
                             for t in range(1, T+1))/T)
        assert (X[0][0]-X[1][0]-expected_difference).contains(0)
        assert (X[0][0]+X[1][0]-expected_sum).contains(0)
        emit(dict(kind="validated_actual_picard_mean_budget", q=13,
                  tau=str(tau), T=T, precision_bits=ctx.prec,
                  n_mean_squared_interval=str(n*M*M),
                  budget_upper=str((W+energies[1]/(4*T)).upper()),
                  positive_budget_margin_lower=str(gap.lower()),
                  mark_sum_difference_checked=True,
                  scope="finite small orbit normalization; no asymptotic positivity"))


def parent_mark_certificates():
    certificates = [json.loads(line) for line in
                    (ROOT/"astra-conic-primal-34-replay224.jsonl").read_text().splitlines()]
    for cert in sorted(certificates, key=lambda r: (r["order"], r["steps"])):
        path = ROOT/cert["exact_input"]
        raw = gzip.decompress(path.read_bytes())
        digest = hashlib.sha256(raw).hexdigest()
        assert digest == cert["uncompressed_sha256"]
        data = json.loads(raw)
        n = (data["order"]-1)//2
        p = Fraction(sum(data["plus"]), data["scale"])
        q = Fraction(sum(data["minus"]), data["scale"])
        P, Q = ball(p), ball(q)
        if cert["kind"] == "arb_mark_preserving_conic_primal":
            assert cert["strict_floor_proved"] and cert["exact_mean_and_sector_proved"]
            lower, upper = P/arb(n).sqrt(), arb(n).sqrt()/Q
            assert lower < upper
            W = 1+ball(Fraction(data["tau"]))*(n-1)/n
            alpha = P*Q/n
            D = arb(cert["d_upper"])
            trial_log = (P/Q).log()/2
            radius = 2*(D/(4*(alpha/W).sqrt())).sqrt().asinh()
            emit(dict(kind="derived_interval_theta_from_preserved_marks",
                      q=data["order"], steps=data["steps"],
                      theta_plus_normalized_lower=str(lower.lower()),
                      theta_plus_normalized_upper=str(upper.upper()),
                      conic_mark_ratio_log_interval=str(trial_log),
                      conic_gap_mark_error_upper=str(radius.upper()),
                      parent_exact_input=path.name,
                      parent_uncompressed_sha256=digest,
                      proof_dependency="accepted Arb224 positive repair and exact root preservation",
                      scope="finite theta bracket; no new large positivity transform"))
        else:
            assert cert["kind"] == "arb_repair_rejected"
            r = data["square_root"]
            assert data["order"] == r*r
            exact_maximum = Fraction(r+1, 2)
            assert q > exact_maximum
            emit(dict(kind="exact_square_all_root_preserving_repairs_impossible",
                      q=data["order"], steps=data["steps"],
                      exact_minus_mark=str(q), exact_maximum_minus_mark=str(exact_maximum),
                      exact_excess=str(q-exact_maximum),
                      excess_interval=str(ball(q-exact_maximum)),
                      parent_exact_input=path.name,
                      parent_uncompressed_sha256=digest,
                      scope="all root-preserving nonnegative minus repairs of this input; not conic infeasibility"))


def main():
    ctx.prec = 224
    K, mv, project = small_kernel()
    budget_checks(K, mv, project)
    parent_mark_certificates()
    emit(dict(kind="all_checks_passed",
              arithmetic="exact rational Paley projector; Arb224; accepted exact Fourier inputs",
              ETH26_solved=False, prime_uniform_positive_repair=False))


if __name__ == "__main__":
    main()
