"""Signed transformed-residual certificate using reciprocal source caps."""

import argparse
from fractions import Fraction
import json
from math import sqrt
from pathlib import Path
import sys

import numpy as np
from scipy.optimize import minimize_scalar

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from smoothing import kernel_action
from square_control import square_field_sign
from theta import paley_sign


def root_maximum(linear, radical, constant, endpoint):
    """Float maximum of L*s+J*sqrt(s²-4)+constant on [2,endpoint]."""
    values = [2*linear+constant,
              linear*endpoint+radical*sqrt(max(0., endpoint**2-4))+constant]
    if radical > 0 and linear < -radical:
        s = -2*linear/sqrt(linear**2-radical**2)
        if s <= endpoint:
            values.append(constant-2*sqrt(linear**2-radical**2))
    return max(values)


def suggest_threshold(sign, z, tau):
    n = len(sign)
    c = np.full(n, 4*float(tau)/n)
    c[0] = 4
    phi = np.sqrt(z*z+c)
    b = phi-phi.mean()-kernel_action(sign, z)
    W = 1+(n-1)*float(tau)/n
    a = 2*sqrt(float(tau)/n)
    B = 2*sqrt(n*W)-n*a
    C = (1+sqrt(2*n+1))*sqrt(W/n)
    endpoint = min(C+1/C, B+a)
    h = float(tau)/n
    alpha, beta = (1+h)/2, (1-h)/2
    def objective(t):
        excess = np.maximum(b[1:]-t, 0).sum()
        linear = b[0]-t+alpha*excess
        radical = beta*excess
        constant = t*B-a*(b[0]-t+excess)
        return root_maximum(linear, radical, constant, endpoint)
    if np.ptp(b[1:]) == 0:
        threshold = float(b[1])
    else:
        fit = minimize_scalar(objective, bounds=(float(b[1:].min()),float(b[1:].max())),
                              method='bounded', options={'xatol':1e-15, 'maxiter':200})
        threshold = float(fit.x)
    return threshold, objective(threshold)


def replay(payload):
    from flint import acb, arb, ctx
    ctx.prec = 160
    q, square_root = payload['order'], payload['square_root']
    sign = square_field_sign(square_root) if square_root else paley_sign(q)
    n = len(sign)
    assert q==2*n+1 and (square_root is None or q==square_root*square_root)
    integers = payload['trial_numerators']
    scale = payload['trial_scale']
    assert len(integers)==n and all(isinstance(x,int) for x in integers)
    assert integers[1:] == integers[:0:-1]
    assert isinstance(scale,int) and scale>0
    total = sum(integers)
    z = [arb(n*x-total)/(n*scale) for x in integers]
    tau = Fraction(payload['tau'])
    assert 0<tau<1
    h = tau/n
    def ball(value):
        value=Fraction(value)
        return arb(value.numerator)/value.denominator
    W = ball(1+(n-1)*h)
    floor = 2*ball(h).sqrt()
    c = [arb(4)]+[4*ball(h)]*(n-1)
    phi = [(x*x+cc).sqrt() for x,cc in zip(z,c)]
    transform = acb.dft(z)
    reflected = [x.real for x in acb.dft([int(s)*x for s,x in zip(sign,transform)], inverse=True)]
    mean_phi = sum(phi)/n
    b = [u-mean_phi-k for u,k in zip(phi,reflected)]
    cost_scale = payload['cost_scale']
    assert isinstance(cost_scale,int) and cost_scale>0
    upper_cost = [int((x*cost_scale).upper().ceil().unique_fmpz()) for x in b]
    threshold_num = payload['threshold_numerator']
    assert isinstance(threshold_num,int)
    threshold = Fraction(threshold_num,cost_scale)
    excess = Fraction(sum(max(x-threshold_num,0) for x in upper_cost[1:]),cost_scale)
    b0 = Fraction(upper_cost[0],cost_scale)
    linear = b0-threshold+(1+h)*excess/2
    radical = (1-h)*excess/2
    mass = 2*(n*W).sqrt()-n*floor
    C = (1+arb(q).sqrt())*(W/n).sqrt()
    endpoint = min((C+1/C).upper(), (mass+floor).upper())
    constant = ball(threshold)*mass-floor*ball(b0-threshold+excess)
    endpoint_value = ball(linear)*endpoint+ball(radical)*(endpoint**2-4).sqrt()+constant
    candidates = [2*ball(linear)+constant, endpoint_value]
    if radical>0 and linear < -radical:
        critical = -2*ball(linear)/(ball(linear**2-radical**2)).sqrt()
        if not critical.lower()>endpoint.upper():
            candidates.append(constant-2*ball(linear**2-radical**2).sqrt())
    pairing_upper = max(x.upper() for x in candidates)
    discrepancy = max(arb(0), (2*W.sqrt()*sum(phi)/arb(n).sqrt()-4*W+pairing_upper).upper())
    radius = (1+discrepancy/4).acosh().upper()
    marker = (z[0]/2).asinh()
    floor_error = W.log()/2
    return dict(order=q, square_root=square_root, tau=str(tau), steps=payload['steps'],
                source_cap_upper=str((C+ball(h)/C).upper()),
                root_source_cap_upper=str(endpoint),
                threshold=str(threshold), positive_excess_upper=str(excess),
                transformed_pairing_upper=str(pairing_upper),
                hyperbolic_discrepancy_upper=str(discrepancy),
                marked_hyperbolic_error_upper=str(radius), trial_marker=str(marker),
                normalized_theta_lower=str((marker-radius-floor_error).exp().lower()),
                normalized_theta_upper=str((marker+radius+floor_error).exp().upper()))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('primes',nargs='*',type=int)
    parser.add_argument('--square-roots',nargs='*',type=int,default=[])
    parser.add_argument('--tau',default='1/20')
    parser.add_argument('--steps',nargs='+',type=int,default=[8,32,128,512])
    parser.add_argument('--certify',action='store_true')
    parser.add_argument('--newton',action='store_true',
                        help='propose one trial by safeguarded Newton, rather than a Picard prefix')
    parser.add_argument('--replay-input',type=Path)
    args=parser.parse_args()
    if args.replay_input:
        print(json.dumps(replay(json.loads(args.replay_input.read_text()))),flush=True)
        return
    tau=Fraction(args.tau)
    if not 0<tau<1 or min(args.steps)<1 or not(args.primes or args.square_roots):
        parser.error('provide fields, floor in (0,1), and positive depths')
    cases=[(p,None) for p in args.primes]+[(p*p,p) for p in args.square_roots]
    for q,root in sorted(cases):
        sign=square_field_sign(root) if root else paley_sign(q)
        n=len(sign)
        c=np.full(n,4*float(tau)/n)
        c[0]=4
        def proposals():
            if args.newton:
                from poisson_weights import weighted_iterate
                vector,_,_=weighted_iterate(sign,c/4,tolerance=1e-12,rounds=96)
                yield 0,vector
                return
            vector=np.zeros(n)
            for t in range(1,max(args.steps)+1):
                vector=(vector+kernel_action(sign,np.sqrt(vector*vector+c)))/2
                if t in args.steps:
                    yield t,vector
        for t,vector in proposals():
            vector=(vector+vector[np.r_[0,np.arange(n-1,0,-1)]])/2
            scale=2**60
            integers=[round(float(x)*scale) for x in vector]
            centered=np.array(integers,dtype=float)/scale
            centered-=centered.mean()
            threshold,tail=suggest_threshold(sign,centered,tau)
            cost_scale=10**14
            payload=dict(order=q,square_root=root,tau=str(tau),steps=t,trial_scale=scale,
                         trial_numerators=integers,cost_scale=cost_scale,
                         threshold_numerator=round(threshold*cost_scale))
            if args.newton:
                payload['proposal']='safeguarded Newton, not an actual Picard prefix'
            if args.certify:
                path=Path(__file__).with_name(f'source-tail-28-q{q}-tau{tau.numerator}_{tau.denominator}-t{t}-input.json')
                path.write_text(json.dumps(payload)+'\n')
                result=replay(payload)
                result['certificate_input']=path.name
                if args.newton:
                    result['proposal']=payload['proposal']
            else:
                phi=np.sqrt(centered*centered+c)
                W=1+(n-1)*float(tau)/n
                discrepancy=max(0.,2*sqrt(W)*phi.sum()/sqrt(n)-4*W+tail)
                result=dict(order=q,square_root=root,tau=str(tau),steps=t,
                            transformed_pairing_trial_bound=tail,
                            hyperbolic_discrepancy_trial_bound=discrepancy,
                            marked_hyperbolic_error_trial_bound=float(np.arccosh(1+discrepancy/4)),
                            residual_norm=float(np.linalg.norm(centered-kernel_action(sign,phi))),
                            status='floating-point diagnostic; use --certify for rigorous bounds')
            print(json.dumps(result),flush=True)


if __name__=='__main__':
    main()
