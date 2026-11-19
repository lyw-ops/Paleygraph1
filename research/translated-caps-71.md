# Using point caps and signed prices on actual translated budgets

The translated opposite-face budgets can pay for the localized collision through a strictly stronger diagonal bound. All translates first give a common cap at each site. One then applies the upper chord of the square on the capped interval and retains the exact linear budget of each translate. This permits signed prices without taking the negative part of an individual translate. At prime \(97\) the two improvements are separately visible on an actual cold-orbit defect profile. The all-prime \(o(d)\) bound on the true selected windows remains open.

## One cap before squaring

Use the normalized endpoint probabilities \(q,r\) on the tested and opposite signs, respectively, from [the positive translated budgets](astra-localized-71.md). Write \(z=q/q_0\), \(w=r/r_0\), \(\gamma=\sqrt n q_0\), and \(T=I\setminus\{0\}\) for the actual bulk support of the tested primary face. The point caps give \(z_i,w_i\in[0,1]\). Keep a fixed opposite optimizer. For each shift \(h\) with positive budget \(b_h=1-w_{-h}>0\), set
\[
 a_{hi}=w_{i-h}/b_h,\qquad i\in T.
\]
The exact equality \(\sum_{i\in T}a_{hi}z_i=1\) holds for every tested optimizer. A shift with zero budget excludes all sites it covers positively, since every summand is nonnegative. On the true support such a shift has zero coefficients. Define
\[
 k_i=\max(1,\max_{h:b_h>0}a_{hi}),\qquad M_i=1/k_i.
\]
The linear budgets and \(z_i\le1\) imply \(0\le z_i\le M_i\). In particular
\[
 k_i z_i^2\le z_i,\qquad
 \sum_{i\in T}k_i a_{hi}z_i^2\le1.
 \tag{1}
\]
Since \(k_i a_{hi}\ge a_{hi}^2\), the nonnegative price cover in (1) dominates the separate-square cover of the same translate family at identical unit prices. Formula (1) can use a better cap \(M_i\) established by any arithmetic argument. The factor \(k_i\) is shared across all translated budgets.

For a nonnegative defect demand \(F\), take **signed** prices \(\lambda_h\in\mathbb R\) with
\[
 \sum_{h:b_h>0}\lambda_h a_{hi}\ \ge\ M_i F_i\qquad(i\in T).
 \tag{2}
\]
Then the upper chord and exact equalities give
\[
 n\sum_i q_i^2 F_i
 =\gamma^2\sum_{i\in T}F_i z_i^2
 \le\gamma^2\sum_{i\in T}F_i M_i z_i
 \le\gamma^2\sum_h\lambda_h .
 \tag{3}
\]
Here \(F_0=0\). Nonnegativity is needed for the combined cover on \(T\). Signed pricing of the individual budgets in (1) by an inequality would be invalid. In (2)–(3) one uses the equalities for the linear masks after the cap. This also allows multiple opposite rows. For any opposite feasible row \(r\) with positive root, the same proof uses budget \(b_h=(nq_0r_0)^{-1}-w_{-h}\). Every budget is nonnegative by the translated equality. All are strictly positive if the maximum entry of \(r\) is strictly below the opposite optimum \((nq_0)^{-1}\). For zero budgets use the same exclusion as above.

There is a precise limit of improving only the linear prices. If the chosen real translated rows span the opposite constant-plus-sector subspace, their shifted linear equations on \(T\), together with the fixed root and the zero-budget exclusions, specify the whole tested face in nonnegative coordinates. In this case finite linear-programming duality says that the infimum in (2) is exactly the maximum of \(\sum_i F_iM_i z_i\) over the actual primary face. Indeed the unnormalized equations are the constant mean and opposite Fourier orthogonality, with fixed normalization at the root. A feasible row on the opposite side whose positional Fourier coefficients are nonzero at every allowed character, including the constant, has real translates spanning that subspace. For example choose the elementary strictly positive affine Jacobi row from a sufficiently small nonzero amplitude of the Fourier sign mask. An affine support restriction need not represent the quadratic objective tightly; the loss from the pointwise chord still has to be estimated.

## Strict improvement on a true prime defect profile

At \(p=97\) the [exact support calculation](astra-face-54-check.py) supplies the two complementary primary faces, and the plus sign is strictly larger. Use the exact minus proposal with allowance \(1/1000\) and flat windows of length three starting at \(1,\ldots,19\) on the actual zero-floor orbit. Let \(F_i\) be the fraction of these windows in which the pinned minus row at site \(i\) is less than \(-1/20\). Its root is excluded. This choice is a finite diagnostic and goes beyond the proved asymptotic depth schedule at this prime.

The checker encloses all the exact threshold decisions on the full plus support. It uses the unique even opposite primary row from the cyclotomic equations. It validates two feasible dual vectors, for the old square-cover LP and the nonnegative cap-cover LP, and two explicit cap covers. Before multiplying by the common factor \(\gamma^2\), the old square-cover minimum exceeds \(1.54235\). The nonnegative cap-cover minimum lies inside \((1.28662,1.28666)\), and the signed cap certificate costs less than \(1.17954\). Thus the cap alone beats the best separate-square cover of this fixed witness, and signed prices beat the best nonnegative cap cover, all on the same defects. The frozen certificates were proposed numerically. Feasibility and strict comparisons use Arb320 and exact rational costs. There is no claim that the signed bound is the exact localized collision or that these prices work at an arbitrary prime. [Checker](translated-caps-71-check.py) · [Interval record](translated-caps-71-checks.jsonl)

## Ranked next tests

1. For the actual common-window defect average, seek a signed cover of \(M_iF_i\) in (2) with total price \(o(d)\) through all prime fields. Control the exact caps at sites receiving repeated defects before trying to optimize many prices. With a full-span translate family, a positive normalized lower bound for the tested linear chord objective rejects this cap choice even if the actual quadratic pairing is small.
2. If the cap cover is too costly, use the cross terms from translated products or a weighted tangent move on the genuine primary face. A prime-uniform upper on the localized collision for one actual optimizer would suffice, even where a worst-optimizer linear bound fails.
