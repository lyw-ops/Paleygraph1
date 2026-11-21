"""Price the seed-Laurent resummation on the genuine two-height envelope."""

from contextlib import redirect_stdout
from math import comb
from pathlib import Path
import io
import json
import runpy


source = Path(__file__).with_name("cold-combined-height-130-check.py")
with redirect_stdout(io.StringIO()):
    inherited = runpy.run_path(str(source))

arb, acb = inherited["arb"], inherited["acb"]
arb_poly = inherited["arb_poly"]
t, price = inherited["t"], inherited["price"]
radius, eps = inherited["N"], inherited["eps"]
slope = inherited["slope"]
symmetric = inherited["symmetric"]
fields = inherited["fields"]
a, b, c, d, z, w, v = inherited["pars"]
center = [arb(0)]*(radius+1)
center[0], center[1], center[2], center[3] = a+b, 3*b/2, a, 3*b/2
for polynomial, coefficient, offset in (
    (fields["kern"]["F"], c, 4),
    (fields["kern"]["G"], d, 5),
    (fields["old"]["R"], z, 2),
    (fields["field"], w+v, 4),
):
    for k in range(offset+1):
        center[k] += coefficient*polynomial[offset+k]*(2 if k else 1)

cut_order = 14
max_degree = 2*cut_order-1
cut_weight = 150
old_tail_price = arb("0.0000407")
seed = arb("2.8284275", arb("0.0000005"))
assert arb("2.828427")**2 < 8 < 8+arb(4)/10**30 < arb("2.828428")**2
assert all(k <= price(k) <= 2*k for k in range(cut_weight+len(inherited["prices"])))

coefficients = [[acb(0)]*(max_degree-j+1) for j in range(max_degree+1)]
for l in range(cut_order):
    m = 2*l+1
    leading = (-1)**l * arb(comb(2*l,l))/(4**l*(2*t.sqrt())**m)
    for j in range(1,m+1):
        factor = leading*comb(m,j)*(seed/2)**(m-j)
        for k in range((m-j)%2,m-j+1,2):
            coefficients[j][k] += factor*comb(m-j,(m-j-k)//2)


def folded(poly, zero_index, k):
    return poly[zero_index+k]*(2 if k else 1)


def tilted(row):
    return sum(x*(arb(k)/5).cosh() for k,x in enumerate(row))


def price_rate(row):
    mass = sum(row)
    moment = sum(x*price(k) for k,x in enumerate(row))
    rates = [mass+moment/slope, mass+moment/5000]
    for k in range(1,len(row)+len(inherited["prices"])):
        shift = sum(x*(price(k+j)+price(k-j))/2 for j,x in enumerate(row))
        rates.append(((k-1)*moment+shift)/price(k))
    return max(rate.upper() for rate in rates)


trial = [1000000,919335,545800,295066,179923,106604,
         64267,38861,23568,14244,8476,4947]


def lower_standard_cone(row):
    size = len(trial)
    image = [arb(0)]*(size+1)
    for k,count in enumerate(trial,1):
        for j,mass in enumerate(row):
            if 1 <= j <= size:
                image[j] += (k-1)*count*mass
            for shift in (k+j,abs(k-j)):
                if 1 <= shift <= size:
                    image[shift] += count*mass/2
    return min((entry/count).lower() for entry,count in zip(image[1:],trial))


h = inherited["h"]
for depth in (601,602):
    core, norm = inherited["residual"](h)
    beta_row = [value+folded(core,radius,k) for k,value in enumerate(center)]
    beta = symmetric(beta_row,radius)
    beta_tilt = tilted(beta_row)
    powers = arb_poly([1])
    parts = [[arb(0)]*(cut_weight+1) for _ in range(2)]
    losses = [arb(0),arb(0)]
    for j in range(1,max_degree+1):
        powers *= beta
        weights = [abs(value).upper()*(2 if k else 1)
                   for k,value in enumerate(coefficients[j])]
        width = len(weights)-1
        poly = symmetric(weights,width)*powers
        zero_index = width+j*radius
        row = [folded(poly,zero_index,k) for k in range(cut_weight+1)]
        tail = sum(folded(poly,zero_index,k)*(arb(k)/5).cosh()
                   for k in range(cut_weight+1,zero_index+1))
        delta = tilted(weights)*j*eps*(beta_tilt+eps)**(j-1)
        index = int(j>1)
        parts[index] = [x+y for x,y in zip(parts[index],row)]
        losses[index] += tail+delta
    whole = [x+y for x,y in zip(*parts)]
    linear = price_rate(parts[0])+10*losses[0]+old_tail_price
    nonlinear = price_rate(parts[1])+10*losses[1]+old_tail_price
    total = price_rate(whole)+10*sum(losses)+old_tail_price
    assert linear < arb("0.527")
    assert nonlinear < arb("0.142")
    assert total < arb("0.666")
    print(json.dumps({
        "kind": "seed_resummation_actual_upper", "height": depth,
        "eventual_linear_upper": "0.527", "eventual_nonlinear_upper": "0.142",
        "eventual_total_upper": "0.666",
    }, sort_keys=True))
    if depth == 601:
        assert lower_standard_cone(whole) > arb("0.570")
        print(json.dumps({
            "kind": "resummed_comparison_obstruction", "height": depth,
            "principal_weights": len(trial), "subinvariance_strict_lower": "0.570",
        }, sort_keys=True))
        _, ratio = inherited["tail_ratio"](norm)
        activation = inherited["retained"](core,0)
        leak = inherited["old"]["polynomial"](inherited["norms"],norm)
        leak -= sum(x*w for x,w in zip(activation,inherited["tilt"]))
        leak += 2*abs(t).sqrt()*abs(inherited["bn"])*ratio**15/(1-ratio)
        assert 0 <= leak < eps
        h = [u.upper() for u in activation[1:]]
        h[0] += inherited["tol"]
        assert inherited["center_mass"]+sum(k*x for k,x in enumerate(h,1))+4*eps < arb("4.8")
