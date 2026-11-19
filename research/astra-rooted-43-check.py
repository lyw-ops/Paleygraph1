"""Certified rooted prime witnesses, all-depth Picard completion, and square control."""
import json
from pathlib import Path
import sys

from flint import arb, arb_mat, ctx

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from square_control import square_field_sign

PAIR = {
    1: [506833354356, 256528905547, 427378566913, 657801944980,
        -58790770914, 715077303345, 474048054715, 493166545644,
        294164497715, 824573545296, 515719630118, 183753890265],
    -1: [808099641387, 684446026891, 535249156681, 782460986344,
         650611114774, 317489703184, 923550943411, 334126767684,
         31769115257, 581049665416, 755103678466, 442134581406, 102710011734],
}


def record(**kwargs):
    print(json.dumps(kwargs, sort_keys=True))


def norm(v):
    return sum(x*x for x in v).sqrt()


def minimum_enclosure(values):
    return min(x.lower() for x in values).union(min(x.upper() for x in values))


def maximum_enclosure(values):
    return max(x.lower() for x in values).union(max(x.upper() for x in values))


def prime_case():
    p, n = 101, 50
    assert all(p % k for k in range(2, 11))
    assert all(pow(4, n//k, p) != 1 for k in (2, 5)) and pow(4, n, p) == 1
    residues = {i*i % p for i in range(1, p)}
    signs = [0]+[1 if (1-pow(4, j, p)) % p in residues else -1 for j in range(1, n)]
    cos = [(arb(2*j)/n).cos_pi() for j in range(n)]
    col = [sum(s*cos[i*j % n] for j,s in enumerate(signs))/n for i in range(n)]
    kernel = arb_mat([[col[(i-j) % n] for j in range(n)] for i in range(n)])
    root = arb(n).sqrt()
    marks = {}
    for sigma, weights in PAIR.items():
        support = [j for j in range(1, 1+n//2) if signs[j] == sigma]
        assert len(support) == len(weights)
        row = [1+sum(a*cos[i*j % n] for a,j in zip(weights, support))/10**12
               for i in range(n)]
        assert all(x > arb(9)/10**8 for x in row)
        assert (sum(row)-n).contains(0)
        marks[sigma] = row[0]
        alpha = row[0]/root
        record(kind="strict_mean_one_witness", p=p, sigma=sigma, precision=ctx.prec,
               root_over_sqrt_n=str(alpha), minimum=str(minimum_enclosure(row)))
        if sigma == -1:
            W = 1+(1-arb(1)/n)/4
            assert alpha-W.sqrt() > arb(8)/1000
            # floor((1+sqrt(4*n+1))/2)=7
            assert (row[0]-7)/6 > arb(15)/100
            record(kind="supercritical_witness", p=p, sigma=sigma, tau="1/4",
                   gamma=str(alpha-W.sqrt()), forbidden_absolute_budget_lower=str((row[0]-7)/6))
            scale = (root*W.sqrt()-1)/(row[0]-1)
            assert 0 < scale < 1
            prob = [(1+scale*(x-1))/n for x in row]
            assert all(x > 0 for x in prob)
            assert (root*prob[0]-W.sqrt()).contains(0)
            wcrit = [arb(1)]+[arb(1)/(4*n)]*(n-1)
            cur = [arb(0)]*n
            for t in range(8):
                phi = [(x*x+4*b).sqrt() for x,b in zip(cur,wcrit)]
                cur = list(kernel*arb_mat(n,1,phi))
                if t == 0:
                    first = cur.copy()
            delta = [x-y for x,y in zip(cur,first)]
            scores = [-root*sum(prob[(i-j) % n]*z for i,z in enumerate(delta)) for j in range(n)]
            threshold = arb(7*77)/2000
            assert scores[0] > threshold and all(threshold > x for x in scores[1:])
            other = maximum_enclosure(scores[1:])
            assert arb("0.26738") < other < arb("0.26740")
            assert arb("0.27055") < scores[0] < arb("0.27057")
            record(kind="critical_exceptional_root", p=p, sigma=sigma, tau="1/4", T=7,
                   relative_threshold="77/2000", exceeding_shifts=[0], root_score=str(scores[0]),
                   largest_other_score=str(other), mixing_weight=str(scale))

    tau = arb(1)/20
    width = arb(1)/10**8
    # Change in the full activation in counting L2 at one common input.
    e = 2*(tau.sqrt()-(tau-width).sqrt())
    w = [arb(1)]+[tau/n]*(n-1)
    center = [arb(0)]*n
    radius = arb(0)
    sums = {1: arb(0), -1: arb(0)}
    mean_sum = arb(0)
    dual_bound = n/marks[-1]
    impossible_margins = []
    possible_margins = []

    def evaluate(r):
        phi = [(x*x+4*wi).sqrt() for x,wi in zip(center,w)]
        nxt = list(kernel*arb_mat(n,1,phi))
        avg = sum(phi)/(2*n)
        gerr = (r+e)/(2*root)
        g = avg+arb(0,gerr.upper())
        xs = {}
        for sigma in (1,-1):
            # Kernel translation symmetry gives K A evaluated directly at 0.
            av = [(x+sigma*y)/2 for x,y in zip(phi,center)]
            p0 = (av[0]-sum(av)/n+sigma*sum(x*z for x,z in zip(col,av)))/2
            xs[sigma] = avg+p0+arb(0,(gerr+r+e).upper())
        return g, xs, nxt

    for t in range(301):
        g, xs, nxt = evaluate(radius)
        if t:
            mean_sum += g
            assert mean_sum > 0
            for sigma in (1,-1):
                sums[sigma] += xs[sigma]
                assert sums[sigma] > mean_sum
            if t <= 6:
                gap = sums[1]/mean_sum-dual_bound
                assert gap > arb("0.00047")
                impossible_margins.append(gap)
            else:
                for sigma in (1,-1):
                    gap = marks[sigma]-sums[sigma]/mean_sum
                    assert gap > arb("0.0107")
                    possible_margins.append(gap)
            if t in (6,7,300):
                record(kind="prefix", p=p, T=t, floor_center="1/20", floor_radius="1/100000000",
                       plus_root=str(sums[1]/mean_sum), minus_root=str(sums[-1]/mean_sum))
        if t < 300:
            mids = [x.mid() for x in nxt]
            # r for the actual next input: nonexpansiveness + floor perturbation + rounding.
            radius = (radius+e+norm([x.rad() for x in nxt])).upper()
            center = mids

    stable_radius = arb(1)/1000
    assert radius < stable_radius
    drift = norm([x-z for x,z in zip(nxt,center)])
    # Uniform Lipschitz constant on the entire closed ball at any of the floors.
    derivative_ranges = [
        (abs(x)+stable_radius) / ((abs(x)+stable_radius)**2 + 4*wi).sqrt()
        for x,wi in zip(center,[arb(1)]+[(tau-width)/n]*(n-1))
    ]
    lipschitz = maximum_enclosure(derivative_ranges).upper()
    assert lipschitz < arb("0.98885") and drift < arb("0.00000186")
    assert radius < arb("0.0000135") and e < arb("0.0000000448")
    assert drift+e+lipschitz*stable_radius < stable_radius
    g, xs, _ = evaluate(stable_radius)
    assert g > 0
    for sigma in (1,-1):
        assert g < xs[sigma] < g*marks[sigma]
    record(kind="all_depth_classification", p=p, tau_interval="1/20 +/- 1/100000000",
           impossible="1 <= T <= 6", strict_simultaneous_completion="every integer T >= 7",
           certified_prefix=300, prefix_dual_min_margin=str(minimum_enclosure(impossible_margins)),
           prefix_primal_min_margin=str(minimum_enclosure(possible_margins)), trapping_radius=str(stable_radius),
           final_center_orbit_error=str(radius), lipschitz=str(lipschitz),
           center_drift=str(drift), uniform_activation_change=str(e),
           tail_plus_mark=str(xs[1]/g), tail_minus_mark=str(xs[-1]/g))


def square_case():
    n, b = 24, 6
    signs = square_field_sign(7)
    assert len(signs) == n and all(signs[j] == 1 for j in range(4,n,4))
    # Fourier transform of 1_B/sqrt(b): probability uniform on B^perp.
    assert n//b == 4 and b*b > n
    w = 1+(1-arb(1)/n)/4
    mixing = ((n*w).sqrt()-1)/(b-1)
    assert 0 < mixing < 1
    record(kind="square_cancellation_free", q=49, subgroup_size=b,
           n=n, mean_one_root=b, absolute_forbidden_budget=0,
           critical_floor="1/4", critical_mixing_weight=str(mixing))


if __name__ == "__main__":
    ctx.prec = 256
    prime_case()
    square_case()
