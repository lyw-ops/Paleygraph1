# Independent check of Report 3 constants: rational upper bounds via squaring.
from fractions import Fraction as F
from math import isqrt
N=4*(F(2031,128)-F(1,2**17))
def c_upper_ok(M,cbound):
    # c(M)=(2/sqrtN)(1+x/2)(1-x)^(-5/2) <= cbound  <=>  4(1+x/2)^2 <= cbound^2 N (1-x)^5
    x=M*M/N
    return 4*(1+x/2)**2 <= cbound**2*N*(1-x)**5
print("c(5.198)<1.22:",c_upper_ok(F(5198,1000),F(122,100)), " <1.2182:",c_upper_ok(F(5198,1000),F(12182,10000)))
print("c(4.873)<1:",c_upper_ok(F(4873,1000),F(1)))
print("c(4.936)<=1.0043:",c_upper_ok(F(4936,1000),F(10043,10000)), " <=1.0042:",c_upper_ok(F(4936,1000),F(10042,10000)))
p0=F(1272,100000); c=F(10043,10000)
for k0 in (F(7739,10000),F(77395,100000),F(7740,10000)):
    disc=(1-k0)**2-4*c*p0
    if disc<=0: print(k0,"disc<=0"); continue
    # u_- = ((1-k0)-sqrt(disc))/(2c); check u_- <= 0.113 : (1-k0)-2c*0.113 <= sqrt(disc)
    lhs=(1-k0)-2*c*F(113,1000)
    ok = lhs<=0 or lhs*lhs<=disc
    print(k0,"disc>0, u_-<=0.113:",ok, float(((1-k0)-float(disc)**0.5)/(2*c)))
# fixed point property check numerically: iterate recursion from 0 with k0=0.7739
k0=0.7739; u=0.0
for j in range(2000): u=0.01272+k0*u+1.0043*u*u
print("iterate limit",u)
# Round 177 replay with 1.066 and 1.22
u=F(0); out=[]
for j in range(10):
    u=F(1272,100000)+F(1066,1000)*u+F(122,100)*u*u; out.append(float(u))
print([round(x,5) for x in out])
