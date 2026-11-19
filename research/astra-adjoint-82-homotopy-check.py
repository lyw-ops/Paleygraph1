"""Uniform cold residual homotopy and warm stationary packet certificates."""
import json
import runpy
from pathlib import Path
from flint import acb, arb, arb_poly,ctx

source=Path(__file__).resolve().parent
kernel=runpy.run_path(str(source/'astra-joint-65-check.py'))
ctx.prec=192
COLD = [
    24274162210844200000,10405934873803000000,5506949744551620000,2744032761803300000,1463574463912060000,
    710760699246702000,335261278579651000,163754823416785000,82108983710018700,42020514297897100,
    21859767591422500,11525510152770300,6145268325048720,3307840421154010,1795090331226460,
    981064323890710,539506594860878,298311312887559,165750206683639,92497228618559,
    51820970792475,29135547888538,16433958894410,9296965473417,5273682886629,
    2998934853058,1709296819560,976319001994,558758362117,320372608287,
    184006284817,105854149838,60987042083,35186992042,20328509007,
    11759117334,6810193849,3948498230,2291745875,1331493799,
    774332551,450722683,262579230,153089590,89309136,
    52110991,30373567,17610566,10002690,5114009,
]
WARM = [
    24278022415653700000,10407632649158000000,5508033766855650000,2744507805427260000,1463854652363650000,
    710860363710527000,335282642954283000,163755111532148000,82104871196264000,42016522281997100,
    21856807333394100,11523516124207200,6143985365487230,3307035551262830,1794593005130420,
    980759999303176,539321578943239,298199336605977,165682652244926,92456567858213,
    51796538856409,29120885927441,16425168313687,9291698779002,5270529102466,
    2997047040571,1708167115039,975643096686,558354019136,320130739883,
    183861610632,105767613304,60935279550,35156028697,20309986340,
    11748036105,6803563973,3944531256,2289372031,1330073154,
    773482275,450213735,262274567,152907210,89199974,
    52045693,30334591,17587461,9989314,5107087,
]

def verify(base,real_half,imag_den,lam,caps,epsilon):
    t=acb(arb(base,real_half),arb(0,arb(1)/imag_den))
    rows,pars=kernel['upper'](t)
    rows[0]=[x*lam for x in rows[0]]
    aa,b,c,d,z,w,v=pars
    leak,coord=kernel['joint']['cap_invariant'](base-real_half,base+real_half,imag_den,
        rows,[aa,b,c,d,z,w+v],[arb(i)/10**6 for i in caps],epsilon)
    # Covers the two marked forcing and bad-lift packages for n >= 1e30.
    repair=arb(1)/10**12
    print(json.dumps(dict(base=str(base),real_halfwidth=str(real_half),imaginary_denominator=imag_den,
        lambda_radius=str(lam),excess=str(leak),budget=str(epsilon),coordinate_cap=str(coord))), flush=True)
    assert leak+repair<epsilon and coord<arb('4.66')
    assert coord/(4*(base-real_half)-coord**2).sqrt()<arb('0.75')
    return t,rows,pars

cold=verify(arb(2031)/128,arb(1)/2**17,2**17,arb(998955)/10**6,COLD,arb(5)/10**7)
verify(arb(16640292)/2**20,arb(1)/2**21,2**21,arb(1),WARM,arb(6)/10**8)

# Freeze the true forced solution on the entire lambda disk.  The root
# subtraction and its lambda factor only affect arity zero.
t,rows,pars=cold
price_seed=[0,100000000,252096962,426022003,610988868,801800102,995794595,
    1191554323,1388305338,1585618222,1783251866,1981069672,2178993704,
    2376979244,2575000515,2773042601,2971096840,3169158191,3367223711,
    3565291678,3763361083,3961431332,4159502075,4357573101,4555644271]
price_seed=[arb(x)/10**8 for x in price_seed]
slope=price_seed[-1]-price_seed[-2]
def price(k):
    k=abs(k)
    if k<len(price_seed):return price_seed[k]
    return price_seed[-1]+(k+1-len(price_seed))*slope
assert all(k<=price(k)<=2*k for k in range(1,len(price_seed)+1)) and 1<slope<2
h=[arb(i)/10**20 for i in COLD]; eps=arb(5)/10**7
n=len(h); zero=sum(i*v for i,v in enumerate(h))+arb(14)/5*eps+arb(1)/10**8
core=arb_poly([v/2 for v in reversed(h)]+[zero]+[v/2 for v in h]); eta=arb(1)/5
def tiltn(row,r):return sum(row[r+k]*(2 if k else 1)*(eta*k).cosh() for k in range(r+1))
B=tiltn(core,n)+eps
power=arb_poly([1]); accum=[arb(0) for k in range(n+1)]; total=arb(0)
for j,row in enumerate(rows[1:],1):
    if j>1:power*=core
    side=[x/2 for x in row[1:]]; width=len(side)
    ker=arb_poly(side[::-1]+[row[0]]+side)
    tmp=ker*power; center=width+(j-1)*n
    for k in range(n+1):accum[k]+=j*(2 if k else 1)*tmp[center+k]
    total+=j*tiltn(ker,width)*B**(j-1)
a,b,c,d,z,w,v=pars; fields=kernel
M=B+fields['kern']['dim']*eta.cosh()+a*(1+(2*eta).cosh())+b*(1+3*eta.cosh()/2+3*(3*eta).cosh()/2)
M+=c*tiltn(fields['kern']['F'],4)+d*tiltn(fields['kern']['G'],5)+z*tiltn(fields['old']['R'],2)+(w+v)*tiltn(fields['field'],4)
s=M**2/(4*(arb(2031)/128-arb(1)/2**17)); bn=arb(1)
for k in range(1,16):bn*=(arb(3)/2-k)/k
total+=4*abs(t).sqrt()*abs(bn)*s**15/M*(15/(1-s)+s/(1-s)**2)
excess=total-sum(x*(eta*k).cosh() for k,x in enumerate(accum))
assert excess>=0
moment=sum(x*price(k) for k,x in enumerate(accum)); mass=sum(accum)
ratios=[moment/slope+mass]
for k in range(1,n+len(price_seed)+1):
    col=(k-1)*moment+sum(x*(price(k+u)+price(k-u))/2 for u,x in enumerate(accum))
    ratios.append(col/price(k))
q=max(y.upper() for y in ratios)+10*excess+arb(1)/10**12
# Actual forcing direction. Undo only its arity-zero homotopy weight.
source_ratio=(M-B)**2/(4*(arb(2031)/128-arb(1)/2**17))
source_tail=2*abs(t).sqrt()*abs(bn)*source_ratio**15/(1-source_ratio)
R=sum(price(k)*x for k,x in enumerate(rows[0]))/(arb(998955)/10**6)+8*source_tail+arb(1)/10**12
assert R<arb('0.17')
radius=arb(7)/10**5
added=((1-q)*radius-radius**2)/R
print(json.dumps(dict(kind='forced_solution_directional_extension',rate=str(q),
    forcing_price_upper=str(R),radius=str(radius),lambda_step_lower=str(added))),flush=True)
assert q<arb('0.99985') and q+2*radius<1 and added>arb(34)/10**9
