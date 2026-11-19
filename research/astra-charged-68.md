# A growing projected-polynomial obstruction for the actual tilted LP

Let \(p>5\) be prime with \(p\equiv1\bmod4\), \(n=(p-1)/2\), \(X_i=\widehat{\chi(1-\cdot)}(i)/\sqrt p\) on the characters of the square subgroup, and \(P=(I-J+sK)/2\) for either sign \(s\). Write \(\ell=Pe_0,\ \kappa=\ell_0,\ D_0=P-\ell\ell^{\mathsf T}/\kappa\). The mean-one trials
\[
 y=1+(\gamma\sqrt n-1)\ell/\kappa+2\sum_{m\in I}c_mD_0T_m(X),\qquad I\subset\{2,3,\ldots\},                 \tag{1}
\]
have the full exact sign Fourier support and mark \(\gamma\sqrt n\). The constant and linear scalar modes are annihilated by \(D_0\). The coefficients, degree list and target mark may depend on the field. This is the actual once-projected scalar family, including the \(KT_m\) fields absent from the unprojected Gram argument. [Anchored projection](scalar-seed-25.md) · [Unprojected trials](astra-charged-67.md)

If \(N_I=1+\sum_{m\in I}m^2=o(\sqrt p)\), then on either sign the largest feasible normalized mark of (1) tends to \(1/\sqrt2\). In particular *every* polynomial of degree \(M=o(p^{1/6})\) is covered, and a sparse list can include an isolated degree \(o(p^{1/4})\). The upper bound even follows from positivity off an adaptive bulk exceptional set \(A\) with \(N_I |A|=o(p)\), for \(\gamma\ge0\). At any prescribed \(\gamma\ge1\) in a fixed bounded interval there is a constant lower bound on the normalized RMS negative part of (1) outside such a set. All asymptotic statements concern sequences satisfying the stated little-oh budgets.

At \(t=L+1\), let \(c(q)=\mathbb E_q[s\sqrt n v_t]-\|v_t\|^2/4\), and take the two actual tilts \(u=h,2h\) of round 67. On the larger sign, the best feasible \(q=y/n\) from (1) loses **at least \(1-1/\sqrt2-o(1)\)** in each actual objective \(\gamma(q)-uc(q)\) against the full \(V(u)\). This rejects these trials as separately accurate evaluations for the proposed value-difference certificate. A common one-sided error in both values can cancel when they are subtracted, so this gap alone gives no lower bound on the true marginal slope.

## A bounded density testing the whole projected correction

Write \(\mathcal Y_m\) for the arithmetic two-lift average of the Mellin traces of \(N_m,N'_m\) from the projected Chebyshev identity. Its compact counterpart \(Z_m\) is the mean of two independent standard traces in \({\rm USp}(d_m)\), \(d_m=2\lfloor m/2\rfloor\). These pairs have independent product symplectic group, also independent of the Jacobi circle \(X=\cos\theta\) in the compact calculation. The exact arithmetic bounds are
\[
 |KT_m(X)-\mathcal Y_m|\le C/\sqrt p,\quad |\mathcal Y_m|\le d_m,\quad
 |\mathbb E_n T_m(X)|\le C m/\sqrt p .
\]
The first bound includes the odd-degree identity stalk of dimension one, and the root correction has \(|\delta_m|\le2\). The last bound uses the pure Jacobi moment estimate, with only the two exceptional full lifts. The normalized Jacobi line has dimension and generic rank one. [Path groups and exact trace formula](parallel-graph-shapes-23.md#a-fixed-number-of-path-columns-gives-no-leading-gain) · [Xi, Theorem 1.3](https://arxiv.org/pdf/1809.04286)

Fix an integer \(k\ge2\) independently of \(p\). Work with the compact base density proportional to
\[
 (1-s X)^k\prod_{m\in I,\ m\le k}(1-s\,{\rm sign}(c_m)Z_m)^6 .
\]
Zero coefficients can be omitted. Denote the normalized expression by \(W_0\), using its *compact* normalizer also upon arithmetic evaluation. This density is nonnegative and bounded by a constant depending only on \(k\) in both models. Its compact normalizer before division is at least one by independence, symmetry and convexity. The tilted circle mean is \(-sk/(k+1)\), from integrating \((1-\cos\theta)^k\). Its \(T_m\) mean vanishes for every \(m>k\) by Fourier orthogonality.

For any of these symplectic pairs let \(\mu_i=\mathbb E Z^i\). Symmetry kills the odd moments, \(\mu_2=1/2\), and \(\mu_4\ge5/8\). Indeed a standard trace has second moment one and fourth moment at least two since both symmetric and alternating squares occur in the tensor square. Independence gives the pair bound. Cauchy–Schwarz gives \(\mu_6\ge2\mu_4^2\ge25/32\). Under the tilt \((1+Z)^6\), the mean is
\[
 \frac{3+20\mu_4+6\mu_6}{17/2+15\mu_4+\mu_6}\ \ge\ 21/20 .
\]
After cross multiplication the difference is increasing in each indicated moment and positive at their lower bounds. Hence under \(W_0\) each low correction satisfies \({\rm sign}(c_m)\mathbb E[T_m(X)+s Z_m]\le-1/20\).

Put \(I_H=\{m\in I:m>k\}\), \(S=\sum_{j\in I_H}j d_j\). If \(S>0\), multiply \(W_0\) by
\[
 \sum_{j\in I_H}\frac{j d_j}{S}
             \left(1-s\,{\rm sign}(c_j)\frac{Z_j}{d_j}\right) .                       \tag{2}
\]
Otherwise retain \(W_0\). This nonnegative density \(W\) is bounded by \(2\|W_0\|_\infty\), including on the actual field after replacing \(Z_m\) with \(\mathcal Y_m\). Its compact mean is one and all low means are unchanged. For each \(m\in I_H\) its compact mean against \({\rm sign}(c_m)[T_m(X)+sZ_m]\) is exactly \(-m/(2S)\). The occurrence of only one high factor per mixture term permits a rank estimate uniform in all the high degrees.

For clarity, put \(M=\max(I\cup\{k\})\). The unnormalized arithmetic mean of \(W\) times \(1\) or \(X\) differs from its compact mean by \(O_k(p^{-1/2}+M/p)\). For the multiplier \(T_m(X)+s\mathcal Y_m\) the difference is \(O_k(m/\sqrt p+mM/p)\), uniformly in \(m\in I\) and all coefficient signs. To verify the estimates, expand each summand of (2) separately. Its dimension-weighted absolute coefficient sum is \(O_k(1)\), since the extra trace is divided by its dimension. The \(T_m\) multiplier is the half sum of the two Jacobi powers on good full lifts, with dimension weight one and word length \(m\). The \(\mathcal Y_m\) multiplier has dimension weight at most \(m\) and word length one. Low factors cost \(O_k(1)\) in both budgets. In the tame rank inequality
\[
 R(A\star B)\le R(A)D(B)+D(A)R(B)
\]
all generators have \(R/D\le 3/2\), including the odd paths. Thus the nonpunctual identity-stalk error is \(O_k(m/\sqrt p)\) in either calculation. The good characters for the finitely many low objects, the Jacobi line and the at most two high pairs in each summand omit \(O_k(1+M)\) lifts; powers of the same Jacobi line need no new exceptions. The product and its tensor replacement at an exceptional lift are bounded by their dimension weight. This accounts for \(O_k(mM/p)\). On good lifts, tensor decomposition in the symplectic factors leaves a pure Jacobi power on their invariant part, with the compact symplectic multiplicity and no arithmetic phase from those factors. The derived group contains the full symplectic product with trivial Jacobi component, so every other constituent has zero geometric unit multiplicity. The pure powers have their circle means with error \(O_k(m/\sqrt p)\) for the \(T_m\) multiplier, or \(O_k(1/\sqrt p)\) per unit dimension weight for the fixed Jacobi powers in the other multiplier, by Xi. This also avoids any assumption about a growing list of jointly equidistributed factors. The comparison applies to all full lifts and hence to the square subgroup by the two-lift average. [Rank and good-character calculation](parallel-depth-window-30.md#2-quantitative-closure-and-a-separate-geometric-ledger) · [Earlier dimension-weight comparison](early-peaks-67.md) · [Katz, Chapters 2–5 and 13](https://web.math.princeton.edu/~nmk/mellin331.pdf)

Off the mark \(\ell_i=(s\sqrt pX_i-1)/(2n)\), \(\kappa=(1-(1+s)/n)/2\). Consequently
\[
 2D_0T_m(X)_i=T_m(X_i)+s\mathcal Y_m(i)+O(m/\sqrt p),\qquad
 1+(\gamma\sqrt n-1)\ell_i/\kappa=1+\frac{s\gamma\sqrt{p/n}}{2\kappa}X_i+O((1+\gamma)/\sqrt p).
\]
Here \((PT_m)_0=O(m)\) by the trace bound, including at the root. Remove the root and the allowed exceptional sites when averaging; their costs for the bounded base tests and the \(m\)-th path test are respectively \(O_k((1+|A|)/n)\) and \(O_k(m(1+|A|)/n)\), using the displayed bulk expressions as bounded test functions also at the omitted root. There is no use of a uniform bound on the marked row value.

Combining the estimates, the signed high-column error is \(O_k(m[p^{-1/2}+M/p+(1+|A|)/n])=o_k(m/S)\) under the budgets. The low-column error is \(o_k(1)\). Thus every tested correction has nonpositive contribution, even with arbitrarily large coefficients. For the unexceptional bulk \(B\) one obtains
\[
 \mathbb E_n[{\bf1}_B W y]\ \le\
  1-\gamma\sqrt2\,\frac{k}{k+1}+o_k(1)(1+\gamma).                    \tag{3}
\]
For nonnegative bulk the left side is nonnegative, so first letting \(p\) grow and then \(k\) grow proves the claimed ceiling. The elementary sign row with bulk values \((\sqrt p+s\widehat{\chi(1-\cdot)}(i))/(\sqrt p+1)\) belongs to the affine class, is feasible including at the mark, and reaches \(1/\sqrt2+o(1)\). For an explicit RMS constant fix \(k=3\). The circle normalizer is \(5/2\), and each of the at most two low factors has \(d_m=2\) and normalizer at least \(17/2+15(5/8)+25/32>18.6\). Thus \(0\le W\le 2(8/(5/2))(3^6/18.6)^2<10^4\) on the field, while \(\mathbb E_n W=1+o(1)\). Applying Cauchy–Schwarz in (3) yields \(\liminf \|{\bf1}_B y_-\|_{2,n}\ge(3\sqrt2/4-1)/100>0.0006\) at the stated marks. In particular the anchored class cannot even approximate a nonnegative larger-face row at its correct mark with vanishing normalized RMS. Finally the range of the actual charged cost on the full polytope has length at most \(R=4\sqrt{nt}\). Comparing the restricted optimizer with any true primary optimizer in the two linear objectives costs at most \(uR=o(1)\) in the secondary term, proving the advertised objective gap. [Actual two-tilt scale](astra-charged-67.md) · [Affine sign witness](fourier.md)

## Necessary accuracy of an untilted positive reciprocal trial

Let \(z,\bar z\) be the actual reciprocal pair in probability normalization at floor \(0<\tau\le1\), with \(W_\tau=1+(1-1/n)\tau\). Let \(\bar q^*\) be any opposite primary optimum of mark \(\bar\alpha\). All sites of \(\bar z\) have probability at most \(\bar\alpha/\sqrt n\) by translation. Bulk reciprocity gives \(z_i\bar z_i=\tau/(n^2W_\tau)\). Opposite Fourier orthogonality and \(\alpha_s\bar\alpha=1\) therefore give
\[
 \alpha_s-\gamma(z)=\frac{n}{\bar\alpha}\sum_{i\ne0}z_i\bar q_i^*
 \ \ge\ \frac{\tau(1-\bar\alpha/\sqrt n)}
                  {\sqrt n\,W_\tau\bar\alpha^2}.                      \tag{4}
\]
This uses neither a selected optimal support nor an endpoint derivative. The reciprocal identity also expresses the left side as
\(\tau\sum_{i\ne0}\bar q_i^*/\bar z_i/(nW_\tau\bar\alpha)\); Cauchy–Schwarz gives the stronger support-dependent lower bound \(\tau(\sum_{i\ne0}\sqrt{\bar q_i^*})^2/(nW_\tau\bar\alpha)\). [Positive reciprocal normalization](astra-scalar-40.md) · [Translation point cap](astra-tail-53.md)

For \(u=h,2h\), every vertex outside the primary face has tilted objective loss at least its primary deficit times \(1-uR/\Delta\ge1/2\), because its deficit is at least the cyclotomic gap \(\Delta\). On the face the tilted loss is nonnegative. Averaging a vertex decomposition yields
\[
 V(u)-[\gamma(z)-uc(z)]\ \ge\ \tfrac12(\alpha_s-\gamma(z))
                 \ \gg\ \tau/\sqrt n.                                \tag{5}
\]
The elementary Jacobi bounds keep both marks in fixed compact positive intervals. At \(t=L+1\), any floor with \(\tau/(hL\sqrt n)\to\infty\) therefore fails individual \(O(hL)\) accuracy in both tilted objectives, on either sign. With the chosen \(h\), the excluded regime is \(\tau\gg\Delta\sqrt L\) in the sense of a diverging ratio. This lower bound still permits cancellation between two erroneous trial values; it does not exclude other ways of controlling \(c(z)\).

Indeed the same elementary affine witness has \(\|y\|_{2,n}=O(1)\), so its *actual* signed charge is at most \(O(\sqrt t)-E_t/4\) by Cauchy–Schwarz and the cold energy bound. Reusing it at both tilts gives a trial-value difference at most \(O(h\sqrt t)\) on either sign. At prime-square orders the true larger marginal instead satisfies \(c_*\ge 2t(\sqrt2-1-o(1))-o(1)\) throughout the growing marked window by the exact square mark and reserve. Thus passing a small same-trial difference is demonstrably insufficient for replacing the exact values in general. These squares are outside the prime target. [Exact reserve and prime-square control](astra-charged-66.md)

1. Compare late signed charge and primary exposure together. Under \(N_I=o(\sqrt p)\), one-stage projected scalar trials lose at least \(1-1/\sqrt2-o(1)\) in each larger-side tilted solve, including at the marked-window degree. A projected construction can instead use jointly dependent fields, repeated sector projections, or degrees beyond this budget. A feasible such trial with a certified tilted objective gap \(o(hL)\) and charge \(o(L)\) at the larger sign would imply the requested bound there.
2. For an untilted reciprocal row, (5) rejects separate objective comparisons at floors \(\tau\gg\Delta\sqrt L\) with diverging ratio. At \(\tau=o(\Delta)\) the preceding round's vertex conditioning still applies. A signed charge \(o(L)\) from above there passes to a true optimal row; the necessary prime-uniform charge estimate remains open.
