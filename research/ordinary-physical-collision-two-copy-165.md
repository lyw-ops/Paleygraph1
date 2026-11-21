# Two-copy identities and genuine diagonal cuts for physical slope collisions

Keep the actual mark \(v\), both physical square masks, and the fixed actual squared thresholds \(a,b>0\) of [Round 164](ordinary-physical-pair-slope-pinning-164.md), with at least one above one half for its quantitative exponent \(\gamma\). Let \(\mathcal P\) be the actual allowed one-pair set of \((A,C)=(1-vx,1-vux)\) with \(u\ne1\). Use the coordinates
\[
 u=\frac{1-C}{1-A},\qquad z=C/A.
\]
This is injective, since \(A=(1-u)/(z-u)\). In particular each fiber is a genuine subset \(Z_u\subseteq Q\) of ratio values, with \(|Z_u|=h(u)\). Before slope-only restrictions, ordered distinct points in one fiber have slope \(t=z_2/z_1\ne1\). Put
\[
 n_{u,t}=|Z_u\cap t^{-1}Z_u|,qquad N_t=\sum_u n_{u,t},\qquad N_1=\sum_u h(u).
\]
For the actual favorable mask and any actual amplitude band just restrict \(t\). Extra restrictions depending on more than \(t\) can be bounded from above by these counts, which use the original one-pair physical masks.

## Exact collision formulas

With counting, unnormalized Mellin transforms, put \(M_\eta=\sum_u|\widehat{1_{Z_u}}(\eta)|^2\). Parseval and \(\sum_\eta M_\eta=nN_1\) give
\[
 \sum_{t\ne1}N_t^2
  =\frac1n\sum_\eta |M_\eta-N_1|^2.
\]
Equivalently, for any actual slope mask \(D\subseteq Q\setminus\{1\}\),
\[
 \sum_{t\in D}N_t^2
 =\sum_{u,u'}\sum_{t\in D}|Z_u\cap t^{-1}Z_u|\,|Z_{u'}\cap t^{-1}Z_{u'}|.
\]
In reciprocal intercept coordinates, \(u\mapsto b_t=u(t-1)/(1-u)\) is injective for fixed \(t\ne1\). Thus the equal-intercept contribution is precisely the term with \(u=u'\), and without the mask its off-diagonal value is
\[
 \sum_u\big(E^\times(Z_u)-h(u)^2\big).
\]
The subtraction is essential: ratio one contains every point in the fiber.

The same-u bound furnished by the proven overlaps is
\[
 \sum_u\big(E^\times(Z_u)-h(u)^2\big)
 \le\sum_u h(u)^3
 \ll_{a,b} p^{2-2\gamma}.
\]
There is no cancellation from a slope sign already fixed on the chosen block. The squared collision sum for the whole fixed moderate band remains open.

## A genuine diagonal loss of only the target scale

Discard collisions of two ordered slope triples that share a complete physical pair \((A_x,C_x)\) at any endpoints. For a fixed first triple and fixed choice of the endpoints to be identified, the shared point fixes \(u,z\); the common slope fixes the other endpoint of the second triple. Hence at most one second triple is possible for each of the four endpoint choices. These collisions cost at most \(4\sum_{t\in D}N_t=O_{a,b}(p^{3/2-\gamma})\) by Round 164. This removes exact and one-endpoint sharing, including repeated rows, while preserving the actual masks.

For the original weighted first moment, rows with \(h(u)\le H\) cost at most \(H\sum_u h(u)=O_{a,b}(Hp)\), uniformly in the genuine slope weight of modulus at most one. For the equal-u portion of the collision sum the same deletion costs \(O(H^2p)\), by the displayed energy bound with \(h(u)\le H\). Thus for fixed \(H\) the weighted problem can restrict to larger overlaps, and for \(H\le p^{1/4}\) the equal-u low-overlap collision part alone is already within the target. High-overlap equal-u quadruples and different-u quadruples with disjoint physical endpoints still require a coupled estimate.
