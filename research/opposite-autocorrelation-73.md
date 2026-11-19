# Opposite autocorrelation prices the differences of supercritical sites

The high-site translation test can use the genuine opposite Fourier constraints rather than only the maximum multiplicity of the chosen differences. Exact cross-sector orthogonality gives a finite autocorrelation budget. At every sufficiently large eligible prime an opposite Fejér probability prices differences in one explicit short character arc more strongly by a factor of order \(\log p\). This excludes some supercritical high-site configurations even when their unrestricted difference count is too large for the bounded-multiplicity test.

## The shared autocorrelation budget

Let \(G\) be the cyclic frequency group of size \(n=(p-1)/2\). Write \(q\) for a feasible probability on the tested sign and \(r\) for any feasible probability on the opposite sign. We need no mark condition on \(r\). For a nonnegative vector \(b\), let
\[
 C_b(h)=\sum_i b_i b_{i+h},\qquad L_b=C_b(0).
\]
The opposite Fourier supports mean that \(q*\widetilde r=\mathbf1/n\), where the tilde reverses the argument. Expanding its squared counting norm gives
\[
 n\sum_{h\ne0} C_q(h) C_r(h)=1-nL_qL_r=:\beta(q,r)\ge0 .
 \tag{1}
\]
This also follows by grouping two difference-pairs with the same displacement. The diagonal is an exact part of the budget and is subtracted before pricing the other differences.

Take a probability \(\mu\) on \(G\) and center the translates of \(q\) with the distribution \(\mu\). The resulting \(v=q*\widetilde\mu\) is feasible and \(v_0=\sum_i\mu_iq_i\). Put \(x_i=(q_i-B/n)_+\), \(M=\sum_i x_i\), and retain \(B>0\). On a smooth opposite window with actual negative-defect set \(S\) as in round 72, Jensen bounds the localized convex tail by
\[
 \frac1n\sum_{i\in S}(nv_i-B)_+^2
   \le n\|\mathbf1_S(x*\widetilde\mu)\|_2^2
   \le n\sum_h C_x(h)C_\mu(h).
 \tag{2}
\]
For \(\lambda\ge0\), let \(e(h)=(C_\mu(h)-\lambda C_r(h))_+\) on \(h\ne0\). By \(x\le q\), \(C_x\le C_q\) and (1), the last quantity of (2) is at most
\[
 nL_x L_\mu+\lambda\beta(q,r)
       +n\min\bigl(L_x\|e\|_1,(M^2-L_x)\|e\|_\infty\bigr).
 \tag{3}
\]
For the two bounds on the error use \(C_x(h)\le L_x\) and
\(\sum_{h\ne0}C_x(h)=M^2-L_x\), respectively. The term with \(\lambda\) can also use
any convex mixture of actual opposite autocorrelations, with the corresponding mixture of the budgets (1). If \(\mu\) is supported at cap sites of a primary optimum then \(v\) stays on the primary face. For arbitrary near-high sites it is still an ordinary feasible probability, and the signed marked comparison of round 72 applies to \(v\) without exact optimality.

For example, if \(\sqrt n\,v_0\ge1+\delta\), \(B=o(d)\), and the fixed negative cutoff is \(u=\delta/8\), the left side of (2) is at least \(c_\delta d\) in every selected window. Thus making the right side of (3) \(o(d)\) excludes these \(\mu\). Formula (3) allows a small amount of uncovered difference mass even if some \(C_r(h)\) vanish. The fixed-budget proof only needs feasibility and the actual marked estimates. It makes no assertion about where the defects occur.

## A uniformly available prime weight on a character arc

Let \(L=\lfloor(\log_2 p)/4\rfloor\). The [prime sign-run construction](astra-endpoint-45.md#a-uniform-prime-estimate-for-the-measurement-fibers) gives, for each sign, an element \(t\) of the positional square subgroup of order exceeding \(2L\), such that the positions \(t^j\) for \(1\le j\le L\) have that sign. Apply it to the opposite sign and take
\[
 r^{\,F}_i=\frac{\left|\sum_{j=0}^L \eta_i(t)^j\right|^2}{n(L+1)}.
\]
Here \(\eta_i\) is the multiplicative character labelled by frequency \(i\). This is a feasible probability on the opposite sign. Its only nonconstant Fourier coefficients are the weights \(1-|j|/(L+1)\) at \(t^j\), \(0<|j|\le L\). Define
\[
 \mathcal B_t=\{h:|\arg \eta_h(t)|\le1/(L+1)\},
\]
using the principal argument. Parseval gives
\[
 C_{r^{\,F}}(h)=\frac1n\sum_{j=-L}^L
 \bigl(1-|j|/(L+1)\bigr)^2\operatorname{Re}\eta_h(t)^j .
\]
On \(\mathcal B_t\) every cosine is at least \(\cos(1)>0\). The sum of squared coefficients is at least \((L+1)/2\). Mix \(r^{\,F}\) with the uniform row in equal weights. This actual opposite feasible \(r\) satisfies
\[
 C_r(h)\ge \frac{3}{4n}+\frac{cL}{n}\mathbf1_{\mathcal B_t}(h).
 \tag{4}
\]
The \(3/(4n)\) is exact from the uniform cross terms, and the Fejér autocorrelation is nonnegative even away from the arc.

Let \(A\) be any nonempty set of coordinates at which \(\sqrt n\,q_i\ge1+\delta\), and put \(a=|A|\). For uniform \(\mu\) on \(A\), \(C_\mu(h)=R_A(h)/a^2\), where \(R_A(h)=|A\cap(A+h)|\). From (4) we can take \(e=0\) in (3) with
\[
 \lambda\le C\frac{n}{a^2}\left(
        \max_{h\ne0,\ h\notin\mathcal B_t}R_A(h)
       +\frac1L \max_{h\ne0,\ h\in\mathcal B_t}R_A(h)\right).
\]
Use zero for a maximum over an empty set. In particular there is a constant \(c_\delta>0\) such that for all sufficiently large eligible primes, all such \(q,A\), and every permissible opposite run \(t\),
\[
 \frac{\sqrt n}{a}+
 \frac{n}{a^2}\left(\max_{h\ne0,\ h\notin\mathcal B_t}R_A(h)
       +\frac1L \max_{h\ne0,\ h\in\mathcal B_t}R_A(h)\right)
 \ \ge\ c_\delta D.
 \tag{5}
\]
To prove the depth scale, if the left side divided by \(D\) tends to zero on a subsequence, choose \(d\to\infty\), \(d=o(D)\), dominating that left side by a diverging factor. For instance choose \(d\) near the geometric mean of \(D\) and the maximum of that left side with one. The endpoint cap \(q_i\le C/\sqrt n\) gives \(nL_x L_\mu\le C\sqrt n/a\). Equations (2)–(4) then contradict the order-\(d\) hinge lower bound for \(v\), whose mark is at least \(1+\delta\). This also establishes the uniform quantifiers in (5).

Thus if \(a\) is comparable to \(\sqrt n\), popular differences on the priced arc can have multiplicity up to order \(DL\) before this test becomes expensive, while differences off it still pay at the \(D\) scale. Large periodic sets may violate these upper hypotheses by a wide margin. A single supercritical root also passes the necessary inequality. The result controls difference geometry where many supercritical sites are available and leaves the actual primary hinge minimum open.

## A single mixed budget for all low-order differences

One can remove the choice of run by averaging the autocorrelations, which are nonnegative. Let \(\mathcal T\) be all admissible opposite runs \(t\) with \(\operatorname{ord}(t)>2L\). If \(h\in G\) has order \(m\le L\), then uniformly in \(h\),
\[
 \#\{t\in\mathcal T:\eta_h(t)=1\}
       = \frac{n}{m\,2^L}+O(L^2\sqrt p).
 \tag{6}
\]
In the sign-run count, insert the average of \(\eta_h^k\), \(0\le k<m\), to enforce \(\eta_h(t)=1\). The term with no sign factors contributes only for \(k=0\) on \(Q\). For every nonempty subset \(J\) of sign factors and every twist, extend the character from \(Q\) to \(\mathbb F_p^\times\) and expand the indicator of \(Q\). Write the resulting term using a primitive character of order \(p-1\) on
\[
 x^\kappa\prod_{j\in J}(1-x^j)^{(p-1)/2}.
\]
A primitive root of order \(\max J\) is a simple root of its largest factor before the displayed exponent, and it appears in no smaller factor. At this nonzero root the multiplicity is \((p-1)/2\), including after the monomial twist. Thus the polynomial is not a \((p-1)\)-st power up to a scalar. The distinct-root form of the Weil bound gives \(O(L^2\sqrt p)\) per term, uniformly in the twist. The expansion coefficients have total absolute sum one. Excluding roots and elements of order at most \(2L\) costs \(O(L^2)\). This proves (6), including its untwisted \(m=1\) count. [Weil's character-sum bound](https://www.pnas.org/doi/10.1073/pnas.34.5.204)

Since \(m\le L\) and \(2^L\le p^{1/4}\), the errors in (6) are relative \(o(1)\). Consequently a proportion at least \(1/(2m)\) of the runs has \(\eta_h(t)=1\), where \(C_{r^{\,F}_t}(h)\ge L/(2n)\). Average those Fejér autocorrelations over all of \(\mathcal T\) and mix in half the uniform autocorrelation. The resulting nonnegative profile \(C_*\) is a convex mixture of actual opposite autocorrelations and obeys
\[
 C_*(h)\ge \frac{c}{n}\left(1+\frac{L}{\operatorname{ord}(h)}\right)
 \qquad(h\ne0).
\]
For orders above \(L\), the uniform part alone supplies this bound. Substituting \(C_*\) in (3) with \(e=0\), and using the same depth argument, gives the following prime-uniform necessary inequality, independent of the choice of run:
\[
 \frac{\sqrt n}{a}+
 \frac{n}{a^2}\max_{h\ne0}
 \frac{R_A(h)}{1+L/\operatorname{ord}(h)}
 \ \ge\ c_\delta D. \tag{7}
\]
Equations (5) and (7) supply two available comparison profiles. The former can also exploit high-order differences lying in a good character arc, which the latter prices at the uniform scale.

## Ranked tests

1. For actual supercritical near-cap configurations, cover their repeated differences by autocorrelations of opposite feasible rows using (3), allowing several prime sign runs and the full actual optimizer. An \(o(d)\) paid cover with small diagonal excludes the configuration. If a fixed class fails, identify whether the residual comes from near-periodic shifts, poor opposite autocorrelation or a small set of possible centering sites.
2. For exact-cap shifts compare the local mask in (2) with the global bound (3). A genuine upper on the localized hinge of one cap-centered optimizer suffices in the marked-window criterion. For an optimizer with a singleton cap, test the actual weighted tail on its primary support directly.
