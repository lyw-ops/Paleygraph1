"""Arb bounds for the first two full complex Jacobi returns and the real tracker."""
import json
from math import comb
from flint import acb, arb, ctx

ctx.prec = 160
t0 = arb(2031) / 128
width = arb(1) / 2**17
t = acb(arb(t0, width), arb(0, width))
low = t0 - width
nterm = 18
z = 2 / t
coef = [acb(0) for _ in range(nterm + 1)]
binom = arb(1)
for k in range(1, nterm + 1):
    binom *= (arb(3)/2-k)/k
    for m in range(1, k+1):
        coef[m] += 2*t.sqrt()*binom*z**k*comb(2*k,k-m)*2/4**k
# Bound the sum of dimensional costs at every omitted order using |binom| <= 1.
rho = abs(z)
tail = 4*abs(t).sqrt()*rho**(nterm+1)*(
    (nterm+1)/(1-rho)+rho/(1-rho)**2)
squares = sum(abs(v)**2 for v in coef[1:])/2
g_lower = squares.sqrt()-tail
g_upper = squares.sqrt()+tail
cap = sum(2*m*abs(coef[m]) for m in range(1,nterm+1))+tail
tail_rms = (sum(abs(v)**2 for v in coef[2:])/2).sqrt()+tail
c = arb('0.120')
# Integrate the true L2 seed multiplier with interval boxes.
seed = arb(8).sqrt()
blocks = 512
v2 = arb(0)
for i in range(blocks):
    angle = arb.pi()*arb(arb(2*i+1)/(4*blocks),arb(1)/(4*blocks))
    x = seed*angle.cos()
    v2 += (x*abs(1/(4*t+x*x).sqrt()-c))**2/blocks
v = v2.sqrt()
# Each degree-k term is proportional to t^(1/2-k).
imcap = width*4*abs(t).sqrt()/low*rho*(1+rho)/(1-rho)**3
assert imcap < arb('0.00001')
g_fourth_squared = (3*squares**2-abs(coef[1])**4/8).sqrt()
g_fourth_squared = (g_fourth_squared.sqrt()+tail)**2
# Include the transported square of the first Legendre mode as a second model term.
q = arb('0.112')
real_cap = seed+cap
range_lo = 4*t0/(4*t0+real_cap**2)**arb('1.5')
range_hi = 1/(4*t0).sqrt()
k3 = 12*abs(t)*(seed+cap)/(4*low-cap**2)**arb('2.5')
dt2 = (4*(4*abs(t)+(seed+cap)**2)+24*abs(t))/(4*low-cap**2)**arb('2.5')
delta_curvature = max(q-range_lo,range_hi-q)+k3*imcap+dt2*abs(t-t0)
quad_error = q*(cap+2*abs(coef[1]))*tail_rms/2
linear = v*g_upper+2*c*tail_rms
err = linear+quad_error+delta_curvature*g_fourth_squared/2
mu = (2*(c*abs(coef[1]))**2+arb(3)/8*(q*abs(coef[1])**2/2)**2).sqrt()
assert mu > err
lower = ((mu*g_lower-cap*err)/(mu+err))**2
upper = ((mu*g_upper+cap*err)/(mu-err))**2
assert mu*g_lower>cap*err
assert lower > arb('0.0230') and upper < arb('0.0377')
print(json.dumps({k:str(v) for k,v in dict(cap=cap, g_lower=g_lower, g_upper=g_upper,
       leading_norm=mu, error_upper=err, mixed_lower=lower, mixed_upper=upper).items()}))
M = arb('4.8')
a = arb(63)
f = (a+M**2).sqrt()
e = 2*(f-a.sqrt())
assert 4*low>a and e < arb('2.68')
assert a/(f*(f+64)) > arb('0.09')
assert 64*a/(f*(f+64))-2*e > arb('0.04')
assert 1+1/arb('0.05') < 25
print(json.dumps({"tracking_huber_coefficient":"0.04","tracking_residual_coefficient":25,
                  "real_residual_limsup_upper":str(4*arb('0.428236')**600)}))
eta = arb(3)/40
weighted_W = (arb('4.768')+arb('3.77')*((5*eta).cosh()-1)
              +arb('1.94')*((50*eta).cosh()-1)/50+arb('0.00001'))
weighted_D = weighted_W/(63-weighted_W**2).sqrt()
transport = 1+1/(arb(2).sqrt()*eta)
assert weighted_W < arb('5.824') and weighted_D*(transport+arb('0.001'))<12
r = 4*arb('0.428236')**600
N = 150
assert arb('1.5')*(1250*arb(12)/11+625*arb('0.52')) < 2600
mark = (25*arb('0.52')*arb('0.428236')**N*r+2600*12**N*r*r)/2
assert mark < arb('2e-275')
print(json.dumps({"adjoint_steps":N,"growth":12,"W_tilt_upper":str(weighted_W),
                  "physical_real_mark_limsup_upper":str(mark)}))
