# Quartic loss of an optimized stationary reference

The [fixed-reference loss](astra-ref-50.md) at the true cold mark has an exact fourth-order coefficient when the reference is moved to a nearby warmer floor. Summing over the two signs reduces it to one bulk regression in the physical cold tangent. The coefficient is strictly positive at every fixed floor for sufficiently large primes. At the flat floor \(a=n\) its sum, multiplied by \(n\), converges to \(1/128\). The expansion takes the step to zero at fixed field.

## Optimized loss

Fix the cold floor \(a>0\), the cold pair \(P,R\) for the two signs, \(W=1+(1-1/n)a\), and \(w_0=1,\ w_i=a/n\) otherwise. Use the weighted orthogonal decomposition into constants and relative tangent spaces \(T_+=V_\sigma/P,\ T_-=V_{-\sigma}/R\) for weights \(w_i/W\). Put \(p=\operatorname{proj}_{T_+}e_0,\ q=\operatorname{proj}_{T_-}e_0\), and
\[
 Z_\pm=\{u\in T_\pm:u_0=0\},\qquad
 \|f\|_{2,b}^2=n^{-1}\sum_{i\ne0} f_i^2 .
\]
On the bulk, the two \(Z\) spaces are orthogonal under this norm. Both marked leverages are positive. Below \(p\) in the tangent formulas denotes the vector. The field prime is denoted by \(p_{\rm fld}\).

At floor \(a e^h\) take the two actual stationary rows as opposite references for the two separate optimizations. Let \(G_+(h)\) be \(W\) minus the maximum of the round-49 score at the true same-side cold mark, with \(R_{a e^h}\) the fixed opposite reference. Define \(G_-(h)\) by swapping the signs. Neither optimization imposes the extra lower-branch constraint of the one-sided certificate. Then
\[
 \begin{aligned}
 G_+(h)&=\frac a4 h^4\|\Pi_{Z_-}(pq)\|_{2,b}^2+O_{p_{\rm fld},a}(|h|^5),\\
 G_-(h)&=\frac a4 h^4\|\Pi_{Z_+}(pq)\|_{2,b}^2+O_{p_{\rm fld},a}(|h|^5).
 \end{aligned}                                                     \tag{1}
\]

To prove this, write \(v=\ell/P\) for a feasible trial and \(r=R_{a e^h}/R\). The exact score gap is \(a\min_{k\ge0}\|\sqrt v-k\sqrt r\|_{2,b}^2\). On the bulk, let \(L\) be the restriction of \(\mathbb R\mathbf1+T_+\). Its orthogonal complement is exactly \(Z_-\) restricted to the bulk. Indeed extension by zero at the mark tests the same orthogonality in the cold weighted norm. Restriction to the bulk is injective on \(\mathbb R\mathbf1+T_+\), since any kernel vector is proportional to \(e_0\), whose projection onto \(T_-\) is \(q\ne0\).

At \(h=0\) the only zero of the gap over \((v,k)\) is \((1,1)\). Equality implies \(v=k^2\) on the bulk and consequently everywhere by injectivity, and the weighted mean of \(v\) is one. The feasible polytope is compact, and the best \(k=E_b\sqrt{vr}/E_b r\) is continuous near \(h=0\), with \(E_b=n^{-1}\sum_{i\ne0}\). Thus every minimizing pair approaches \((1,1)\). There is a feasible comparison with \(v=1,k=1\) of loss \(O(|h|^2)\), so at a minimum \(v-k^2r=O(|h|)\) in bulk norm. Here \(r=1+O(h)\) entrywise. Applying the inverse of the bulk restriction to \(v-k^2\mathbf1\) and using the weighted mean gives \(v=1+O(|h|)\), \(k=1+O(|h|)\) entrywise with constants at fixed field. It follows that squaring
\[
 \sqrt v-k\sqrt r=\frac{v-k^2r}{\sqrt v+k\sqrt r}
\]
 costs a factor \(1/4+O(|h|)\). The normal component of its numerator is \(-k^2\Pi_{Z_-}r\), giving the corresponding lower bound.

For the upper bound lift \(\Pi_L r\) back to \(\mathbb R\mathbf1+T_+\). Its lift \(l\) satisfies \(l=1+O(h)\). Choose \(v=l/\mathbb E_w l\) and \(k^2=1/\mathbb E_w l\), where \(\mathbb E_w\) uses \(w_i/W\). This gives a positive feasible trial for small \(|h|\). Its bulk numerator is exactly \(-k^2\Pi_{Z_-}r\). Together the two bounds give
\[
 G_+(h)=a(1/4+O(|h|))\|\Pi_{Z_-}r\|_{2,b}^2.
\]
If the projection vanishes, the constructed pair achieves zero.

Let \(s=P_{a e^h}/P\). The product \(sr\) is constant on the bulk for each \(h\), and \(s'(0)=-p,\ r'(0)=-q\), with the minus sign from warming the bulk relative to the mark. Pair its second derivative with \(Z_-\). The \(s''\) term vanishes since \(s''\in T_+\), as does the derivative of the bulk product. Hence \(\Pi_{Z_-}r''(0)=-2\Pi_{Z_-}(pq)\). Also \(\Pi_{Z_-}\mathbf1=\Pi_{Z_-}q=0\). Taylor expansion gives (1).

## The combined coefficient

The complement of \(Z_+\oplus Z_-\) on the bulk is \(\mathrm{span}\{\mathbf1,p\}\) there. The two spaces are orthogonal with a combined dimension of \(n-3\) by positive marked leverage. The bulk constraint \(q=-1/W-p\) makes both \(\mathbf1\) and \(p\) orthogonal to these spaces. The bulk of \(p\) is nonconstant. If it were constant then weighted mean zero would give \(p=\lambda(e_0-\mathbf1/W)\), and orthogonality to \(q\) together with both positive leverages rules this out. Therefore
\[
 \lim_{h\to0}\frac{G_+(h)+G_-(h)}{h^4}
 =\frac a4\min_{u,v\in\mathbb R} E_b(p_i^2-u-vp_i)^2.              \tag{2}
\]
The coefficient vanishes exactly when \(p\) takes at most two values on the bulk. The algebra-propagation argument in the [warm tangent note](astra-ref-50.md#simultaneous-exact-scores-force-a-two-valued-flat-bulk-column) takes such a two-valued tangent at any floor to a flat Fourier column of at most two bulk values. The prime arcsine law therefore makes (2) strictly positive at each positive floor for every sufficiently large prime.

At \(a=n\), \(p=((I-J)+\sigma K)e_0/2\), so on the bulk \(p_i=-1/(2n)+\sigma z_i/(2\sqrt n)\) with \(z_i=\sqrt n K_{i0}\). Thus \(n\) times (2) equals \(\min_{u,v}E_b(z_i^2-u-vz_i)^2/64\). The [prime Jacobi law](fourier.md#joint-distribution-on-the-even-modes) and the uniform bound \(|z_i|\le \sqrt{p_{\rm fld}/n}\) give convergence of the moments through order four to those of \(\sqrt2\cos\Theta\) for uniform \(\Theta\). Its first and third moments are zero, its second moment is 1, and its fourth is \(3/2\). The regression residual tends to \(1/2\), giving \(1/128\).

## The exact cost of the bulk lift

For \(u\in\mathbb R\mathbf1+T_+\), orthogonality to \(q\) gives \(q_0 u_0=-a E_b(uq)\). Since \(q\) is the projection of \(e_0\), \(a E_b q^2=q_0(1-q_0)\). Consequently
\[
 |u_0|\le \sqrt{\frac{a(1-q_0)}{q_0}}\|u\|_{2,b},\qquad
 \|u\|_w\le \sqrt{\frac{a}{Wq_0}}\|u\|_{2,b}.
\]
Equality holds for \(u=e_0-q\), so the second constant is the operator norm of the inverse bulk restriction. On a compact floor interval, lower bounds on both marked leverages control both lift norms uniformly. This leaves the entrywise positivity of the lifted rows and the corresponding control of the square-root denominators to be proved.

The [checker](reference-curvature-50-check.py) independently evaluates the two projected norms and the scalar regression at three flat prime controls using Arb 192. It checks agreement of the two expressions and positive curvature. Run the checker with the project virtual environment to reproduce the [records](reference-curvature-50-checks.jsonl).

1. At a fixed cold floor, bound the bulk regression residual and the localization constants in the linear lift, using actual prime cold tangents. A vanishing residual through unbounded primes refutes a uniform positive quartic obstruction at that floor. A positive coefficient without control of the finite-step remainder gives no fixed-step obstruction.
2. For propagation from a hot interval, track the same zero-mark tangent projections of warm row ratios after a step. A positive lower bound on the projection together with a quantitative nearby optimizer estimate can reject a common reference. To construct feasible trial marks, instead seek a prime-uniform remainder upper bound and positivity of the warm tangent trial. The flat limit above alone does not control either task at fixed cold floor.
