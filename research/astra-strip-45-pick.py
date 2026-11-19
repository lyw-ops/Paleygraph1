"""A marked obstruction from real spectral certificates and multipoint Schwarz tests."""
import argparse
from fractions import Fraction
import json
from pathlib import Path
import runpy
from flint import arb
lib=runpy.run_path(str(Path(__file__).with_name("astra-strip-45-check.py")))
rat=lib["rat"]
def test(xs,values,center,radius,order_seed):
    # Leja ordering in the pseudohyperbolic metric limits the amplification of enclosure errors.
    rs=[rat((x-center)/(x+center)/radius) for x in xs]
    take=[i for i,r in enumerate(rs) if abs(r)<rat("0.85")]
    order=[]
    weights=[1.0 for _ in rs]
    if take:
        weights[take[order_seed % len(take)]]=1.01
    while take:
        i=max(take,key=lambda k:weights[k])
        take.remove(i)
        order.append(i)
        for k in take:
            weights[k]*=float(abs((rs[k]-rs[i])/(1-rs[i]*rs[k])))
    vals=[v for v in values]
    for j,i in enumerate(order):
        v=vals[i]
        if abs(v)>1:
            return j,order[:j+1],v
        if not abs(v)<1:
            return
        for k in order[j+1:]:
            numer=vals[k]-v
            denom=(1-vals[k]*v)*(rs[k]-rs[i])/(1-rs[k]*rs[i])
            vals[k]=numer/denom
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--prime",type=int,default=89)
    parser.add_argument("--square",action="store_true")
    a=parser.parse_args()
    sign=lib["square_field_sign"](a.prime) if a.square else lib["paley_sign"](a.prime)
    xs=[Fraction(1,32)*Fraction(5,4)**i for i in range(30)]
    values=[]
    for x in xs:
        # A tiny but positive disk is sufficient for the real mark enclosure.
        _,_,_,_,mark=lib["disks"](sign,x,Fraction(1,1024**6),1,20 if a.square else 8)
        values.append(mark)
    for radius in map(Fraction,["1/2","3/5","2/3","3/4","4/5","17/20","9/10","19/20"]):
        successes=[]
        for center in xs:
            radial=[center*(1-radius)/(1+radius),center*(1+radius)/(1-radius)]
            if radial[0]<Fraction(1,32) or radial[1]>2048:
                continue
            c=rat(Fraction(len(sign)-1,len(sign)))
            r=rat(radius)
            b=rat(center)
            phi=(2*c*b*r/(1-r*r+c*b*(1+r*r))).asin()
            scaled=[(v*arb.pi()/(2*phi)).tanh() for v in values]
            for seed in range(12):
                out=test(xs,scaled,center,radius,seed)
                if out:
                    successes.append((out[0],center,out))
        if successes:
            _,c,(j,order,v)=min(successes,key=lambda t:t[0])
            print(json.dumps(dict(kind="multipoint_marked_obstruction",order=len(sign)*2+1,center=str(c),radius=str(radius),angle_upper=(2*rat(radius).atan()).upper().str(12),real_floors=[str(xs[i]) for i in order],schur_value=v.str(11)),sort_keys=True),flush=True)
            return
    print(json.dumps(dict(kind="schur_scan_inconclusive",order=2*len(sign)+1)),flush=True)
if __name__=="__main__":
    main()
