"""Arb packet Schur tests at physical nine-center predictors on the closed square."""
import json
import runpy
from pathlib import Path
from flint import acb, arb, arb_poly, ctx

old = runpy.run_path(str(Path(__file__).with_name('astra-predictor-76-check.py')))
ctx.prec = 192
fields = old['fields']
N, KEEP = old['N'], old['KEEP']
symmetric, tilt, eps = old['symmetric'], old['tilt'], old['eps']
a, half = arb(2031)/128, arb(1)/2**17
t = acb(arb(a, half), arb(0, half))
rows, pars = fields['upper'](t)
rows = [[x.upper() for x in row] for row in rows]
folded = [symmetric(row, KEEP) for row in rows]
norms = [sum(v*w for v,w in zip(row,tilt)) for row in rows]
a1,b,c,d,z,w,v = pars
seed = fields['kern']['dim']
def polytilt(poly, r):
    return sum(poly[r+i]*(2 if i else 1)*tilt[i] for i in range(r+1))
center = seed*tilt[1]+a1*(1+tilt[2])+b*(1+3*tilt[1]/2+3*tilt[3]/2)
center += c*polytilt(fields['kern']['F'],4)+d*polytilt(fields['kern']['G'],5)
center += z*polytilt(fields['old']['R'],2)+(v+w)*polytilt(fields['field'],4)
# Fixed rational trial prices, linearly extended by their final secant.
scaled = [0,100000000,252200485,426274040,611406156,802387069,996550741,
          1192477542,1389393325,1586868991,1784663875,1982641789,
          2180725131,2378869432,2577049092,2775249319,2973461537,
          3171680760,3369904083,3568129809,3766356945,3964584907,
          4162813351,4361042071,4559270933]
values = [arb(i)/10**8 for i in scaled]
slope=values[-1]-values[-2]
assert all(k<=x<=2*k for k,x in enumerate(values)) and 1<slope<2
def price(k):
    k=abs(k)
    if k<len(values): return values[k]
    return values[-1]+(k+1-len(values))*slope

bn=arb(1)
for i in range(1,16): bn *= (arb(3)/2-i)/i
h=[arb(0)]*N
product=arb(1)
res0=None
last=0
best=arb(0)
strong=arb(0)
A=4*(a-half)
raw_factor=2*abs(t).sqrt()*A.sqrt()
chosen=set(range(1,301)) | set(range(305,601,5))
for height in range(1,601):
    zero=sum(i*x for i,x in enumerate(h))+arb(14)/5*eps+arb(1)/10**8
    core=symmetric([zero]+h,N)
    power=arb_poly([0]*KEEP+[1]); partial=arb_poly()
    for j,kr in enumerate(folded):
        if j:
            tmp=power*core
            power=arb_poly([tmp[i+N] for i in range(2*KEEP+1)])
        tmp=kr*power
        partial+=arb_poly([tmp[i+2*KEEP] for i in range(N+1)])
    next_h=[(2*partial[k]).upper() for k in range(1,N+1)]
    next_h[0]+=arb(1)/10**12
    assert all(b>=a for a,b in zip(h,next_h))
    h=next_h
    if height==1:
        res0=sum(price(k)*x for k,x in enumerate(h,1))+8*eps
    if height not in chosen: continue
    zero=sum(i*x for i,x in enumerate(h))+arb(14)/5*eps+arb(1)/10**8
    core=symmetric([zero]+h,N)
    norm=zero+sum(x*y for x,y in zip(h,tilt[1:]))+eps
    power=arb_poly([0]*KEEP+[1]); der=arb_poly()
    for j in range(1,len(rows)):
        if j>1:
            tmp=power*core
            power=arb_poly([tmp[i+N] for i in range(2*KEEP+1)])
        tmp=folded[j]*power
        der+=arb_poly([j*tmp[i+2*KEEP] for i in range(N+1)])
    mu=[der[k]*(2 if k else 1) for k in range(N+1)]
    M=center+norm
    ratio=M**2/(4*(a-half))
    assert ratio<1
    tail=4*abs(t).sqrt()*abs(bn)*ratio**15/M*(15/(1-ratio)+ratio/(1-ratio)**2)
    leak=sum(j*norms[j]*norm**(j-1) for j in range(1,len(rows)))-sum(x*y for x,y in zip(mu,tilt))+tail
    assert leak>=0
    norm0=sum(mu); moment=sum(x*price(i) for i,x in enumerate(mu))
    def ordinary(k):
        return (k-1)*moment+sum(x*(price(k+i)+price(k-i))/2 for i,x in enumerate(mu))
    cutoff=N+len(values)
    # For k >= cutoff both the image column price and its source are affine.
    limits=[ordinary(k)/price(k) for k in range(1,cutoff+1)]
    limits.append(moment/slope+norm0)
    # Absolute-price defect is <= 2(1+|u|) per unit kernel mass,
    # hence <= 10 cosh(u/5); column repair is < 1e-12 for n >= 1e30.
    rate=max(x.upper() for x in limits)+10*leak+arb(1)/10**12
    product*=rate**(height-last)
    last=height
    if rate<1:
        br=min(arb(3)/100,(1-rate)/2)
        hom=((1-rate)*br-br**2)/(res0*product)
        if hom.lower()>best:
            best=hom.lower(); bestrow=(height,str(rate),str(res0*product),str(br),str(hom))
    if height<=300:
        second=arb_poly(); power=arb_poly([0]*KEEP+[1])
        for j in range(2,len(rows)):
            if j>2:
                tmp=power*core
                power=arb_poly([tmp[i+N] for i in range(2*KEEP+1)])
            tmp=folded[j]*power
            second+=arb_poly([j*(j-1)*tmp[i+2*KEEP] for i in range(N+1)])
        sec=[second[k]*(2 if k else 1) for k in range(N+1)]
        tail2=2*abs(t).sqrt()*abs(bn)*ratio**15/M**2*(870/(1-ratio)+118*ratio/(1-ratio)**2+4*ratio*(1+ratio)/(1-ratio)**3)
        leak2=sum(j*(j-1)*norms[j]*norm**(j-2) for j in range(2,len(rows)))-sum(x*y for x,y in zip(sec,tilt))+tail2
        assert leak2>=0
        small=30; far=small+N+len(values)
        P=[sum(x*(price(k+i)+price(k-i))/2 for i,x in enumerate(sec)) for k in range(far+small+1)]
        m0=sum(sec); m1=sum(k*x for k,x in enumerate(sec))
        # Two large packets use the linear price majorant. One small packet
        # and arbitrarily large partner reduce to affine/affine after far.
        assert all(price(i+1)*i>=price(i)*(i+1) for i in range(1,len(values)))
        tested=[2*(m1+2*m0)*(small/price(small))**2]
        for k in range(1,small):
            den=price(k)
            for l in range(k,far+1):
                out=(k-1)*(l-1)*P[0]+(l-1)*P[k]+(k-1)*P[l]+(P[k+l]+P[abs(k-l)])/2
                tested.append(out/(den*price(l)))
            tested.append(((k-1)*P[0]+P[k]+k*slope*m0)/(den*slope))
        bilinear=max(x.upper() for x in tested)+12*leak2+arb(1)/10**12
        mass=seed+2*a1+3*b+4*c+arb(23)*d/4+8*(z+w+v)+sum(k*x for k,x in enumerate(h,1))+4*eps
        for mill in range(1,701):
            radius=arb(mill)/1000; u=mass+radius
            assert u<6
            f3=3*raw_factor*u/(A-u**2)**(arb(5)/2)
            f4=3*raw_factor*(A+4*u**2)/(A-u**2)**(arb(7)/2)
            cubic=2*(u*f4+3*f3)+arb(1)/10**12
            if not rate+bilinear*radius+cubic*radius**2/2<1: break
            hom=((1-rate)*radius-bilinear*radius**2/2-cubic*radius**3/6)/(res0*product)
            if hom.lower()>strong:
                strong=hom.lower(); strongrow=(height,mill,str(rate),str(res0*product),str(bilinear),str(cubic),str(hom))
    if height in (100,250,275,300,600):
        print(json.dumps(dict(kind='physical_packet_operator',height=height,
          rate_upper=str(rate),omitted_tilted_mass=str(leak),
          first_increment_upper=str(res0),segment_residual_bound=str(res0*product))),flush=True)
    if height==250: assert rate<arb('0.998')
    if height==600: assert rate<arb('1.047')

print(json.dumps(dict(kind='best_certified_residual_homotopy',row=bestrow)),flush=True)
print(json.dumps(dict(kind='best_second_derivative_residual_homotopy',row=strongrow)),flush=True)
r=4*arb('0.428236')**600
Nadj=568
G=arb('1.047')
mark=(25*arb('0.52')*arb('0.428236')**Nadj*r+
      (1250*arb('1.5')*(G**(Nadj+1)-1)/(G-1)+625*arb('0.52')*arb('1.5')*G**Nadj)*r**2)/2
print(json.dumps(dict(kind='true_stationary_mark',adjoint_depth=Nadj,mark_limsup_upper=str(mark))),flush=True)
assert mark<arb('7.57e-426') and best>arb('0.0787') and strong>arb('0.5021')
# Check the real comparison with the parity-even Newton remainder.
root63=arb(63).sqrt(); Hmax=arb('0.104'); Hratio=arb('2.084'); small=arb('0.0137')
fmax=(63+arb('4.9')**2).sqrt()
assert 1/(1-arb('0.52'))<Hratio and Hmax*Hratio/(2*root63)<small
assert Hmax**2/root63<arb('0.0014') and 63/(fmax*(fmax+1))>arb('0.65')
assert arb('5.9')/(63+arb('5.9')**2).sqrt()<arb('0.6')
assert (1+arb('1.125'))/(arb('0.65')-arb('0.32'))<7
comparison=Hratio*arb(7).sqrt()*small/root63+(2+Hmax/root63)*7*small**2
assert comparison<arb('0.013')
print(json.dumps(dict(kind='true_stationary_minus_newton_remainder',
    huber_tracking_constant=7,remainder_L1_over_initial_RMS_squared=str(comparison))),flush=True)
