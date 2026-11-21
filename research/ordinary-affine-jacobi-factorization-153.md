# Complete Jacobi sums for the true deficit-weighted moment

Use \(Q,G,n,\sigma,\rho=-\sigma\) and the genuine near-critical \(b\) from [Round 152](ordinary-affine-correlations-152.md). Thus \(b\ge0\), \(b_0=0\) at the marked Fourier coordinate, \(r=\mathbb E b>0\), \(\|L_\sigma b\|_{2,n}/r=o(1)\), and \(m_{\rm eff}\sim n/\sqrt p\). Put \(\nu_j=b_j/(nr)\) and \(f(y)=\sum_j\nu_j j(y)\) on \(Q\), zero elsewhere. Lift each \(j\) to its two characters of \(\mathbb F_p^\times\). Each lift \(\eta\) has weight \(w_\eta=\nu_{\eta|_Q}/2\). Treat every multiplicative character, including the trivial one, as zero at \(0\).

The actual pin gives the uniform cap \(\max\nu_j=O(p^{-1/2})\). Indeed
\[
 b-\rho Kb=2P_\sigma b+Jb,\qquad
 P_\sigma b=L_\sigma b+\frac{\ell^{\mathsf T}b}{\ell_0}\ell,\qquad
 \ell=P_\sigma e_0 .
\]
Here \(J\) averages. On the bulk, the rank-one term is \(O(r)\) pointwise by the Jacobi entry cap, and \(\|L_\sigma b\|_\infty\le\sqrt n\|L_\sigma b\|_{2,n}=o(\sqrt n\,r)\). The bound \(\|Kb\|_\infty\le\sqrt p\,r\) proves the cap. In particular this prevents rare spikes in the true lifted weights from dominating a trivial-character resonance.

## Removing the square restriction at cost \(O(p)\)

For any anchor \(a\in G\) and full lift \(\gamma\), define \(h_\gamma(x)=f(1-vx)\overline{\gamma(1-vx)}\) on \(\mathbb F_p\), where \(\chi(v)=\rho\). Its square restriction is the genuine \(g_a\). The removed squared mass is \(O(1)\), uniformly in \(a\). For a nonzero nonsquare \(x\), the contributing \(y=1-vx\in Q\) has \(\chi(1-y)=\sigma\), so this follows from \(\langle b,(I-\rho K)b\rangle_{2,n}=O(r^2)\) and Parseval. The value at \(x=0\) is \(1\).

Let \(C_a(u)\) denote the restricted correlation from Round 152 and \(C_\gamma^{\rm full}(u)\) its analogue summed over all \(x\in\mathbb F_p\). For \(u\in Q\), multiplication by \(u\) preserves the square and nonsquare sets, and
\[
 C_\gamma^{\rm full}(u)=C_a(u)+C_\gamma^{\rm ns}(u)+1 .
\]
The unnormalized multiplicative Fourier coefficients of \(g_a\) on \(Q\) are uniformly \(O(\sqrt p)\). To see this, expand \(h_\gamma\) in the full lifts with weights \(w\) and expand \(1_Q(x)\) by its two characters. Each coefficient is a weighted sum of ordinary two-factor Jacobi sums after scaling \(x\) by \(v\). The only term of size \(p-2\) requires both characters trivial, and its lift weight is \(O(p^{-1/2})\).

Identify the nonsquare coset with \(Q\) by a fixed nonsquare scalar. For this coset row \(r_\gamma\), one has \(\|r_\gamma\|_2^2=O(1)\). Multiplicative Parseval bounds the sum of \(C_a(u)\overline{C_\gamma^{\rm ns}(u)}\) over \(Q\) by \(\max|\widehat g_a|^2\,\|r_\gamma\|_2^2=O(p)\), using unnormalized transforms. The sum of \(C_a\) is \(|\widehat g_a(1)|^2=O(p)\). The square sum of \(C_\gamma^{\rm ns}+1\) is also \(O(p)\). Removing \(u=1\) changes their combined bound by \(O(\sqrt p)\) since \(\|g_a\|_2^2=O(\sqrt p)\) in the critical range. Hence the two squared-correlation sums over \(u\in Q\setminus\{1\}\) differ additively by \(O(p)\), uniformly in the anchor and lift.

## Factoring all three complete sums

Write \(J(U,V)=\sum_z U(z)V(1-z)\) over the full field. In \(C_\gamma^{\rm full}(u)\) use two lifted characters \(U,V\), and make the change \(1-vx=-(1-u)z/u\). The other argument is then \((1-u)(1-z)\). This gives
\[
 C_\gamma^{\rm full}(u)
  =\sum_{U,V}w_Uw_V J(\gamma/V,U/\gamma)\,
    (\gamma/V)(-1)\, (U/V)(1-u)\, (V/\gamma)(u).
\]
On expanding the square let \(U',V'\) be the second pair, put \(B=V/V'\), \(C=(U/V)/(U'/V')\), and write \(J_1,J_2\) for the first two Jacobi factors from the unprimed and primed variables. Summation over \(u\in Q\setminus\{1\}\) turns the last two factors into
\[
 \frac{J(B,C)+J(B\chi,C)}2 .
\]
The zero convention already removes \(u=0,1\). Thus the exact full moment is the weighted sum of \(J_1\overline{J_2}J(B\chi^e,C)\) times \((\gamma/V)(-1)\overline{(\gamma/V')(-1)}\), with \(e=0,1\) equally weighted. The anchor lift can be drawn with the same true weight \(w\), since the ambient correlation depends only on the quotient anchor.

## All fixed resonances cost \(O(p)\)

A Jacobi factor has modulus \(\sqrt p\) when both arguments and their product are nontrivial. The two-trivial value is \(p-2\), and every other degenerate value has modulus at most one. Fix the anchor and \(e\), and put \(\kappa=\max_\eta w_\eta=O(p^{-1/2})\). The three events with value \(p-2\) are
\[
 U=V=\gamma,\qquad
 U'=V'=\gamma,\qquad
 (U',V')=(U\chi^e,V\chi^e).
\]
Each has total probability at most \(\kappa^2\) under the four independent weights. Any two together determine the four variables, so their intersection has weight at most \(\kappa^4\). The absolute contribution with exactly one large factor is at most \(O(p^2\kappa^2)=O(p)\). Two or more contribute \(O(p^3\kappa^4)=O(p)\). With no large factor but some remaining degeneracy, the product is at most \(p\). These bounds hold for each anchor and so hold under its actual weight.

On the tuples with three nondegenerate factors the product is \(p^{3/2}\) times a phase. One may additionally remove any fixed finite list of relations of the form \(\prod_{j=0}^4\gamma_j^{d_j}=\xi\), where \((\gamma_0,\ldots,\gamma_4)=(\gamma,U,V,U',V')\), the bounded integer exponents are not all zero, and \(\xi\) is prescribed. Condition on all variables except one with \(d_j\ne0\). It has at most \(|d_j|\) possible values in the cyclic character group and probability \(O(\kappa)\). Hence the removed regular terms cost \(O(p^{3/2}\kappa)=O(p)\) for each fixed relation. Fixed collisions, inversions and balanced product identities are included in this argument.

Consequently the true deficit-weighted moment is \(p^{3/2}\) times the real weighted average of those regular phases, up to \(O(p)\), even after these finite exclusions. The desired upper is a real phase-average upper \(O(p^{-1/2})\) in the actual near-critical branch. The required \(\omega(p)\) lower from Round 152 must come from the regular terms, independent of the chosen fixed list. Complete Jacobi size bounds alone give \(O(p^{3/2})\) and leave the required cancellation open.

## The scalar correction for a true critical anchor

There is also a more precise comparison of the ambient and restricted moments. On the wrong-sign part of \(Q\), the exact pin identity gives
\[
 f(y)=c+e(y),\qquad
 c=\frac{\ell^{\mathsf T}b}{\ell_0 n r}=O(p^{-1/2}),\qquad
 \sum_{\substack{y\in Q\\ \chi(1-y)=\sigma}}|e(y)|^2=o(1).
\]
Here the inverse Fourier transform of \(\ell\) is the wrong-sector indicator for \(y\ne1\), and the last estimate follows from \(\|L_\sigma b\|_{2,n}/r=o(1)\). Therefore the nonsquare row \(r_\gamma\) is, within \(o(1)\) in counting second norm, the row \(c\,1_Q(1-vx)\overline{\gamma(1-vx)}\) on nonsquare \(x\). All anchors of positive true weight are nontrivial on \(Q\) because \(b_0=0\). Each unnormalized multiplicative coefficient of the template on the nonsquare coset is \(O(1)\) by the two-factor Jacobi bound, expanded in the two lifts, with no two-trivial term. The error row has Fourier supremum \(o(\sqrt p)\).

Thus the nonsquare square-correlation sum and nonsquare mean are \(o(p)\) by Parseval. The cross term with \(g_a\) is \(O(\|g_a\|_2^2)+O(p)\|e\|_2^2=o(p)\), using the template supremum and the \(O(\sqrt p)\) supremum of \(\widehat g_a\). The only remaining differences at order \(p\) are the \(x=0\) constant term and its cross with \(g_a\). Uniformly on supported anchors they give \((n-1)+2|\widehat g_a(1)|^2+o(p)\) after excluding \(u=1\).

The exact coefficient at the trivial multiplicative character is
\[
 \widehat g_a(1)
 =\tfrac12\left(n\nu_a-1+\rho\sqrt p\sum_j\nu_j k(j-a)\right).
\]
It follows by expanding the square indicator in \(y=1-vx\), where \(y=1\) is omitted. Near-critical flattening makes both \(n\nu_a/\sqrt p\) and \(\rho\sum_j\nu_j k(j-a)\) tend to one in true-anchor probability. For the first use the \(\ell^1\) uniform approximation on the near-flat set and its size \((1+o(1))n/\sqrt p\). For the second use the vanishing within-set phase deficit. The uniform cap permits averaging the squared coefficient. Thus the full-field true anchor moment exceeds the restricted one by \((5/2+o(1))p\). This correction has the same size as the degenerate terms and cannot supply the known superlinear growth.
