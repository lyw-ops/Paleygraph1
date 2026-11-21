# Growth of paired quotients under the actual projective maps

Let \(X\subset\mathbb F_p^\times\), \(N=|X|\le\sqrt p\), and let \(\phi(x)=(ax+b)/(cx+d)\) with \(abcd(ad-bc)\ne0\). Suppose \(\phi(X)\subset\mathbb F_p^\times\). Then
\[
 \max\{|X/X|,\ |\phi(X)/\phi(X)|\}\gg N^{18/17}
\]
with an absolute constant. Here every point of \(X\) is a genuine nonzero, finite input and output.

Put \(U=X/X\), \(V=\phi(X)/\phi(X)\), write \(D_u(x)=ux\), \(M_v=\phi^{-1}D_v\phi\), and take \(\mathcal T=\{D_uM_v:u\in U,v\in V\}\) in \(\mathrm{PGL}_2(\mathbb F_p)\). The two diagonal tori intersect only in the identity, since their respective two fixed points differ and a nonidentity projective map has at most two fixed points. Thus \(|\mathcal T|=|U||V|\). For every \(x,y,z\in X\), choose \(v=\phi(y)/\phi(x)\), \(u=z/y\). This gives the incidence \(D_uM_v(x)=z\), and the triple is recovered from the incidence by the uniqueness of \(u,v\) and \(y=M_v(x)\). Therefore \(I(X\times X,\mathcal T)\ge N^3\).

## Energy of the transformations

A left relative transformation has form \(D_uM_wD_{u'}^{-1}\), \(w=v/v'\). Up to scaling, write
\[
 M_w=\begin{pmatrix}
 adw-bc & bd(w-1)\\
 -ac(w-1)& ad-bcw
 \end{pmatrix}.
\]
For \(w\ne1\), both off-diagonal entries are nonzero. The ratio \(m_{11}m_{22}/(m_{12}m_{21})\) is invariant under left and right diagonal multiplication. It is a nonconstant ratio of quadratic polynomials in \(w\), because the denominator vanishes at \(w=1\) and the numerator there is \((ad-bc)^2\ne0\). Consequently each relative transformation with nonzero off-diagonals determines at most two possible \(w\).

When \(M_w\) has a nonzero diagonal entry, a given relative transformation and \(w\) determine \(u,u'\) uniquely. If \(m_{22}\ne0\), normalize the lower-right entry and read the two off-diagonals. If \(m_{22}=0\), compare each off-diagonal with the nonzero upper-left entry. Hence the relative multiplicity on this part is at most \(2|V|\), while the sum of multiplicities is at most \(|U|^2|V|^2\). The squared sum is \(O(|U|^2|V|^3)\).

For \(w=1\), the relative matrix is diagonal and its contribution to squared multiplicity is \(|V|^2 E^\times(U)\le |U|^3|V|^2\). There are at most two \(w\) for the antidiagonal case. At any such fixed \(w\) and fixed relative antidiagonal matrix, \(u\) determines \(u'\), so each multiplicity is at most \(|U||V|\) and their total is at most \(|U|^2|V|\). The squared energy of this case is also \(O(|U|^3|V|^2)\). These cases prove
\[
 E(\mathcal T)\ll |U|^2|V|^3+|U|^3|V|^2 .
\]

Apply [Warren and Wheeler, Theorem 4](https://www.ricam.oeaw.ac.at/files/reports/21/rep21-30.pdf), which for a grid \(A\times B\) with \(|B|\le\sqrt p\) bounds incidences by
\[
 I(A\times B,\mathcal T)\ll
 |A|^{1/2}|B|^{7/10}|\mathcal T|^{3/5}E(\mathcal T)^{1/10}
 +|B|^{1/2}|\mathcal T|.
\]
The energy is their left-relative energy, as counted above. Set \(A=B=X\), \(L=\max(|U|,|V|)/N\). The lower bound gives \(N^3\ll L^{17/10}N^{29/10}+L^2N^{5/2}\), hence \(L\gg N^{1/17}\).

## Consequence for the actual heavy levels

Use the actual cap and \(g\) from [Round 173](ordinary-weighted-affine-vertical-saving-173.md). With \(\epsilon=1/840\), \(\delta=2\epsilon\), any set \(X\) with \(g(x),g(\phi(x))\ge p^{-\epsilon}\) has size \(O(p^{1/2-\delta})\) for the four-nonzero-coefficient maps. Otherwise start with at most \(\lfloor\sqrt p\rfloor\) elements and apply the same two hereditary BSG extractions as in Round 173. They give a common restriction of size \(N'\gg p^{1/2-(5/2)\epsilon-(9/4)\delta}\) and both quotient sizes at most \(C p^{12\epsilon+6\delta}N'\). This conflicts with the preceding bound, since
\[
 \frac{1/2-(5/2)\epsilon-(9/4)\delta}{17}-(12\epsilon+6\delta)
 =\frac{1}{2856}>0 .
\]
For a nonmonomial projective map with a zero entry, an input or output inversion, or both, puts it into the nontrivially shifted affine case, covered by Round 173. Inversion preserves \(g\). The four-nonzero result and the old zero-entry result give the uniform unweighted high-level bound at threshold \(p^{-1/1280}\) for every nonmonomial projective map. The two light pieces in the weighted overlap each cost at most \(p^{-1/1280}G\) by injectivity. Thus, uniformly on the actual branch,
\[
 \sum_{x\notin\{0,\infty\},\;\phi(x)\notin\{0,\infty\}}g(x)g(\phi(x))
 \ll p^{1/2-1/1280}.
\]
The four-nonzero case by itself admits the stronger \(p^{1/2-1/840}\) bound. Monomial maps \(x\mapsto a x\) or \(x\mapsto a/x\) are excluded.

## Pointwise generic right differences and parameter rows

Use the exact genuine right action from [Round 174](ordinary-affine-difference-pins-174.md), now writing its parameters as \(a,c\). Let \(\varepsilon_*=1/1280\) and \(\varepsilon_1=1/840\). For \(a,c\ne0\) and \(a\ne1\), the \(Y\)-map \(Y'=aY/(1-cY)\) is nonmonomial. The matrix of the \(D\)-map has nonzero lower-left and upper-right entries, the latter because \(Y'\ne aY\). The other entries can vanish at only \(Y=1/a\) or \((1+c)Y=1\). These at most two fibers cost \(O(G)\) at fixed \(a,c\), since \(Y\) is fixed and \(D'\) is uniquely determined by \(D\). When both entries vanish, \(c=a-1,\ Y=1/a\), the \(D\)-map is reciprocal and \(Y'=a\).

For every other \(Y\), the weighted inner \(D\)-sum is \(O(p^{1/2-\varepsilon_1})\), even with both physical square masks retained. The \(Y\)-sum with both weights is independently \(O(p^{1/2-\varepsilon_*})\). Therefore the actual generic right correlation is
\[
 \Delta(a,c)=O(p^{1-\varepsilon_*-\varepsilon_1})
\]
uniformly. Removing any additional positive subclass preserves this upper. For fixed \(a\), summing over \(c\) gives exactly \(\sum_r m_r m_{ar}\) for the full physical correlation, where \(m_r\) is the genuine \(r\)-row mass. For fixed \(c\), sum instead over \(a\) and upper bound the inner sum by the \(b'\)-row mass at \(b'=b+cr\). The two row maxima from [Round 173](ordinary-full-diagonal-two-pin-173.md) are \(O(p^{1/2-\varepsilon_*})\) and the total line mass is at most \(G^2\). Thus the squared generic sum in either fixed parameter row is \(O(p^{5/2-2\varepsilon_*-\varepsilon_1})\).

Across all \(a,c\), the direct first-mass bound \(\sum\Delta\le G^4\) gives only \(O(p^{3-\varepsilon_*-\varepsilon_1})\) when paired with the new maximum. That is weaker than the existing whole-energy bound. A new summed argument using the distribution of the generic large correlations is still needed.
