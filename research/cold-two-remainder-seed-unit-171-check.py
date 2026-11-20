from fractions import Fraction as Q
from math import comb

center = Q(2031, 128)
a = Q(1, 2**17)
N = 4*(center-a)
M = Q(4811, 1000)
x = M**2/N
eps = Q(11, 1000)
y_max = Q(8000001, 1000000)
y0 = 8/(4*center)
y1 = y_max/(4*center)
delta = y_max*Q(1, 2**16)/(4*center*(center-a))
rho = Q(127, 1000)
def c(l):
    return Q(comb(2*l, l), 4**l)
def b(l):
    return (2*l+1)*c(l)
def al(l):
    return b(l)*c(l)
def f(k):
    return Q(4*(k+1), 3)*al(k+1)
def alternating_upper(coef):
    return 1-coef(1)*y0+coef(2)*y1**2-coef(3)*y0**3+coef(4)*y1**4

assert y1+delta<rho
U = alternating_upper(al)+delta*(3+rho)/(1-rho)**3
U1 = alternating_upper(f)+delta*Q(8, 3)/(1-rho)**3
s_lo = Q(282842712, 10**8)
s_hi = Q(282842731, 10**8)
rt_N = Q(7966725769249, 10**12)
rt_x = Q(797070143291, 10**12)
assert s_lo**2 < 8 < y_max < s_hi**2
assert rt_N**2 < N and rt_x**2 < 1-x
assert U1 < Q(802, 1000)
pure_debits = sum(b(l)*(l+2*(1-l)*c(l))*(8/N)**l for l in range(1, 5))
mixed_debits = sum(b(l)*4*(2*l)*(2*c(l))*s_lo*8**(l-1)*(M-s_hi)/N**l for l in range(1, 5))
mixed_credit = 12*s_hi*(M-s_lo)*U1/N
remaining = (2+x-12/N)/((1-x)**2*rt_x)-2+2*U-pure_debits+mixed_credit-mixed_debits
assert 0 < remaining
upper = eps**2/rt_N*remaining
assert upper < Q(8873856, 10**11)
assert Q(1066, 1000)*upper < Q(946, 10**7)
print('Rational checks passed for the mixed scalar, source and first outer step.')

def f2(k):
    return Q(4*(k+1)**2, 3)*al(k+1)

U2 = alternating_upper(f2) + Q(4,3)*delta*(4+2*rho)/(1-rho)**4
assert U2 < Q(635, 1000)
two_debits = sum(4*b(l)*comb(2*l,2)*c(l-1)*8**(l-1)*(M-s_hi)**2/N**l
                 for l in range(1, 5))
two_credit = 6*(M-s_lo)**2*U2/N
remaining_two = remaining+two_credit-two_debits
assert 0 < remaining_two
upper_two = eps**2/rt_N*remaining_two
assert upper_two < Q(8311056, 10**11)
assert Q(1066, 1000)*upper_two < Q(8861, 10**8)
print('Rational checks passed for the two-remainder scalar, source and first outer step.')
