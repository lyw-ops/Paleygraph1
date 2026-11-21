# An affine-action power gain on the full physical slope diagonal

Use the genuine completed nonnegative majorant \(P_s\) of [Round 166](ordinary-regular-character-collisions-166.md), with the true \(g=|f|^2\), outer \(w=g(1-g)\) and full lift \(\omega\). Thus \(G=\sum g=O(\sqrt p)\), \(0\le g,w\le1\), and \(\sum_s w(s)\le G\). Keep the actual physical mark and the square restriction. The following is a bound on the full diagonal, independent of the matching split:
\[
 \sum_{s\ne0,1} w(s) P_s^2=O(p^{19/8}).
\]
The elementary pointwise \(O(G^2)\) bound with the true \(w\) gives \(O(p^{5/2})\). The required estimate is \(O(p^{3/2})\), so this gain does not close the slope criterion.

## Exact action after inverting the output coordinate

Off the two priced zero endpoints, use the \((r,b)\) chart of [Round 171](ordinary-affine-line-energy-171.md) from the actual nonzero \(Y,D\ne1\), \(Y\ne D\):
\[
 r=\frac{Y-D}{1-D},\qquad b=\frac{D(1-Y)}{Y(1-D)},\qquad
 s=b+\frac r E,\qquad C=E D/Y,\qquad A=sE .
\]
Since \(b=(D/Y)u^{-1}\) and \(Y,D\in Q\) on nonzero terms, the exact physical square mask is \(b\in Q\). Write \(X=1/s\) and
\[
 \frac1A=\frac1r-\frac b r X=: j_{Y,D}(X),\qquad
 C=\frac{A D X}{Y}.
\]
Here \(r,b\ne0\). At \(X\ne0,1\), use zero extension at \(j_{Y,D}(X)=0\). That is precisely the excluded pole \(s=b\). The previously priced \(A=1\) boundary can be completed positively. The other zero endpoint remains removed by \(Y,D\ne1\). Extend the resulting upper to \(X\) on the entire field by the formula below.

Let \(h(e)=g(e^{-1})\) for \(e\ne0\), \(h(0)=0\), and \(h_\beta(e)=h(e)\beta(e^{-1})\), zero also at \(e=0\). Open only \(g(C)\) using the true full-lift character law. For any selected set of pairs \(Y,D\), the completed contribution as a function of \(X\) is exactly
\[
 \sum_\beta \omega(\beta)\beta(X)
       \sum_{\substack{Y,D \text{ selected}\\ b\in Q}}
       g(Y)g(D)\beta(D/Y)\ h_\beta(j_{Y,D}(X)).
\]
Every character, including the trivial one, is extended by zero at \(X=0\). On nonzero \(X\), this identity follows from \(C=A(D/Y)X\); at \(X=0\) both are set to zero. The inner operators are affine permutation actions, up to taking the group inverse to match the convention of Round 171. The unrestricted constant contribution is \(O(G^3/\sqrt p)\) in second norm for each \(\beta\). Indeed the pair coefficient mass is at most \(G^2\) and the input mean has second norm at most \(G/\sqrt p\). The outer factor \(\beta(X)\) only decreases counting second norms.

## Affine energy with the projective change of parameters

The new transformations have parameters \((r',b')=(-b/r,1/r)\). This is the restriction of an invertible projective transformation on the parameter plane to \(r\ne0\). It is injective. Every target parameter line pulls back to a line in the original \((r,b)\) chart, or to a set empty in the affine domain. With first-coordinate level set size \(U\) for \(Y\) and second-coordinate size \(V\) for \(D\), Round 171 gives at most \(\min(U,V)\) points on old vertical lines and at most \(2V\) on any other old affine line. Both the new vertical and the new arbitrary line bounds are therefore at most \(2V\). The energy bound applies to the transformations \(j_{Y,D}\) themselves. Passing to inverse actions in the operator norm argument is harmless because \(h\mapsto h\circ j\) is the adjoint of the standard unitary action of \(j\); conjugating the coefficients and taking the adjoint preserves the norm.

Use the primary affine-energy theorem and its group Plancherel consequence exactly as in Round 171. More explicitly, for a level set of lines of size at most \(UV\), the fourth root of its energy is \(O(U^{5/8}V^{3/4}+U^{1/2}V^{3/4})\) when \(2V|\mathcal L|\le p^2\). [Petridis, Roche-Newton, Rudnev and Warren, Theorem 2.1](https://arxiv.org/abs/1911.03401)

For \(\tau=p^{-1/8}\), retain heavy pairs with \(g(Y),g(D)>\tau\). Layer cake only uses levels with \(U,V\le G/\tau=O(p^{5/8})\), so the energy theorem's condition holds eventually. The bounds \(U\le G/a,V\le G/d\) for threshold parameters \(a,d\in(0,1)\) are integrable to the displayed exponents. This gives mean-zero operator norm \(O(p^{1/4}(G^{11/8}+G^{5/4}))=O(p^{15/16})\) for each \(\beta\), uniformly with the actual phases and the actual \(b\)-square mask. Since \(\|h_\beta\|_2\le\sqrt G\) and \(\sum_\beta\omega(\beta)=1\), the exact completed heavy diagonal has second norm \(O(p^{19/16})\) after the input constant is included. Inversion \(s\leftrightarrow X\) preserves counting norms away from zero. Multiplying by \(\sqrt{w(s)}\) can only reduce that norm, giving heavy cost \(O(p^{19/8})\).

For light pairs, reuse the true pointwise pins of Round 171 with \(t=s\). If \(g(Y)\le\tau\), at fixed \(s,C,D\) there is at most one \(Y\); if \(g(D)\le\tau\), at fixed \(s,C,Y\) the nonzero \(D\) satisfies the stated monic quadratic. Hence the light part is \(O(\tau G^2)\) pointwise, and now the single diagonal sum costs \(O(\tau^2 G^5)=O(p^{9/4})\). The named endpoint errors cost \(O(p^{3/2})\). These bounds prove the displayed full diagonal estimate by the triangle inequality in the actual weighted norm.

This bound uses the explicit Möbius modulation of the diagonal and does not infer a diagonal restriction from the two-dimensional norm. The light estimate already reaches \(O(p^{3/2})\) if \(\tau\le p^{-1/2}\), but the current layer-cake operator bound would still be too large and its size test would not cover all such levels. Even an optimistic \(O(p^2)\) affine energy at the main levels would yield only \(O(p^2)\) via this unweighted second-norm argument. Reaching \(O(p^{3/2})\) needs further use of the output weight or a different estimate for the true twisted input and output together.

## Stronger bound from incidence on the same diagonal

There is a stronger conclusion if the fourth weight is completed positively at this stage. Keep the genuine \(b\in Q\) constraint but use \(g(C)\le1\), so the heavy upper only has weights \(g(Y)g(D)h(j_{Y,D}(X))\), where \(h(e)=g(e^{-1})\). For an arbitrary output set \(T\subset\mathbb F_p\), test the sum of this upper on \(T\). At a level \(S\) of the input \(h\) the count is a point-line incidence for \(S\times T\), using the inverse graphs \(X=j_{Y,D}^{-1}(e)\). Inversion of affine transformations is itself projective on the parameter plane \((a,b)\), via \((1/a,-b/a)\). Thus both line multiplicity bounds \(2V\) still hold for the inverse graphs. Every graph has nonzero slope.

The finite-prime-field incidence bound from the same primary paper is
\[
 I(S\times T,\mathcal L)\ll
 |T|^{1/2}\bigl(|S|^{5/8} E(\mathcal L)^{1/8}|\mathcal L|^{1/2}
       +|\mathcal L|\max\{1,|S|/\sqrt p\}\bigr).
\]
See [Petridis, Roche-Newton, Rudnev and Warren, Theorem 1.1, equation (4)](https://arxiv.org/abs/1911.03401). Use the exact level range from the heavy cut, so the energy theorem applies to these inverse graphs. The factor \(E(\mathcal L)^{1/8}|\mathcal L|^{1/2}\) is at most a constant times
\(U^{13/16}V^{7/8}+U^{3/4}V^{7/8}\). Layer cake on the three weights is summable without loss: each of these exponents and the input exponent \(5/8\) is less than one, and the size of each level at threshold \(a\) is at most \(G/a\). The first incidence term is therefore at most \(O(|T|^{1/2}G^{37/16})\). For the second term use the exact integrals of the cardinalities, so that \(\int_0^1|\{h>a\}|\,da=G\) and \(\iint|\mathcal L|\,da\,dd\le G^2\). This gives \(O(|T|^{1/2}G^2(1+G/\sqrt p))\). The extra square mask only reduces the incidence sets.

The resulting bound for every output set is \(O(|T|^{1/2}p^{37/32})\). Sort the nonnegative heavy upper in decreasing order. Its \(k\)-th value is \(O(p^{37/32}/\sqrt k)\) by the bound on its largest \(k\) sites. Consequently its squared second norm is \(O(p^{37/16}(1+\log p))\). The actual outer \(w\le1\) can reduce this value, and the light term and endpoint errors were already smaller. Thus the stronger full diagonal result is
\[
 \boxed{\displaystyle \sum_{s\ne0,1}w(s)P_s^2
        =O\bigl(p^{37/16}(1+\log p)\bigr).}
\]
Here the incidence estimate is applied to a genuine positive upper on the same physical diagonal. It does not give a \(p^{3/2}\) estimate, and the proof does not use special localization of the output on the actual moderate \(g\)-set.

## An improvement of the two-dimensional one-match energy

The same incidence argument gives a smaller exponent for the full twisted kernel as well. For fixed \(t\), use the exact \(s=b+r e\) chart and \(h_t(e)=g(t/e)\) from Round 171. In the positive upper omit \(g(C)\) and retain the \(b\)-square restriction. The graphs are \(s=b+re\) themselves, with \(e\) the input coordinate of the incidence grid. The original multiplicity bounds \(m_{\mathcal L},M_{\mathcal L}\le2V\) apply.

For this application one may remove the lower threshold on \(g(Y),g(D)\). In the paragraph after Theorem 2.1, the primary paper states the prime-field extension without the size test, adding \(O(m_{\mathcal L}|\mathcal L|^3/p)\) in the equal-set case. Its extra contribution to \(E^{1/8}|\mathcal L|^{1/2}\) is bounded by \(O(p^{-1/8}U^{7/8}V)\). The first two energy terms still integrate as above. The exponent one on \(V\) costs at most \(G\) by the exact layer-cake integral \(\int_0^1V(d)\,dd\le G\), and the \(U\) and input exponents \(7/8,5/8\) are integrable. Thus the extra term in the incidence test on any \(T\) is
\[
 O\bigl(|T|^{1/2}p^{-1/8}G^{5/2}\bigr)
   =O\bigl(|T|^{1/2}p^{9/8}\bigr).
\]
It is smaller than the existing \(O(|T|^{1/2}p^{37/32})\) bound. No physical light contribution is then needed for this incidence variant. For each \(t\), rearrangement gives the squared bound \(O(p^{37/16}(1+\log p))\) as above, uniformly in \(t\). The true \(w(t)\) sum gives
\[
 \sum_{s\ne0,1,t} w(t)|H_\alpha(s,t)|^2
       =O(p^{45/16}(1+\log p)).
\]
The prior endpoint errors are smaller. Translating to the matching-number-one covariance gives \(O(p^{29/16}(1+\log p))\), including the old \(O(p^{3/2})\) error. This improves \(O(p^{15/8})\), still above \(O(p^{3/2})\). The same no-threshold extension also works for the diagonal incidence argument, with its stated exponent unchanged.
