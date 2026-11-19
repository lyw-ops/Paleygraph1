# Marked response on translated frequency cosets

Let $B\le Q$ have order $b\asymp\sqrt q$, and write $A=B^\perp$. Take a frequency set $S$ that is a union of at most a fixed number of cosets of $A$, all disjoint from $A$. In particular $0\notin S$. Use $R(D)$ for the weighted response matrix of [response-locality.md](response-locality.md), with $R(0)=K$.

## A uniform bound from the zero reference

For every strict diagonal $D$ supported on $S$,

$$|R(D)_{00}-K_{00}|=O(q^{-1/2}).$$

The constant depends on the number of cosets and the size range of $b$. In particular this applies when the compression $K_{SS}$ has eigenvalues tending to either endpoint of $[-1,1]$.

The [shift formula and monotonicity](response-locality.md#changing-an-entire-set) bound arbitrary changes on $S$ by the two constant shifts in the hyperbolic coordinates. Write $c=P_SK e_0$. For sign $\sigma=\pm1$ and shift size parameter $0\le u<1$, the corresponding absolute response change is

$$u\langle c,(I-\sigma u K_{SS})^{-1}c\rangle\le\sum_f \frac{|\langle f,c\rangle|^2}{1-\sigma\alpha_f},$$

where $f$ ranges over an orthonormal eigenbasis of $K_{SS}$ and $\alpha_f$ is the corresponding eigenvalue. Terms with zero denominator have zero coupling, as also follows below.

The eigenbasis can be chosen by the [positional coset blocks](subgroup-modes.md#compression-to-frequency-cosets). In each block the unitary inverse Fourier image $g=\mathcal F^{-1}f$ is supported on one positional coset $C$ of $B$ and has sum zero on $C$. Indeed each of the tested frequency cosets restricts to a nontrivial character of $B$. The eigenvalue satisfies $\alpha_f=\sum_{a\in C}s(a)|g(a)|^2$. Subtracting $\sigma$ from $s$ inside the inner product with $g$ and applying Cauchy–Schwarz gives

$$|\langle f,K e_0\rangle|^2=\frac1n\left|\sum_{a\in C}(s(a)-\sigma)\overline{g(a)}\right|^2
\le\frac{2b}{n}(1-\sigma\alpha_f).$$

There are only $O(1)$ eigenvalues with $|\alpha_f|>1/2$ by $\|K_{SS}\|_{\rm F}^2\le q|S|^2/n^2=O(1)$. Their total contribution is $O(b/n)$. The other terms are at most $2\|c\|_2^2\le 2q|S|/n^2$. Both bounds are $O(q^{-1/2})$, proving the claim for both signs.

## A clipped arithmetic reference

An extension allows a clipped fixed-depth Picard diagonal as the reference, with its entries on $S$ and at $0$ set to zero. Assume the clipping bound is $\rho<1$, fixed in $q$. For a sign $\sigma$, suppose the eigenvalues in the **identity positional block** $C=B$ of $K_{SS}$ satisfy $\sigma\alpha_f\le1-\delta$ for a fixed $\delta>0$. Then arbitrary changes of sign $\sigma$ in the hyperbolic coordinates on $S$ have marked effect $o(1)$. If the identity block has a gap for both signs, the claim holds for arbitrary changes on $S$. As in the fixed-depth argument, the background calculation uses the [trace closure rules](iteration-parity.md).

Write $D_b$ for this reference, $X$ for the inverse of $H(D_b)$ with zero extension on constants, and $R=R(D_b)$. For $f$ supported on $S$ and $x=Xf$, we have $Rf=Mx$ since $D_b f=0$, and $Mf=f$. Contractivity gives

$$\|x-\sigma f\|_2^2\le\frac{2}{1-\rho^2}\langle f,(I-\sigma R_{SS})f\rangle.$$

As $Kx=P(D_bx+f)$, we have $f-\sigma Kf=Jf-PD_bx+K(x-\sigma f)$. The norm of this expression is at most $(2+\rho)\|x-\sigma f\|_2$, using $Jx=0$ and $D_bf=0$. Now $2\langle f,(I-\sigma K_{SS})f\rangle=\|f-\sigma Kf\|^2+\|Jf\|^2$, so

$$I-\sigma R_{SS}\succeq \frac{1-\rho^2}{(2+\rho)^2+1}(I-\sigma K_{SS}).$$

The shift formula at this reference therefore bounds the marked change by a constant depending on $\rho$ times $\sum_f |\langle f,Xe_0\rangle|^2/(1-\sigma\alpha_f)$. This follows first with $u<1$ by inverting $(1-u)I+u(I-\sigma R_{SS})$ and then bounding each positive-gap term by its value at $u=1$.

Let $\ell=D_b X e_0$. This vector vanishes on $S$, and $Xe_0=K e_0+K\ell$. The [fixed-depth argument for the inverse column](response-locality.md#a-uniformly-bounded-background) gives $\|P_S X e_0\|_2=o(1)$, so eigenvalues with $1-\sigma\alpha_f$ bounded below have vanishing total contribution. For the others, $C\ne B$ by hypothesis. We can write

$$\langle f,Xe_0\rangle=\langle f,K e_0\rangle+\langle (K-\sigma I)f,\ell\rangle.$$

The inverse Fourier image of $(K-\sigma I)f$ is supported on $C$ and has squared norm at most $2(1-\sigma\alpha_f)$. Hence the second term, squared and divided by $1-\sigma\alpha_f$, is bounded by $2\|\mathbf1_C\mathcal F^{-1}\ell\|_2^2$. This also gives zero coupling if the gap is zero.

To see that the last positional norm tends to zero, start before zeroing the reference on $S$. The scaled inverse column $\sqrt n\,Xe_0$ is approximable in normalized $\ell_2$ by bounded negative expressions, by the Neumann series in the fixed-depth argument. Multiplication by the clipped odd diagonal gives even expressions. Each such expression has inverse Fourier trace supported at $1$ in its punctual part and bounded by $O(q^{-1/2})$ off $1$ in its nonpunctual part, by the stalk weight bound. Thus the inverse unitary Fourier image of the corresponding unscaled vector has vanishing norm on $C\ne B$, since $|C|=O(\sqrt q)$. The approximation errors in unscaled $\ell_2$ can be made arbitrarily small. Zeroing the reference on $S$ changes the inverse column and its product with the diagonal by $o(1)$ in unscaled $\ell_2$, by the same resolvent identity used for column delocalization. This proves the required positional bound. Combining it with the zero-reference estimate for the first term and the bounded count of small gaps gives the extension.

For a single translated frequency coset at $b\sim\sqrt q$, the [identity-block constraints](subgroup-modes.md#which-scalar-blocks-can-approach-norm-one) supply both gaps when $b$ is odd and the negative-shift gap when $b$ is even. The extension still requires the actual background to be controlled by the reference.

## Comparison of prescribed diagonals

The [coset experiment](../data/response-cosets.csv) uses $D_i=1-1/q$ on the tested support and zero elsewhere. It compares the unshifted annihilator with its mark deleted, the half-shifted coset, and the pair of opposite shifts by one frequency. At $q=389^2$ with $b=388$, the half-shifted coset has the same near-unit compression norm as the full annihilator, namely $387/388$. Its marked entry is about $0.002707$, compared with $0.663806$ for the unshifted support with the mark deleted. For $p=153649$ and $b=388$ the two entries are about $0.002231$ and $0.002402$. These are floating-point solves of the prescribed-diagonal comparison, with [replay in the shift probe](../response_shift.py). Smaller dense tests verify the comparison for mixed-sign perturbations and check zero marked coupling on 25 endpoint modes using positional-block eigenbases.
