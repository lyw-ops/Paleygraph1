# What two zero-floor weighted tail tests require

Use the actual averaged iterates and exact ordinary optimizers of the [fixed-depth weighted test](zero-floor-averaged-weighted-tail.md). Fix the cap \(M\), write \(\alpha_M(p)\) for the deficit at the actual capped zero-floor fixed point, and write
\[
 G_{\epsilon,M,J}(p)=
 \mathbb E_n[(F_\epsilon-M/2)_+\ \overline{T_\epsilon}]
\]
with \(J\) held fixed before taking the prime limit. All conventions and real sheets are those of the preceding notes.

At any common horizon, add the two inequalities (2) from the averaged test. The products \(\lambda_+\lambda_-=1\) and \(T_{+,j}+T_{-,j}=1_{\{i\ne0\}}|h_j|\) are exact. The sum of the nonnegative spill reserves is at least \(\overline{\alpha}_{\rm bulk}/4\), where \(\alpha_{{\rm bulk},j}=\mathbb E_n[1_{\{i\ne0\}}(h_j^2+2M|h_j|)]\). The terminal scalar charges are \(O_M(J^{-1})\). At fixed \(J\), both normalized marks in the averaged test tend uniformly to \(2\) as \(p\to\infty\), and the \(\lambda_\epsilon\)'s are uniformly bounded by the entry estimate. Thus
\[
 G_{+,M,J}+G_{-,M,J}\ \ge\
 2(\lambda_++\lambda_- -2)
   +\tfrac14\overline{\alpha}_{\rm bulk}
   -O_M(J^{-1})-o_{M,J,p}(1).                                      \tag{1}
\]
The same bound holds if the optimizers used for the two signs at a given horizon are chosen independently, since each valid optimizer has the same marked ratio and the uniform terminal bound.

The actual zero-floor midpoint comparison in the [capped mark and spill note](zero-floor-mark-and-cap-budget.md) bounds the averaged squared bulk spill difference by \(O_M(J^{-1})\). Moreover, the true zero-floor fixed point and all averaged iterates have normalized second norm \(O_M(1)\) by nonexpansiveness and the fixed-point norm bound. Therefore the averaged difference between the squared norms of the bulk spills is \(O_M(J^{-1/2})\) by Cauchy–Schwarz. The same estimate holds for their first absolute means. The marked part of the fixed-point deficit tends to zero by the zero-floor marked bound at fixed \(M\). Substituting into (1) gives
\[
 G_{+,M,J}+G_{-,M,J}
 \ \ge\ 2(\lambda_++\lambda_- -2)+\tfrac14\alpha_M(p)
                 -O_M(J^{-1/2})-o_{M,J,p}(1).                     \tag{2}
\]
Consequently, vanishing of the sum of the actual weighted tails along common large horizons, with primes taken first, requires \(\alpha_M(p)\to0\). The small-cap lower in the preceding note now gives an explicit obstruction to that common-horizon strategy for \(2\le M\le9/4\), independently of the truth of the original theta limit.

The individual squared-spill reserve also handles distinct horizon subsequences. If both individual tail tests vanish along their own horizons at a fixed cap, the averaged test proves \(\lambda_\epsilon\to1\) for each sign. Returning to either inequality (2) of that test and retaining the squared-spill reserve then forces \(\limsup_p\|1_{\{i\ne0\}}h_0\|_{2,n}^2=0\). Indeed its finite-horizon squared reserve differs from that for the fixed point by \(O_M(J^{-1/2})\) as above. The marked spill is negligible in normalized second norm at that cap. The exact deficit identity and the first-norm bound by the second norm imply \(\alpha_M(p)\to0\). Thus allowing independent horizon sequences does not avoid the small-cap obstruction.

At a larger fixed cap this isolates a first necessary unweighted arithmetic test before the genuinely weighted ordinary-optimizer tail. It gives no implication from unweighted vanishing to the weighted upper.
