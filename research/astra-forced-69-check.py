"""Outward bounds on the true larger-sign forced barrier at p=13, t=3."""
import json
from flint import arb, ctx


def main():
    ctx.prec = 192
    n, time = 6, 3
    root = arb(n).sqrt()
    squares = {j * j % 13 for j in range(1, 13)}
    generator = 4
    signs = [0] + [1 if (1 - pow(generator, j, 13)) % 13 in squares else -1
                   for j in range(1, n)]
    assert signs == [0, 1, -1, -1, -1, 1]
    cosines = [arb(x) / 2 for x in [2, 1, -1, -2, -1, 1]]
    col = [sum(s * cosines[k*j % n] for j, s in enumerate(signs)) / n for k in range(n)]
    state = [arb(0)] * n
    for _ in range(time):
        active = [abs(v) for v in state]
        active[0] = (4 + state[0]**2).sqrt()
        state = [sum(col[(i-j) % n] * active[j] for j in range(n)) for i in range(n)]
    score = [-root * v for v in state]
    energy = sum(v**2 for v in state)
    # The symmetric minus rows have coordinates (a,b,c,d,c,b).
    # a=3-(3b+c)/2, d=3-(b+3c)/2.  The known primary vertex has b=c=0.
    slope_b = (-3*score[0] + 4*score[1] - score[3]) / (2*n)
    slope_c = (-score[0] + 4*score[2] - 3*score[3]) / (2*n)
    charge_star = (score[0]+score[3])/2 - energy/4
    h = arb(1) / (2 * n**(2*n) * 4 * (1 + 4*arb(n*time).sqrt()))
    for k in [1, 2]:
        x, z = arb('0.55 +/- 0.05'), arb('1.65 +/- 0.15')  # b/h, c/h
        for _ in range(4):
            a = 3 - h*(3*x+z)/2
            d = 3 - h*(x+3*z)/2
            assert a > 0 and d > 0
            fx = 1/(3*(3/(2*root) + k*h*slope_b + h*(3/a + 1/d)/12))
            fz = 1/(3*(1/(2*root) + k*h*slope_c + h*(1/a + 3/d)/12))
            # A strict inclusion in the first box yields existence by Brouwer.
            if _ == 0:
                assert x.contains_interior(fx) and z.contains_interior(fz)
            x, z = fx, fz
        primary = (3*x+z)/(2*root)
        charge = charge_star + h*(slope_b*x+slope_c*z)
        assert abs(primary - arb(2)/3) < arb('1e-9')
        assert abs(charge-charge_star) < arb('1e-9')
        print(json.dumps(dict(prime=13, n=n, time=time, side='minus', tilt=k,
                              h=str(h), scaled_primary_loss=str(primary),
                              charge_minus_primary_face_charge=str(h*(slope_b*x+slope_c*z)),
                              primary_face_charge=str(charge_star)), sort_keys=True))


if __name__ == '__main__':
    main()
