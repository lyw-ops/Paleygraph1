# Total clipping correction as the phase cap opens

Fix one physical floor \(t\) in the right half-plane. On the range of symmetric phase caps \(|\tan\phi_i|\le a<1\) with \(a>|\Im t|/(2\Re t)\), the canonical total bulk correction is a continuous, nonincreasing function of \(a\). Wherever positive it decreases at a rate bounded below by the total product on the positively corrected sites, with a coefficient independent of the field. The conclusion allows nonunique clipped rows. It relates different cap tests at the same floor and leaves the required vanishing at a common cap open.

## Comparing genuine roots at different caps

Let \(s=u+iv=n/t\). At each \(a\), use the genuine [clipped product equations](real-phase-projection-89.md#an-everywhere-positive-clipped-construction) with \(\kappa=a^{-2}\). Write \(q_i=1+e_i\) for the bulk products, \(w=\Re A\,\Re B>0\), \(\nu=\sqrt w\), \(J_w\) for the weighted real reflection, \(b=v/(2\nu_0)\), and \(z=bJ_w e_0\). In particular \(w_i+z_i^2=q_i\) in the bulk and \(D_i=z_i/\nu_i\) is its phase tangent. Let \(\mathcal A=\{i\ne0:e_i>0\}\) and write \(E(a)=\sum_{i\ne0}e_i\), with **counting** normalization.

Existence of an even clipped pair holds at every cap by the positive real weight box. The section below applies to any genuine clipped pair. For a fixed cap the anisotropic bulk secant estimate of [round 90](clipped-signs-90.md) holds for every \(0<a<1\). The marked relative phase is at most \(|\arg(t)|/2<\arctan a\), by the two same-sign marked tangents and the range assumption. Therefore the marked secant is strict in that metric. The common mean from the Hilbert identity makes \(E(a)\) canonical at each cap.

For a compact interval of caps in this range, the real weighted box has a positive lower bound and a finite upper bound for each fixed field. The real stationary factors are bounded by their common real-part sum and bounded below by the weight minima divided by that same bound on the opposite factors. Tangents are bounded by \(a\) on the bulk and by \(|v|/u\) at the mark. Thus the genuine clipped pairs lie in a compact set inside the positive real-part chart, their graph is closed there, and \(E(a)\) is continuous by compactness and its canonicity. The graph is semialgebraic. The complementary sectors and mean impose linear equations, the prescribed products impose polynomial equations in real and imaginary coordinates, and the bulk cap and correction conditions are the polynomial constraints \((\Im A_i)^2\le a^2(\Re A_i)^2\), \(e_i\ge0\), and \(e_i(a^2(\Re A_i)^2-(\Im A_i)^2)=0\). Semialgebraic selection and the one-variable piecewise differentiability theorem give genuine differentiable pairs on finitely many open subintervals of a compact cap interval. For example, select by semialgebraic triviality over a finite partition and take the coordinatewise smooth subintervals of each resulting section. No common differentiable selection across all breakpoints is required. [Hardt's semialgebraic triviality](https://doi.org/10.2307/2374240)

## Dissipation from the same physical reflection

At a point of a differentiable selection fix the floor. The [fixed-product elimination](astra-contact-91.md#real-differential-with-the-marked-product-held-fixed) gives a real symmetric \(L\) with \(\|L\|\le a\) and
\[
 dz_B=H\,\operatorname{diag}(1/(2\nu_B))\,dq_B,
 \qquad H=(I+LD_B)^{-1}L=H^{\mathsf T}.
\]
Here \(B\) denotes the bulk, and \(D_B\) also denotes its diagonal operator. The norm proof in that elimination applies for every \(0<a<1\): the norm of the eliminated marked \(2\)-by-\(2\) matrix is \(|D_0|/\sqrt{1+(b/\nu_0)^2}\le |v|/(2u)<a\), and the bulk tangents have modulus at most \(a\). Thus the feedback \(\|LD_B\|\le a^2<1\) and the response applies even if some sites are exactly tied.

Let \(h_i=\dot q_i/\nu_i\), and use a dot for differentiation in \(a\). Since each \(q_i\ge1\), \(h_i=0\) off \(\mathcal A\) at these differentiable points. On \(\mathcal A\) set \(\sigma_i=\operatorname{sign}(D_i)\), \(S=\operatorname{diag}(\sigma_i)\), and \(m=(1+a^2)/a\). Differentiate \(q_i=(1+a^{-2})z_i^2\) there and divide by \(\nu_i\). This yields
\[
 M h_{\mathcal A}=-2\nu_{\mathcal A}/a,\qquad
 M=I-m S H_{\mathcal A\mathcal A},\qquad
 -E'(a)=\frac a2\,h_{\mathcal A}^{\mathsf T}M h_{\mathcal A}.             \tag{1}
\]
When \(\mathcal A\) is empty the derivative is zero. The opposite sign blocks of \(M\) are skew transposes. On a given sign \(\sigma\) put \(T=\sigma D_B\), \(X=\sigma L\), and \(G_T(X)=(I+XT)^{-1}X\). By the Loewner derivative formula of round 91, \(-aI\preceq X\preceq aI\) implies
\[
 0\preceq \Gamma_\sigma=G_T(aI)-G_T(X)
       \preceq G_T(aI)-G_T(-aI)
       =2a(I-a^2T^2)^{-1}.
\]
On the \(\sigma\)-supported subspace, multiplication by \(T\) is exactly \(a\). For \(f\) supported there the full row \((I-m\sigma H)f=m\Gamma_\sigma f\). Restriction to \(\mathcal A\) followed by multiplication by \(\sigma S\) gives \(Mf\). It follows that
\[
 \|Mf\|^2\le m^2\|\Gamma_\sigma\|\,f^{\mathsf T}\Gamma_\sigma f
            \le \frac{2}{1-a^2}\, f^{\mathsf T}Mf .
\]
For both signs together use \(\|M(f_++f_-)\|^2\le2(\|Mf_+\|^2+\|Mf_-\|^2)\). The skew off-diagonal blocks cancel in the quadratic form. Thus \(M\) has positive semidefinite symmetric part and
\[
 \|Mh\|^2\le \frac4{1-a^2}h^{\mathsf T}Mh .
\]
Substitution of (1) proves the field-independent inequality
\[
 \boxed{\quad -E'(a)\ \ge\
    \frac{1-a^2}{2a(1+a^2)}\sum_{i\in\mathcal A}(1+e_i)
   =\frac{1-a^2}{2a(1+a^2)}\big(|\mathcal A|+E(a)\big).\quad}           \tag{2}
\]
On a subinterval with one active sign the coefficient doubles. The individual signed totals can have an extra term from the opposite sign block in (1).

These inequalities hold on each differentiable subinterval. Integrate on compact pieces, take the one-sided limits, and sum over the finite partition. In particular, for any \(a_1<a_2<1\) in the allowed range,
\[
 E(a_1)-E(a_2)\ \ge\
 \int_{a_1}^{a_2}\frac{1-a^2}{2a(1+a^2)}
          \big(|\mathcal A(a)|+E(a)\big)\,da                            \tag{3}
\]
for any piecewise semialgebraic choice of genuine rows. Each cap with positive \(E\) has at least one positively corrected site. Thus if \(E(a_2)>0\), the integral is bounded below by the same integral with \(|\mathcal A|\) replaced by one. Equivalently, initial price less than or equal to that one-site charge forces exact zero at the wider cap. The one-site threshold in counting units is
\[
 \frac12\log\frac{a_2(1+a_1^2)}{a_1(1+a_2^2)} .
\]
One can also keep the \(E(a)\) term by integrating \(-\partial_a\log(1+E)\) while the correction is positive. Let \(C_{12}\) be the displayed one-site threshold. It follows that \(E(a_2)\le[(1+E(a_1))e^{-C_{12}}-1]_+\). The same argument with \(2C_{12}\) applies when at most one sign is positively corrected on the interval. These are dimension-free thresholds for the unaveraged correction. The round-90 cold residual bound controls the averaged correction and still permits the unaveraged value to exceed these thresholds for unbounded fields.

## A real-column test throughout the positive-correction range

At any cap in the sweep with the stronger marked condition \(|v|/u<a\), the [two-real-mark representation](real-two-marks-91.md) still applies when \(E(a)>0\). Its shared bulk profile is \(k_i=q_i-(1+a^{-2})z_i^2\in[0,1]\). The marked absolute phases stay in the cone, since both marked tangents have modulus at most \(|v|/u\). Let \(r_\pm=\sqrt{h\pm v/a}\) be the endpoints of its real column integral and choose any \(0<\xi<1\). Set \(k'_i=\max(k_i,\xi)\), \(b_i=(\xi-k_i)_+\), and \(\lambda_i=b_i/\sum_B b_j\) when this sum is positive. Write \(\sigma_i=\operatorname{sign}z_i\). The Hellinger comparison of [the real-column transfer](astra-velocity-92.md#simultaneous-changes-to-the-real-weights) uses only nonnegative stationary endpoints with common bulk weights, so it gives
\[
 \int_{r_-}^{r_+}\sum_i\lambda_i\sigma_i(J_{(r^2,k')})_{i0}\,dr
 \ge \sqrt\xi\left[2\operatorname{arctanh}\sqrt{\frac{1-\xi}{1+a^2\xi}}
             +\frac{\xi}{\sum_B b_j}\sum_{i\in\mathcal A}\log(1+e_i)\right].       \tag{4}
\]
In fact the favorable original product in that comparison is \(F_i=(\nu_i+|z_i|/a)^2\). It is \(q_i\) times the favorable product at bulk product one and depleted weight \(k_i/q_i\). The latter is decreasing in the depleted weight on \([0,1]\): write it as \((\sqrt{1-z^2}+|z|/a)^2\), where \(0\le |z|\le a/\sqrt{1+a^2}\). At depleted weight \(\xi\), its ratio to \(\xi\) is \((1+d)/(1-d)\) with \(d=\sqrt{(1-\xi)/(1+a^2\xi)}\). Hence on the selected sites \(\log(F_i/\xi)\ge 2\operatorname{arctanh}d+\log q_i\). Every corrected site has \(k_i=0\) and \(b_i=\xi\), so averaging gives (4). This extends the necessary almost-flat real-column large response from the first tie to every positively corrected cap. The additional log term retains the actual sizes of the clipped products.

## Prime validation

At \(p=173\) and \(t=1/50+13i/1000\), the real-start branch has one site near first contact. The checker encloses the true clipped solution at three rational caps and applies a differentiated fixed-point equation at each positively charged cap. Floating-point iterations propose the centers, while outward contraction and interval derivatives certify all records. At \(a=7/10\) and \(a=707/1000\) the positive orbit \(43\) is the only charged site. Their correction slopes lie in \((-10.483,-10.482)\) and \((-10.286,-10.285)\), respectively. At \(a=143/200\) the site is strictly inside the cap and the original product equations hold on every site. This parameter lies outside the nominated cold square. [Checker](cap-sweep-92-check.py) · [Outward records](cap-sweep-92-checks.jsonl)

1. Combine the integrated loss (3) with a lower bound on the number or the total product of active coordinates forced by the same physical residual on an interval of caps. The threshold for a single site is insufficient at unbounded \(p\).
2. Seek a compression estimate for the actual two sign blocks that improves the coefficient or separately controls the signed transfer in (1). Track the same floor throughout the comparison.
