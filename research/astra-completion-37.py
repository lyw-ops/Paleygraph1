"""Certify a second pinned repair of round 36's saved Fourier input at p=7340033."""
import gc
import gzip
import hashlib
import json
from fractions import Fraction
from pathlib import Path
import sys

from flint import acb, arb, ctx

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from theta import paley_sign

INPUT = HERE / 'endpoint-stress-36-p7340033-t128-input.json.gz'
EXPECTED = 'f1e99a29831f9bf717d167ae31dcf9bf4c5248e17842f72042c72f7b3b47c24e'


def ball(rational):
    rational = Fraction(rational)
    return arb(rational.numerator) / rational.denominator


def main():
    ctx.prec = 128
    contents = gzip.decompress(INPUT.read_bytes())
    assert hashlib.sha256(contents).hexdigest() == EXPECTED
    trial = json.loads(contents)
    del contents
    order = trial['order']
    assert order == 7340033 and trial['steps'] == 128
    sign = paley_sign(order)
    n = len(sign)
    scale = trial['scale']
    assert isinstance(scale, int) and scale > 0
    key = 'minus'
    coefficients = trial.pop(key)
    plus_mark = Fraction(sum(trial.pop('plus')), scale)
    minus_mark = Fraction(sum(coefficients), scale)
    assert len(coefficients) == n and coefficients[0] == scale
    assert coefficients[1:] == coefficients[:0:-1]
    assert all(isinstance(x, int) and (i == 0 or x == 0 or sign[i] == -1)
               for i, x in enumerate(coefficients))
    print('Computing exact saved-row DFT', file=sys.stderr, flush=True)
    raw = [item.real / scale for item in acb.dft(coefficients)]
    del coefficients
    gc.collect()
    first_cut = 2 * ball(trial['kappa'])
    assert trial['kappa'] == '1/1000' and raw[0] > first_cut
    deficit = [arb(0)]
    for x in raw[1:]:
        if x < first_cut:
            deficit.append(first_cut - x)
        else:
            assert x > first_cut
            deficit.append(arb(0))
    mask = [int(i != 0 and sign[i] == -1) for i in range(n)]
    assert mask[1:] == mask[:0:-1] and sum(mask) * 2 == n
    print('Computing the first pinned reflection', file=sys.stderr, flush=True)
    ell = [item.real / n for item in acb.dft(mask)]
    a = ball(Fraction(1, 2))
    assert (ell[0] - a).contains(0)
    freq = acb.dft(deficit)
    del deficit
    for i, keep in enumerate(mask):
        if not keep:
            freq[i] = acb(0)
    del mask
    pd = [item.real / n for item in acb.dft(freq)]
    del freq
    scalar = pd[0] / a
    # d is even, so the same DFT twice implements an inverse on its support.
    threshold = ball(Fraction(1, 5000))
    mass = arb(0)
    active = 0
    lowest = arb(1)
    lowest_index = None
    for i in range(1, n):
        y = raw[i] + 2 * (pd[i] - ell[i] * scalar)
        if y < threshold:
            active += 1
            mass += threshold - y
            if y.upper() < lowest.upper():
                lowest = y
                lowest_index = i
        else:
            assert y > threshold
    assert lowest < 0
    b = (1 + arb(order).sqrt()) / (2 * n)
    gamma = 2 * b + 2 * b**2 / a
    second_floor = threshold - gamma * mass
    assert second_floor > 0 and minus_mark > 1
    # The accepted plus certificate is tied to the same exact input and mark.
    plus_record = json.loads((HERE / 'endpoint-stress-36-negative-certified.jsonl').read_text())
    assert plus_record['uncompressed_sha256'] == EXPECTED
    plus = plus_record['sides'][0]
    assert plus['side'] == 1 and plus['nonnegative_proved']
    assert Fraction(plus['exact_mark']) == plus_mark
    assert arb(plus['repaired_min_lower']) > 0
    root = arb(n).sqrt()
    print(json.dumps(dict(kind='arb_saved_input_second_pinned_repair',
                          order=order, steps=trial['steps'], precision_bits=ctx.prec,
                          input_sha256=EXPECTED, first_minus_min_witness_index=lowest_index,
                          first_minus_witness_upper=str(lowest.upper()),
                          second_minus_clip_threshold='1/5000',
                          second_minus_active=active, second_minus_deficit_mass_upper=str(mass.upper()),
                          pinned_spill_coefficient_upper=str(gamma.upper()),
                          second_minus_bulk_min_lower=str(second_floor.lower()),
                          first_plus_min_lower=plus['repaired_min_lower'],
                          plus_certificate_source='endpoint-stress-36-negative-certified.jsonl',
                          plus_mark=str(plus_mark), minus_mark=str(minus_mark),
                          theta_lower_exact=str(plus_mark), theta_upper_exact=str(Fraction(n)/minus_mark),
                          normalized_lower=str((ball(plus_mark)/root).lower()),
                          normalized_upper=str((root/ball(minus_mark)).upper()),
                          exact_orbit_claim=False), sort_keys=True))


if __name__ == '__main__':
    main()
