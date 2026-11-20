# The single-repair reciprocal cubic and a Legendre trace sum

Use the actual late repair and true reciprocal factors from [Rounds 112–115](residual-level-bands-115.md). All norms and means below are normalized. Write \(m=\mathbb E_n h\), \(\mu=\mathbb E_n g=\mathbb E_n g_-\), \(u=\epsilon Kh\), \(A=u(0)\), and \(q=\sqrt n\mu\). The weights \(\pi,\omega,\omega^-\) are \(h/(nm),g/(n\mu),g_-/(n\mu)\). In particular \(\mathbb E_n(hg)\asymp n^{-1/2}\), \(\mathbb E_n(hg_-)=O(n^{-3/4})\), \(\|u-h\|_{2,n}=O(n^{-1/2})\), and \(h(0)=0\). Set \(w=hg/(n\mathbb E_n(hg))\). This is a probability on the actual favored overlap, with \(\max w=O(n^{-1/2})\). Write \(k=\lambda/\sqrt p\) and \(z=\epsilon k\) as before.

## Keep the one potentially leading collision

Let \(M=\mathbb E_n[u(Kg)(Kg_-)]\) and denote its expansion over **distinct** shifts by
\[
 M_{\rm dist}=\epsilon (\sqrt p)^3 m\mu^2
       \sum_{a,b,c\,\mathrm{distinct}}\pi_a\omega_b\omega_c^- T_3(a,b,c).
\]
This cubic has one repair draw and both true stationary draws. The exact product identity and Cauchy–Schwarz give
\[
 M=\mu\mathbb E_n(hg)-\frac{1-t/n}{n}A+O(n^{-5/4}).
\]
Indeed \(\mathbb E_n|u-h|g+\mathbb E_n|u|g_-=O(n^{-3/4})\) by \(\|g\|_{2,n}+\|g_-\|_{2,n}=O(n^{-1/4})\) and the true overlap with \(g_-\); also \(\mathbb E_n|u|=O(n^{-1/2})\).

The \(h,g_-\) and \(g,g_-\) collision masses are respectively \(O(n^{-3/4})\) and \(O(n^{-1})\). For each exactly-two-equal pattern, Katz gives \(O(p^{-1/2})\) pointwise, so these two contributions are \(O(n^{-5/4})\) in total. The all-equal mass is at most \(\|\omega\|_\infty\sum_y\pi_y\omega^-_y=O(n^{-5/4})\). Retain the \(h,g\) equal pair, with the opposite draw unconstrained. Summing this pair exactly by \(Kg_-=-\epsilon(g_--\mu)\) gives the contribution
\[
 -\frac pn\,\mu\mathbb E_y\left[h_y g_y\left(\sum_x\omega_x^- k(x-y)^2-v_n\right)\right],
 \qquad v_n=\mathbb E_n k^2=\frac{n-1}{p}.
\]
The normalization for \(v_n\) follows by taking the diagonal of \(K^2=I-J_0\) and using \(K_{xy}=\sqrt p\,k(x-y)/n\). Subtracting the collision cancels the constant baseline up to \(\mu\mathbb E_n(hg)/n=O(n^{-2})\). Hence
\[
 \boxed{\ n M_{\rm dist}=p\mu\mathbb E_n(hg)\,\mathcal L -(1-t/n)A+O(n^{-1/4}),\quad
       \mathcal L=\sum_{x,y}\omega^-_x w_y k(x-y)^2\ .\ }             \tag{1}
\]
In the actual trimmed residual branch, \(A\to0\), and the prefactor \(p\mu\mathbb E_n(hg)\) is comparable to one. Thus \(M_{\rm dist}=o(n^{-1})\) there if and only if \(\mathcal L\to0\). This means that almost all of the corresponding weighted *pairs* must have Jacobi difference near zero, not merely that the anchored source level concentrates. The positive anchored level also transfers from \(h^2g\) to \(hg\): weighted Cauchy–Schwarz gives \(\mathbb E_n[hg|W|]\le(\mathbb E_n h^2gW^2)^{1/2}(\mathbb E_n g)^{1/2}=o(n^{-1/2})\), hence \(\mathbb E_w|W|\to0\).

## Conversion to a restricted Legendre family

For a positional element \(v\in Q\), let \(s(v)=\chi(1-v)\) and \(\widehat{w}(v)=\sum_{y\in G}w_y y(v)\), using the same Fourier convention for \(\omega^-\). The normalized positional coefficients of \(k^2\) are
\[
 c(v)=\frac1p\sum_{a\in Q}s(a)s(v/a).
\]
For \(v=1\), this is \((n-1)/p\). For \(v\ne1\) in \(Q\), define \(a_p(v)=p+1-\# E_v(\mathbb F_p)\) for the Legendre curve \(E_v:Y^2=X(X-1)(X-v)\). Then
\[
                          c(v)=\frac{-2-a_p(v)}{2p}.                 \tag{2}
\]
Indeed \(s(a)s(v/a)=\chi((1-a)(a-v))\) for square \(a\). Inserting the square indicator on nonzero \(a\) makes the unweighted quadratic character sum \(-2\) after removal of the \(a=0\) value \(1\). The weighted part is the full cubic character sum \(-a_p(v)\) since its \(a=0\) term vanishes and \(\chi(-1)=1\). The exact opposite sector of \(g_-\) gives \(\widehat{\omega^-}(v)=0\) when \(v\ne1\) and \(s(v)\ne-\epsilon\). Fourier inversion therefore yields
\[
 \mathcal L=\frac{n-1}{p}-\frac{1}{2p}
       \sum_{\substack{v\in Q\\s(v)=-\epsilon}}(a_p(v)+2)
           \widehat{\omega^-}(v)\overline{\widehat w(v)}.           \tag{3}
\]
The sum is real by symmetry. The constant 2 contributes \(O(p^{-1})\) using the reciprocal identity at the unmarked coordinates: \(\sum_y \omega_y^- w_y=tm/(n^2\mu\mathbb E_n(hg))=O(n^{-3/2})\). Positional orthogonality thus gives \(\sum_{v\ne1}\widehat{\omega^-}(v)\overline{\widehat w(v)}=-1+O(n^{-1/2})\). Write \(\mathcal T=p^{-1}\sum_{s(v)=-\epsilon}a_p(v)\widehat{\omega^-}(v)\overline{\widehat w(v)}\). An upper below 1 with fixed margin for \(\mathcal T\) would force \(\mathcal L\) bounded below. Pointwise Hasse and Parseval give only an order-one upper. The true opposite sectors give the needed margin by another argument.

## Exact all-translate spreading for the true pair

The true normalized stationary laws have disjoint nonconstant positional spectra, since their centered rows belong to opposite eigenspaces. Translation in the frequency group commutes with \(K\). Consequently the exact uniform pair identity holds at **every** difference \(d\):
\[
                 \sum_y\omega_y\omega^-_{y+d}=1/n.
\]
Equivalently, \(\mathbb E_n[g_y g_-(y+d)]=\mu^2\), including the marked coordinates. Moreover \(w_y\le C_0\omega_y\) pointwise with \(C_0=\|h\|_\infty\mu/\mathbb E_n(hg)=O(1)\). Thus its paired difference law \(R_d=\sum_y w_y\omega^-_{y+d}\) has \(R_d\le C_0/n\). This exploits the actual two true factors and requires no uniformity assumption on the repair law by itself.

The unweighted \(k\)-values tend to the arcsine law on \([-1,1]\) as \(p\to\infty\). In the two-lift formula of [the Fourier notes](fourier.md), \(k\) is the real part of \(J(\alpha,\chi)/\sqrt p\) away from the bounded exceptions, and the two lifts are conjugate. The fixed quadratic-character case of [the Jacobi equidistribution theorem](https://arxiv.org/abs/1809.04286) applies on full characters. Averaging the real parts therefore gives the same limit on the quotient. For a fixed \(C\ge\sup C_0\), choose \(b=\sin(\pi/(2C))\). The bound \(\mathcal L\ge b^2-C\mathbb E_n(b^2-k^2)_+\) and the arcsine law give
\[
 \liminf \mathcal L\ge \frac12-\frac{C\sin(\pi/C)}{2\pi}>0.
\]
The expression is the arcsine integral over the fraction \(1/C\) closest to zero, multiplied by \(C\). Formula (3) now gives a fixed upper margin below 1 in the restricted weighted Legendre trace sum.

By (1), throughout the actual trimmed residual branch where \(A\to0\), the signed distinct reciprocal cubic with a **single repair draw** obeys \(M_{\rm dist}\gtrsim n^{-1}\). Thus simultaneous small signed trimmed moments and \(M_{\rm dist}=o(n^{-1})\) are inconsistent on this actual obstruction. The arithmetic upper required for this remaining cubic is open. The strict Legendre upper here is a deduction from the exact uniform translate identity and unweighted equidistribution; it is not a power-saving estimate for the distinct cubic itself.

## The opposite singleton and the fully unmarked sum

In the distinct cubic, the repair mark is absent. For the opposite draw at zero, the complete contribution is \(c_-\mathbb E_n[u(g-\mu)z]=c_-\mathbb E_n[hg z]+O(n^{-5/4})\) by stationarity and the late \(2\)-norm error. Here \(c_-=g_-(0)\sqrt p/n\). The only possible removed pairs are the two other draws equal, of mass at most \(O(n^{-1/2})\) before conditioning on the marked atom of size \(O(n^{-1/2})\), or the favored draw also at zero. The Katz bound for two equal shifts with the other distinct, and \(h(0)=0\), make these errors \(O(n^{-3/2})\). For a favored draw at zero the complete term is \(O(n^{-5/4})\) from \(\mathbb E_n|u Kg_-|=O(n^{-3/4})\) and its column size \(O(n^{-1/2})\); the removed ties have smaller order by the same collision bounds. Thus if \(M_{\rm dist}^{\circ}\) denotes the all-unmarked distinct expansion, the level concentration \(\mathbb E_w |W|\to0\) gives
\[
 n M_{\rm dist}=n M_{\rm dist}^{\circ}+n\mu\mathbb E_n(hg)+o(1),\qquad
 n M_{\rm dist}^{\circ}=-n\mu\mathbb E_n(hg)\,\mathcal T+o(1)
\]
on the residual branch. In particular, a small fully unmarked cubic alone does not supply the small **full** cubic required to rule out that branch. It would leave the positive singleton. Full cancellation would require a negative bulk term with exactly the same leading magnitude as that singleton. The Legendre upper prevents this proposed balance under the residual hypotheses. The unresolved question is whether an independent prime estimate forces the full signed cubic to be small, or eliminates the residual by another consequence of the actual orbit.
