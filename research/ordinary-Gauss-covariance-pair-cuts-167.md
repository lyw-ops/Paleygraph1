# Paired Gauss factors in the true regular slope covariance

Use the actual positive completed collision majorant and the regular triple Jacobi transform of [Round 166](ordinary-regular-character-collisions-166.md). All characters are on \(\mathbb F_p^\times\), \(m=p-1\), the two outer square lifts are \(i=0,1\), \(\kappa=\max\omega=O(p^{-1/2})\), and \(\ell=\omega-\omega*\omega\). Write \(G(\chi)=\sum_{x\ne0}\chi(x)e_p(x)\) and \(g_\chi=G(\chi)/\sqrt p\), including \(g_1=-p^{-1/2}\). Regular factors have \(|g_\chi|=1\). Do not confuse these normalized Gauss values with the physical multiplier \(|f|^2(1-|f|^2)\).

## Phase coordinates

On each regular tuple and its regular Mellin frequency \(\psi\), the three-Jacobi product divided by \(p^{3/2}\), including its actual sign at \(-1\), equals
\[
 C_i(\alpha,\beta,\gamma,\delta)\,
 g_{\alpha/\psi}g_{\delta/\psi}
 \overline{g_{\bar\beta/\psi}\,g_{\bar\gamma/\psi}},
\]
where \(C_i\) has modulus one, is independent of \(\psi\), and can be written as
\[
 C_i=(\beta\gamma)(-1)\,
 \overline{g_{\chi^i\alpha\gamma}}\,
 g_{\alpha\beta\gamma\delta}\,
 \overline{g_{\chi^i\beta\delta}\,g_{\gamma\delta}\,g_{\alpha\beta}} .
\]
This follows from \(J(a,b)=G(a)G(b)/G(ab)\) on the checked regular set and \(g_{\bar a}=a(-1)\overline{g_a}\). The first three factors of \(C_i\) including \((\beta\gamma)(-1)\) are genuine fixed factors, not a simplification of the actual probability law. The plus numerator labels \(\{\alpha,\delta\}\) are disjoint from the minus labels \(\{\bar\beta,\bar\gamma\}\) within a single regular tuple: coincidence would impose one of \(\alpha\beta,\alpha\gamma,\beta\delta,\gamma\delta=1\), all excluded in Round 166.

At fixed \(h=\psi'/\psi\), open the two independent four-character draws. The covariance sum over \(\psi\) has four plus factors with labels
\[
 \alpha,\delta,\bar\beta'/h,\bar\gamma'/h
\]
and four minus factors with labels
\[
 \bar\beta,\bar\gamma,\alpha'/h,\delta'/h .
\]
All moving arguments divide these labels by \(\psi\). The fixed ratio factors are \(C_i\overline{C_{i'}}\). At most eight \(\psi\)'s are removed by the two inner regular Mellin cuts. Each exact opposite-side match cancels on the regular frequencies. As matches are necessarily across the two independent draws, \(j\) disjoint matches impose \(j\) equality conditions between disjoint pairs of independent draws at fixed \(h\). Their probability is \(O(\kappa^j)\), including repeated labels by a union over finitely many matchings.

## Two or more matches are within the target scale

For a complete sum over \(\psi\) with \(r\) residual factors on each side and disjoint multisets \((A_j)_{j=1}^r,(B_j)_{j=1}^r\), multiplicative orthogonality first gives \(\prod x_j=\prod y_j\) in the additive Gauss expansion. Put \(x_j=t_j y_j\). Since every \(A_j\bar B_j\) is nontrivial, any \(t_j=1\) gives zero after summing \(y_j\). Thus the complete sum is exactly
\[
 \frac{m}{p^r}\prod_j G(A_j\bar B_j)\!
 \sum_{\substack{t_1\cdots t_r=1\\t_j\ne1}}
 \prod_j A_j(t_j)\,\overline{A_j\bar B_j}(t_j-1).
\]
Any removed \(\psi\)'s cost at most eight in the completed residual product, since all normalized Gauss moduli are at most one.

For \(r=2\), write the plus labels \(A,D\) and minus labels \(B,C\). Substitution \(t_2=t_1^{-1}\) gives the final exact factor
\[
 (\bar A B)(-1)\,J(A\bar C,BC/(AD)).
\]
Here \(A\bar C\ne1\). The complete correlation is therefore \(O(\sqrt p)\). For \(r=1\), the residual correlation is exactly zero since the product constraint forces \(t_1=1\). For \(r=0\) the regular sum is at most \(m\).

The true quadratic form has prefactor \(p^3/m\) after the above Gauss normalization and \(\|\ell\|_1\le2\). Consequently the contributions of exactly two matches, exactly three matches, and four matches are bounded separately in absolute value by
\[
 O(p^{5/2}\kappa^2),\qquad O(p^2\kappa^3),\qquad O(p^3\kappa^4),
\]
respectively. All are \(O(p^{3/2})\) with the genuine cap, independent of the sign of \(\ell(h)\). This is an exact arithmetic removal on the actual completed majorant, including both outer lifts. The zero-match and one-match classes, with \(r=4\) and \(r=3\), still require a weighted estimate. Uniformly bounding their individual complete correlations without using the outer weights would not supply enough savings in general.

## Completing the remaining two classes

The frequency deletions can also be charged before attacking the last two classes. When there is no match, the completed product at any removed \(\psi\) has at least one \(g_1=-p^{-1/2}\), while every other \(|g_\chi|\le1\). Thus the omitted complete-sum contribution has size \(O(p^{-1/2})\) for each tuple. With prefactor \(p^3/m\) its total costs \(O(p^{3/2})\). When there is one match, the residual completed product is only bounded by one at a removed frequency, but the match probability \(O(\kappa)\) again pays \(O(p^{3/2})\). This reduces both surviving classes to their complete sums at the target error scale. For the one-match class an \(O(1)\) bound on the signed \(\ell,\omega\) average of the \(3+3\) residual sum after extracting the single match probability would suffice. The zero-match class has no such probability gain.
