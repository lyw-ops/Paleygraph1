"""Check the cold Picard collision identity on actual critical probabilities."""
import json
from pathlib import Path
import runpy
import sys

from flint import arb, arb_mat, ctx

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from square_control import square_field_sign


def dot(x, y):
    return sum(a*b for a, b in zip(x, y))


def check(order, sigma, times):
    if order == 101:
        n = 50
        residues = {i*i % order for i in range(1, order)}
        signs = [0] + [1 if (1-pow(4, k, order)) % order in residues else -1
                       for k in range(1, n)]
    else:
        signs = list(map(int, square_field_sign(7)))
        n = len(signs)
    root = arb(n).sqrt()
    cos = [(arb(2*i)/n).cos_pi() for i in range(n)]
    col = [sum(s*cos[i*j % n] for j, s in enumerate(signs))/n for i in range(n)]
    kernel = arb_mat([[col[(i-j) % n] for j in range(n)] for i in range(n)])

    def apply(x):
        return list(kernel*arb_mat(n, 1, x))

    if order == 101:
        coeffs = runpy.run_path(str(ROOT/'research/astra-rooted-43-check.py'))['PAIR'][sigma]
        support = [i for i in range(1, n//2+1) if signs[i] == sigma]
        assert len(support) == len(coeffs)
        row = [1+sum(a*cos[i*k % n] for a, k in zip(coeffs, support))/10**12
               for i in range(n)]
        assert min(z.lower() for z in row) > 0
    else:
        assert n == 24 and all(signs[i] == 1 for i in range(4, n, 4))
        row = [arb(6 if i % 6 == 0 else 0) for i in range(n)]
    alpha = (1+(1-arb(1)/n)/4).sqrt()
    mix = (alpha*root-1)/(row[0]-1)
    assert 0 < mix < 1
    mu = [(1+mix*(y-1))/n for y in row]
    assert all(y > 0 for y in mu)
    assert (sum(mu)-1).contains(0) and (root*mu[0]-alpha).contains(0)
    d = [root*y-1/root for y in mu]
    assert all((y-sigma*x).contains(0) for x, y in zip(d, apply(d)))
    collision = dot(d, d)
    v = [arb(0)]*n
    B = arb(0)
    H = arb(0)
    mean_loss = arb(0)
    for t in range(1, max(times)+1):
        phi = [abs(z) for z in v]
        phi[0] = (v[0]*v[0]+4).sqrt()
        b = phi[0]-abs(v[0])
        B += 2-b
        g = sum(phi)/(2*root)
        mean_loss += (1-g)**2
        H += root*sum(y*(abs(z)-sigma*z) for y, z in zip(mu, v))
        v = apply(phi)
        if t in times:
            Kv = apply(v)
            C = dot(v, Kv)
            proj = [(z+sigma*w)/2 for z, w in zip(v, Kv)]  # v has zero mean
            residual = [x-sigma*z for x, z in zip(d, proj)]
            distance = dot(residual, residual)
            bound = 2*((2*t-B)*alpha-2*t+mean_loss)-sigma*C/2
            projected_energy = dot(proj, proj)
            projection_score = sigma*dot(d, proj)
            assert projected_energy > 0 and projection_score > 0
            directional = projection_score**2/projected_energy
            assert directional > bound+2*H and collision > directional
            defect = collision-bound-distance-2*H
            assert defect.contains(0) and defect.rad() < arb('1e-55')
            assert H > 0 and distance > 0 and bound > 0
            print(json.dumps(dict(order=order, sigma=sigma, tau_of_shell='1/4',
                                  tau_of_orbit=0, T=t, precision=ctx.prec,
                                  collision_excess=str(collision), root=str(alpha),
                                  finite_lower_bound=str(bound), directional_energy=str(directional),
                                  squared_distance=str(distance),
                                  wrong_sign_reserve=str(H), identity_error=str(defect)),
                             sort_keys=True))


if __name__ == '__main__':
    ctx.prec = 512
    check(101, -1, [3, 7, 13])
    check(49, 1, [3, 7, 8])
