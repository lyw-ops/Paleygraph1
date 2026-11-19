# Weighted transfer for the fourth positive increment

For the actual stationary marks through eligible primes,
\[
 \limsup_{p\to\infty}\sup_{31/5\le t\le25/4}|m_p(t)|<0.01699,\qquad
 \limsup_{p\to\infty}\sup_{25/4\le t\le207/32}|m_p(t)|<0.0149 .
\]
The four-step trial remains the degree-16 polynomial centered at \(x^2=12\). The new estimate transfers the leading fourth increment \(K(xw)\) with its true conditional moments and compares the remaining part by a separate positive denominator. Uniform scalar checks enclose the bounds after this arithmetic reduction.

## Refined second and third errors

Use \(S=2x,\ H(s)=\sqrt{4t+s^2},\ A=H''/2\), and all coefficients and error bounds of [round 56](centered-positive-56.md), with \(\delta_j=V_j-V_{j-1}\), \(\delta_2=\lambda z+\text{error}\) and \(\delta_3=\nu w+\text{error}\). In particular \(\lambda=2b\kappa,\ \nu=2\lambda\kappa,\ \kappa=(4t+6)^{-1/2}\). Let \(a_2^*=(a_{\max}^2+a_{\min}^2)/2\). As a function of \(S^2\), \(A(S)^2\) is convex. Its endpoint chord on \([0,8]\), with \(\mathbb E S^2=4\), gives \(\mathbb E A(S)^2\le a_2^*\).

For the centered quadratic part of the second increment, \(A(S)(G^2-v)\) is orthogonal to \(v(A(S)-\mathbb E A(S))\) by independence of \(S,G\), where \(G=V_1-S\) and \(v=\lim\mathbb E G^2\). Hence the even quadratic variance in \(\epsilon^2\) can be estimated by
\[
 a_2^*(2v^2-b^4/8)+v^2a_{\rm var}^2 .
\]
More precisely this quadratic variance enters under the same square root as the first-order odd variance, before adding the cubic and polynomial errors.

For the third increment, the two quadratic model terms
\[
 2b\lambda A(S)YZ,\qquad \lambda^2 A(S)(Z^2-1/2)
\]
are orthogonal and have combined variance at most \(a_2^*(b^2\lambda^2+\lambda^4/2)\), since both squared factors have constant conditional means given \(S\). The linear model error \(\lambda[H'(S)-\kappa S]Z\) has variance at most \(\lambda^2D^2/2\). Its covariance with the first quadratic term vanishes since \(Y\) is centered and independent. Its covariance with the second is \((\lambda^3/16)\mathbb E[(H'(S)-\kappa S)A(S)S]\), by \(\mathbb E(Z^3\mid S)=S/16\). This identity follows from the determinant term in the rank-three tilted moments. Cauchy–Schwarz bounds twice its absolute value by \(\lambda^3D a_{\max}/4\). Take one square root of the sum of the two model variances and that covariance bound, then add the retained third-step centering, tail, replacement and truncation bounds to obtain \(\xi\). All these estimates use uniformly vanishing errors on the compact floor intervals as in round 56. [Rank-three tilted moments](nested-positive-54.md#the-tilted-midpoint-in-the-third-increment)

## Leading fourth increment and its remainder

Put \(\mu=2\nu\kappa\) and \(u=K(xw)\). The [rank-five through seven calculation](weighted-arithmetic-57.md) gives \(\mathbb E(U^2\mid X,Y,Z,W)=1/2,\ \mathbb E(U^3\mid X,Y,Z,W)=0,\ \mathbb E(U^4\mid X,Y,Z,W)=3/4\), with good-frequency radius \(U_*=23/\sqrt2\). The exceptional frequency is negligible for the norms. We bound \(\|\delta_4-\mu u\|_{2,n}\) by the following \(\zeta+o(1)\).

In \(H(V_2+\delta_3)-H(V_2)\), replacing \(\delta_3\) by \(\nu w\) costs at most \(\xi B_*/H(B_*)\), with \(B_*=B_2+(\Delta_3+\nu W_*)/2,\ W_*=8\), by the absolute midpoint secant bound. Replacing the base \(V_2\) by \(M=S+by+\lambda z\) costs at most \(\nu W_*(\tau+\epsilon)/(2\sqrt t)\). For the latter estimate, write the difference of two increments as the integral of \(H'\) along their common shift, and bound the difference of the derivatives by the global \(\|H''\|_\infty=1/(2\sqrt t)\).

The resulting \(H(M+\nu w)-H(M)\) equals \(\nu wH'(M)\) up to norm \(\nu^2a_{\max}(7/8)\) by the second derivative bound and \(\mathbb E W^4=49/64\). To isolate \(\nu\kappa Sw\), put \(A_0=bY+\lambda Z\). Then
\[
 \mathbb E(A_0\mid S)=0,\quad
 \mathbb E A_0^2=(b^2+\lambda^2)/2,\quad
 \mathbb E A_0^4=5b^4/8+3b^2\lambda^2/2+3\lambda^4/4.
\]
Expand \(H'(S+A_0)\) at \(S\), keeping the first derivative term. The old error \(H'(S)-\kappa S\) is orthogonal to \(H''(S)A_0\) by the conditional mean. The conditional second moment \(\mathbb E(A_0^2\mid S)=(b^2+\lambda^2)/2\) is constant, so the chord bound for \(\mathbb E A(S)^2\) also applies here. Thus
\[
 \|H'(S+A_0)-\kappa S\|_2
 \le \sqrt{D^2+4a_2^*\mathbb E A_0^2}
       +(M_3/2)\sqrt{\mathbb E A_0^4}.
\]
Since the conditional second moment of \(W\) given the older fields is \(1/2\), multiply this entire bound by \(\nu/\sqrt2\). Sum the listed terms and \(e_2+e_3\) to get \(\zeta\). Applying \(K\) contracts and sends \(\nu\kappa Sw\) to \(\mu u\).

## Split square-root weight comparison

Set \(V=V_3\), \(\delta=\delta_4\), \(\delta_0=\mu u\), and \(P(V,d)=t-(2V+d)d/4\). The actual trial ideal product \(P(V,\delta)\) has the inherited bound \(L_4=t-(2B_3+\Delta_4)\Delta_4/4\). The leading trial \(P(V,\delta_0)\) has bound \(L_\mu=t-(2B_3+\mu U_*)\mu U_*/4\) on good coordinates. The leading comparison can be restricted to those coordinates. The omitted frequency is the mark, which is already normalized to one in the weight comparison. The positive trial proof gives the exact factors positive also at that coordinate. The scalar interval checker verifies both lower bounds stay positive and supplies the scaled product lower bound after the polynomial correction \(C_4=(2H(B_3)+e_3)e_3/4\).

Compare the two roots using their distinct lower bounds. The norm of their difference is at most
\[
 \frac{(2B_3+\Delta_4+\mu U_*)\zeta}{4(\sqrt{L_4}+\sqrt{L_\mu})}+o(1).
\]
For the root of the leading trial versus \(\sqrt t\), its numerator is \(\mu(2V+\mu u)u\). Use the model \(M_3^*=S+bY+\lambda Z+\nu W\) for \(V\), with error at most \(\tau+\epsilon+\xi+o(1)\). By the conditional moments of \(U\), the norm of \(2M_3^*U+\mu U^2\) is
\[
 \sqrt{2\mathbb E (M_3^*)^2+3\mu^2/4},\qquad
 \mathbb E (M_3^*)^2=4+(b^2+\lambda^2+\nu^2)/2 .
\]
The remaining numerator cost is \(2\mu U_*(\tau+\epsilon+\xi)\). Divide their sum, with the model norm multiplied by \(\mu\), by \(4(\sqrt t+\sqrt{L_\mu})\). Finally add \(C_4/(\sqrt{L_4-C_4}+\sqrt{L_4})\) to account for the activation polynomial. The result is an upper bound for the square-root weight distance \(d\) after the usual \(o(1)\) marked normalization. The [positive weight transfer](prime-increments-52.md#positive-pair-and-marked-transfer) gives the bound \(d(\sqrt t+d)/\sqrt{1+(\sqrt t+d)^2}+o(1)\).

The [Arb192 checker](weighted-positive-57-check.py) verifies 512 closed slabs of width \(1/10240\) down to \(31/5\) with product margin \(0.065\), and 112 closed slabs of width \(1/512\) from \(25/4\) to \(207/32\) with margin \(0.33\). The two [records](weighted-positive-57-checks.jsonl) certify the strict scalar bounds. At \(25/4\), a point diagnostic with the older second and third projection enclosures and just the split transfer gave about \(0.017295\), which motivated keeping the indicated covariance. At \(31/5\), replacing the chord bound by the supremum of \(A^2\) in the fourth projection would give about \(0.017069\). The averaged chord and the strict interval margins establish the stated range.

1. To move materially below this floor, improve the pointwise product envelope as well as the norm estimate. Keeping the first distinguished signed fields inside the finite polynomial loop may lower the fourth difference radius. A strict positive product and a transferred bound below \(0.017\) throughout a new interval would confirm the gain. A uniform lower bound on the actual square-root distance above the transfer threshold would reject the same trial there.
