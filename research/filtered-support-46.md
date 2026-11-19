# Weighted uncertainty from translated forbidden masks

For every sufficiently large eligible prime, a feasible positive row with a normalized mark bounded below must have positive bulk mass outside certain Bohr arcs in every generator direction. In particular an actual larger-theta endpoint cannot put its bulk support in one such arc with only \(o(p^{1/6}/\log p)\) exceptions. The proof uses a logarithmically growing intersection of forbidden masks and controls the effect of an error on the original forbidden mask. The unstructured endpoint case remains open.

## Filtering an affine spectrum

Write \(n=(p-1)/2\), \(Q=(\mathbb F_p^\times)^2\), \(G=\widehat Q\). For \(x\in\mathbb C^G\) use \(\widehat x(t)=\sum_{\gamma\in G}x_\gamma\gamma(t)\) and counting norms on \(G\). Let \(D=\{t\in Q:\chi(1-t)=-\sigma\}\) be the forbidden mask. A row of sign \(\sigma\) has \(\widehat x=0\) on \(D\). For distinct \(a_1,\ldots,a_k\in Q\), a complex filter with coefficients \(c_j\) and the common forbidden set are

\[
 P(\gamma)=\sum_{j=1}^k c_j\gamma(a_j),\qquad
 D_A=\bigcap_{j=1}^k a_j^{-1}D.
\]

There is an absolute \(C\) such that

\[
 \left||D_A|-n2^{-k}\right|\le C k\sqrt p,\qquad
 \max_{\gamma\ne1}\left|\sum_{t\in D_A}\gamma(t)\right|\le C k\sqrt p.
\tag{1}
\]

Indeed expand \(2^{-k}\prod_j(1-\sigma\chi(1-a_jt))\) on \(Q\). It agrees with the indicator outside the at most \(k\) roots, and is between zero and one everywhere. The empty term sums to \(n\), or to zero with a nontrivial \(\gamma\). For every nonempty term, extend \(\gamma\) to \(\mathbb F_p^\times\) and use \((1+\chi(t))/2\) to select \(Q\). Each resulting character sum is the sum of a single generator character applied to a product of a power of \(t\) and powers of distinct linear factors \(1-a_jt\). At every selected nonzero root the exponent is \((p-1)/2\), so the polynomial is not a \((p-1)\)-st power. The distinct-root form of the multiplicative Weil bound costs \(O(k\sqrt p)\), uniformly also in the exponent at zero. Restriction to nonzero \(t\) costs at most one. Averaging the \(2^k-1\) bounds and adding the root discrepancy gives (1). [Weil's character sum bound](https://doi.org/10.1073/pnas.34.5.204)

Put \(z_\gamma=P(\gamma)x_\gamma\), \(\Pi_D x=\mathcal F^{-1}(\mathbf1_D\widehat x)\), and \(C_P=\sum_j|c_j|\). On \(D_A\) one has \(\widehat z(t)=\sum_j c_j\widehat x(a_jt)\). The triangle inequality for the norm with squared weight \(1/n\), then Parseval on \(D\), give

\[
 n^{-1}\sum_{t\in D_A}|\widehat z(t)|^2 \le C_P^2\|\Pi_D x\|_2^2 .
\]

Expand the left side by pulling out its diagonal terms and use (1) on every off-diagonal term. For all \(k\) such that \(C k\sqrt p\le n2^{-k-1}\), this gives

\[
 \|P x\|_2^2
 \ \ll\ \frac{k2^k}{\sqrt p}\|P x\|_1^2
       +2^k C_P^2\|\Pi_D x\|_2^2.                                 \tag{2}
\]

The constants are independent of the filter and field. The size condition holds, for example, uniformly at \(k\le \tfrac14\log_2 p\) for large \(p\). In the exact cone, (2) tests a filtered portion of the row without creating any error from the size of the unfiltered part. A filter that is uniformly small on a high-mass part of the row can therefore detect a small remainder. The factor \(2^k\) records the thinning of the simultaneous mask.

## A long-order direction at the exact mark

Let \(x\ge0\), \(\widehat x|_D=0\), \(\sum x_\gamma=\sqrt n\), and \(\alpha=x_1\ge a>0\), where \(a\) is fixed. Choose any \(g\in Q\) of order greater than

\[
 r=\left\lceil \tfrac16\log_2 p+\log_2\log_2 p\right\rceil .
\]

Use \(P(\gamma)=((1+\gamma(g))/2)^r\), which has \(C_P=1\), coefficients at \(r+1\) distinct positions, and \(P(1)=1\). Let \(\mu=x/\sqrt n\), and isolate the bulk outside the indicated arc by

\[
 I_g=\{\gamma:|1+\gamma(g)|\le1/2\},\qquad
 \eta_g=\mu(G\setminus(I_g\cup\{1\})).
\]

Here \(1\notin I_g\), the filter has magnitude at most \(4^{-r}\) on \(I_g\), and its magnitude is at most one everywhere. Consequently

\[
\begin{split}
 \alpha &\le \|P x\|_2\\
 &\ll \sqrt{r+1}\,2^{r/2}p^{1/4}
     \left(4^{-r}+\frac{\alpha}{\sqrt n}+\eta_g\right).
\end{split}                                                        \tag{3}
\]

The prefactor is \(O(p^{1/3}\log p)\), and its product with \(4^{-r}\) is \(O((\log p)^{-1})\). Its product with \(1/\sqrt n\) tends to zero, so the mark term is absorbed. For every such \(g\) and all sufficiently large \(p\),

\[
 \eta_g\gg_a p^{-1/3}/\log p.                                       \tag{4}
\]

At an actual optimum every coordinate is at most its root value \(\alpha\), by translating any coordinate to the root. For the larger-theta sign one has \(\alpha\ge1\), and the Jacobi bound gives \(\alpha=O(1)\). Thus (4) forces at least \(c p^{1/6}/\log p\) active bulk coordinates off \(I_g\), in each long-order direction. The condition is weak on arbitrary dense sets and gives no \(o(D(p))\) bound for either atom term on the exact face. Its gain is a weighted exclusion even when all but a small number of support coordinates lie in the arc. For approximate rows (2) quantifies the incurred error rather than relocating the marked coefficient.

For \(k\) fixed this argument also works over square fields, and its proof through logarithmic \(k\) uses no prime-specific estimate beyond the same Weil bound. In particular (4) cannot rule out the diffuse-in-direction subfield obstruction. The complementary subgroup comparison in this round uses the separate prime clique cap.
