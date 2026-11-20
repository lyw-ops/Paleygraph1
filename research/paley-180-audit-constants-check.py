from decimal import Decimal as Dm, getcontext
from fractions import Fraction as Fr
getcontext().prec=60
# Report 2 rows
def inv(a,p): return pow(a%p,p-2,p)
p=101
for pi in range(2,p):
  for X in range(2,p):
    for rho in range(1,p):
      if len({0,1,X,pi,rho})<5: continue
      # fixed pi varying rho'=rho
      z=(1-pi)*inv(rho-pi,p)%p
      assert rho*(1-pi)*inv(rho-pi,p)%p==(pi*z+1-pi)%p
      # fixed rho varying pi'=pi
      c=(X-rho)*inv(1-rho,p)%p
      assert c not in (0,1)
      assert (X-pi)*inv(rho-pi,p)%p==(c*z+1-c)%p
print("rows ok")
# Report 3 constants
R600=4*Dm('0.449922')**600
print("4*0.449922^600 =",R600)
eps=Dm('0.545')**2*R600; print("eps* =",eps, eps<Dm('9.07e-209'))
print("eps/(1-.545)",eps/Dm('0.455'))
for rho,q in ((Dm('0.025'),Dm('0.525')),(Dm('0.05'),Dm('0.535')),(Dm('0.375'),Dm('0.545'))):
    print("Lambda room rho",rho, (rho/2)*(1-q)/Dm('9.07e-209'))
N=4*(Fr(2031,128)-Fr(1,2**17)); s=Fr(2828428,10**6)
import math
for rho in ('0.025','0.05','0.375','0.3906'):
    B=Fr(1963,1000)+Fr(rho)
    mono=2*s*B*(N-2*B*B)-4*B*B*(s+B)**2
    q=math.sqrt(float((s+B)**2/(N+(s+B)**2)))
    print("rho",rho,"monotone",mono>0,"q(u=1)",q)
print("2^-7/8",2**(-7/8), "0.545^8<2^-7", Fr(545,1000)**8<Fr(1,128))
print("kappa thresholds",1-0.01272/0.375,1-0.01272/0.025)
print("rho max analytic", math.sqrt(float(N)/2)-1.963)
# Report 1 exponent arithmetic
F=Fr
print(F(11,4)-F(3,836)-F(43,16)==F(197,3344), F(5,16)+F(43,128)+F(1,2)==F(147,128), F(147,64)+F(1,2)==F(179,64),
 F(29,16)-F(3,3344)-F(115,64)==F(197,13376), F(9,8)+F(43,64)==F(115,64))
# Report 2 exponents
print(F(1,2)-F(1,1280)+F(11,8)==F(2399,1280), F(1,2)-F(1,1280)+F(45,32)==F(2439,1280), F(1,2)-F(1,1280)+F(179,128)==F(2429,1280), F(1,2)+F(179,128)==F(243,128), F(139,128)+F(5,16)==F(179,128))
