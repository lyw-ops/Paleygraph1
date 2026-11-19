"""Stress the specified averaged repair using one Picard FFT per step.

All output is floating diagnostics, not a positivity certificate or an
exact orbit enclosure. The endpoint formula is the identity audited in
round 35; the small direct-projection comparison checks its implementation.
"""
import argparse
from fractions import Fraction
import gzip
import hashlib
import json
from math import sqrt
from pathlib import Path
import sys

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from smoothing import kernel_action
from theta import paley_sign


def emit(row):
    print(json.dumps(row, sort_keys=True), flush=True)


def run(prime, T, tau, kappa, direct=False, save_input=False):
    sign = paley_sign(prime)
    n = len(sign)
    w = np.full(n, tau/n); w[0] = 1
    phi_previous = 2*np.sqrt(w)
    mu0 = phi_previous.mean()/2
    v_previous = np.zeros(n)
    v1 = kernel_action(sign, phi_previous)
    v = v1.copy()
    sum_phi, sum_v = np.zeros(n), np.zeros(n)
    mean_sum = 0.
    direct_sum = [np.zeros(n), np.zeros(n)] if direct else None
    def P(side, f):
        return (f-f.mean()+side*kernel_action(sign, f))/2
    for t in range(1, T+1):
        phi = np.hypot(v, 2*np.sqrt(w))
        mu = phi.mean()/2
        next_v = kernel_action(sign, phi)
        sum_phi += phi+phi_previous
        sum_v += v+v_previous
        mean_sum += mu
        if direct:
            for j, side in enumerate((1,-1)):
                direct_sum[j] += P(side, (phi+side*v)/2)
        if t == T:
            terminal = v+next_v-v1
            M = mean_sum/T
            e0 = np.zeros(n); e0[0] = 1
            ke0 = kernel_action(sign,e0)
            payload = dict(schema='astra-averaged-positive-36-exact-Fourier-v1',
                           order=prime,steps=T,tau=str(Fraction(str(tau))),
                           kappa=str(Fraction(str(kappa))),scale=2**90,
                           proposal='float-one-FFT-endpoint-average-then-exact-Fourier-rounding',
                           exact_orbit_claim=False,
                           floating_n_mean_squared=float(n*M*M))
            for j, side in enumerate((1,-1)):
                X = (mu-mu0)/(2*T)+(sum_phi+side*(sum_v+terminal))/(4*T)
                raw = X/M
                if save_input:
                    ft = np.fft.rfft(raw).real/n
                    half = [2**90]+[
                        round(float(ft[k])*2**90) if sign[k]==side else 0
                        for k in range(1,n//2+1)]
                    payload['plus' if side==1 else 'minus'] = half+half[-2:0:-1]
                if direct:
                    target = 1+direct_sum[j]/(T*M)
                    discrepancy = float(np.max(np.abs(raw-target)))
                    assert discrepancy < 2e-12
                    emit(dict(kind='floating_direct_projection_comparison',
                              p=prime,T=T,side=side,max_error=discrepancy))
                ell = (e0-1/n+side*ke0)/2
                aa = (n-1-side)/(2*n)
                d = np.maximum(2*kappa-raw,0);d[0]=0
                ld = P(side,d)-ell*(ell@d)/aa
                out = raw+2*ld
                index = int(np.argmin(out))
                gamma = (1+sqrt(prime))/n+(1+sqrt(prime))**2/(2*n*n*aa)
                emit(dict(kind='floating_large_prime_averaged_repair',p=prime,n=n,
                          T=T,tau=tau,kappa=kappa,side=side,
                          n_average_mean_squared=float(n*M*M),
                          sharp_budget=float(w.sum()+(1-sqrt(tau/n))**2*(1-1/n)/T),
                          normalized_mark=float(raw[0]/sqrt(n)),
                          raw_bulk_min=float(raw[1:].min()),
                          active=int(np.count_nonzero(d)),deficit_mass=float(d.sum()),
                          signed_spill=float(np.max(d[1:]-2*ld[1:])),
                          absolute_spill=float(gamma*d.sum()),
                          repaired_min=float(out[index]),minimizer=index,
                          positivity_observed=bool(out[index]>0),
                          mark_preservation_error=float(abs(out[0]-raw[0])),
                          mean_preservation_error=float(abs(out.mean()-1)),
                          scope='floating only; exact input and interval replay needed for any sign claim'))
            if save_input:
                path=Path(__file__).parent/f'endpoint-stress-36-p{prime}-t{T}-input.json.gz'
                data=(json.dumps(payload,sort_keys=True,separators=(',',':'))+'\n').encode()
                with path.open('wb') as file:
                    with gzip.GzipFile(filename='',mode='wb',fileobj=file,mtime=0) as z:
                        z.write(data)
                emit(dict(kind='saved_exact_endpoint_input',p=prime,T=T,
                          exact_input=path.name,uncompressed_sha256=hashlib.sha256(data).hexdigest(),
                          exact_orbit_claim=False))
        v_previous, v = v, next_v
        phi_previous = phi


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--primes',type=int,nargs='+',required=True)
    parser.add_argument('--T',type=int,default=128)
    parser.add_argument('--tau',type=float,default=.05)
    parser.add_argument('--kappa',type=float,default=.001)
    parser.add_argument('--direct',action='store_true')
    parser.add_argument('--save-input',action='store_true')
    args=parser.parse_args()
    assert args.T>0 and args.tau>0 and args.kappa>0
    for p in args.primes:
        run(p,args.T,args.tau,args.kappa,args.direct,args.save_input)
    emit(dict(kind='all_diagnostics_completed',primes=args.primes,T=args.T,
              floating_only=True,
              parent_endpoint_note_sha256=hashlib.sha256(
                  (Path(__file__).parent/'astra-signed-repair-35.md').read_bytes()).hexdigest()))


if __name__=='__main__':
    main()
