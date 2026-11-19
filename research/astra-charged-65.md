# Paired prices near the true face minimum

At **every** actual prime and time where the charged objective varies on the product of the two even optimal faces, generic relative-interior references can approach its minimum with a strictly positive *constant* round-64 cap-normal tangent norm. Thus even at one field and time no finite multiple of the available improvement bounds that norm over all generic references. The other direction of the round-64 comparison remains valid. At $p=97,t=32$, even the best global price assigning each entire original score interval to just one sign loses more than $0.000268914$ in the charged lower bound. The two phenomena have different causes.

There is also a rank-independent uniform bound on the number of intervals that need genuine price splitting for a prescribed additive tolerance. A separate construction chooses one actual whole probability on each face by minimizing two linear functions. This gives a computable upper bound retaining the energy charge. None of these bounds establishes the all-prime late objective.

## Where the cap-normal estimate loses its scale

Use the [true optimal face program](astra-tail-53.md) on the attainable inversion orbits. Evenization preserves both laws and the charge. Let $F=F_+\times F_-$, with the full mass, support, mark and Fourier equations on both sides. Write $Z_s(i)=s\sqrt n\,v_t(i)$, $E_t=\|v_t\|^2$ and $J(q)=M_t(q)-E_t/4$. Sort the union of the two sign scores into distinct values $a_0<\cdots<a_K$. On $(a_k,a_{k+1})$ set $w_k=a_{k+1}-a_k$, $S_{s,k}(q)=q_s\{Z_s>a_k\}$ and $d_k=S_{+,k}-S_{-,k}$. For $0\le\lambda_k\le1$ the global affine lower price is
$$
 L_\lambda(q)=a_0-E_t/4+\sum_k w_k\{S_{-,k}(q)+\lambda_k d_k(q)\},
 \qquad J(q)=\max_\lambda L_\lambda(q).
$$
The [round-64 no-thin-denominator formula](astra-coupling-64.md) gives the dual norm of the derivative of $J$ on a generic overlap chamber. In a tangent basis $S$ with the cap metric $Q=S^\mathsf{T}A^{-2}S$, it is $\sqrt{g^\mathsf{T}Q^{-1}g}$ for the chamber derivative $g$. Both $Q$ and $g$ are independent of the reference inside the chamber. A singleton side can be omitted.

If $J$ is nonconstant, some full-dimensional nonconstant chamber has a minimizing point in its closure. To see this, join a minimizer to a relative-interior point with larger value by a line segment. The closed minimizing set meets the segment in an initial interval. Immediately after its last point the piecewise-affine restriction has strictly positive slope on a nonempty interval. The subdivision by all prefix and survival equalities is finite. A full-dimensional chamber whose closure contains a subinterval right after this last point has nonzero derivative and contains the minimizing point in its closure. This argument also covers segments contained in subdivision walls, by passing to an incident full-dimensional chamber. In that chamber take relative-interior references tending to the minimizing point, avoiding all nonidentical prefix equalities. Their gaps $J(b)-\min_F J$ tend to zero, while their cap-normal norm equals the same strictly positive number. The claim is per actual face and time, with no assumption that nonconstant face objectives occur on infinitely many primes. Whenever they do occur along a sequence, the references may be selected to make the ratio exceed any prescribed finite sequence. This refutes a reference-uniform relative estimate. It leaves an additive estimate for prescribed references open.

There is a second independent loss. The affine function attained at a strict reference can continue downhill *past a survival tie*, even when its cost is minimized using the exact Fourier and positivity constraints. Put $H(\lambda)=\min_{q\in F}L_\lambda(q)$. The two marginal minimizations separate. Finite LP duality gives
$$
 \min_F J=\max_{\lambda\in[0,1]^K}H(\lambda).
$$
For example, introduce epigraph variables for $(d_k)_+$ in the primal LP. The two nonnegative multiplier shares of $w_k$ form the price split. At a primal-dual optimum the split is forced to the attaining side on strict intervals. It is free to mix on tied intervals subject to minimizing $L_\lambda$ at the chosen true pair. Thus using the attainable signs at a nearby reference and then solving both marginal LPs exactly can still give a fixed positive dual deficiency. The finite test below quantifies this even after optimizing over *all* unsplit profiles.

## How many price splits can matter at growing depth?

Fix one minimizing true pair $q^*$ and a maximizing dual price. Only tie indices $I=\{k:d_k(q^*)=0\}$ can have interior prices. Let $r$ be the rank of the derivatives of $d_k|_{\mathrm{aff}(F)}$ for $k\in I$. One can choose an exact optimal price with at most $r$ fractional coordinates. Indeed, keep all strict prices and fix the combined affine derivative of the tie contribution. A vertex of the resulting box section has at most $r$ interior coordinates by the kernel-direction test. This preserves the whole affine function because its value at $q^*$ remains fixed. This rank bound can be much smaller than the total count of ties.

At additive tolerance $h>0$ one may further keep fractional prices only on score intervals of width greater than $h$, with **error at most $h$ simultaneously on every whole pair**. Traverse the intervals in increasing score order and accumulate the weighted rounding error $e=\sum_{k<j} w_k(\lambda'_k-\lambda_k)$. Leave pure and wide prices unchanged. On any remaining interval choose 0 or 1 to minimize the new absolute error. The candidate errors bracket the old error at distance $w_k\le h$ from one another. If they straddle zero the nearer endpoint is within $h/2$. If they are on the same side of zero the nearer endpoint has magnitude at most the previous magnitude. Starting from zero therefore keeps every prefix in $[-h/2,h/2]$. The signed price change integrates this prefix error at the actual scores under plus, minus its integral under minus. Both rows have mass one, proving the bound. The charge cancels exactly in this comparison.

Let $k$ be the number of wide intervals in the whole score grid. Their upper endpoints $z_1<\cdots<z_k$ are pairwise separated by gaps greater than $h$. Each value occurs among the two signed actual score vectors, so $\sum_i z_i^2\le2nE_t$. For $k\ge1$,
$$
 2nE_t\ge \sum_i(z_i-\bar z)^2
   =k^{-1}\sum_{i<j}(z_j-z_i)^2
   \ge h^2 k(k^2-1)/12 .
$$
Start with the rank-sparse exact optimum, then round as above. The resulting paired lower bound is within $h$ of the full minimum, with at most $\min(r,k)$ fractional layers and $k(k^2-1)\le24nE_t/h^2$. In particular for fixed $\epsilon>0$, at every late time the actual $E_t\le4t$ gives $O(1+(n/(\epsilon^2t))^{1/3})$ mixed prices at loss at most $\epsilon t$. Pure choices on the other intervals still have to be found and the two full marginal constraints still have to be priced. Purity refers to the original intervals between consecutive distinct atomic scores. Adding artificial interior knots can implement any fractional price by a switch within that interval.

A second tolerance bound uses the actual feasible probability ranges. On each interval take any valid $l_k\le d_k(q)\le u_k$ for **every** $q\in F$. The exact endpoints can be obtained from the two independent linear programs on each face for that threshold. Put $b_k=w_ku_k(-l_k)/(u_k-l_k)$ when $l_k<0<u_k$ and zero otherwise. Any exact optimal price can be rounded at a mixed layer, with loss at most $b_k$ uniformly on the whole product: rounding down costs at most $w_k\lambda_k u_k$, rounding up costs at most $w_k(1-\lambda_k)(-l_k)$. The lesser is bounded by $b_k$. When the range lies on one side of zero use that side. Applied to the rank-sparse optimum, the pure-profile deficiency is at most the sum of the $r$ largest $b_k$, as well as at most the largest width among its mixed layers by prefix rounding. The lower-certificate complexity bound does not supply a favorable charged value.

## A whole feasible primal pair from the same ranges

Use the fixed price $\lambda_k=u_k/(u_k-l_k)$ at straddling layers and the dominant sign otherwise. For every whole pair,
$$
 0\le J(q)-L_\lambda(q)
    =\sum_k w_k\{(d_k(q))_+-\lambda_kd_k(q)\}
    \le B:=\sum_k b_k .
$$
The upper bound on each straddling layer follows by checking both endpoints. It is the smallest possible worst-case local deficit for a fixed sharing fraction using just that range, since the negative and positive endpoint errors are equal. Choose a whole linear minimizer $q_s^0\in F_s$ independently on each sign using this *one common profile*. Then
$$
 H(\lambda)\le J^{\rm face}\le J(q^0)
    =H(\lambda)+\sum_k w_k\{(d_k(q^0))_+-\lambda_kd_k(q^0)\}
    \le H(\lambda)+B .
$$
This constructs a true feasible pair on the entire integral, including every Fourier constraint. The thresholdwise extremizers used to enclose the ranges need never be combined into a probability. The realized middle sum can sharpen the range-only error, and the energy is already charged once in $H$. In particular a single late time per prime with $H(\lambda)+B\le o(t)$, or with that bound for the measured $J(q^0)$, suffices. No prime-uniform estimate of these quantities is proved here.

## True prime check

At $p=97,t=32$ use the [four exact cyclotomic vertices](astra-charged-61.md), [optimal survival kink](astra-coupling-64.md), and the actual cold scores enclosed with Arb. The checker includes every attainable orbit with its total probability. The four appreciably ambiguous layers give a combined range budget in $(.005024841,.005024842)$, including all other layers with the outward endpoint enlargements. The linear trial chooses the plus vertex $u=0, .151367615<v<.151367616$ and the true minus singleton. Its charged objective lies in $(1.507784872,1.507784873)$. The range-price lower bound lies in $(1.502760031,1.502760032)$. The exact full minimum is in $(1.506178301,1.506178302)$.

There is one tied layer at the full minimizing point $(0,v_*)$, above the score of minus orbit 24. Its survival difference is $d_0+d_u u+d_v v$. Along each of the two paths $u=x, v=v_*+x(\eta-d_u)/d_v$, $0<x\le10^{-8}$, this difference equals $\eta x$, with $\eta=\pm1$. Both paths are in the relative interior. Every other survival inequality is strict, so every attained allocation is forced. The checker minimizes each of those two allocations over all four true vertices. Its rows give outward bounds for the limiting loss even using that exact marginal minimization.

| $\eta$ | True gap divided by $x$ | Cap tangent dual norm | Limit of $J(b)-H(\lambda_b)$ |
|---|---:|---:|---:|
| $-1$ | $(.197897547,.197897548)$ | $(.136379361,.136379362)$ | $(.000268914,.000268915)$ |
| $+1$ | $(.248465616,.248465617)$ | $(.173023443,.173023444)$ | $(.003381649,.003381650)$ |

Globally, a fixed-sign layer can be assigned to its dominating side pointwise. After interval testing at all four vertices, at most five layers remain undecided (including an endpoint-equality case). Enumerating all 32 unsplit profiles there proves that the **best** unsplit lower bound is in $(1.505909386,1.505909387)$, with deficiency in $(.000268914,.000268915)$. Allowing the one optimal fractional layer from round 64 closes that gap exactly. This is a finite obstruction to universally exact unsplit prices. Its magnitude is not a growing-window lower bound.

Reproduce the [four outward records](astra-charged-65-checks.jsonl) with `.venv/bin/python -B research/astra-charged-65-check.py`. The [checker](astra-charged-65-check.py) reuses the exact face geometry and the score ordering, which the prerequisite checker verifies by strict Arb comparisons.

1. On the true late faces bound the chord lower price and its realized remainder for the same independently minimized whole pair. A nonpositive limsup of the least resulting $J(q^0)/t$ through all eligible primes passes. A fixed positive normalized lower bound on this *trial* throughout a late prime subsequence rejects the trial.
2. Seek a full-face lower margin using the slope-rounded dual with $h=\epsilon t$ and the actual marginal LPs. A margin $\eta t$ at every late time on an unbounded prime subsequence rejects the charged-window upper estimate. Conversely, a genuine margin $2\eta t$ must be visible with this split budget at $\epsilon=\eta$. If the best admissible certificate falls below $\eta t$, the larger margin is excluded at the tested time.
