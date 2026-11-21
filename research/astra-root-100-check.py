"""Replay the true head and certify a projected law and all clique upper bounds."""
from pathlib import Path
import json
import runpy

from flint import acb, arb, arb_mat, ctx, fmpq
import numpy as np
from scipy.optimize import linprog

root = Path(__file__).parent
previous = runpy.run_path(str(root / "astra-quotient-99-check.py"))
base = previous["base"]
ctx.prec = 384


def replay():
    record = previous["replay"]()
    head = record["hot_above_6_over_5"]
    b = 48
    signs = base["paley_sign"](769)
    allowed = {k for k in range(b) if k == 0 or signs[8*k] == 1}
    cosine = [arb.cos_pi_fmpq(fmpq(2*j, b)) for j in range(b)]
    waves = [acb(cosine[j], arb.sin_pi_fmpq(fmpq(2*j,b))) for j in range(b)]
    kernel = [sum(cosine[r*k % b] for k in allowed)/b for r in range(b)]
    gram = arb_mat([[kernel[(r-t) % b] for t in head] for r in head])
    background = arb(27)/100
    coeff = gram.solve(arb_mat([[kernel[r]+background] for r in head]))
    mass = [kernel[r]+background-sum(kernel[(r-t) % b]*coeff[j,0]
                                      for j,t in enumerate(head)) for r in range(b)]
    assert all(mass[r].contains(0) for r in head)
    assert all(mass[r] > 0 for r in range(b) if r not in head)
    trial = mass[0]/sum(mass)
    assert trial > arb(36)/1000

    def cliques(D, candidates):
        yield D
        for i, z in enumerate(candidates):
            yield from cliques(D+[z], [v for v in candidates[i+1:] if (v-z) % b in allowed])

    count = 0
    largest = arb(0)
    for D in cliques([0], sorted(allowed-{0})):
        # Squared distance of ones to the span of the head waves gives the
        # clique optimum. A rounded candidate in that span certifies an upper.
        mat = np.exp(2j*np.pi*np.outer(D, head)/b)
        proposal = np.linalg.lstsq(mat, np.ones(len(D)), rcond=1e-10)[0]
        a = [acb(arb(round(v.real*10**10))/10**10, arb(round(v.imag*10**10))/10**10)
             for v in proposal]
        residuals = [1-sum(c*waves[z*r % b] for c,r in zip(a,head)) for z in D]
        value = sum(v.real*v.real+v.imag*v.imag for v in residuals)/b
        assert value < arb(22777)/10**6
        largest = largest.max(value)
        count += 1
    assert count == 828

    # With a symmetric head and inversion-invariant forbidden set, symmetrize
    # any law. Each variable below is total mass on an inversion orbit.
    reps = [j for j in range(b//2+1) if j not in head]
    forbidden = [j for j in range(1,b//2+1) if j not in allowed]
    rows = [[arb(1)]*len(reps)] + [[cosine[k*r % b] for r in reps] for k in forbidden]
    rhs = [1]+[0]*len(forbidden)
    lp = linprog([-int(r==0) for r in reps], A_eq=np.asarray(rows,dtype=float), b_eq=rhs)
    assert lp.success
    cols = [i for i,x in enumerate(lp.x) if x>1e-8]
    mat = arb_mat([[row[i] for i in cols] for row in rows])
    solution = mat.solve(arb_mat([[d] for d in rhs]))
    assert all(solution[i,0]>0 for i in range(len(cols)))
    assert reps[cols[0]] == 0
    floor = solution[0,0]
    assert floor > arb(76455)/10**6
    # The two maximal proper subgroups have orders 16 and 24. Restriction
    # folds every forbidden position into a mandatory Fourier zero.
    folded = {d: sorted(set(range(d)) - {k % d for k in range(b) if k not in allowed})
              for d in (16, 24)}
    assert folded == {16:[0,8], 24:[0,4,5,8,10,14,16,19,20]}
    delta = (2*cosine[2]/arb(3).sqrt()-1)/(2*cosine[10])
    assert abs(delta) < 1/arb(3).sqrt()
    return dict(prime=769, horizon=16, quotient_order=b, physical_erasure="2+2j",
                cutoff="6/5", actual_head=head, precision=ctx.prec,
                projected_law_background="27/100",
                projected_law_root_units_1e_minus_9=base["enclose"](trial),
                rooted_cliques=count, remaining_folded_modes=folded,
                largest_clique_upper_certificate_units_1e_minus_9=base["enclose"](largest),
                positive_basic_root_units_1e_minus_9=base["enclose"](floor),
                positive_basic_root_orbits=[reps[i] for i in cols],
                all_law_upper=record["four_head_all_law_root_strict_upper"])


if __name__ == "__main__":
    print(json.dumps(replay(),sort_keys=True))
