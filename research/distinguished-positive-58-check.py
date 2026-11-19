"""One positive polynomial update from the exact distinguished fields."""
import json
from pathlib import Path
import runpy

from flint import arb, arb_poly, ctx

previous = runpy.run_path(str(Path(__file__).with_name("weighted-positive-57-check.py")))
centered = previous["centered"]
histogram = previous["histogram"]
warm = previous["warm"]
remainder = previous["nested"]["remainder"]
activation = previous["activation"]
SEED = previous["SEED"]

# Positive half of each symmetric boundary measure, including its zero atom.
SEED_FIELDS = (
    (arb(1), arb(0), arb(1)/2),
    (arb(1), arb(3)/4, arb(0), arb(1)/4),
    (arb(7)/4, arb(1)/2, arb(1)/2, arb(0), arb(1)/8),
)


def field_poly(weights):
    return arb_poly(list(reversed(weights[1:]))+list(weights))


def absolute_weight(poly, zero, shift):
    if shift == 0:
        return 2*sum(index*poly[zero+index] for index in range(1,zero+1))
    return sum(2*max(index,shift)*poly[zero+index] for index in range(1,zero+1)) + shift*poly[zero]


def difference_radius(modes, amplitudes):
    last = max(len(f) for f in SEED_FIELDS)-1
    positive = [arb(0)]*(last+1)
    for coefficient, weights in zip(amplitudes,SEED_FIELDS):
        for j,w in enumerate(weights):
            positive[j] += abs(coefficient).upper()*w
    base = field_poly(positive)
    power = arb_poly([1])
    radius = arb(0)
    degree = len(modes)-1
    for j in range(degree+1):
        for k in range(degree-j+1):
            if (j,k) == (0,2):
                radius += 2*abs(modes[0][2]-amplitudes[0]).upper()
            elif (j,k) == (1,1):
                for i,alpha in enumerate(amplitudes):
                    subtract = (amplitudes[i+1] if i+1 < len(amplitudes) else arb(0))
                    coefficient = abs(modes[1][1]*alpha-subtract).upper()
                    weights = SEED_FIELDS[i]
                    radius += coefficient*absolute_weight(field_poly(weights),len(weights)-1,1)
            else:
                radius += abs(modes[j][k]).upper()*absolute_weight(power,last*j,k)
        power *= base
    return radius.upper()


def euclidean_residual(t, b, lam, nu, tail, radius, err):
    coef, delta, a_max, a_var, m3, derivative_second = centered["expansion_constants"](t)
    v = (b*b+lam*lam+nu*nu)/2
    var_square = 2*v*v-b**4/8+nu**4/32
    scalar = tail + v*a_var
    cross = 6/(4*t)**2/(4*t).sqrt()
    model_squares = []
    for c,following in ((b,lam),(lam,nu)):
        offset = coef*c-following/2
        model_squares.append((delta*c)**2+4*abs(offset).upper()**2
                             +2*c*max(arb(0),offset.upper())*cross)
    linear = sum(model_squares)/2
    linear += derivative_second*nu**2/2
    quadratic = previous["cap_a2"](a_max,a_var)*var_square
    covariance = lam**2*model_squares[1].sqrt()*a_max/4
    cubic = m3*radius*(v*v+var_square).sqrt()/6
    return ((scalar*scalar+linear+quadratic+covariance).sqrt()+cubic+err).upper()


def trial(t, lambda_scale, nu_scale):
    center, order = arb(12), 8
    modes=histogram["centered_modes"](t,center,order)
    b=modes[0][2]
    coef, _, _, _, _, _ = centered["expansion_constants"](t)
    lam=2*b*coef*lambda_scale
    nu=2*lam*coef*nu_scale
    amplitudes=(b,arb(2).sqrt()*lam,2*nu)
    assert b>0 and lam>0 and nu>0
    radius = sum(abs(a).upper()*sum(2*i*w for i,w in enumerate(f)) for a,f in zip(amplitudes,SEED_FIELDS))
    total = (SEED+radius).upper()
    shift = difference_radius(modes,amplitudes)
    err = remainder(t,center,order,total)
    seed_err = remainder(t,center,order,SEED)
    tail = (sum(abs(v).upper()**2 for v in modes[0][4:])/2).sqrt()
    rms=euclidean_residual(t,b,lam,nu,tail,radius,err+seed_err)
    pair=2*total+shift
    ideal=t-pair*shift/4
    truncation=(2*activation(t,total)+err)*err/4
    product=ideal-truncation
    assert product>0 and 2*t.sqrt()>err
    distance=rms*pair/(4*(t.sqrt()+ideal.sqrt()))
    distance+=truncation/(ideal.sqrt()+product.sqrt())
    norm=(t.sqrt()+distance).upper()
    return (distance*norm/(1+norm*norm).sqrt()).upper(),product.lower()


def certify(first, last, divisions, cap, product_floor, lambda_scale, nu_scale):
    for k in range(first,last):
        mark, product = trial(warm.slab(k,divisions),lambda_scale,nu_scale)
        assert mark < cap and product > product_floor,(k,mark,product)
    print(json.dumps(dict(kind="distinguished_positive_start", slab_indices=[first,last],
                          divisions=divisions, mark_cap=str(cap), product_floor=str(product_floor),
                          lambda_scale=str(lambda_scale), nu_scale=str(nu_scale),
                          distinguished_fields=3, polynomial_center=12,
                          polynomial_degree=16),sort_keys=True))


if __name__ == "__main__":
    ctx.prec = 192
    certify(83*320, 31*1024, 5120, arb(1699)/100000, arb(149)/100,
            arb(19)/20, arb(3)/4)
    certify(5*1024, 83*64, 1024, arb(199)/10000, arb(92)/100,
            arb(19)/20, arb(3)/4)
    certify(19*256, 5*1024, 1024, arb(258)/10000, arb(52)/100,
            arb(9)/10, arb(13)/20)
