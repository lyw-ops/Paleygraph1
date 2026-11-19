"""Uniform interval certificate with the first rank-three feedback distinguished."""
from collections import defaultdict
from math import comb
from pathlib import Path
import json
import runpy
from flint import acb, arb, arb_poly, ctx

prev = runpy.run_path(str(Path(__file__).with_name("astra-signed-54-check.py")))
domain = runpy.run_path(str(Path(__file__).with_name("marked-domain-53-check.py")))
D = prev["D"]
ctx.prec = 192
P = prev["legendre_powers"]()
W = arb_poly([arb(1)/4,0,arb(3)/4,1,arb(3)/4,0,arb(1)/4])
UNIT = arb(1)/4


def make(t, lower=False, fusion=False):
    endpoint = arb.lower if lower else arb.upper
    modes = domain["laurent"](t,True)
    center = modes[0][2]
    correction = modes[2][2]*center**2/2 if fusion else acb(0)
    a = center+correction
    apow = [a**i for i in range(D+1)]
    grouped = {}
    for r in range(D+1):
        for k in range(D-r+1):
            g = defaultdict(lambda: acb(0))
            for h in range(D-r-k+1):
                c = modes[r+h][k]*comb(r+h,r)*apow[h]
                if c == 0:
                    continue
                for key,mult in P[h].items():
                    g[key] += c*mult
            grouped[r,k] = g
    beta = 2*grouped[0,1][1,0]
    beta_abs = endpoint(abs(beta))
    def kernel(j, amended):
        n = 2*(D-j)
        row = [arb(0) for i in range(2*n+1)]
        for k in range(D-j+1):
            g = grouped[j,k].copy()
            if amended:
                if (j,k) == (0,2):
                    # Remove modes[0][2] before interval arithmetic.
                    g[0,0] = sum((modes[h][2]*apow[h]*P[h].get((0,0),0)
                                  for h in range(1,D-k+1)),acb(0)) - correction
                if (j,k) == (0,1):
                    g[1,0] = g[0,1] = acb(0)
                for key,val in grouped.get((j+2,k),{}).items():
                    g[key] = g.get(key,0) + comb(j+2,2)*beta**2*UNIT*val
            for (u,v),val in g.items():
                price=endpoint(abs(val))*(v+1)/2
                for w in range(-2*u,2*u+1,4):
                    row[n+w+k] += price
                    row[n+w-k] += price
        return arb_poly(row)
    raw = [kernel(j,False) for j in range(D+1)]
    out = []
    for j in range(D+1):
        n = 3*(D-j)
        pol = kernel(j,True).left_shift(n-2*(D-j))
        for ell in range(1,D-j+1):
            if ell == 1:
                power = W
            else:
                power *= W
            factor = power if ell != 2 else power - arb_poly([UNIT]).left_shift(6)
            row = raw[j+ell]*factor
            pol += row.left_shift(n-2*(D-j-ell)-3*ell)*(comb(j+ell,j)*beta_abs**ell)
        if fusion:
            # The group characters carry the positive-trace convention of round 32.
            # The test below keeps only the Legendre-trivial sector.
            saved = [arb(0) for _ in range(2*n+1)]
            def leg_unit(r,e):
                v=grouped.get((r,abs(e)),{}).get((0,0),acb(0))
                return v/(2 if e else 1)
            if j+2<=D:
                for e in range(-8,9):
                    for shift, weights in ((1,(-1,-1,3)),(-1,(1,1,-3)),
                                            (-1,(-1,0,0)),(1,(1,0,0))):
                        entries = [beta*(j+1)*leg_unit(j+1,e)/4,
                                   beta**2*comb(j+2,2)*leg_unit(j+2,e-shift)/16,
                                   beta**3*comb(j+3,3)*leg_unit(j+3,e)*3/16]
                        diff=sum(abs(v) for v in entries)-abs(sum(entries))
                        saving=max(arb(0),diff.upper() if lower else diff.lower())
                        for k in weights:
                            if abs(k-e)<=n:
                                saved[n+k-e] += saving
            pol -= arb_poly(saved)
        out.append([pol[n+k]*(2 if k else 1) for k in range(n+1)])
    return out,abs(a).upper(),beta_abs


def verify(w,a,b,low,high,caps,e):
    n=len(caps)
    h=[arb(x)/10**13 for x in caps]
    eta=arb(1)/5
    zero=sum(i*v for i,v in enumerate(h))+e/eta+arb(1)/10**8
    side=[v/2 for v in h]
    base=arb_poly(side[::-1]+[zero]+side)
    norm=zero+sum(v*(eta*k).cosh() for k,v in enumerate(h,1))
    leak=arb(0)
    pooled=[arb(0)]*(D*n+3*D+1)
    power=arb_poly([1])
    for j,ker in enumerate(w):
        if j: power *= base
        side=[v/2 for v in ker[1:]]
        row=power*arb_poly(side[::-1]+[ker[0]]+side)
        center=j*n+len(side)
        for i in range(1,len(row)-center):
            pooled[i]+=2*row[center+i]
        if j:
            leak += sum(v*(eta*k).cosh() for k,v in enumerate(ker))*j*(norm+e)**(j-1)*e
    for k,v in enumerate(pooled[1:],1):
        cap=h[k-1] if k<=n else arb(0)
        leak+=max(arb(0),(v-cap).upper())*(eta*k).cosh()
    seed=prev["warm"]["SEED"]
    total=seed*eta.cosh()+a*(1+(2*eta).cosh())+b*(1+arb(3)/2*eta.cosh()+(3*eta).cosh()/2)+norm+e
    r=total**2/(4*low)
    assert r<1
    c=arb(1)
    for ell in range(1,D//2+2):
        c *= (arb(3)/2-ell)/ell
    tail=2*high.sqrt()*abs(c)*r**(D//2+1)/(1-r)
    leak+=tail
    B=seed+2*a+3*b+zero+sum(h)+e
    assert leak < arb(38)/10**6 < e
    assert B < arb(47)/10


CASES = [(8135, 8138, 512,
  [2843769851248, 1403399893286, 593714823822, 370653050416, 153516747282, 68475674185, 32067654118,
   15550575990, 7741242339, 3933212606, 2031403032, 1063343363, 562879583, 300800846, 162061341,
   87932235, 48006929, 26353152, 14536901, 8053798, 4479517, 2500357, 1400147, 786367, 442843, 250008,
   141468, 80220, 45579, 25945, 14794, 8449, 4833, 2769, 1588, 912, 525, 302, 174, 101, 58, 34, 20, 12,
   7, 4]),
 (8137, 8141, 512,
  [2800520808071, 1385177512696, 584527579314, 365780494323, 150886099087, 67029976055, 31263188806,
   15098774814, 7485689265, 3787842199, 1948326872, 1015684561, 535450164, 284970375, 152903082,
   82622869, 44923206, 24559157, 13491688, 7444033, 4123362, 2292106, 1278258, 714960, 400976, 225442,
   127042, 71744, 40596, 23013, 13068, 7433, 4234, 2416, 1380, 789, 452, 259, 149, 86, 50, 29, 17, 10, 6,
   3]),
 (8140, 8146, 512,
  [2836138429316, 1400098016027, 592042908289, 369731547805, 153025225514, 68205698759, 31917291193,
   15466007642, 7693329653, 3905911208, 2015773886, 1054361754, 557701385, 297807173, 160326463,
   86924744, 47420772, 26011568, 14337551, 7937303, 4411360, 2460437, 1376743, 772633, 434777, 245268,
   138679, 78579, 44613, 25375, 14458, 8251, 4716, 2700, 1547, 888, 510, 294, 169, 98, 57, 33, 19, 11, 7,
   4]),
 (1018, 1027, 64,
  [2869924097900, 1414409837626, 599254878697, 373564677002, 155098235309, 69350596073, 32557155208,
   15827013203, 7898429538, 4023081259, 2083012206, 1093090186, 580078527, 310771258, 167854559,
   91305083, 49974094, 27502275, 15209107, 8447518, 4710388, 2635877, 1479772, 833191, 470401, 266240,
   151034, 85862, 48909, 27911, 15955, 9136, 5239, 3009, 1730, 996, 575, 332, 192, 111, 65, 38, 22, 13,
   7, 4])]


def rectangle(first,last,div,caps):
    width=arb(1)/2048
    env=None
    a=b=arb(0)
    for ix in range(first,last):
        t=acb(prev["warm"]["slab"](ix,div),arb(0,width))
        w,al,be=make(t,fusion=True)
        if env is None: env=w
        else: env=[[max(u,v) for u,v in zip(ou,ov)] for ou,ov in zip(env,w)]
        a,b=max(a,al),max(b,be)
    e=arb(6)/10**5
    verify(env,a,b,arb(first)/div,abs(acb(arb(last)/div,width)),caps,e)
    print(json.dumps(dict(kind="rank_three_signed_complex_rectangle",slabs=[first,last],
                          division=div,imaginary_half_width="1/2048",cap_count=len(caps),
                          residual_limit="6/100000",residual_output_upper="38/1000000",
                          scaled_vector_upper="4.7",precision=ctx.prec),sort_keys=True))


def escape():
    floor = arb(127)/8
    _,a,b = make(acb(floor))
    lower,_,_ = make(acb(floor),True)
    radius=arb(2)
    r=(prev["warm"]["SEED"]+2*a+3*b+radius)**2/(4*floor)
    assert r<1
    c=arb(1)
    for ell in range(1,D//2+2):
        c*=(arb(3)/2-ell)/ell
    tail=2*floor.sqrt()*abs(c)*r**(D//2+1)/(1-r)
    n=24
    shift=14
    kernels=[]
    for j in range(9):
        error = tail/radius**j
        side=[max(arb(0),(v/2-error).lower()) for v in lower[j][1:shift+1]]
        zero=max(arb(0),(lower[j][0]-error).lower())
        kernels.append(arb_poly(side[::-1]+[zero]+side))
    assert kernels[2][shift]>arb(1)/20
    h=[arb(0)]*n
    for height in range(1,2501):
        side=[v/2 for v in h]
        base=arb_poly(side[::-1]+[sum(i*v for i,v in enumerate(h))]+side)
        power=arb_poly([1])
        out=[arb(0)]*n
        for j,ker in enumerate(kernels):
            if j: power*=base
            row=ker*power
            for k in range(1,n+1):
                out[k-1]+=2*row[shift+j*n+k]
        h=[v.lower() for v in out]
        if sum(i*v for i,v in enumerate(h,1))>21:
            print(json.dumps(dict(kind="rank_three_quadratic_unit_escape",floor="127/8",height=height,quadratic_lower="1/20",mass_lower=21,packets=n,shifts=shift,arities=len(kernels)-1),sort_keys=True))
            return
    raise AssertionError("no lower escape")


if __name__ == "__main__":
    for case in CASES:
        rectangle(*case)
    escape()
