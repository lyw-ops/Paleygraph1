# Positivity and correctly scaled marginals can allow a large abstract quotient

The actual dual of [Round 168](ordinary-quotient-positive-dual-168.md) uses the genuine Jacobi projector and the true active set. The following abstract control retains the affine minimum and normalizations and shows why positivity with a small negative forcing cannot alone control its quotient. It is not an ordinary-prime construction.

Take \(1\ll T=o(\sqrt n)\), \(q=\alpha\sqrt n\) for fixed \(\alpha>0\), a marked copy of \(e_0\), and an unmarked index \(j\). Let \(k=\lfloor n/(64T)\rfloor\), \(l=n-k-2\). Define a real vector \(u\) by \(u_0=0,u_j=1\), by \(\sqrt{nT/k}\) on \(k\) other indices and by \(-(1+\sqrt{knT})/l\) on the remaining \(l\) indices. It has sum zero,
\(\|u\|_2^2=nT+O(n)\), and its negative entries stay above \(-1/4\) eventually. The positive bulk entries are \(O(T)=o(q)\). Put \(v=u/\|u\|\), \(\epsilon=v_j=1/\|u\|\), and \(\mathcal W=\mathbb Rv\).

Write \(\mathbf1_{\mathrm b}\) for the unmarked indicator, \(b=(n-q)/(n-1)\) and \(P\) for orthogonal projection on \(\operatorname{span}(e_0,\mathbf1_{\mathrm b},v)^\perp\). Set
\[
 F_A=q e_0+b\mathbf1_{\mathrm b}
               -\frac{b+1}{1-1/(n-1)-\epsilon^2}\,P e_j .
\]
Then \(F_A\perp v\), its mark is \(q\), its mass is \(n\), and its value at \(j\) is exactly \(-1\). At every other unmarked index its value is \(b+O(1/n)\): the correction there is bounded by a constant times \(1/(n-1)+|\epsilon v_i|=O(1/n)\). The minimum-norm nonnegative vector in the actual affine line of this model, \(F_A+\mathbb R u\), is \(F_A+u\). Indeed nonnegativity at \(j\) forces coefficient at least 1, and coefficient 1 is feasible at every other coordinate by the lower bound on the negative entries of \(u\). The resulting vector has true zero set \(\{j\}\) in the model, is nonnegative of mass \(n\), has mark \(q\), and remains under that mark at all unmarked entries.

Its correction is \(u=P_\mathcal W e_j/\epsilon^2\). Thus the true model dual uses exactly one positive coefficient; its normalized probability is \(\delta_j\) with forcing 1. The projected probability has squared norm \(\epsilon^2\), giving the normalized quotient penalty
\[
 \frac{1}{n\|P_{\mathcal W}e_j\|_2^2}
 =T+O(1).
\]
Even the entries of \(P_\mathcal W\) are \(O(T/n)=o(n^{-1/2})\) here. This relieves neither actual prime cost: the model imposes no Jacobi sector equation, positive complementary interpolation, or arithmetic compression geometry. It fixes the gap in the raw abstract example, whose claimed unconstrained affine representative was incompatible with the chosen full-dimensional direction space.
