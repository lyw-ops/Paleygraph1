# Two nonnegative prices for the signed marked projection

The capacity trace on the true face is determined to additive \(O_\delta(d^{-1/2})\) by one positive marked leverage. Its exact factorization separates the ordinary signed leverage from one angle involving nonnegative exterior multipliers. At a fixed gap the actual pin gives an explicit such multiplier. Its projected error is small simultaneously on **all** coordinates. The fixed common head gives a second multiplier with exponentially small error. Both tests apply to the same signed marked row and retain their own positive prices on its negative coordinates.

## Root leverage with the actual complementary support

Use the good time, true pin \(R\), companion \(Z\), length \(d\), deficit cutoff \(u=\delta/8\), mask \(P\), and capacities \(c\) of [round 84](astra-capacity-84.md). The optional head \(T\) is empty or the single frozen head of [round 83](astra-split-83.md). Put \(h=Z1_P\), \(g=1_T+h/d\). Let \(a\) be the larger optimum and \(r\) any genuine opposite optimizer with \(nar_0=1\). Write \(S=\{i\ne0:r_i=0\}\), \(I=\{0\}\cup S\), \(C=S\cap (T\cup P)\). On \(I\) use the positive weights
\[
 w_0=a^2,\qquad w_i=c_i\quad(i\in C),\qquad w_i=da\quad(i\in S\setminus C).
\]
Let \(W=\operatorname{diag}(\sqrt{w_i})\). In the ordinary Euclidean space on \(I\) let \(V\) consist of all \(x\) for which \(Wx\), extended by zero, lies in the constants plus the primary Fourier sector. Write \(L\) for its orthogonal projector, \(e=e_0\), and \(\ell=L_{00}\). These use only the true opposite support, weights and Fourier projector. For example with \(E_I\) the coordinate inclusion and \(P_{-\sigma}\) the pure opposite projector, \(L\) is the kernel projector of \(P_{-\sigma}E_I W\).

Every such signed row \(y=E_IWx\) satisfies \(\sum_i y_i=n\langle y,r\rangle=nr_0y_0=x_0\). Hence \(x_0=1\) gives the prescribed root \(y_0=a\) and mass one. Requiring \(x\ge0\) describes precisely the full genuine face. The availability of an optimizer implies \(\ell>0\). Define the positive marked leverage by
\[
 \ell_+=\|\operatorname{proj}_{V\cap\mathbb R_+^I}e\|^2.
\]
The least full squared norm of a positive row \(x\) with \(x_0=1\) is \(1/\ell_+\). Indeed the cone projection \(v\) satisfies \(v_0=\|v\|^2>0\) and \(x_0\le\langle v,x\rangle\le\|v\|\|x\|\) on the cone. The row \(v/\ell_+\) attains equality.

The genuine trace \(\Xi\) in round 84 satisfies
\[
 0\le \sqrt{1/\ell_+-1}-\Xi\le \sqrt{c(C)+1/d}
                  =O_\delta(d^{-1/2}).                                      \tag{1}
\]
In fact \(h_i>(2d-1)u\) on \(P\) by the actual terminal pairing. Thus \(c_i\le d/[n(1+h_i)]\ll_\delta1/n\) there, and \(|P|/n\ll_\delta 1/d\). The common head has exponentially small \(c(T)\). For each true \(q\), compare its weighted exterior vector with \(1_C(q-c)_+/\sqrt c\), extended by zero. The difference has squared norm at most \(c(C)+\sum_{S\setminus C}q_i^2/(da)\le c(C)+1/d\), by the actual point cap \(q_i\le a\). The exterior norm dominates the overflow norm pointwise. Taking the two minima gives (1). In particular \(d\ell_+\to\infty\) is equivalent to \(\Xi=o(\sqrt d)\) on these profiles. This gives the genuine joint mismatch upper \(o(1)\) from round 84.

## The sign loss and an explicit multiplier from the actual pin

Use the ordinary cosine of nonzero Euclidean vectors and set
\[
 \rho=\sup_{z\ge0,\ z_0=0,\ Lz\ne0}
       \frac{[-\langle Le,Lz\rangle]_+}{\sqrt\ell\,\|Lz\|},
 \qquad
 \boxed{\ \ell_+=\min_{z\ge0,\ z_0=0}\|L(e+z)\|^2
                     =\ell(1-\rho^2).\ }                                  \tag{2}
\]
Use zero if the test family is empty. The polar of the positive cone in \(V\), considered in the full space, is \(V^\perp-\mathbb R_+^I\), a closed polyhedral cone. The squared distance of \(e\) to this polar is \(\ell_+\). Eliminating \(V^\perp\) gives the minimum in (2) initially over all \(z\ge0\). A positive \(z_0\) only increases the best squared norm, by factoring \(1+z_0\) out of \(e+z\). Minimizing on each nonnegative ray gives the cosine formula. For an attaining \(z\), the cone projection is \(L(e+z)\), and complementarity gives \(z_i[L(e+z)]_i=0\) for every \(i\). Thus an optimal angular witness can charge only zeros of the attained genuine row.

Write \(m=R_0/\sqrt n\), \(M=1-a\), \(\gamma=\sqrt n a\), and
\[
 B=aR_0-\overline R-uM=m(\gamma-1-\epsilon)-uM .
\]
At the prescribed fixed gap \(B\gg_\delta1\). Let \(t_i^\pm=\sqrt{w_i}(R_i+u)_\pm\) for \(i\in S\), \(t_0^\pm=0\). There is an exact vector identity and a one-sided prime-uniform bound
\[
 L(Be+t^+)=Lt^-,\qquad \|t^-\|\ll_\delta d^{-1/2}.                        \tag{3}
\]
Indeed every \(x\in V\) has exterior pairing \(\sum_S y_i(R_i+u)=-Bx_0\), including signed \(x\). This proves the identity by orthogonality. The negative part is supported on \(C\cap P\), and there it is bounded by \(\theta h\) with \(\theta=(2d-1)^{-1}\). The actual bound \(\sum_C c_i(h_i/d)^2\ll_\delta1/d\) gives the stated norm. The positive multiplier \(t^+/B\) in (2) is thus prescribed by the physical pin. If \(d\ell\to\infty\), its projected vector approximates \(-Le\) in relative norm \(O_\delta((d\ell)^{-1/2})\).

The canonical signed marked row \(y=E_IWLe/\ell\) has full weighted norm \(1/\sqrt\ell\). Its negative sites must satisfy the measurable price
\[
 \sum_{i\in S}(y_i)_-(R_i+u)_+
    \ \ge\ B-O_\delta\big((d\ell)^{-1/2}\big).                           \tag{4}
\]
Indeed \(\sum_S y_i(R_i+u)_+=-B+\sum_S y_i(R_i+u)_-\), and the last sum is bounded in absolute value by \(\|t^-\|/\sqrt\ell\). Establishing \(d\ell\to\infty\) and an \(o(1)\) upper on the left at one admissible time therefore suffices against a fixed gap. This test requires just a signed projector solve and the positive part of the actual pin.

The same interpolation gives a signed support estimate for **every** root trace direction in round 84, including the ones tested by its (7) and (8). Normalize a direction by \(H=U-(U_0/r_0)r\) and put \(N^2=\sum_C c_i(U_i)_+^2\). Then \(H_0=0\), \(H|_S=U|_S\), and \(b(U)=\overline H=\sum_S y_i U_i\). Since \(U\le0\) on \(S\setminus C\),
\[
 \left|b(U)-\sum_C c_i(U_i)_+ +\sum_S y_i(U_i)_-\right|
 \le N\left(\sum_C (y_i-c_i)^2/c_i\right)^{1/2}
 \le N\big(\sqrt{1/\ell-1}+\sqrt{c(C)}\big).                         \tag{7}
\]
The expression in absolute values equals \(\sum_C(y_i-c_i)(U_i)_+\). Thus, when \(d\ell\to\infty\), the trace divided by \(\sqrt d\) agrees up to \(o(1)\) with the supremum of \([-\sum_S y_i(U_i)_-]_+/(\sqrt d\,N)\). Zero denominators contribute zero on both sides because then \(-\sum_S y_i(U_i)_-=b(U)\le0\). This transfers the signed exterior mean on the positive support of \(r\) to a price on the exposed side, retaining the credit from positive \(y\) at negative \(U\).

For the common head let \(\beta=\min_{q\in\mathcal Q_a}q(T)>0\). Finite LP duality on the moment equations on \(S\) supplies a real opposite \(U\) satisfying \(U_i\le1_T(i)\) on \(S\) and \(\overline U-aU_0=\beta\). Define \(s_i=\sqrt{w_i}(1_T(i)-U_i)\ge0\) on \(S\) and set \(s_0=0\). With \(1_{S\cap T}\) extended by zero at the root,
\[
 L(\beta e+s)=L W1_{S\cap T},\qquad
 \|W1_{S\cap T}\|\le\sqrt{c(T)},\qquad
 \sum_S (y_i)_-(1_T(i)-U_i)\ge\beta-\sqrt{c(T)/\ell}.                    \tag{5}
\]
The vector identity again follows by testing every signed row, now with \(U\). The canonical row has \(|y(T)|\le\sqrt{c(T)/\ell}\), giving the last inequality. In particular \(\ell_+\le c(T)/\beta^2\). The head price and the pin price constrain the same negative sites of the same signed row, with their respective weights. The two prices can be supported on different subsets of those sites.

## Deleting negative coordinates while retaining a genuine row

The ordinary signed projector also yields a finite lower certificate for \(\ell_+\). On any current support \(B'\subset I\) containing the root, let \(L'\) project onto the corresponding subspace of \(V\), extended by zero. For a site \(i\) with \(L'_{i0}<0\), enforcing \(x_i=0\) updates the projector by
\[
 L''=L'-\frac{L'e_i e_i^tL'}{L'_{ii}},\qquad
 L''_{00}=L'_{00}(1-\eta_i),\qquad
 \eta_i=\frac{|L'_{i0}|^2}{L'_{00}L'_{ii}}.                               \tag{6}
\]
The negative entry ensures \(L'_{ii}>0\). Start with any genuine normalized \(x\). Move on the segment from \(x\) toward \(L'e/L'_{00}\). Delete a negative coordinate at the first time it hits zero, allowing time zero when it already vanishes. Up to this time every coordinate is nonnegative, and the root is one along the whole segment. Carry the endpoint as the next genuine row. Thus every pivot has \(\eta_i<1\). After at most \(|I|-1\) pivots the current root column is nonnegative and supplies a genuine comparison row. Its attained leverage is \(\ell\prod_i(1-\eta_i)\le\ell_+\), yielding a prime-uniform sufficient test \(d\ell\prod_i(1-\eta_i)\to\infty\).

There exists a pivot path attaining equality. Start with the full positive minimum-norm marked row \(x^*\). On each restriction containing its support it is still the positive minimizer. If the current signed minimum \(x^s=L'e/L'_{00}\) differs from \(x^*\), some zero of \(x^*\) has \(x_i^s<0\). Otherwise the segment toward \(x^s\) would have a feasible initial interval and strict norm decrease by orthogonality of \(x^s\) to the zero-root tangent. Delete that zero. The terminal signed minimum is then \(x^*\). The path construction for a general initial row gives a lower bound without knowing this optimum.

## A negative pair necessary for positive completion

At prime 97, the actual time-four profile, the frozen twenty-site head and capacity scale \(1/5\) of [round 84](astra-capacity-84.md), take uncharged weight \(4a\). The ordinary signed leverage is in \((0.725461134,0.725461135)\). The positive leverage is in \((0.381738160,0.381738161)\) and the exact squared cosine in (2) is in \((0.473799294,0.473799295)\). The signed marked row assigns the reflected pair \(2,46\) combined mass in \((-0.021003934,-0.021003933)\). Yet the minimum of this pair mass over **all** true optimizers is in \((0.031888198,0.031888199)\). Deleting this one reflected negative pair destroys all genuine marked completions. The two other negative pairs, at anchors \(10,21\) and their reflections, carry the positive multipliers attaining (2).

The interval check uses the exact two-parameter even slice of the complementary cyclotomic faces and its normalized three-column span before fixing the root. Reflection preserves all weights and the root, so the ordinary root projection and the positive cone projection are even. Minimizing the reflected pair mass over evenized rows also gives its full-face minimum. A positive combination of the anchor-10 and site-3 inequalities certifies the lower, with a feasible equality point. Direct multiplication verifies both the optimal projected nonnegative multiplier and the unnormalized physical identity (3). At this finite cutoff \(B<0\), so it does not instantiate the fixed-gap conclusion. [Arb384 replay](astra-overflow-85-check.py) · [Interval receipt](astra-overflow-85-checks.jsonl)

1. On one admissible prime window, bound the ordinary signed leverage from below with \(d\ell\to\infty\). Then test the actual signed negative-coordinate price in (4), or simultaneously its frozen-head counterpart (5).
2. For a direct positive completion, estimate cumulative marked leverage lost in (6) along a path retaining a genuine row. Alternatively bound the exterior positive cosine in (2) at the required joint rate \(d\ell(1-\rho^2)\to\infty\). The marked prime-uniform rate is open.
