# The exact physical right difference and target-scale shared-label energy cuts

Use the actual \(\mu_0(r,b)=g(Y)g(D)\) with \(b\in Q\), both nonzero endpoint exclusions, and \(r=(Y-D)/(1-D)\), \(b=D(1-Y)/(Y(1-D))\). Thus \(r,b\ne0,1\), and the map \((Y,D)\mapsto(r,b)\) is injective on this physical domain. Let \(G=\sum g=O(\sqrt p)\). Counting norms and the original eligible prime family are used throughout.

## Correct semidirect action

Interpret a line \(j=(r,b)\) as the map \(e\mapsto re+b\). For \(h=(a,c)\), where \(a\ne0\), the line \(j'=jh\) has
\[
 r'=ar,\qquad b'=b+cr.
\]
Both charts are retained only if their original physical exclusions and square masks hold. The exact inverse is
\[
 Y=\frac r{1-b},\qquad D=\frac{Y-r}{1-r}
   =\frac{br}{(1-r)(1-b)}.
\]
It follows immediately that
\[
 Y'=\frac{aY}{1-cY},\qquad
 D'=\frac{Y'-ar}{1-ar}
    =\frac{Y'-aY+(a-Y')D}{1-aY+(a-1)D}.
\]
A zero denominator excludes the proposed prime-field pair. These identities are compatible. The raw counterexample's values \(r=1/5,\ b=3/10\) instead give \(Y=2/7,\ D=3/28\). For its \(a=11/10,\ c=1/5\), both routes give \(Y'=1/3\).

Define the true right-difference correlation
\[
 \Delta(a,c)=\sum_{j:\,j,jh\ {\rm retained}}\mu_0(j)\mu_0(jh).
\]
Its full squared sum is the weighted energy of [Round 173](ordinary-weighted-affine-vertical-saving-173.md).

## Coincidence of one physical label in the line pair

For a specified equality between one role of \((Y,D)\) and one role of \((Y',D')\), let \(\Delta_{\rm eq}\) be the corresponding nonnegative part of \(\Delta\). For \(h\ne(1,0)\), each of the four choices has pointwise cost at most \(G\).

- \(Y=Y'\) fixes at most one \(Y\), by \(a+cY=1\); the remaining \(D\)-mass is at most \(G\).
- \(D=D'\) gives \(Y'=aY+(1-a)D\). For \(a\ne1\) this fixes at most one \(D\) for each \(Y\), and the \(Y\)-mass is at most \(G\). If \(a=1,c\ne0\), it would imply \(Y'=Y\), which is impossible.
- \(D=Y'\) fixes at most one \(D\) at each \(Y\).
- \(Y=D'\) also fixes at most one \(D\) at each \(Y\). With \(Y,h\) fixed on the retained domain, \(D\mapsto r\), \(r\mapsto ar\), and \(ar\mapsto (Y'-ar)/(1-ar)\) are all injective. This uses \(Y,Y'\ne1\).

For the sum over \(h\) of any such subcorrelation, each ordered physical line pair occurs at exactly one right difference. The sum is bounded by \(G^3\): in the two line sets take the marginals of their specified roles at the common literal label. Either marginal has maximum at most \(G\) and total at most \(G^2\). It follows that
\[
 \sum_{h\ne(1,0)}\Delta_{\rm eq}(h)^2\le G^4 .
\]
At the identity the entire \(\Delta(1,0)\le G^2\), including the portions with repeated labels. Thus the union of repeated cross-line literal labels is removable from the correlation at cost \(O(p^2)\) in squared norm. The triangle inequality is used before squaring the remaining correlation; the mixed products of the removed and remaining correlations are not separately estimated.

## Two elementary subfamilies of differences

Let \(\varepsilon_*=1/1280\), \(\tau=p^{-\varepsilon_*}\). The existing uniform two-level affine estimate and the two injective light tails show that
\(\sum_x g(x)g(\alpha x+\beta)=O(p^{1/2-\varepsilon_*})\) for every \(\alpha\beta\ne0\). This applies after taking both argument reciprocals as well, by inversion symmetry of \(g\).

For a nonidentity translation \(a=1,c\ne0\), \(1/Y'=1/Y-c\) is nontrivial affine and \(D\mapsto D'\) is affine with nonzero translation and slope at each retained \(Y\). In fact \(Y'\ne Y\), \(Y,Y'\ne1\), and
\[
 D'=\frac{Y'-Y+(1-Y')D}{1-Y}.
\]
Thus \(\Delta(1,c)=O(p^{1-2\varepsilon_*})\) after applying the actual two-level bound to \(Y\) and then \(D\). Summing all such correlations counts only ordered pairs sharing \(r\), so the first sum in \(c\) is at most \(O(G^2p^{1/2-\varepsilon_*})\) by the true \(r\)-row mass of [Round 173](ordinary-full-diagonal-two-pin-173.md). Their total squared sum is consequently \(O(p^{5/2-3\varepsilon_*})\).

For a nonidentity pure dilation \(c=0,a\ne1\), the ordered pairs share \(b\), so the \(b\)-row mass gives the same first-sum bound. Here \(Y'=aY\), and
\[
 \frac1{D'}=\frac{1-aY}{a(1-Y)}\frac1D+\frac{a-1}{a(1-Y)}.
\]
Both coefficients are nonzero for each retained \(Y\). Applying the reciprocal two-level bound to \(D\) and a first-mass bound to \(Y\) gives \(\Delta(a,0)=O(Gp^{1/2-\varepsilon_*})\). The pure dilations therefore have squared sum \(O(p^{5/2-2\varepsilon_*})\). Both family bounds exceed the \(O(p^2)\) target. The all-distinct generic right-difference energy remains open.
