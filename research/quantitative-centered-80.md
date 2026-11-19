# A quantitative centered remainder bound from the first boundary moment

The two-circle argument gives a quantitative lower bound for a centered real Taylor remainder using only the first and second circle energies, the correction's first two norms, and the cap of the predictor. It avoids any uniform bound on the correction or on its circle derivatives at individual points. The bound applies in the compact Mellin models of [round 79](astra-fixed-79.md), with the stated field-first order of limits.

## First boundary moment and conditional mixing

Write \(A_{\alpha,k}\) for the orthogonal projection onto angular frequency \(k\in\mathbb Z\) for the boundary circle \(\alpha=1,\chi\). In particular \(A_{\alpha,0}\) is averaging over that circle. For a square-integrable function in the trace closure define
\[
 {\cal E}_1(f)=\tfrac12\sum_\alpha\sum_k k^2\|A_{\alpha,k}f\|_2^2,
 \quad {\cal E}_{1/2}(f)=\tfrac12\sum_\alpha\sum_k |k|\|A_{\alpha,k}f\|_2^2,
 \quad M(f)=\tfrac12\sum_\alpha \|f-A_{\alpha,0}f\|_2^2 .
\]
All norms use probability Haar measure. The first absolute boundary moment gives the stronger first inequality
\[
              \operatorname{Var}(f)\le{\cal E}_{1/2}(f)
                         \le \sqrt{M(f){\cal E}_1(f)} .                   \tag{1}
\]
Indeed, for a nonpunctual geometric simple with generic rank \(r\) and convolution dimension \(d\), the pooled \(|k|\) moment of the two weight lists is exactly \(r\) by the [two-fiber identity](astra-feedback-52.md#reading-rank-from-two-mellin-characters). On its twisted character over the arithmetic coset, the weight of each angular frequency in \(L^2\) is the corresponding multiplicity divided by \(d\), by Schur matrix-coefficient orthogonality with the unitary intertwiner. Thus the energy coefficient is \(r/d\ge1\). Constants contribute zero, and distinct geometric simples are orthogonal also after applying the circle frequency projections, since these only change the matrix coefficient within each simple. The other inequality is Cauchy--Schwarz over the nonzero angular frequencies and the two circles. At a fixed expression all spectra on each block are bounded. Hence (1) passes to the compact limits in round 79 and extends in the first-derivative graph norm, using (1)'s upper bound and continuity of circle averaging. This works for even and odd trace expressions and their products.

There is a sharper variant for bounded real \(f\) with \(|f|\le1\). Write \(T(f)=\frac12\sum_\alpha\|\partial_\alpha f\|_1\), \(J={\cal E}_1(f)\). The Fejér identity represents the \(|k|\) energy by integrating squared differences along each circle against \(1/(4\sin^2(\theta/2))\), with the factor \(d\theta/(2\pi)\). For a difference at angle \(\theta\) its squared norm averaged over the two circles is bounded by both \(\theta^2J\) and \(2|\theta|T(f)\). These bounds follow by integration of the derivatives and by \(|f(x)-f(y)|\le2\). Splitting the integral at \(\min(\pi,T(f)/J)\) shows
\[
       \operatorname{Var}(f)\le C T(f)\,[1+\log^+(J/T(f))].              \tag{1a}
\]
When \(T(f)=0\) the right side is taken to be zero. The formula follows first on the derivative domain by angular Fourier expansion and then by Tonelli for the nonnegative squares. In particular take \(J\le J_0\) and \(\operatorname{Var}(f)\ge v_0>0\). Monotonicity and inversion of \(x\mapsto x[1+\log^+(J_0/x)]\) give
\[
               T(f)\ge \frac{c v_0}{1+\log^+(C J_0/v_0)}.             \tag{1b}
\]
For example, substituting a sufficiently small constant times the right side into the increasing function gives a strict value below \(v_0/C\), since \(\log(1+\log^+ y)\le 1+\log^+ y\) for \(y>0\).

## The centered real remainder

Take a compact real floor interval \(0<t_{\min}\le t\le t_{\max}<\infty\), and a real base row \(|W|\le C_W\). Let \(F_t(x)=\sqrt{4t+x^2}\). For a real, nonzero, mean-zero correction \(h\) in the graph-norm closure of real trace functions put
\[
 B=F_t(W+h)-F_t(W)-F'_t(W)h,\quad
 m=\|h\|_1,\quad L=\|h\|_2,\quad E={\cal E}_1(h),\quad
 b=\int B,\quad \eta=\|B-b\|_2.
\]
There is an absolute \(c>0\) such that
\[
                       \boxed{\quad
          \eta\ \ge\ c\frac{b^4}{E^{3/2}}\left(\frac{m}{L}\right)^4 .
                              \quad}                                    \tag{2}
\]
Also, \(b\ge\kappa m^2/(1+m)>0\), with \(\kappa>0\) depending only on \(C_W,t_{\min},t_{\max}\). To see the latter, use a positive lower bound for \(F_t''\) on \(|x|\le C_W+1\) in the Taylor integral. For \(|h|\le1\) the integral gives a lower bound proportional to \(|h|^2\). For \(|h|\ge1\) integrate over the first segment of length \(1/2\) to give a lower bound proportional to \(|h|\). In both cases \(B\ge\kappa |h|^2/(1+|h|)\), and \(x^2/(1+x)\) is convex for \(x\ge0\). Convexity and the derivative cap one also give \(0\le B\le2|h|\).

For (2), choose \(k=b/8\le m/4\) and a smooth function \(s(h)=\psi(h/k)\), where \(\psi\) takes values in \([-1,1]\), equals the sign for \(|x|\ge1\), and has bounded derivative. The masses of \(h\) on its two signs both have first moment \(m/2\). Thus \(\Pr(h\ge k)\) and \(\Pr(h\le-k)\) are each at least \(m^2/(16L^2)\) by Cauchy--Schwarz. Since \(s\) is identically \(+1\) and \(-1\) on these sets, respectively, its variance is at least \(m^2/(8L^2)\).

On \(\{|h|< k\}\), one has \(B\le b/4\), so this set has measure at most \(C\eta^2/b^2\). The weak chain rule from [round 79](astra-fixed-79.md#the-centered-remainder-and-the-exact-correction) gives
\[
                 {\cal E}_1(s)\le CE/b^2,\qquad
                    \tfrac12\sum_\alpha\|\partial_\alpha s\|_1
                              \le C\sqrt E\,\eta/b^2 .
\]
The second bound uses Cauchy--Schwarz on the transition set. On each circle \(\|s-A_{\alpha,0}s\|_1\le C\|\partial_\alpha s\|_1\), by integrating differences along the rotation. This holds in the graph closure by the same inequality on trace polynomials. Since \(|s-A_{\alpha,0}s|\le2\), it gives \(M(s)\le C\sqrt E\,\eta/b^2\). Now (1) bounds \(\operatorname{Var}(s)\) by \(C E^{3/4}\eta^{1/2}/b^2\). Combine with the variance lower bound to obtain (2).

Using (1b) instead, with \(T(s)\le C\sqrt E\,\eta/b^2\), \(J_0=CE/b^2\) and \(v_0=(m/L)^2/8\), gives the sharper bound
\[
 \eta\ \ge\
 \frac{c\, b^2 (m/L)^2}
      {\sqrt E\, [1+\log^+(C(E/b^2)(L/m)^2)]}.                    \tag{2a}
\]

## Application to a bounded Picard predictor

In a compact model let the actual signed increment \(R\) have bounded preimage \(P\) of positive type under \(\mathcal K\), so \(R=\mathcal K P\). This holds for each positive finite Jacobi height by taking \(P=F_t(U_j)-F_t(U_{j-1})\), and at the Jacobi seed by taking \(P=F_t(S)\). At the initial nine-center row subtract its fixed preimage as in round 79. Suppose \(R\) is also bounded. Set \(r=\|R\|_2>0\) and \(D=F_t'(W)\), with \(\|D\|_\infty\le v<1\) and \(\max_\alpha\|\partial_\alpha D\|_\infty\le C_D\). Use the exact correction \(h=(I-\mathcal K D)^{-1}R\) as in round 79. The isometry modulo constants and the Newton equation give
\[
 r^2=\langle R,h\rangle-\langle P-\overline P,Dh\rangle,\qquad
 m\ge r^2/(\|R\|_\infty+2v\|P\|_\infty),\qquad L\le r/(1-v).
\]
The Dirichlet contraction and the product estimate give
\[
       E^{1/2}\le \frac{{\cal E}_1(R)^{1/2}}{1-v}
                             +\frac{C_D r}{(1-v)^2}.
\]
Thus (2) yields, for \(0<r\le1\), the quantitative normalized bound
\[
             \eta\ \ge\ c_*\frac{r^{20}}{({\cal E}_1(R)^{1/2}+r)^3},       \tag{3}
\]
where \(c_*>0\) depends only on the displayed caps, floor interval and \(v\). The powers follow from \(b^4\gg m^8/(1+m)^4\), \((m/L)^4\), and \(m\gg r^2\). For a fixed compact prefix the normalized physical remainder has the same subsequential centered norm by the marked restoration in round 79. Formula (3) separates a quantitative increment lower bound and a Dirichlet upper bound from the nonlinear centering step. Its field-first transfer does not supply a simultaneous estimate at growing depth or an effective prime threshold.

With \(Q={\cal E}_1(R)^{1/2}+r\), (2a) improves (3) to
\[
               \eta\ \ge\ \frac{c_* r^{10}}
                     {Q[1+\log^+(C_* Q^2/r^{10})]}.              \tag{4}
\]
Indeed \(b\gg r^4\), \(m/L\gg r\) and \(\sqrt E\ll Q\). These give the lower bound on the prefactor and the upper bound on the logarithm, uniformly for \(0<r\le1\).

## A square of a finite negative trace field

Let \(f\) be real, mean zero and of negative trace type. Put \(b_f=\|f\|_2^2>0\), \(\eta_f=\sqrt{\operatorname{Var}(f^2)}\). Suppose its angular spectrum on both circles is supported on \([-w,w]\), \(w\ge1\). The rank equality \(d=r\) on its negative constituents implies \({\cal E}_{1/2}(f)=b_f\) and \({\cal E}_1(f)\le w b_f\). Then
\[
                  \operatorname{Var}(f^2)\ge
                         \frac{c\,b_f^2}{w(1+\log w)^2}.           \tag{5}
\]
If \(\eta_f\ge b_f\), this is immediate after choosing a small absolute \(c\). Otherwise Hölder gives \(\|f\|_1\ge \|f\|_2^3/\|f\|_4^2\ge\sqrt{b_f/2}\). Saturate the sign smoothly at \(|f|=\sqrt{b_f}/8\). As above each sign has fixed positive probability, hence the saturated sign has variance bounded below. Its transition set has measure \(O(\eta_f^2/b_f^2)\) since \(f^2\) is at most \(b_f/64\) there. Writing \(E_f={\cal E}_1(f)\), its derivative has \(T\ll\sqrt{E_f}\eta_f/b_f^{3/2}\) and its \(J\) is \(O(E_f/b_f)\). Apply (1b) with a fixed positive \(v_0\) to obtain \(\eta_f\gg b_f^{3/2}/[\sqrt{E_f}(1+\log^+(C E_f/b_f))]\), which gives (5).

## Transfer of the leading square at logarithmic heights

Let \(S=2\sqrt n K e_0\) and take the actual leading coefficient rows \(L_1=K(S^2/2)\), \(L_{j+1}=K(SL_j)\). As in [the simultaneous field comparison](astra-dissipation-80.md#explicit-logarithmic-height-field-comparison-for-the-leading-coefficients), their compact counterparts \(H_j\) are real negative trace fields, with representation mass \(D_j\ll6^j\) and raw evaluation error \(\|L_j-E_pH_j\|_{2,n}\ll6^j/\sqrt p\). These are estimates on a finite expression at each field, with the displayed uniform cost. Reality in the lift-average follows from reciprocity under multiplicative inversion, which exchanges the two quadratic lift descriptions after the \(\chi(1-x)\) twist. Equivalently take the real parts of the compact counterparts and their evaluations. The transport commutes with this involution, so the recursion and the same bounds apply. Their angular weights have \(|k|\le j+1\) on both circles: two seed weights enter the first return, and each later multiplication adds one seed weight before transport. Transport preserves the pooled nonzero weights and inserts zeros. In particular no individual output weight can exceed the maximum of the two input lists.

On the same compact Haar coset, put \(b_j=\|H_j\|_2^2\). The exact seed-angle covariance gives \(b_j=(s_p^4/32)(s_p^2/2)^{j-1}\ge 2\cdot4^{j-1}\), where \(s_p=2\sqrt{p/n}\). Moreover, the [averaged path energy bound](astra-dissipation-80.md#average-and-worst-cumulative-discounts-on-jacobi-paths) gives \({\cal E}_1(H_j)\le1296 b_j\) at every height, using inequivalence of the collected Jacobi paths. Applying the pre-bandwidth estimate in the proof of (5) with this energy gives the stronger \(\operatorname{Var}(H_j^2)\gg b_j^2\), with an absolute constant.

For clarity about the fourth-moment transfer, a product of four negative constituents of dimensions \(d_1,\ldots,d_4\) has generic rank at most \(4d_1d_2d_3d_4\). This is the [tame generic-fiber bound](large-smoothing.md#an-exact-bound-for-even-products) iterated through the convolution, retaining its possible punctual contributions of rank zero. All constituents in the product retain boundary characters \(1,\chi\). Hence the fourth moment of the raw evaluation differs from the compact Haar value by \(O(D_j^4/\sqrt p)\). The nonpunctual stalk at one costs its generic rank times \(p^{-1/2}\); the two exceptional full characters cost \(O(D_j^4/p)\); the punctual stalk is the exact arithmetic Haar moment. The same argument with two factors gives error \(O(D_j^2/\sqrt p)\) for the second moment.

Both \(\|E_pH_j\|_\infty\) and \(\|L_j\|_\infty\) are \(O(6^j)\). For the latter use the normalized second-norm comparison times \(\sqrt n\) in addition to the raw sup bound. Therefore the physical fourth moment changes by at most \(O(6^{4j}/\sqrt p)\) upon replacing the raw field by \(L_j\). Subtracting the squares of their second moments has the same error. It follows that for all sufficiently large eligible primes, simultaneously for \(1\le j\le(\log_2p)/32\),
\[
          \operatorname{Var}_n(L_j^2)
                \ge c\,\|L_j\|_{2,n}^4.                        \tag{6}
\]
Here the total additive error \(O(6^{4j}/\sqrt p)\) is \(o(1)\) uniformly through this range. The lower bound from \(b_j\ge 2^j\) is bounded away from zero uniformly in \(j\), and \(\|L_j\|_{2,n}^2=b_j+o(1)\). This extends the leading-square nonvanishing of round 78 to genuine growing height. It is a large-floor coefficient estimate. A bound on the full nonlinear Newton remainder at \(2031/128\) on this growing range still requires a quantitative parameter transfer and control of the non-leading terms.

1. Obtain a rate for the real increment and its Dirichlet energy when the predictor depth grows, then compare (3) to the counting tolerance. Uniform control of the transfer errors is needed at the same depth.
2. Test the exact Dirichlet dissipation of the transported positive field to distinguish a genuine loss of large-energy terms from a bound on a single rank ratio.
