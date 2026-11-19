# Centered activation differences in the positive four-step trial

For the actual stationary marks through eligible primes,
\[
 \limsup_{p\to\infty}\sup_{207/32\le t\le27/4}|m_p(t)|<0.01699,\qquad
 \limsup_{p\to\infty}\sup_{25/4\le t\le207/32}|m_p(t)|<0.0232 .
\]
The trial is still the degree-16 polynomial centered at \(x^2=12\). The pointwise product bound comes from the same packet envelopes. The improvement comes from a centered expansion of the second and third increments before applying \(K\). This keeps the squared first increment centered and combines its even part with the first-order odd part in Euclidean norm.

## Scalar bounds for an expansion at the seed

Use \(S=2x\), the iterates \(V_j\), the first increment \(G=V_1-S=by+G_{\rm tail}+o(1)\), and polynomial errors \(e_j\) from [round 54](nested-positive-54.md). Denote the limiting variance of \(G\) by \(v\), the limiting RMS of the tail by \(\tau\), the sup bounds for \(V_j\) by \(B_j\), and those for \(V_j-V_{j-1}\) by \(\Delta_j\). All norms below are normalized Euclidean norms and the inequalities for the finite fields include uniform \(o(1)\) on each indicated compact interval.

Let \(H(s)=\sqrt{4t+s^2}\), \(A(s)=H''(s)/2\), and
\[
 \begin{gathered}
 \kappa=(4t+6)^{-1/2},\qquad
 D=\frac4{\sqrt{4t}\sqrt{4t+6}(\sqrt{4t}+\sqrt{4t+6})},\\
 a_{\max}=\frac1{4\sqrt t},\qquad
 a_{\min}=\frac{2t}{(4t+8)^{3/2}},\qquad
 a_{\rm var}=\frac{a_{\max}-a_{\min}}2,\qquad
 M_3=\frac{12}{25\sqrt5\,t},\qquad
 L=1-\sqrt{\frac{t}{t+2}} .
 \end{gathered}
\]
On the limiting seed support, \(A(S)\) lies between \(a_{\min}\) and \(a_{\max}\). The global third derivative bound \(M_3\) follows by maximizing \(12t|s|/(4t+s^2)^{5/2}\). Rationalizing the difference \(H'(S)-\kappa S\) gives the RMS bound \(D\), since \(\mathbb E[S^2(S^2-6)^2]=16\) for the arcsine seed. Also \(\mathbb E[H'(S)^2]=L\). The finite seed has a sup bound tending to \(2\sqrt2\), so these estimates apply with vanishing errors.

## Second projection

Set \(\lambda=2b\kappa\), so \(K(b\kappa Sy)=\lambda z\). Consider the second input difference, ignoring the polynomial errors temporarily,
\[
 H(S+G)-H(S)=H'(S)G+A(S)G^2+R,\qquad
 |R|\le M_3|G|^3/6 .
\]
Write the residual first-order term as \(by[H'(S)-\kappa S]+G_{\rm tail}H'(S)\), with a vanishing correction. The first-feedback joint law makes it orthogonal in the limit to each function of \((S,G)\) even in \(S\) when the function is formed using the feedback coordinates as well. In detail the first-feedback family is independent of \(S\), whose law is symmetric. Also \(y\) and \(G_{\rm tail}\) are centered and mutually orthogonal, and the limiting second moment of \(y\) is \(1/2\). Thus the first-order residual has limiting squared norm at most \(b^2D^2/2+L\tau^2\).

Center the quadratic part before applying \(K\). The term \(A(S)(G^2-v)\) has RMS at most \(a_{\max}\sqrt{2v^2-b^4/8}\), using the fourth-moment bound for \(G\). The centered \(v A(S)\) has RMS at most \(v a_{\rm var}\), by the range of \(A(S)\). The centered quadratic part is even in \(S\), so its bound combines in quadrature with the first-order residual. The Taylor remainder is bounded by its uncentered norm using \(\|G\|_\infty\le\Delta_1+o(1)\). Since \(K\) contracts and kills constants,
\[
 \|V_2-V_1-\lambda z\|_{2,n}\le\epsilon+o(1),\quad
 \epsilon=
 \sqrt{b^2D^2/2+L\tau^2+
        \big(a_{\max}\sqrt{2v^2-b^4/8}+v a_{\rm var}\big)^2}
 +\frac{M_3\Delta_1\sqrt{3v^2-b^4/8}}6+e_0+e_1 .
\]

## Third projection

Replace the second increment by \(\lambda z\) in the third input difference. The error before applying \(K\) is at most \(\epsilon B_*/H(B_*)+o(1)\), where
\[
 B_*=B_1+(\Delta_2+\lambda Z_*)/2,\qquad Z_*=3\sqrt2 .
\]
Indeed the absolute secant of \(H\) is bounded by the absolute derivative at the midpoint by convexity of \(H\); \(|z|\le Z_*+o(1)\) on good frequencies. The exceptional frequency is bounded and negligible for the normalized Euclidean norms.

Write the resulting model difference as
\[
 H(S+G+\lambda z)-H(S+G)
 =\lambda z H'(S)+A(S)(2\lambda Gz+\lambda^2z^2)+R'.
\]
The first term after \(K\) has leading part \(\nu w\), where \(w=K(xz)\) and \(\nu=2\lambda\kappa\). The error from this term is bounded by \(\lambda D/\sqrt2\) since \(\mathbb E(Z^2\mid S)=1/2\).

In the quadratic term, use \(G=by+G_{\rm tail}+o(1)\) and subtract the constant part of \(A(S)/2\) in the \(z^2\) term before applying \(K\). The fields \(2b\lambda A(S)YZ\) and \(\lambda^2 A(S)(Z^2-1/2)\) are orthogonal since \(Y\) is centered and independent of \((S,Z)\). Their combined RMS is at most \(a_{\max}\sqrt{b^2\lambda^2+\lambda^4/2}\), using \(\mathbb E(Z^4\mid S)=3/4\). The correction from the centered part of \(A(S)/2\) is at most \(\lambda^2a_{\rm var}/2\). The part involving \(G_{\rm tail}\) costs at most \(2\lambda a_{\max} Z_*\tau\).

Integrate the first-order Taylor remainder for \(H'\) along the segment from \(S+G\) to \(S+G+\lambda z\). Minkowski gives
\[
 \|R'\|_{2,n}\le (M_3/2)\lambda\big(g_2+\lambda g_1+\lambda^2 g_0/3\big)+o(1),
\]
where
\[
 \begin{split}
 g_2&=\min\{Z_*\sqrt{3v^2-b^4/8},\ b^2\sqrt5/4+(\Delta_1+2b)Z_*\tau\},\\
 g_1&=b\sqrt{3/8}+Z_*^2\tau,\qquad g_0=Z_*\sqrt{3/4}.
 \end{split}
\]
These bound the norms of \(G^2z,Gz^2,z^3\), respectively. For the second bound on \(G^2z\), use \(G^2-b^2y^2=(G-by)(G+by)\), the sup bound \(2+o(1)\) for \(y\), and \(\mathbb E(Y^4 Z^2)=5/16\). The projection error \(\xi\) for \(\|V_3-V_2-\nu w\|_{2,n}\) is the sum of the preceding replacement, linear, quadratic and remainder bounds, plus \(e_1+e_2\).

## Positive combination

Substitute \(\epsilon,\xi,\lambda,\nu\) into the [fourth midpoint and transfer](rank-four-positive-55.md#fourth-increment-and-positive-transfer). That estimate uses the conditional rank-four second moment exactly and the upper bound \(25/32\) for its conditional fourth moment. The polynomial support envelopes give strict scaled bulk product lower bounds \(1.47\) on \([207/32,27/4]\) and \(0.33\) on \([25/4,207/32]\). The [interval checker](centered-positive-56-check.py) proves both margins along with the displayed mark bounds, using rational subdivisions and Arb at 192 bits. The [two records](centered-positive-56-checks.jsonl) are scalar certificates. The arithmetic moment limits and the positivity transfer identify their consequences for all sufficiently large eligible primes.

The unsigned fifth-step packet envelope already loses positivity at \(13/2\): a floating evaluation of the sufficient ideal-product bound is about \(-25\). A pointwise upper-envelope failure leaves actual product positivity undecided. Changing the polynomial center or truncation order in a finite point diagnostic made little difference to the \(0.017\) crossing for the fourth-step estimate.

1. Isolate the leading part of \(K(xw)\) in the fourth increment and control its product with the old midpoint in Euclidean norm. Write \(F_t(d)=d(\sqrt t+d)/\sqrt{1+(\sqrt t+d)^2}\) for the mark bound from square-root product dispersion \(d\). A lower bound \(d_{\rm lo}\) with \(F_t(d_{\rm lo})\ge0.017\) rejects this particular transfer at that tolerance. A rigorous upper bound \(d_{\rm hi}\) with \(F_{25/4}(d_{\rm hi})<0.017\) would extend the range without adding another Picard step.
