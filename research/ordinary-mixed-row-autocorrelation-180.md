# Mixed row autocorrelation and the slope-product sum

Use the actual \(\mu(r,b)=g(Y)g(D)\), the square mask and the interior exclusions of [Round 171](ordinary-affine-line-energy-171.md), with counting norms throughout. Write \(m(r)=\sum_b\mu(r,b)\), \(M_1=\sum_r m(r)\le G^2\) and \(W_\xi=\sum_r m(r)m(\xi/r)\), as in [Round 178](ordinary-weighted-slope-product-incidence-178.md). This note proves
\[
 \sum_\xi W_\xi^{3/2}=O(p^{43/16}),
\]
improving the Round 178 bound \(O(p^{11/4-3/836})\). As a consequence, the genuine right energy, the weighted affine incidence and the one-match covariance improve. The one-match target \(O(p^{3/2})\) remains open.

The argument was found by a native Claude research agent (archived draft: [native-claude-ordinary-prime-mixed-row-slope-product-180.md](native-claude-ordinary-prime-mixed-row-slope-product-180.md)) and checked by an independent agent audit ([native-claude-audit-180.md](native-claude-audit-180.md)). Both are agent work, not human review.

## The autocorrelation at λ ≠ 1

Put \(C(\lambda)=\sum_r m(r)m(\lambda r)\). Then
\[
 \sum_\lambda C(\lambda)=M_1^2,\qquad \sum_\lambda C(\lambda)^2=\sum_\xi W_\xi^2=E^\times(m),\qquad C(\lambda)=C(1/\lambda).
\]

**Drop the mask.** Removing the square mask \(b\in Q\) is a positive upper bound. With \(r=(Y-D)/(1-D)\), and since \(D\) determines \(Y=r+(1-r)D\) at fixed \(r\), the unmasked row satisfies \(m^\sharp(r)\le G\).

**Unfold.** The completed \(C^\sharp(\lambda)\) is the sum of \(g(Y_1)g(D_1)g(Y_3)g(D_3)\) over the tuples with all coordinates in \(\mathbb F_p\setminus\{0,1\}\), \(Y_i\ne D_i\), and
\[
 (Y_1-D_1)(1-D_3)=\lambda(Y_3-D_3)(1-D_1).
\]

**A genuine line family.** For \(\lambda\notin\{0,1\}\), let \(\ell_{D_1,D_3}\) be the set of points \((X,Z)\) with \((1-D_3)(X-D_1)=\lambda(1-D_1)(Z-D_3)\).
- Its slope is \((1-D_3)/(\lambda(1-D_1))\), which is neither \(0\) nor \(\infty\).
- It passes through \((D_1,D_3)\) and meets \(Z=1\) at \(X=\lambda+(1-\lambda)D_1\).
- Hence the line determines \((D_1,D_3)\), and the lines are distinct.

At \(\lambda=1\), and for \(W_\xi\) itself, the corresponding families are a pencil or hyperbolas. This is why the earlier approaches gave no incidence gain.

**Determination.** Each of the four variables is determined by the other three on the relation:
- The coefficients of \(Y_1\) and \(Y_3\) are \(1-D_3\ne0\) and \(\lambda(1-D_1)\ne0\).
- If the coefficient of \(D_1\) vanishes, the relation forces \(Y_1=1\).
- If the coefficient of \(D_3\) vanishes, the remaining constant is \((Y_1-D_1)(1-Y_3)\ne0\).

**Incidence input.** Use [Stevens–de Zeeuw, Theorem 4](https://arxiv.org/abs/1609.06284). For \(|A|=a\le b=|B|\), \(ab^2\le n^3\) and \(an\ll p^2\), the incidences between \(A\times B\) and \(n\) lines satisfy
\[
 I\ll a^{3/4}b^{1/2}n^{3/4}+n .
\]
- The case \(ab^2>n^3\) obeys the same bound, because \(I\le an\) for nonvertical lines and \(an\le a^{3/4}b^{1/2}n^{3/4}\) when \(a\le b\).
- The lines are also nonhorizontal, so the coordinates may be swapped to put the smaller set first.
- Since \(a^{3/4}b^{1/2}\le(ab)^{5/8}\), this gives \((|U_1||U_3|)^{5/8}(|V_1||V_3|)^{3/4}+|V_1||V_3|\) for point levels \(U_i\) and line-parameter levels \(V_i\).

**Heavy and light parts.** Put \(\tau=p^{-1/8}\).
- *Heavy.* Apply the layer cake to \(g1_{g>\tau}\) in all four roles. Every level has size at most \(G/\tau=O(p^{5/8})\), so \(an\le(G/\tau)^3=O(p^{15/8})\) satisfies the hypothesis. Jensen gives \(\int|U|^\theta\le G^\theta\) for \(\theta\le1\), so the heavy part is \(O(G^{11/4}+G^2)\).
- *Light.* A tuple with a light role in a given variable costs at most \(\tau G^3\), by the determination property.

Hence, uniformly in \(\lambda\ne1\),
\[
 C(\lambda)\ll G^{11/4}+G^2+p^{-1/8}G^3=O(p^{11/8}).
\]

## Energy, slope products and propagation

From \(C(1)=\sum m^2\le G M_1\le G^3\),
\[
 E^\times(m)\le C(1)^2+\sup_{\lambda\ne1}C(\lambda)\,M_1^2=O(p^{27/8}),\qquad
 \sum_\xi W_\xi^{3/2}\le M_1E^\times(m)^{1/2}=O(p^{43/16}).
\]
Round 178's weighted point-plane step bounds the energy by the three sums \(\sum_\xi W_\xi^2/p\), \(\sum_\xi W_\xi^{3/2}\) and \(G(1+\log p)\sum_\xi W_\xi\). It depends on the distribution of \(\xi\) only through these sums, and every quantity is monotone in the weight. Substituting the new bounds verbatim gives:

| Quantity | New bound | Round 178 bound |
|---|---|---|
| Genuine right energy \(\mathcal E(\mu)\) | \(O(p^{43/16})\) | \(O(p^{11/4-3/836})\) |
| \(H_\alpha\), counting second norm over \(s\), uniform in \(t\) | \(O(p^{147/128})\) | \(O(p^{37/32-3/6688})\) |
| \(\sum w(t)\lvert H_\alpha\rvert^2\) | \(O(p^{179/64})\) | \(O(p^{45/16-3/3344})\) |
| One-match covariance | \(O(p^{115/64})\) | \(O(p^{29/16-3/3344})\) |

The one-match target is \(O(p^{96/64})\).

With the Round 176 generic maximum ([two-torus note](ordinary-two-torus-projective-overlap-176.md)), the fixed-slope first mass \(\sum_c\Delta(a,c)=C(a)\) is \(O(p^{11/8})\) for every \(a\ne1\). The fixed-\(a\) generic squared mass is therefore \(O(p^{19/8-1/1280-1/840})\).

## Limit of this route

These are statements about the method, not lower bounds for \(H_\alpha\).

- \(\sum_\xi W_\xi^{3/2}\ge M_1^3/\sqrt{p-1}\), and \(\mathcal E(\mu)\ge M_1^4/(p(p-1))\).
- The Rudnev–Shkredov second-norm route gives one-match output of size \(p^{1/8}\mathcal E^{1/4}M_1\), with the actual \(M_1\) throughout. This is the audit's correction of the draft, which mixed in the cap \(M_1\le p\).
- Therefore the route cannot reach \(O(p^{3/2})\) when \(M_1\gg p^{15/16+\varepsilon}\). When \(M_1\asymp p\) it stops at \(p^{13/8}\). Whether \(M_1\asymp p\) is not known.

The draft's reformulation of the target as a mean-subtracted level estimate is a sufficient heuristic, not a proved equivalence.

## Checks

[paley-180-audit-incidence-check.py](paley-180-audit-incidence-check.py) checks, exhaustively at \(p=13,17,29,37\) and for all \(\lambda\notin\{0,1\}\):
- distinctness of the lines;
- the determination property;
- the incidence identity for \(C^\sharp(\lambda)\), with random integer weights;
- \(\sum C^2=\sum W^2\) for the masked weight.

These are finite diagnostics. The synthetic-weight FFT runs in the draft were not replayed and are not evidence about the actual \(g\).

## Next tests

1. Bound the one-match term directly by slope fibres, using \(C(a)\) at fixed slope and the translation overlaps of the level sets, without passing through \(\mathcal E(\mu)\).
2. Improve \(\sup_{\lambda\ne1}C(\lambda)\) below \(p^{11/8}\) using the actual level-set structure.
