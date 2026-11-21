# Quadratic parameter curves for the actual diagonal and transverse rows

Use the actual \(g,w,G\) and interior of [Round 177](ordinary-shifted-energy-four-factor-diagonal-177.md). The genuine inverted-output transformations are
\[
 j_{r,b}(X)=1/r-(b/r)X,\qquad X=1/s,
\]
with weights \(\mu_*(j_{r,b})=g(Y)g(D)\) on the actual domain of [Round 176](ordinary-inverted-vertical-power-saving-176.md). The projective parameter map \((r,b)\mapsto(-b/r,1/r)\) preserves the upper \(2G\) for weighted mass on every parameter-plane line, because its inverse image lies in an old affine line or is empty. Total mass is at most \(G^2\).

## Two affine families with bounded relative fibers

An inverted vertical row has \(k=r/b\) fixed and nonzero. With \(x=1/Y,\ y=1/D\), the exact inverse formula is \(y=x+k(x^2-x)\). Thus its mass is bounded by
\[
 B(k)=\sum_{x\ne0,1}g(x)g(x+kx(x-1)),
\]
by inversion symmetry and positivity. For the maps \(L_x:k\mapsto x(x-1)k+x\), the left difference \(L_yL_x^{-1}=(a,d)\) gives \(y=ax+d\) and
\[
 a(a-1)x^2+2ad x+d(d-1)=0 .
\]
The polynomial is nonzero except at the identity, giving at most two pairs at any nonidentity left difference.

There is a parallel exact calculation for each genuine transverse projection with parameter \(c\ne0\). For \(q=b+cr\) the inverse labels satisfy
\[
 (qx-c)y=x(x+q-1-c),\qquad
 y=1+\frac{(x-1)(x-c)}{qx-c}
\]
where the denominator is nonzero. Only \(q\ne0,1\) contributes to its mixed first mass with the genuine \(b\)-row, as \(n_0=n_1=0\). If \(x=c\), the original equation forces \(y=1\) for these \(q\), which is excluded. Hence use \(x\notin\{0,1,c\}\), and put \(F(x)=(x-1)(x-c)\). A zero denominator cannot satisfy the equation on this domain. The affine maps in \(q\) for \(z=1/(y-1)\) are the distinct
\[
 L_x:q\longmapsto \frac{xq-c}{F(x)} .
\]
For \(L_yL_x^{-1}=(a,d)\), now \(x,y\) denote two parameters of the affine family. Its slope and intercept equations yield \(L=1-dF(x)/(ca)=x/y\ne0\) and \(F(y)=F(x)/(aL)\). Substitution gives \(a(x-L)(x-cL)=F(x)L\). Factoring the two terms on the left by \(x-1\) and \(x-c\), respectively, and cancelling \(F(x)\) yields
\[
 (a-1)+d\bigl((1+1/c)x-2\bigr)+\frac{d(d+1)}{ca}(x-1)(x-c)=0 .
\]
For \(d\notin\{0,-1\}\) this is quadratic. At \(d=0\) the only exceptional map is the identity. At \(d=-1\) the polynomial vanishes identically only for \(a=c=-1\). In every case \(x\) determines \(y\). The left difference fibers of both families have multiplicity at most two outside at most two fixed exceptional elements. With weights \(g(x)\), the exceptional relative masses are at most \(G\), and the total relative mass is at most \(G^2\).

## Squared row masses and transverse consequence

For either family let \(B_0(k)\) be its action on the respective nonnegative vertical function, namely \(g(y)\) for the first and \(g(1+1/z)\) for the second, extended by zero at \(z=0\). Each vertical function is bounded by one and has mass at most \(G\). The actual projection is bounded by \(B_0\), using the required square masks and endpoints in the original sum and dropping them only in this positive upper.

For one level \(S\) of the vertical function, \(U=|S|\), expand the squared norm of \(\sum_x g(x)1_S(L_x(k))\) in \(k\). The change of variables \(v=L_x(k)\) gives the weighted average of the overlaps \(m(h)=|S\cap hS|\) under the left relative mass at \(h=L_yL_x^{-1}\). By the rich affine-line bound used in [the slope-product note](ordinary-weighted-slope-product-incidence-178.md), at most \(O(U^5/t^4)\) maps have overlap at least \(t\) for \(t\ge C\max\{1,U^2/p\}\), with absolute \(C\). Use the split
\[
 H=\max\!\left\{C(1+U^2/p),\ (U^5/G^2)^{1/4}\right\}.
\]
The exceptional elements cost \(O(GU)\). For the others use total weight at most \(G^2\) up to the split and maximum weight two to estimate the excess above the split by the tail integral \(O(U^5/H^3)\). The squared norm is \(O(GU+G^2(1+U^2/p)+G^{3/2}U^{5/4})\). An empty level has zero contribution. Apply layer cake and the counting second-norm triangle inequality to the genuine vertical function. Using \(\int_0^1 U\,du\le G\), \(\int_0^1 U^{1/2}\,du\le\sqrt G\), and \(\int_0^1 U^{5/8}\,du\le G^{5/8}\) gives a second norm \(O(G+G^2/\sqrt p+G^{11/8})=O(G^{11/8})\), since \(1\le G=O(\sqrt p)\). The squared inverted vertical and transverse row masses are therefore both \(O(p^{11/8})\).
This includes the monomial row \(k=1\) and the relevant cancelled row \(q=c\).

As in the slope-product note, the actual fixed-\(c\) first mass is \(\sum_{a\ne0}\Delta(a,c)=\sum_q n_{c,q}n_q\). Here \(n_{c,q}\) is the true transverse mass at \(b+cr=q\), and \(n_q\) the original \(b\)-row. Apply the new squared bound and the Round 177 bound \(\sum_q n_q^2=O(p^{3/2-3/418})\). For every \(c\ne0\) the first mass is
\[
 O(p^{23/16-3/836}).
\]
Multiplying by the genuine generic maximum of Round 176 gives the corresponding fixed-\(c\) squared sum for \(a\ne1\), with the added power \(p^{1-1/1280-1/840}\). This result does not close the whole generic energy.

## Transfer to the entire weighted diagonal

Use the weighted point-plane argument of the slope-product note for \(\mu_*\), with the inverted squared vertical row bound just proved. This gives
\[
 \mathcal E(\mu_*)=O(p^{43/16}).
\]
To bound the exact full diagonal positively, first complete \(g(C)\le1\) and use weighted affine incidence for \(j_{r,b}\), with output \(X=1/s\) horizontal and levels of \(g(A)\) under inversion vertical. The integral of the square root of the vertical level size is \(O(\sqrt G)\). Thus the coefficient of the output-set size to the \(5/8\) power is \(O(p^{139/128})\), using \(43/128+1/2+1/4=139/128\). The secondary term is \(O(G^{5/2}(1+|T|/\sqrt p))\) on output set \(T\). Decreasing rearrangement and \(\sum_s w(s)\le G,\ w(s)\le1\) give the preliminary bound \(O(p^{147/64})\), with the secondary squared contributions \(O(p^{9/4})\).

To apply the all-four-heavy shifted argument of Round 177, take \(\epsilon=1/1600,\ \delta=2\epsilon=1/800\). A role with \(g<p^{-\epsilon}\) can be sent to \(C\) by physical symmetries, gaining \(p^{-2\epsilon}\) in the squared norm from the new preliminary bound. A role in the leftover of size \(O(p^{1/2-\delta})\) can be sent to \(A\), saving \(p^{-\delta/2}\) in the primary coefficient and \(p^{-\delta}\) after squaring. For all four arguments in the extracted set, its actual first mass is \(O(p^\alpha)\) using exactly the size-dependent formula
\[
 \alpha=\tfrac{18}{13}+\tfrac4{13}\max\{49\epsilon,36\epsilon+9\delta\}
       =279/200 .
\]
On the first \(\lfloor p^{99/200}\rfloor\) rearranged positions the output-first estimate gives \(O(p^{139/64+(99/200)/4}+p^{9/4})\) in squared norm. For the remaining positions use the first mass, giving \(O(p^{2\alpha-99/200})\). The first leading exponent is \(147/64-1/800=3673/1600\), and the tail exponent is smaller by \(1/1600\). Adding these cuts and the already priced endpoints in the genuine weighted norm proves
\[
 \boxed{\sum_s w(s) P_s^2=O(p^{3673/1600}).}
\]
The favorable and distinct-pole positive parts inherit this upper. The sufficient \(O(p^{3/2})\) whole bound and a genuinely coupled second-moment estimate are still open.

## Shared inverted vertical parameter

For the positive collision between copies with a common \(k=r/b\), let \(m_k\) be the actual vertical row mass. Its nonnegative kernel is at most \(m_k\) at each \(s\), and its first mass in \(s\) is \(O(p^{1/2-1/1280}m_k)\) by the same per-line sum of \(g(A)g(C)\) as in [Round 173](ordinary-full-diagonal-two-pin-173.md). The actual squared row mass then bounds the shared-\(k\) weighted collision by \(O(p^{15/8-1/1280})\).

With one further projective relation between prescribed physical labels of the two copies, this shared-\(k\) collision is at the sufficient \(O(p^{3/2})\) scale. Indeed at fixed \(s,k\), put \(x=1/Y\) and \(u=1+kx\). The retained chart has
\[
 r=k/u,\quad b=1/u,\quad
 A=ks/(su-1),\quad C=k/((u-k)(su-1)),\quad
 Y=1/x,\quad D=1/(x(1+k(x-1))).
\]
Each of these four labels fixes \(x\) up to at most two choices. The resulting kernel indexed by \(s,k\) and one label has first mass at most \(G^3\) by the original three-label pin and maximum at most two. In its squared norm weighted by \(w(s)\), a prescribed projective matching of the finite labels, allowed to depend on \(s,k\), is bounded by Cauchy–Schwarz at cost \(2G^3\), as in [Round 175](ordinary-favorable-sign-identity-175.md). This is a separate positive cut, with bounded union cardinality when several such matchings are used.
