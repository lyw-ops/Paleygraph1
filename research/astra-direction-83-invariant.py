"""Direct cold physical packet cap, resolving the first eight omitted binomial orders."""
import json, runpy
from pathlib import Path
from flint import acb,arb,arb_poly,ctx
src=Path(__file__).resolve().parent
fields=runpy.run_path(str(src/'astra-joint-65-check.py'))
ctx.prec=192
eta=arb(1)/5
N=58
EPS=arb(2)/10**10
lam=arb(9989704)/10**7
squares=[('cold',arb(2031)/128,arb(1)/2**17,lam),('warm',arb(16640291)/2**20,arb(1)/2**20,arb(1)),('edge',arb(133122319)/2**23,arb(3)/2**23,arb(1))]

def symmetric(row):
    sides=[x/2 for x in row[1:]]
    return arb_poly(sides[::-1]+[row[0]]+sides)

def cn(row,r):return sum(row[r+k]*(2 if k else 1)*(eta*k).cosh() for k in range(r+1))

def data(base,hw,lam):
    t=acb(arb(base,hw),arb(0,hw)); rows=None; pars=None
    slices=8 if lam<1 else 4
    w=hw/slices
    for i in range(slices):
        for j in range(slices//2):
            sub=acb(arb(base+(2*i+1-slices)*w,w),arb((2*j+1)*w,w))
            r,p=fields['upper'](sub)
            if rows is None: rows,pars=r,p
            else:
                rows=[[max(a.upper(),b.upper()) for a,b in zip(aa,bb)] for aa,bb in zip(rows,r)]
                pars=[max(a.upper(),b.upper()) for a,b in zip(pars,p)]
    rows[0]=[lam*x for x in rows[0]]
    a,b,c,d,z,w,v=pars
    # These are exactly the symmetric polynomials used in the tilted radius.
    comps=[(1,symmetric([0,fields['kern']['dim']])),(2,symmetric([a,0,a])),
        (3,symmetric([b,arb(3)*b/2,0,arb(3)*b/2])),(4,c*fields['kern']['F']),
        (5,d*fields['kern']['G']),(2,z*fields['old']['R']),(4,(w+v)*fields['field'])]
    center=sum((pol.left_shift(5-r) for r,pol in comps),arb_poly())
    seed_dim=fields['kern']['dim']+2*a+3*b+4*c+arb(23)*d/4+8*(z+w+v)
    return t,rows,center,seed_dim

def tail_coeff(t,base,hw):
    bn=arb(1); coeff=[]
    for i in range(1,24):
        bn=bn*(arb(3)/2-i)/i
        if i>=15: coeff.append(2*abs(t).sqrt()*abs(bn)/(4*(base-hw))**i)
    return coeff

def image(base,hw,data,h):
    t,rows,center,seed_dim=data
    b=symmetric([sum(i*x for i,x in enumerate(h))+arb(14)/5*EPS]+h)
    norm=cn(b,N)+EPS
    pooled=[arb(0)]*(N+1); total=arb(0)
    power=arb_poly([1])
    for j,row in enumerate(rows):
        if j: power*=b
        p=power*symmetric(row);r=j*N+len(row)-1
        for k in range(N+1):pooled[k]+=(2 if k else 1)*p[r+k]
        total+=sum(x*(eta*k).cosh() for k,x in enumerate(row))*norm**j
    cap=center.left_shift(N-5)+b; M=cn(center,5)+norm
    # Full raw powers on the symmetric physical boundary. Including the whole
    # tail for arity zero covers every |lambda| <= the stated radius.
    power=cap**30; sq=cap*cap; coeff=tail_coeff(t,base,hw)
    for i,x in enumerate(coeff[:-1],15):
        if i>15:power*=sq
        r=2*i*N
        for k in range(N+1):pooled[k]+=(2 if k else 1)*x*power[r+k]
        total+=x*M**(2*i)
    leak=total-sum(x*(eta*k).cosh() for k,x in enumerate(pooled))
    ratio=M**2/(4*(base-hw)); assert ratio<1
    leak+=coeff[-1]*M**46/(1-ratio)
    return pooled[1:],leak,seed_dim+b[N]+sum(h)+EPS

def verify(label,base,hw,lam,data,caps):
    h=[arb(x)/10**20 for x in caps]; out,leak,cap=image(base,hw,data,h)
    assert leak>=0
    leak+=sum(max(arb(0),(x-y).upper())*(eta*k).cosh() for k,(x,y) in enumerate(zip(out,h),1))
    leak+=arb(1)/10**12
    rec=dict(kind='resolved_binomial_tail_invariant',domain=label,base=str(base),halfwidth=str(hw),lambda_radius=str(lam),excess=str(leak),budget=str(EPS),coordinate_cap=str(cap),passes=bool(leak<EPS))
    print(json.dumps(rec),flush=True)
    return leak<EPS and cap<arb('4.66')

def directional(base,hw,lam,data,caps):
    t,rows,center,unused_dim=data
    h=[arb(x)/10**20 for x in caps]
    B=symmetric([sum(i*x for i,x in enumerate(h))+arb(14)/5*EPS]+h)
    norm=cn(B,N)+EPS
    total=arb(0);mu=[arb(0)]*(N+1);pw=arb_poly([1])
    for j,row in enumerate(rows[1:],1):
        if j>1:pw*=B
        r=(j-1)*N+len(row)-1;p=j*pw*symmetric(row)
        for k in range(N+1):mu[k]+=(2 if k else 1)*p[r+k]
        total+=j*sum(x*(eta*k).cosh() for k,x in enumerate(row))*norm**(j-1)
    A=4*(base-hw); M=cn(center,5)+norm; ratio=M**2/A
    ell=15; bn=arb(1)
    for j in range(1,ell+1):bn*= (arb(3)/2-j)/j
    tail=4*abs(t).sqrt()*abs(bn)*ratio**ell/M*(ell/(1-ratio)+ratio/(1-ratio)**2)
    excess=total+tail-sum(x*(eta*k).cosh() for k,x in enumerate(mu))
    assert excess>0
    prices=[0,100000000,252096962,426022003,610988868,801800102,995794595,
        1191554323,1388305338,1585618222,1783251866,1981069672,2178993704,
        2376979244,2575000515,2773042601,2971096840,3169158191,3367223711,
        3565291678,3763361083,3961431332,4159502075,4357573101,4555644271]
    prices=[arb(x)/10**8 for x in prices]; slope=prices[-1]-prices[-2]
    def price(k):
        k=abs(k)
        if k<len(prices):return prices[k]
        return prices[-1]+(k+1-len(prices))*slope
    moment=sum(x*price(k) for k,x in enumerate(mu)); mass=sum(mu)
    ratios=[mass+moment/slope]
    for k in range(1,N+len(prices)+1):
        col=(k-1)*moment+sum(x*(price(k+u)+price(k-u))/2 for u,x in enumerate(mu))
        ratios.append(col/price(k))
    q=max(a.upper() for a in ratios)+10*excess+arb(1)/10**12
    L=base-hw; U=abs(t); dim=arb('4.6531'); im=dim-arb('2.8284')
    d=dim/(4*L+dim**2-2*im**2).sqrt();curvature=4*U/(4*L-im**2)**(arb(3)/2)
    assert q<arb('.999902') and d<arb('.526') and curvature<arb('.137')
    assert arb('.17')/(1-q)<1728
    ball=arb(48)/10**6
    extra=((1-q)*ball-ball**2)/arb('.17')
    assert q+2*ball<1 and extra>arb(14)/10**9 and arb('4.652665')+ball<arb('4.653')
    length=1-lam
    strip_cap=im+1728*length+arb(3600000)*length**2/2
    assert strip_cap<arb('5.52') and strip_cap**2<2*L
    geometric=(4*(arb(152704318)**2+arb(144290996)**2)).sqrt()/10**12
    assert geometric/(1+d)>arb('.000275')
    # L^2 counting and packet prices are used on each actual summand before summing.
    P=arb('.17'); moments={}
    for order in (2,4,8,16,64):
        z=arb(2)/order
        rate=d**z*q**(1-z); nested=d**(z/2)*q**(1-z/2)
        assert 0<rate<1 and 0<nested<1
        first=P/(1-rate)
        second=(arb(2)**(1-z)*curvature**z*P**2)/((1-rate)*(1-nested)**2)
        moments[str(order)]=dict(first=str(first),second=str(second))
    print(json.dumps(dict(kind='physical_forcing_direction_moments',square_lambda=str(lam),
        packet_derivative=str(q),counting_derivative=str(d),physical_curvature=str(curvature),
        newton_ball=str(ball),extra_forcing_radius_lower=str(extra),
        imaginary_strip_sufficient_cap=str(strip_cap),center_source_limiting_RMS_lower=str(geometric),
        moments=moments)),flush=True)

if __name__=='__main__':
    path=src/'astra-direction-83-caps.json'
    caps=json.loads(path.read_text())
    for label,base,hw,lam in squares:
        d=data(base,hw,lam)
        assert verify(label,base,hw,lam,d,caps[label])
        if label=='cold': directional(base,hw,lam,d,caps[label])
