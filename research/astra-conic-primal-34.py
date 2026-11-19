"""Source-free Picard proposals and marked-preserving Paley floor repair.

All writes have astra-conic-primal-34 prefix. No stationary solver is used.
Saved rational Fourier inputs, not floating iteration histories, are trusted
by Arb replay. The replay independently evaluates the clipped reflection.
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

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from smoothing import kernel_action
from theta import paley_sign
from square_control import square_field_sign


def emit(row):
    print(json.dumps(row, sort_keys=True), flush=True)


def pathcheck(path):
    path = Path(path)
    assert path.parent.resolve() == HERE
    assert path.name.startswith('astra-conic-primal-34')
    return path


def signs(order, root):
    return square_field_sign(root) if root else paley_sign(order)


def projector(sign, side, x):
    return (x - np.mean(x) + side*kernel_action(sign, x))/2


def raw_pair(sign, vector, w):
    total = np.hypot(vector, 2*np.sqrt(w))
    high = (total+np.abs(vector))/2
    a = np.where(vector >= 0, high, w/high)
    b = np.where(vector >= 0, w/high, high)
    return [1+projector(sign, side, raw)/raw.mean()
            for side, raw in [(1,a),(-1,b)]]


def repair(sign, side, raw, kappa):
    n = len(sign)
    e0 = np.zeros(n); e0[0] = 1
    ell = projector(sign, side, e0)
    a = (n-1-side)/(2*n)
    assert abs(ell[0]-a) < 1e-12
    deficit = np.maximum(2*kappa-raw, 0); deficit[0] = 0
    ld = projector(sign, side, deficit)-ell*(ell@deficit)/a
    clipped = raw+deficit
    out = raw+2*ld
    gamma = (1+sqrt(2*n+1))/n + (1+sqrt(2*n+1))**2/(2*n*n*a)
    return out, clipped, deficit, gamma


def payload_for(sign, pair, order, root, tau, kappa, steps):
    n = len(sign); scale = 2**90
    payload = dict(schema='astra-conic-primal-34-clipped-reflection-v1',
                   order=order, square_root=root, tau=str(tau),
                   kappa=str(kappa), steps=steps, scale=scale,
                   proposal='Picard-from-zero-then-exact-Fourier-rounding')
    for side, raw, key in [(1,pair[0],'plus'),(-1,pair[1],'minus')]:
        ft = np.fft.fft(raw).real/n
        half = [scale]+[round(float(ft[j])*scale) if sign[j] == side else 0
                        for j in range(1,n//2+1)]
        payload[key] = half+(half[-2:0:-1] if n%2 == 0 else half[:0:-1])
    return payload


def save(payload, path):
    path = pathcheck(path)
    data = (json.dumps(payload, sort_keys=True, separators=(',',':'))+'\n').encode()
    with path.open('wb') as f:
        with gzip.GzipFile(filename='', mode='wb', fileobj=f, mtime=0) as z:
            z.write(data)
    return hashlib.sha256(data).hexdigest()


def exact_audit():
    """Independent rational matrix audit at the actual field F_13."""
    F=Fraction; n=6
    sign=[int(x) for x in paley_sign(13)]
    cosine=list(map(F,[1,F(1,2),F(-1,2),-1,F(-1,2),F(1,2)]))
    kernel=[sum(sign[j]*cosine[(i*j)%n] for j in range(n))/n for i in range(n)]
    K=[[kernel[(i-j)%n] for j in range(n)] for i in range(n)]
    I=[[F(i==j) for j in range(n)] for i in range(n)]
    def mm(A,B):
        return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    assert mm(K,K)==[[I[i][j]-F(1,n) for j in range(n)] for i in range(n)]
    for side in [1,-1]:
        P=[[(I[i][j]-F(1,n)+side*K[i][j])/2 for j in range(n)] for i in range(n)]
        a=F(n-1-side,2*n);ell=[P[i][0] for i in range(n)]
        assert ell[0]==a and mm(P,P)==P
        L=[[P[i][j]-ell[i]*ell[j]/a for j in range(n)] for i in range(n)]
        R=[[2*L[i][j]-I[i][j] for j in range(n)] for i in range(n)]
        assert mm(L,L)==L and mm(R,R)==I
        assert all(sum(row)==0 and row[0]==0 for row in L)
        assert all(R[i][j]==side*K[i][j]-F(1,n)-2*ell[i]*ell[j]/a
                   for i in range(n) for j in range(n))
        emit(dict(kind='exact_actual_Paley_reflection_identity',order=13,side=side,
                  rank_diagonal=str(a),kernel_first_row=[str(x) for x in K[0]],
                  projection_idempotence=True,reflection_isometry=True,
                  mean_and_mark_preserved=True,signed_scatter_identity=True))


def check_records():
    from flint import arb, ctx
    ctx.prec=256
    rows=[json.loads(x) for x in (HERE/'astra-conic-primal-34-replay224.jsonl').read_text().splitlines()]
    assert len(rows)==6
    upper={(9413,40):'.735334',(9413,44):'.313868',(9413,48):'.131884',
           (1000033,40):'.987402',(1000033,48):'.212819'}
    positive=0;rejected=0
    for row in rows:
        data=gzip.decompress((HERE/row['exact_input']).read_bytes())
        assert hashlib.sha256(data).hexdigest()==row['uncompressed_sha256']
        if row['kind']=='arb_mark_preserving_conic_primal':
            positive+=1
            assert arb(row['d_over_kappa_upper']) < arb(upper[row['order'],row['steps']])
            assert all(s['floor_proved'] and arb(s['repaired_min_lower']) > arb('0.001') for s in row['sides'])
            if row['order']==1000033 and row['steps']==40:
                assert all(arb(s['actual_negative_spill_upper']) < arb('.001') for s in row['sides'])
                assert not any(s['coherence_condition_proved'] for s in row['sides'])
        else:
            rejected+=1
            assert row['kind']=='arb_repair_rejected' and row['order']==151321
            assert arb(row['sides'][1]['test_value_upper']) < arb('-.37428998128')
    assert positive==5 and rejected==1
    exact=[json.loads(x) for x in (HERE/'astra-conic-primal-34-exact.jsonl').read_text().splitlines()]
    assert len(exact)==2 and all(x['reflection_isometry'] for x in exact)
    diagnostics=[]
    for filename in ['astra-conic-primal-34-diagnostics.jsonl','astra-conic-primal-34-large-diagnostics.jsonl']:
        diagnostics.extend(json.loads(x) for x in (HERE/filename).read_text().splitlines())
    assert len(diagnostics)==74
    files=[HERE/'astra-conic-primal-34.md',HERE/'astra-conic-primal-34.py',
           HERE/'astra-conic-primal-34-replay224.jsonl',HERE/'astra-conic-primal-34-exact.jsonl']
    files+=sorted(HERE.glob('astra-conic-primal-34-*-input.json.gz'))
    emit(dict(kind='round34_record_audit',positive_certificates=positive,
              rigorously_rejected_trials=rejected,exact_matrix_audits=len(exact),
              floating_diagnostic_rows=len(diagnostics),
              table_bounds_checked=True,input_hashes_checked=True,
              uniform_prime_primal_proof=False,HR_proved=False,ETH26_solved=False,
              sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in files}))


def replay(path, precision):
    from flint import acb, arb, ctx
    ctx.prec = precision
    data = gzip.decompress(Path(path).read_bytes())
    payload = json.loads(data)
    assert payload['schema'] == 'astra-conic-primal-34-clipped-reflection-v1'
    sign = signs(payload['order'], payload['square_root'])
    n = len(sign); scale = payload['scale']
    assert isinstance(scale,int) and scale > 0
    def ball(value):
        r = Fraction(value)
        return arb(r.numerator)/r.denominator
    tau, kappa = ball(payload['tau']), ball(payload['kappa'])
    assert tau > 0 and 0 < kappa < arb(1)/2
    W = 1+(n-1)*tau/n
    m = [n/W]+[tau/W]*(n-1)
    pairs=[]; clipped_pairs=[]; norms=[]; records=[]
    for key,side in [('plus',1),('minus',-1)]:
        coeff=payload[key]
        assert len(coeff)==n and all(isinstance(x,int) for x in coeff)
        assert coeff[0]==scale and coeff[1:]==coeff[:0:-1]
        assert all(x==0 for j,x in enumerate(coeff) if j and sign[j]!=side)
        raw=[x.real/scale for x in acb.dft(coeff)]
        assert raw[0] >= kappa
        # Separate every branch by intervals: there are no guessed active sets.
        deficit=[arb(0)]
        for x in raw[1:]:
            if x < 2*kappa:
                deficit.append(2*kappa-x)
            elif x >= 2*kappa:
                deficit.append(arb(0))
            else:
                raise AssertionError('raise precision to decide clipping branch')
        a=arb(n-1-side)/(2*n)
        assert a > 0
        mask=[int(j != 0 and sign[j]==side) for j in range(n)]
        ell=[x.real/n for x in acb.dft(mask)]
        assert (ell[0]-a).contains(0)
        # d is even. Applying the unnormalized DFT twice yields n*d.
        ft=acb.dft(deficit)
        pd=[x.real/n for x in acb.dft([ft[j]*mask[j] for j in range(n)])]
        scalar=sum(x*y for x,y in zip(ell,deficit))/a
        ld=[x-y*scalar for x,y in zip(pd,ell)]
        out=[x+2*y for x,y in zip(raw,ld)]
        clipped=[x+y for x,y in zip(raw,deficit)]
        gamma=(1+arb(2*n+1).sqrt())/n+(1+arb(2*n+1).sqrt())**2/(2*n*n*a)
        mass=sum(deficit); energy=sum(x*x for x in deficit)
        floor_proved=all(x >= kappa for x in out)
        failed_index=min(range(n),key=lambda i: out[i].upper())
        if not floor_proved:
            assert out[failed_index] < kappa, 'raise precision to decide floor'
        assert (sum(out)/n-1).contains(0)
        assert (out[0]-raw[0]).contains(0)
        reflection_energy=sum((x-y)**2 for x,y in zip(out,clipped))
        assert (reflection_energy-energy).contains(0)
        # Independent Fourier-support check, in addition to the symbolic proof.
        outft=acb.dft(out)
        assert all(x.real.contains(0) and x.imag.contains(0)
                   for j,x in enumerate(outft) if j and sign[j]!=side)
        pairs.append(out); clipped_pairs.append(clipped); norms.append(energy.sqrt())
        records.append(dict(side=side,
                            active_coordinates=sum(x > 0 for x in deficit),
                            raw_bulk_min_lower=str(min(x.lower() for x in raw[1:])),
                            deficit_mass_upper=str(mass.upper()),
                            deficit_energy_upper=str(energy.upper()),
                            coherence_spill_upper=str((gamma*mass).upper()),
                            coherence_condition_proved=bool(gamma*mass <= kappa),
                            actual_negative_spill_upper=str(max(arb(0),max((y-x).upper() for x,y in zip(out[1:],clipped[1:])))),
                            repaired_min_lower=str(min(x.lower() for x in out)),
                            floor_proved=floor_proved,
                            test_index=failed_index,
                            test_value_upper=str(out[failed_index].upper()),
                            mark_preserved=True, reflection_isometry_checked=True))
    if not all(row['floor_proved'] for row in records):
        emit(dict(kind='arb_repair_rejected',order=payload['order'],
                  square_root=payload['square_root'],tau=payload['tau'],
                  kappa=payload['kappa'],steps=payload['steps'],precision_bits=precision,
                  exact_input=Path(path).name,uncompressed_sha256=hashlib.sha256(data).hexdigest(),
                  sides=records,scope='this reflection trial fails; no conic lower bound'))
        return
    gap=sum((mm.sqrt()-(p*q).sqrt())**2 for mm,p,q in zip(m,*pairs))/n
    clipgap=sum((mm.sqrt()-(p*q).sqrt())**2 for mm,p,q in zip(m,*clipped_pairs))/n
    bulkcap=max(x.upper() for pair in pairs+clipped_pairs for x in pair[1:])
    error=(bulkcap/(kappa*n)).sqrt()*sum(norms)/(1+arb(2).sqrt())
    bound=(clipgap.sqrt()+error)**2
    emit(dict(kind='arb_mark_preserving_conic_primal',order=payload['order'],
              square_root=payload['square_root'],tau=payload['tau'],
              kappa=payload['kappa'],steps=payload['steps'],precision_bits=precision,
              exact_input=Path(path).name,uncompressed_sha256=hashlib.sha256(data).hexdigest(),
              strict_floor_proved=True,exact_mean_and_sector_proved=True,
              d_upper=str(gap.upper()),d_over_kappa_upper=str((gap/kappa).upper()),
              clipped_gap_upper=str(clipgap.upper()),
              lemma_gap_upper=str(bound.upper()),
              lemma_repair_distance_upper=str(error.upper()),
              bulk_cap_upper=str(bulkcap),sides=records))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--primes',type=int,nargs='*',default=[])
    parser.add_argument('--square-roots',type=int,nargs='*',default=[])
    parser.add_argument('--tau',default='1/20')
    parser.add_argument('--kappa',nargs='+',default=['1/1000'])
    parser.add_argument('--steps',type=int,nargs='+',default=[24,32,40,48,64,96,128])
    parser.add_argument('--save',action='store_true')
    parser.add_argument('--save-rejected',action='store_true')
    parser.add_argument('--precision',type=int,default=160)
    parser.add_argument('--replay',type=Path)
    parser.add_argument('--exact',action='store_true')
    parser.add_argument('--check-records',action='store_true')
    args=parser.parse_args()
    if args.exact:
        exact_audit();return
    if args.check_records:
        check_records();return
    if args.replay:
        replay(args.replay,args.precision);return
    tau=Fraction(args.tau)
    assert tau>0 and min(args.steps)>0
    for order,root in [(p,None) for p in args.primes]+[(h*h,h) for h in args.square_roots]:
        sign=signs(order,root);n=len(sign)
        w=np.full(n,float(tau)/n);w[0]=1
        m=w*n/(1+(n-1)*float(tau)/n)
        vector=np.zeros(n)
        for step in range(1,max(args.steps)+1):
            vector=kernel_action(sign,np.hypot(vector,2*np.sqrt(w)))
            if step not in args.steps:continue
            raw=raw_pair(sign,vector,w)
            for kvalue in args.kappa:
                kr=Fraction(kvalue);k=float(kr)
                assert 0<k<.5
                allparts=[repair(sign,side,x,k) for side,x in [(1,raw[0]),(-1,raw[1])]]
                out=[x[0] for x in allparts];clip=[x[1] for x in allparts]
                deficits=[x[2] for x in allparts]
                spills=[x[3]*float(x[2].sum()) for x in allparts]
                good=max(spills)<k and min(x[0] for x in raw)>=k
                positive=min(x.min() for x in out)>0
                floor_good=min(x.min() for x in out)>=k
                clipgap=float(np.mean((np.sqrt(m)-np.sqrt(clip[0]*clip[1]))**2))
                gap=float(np.mean((np.sqrt(m)-np.sqrt(out[0]*out[1]))**2)) if positive else None
                cap=max(float(x[1:].max()) for x in out+clip)
                error=sqrt(cap/(k*n))*sum(float(np.linalg.norm(d)) for d in deficits)/(1+sqrt(2))
                constant=[]
                for x in raw:
                    shift=max(0.,(k-float(x.min()))/(1-k))
                    constant.append((x+shift)/(1+shift))
                constantgap=float(np.mean((np.sqrt(m)-np.sqrt(constant[0]*constant[1]))**2))
                if floor_good:
                    assert gap <= (sqrt(clipgap)+error)**2+1e-10
                emit(dict(kind='floating_source_free_repair',order=order,square_root=root,
                          tau=str(tau),kappa=str(kr),steps=step,
                          raw_bulk_min=[float(x[1:].min()) for x in raw],
                          active_counts=[int(np.sum(d>0)) for d in deficits],
                          deficit_mass=[float(d.sum()) for d in deficits],
                          spill_over_kappa=[x/k for x in spills],
                          theorem_hypotheses=bool(good),
                          direct_floor_hypotheses=bool(floor_good),
                          negative_spill_over_kappa=[float(np.max(c[1:]-o[1:]))/k for o,c in zip(out,clip)],
                          repaired_min=[float(x.min()) for x in out],
                          clipped_gap=clipgap, repaired_gap=gap,
                          repaired_slope=gap/k if gap is not None else None,
                          lemma_gap=(sqrt(clipgap)+error)**2 if floor_good else None,
                          constant_repair_slope=constantgap/k,
                          bulk_cap=cap))
                if (args.save and floor_good) or (args.save_rejected and not floor_good):
                    stem=f'astra-conic-primal-34-q{order}-t{step}-tau{tau.numerator}_{tau.denominator}-k{kr.numerator}_{kr.denominator}-input.json.gz'
                    path=HERE/stem
                    save(payload_for(sign,raw,order,root,tau,kr,step),path)
                    replay(path,args.precision)


if __name__=='__main__':
    main()
