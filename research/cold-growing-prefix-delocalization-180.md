# The growing cold prefix: size at height 602 and a delocalization criterion

The setting is unchanged:
- the genuine nine-center start and both lifts;
- the physical mark \(t_0=n\);
- the original closed square \(Q\) about \(a=2031/128\), of half-width \(2^{-17}\);
- the increments \(R_j=V_{j+1}-V_j\).

Norms: \(\|\cdot\|_{2,n}\) is the normalized second norm; \(\|\cdot\|_\infty\) is the coordinate supremum.

[Round 173](cold-logarithmic-finite-tube-173.md) reduced common continuation to coordinate confinement of \(V_{602},\dots,V_{602+k_n}\), \(k_n=\lceil(4/7)\log_2n\rceil\), with fixed clearance. This round neither proves nor refutes that test. It shows that the apparent conflict with [Round 179](cold-fixed-counting-source-obstruction-179.md) is a normalization effect. It writes the uncontrolled quantity exactly and proves a sufficient criterion.

The analysis comes from a native Claude research agent (archived draft: [native-claude-cold-prime-signed-growing-prefix-180.md](native-claude-cold-prime-signed-growing-prefix-180.md)). An independent agent audit checked it ([native-claude-audit-180.md](native-claude-audit-180.md)). Its corrections are incorporated below.

## Size of the increment at height 602

[Round 80](astra-dissipation-80.md) bounds the physical complex normalized residual at row 600 on \(Q\):
\[
 \limsup_p\sup_Q\|R_{600}\|_{2,n}\le4(0.449922)^{600}<3.051\cdot10^{-208}.
\]

The next two steps contract by \(0.545\). The segments \([V_{600},V_{601}]\) and \([V_{601},V_{602}]\) satisfy \(|z-S_i|\le1.963\) ([Rounds 126, 162 and 177](cold-seed-centered-larger-tube-177.md)). This lies inside the seed-centred region where the scalar derivative is below \(0.545\). The mark derivative is \(O(n^{-1/2})\).

Combined with the Round 179 lower bound and the fixed prefix through \(V_{612}\) in the \(3/8\) disks,
\[
 0<\liminf_p\inf_Q\|R_{602}\|_{2,n}\le\limsup_p\sup_Q\|R_{602}\|_{2,n}<9.07\cdot10^{-209}.
\]
Both thresholds are ineffective. They inherit fixed-height compact transfer.

Caveat on the lifts: Round 80 does not state "both lifts" verbatim for this residual. The later transfers of Rounds 162 and 179 do, so the inheritance is consistent but not verbatim.

## The conflict is a normalization effect

The unnormalized lower bound \(c\sqrt n\) of Round 179 is a corollary of its normalized statement. It is compatible with coordinate entries of order \(10^{-208}\). Inside the polydisk, \(\|V_{602+k}-V_{602}\|_{2,n}<2\cdot10^{-208}\) eventually. Coordinate confinement therefore holds exactly when the increments stay delocalized across the \(n\) coordinates.

\(K\) is a real symmetric circulant, since \(\chi(-1)=1\). The exact secant identity is
\[
 R_{h+1,i}=\frac{\sqrt n}{2}\,\mathbb E_n\bigl[(\tau_iS)\,\tilde D_h\,R_h\bigr],\qquad
 \tilde D_h=\int_0^1\Phi_t'(V_h+sR_h)\,ds,
\]
where \(\tau_iS=2\sqrt n\,Ke_i\) is the shifted seed. The uncontrolled quantity is the signed coordinate sum \(\sum_h R_{h,i}\) through the cutoff. Equivalently, it is the size of these \(n\) correlations compared with their root mean square.

Two facts about the method:
- Bounds that use only the operator norms available (row \(\ell^2\) and entrywise) lose exactly \(\sqrt n\), because flat rows attain them.
- The entrywise Round 162 bound concerns the frozen \(D_{602}\), not products of the moving secants.

## Criterion D (sufficient)

Fix \(\rho\in\{0.025,0.05,3/8\}\) with contraction \(q_\rho\), and fix \(0<\eta<\rho\), \(\Lambda\ge1\) and \(\gamma\ge1\) with \(q_\rho\gamma<1\). Suppose that for all large eligible \(p\), all \(t\in Q\), both lifts, and every \(k<k_n\) along a prefix that has so far stayed in the \(\rho\)-polydisk,
\[
 \|R_{602+k}\|_\infty\le\Lambda\gamma^k\|R_{602+k}\|_{2,n}.
\]
Then the prefix stays in the \((\rho-\eta)\)-polydisk with clearance \(\eta\), and the Round 173 tail gives common stationary continuation on the interior of \(Q\).

The proof is induction on \(k\):
- Convexity gives \(\|R_{602+i}\|_{2,n}\le q^i\varepsilon'\).
- The triangle inequality bounds the sup displacement by \(\Lambda\varepsilon'/(1-q\gamma)\).
- \(0.545^8<2^{-7}\) was checked exactly.

With \(\gamma=1\) and \(\eta=\rho/2\), any \(n\)-independent \(\Lambda\) below \(6.5\cdot10^{205}\) suffices at \(\rho=0.025\), and below \(9.4\cdot10^{206}\) at \(\rho=3/8\).

A signed, sup-dominating price whose secant rate \(\kappa\) satisfies \(0.01272/(1-\kappa)<\rho-\eta\) also suffices. That means \(\kappa<0.966\) at \(\rho=3/8\).

**Scope (audit correction).** Criterion D is sufficient, not necessary. Confinement needs only the signed cumulative sums to stay below \(\rho\). A growing ratio, or decay of the supremum at a rate unrelated to \(1/q\), is not excluded by confinement itself.

What is proved about the method:
- Any \(\Lambda_n\to\infty\) defeats Criterion D, because \(\liminf\|R_{602}\|_{2,n}>0\). Starting from any later fixed height does not help.
- An unsigned price with rate at least one diverges over \(k_n\) steps.

What is heuristic only: the claim that a moving Newton predictor reduces to the same signed sum. Only the frozen correction was analysed. The [Round 83](astra-direction-83.md) expansion records concern a different collection rule and are only analogous evidence.

## Larger radius

The analyticity margin \(N-2(1.963+\rho)^2>0\) holds for \(\rho<3.670\). Throughout that range the seed-centred derivative bound gives contraction \(q(\rho)<1\), and the tail works with \(k_n=\lceil c\log_2n\rceil\) for \(c>1/(2\log_2(1/q))\). The current \(c=4/7\) works up to \(\rho\approx0.39\).

The values \(q(0.025)\approx0.5174\), \(q(0.05)\approx0.5193\) and \(q(3/8)\approx0.5441\) satisfy the monotonicity condition that puts the maximum at the endpoint. They are new seed-centred values. Values for \(\rho\ge0.75\) come from a floating-point grid and are evidence only.

A larger radius enlarges the budget linearly. It does not remove the need for an \(n\)-independent delocalization bound.

## Evidence and checks

[paley-180-audit-constants-check.py](paley-180-audit-constants-check.py) recomputes with exact fractions and 60-digit decimals:
- \(4(0.449922)^{600}\) and the \(0.545^2\) factor;
- the \(\Lambda\) budgets;
- the analytic radius \(3.6703\);
- the endpoint monotonicity at the four listed radii.

The draft's floating-point experiments were not replayed and are not inputs to any statement here. They used a Jacobi-seed start rather than the nine-center row, did not separate the lifts, and stopped at heights at most 40 and depth 800. They observed sup/RMS of about \(\sqrt{2\ln n}\) and an \(\ell^2\) rate of about \(0.24\) per step.

## Next tests

1. A signed, cross-vertex collected price for the secant operator on the \(3/8\) polydisk about \(V_{602}\), with rate below \(0.966\).
2. A fixed-height bound for the compact coset supremum of the increment fields, with a sup transfer. Either it supplies a bounded ratio, or it locates a coordinate that defeats Criterion D.
