"""Independent exact endpoint algebra and small floating implementation checks.

No large FFT, stationary solve, or positivity certificate is run.
All output goes to stdout; use -B.
"""

from fractions import Fraction as F
import importlib.util
import json
from pathlib import Path


def emit(row):
    print(json.dumps(row, sort_keys=True), flush=True)


def exact_endpoint():
    n = 6
    kernel = [F(x, 6) for x in [-1, 3, -1, -3, -1, 3]]

    def K(x):
        return [sum(kernel[(i-j) % n]*x[j] for j in range(n)) for i in range(n)]

    def P(side, x):
        mean = sum(x)/n
        return [(a-mean+side*b)/2 for a, b in zip(x, K(x))]

    cosine = list(map(F, [1, F(1, 2), F(-1, 2), -1, F(-1, 2), F(1, 2)]))
    # Rational activations are arbitrary and even here; endpoint algebra
    # only needs v_{t+1}=K phi_t. This is not a fixed-weight orbit claim.
    phi = [[2+F(t+1, 10)*cosine[i]+F(t+2, 30)*(-1)**i
            for i in range(n)] for t in range(6)]
    vec = [[F(0)]*n]+[K(x) for x in phi]
    mu = [sum(x)/(2*n) for x in phi]
    for T in [1, 2, 5]:
        mean = sum(mu[1:T+1])/T
        phi_sum = [sum(phi[t][i]+phi[t-1][i] for t in range(1, T+1))
                   for i in range(n)]
        old_v_sum = [sum(vec[t][i]+vec[t-1][i] for t in range(1, T+1))
                     for i in range(n)]
        terminal = [vec[T][i]+vec[T+1][i]-vec[1][i] for i in range(n)]
        assert [x+y for x, y in zip(old_v_sum, terminal)] == [
            sum(vec[t][i]+vec[t+1][i] for t in range(1, T+1)) for i in range(n)]
        for side in [1, -1]:
            raw = [[(x+side*y)/2 for x, y in zip(phi[t], vec[t])]
                   for t in range(1, T+1)]
            assert all(x > 0 for row in raw for x in row)
            projected = [P(side, row) for row in raw]
            direct = [mean+sum(row[i] for row in projected)/T for i in range(n)]
            endpoint = [(mu[T]-mu[0])/(2*T)+(x+side*(y+z))/(4*T)
                        for x, y, z in zip(phi_sum, old_v_sum, terminal)]
            assert direct == endpoint
            positive_average = [sum(row[i] for row in raw)/T for i in range(n)]
            drift = [vec[T+1][i]-vec[1][i] for i in range(n)]
            correction = [side*x/(2*T) for x in P(-side, drift)]
            assert direct == [x+y for x, y in zip(positive_average, correction)]
            negative_square = sum(max(-x, F(0))**2 for x in direct)
            assert negative_square <= sum(x*x for x in correction)
            opposite_average = [
                sum((phi[t][i]-side*vec[t][i])/2 for t in range(1, T+1))/T
                for i in range(n)]
            lower_product = min((phi[t][i]**2-vec[t][i]**2)/4
                                for t in range(1, T+1) for i in range(n))
            assert lower_product > 0
            normalized = [x/mean for x in direct]
            U = [x/mean for x in positive_average]
            opposite_U = [x/mean for x in opposite_average]
            r = lower_product/mean**2
            assert all(x*y >= r for x, y in zip(U, opposite_U))
            h_squared = sum((x/mean)**2 for x in correction)/n
            for kappa in [F(1, 100), F(1, 2), F(2)]:
                deficit_mean = sum(max(2*kappa-x, F(0))
                                   for x in normalized[1:])/n
                assert max(deficit_mean-kappa**2/r, F(0))**2 <= h_squared
            emit({"kind": "exact_actual_p13_endpoint_algebra", "T": T, "side": side,
                  "one_FFT_endpoint_equals_direct_projection": True,
                  "positive_average_plus_terminal_projection_identity": True,
                  "negative_part_endpoint_bound_checked": True,
                  "normalized_clipped_deficit_bound_checked": True,
                  "scope": "arbitrary rational activations; no fixed-weight or positivity claim"})


def small_implementation():
    path = Path(__file__).parent/"endpoint-stress-36.py"
    spec = importlib.util.spec_from_file_location("paley_endpoint_stress36", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    for prime, T in [(13, 1), (13, 8), (17, 8)]:
        module.run(prime, T, .05, .001, direct=True)


if __name__ == "__main__":
    exact_endpoint()
    small_implementation()
    emit({"kind": "all_checks_passed", "large_FFT_run": False})
