"""Exact Fourier witnesses for averaged Paley proposals; positivity, not a floor.

Float Picard is only a proposal generator. Replay trusts saved integers only.
All writes have the astra-averaged-positive-36 prefix. Use python -B.
"""
import argparse
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path
import sys

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from smoothing import kernel_action
from theta import paley_sign

PREFIX = 'astra-averaged-positive-36'
SCHEMA = PREFIX + '-exact-Fourier-v1'


def emit(value):
    print(json.dumps(value, sort_keys=True), flush=True)


def save(payload, suffix):
    path = HERE / (PREFIX + suffix)
    data = (json.dumps(payload, sort_keys=True, separators=(',', ':'))+'\n').encode()
    with path.open('wb') as f:
        with gzip.GzipFile(filename='', mode='wb', fileobj=f, mtime=0) as z:
            z.write(data)
    return path


def proposals(prime, depths, tau, kappa):
    sign = paley_sign(prime)
    n = len(sign)
    w = np.full(n, float(tau)/n); w[0] = 1
    v = kernel_action(sign, 2*np.sqrt(w))
    mean_sum = 0.
    sums = [np.zeros(n), np.zeros(n)]
    scale = 2**90
    for t in range(1, max(depths)+1):
        phi = np.hypot(v, 2*np.sqrt(w))
        mean_sum += phi.mean()/2
        for j, side in enumerate((1, -1)):
            raw = (phi+side*v)/2
            sums[j] += (raw-raw.mean()+side*kernel_action(sign, raw))/2
        if t in depths:
            M = mean_sum/t
            payload = dict(schema=SCHEMA, order=prime, steps=t,
                           tau=str(tau), kappa=str(kappa), scale=scale,
                           proposal='float-zero-Picard-average-t1-through-T-then-exact-Fourier-rounding',
                           exact_orbit_claim=False,
                           floating_n_mean_squared=float(n*M*M))
            for j, (key, side) in enumerate((('plus', 1), ('minus', -1))):
                raw = 1+sums[j]/mean_sum
                ft = np.fft.fft(raw).real/n
                half = [scale]+[round(float(ft[k])*scale) if sign[k] == side else 0
                                for k in range(1, n//2+1)]
                payload[key] = half+half[-2:0:-1]
                assert len(payload[key]) == n
            path = save(payload, f'-p{prime}-t{t}-input.json.gz')
            emit(dict(kind='saved_exact_input', exact_input=path.name,
                      order=prime, steps=t, scope='no exact orbit assertion'))
        v = kernel_action(sign, phi)


def replay(path, precision):
    from flint import acb, arb, ctx
    ctx.prec = precision
    data = gzip.decompress(Path(path).read_bytes())
    payload = json.loads(data)
    assert payload['schema'] == SCHEMA
    sign = paley_sign(payload['order'])  # includes trial-division prime check
    n = len(sign); scale = payload['scale']
    assert isinstance(scale, int) and scale > 0
    def ball(x):
        x = Fraction(x)
        return arb(x.numerator)/x.denominator
    kappa = ball(payload['kappa'])
    assert 0 < kappa < arb(1)/2
    records = []; marks = []
    for key, side in [('plus', 1), ('minus', -1)]:
        coeff = payload[key]
        assert len(coeff) == n and all(isinstance(x, int) for x in coeff)
        assert coeff[0] == scale and coeff[1:] == coeff[:0:-1]
        assert all(x == 0 for j, x in enumerate(coeff) if j and sign[j] != side)
        mark = Fraction(sum(coeff), scale); marks.append(mark)
        raw = [x.real/scale for x in acb.dft(coeff)]
        assert raw[0] > 0 and (raw[0]-ball(mark)).contains(0)
        deficit = [arb(0)]
        for x in raw[1:]:
            if x < 2*kappa:
                deficit.append(2*kappa-x)
            elif x > 2*kappa:
                deficit.append(arb(0))
            else:
                raise AssertionError('undecided clipping branch; increase precision')
        a = arb(n-1-side)/(2*n)
        assert a > 0
        mask = [int(j != 0 and sign[j] == side) for j in range(n)]
        assert mask[1:] == mask[:0:-1]
        assert 2*sum(mask) == n-1-side  # exact ell(0)=a, before any interval DFT
        ell = [x.real/n for x in acb.dft(mask)]
        assert (ell[0]-a).contains(0)
        ft = acb.dft(deficit)
        pd = [x.real/n for x in acb.dft([ft[j]*mask[j] for j in range(n)])]
        del ft
        scalar = sum(x*y for x, y in zip(ell, deficit))/a
        out = [x+2*(p-e*scalar) for x,p,e in zip(raw,pd,ell)]
        del pd, ell
        assert (sum(out)/n-1).contains(0)
        assert (out[0]-ball(mark)).contains(0)
        assert all((out[i]-out[-i]).contains(0) for i in range(1, n//2+1))
        energy = sum(x*x for x in deficit)
        assert (sum((y-x-d)**2 for x,y,d in zip(raw,out,deficit))-energy).contains(0)
        outft = acb.dft(out)
        assert (outft[0].real/n-1).contains(0)
        assert all(x.real.contains(0) and x.imag.contains(0)
                   for j,x in enumerate(outft) if j and sign[j] != side)
        del outft
        minimum = min(x.lower() for x in out)
        positive = all(x > 0 for x in out)
        index = min(range(n), key=lambda i: out[i].upper())
        if not positive:
            assert out[index] < 0, 'undecided positivity; increase precision'
        spill = max(arb(0), max((x+d-y).upper()
                               for x,d,y in zip(raw[1:],deficit[1:],out[1:])))
        records.append(dict(side=side, exact_mark=str(mark),
                            active_coordinates=sum(x > 0 for x in deficit),
                            raw_min_lower=str(min(x.lower() for x in raw)),
                            repaired_min_lower=str(minimum),
                            signed_spill_upper=str(spill),
                            deficit_mass_upper=str(sum(deficit).upper()),
                            nonnegative_proved=positive,
                            old_kappa_floor_proved=all(x >= kappa for x in out),
                            witness_index=index, witness_upper=str(out[index].upper()),
                            exact_mean_sector_evenness_mark_proved=True,
                            independent_DFT_constraints_checked=True,
                            reflection_energy_checked=True))
        del raw, deficit, out
    positive = all(r['nonnegative_proved'] for r in records)
    result = dict(kind='arb_positive_completion' if positive else 'arb_negative_trial',
                  order=payload['order'], steps=payload['steps'], tau=payload['tau'],
                  kappa=payload['kappa'], precision_bits=precision,
                  exact_input=Path(path).name,
                  uncompressed_sha256=hashlib.sha256(data).hexdigest(),
                  sides=records, exact_orbit_claim=False,
                  uniform_prime_claim=False)
    if positive:
        rootn = arb(n).sqrt()
        lo, hi = ball(marks[0])/rootn, rootn/ball(marks[1])
        assert lo < hi
        result.update(theta_plus_over_sqrtn_lower=str(lo.lower()),
                      theta_plus_over_sqrtn_upper=str(hi.upper()),
                      theta_plus_lower_exact=str(marks[0]),
                      theta_plus_upper_exact=str(Fraction(n)/marks[1]),
                      scope='strict finite theta bounds from exact Fourier marks; no Picard budget asserted for rounded inputs')
    else:
        result['scope'] = 'specified repair fails on an actual prime; does not exclude another completion or prove eventual failure'
    emit(result)


def endpoint_audit(precision):
    """Check the actual small orbit and evaluate the proved explicit horizon.

    This audits identities; the uniform inequalities are proved in the note.
    It does not simulate the large horizons or assert cancellation there.
    """
    from flint import arb, ctx
    ctx.prec = precision
    F = Fraction
    def ball(x):
        x = F(x)
        return arb(x.numerator)/x.denominator
    n = 6
    sign = [int(x) for x in paley_sign(13)]
    cos = list(map(F, [1, F(1,2), F(-1,2), -1, F(-1,2), F(1,2)]))
    kernel = [sum(sign[j]*cos[i*j % n] for j in range(n))/n for i in range(n)]
    K = [[kernel[(i-j) % n] for j in range(n)] for i in range(n)]
    def mv(v):
        return [sum(ball(k)*x for k,x in zip(row,v)) for row in K]
    def P(v, side):
        mean = sum(v)/n
        return [(x-mean+side*y)/2 for x,y in zip(v,mv(v))]
    w = [arb(1)]+[ball(F(1,120))]*5
    W = sum(w)
    vectors = [[arb(0)]*n]; phis = []; mus = []; energies = [arb(0)]
    for t in range(17):
        phi = [(x*x+4*weight).sqrt() for x,weight in zip(vectors[t],w)]
        phis.append(phi); mus.append(sum(phi)/(2*n))
        vectors.append(mv(phi)); energies.append(sum(x*x for x in vectors[-1]))
    for T in (4, 8, 16):
        for name in ('uniform', 'triangular', 'zero-start'):
            if name == 'uniform':
                alpha = [F(0)]+[F(1,T)]*T
            elif name == 'triangular':
                alpha = [F(0)]+[F(2*(T+1-t),T*(T+1)) for t in range(1,T+1)]
            else:
                alpha = [F(1,T+1)]*(T+1)
            M = sum(ball(a)*mu for a,mu in zip(alpha,mus))
            weighted_C = n*sum(ball(a)*mu*mu for a,mu in zip(alpha,mus))
            telescope = W+sum(ball(alpha[t])*(energies[t]-energies[t+1])/4
                              for t in range(T+1))
            assert (weighted_C-telescope).contains(0)
            assert weighted_C-n*M*M > 0
            budget = W if name == 'zero-start' else W+ball(alpha[1])*energies[1]/4
            assert budget-n*M*M > 0
            for side in (1, -1):
                X = [M]*n
                for t,a in enumerate(alpha):
                    row = [(phi+side*v)/2 for phi,v in zip(phis[t],vectors[t])]
                    projected = P(row, side)
                    X = [x+ball(a)*y for x,y in zip(X,projected)]
                if name != 'zero-start':
                    scalar = sum(ball(alpha[t])*(mus[t]-mus[t-1])/2
                                 for t in range(1,T+1))
                    assert scalar > 0
                    expected = []
                    for i in range(n):
                        positive = sum(ball(alpha[t])*(phis[t][i]+side*vectors[t][i]
                                       +phis[t-1][i]+side*vectors[t-1][i])/4
                                       for t in range(1,T+1))
                        terminal = sum(ball(alpha[t])*(vectors[t+1][i]-vectors[t-1][i])
                                       for t in range(1,T+1))*side/4
                        expected.append(scalar+positive+terminal)
                    assert all((x-y).contains(0) for x,y in zip(X,expected))
            emit(dict(kind='arb_actual_weighted_endpoint_audit', order=13, T=T,
                      weights=name, exact_weights=list(map(str,alpha)),
                      weighted_energy_identity_checked=True,
                      projected_mean_budget_checked=True,
                      endpoint_identity_checked=name != 'zero-start',
                      n_mean_squared=str(n*M*M), budget_upper=str(budget.upper()),
                      scope='actual small orbit; no large-depth arithmetic assertion'))
    # The decreasing-weight simplex vertices are uniform prefixes.
    for T in (3, 4, 16, 128):
        b = F(1,2)  # dimensionless b/D; symbolic proof covers [0,1]
        best = (2+b)/T
        costs = [F(1)]+[(2+b)/k for k in range(2,T+1)]
        assert min(costs) == best
    emit(dict(kind='exact_weight_extreme_point_check', horizons=[3,4,16,128],
              scope='normalization audit; general extremal argument is in the proof'))
    for prime in (9413, 1000033):
        n = (prime-1)//2
        c = ball(F(1,20*n)); W = 1+(n-1)*c
        R = 2*W.sqrt()*arb(prime).sqrt().sqrt()
        A = 2*(prime*W/n).sqrt()
        D = R+A
        b = 2*(1-c.sqrt())*arb(prime).sqrt()/n
        a = 2*c/((D*D+4*c).sqrt()+D)
        threshold = (2*D+b)/(4*a)
        T = int(threshold.upper().floor().unique_fmpz())+1
        margin = a-(2*D+b)/(4*T)
        assert margin > 0
        emit(dict(kind='arb_explicit_all_prime_positivity_horizon', order=prime,
                  tau='1/20', T=T, orbit_coordinate_cap_upper=str(D.upper()),
                  horizon_threshold_upper=str(threshold.upper()),
                  proved_raw_X_min_lower=str(margin.lower()),
                  scope='analytic bound, not an executed orbit; marked Cesaro condition at this horizon is unproved'))


def check_records():
    import ast
    import re
    from flint import arb, ctx
    ctx.prec = 256
    rows = [json.loads(line) for line in (HERE/(PREFIX+'-replay224.jsonl')).read_text().splitlines()]
    assert len(rows) == 4
    expected = {(9413,128): True, (1000033,128): True,
                (9413,64): False, (1000033,64): False}
    table = {9413: ('.0006806378966','.0009350215157','.9776457667269','1.0239190558274'),
             1000033: ('.00004737707156','.0002321502056','.9779871590158','1.0242208463919')}
    for row in rows:
        data = gzip.decompress((HERE/row['exact_input']).read_bytes())
        assert hashlib.sha256(data).hexdigest() == row['uncompressed_sha256']
        payload = json.loads(data)
        assert not payload['exact_orbit_claim'] and not row['exact_orbit_claim']
        positive = expected[row['order'],row['steps']]
        assert all(s['nonnegative_proved'] == positive for s in row['sides'])
        assert all(s['exact_mean_sector_evenness_mark_proved'] and
                   s['independent_DFT_constraints_checked'] and
                   s['reflection_energy_checked'] for s in row['sides'])
        for key, record in zip(('plus','minus'),row['sides']):
            assert Fraction(record['exact_mark']) == Fraction(sum(payload[key]),payload['scale'])
        if positive:
            lo_p, lo_m, lo_theta, hi_theta = table[row['order']]
            assert arb(row['sides'][0]['repaired_min_lower']) > arb(lo_p)
            assert arb(row['sides'][1]['repaired_min_lower']) > arb(lo_m)
            assert arb(row['theta_plus_over_sqrtn_lower']) > arb(lo_theta)
            assert arb(row['theta_plus_over_sqrtn_upper']) < arb(hi_theta)
            assert not any(s['old_kappa_floor_proved'] for s in row['sides'])
        else:
            assert all(arb(s['witness_upper']) < 0 for s in row['sides'])
    older = []
    for suffix in ('-certified-small.jsonl','-certified-large.jsonl'):
        older.extend(json.loads(line) for line in (HERE/(PREFIX+suffix)).read_text().splitlines())
    for row in older:
        new = next(r for r in rows if (r['order'],r['steps']) == (row['order'],row['steps']))
        assert row['uncompressed_sha256'] == new['uncompressed_sha256']
        for a,b in zip(row['sides'],new['sides']):
            assert (a['exact_mark'],a['active_coordinates'],a['witness_index']) == (
                b['exact_mark'],b['active_coordinates'],b['witness_index'])
    audits = [json.loads(line) for line in (HERE/(PREFIX+'-endpoint-audit.jsonl')).read_text().splitlines()]
    assert len(audits) == 12
    assert sum(r['kind']=='arb_actual_weighted_endpoint_audit' for r in audits) == 9
    assert sum(r['kind']=='arb_explicit_all_prime_positivity_horizon' for r in audits) == 2
    for row in audits:
        if row['kind']=='arb_explicit_all_prime_positivity_horizon':
            assert arb(row['proved_raw_X_min_lower']) > 0
    script = HERE/(PREFIX+'.py'); note = HERE/(PREFIX+'.md')
    ast.parse(script.read_text())
    for path in (script,note):
        assert all(line == line.rstrip() for line in path.read_text().splitlines())
        assert not any(ord(c) < 32 and c not in '\n\t\r' for c in path.read_text())
    for link in re.findall(r'\]\(([^)]+)\)',note.read_text()):
        if '://' not in link:
            assert (HERE/link.split('#')[0]).is_file(), link
    files = [p for p in sorted(HERE.glob(PREFIX+'*')) if p.name != PREFIX+'-checks.json']
    emit(dict(kind='round36_prefix_audit', positive_prime_pairs=2,
              negative_prime_trials=2, primary_precision_bits=224,
              exact_inputs=4, weighted_orbit_audits=9, explicit_horizon_evaluations=2,
              table_bounds_checked=True, saved_input_hashes_checked=True,
              static_AST_and_markdown_checks=True,
              uniform_fixed_depth_prime_completion_proved=False,
              growing_horizon_marked_cancellation_proved=False, ETH26_solved=False,
              sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in files}))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--generate', type=int, nargs='*')
    ap.add_argument('--steps', type=int, nargs='+', default=[128])
    ap.add_argument('--tau', default='1/20')
    ap.add_argument('--kappa', default='1/1000')
    ap.add_argument('--replay', nargs='*', default=[])
    ap.add_argument('--precision', type=int, default=192)
    ap.add_argument('--endpoint-audit', action='store_true')
    ap.add_argument('--check-records', action='store_true')
    args = ap.parse_args()
    for p in args.generate or []:
        proposals(p, args.steps, Fraction(args.tau), Fraction(args.kappa))
    for path in args.replay:
        replay(path, args.precision)
    if args.endpoint_audit:
        endpoint_audit(args.precision)
    if args.check_records:
        check_records()


if __name__ == '__main__':
    main()
