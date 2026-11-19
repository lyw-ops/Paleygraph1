# The rank-three feedback bounds the third positive-trial increment

The degree-16 centered polynomial trial of [round 53](astra-histogram-53.md#four-positive-updates-with-a-centered-polynomial) gives the following uniform bounds for the actual stationary marks through eligible primes.

| Floor interval | Strict upper bound on \(\limsup_{p\to\infty}\sup_t |m_p(t)|\) | Limiting lower bound on scaled bulk trial products |
|---|---:|---:|
| \([223/32,15/2]\) | \(0.01699\) | \(3.3\) |
| \([27/4,223/32]\) | \(0.0202\) | \(2.5\) |

Consequently the prime \(0.017\) tolerance extends to \([223/32,25]\). The same trial polynomial is used, with its third Euclidean increment estimated from the known joint law of the first rank-three feedback. The proof uses interval enclosures of scalar bounds. It gives a fixed positive tolerance, and no prime-uniform bound at the cold floor \(1/2\).

## Separating the leading second increment

Use the actual finite polynomial iterates \(V_0=S=2\sqrt n K e_0,\ V_j=S+KP_t(V_{j-1})\), with the degree-16 even polynomial centered at \(x^2=12\). Write \(H(x)=\sqrt{4t+x^2}\) and let \(e_j\) bound \(|P_t-H|\) on the input range of \(V_j\). Use normalized Euclidean norms. The packet estimate of round 53 gives sup bounds for \(V_j\) and for their differences from the same coefficient envelope.

Write \(b=c_{0,2}>0\) for the second Chebyshev coefficient of \(P_t(sx)\), with \(s=2\sqrt2\), and \(G=V_1-S\). Under the [joint seed law](parallel-graph-shapes-23.md#a-fixed-number-of-path-columns-gives-no-leading-gain), \(G\) has limiting variance \(v=\frac12\sum_{k\ge2}c_{0k}^2\), and splits as \(G=bK(x^2)+G_{\rm tail}+o(1)\), where \(x=S/2\). In this expansion \(2n/q=1+o(1)\) is the conversion from \(KT_2\) to \(K(x^2)\). The limiting RMS of the tail is \(\tau=(\frac12\sum_{k\ge4}c_{0k}^2)^{1/2}\). The entire first feedback and its tail are asymptotically independent of \(S\). The limiting fourth moment of \(G\) is at most \(3v^2-b^4/8\), since the second Chebyshev feedback has fourth moment \(5/8\) and variance \(1/2\), and the other modes have fourth moments at most \(3/4\). These limits are uniform on the displayed floor intervals by continuity of the finitely many coefficient functions.

Set \(\delta=V_2-V_1\), \(z=K(x\,K(x^2))\). The untruncated second input difference is
\[
 H(S+G)-H(S)=\frac{2SG+G^2}{H(S+G)+H(S)}.
\]
If \(B_1\) is the packet upper bound for \(V_1\), enclose the reciprocal denominator between \(\ell=(H(B_1)+H(s))^{-1}\) and \(h=(4\sqrt t)^{-1}\), with errors \(o(1)\) as \(p\to\infty\). Put \(r=(h+\ell)/2,\ \lambda=4br\). Then
\[
 \|\delta-\lambda z\|_{2,n}
 \le \tfrac{h-\ell}{2}\sqrt{16v+3v^2-b^4/8}
      +r\left(4\tau+\sqrt{2v^2-b^4/8}\right)+e_0+e_1+o(1)
 =:\epsilon+o(1).
\]
Here \(\|2SG+G^2\|_{2,n}^2\le16v+3v^2-b^4/8+o(1)\) by independence and \(\mathbb E S=0\), and \(\|2S G_{\rm tail}\|_{2,n}\le4\tau+o(1)\). The \(G^2\) term is centered because \(K\) kills constants. All uses of \(K\) in this estimate are in Euclidean norm.

## The tilted midpoint in the third increment

Let \(M=(V_1+V_2)/2\). Convexity gives \(|H(V_2)-H(V_1)|\le |\delta|\,|H'(M)|\) pointwise. Replace the midpoint by \(U+\lambda z/2\), with \(U=S+bK(x^2)\). Its normalized Euclidean error is at most \(\tau+\epsilon/2+o(1)\). Also \(|H''|\le1/(2\sqrt t)\) and \(|z|\le3\sqrt2+o(1)\) on the good frequencies by the pointwise compact-group law. The single exceptional frequency incurs \(o(1)\) in normalized Euclidean norm, since all fixed fields in this estimate are bounded. If \(\Delta_2\) is the packet sup bound for \(\delta\), write \(B_M=B_1+\Delta_2/2\). The third increment is bounded by
\[
 \begin{split}
 \|V_3-V_2\|_{2,n}\le{}&
 \lambda\Big(\mathbb E\big[Z^2\,|H'(2X+bY+\lambda Z/2)|^2\big]\Big)^{1/2}\\
 &+\frac{B_M\epsilon}{\sqrt{4t+B_M^2}}
 +\frac{3\sqrt2\,\lambda}{2\sqrt t}(\tau+\epsilon/2)
 +e_1+e_2+o(1),
 \end{split}
\]
where \((X,Y,Z)\) is the [rank-three law](joint-law-32.md#2-a-concrete-compact-probability-model) for \(x,K(x^2),z\). This keeps the dependence of the modeled midpoint on the second increment.

For the first term, tilt the compact-model probability by \(2Z^2\). The conditional moments under the tilted law, given the Jacobi circle \(J\), are
\[
 \mathbb E_{\rm tilt} Z=X/4,\qquad
 \mathbb E_{\rm tilt} Z^2=3/2,\qquad
 \mathbb E_{\rm tilt} Z^3=35X/32 .
\]
To see the normalizations, for one of the conditional \(U(3)\) traces in the model, the real trace has conditional moments of orders \(1,\ldots,5\) equal to \(0,\ 1/2,\ (\Re J)/4,\ 3/4,\ 15(\Re J)/16\). The nonzero unbalanced complex trace moments are the determinant term in degree three and its degree-five counterpart. They follow from the [Schur--Weyl rule](joint-law-32.md#4-exact-mixed-moment-rule), with multiplicities one for partition \((1,1,1)\) and three for \((2,1,1)\), respectively. Center symmetry removes the other unbalanced terms. Independence of the two conditional traces and the factor \(1/\sqrt2\) in \(Z\) give the displayed moments. Their conditional second moment before tilting is \(1/2\), so the tilt leaves the law of \((X,Y)\) unchanged.

Put \(A=(2X+bY+\lambda Z/2)^2\). Expanding with these conditional moments and \(\mathbb E Y^2=1/2,\ \mathbb E Y^4=5/8\) gives
\[
 \begin{split}
 M_A:=\mathbb E_{\rm tilt} A&=4+b^2/2+\lambda/2+3\lambda^2/8,\\
 \operatorname{Var}_{\rm tilt}(A)&\ge
 8+8b^2+3b^4/8+(2+b^2)\lambda+(23/4+3b^2/4)\lambda^2 .
 \end{split}
\]
The omitted cubic term is \(23\lambda^3/32\), and the omitted quartic is nonnegative by \(\mathbb E_{\rm tilt} Z^4\ge(3/2)^2\). Both \(b,\lambda\) are positive on the certified intervals. With \(L=(s+2b+3\sqrt2\,\lambda/2)^2\), the support of \(A\) is in \([0,L]\). The negative second derivative of \(a\mapsto a/(4t+a)\) bounds a strict Jensen gap, just as in the second-increment calculation of [round 52](prime-increments-52.md#tilted-second-increment-estimate). In particular
\[
 \mathbb E\big[Z^2 |H'(2X+bY+\lambda Z/2)|^2\big]
 \le \tfrac12\left[
 \frac{M_A}{4t+M_A}
 -\frac{4t\,\operatorname{Var}_{\rm tilt}(A)}{(4t+L)^3}
 \right].
\]
Use the stated lower bound for the variance. This calculation uses the actual rank-three joint law, including its determinant constraint. It would be unjustified to take \(X\) and \(Z\) independent.

## Positive trial and verification

The fourth increment uses the Lipschitz constant of \(H\) on the packet sup interval and the two polynomial remainders there. Use the same strict product lower bound and square-root weight transfer as in the [prime increment proof](prime-increments-52.md#positive-pair-and-marked-transfer). These identify the actual \(m_p(t)\) through the positive pair at the trial product weights. The [interval checker](nested-positive-54-check.py) uses rational slabs of width \(1/1024\) and \(1/512\) on the two intervals respectively. It uses lower interval endpoints for the positive terms of the variance lower bound and upper endpoints for the mean, support radius, and norm factors. The two [records](nested-positive-54-checks.jsonl) verify the stated margins. The numerical failure of the simpler sup-Lipschitz estimate for the third step near \(7\) motivated this calculation; that earlier estimate did not refute the trial.

1. Isolate the leading part of \(K(xz)\) and \(K((Kx^2)^2)\) to refine the fourth Euclidean step. A uniform strict product bound and transfer below \(0.017\) at \(27/4\) would extend the range. A rigorous third- or fourth-increment lower bound above the allotted error rejects that predictor at the stated tolerance.
2. Try a different positive polynomial trial if its bulk positivity envelope fails. A nonpositive actual trial coordinate along unbounded primes refutes that proposed positive construction. Loss of slack in a scalar majorant alone does not give this conclusion.
