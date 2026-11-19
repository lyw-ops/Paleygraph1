# The exact opposite-law price of exposed Schur heads

A single genuine opposite probability attains the best possible root-residual price for any fixed exposed head set. That price equals the largest mass any optimizer on the actual marked face can put on the same set. Restricting the law to mixtures of translates of one prescribed opposite optimizer can cost more. On the four actual [round-80 masks](astra-surviving-80.md), even after crediting the clipping floor, this restriction costs between 1.85 and 2.16 times the exact clipped mass. At the prime 97, another genuine optimizer on the same marked face forces a surcharge exceeding 0.07712 even when *all* genuine opposite laws are allowed. There is also an explicit prime-uniform lower bound for the price in a hypothetical supercritical high-density branch.

## Exact price and an optimal genuine law

Write \(V_s\) for the real span of the constant and allowed side-\(s\) Fourier modes on \(G\). The feasible laws are the nonnegative unit-mass elements of \(V_s\). Fix the optimal root \(a=q_0\) and write \(\mathcal Q_a\) for this entire marked primary face. Let \(r^*\) be any opposite optimum at zero, so \(nar^*_0=1\). If \(D_j\ge0\) is a fixed demand on the bulk, the following identity holds, with an attained minimum:
\[
 \min_{U\in V_{-s},\ U\ge0,\ U_j\ge D_j\ (j\ne0)}
       (\overline U-aU_0)
   =\max_{q'\in\mathcal Q_a}\sum_{j\ne0}q'_jD_j.                  \tag{1}
\]
Here \(\overline U=n^{-1}\sum U\). For a bulk indicator \(D=1_F\) with nonempty \(F\), normalizing any such \(U\) gives a genuine opposite feasible probability \(w=U/(n\overline U)\) and a level \(t=1/\overline U\). Its cost is \((1-na w_0)/t\), with \(nw_j\ge t\) on \(F\). Conversely, any such law and level give \(U=nw/t\). Translations preserve feasibility, and mixtures of arbitrary genuine translated laws are again genuine. Thus (1) computes their full capacity with a single law.

Indeed the bulk variables \(y_j=q'_j\ge0\), with the root fixed, obey precisely \(\sum_{j\ne0}y_jU_j=\overline U-aU_0\) for every real \(U\in V_{-s}\). The constant equation normalizes the mass and all the other equations impose the opposite Fourier zeros. Finite LP duality on these equalities gives (1) first with \(U_0\) unrestricted. Add \(\lambda r^*\), \(\lambda\ge0\), to make the root nonnegative. This preserves the optimal cost because \(\overline{r^*}-ar^*_0=0\); every bulk inequality survives. If \(F\) is exposed, \(r^*_j=0\) there. The same operation makes the normalized law arbitrarily close to the opposite optimum while preserving its price and all relative levels on \(F\). Root proximity alone consequently gives no gain in this ratio. This positivity repair upgrades the [signed spanning-family construction](translated-caps-71.md) to one genuine global law for the linear head demand.

For the actual high-branch rows and quantities \(S,W,\rho,M,B\) of round 80, use \(A=\{0\}\), \(x=(q-B/n)_+\), and freeze
\[
 F=\{j\ne0:W(j)>\rho/8,\ x_j>0\}.
\]
All these heads are exposed. Write \(x(F)=\sum_F x_j\) and \(C(F)\) for (1) with demand \(1_F\). Then the best clipping-adjusted bound delivered by these certificates is exactly
\[
 C(F)-B|F|/n=x(F)+\max_{q'\in\mathcal Q_a}[q'(F)-q(F)].       \tag{2}
\]
Only the row defining \(F\) must clear the floor there. Other optimizers are tested on the *same* fixed set. Equation (2) shows where a uniform upper must enter even with complete freedom to design the opposite law.

There is a computable lower bound for the surcharge in (2) that uses only the positive support of the given row. On \(J=\{j\ne0:q_j>0\}\), regress \(1_F\) against \(V_{-s}|_J\) in the inner product with weights \(q_j\), and let \(e\) be the residual. If \(e\ne0\), it has both signs by the constant equation. Put \(u_0=0\), \(u_j=q_je_j\) on \(J\), and zero elsewhere. Then \(q+u/\|e_-\|_\infty\) is another genuine optimizer by the same equalities. Its head mass increases by \(\sum_Jq_je_j^2/\|e_-\|_\infty\), a forced positive surcharge. If \(q\) lies in the relative interior of the full face and \(e=0\), the demand agrees with one opposite potential on the entire possible bulk support, so every optimizer gives the same head mass and the surcharge vanishes. At a boundary point, other supports can still matter.

## A prime-uniform lower estimate before fitting a cover

There is an explicit finite lower bound for (2) using the selected high rows, including a sharper bound when individual heads have small capacities. Write \(v_i=q_i1_S/M_S\), \(L=n\sum_S q_i^2\), \(m=1/\sum v_i^2\), \(z=q-x\), \(\mu=\sum z_j\), and \(H=\sum_{j\ne0}x_jW(j)\). The exact eigen-equation \(sKq=q-\mathbf1/n\), symmetry of \(K\), and the second moment of \(W\) give
\[
 H\ge H_0:=\frac{L}{\sqrt p M_S}
 \left(1-\sqrt{\frac{(B\mu-\mu^2)(1-m/n)}{L}}\right)
 -\frac1{\sqrt p}-x_0W(0).                                      \tag{3}
\]
In fact \(\sum_jq_jW(j)=(L/M_S-1)/\sqrt p\). The field \(W\) has counting mean zero and squared Euclidean norm \((n^2/p)(1/m-1/n)\). Subtract \(\mu/n\) from each \(z_j\) and use \(\sum z_j^2\le B\mu/n\). This proves (3) using \(m=nM_S^2/L\).

Put \(t_0=\rho/8\), \(V_j=W(j)-t_0\) on \(F\), and take certified clipped caps \(c_j\ge x_j\) there. One choice uses every shift of a genuine opposite optimizer:
\[
 c_j=\left(\min\left(a,\min_{h:r^*_{j-h}>0}
             \frac{1/n-a r^*_{-h}}{r^*_{j-h}}\right)-B/n\right)_+.
\]
Since all exterior sites outside \(F\) with positive clipped mass have \(W\le t_0\), for every \(\lambda\ge0\),
\[
 C(F)-B|F|/n\ \ge\ x(F)\ \ge\
       \lambda(H_0-t_0M)-\sum_{j\in F}c_j(\lambda V_j-1)_+.       \tag{4}
\]
Use \(\lambda V_j\le1+(\lambda V_j-1)_+\) on each head. The actual \(H\) can replace its lower bound. Optimizing this one-variable bound gives the exact least total mass of numbers \(0\le u_j\le c_j\) whose \(V\)-weighted sum is at least \(H_0-t_0M\), by fractional knapsack duality. The breakpoints are \(1/V_j\), so no large LP is required.

Under the round-80 hypotheses \(L\to\infty\), \(B=o(L)\), \(A=\{0\}\), the optimal point cap \(a=O(n^{-1/2})\) and \(|W|\le1\) make the last two terms of (3) negligible relative to \(L/(\sqrt p M_S)\). Consequently \(H/M\ge(\sqrt{n/p}-o(1))\rho\). In particular \(\rho\le\sqrt{p/n}+o(1)\) since \(H\le M\). Taking \(\lambda=1/(1-\rho/8)\) in (4) gives the prime-uniform estimate
\[
 C(F)-B|F|/n\ \ge\ x(F)\ \ge\
 \frac{\sqrt{n/p}-1/8-o(1)}{1-\rho/8}\,\rho M.                  \tag{5}
\]
The numerator tends to \(1/\sqrt2-1/8\). This lower bound applies independently of the moment index and the density split whenever the stated collision and clipping hypotheses hold. A price below it on one required mask would exclude that supercritical configuration. Equation (5) alone gives no such upper.

## The extra cost of a prescribed translate family

For a fixed genuine opposite law \(r\), let \(b_h=1/n-ar_{-h}\). For shifts with \(b_h>0\) put \(\eta_h=\sum_F q_jr_{j-h}/b_h\), \(\eta=\max_h\eta_h\). A zero-budget shift vanishes on the positive bulk support of \(q\). Each positive-budget shift spends fraction \(\eta_h\) on \(F\), so any nonnegative combination covering \(1_F\) costs at least \(q(F)/\eta\). This is sharp for the relaxation that demands coverage only after averaging against \(q1_F\): use a maximizing shift and scale. Equality at the stronger pointwise price \(q(F)\) requires each paid shift to have zero overlap with positive primary mass outside \(F\), and the combination to equal one on \(F\). These tests also apply to several genuine base laws by taking the maximum over all their shifts.

The [Arb384 checker](astra-cover-81-check.py) rebuilds the four actual terminal masks, with \(B=1\), from their pinned orbits. On each the primary positive even bulk coordinates match in number the opposite cosine modes; the associated matrix is certified invertible. Interpolating \(1_F\) on these coordinates in the pure opposite cosine sector gives an exact signed field. Add a sufficiently large positive multiple of \(r^*\) to repair every remaining site, including the root, and normalize to a probability. The closed-form law has exact price \(q(F)\), even when tested against nonsymmetric feasible rows. For the fixed \(r^*\) translate cone the checker certifies both LP directions by rescaling dyadic proposals after outward evaluation. Symmetrizing shifts leaves the cost and feasibility unchanged for these even masks. Values below are rounded. [Interval records](astra-cover-81-checks.jsonl)

| Prime | Actual exposed heads | Exact clipped mass | Fraction captured by best shift \(\eta\) | Best raw translate price | Best translate price after floor / exact clipped mass |
|---:|---:|---:|---:|---:|---:|
| 101 | 5 | 0.17743 | 0.64027 | 0.48167 | 2.15109 |
| 257 | 18 | 0.32704 | 0.69013 | 0.74831 | 1.85817 |
| 409 | 28 | 0.32890 | 0.72847 | 0.81267 | 2.05358 |
| 769 | 58 | 0.33293 | 0.66004 | 0.86235 | 2.13653 |

At these finite cutoffs the universal input \(H_0\) gives zero in (4); the measured \(H\) gives lower bounds \(0,0.11434,0.08120,0.05686\) respectively. The four computations neither instantiate the order-depth asymptotic hypotheses nor establish a uniform loss for fixed translates at large primes.

## A strict obstruction on the full opposite cone at prime 97

Use the [exact two-dimensional even larger face](astra-face-54.md) at prime 97. Take the interior row with both free anchored coordinates equal to \(1/1000\) in that parameterization. At terminal time four with the same fixed cutoffs and pinning rule, its six positive clipped heads are \(F=\{5,13,18,30,35,43\}\). Their clipped mass is in \((0.26478818,0.26478819)\). The optimum over **all** genuine opposite laws after subtracting the floor is in \((0.34190878,0.34190879)\), forcing a surcharge in \((0.07712060,0.07712061)\).

The sharp lower witness is a different genuine optimizer on the original face: the two coordinates 3 and 19 and their reflections vanish, and its mass on these six frozen heads attains the larger price after subtracting the same floor. For the matching upper bound, interpolate the indicator on its positive bulk using the opposite cosine modes. The resulting field is strictly positive on the newly vanished coordinates; adding a free multiple of the opposite optimum repairs all other sites and gives a genuine globally nonnegative law. The witness and law certify both inequalities on the whole face, including nonsymmetric rows. The interval record also gives the achieved normalized level and root budget. This is a finite example of the surcharge in (2) for the actual head construction.

## Ranked next tests

1. Freeze the exposed heads at one admissible high-branch time, check the tangent surcharge, and construct a positive opposite interpolant on the entire possible primary support. To exclude the branch, its floor-adjusted price must beat (5) or the stronger sorted bound (4) on one required mask. The full-cone theorem identifies any residual obstruction with actual optimizer mass on those frozen heads. Monitor the normalized level and root budget together.
2. For a restricted family, measure \(\eta\) before fitting any LP. If its lower cost already exceeds the target, enlarge the actual opposite family or switch to the full-face computation. Estimate the individual cap and bias order statistics in (4) at growing depths; the four shallow masks give no asymptotic separation.
