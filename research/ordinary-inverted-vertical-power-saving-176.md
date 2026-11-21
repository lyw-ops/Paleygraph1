# A vertical power saving in the actual full diagonal

Use the actual completed diagonal, cap, weights, physical exclusions and eligible prime branch of [Rounds 172–175](ordinary-full-diagonal-two-pin-173.md). The inverted-output chart has line transformation
\[
 j_{Y,D}(X)=\frac1r-\frac b rX,\qquad
 X=1/s,\quad r=\frac{Y-D}{1-D},\quad b=\frac{D(1-Y)}{Y(1-D)} .
\]
A vertical level fiber in its affine parameter plane has \(b/r=\lambda\ne0\). On the genuine domain this is equivalent to
\[
 D=\frac{\lambda Y^2}{1+(\lambda-1)Y},\qquad
 \frac1D=\lambda^{-1}\left(\frac1{Y^2}+\frac{\lambda-1}{Y}\right).
\]
When \(\lambda=1\), \(D=Y^2\), so its genuine line mass is at most \(G=\sum g\). At every output the contribution of this single row is at most \(G\). Its weighted squared norm is at most \(G^3=O(p^{3/2})\), using \(\sum w\le G\); remove it by the triangle inequality from the partition into row and nonrow kernels.

## Paired quotient growth for a shifted quadratic

Let \(F(x)=x(x+d)\), \(d\ne0\). For \(X\) consisting of nonzero inputs and nonzero outputs, \(N=|X|\le\sqrt p\), one has
\[
 \max\{|X/X|,\ |F(X)/F(X)|\}\gg N^{1+1/22}.
\]
To prove this put \(U=X/X\), \(V=F(X)/F(X)\), \(L=\max(|U|,|V|)/N\). If \(L>N^{1/22}\) the claim holds. Otherwise use the distinct points \((z,F(x)/z)\), \(z,x\in X\), and lines
\[
 W=\frac{1}{u^2v}Z+\frac{d}{uv},\qquad u\in U,\ v\in V.
\]
The two coefficients determine \(u,v\) uniquely, using \(d\ne0\). For every \(x,y,z\in X\), the choices \(u=z/y,\ v=F(y)/F(x)\) give the incidence, and an incidence determines \(y=z/u\) and at most two \(x\). Thus \(I\ge N^3/2\).

The number \(m=N|F(X)|\) of points is between \(N^2/2\) and \(N^2\), and the number \(l=|U||V|\) of lines is at least \(m\) and at most \(L^2 N^2\le N^{2+1/11}\). For sufficiently large \(N\), \(m^{7/8}<l<m^{8/7}\). Also \(m^{-2}l^{13}\ll N^{255/11}\le p^{255/22}\), with \(255/22<15\). Thus [Stevens–de Zeeuw, Theorem 3](https://arxiv.org/abs/1609.06284) applies and gives \(N^3/2\le I\ll (ml)^{11/15}\le L^{22/15}N^{44/15}\), yielding the claim. Bounded \(N\) is included by the constant.

Set \(\epsilon=1/1080,\ \delta=2\epsilon,\ \tau=p^{-\epsilon}\). For every \(\lambda\ne0,1\), the input \(x=1/Y\) and output \(1/D\) are related by \(F(x)\) up to the scalar \(\lambda^{-1}\), which does not change quotient sizes. Inversion preserves the actual \(g\). If a level fiber with \(g(Y),g(D)\ge\tau\) has more than a constant times \(p^{1/2-\delta}\) elements, restrict it to at most \(\lfloor\sqrt p\rfloor\) and to an injective subset for \(F\), losing at most a factor two. Apply the actual hereditary R173 two-BSG argument to the inverse input and inverse output before invoking paired quotient growth. The resulting restriction size is at least a constant times \(p^{1/2-(5/2)\epsilon-(9/4)\delta}\); both quotient sizes divided by this restriction size are \(O(p^{12\epsilon+6\delta})\). Contradiction follows from
\[
 \frac{1/2-(5/2)\epsilon-(9/4)\delta}{22}-(12\epsilon+6\delta)
   =\frac{1}{4752}>0.
\]
Therefore the vertical maximum \(m_{\mathcal L}\) in the original family of inverted-chart lines is \(O(p^{1/2-\delta})\) on the high level range. The identity above is used directly on the line family in this orientation, with the monomial row already removed.

## Consequence for the genuine full weighted diagonal

Use the output-first incidence and rearrangement from [Round 173](ordinary-full-diagonal-two-pin-173.md), retaining the physical square mask and the output weight, and completing \(g(C)\le1\) for this bound. With \(U,V\) now the sizes of the \(Y,D\) levels and \(\mathcal L\) their line set, the dominant piece of \(E(\mathcal L)^{1/8}|\mathcal L|^{1/2}\) is bounded by \(m_{\mathcal L}^{1/16}(UV)^{13/16}\) by the primary affine-energy estimate. On thresholds at least \(\tau\), layer integration in the two line weights and the input \(g(A)\) gives
\[
 O(p^{1/32-\delta/16} G^{17/8})=O(p^{35/32-\delta/16}).
\]
If either threshold is below \(\tau\), the direct vertical fiber formula gives \(m_{\mathcal L}\le\min(U,2V)\le\sqrt{2UV}\); integrating the resulting \((UV)^{27/32}\) over either low range gives a factor \(\tau^{5/32}\). This covers the desired saving \(\tau^{1/8}\) there. The other energy term and the all-level prime-field extension from [Round 172](ordinary-full-diagonal-affine-172.md) integrate to \(O(G^{17/8}+p^{-1/8}G^{19/8})=O(p^{17/16})\): their level factors are \(U^{3/4}V^{7/8}\) and \(p^{-1/8}U^{7/8}V\), followed by the square root of the input level size. Use the exact integral \(\int_0^1 V\,d\beta=G\) as an upper in the term linear in \(V\). The prime-field term thus allows the all-level argument, with no independent removal of light inputs.

The secondary incidence term is unchanged. For the positive upper kernel \(H\) on the remaining slope family, the sorted values obey
\[
 H^*(k)\ll p^{35/32-\delta/16}k^{-3/8}
   +\min\{G^2,G^{5/2}/k\}+G^{5/2}/\sqrt p .
\]
Use \(w\le1,\sum w\le G\), so weighted square sum is bounded by the unweighted top \(\lceil G\rceil\) square sum, even though the ordering of the values depends on the prime. The first term contributes \(O(p^{37/16-\delta/8})\). The other terms contribute \(O(G^{9/2}+G^6/p)\) as in Round 173, which is smaller. The monomial vertical row and physical endpoint errors are then restored in weighted norm, yielding the genuine whole bound
\[
 \boxed{\sum_s w(s)P_s^2=O(p^{37/16-1/4320}).}
\]
The proof applies also to the favorable and distinct-pole portions by nonnegativity. The sufficient \(O(p^{3/2})\) bound remains open; this estimate still uses the positive upper that drops \(g(C)\).
