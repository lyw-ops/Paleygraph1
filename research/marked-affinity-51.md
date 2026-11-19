# A marked bound from bulk product affinity

A positive complementary pair supplies a certified real mark at its own product weights. Its transfer to the actual weights improves on the square-root weight bound when the mark carries a substantial fraction of the total weight. At \(a=1/2\), the new bound certifies \(|m_p(a)|<0.017\) with short zero-start Picard prefixes at primes 97 and 173 for which the old distance bound exceeds 0.018. Both pairs are built at the target floor. No stationary solve is used.

## Keep the two complementary cross products

Let \(P,Q\) and \(P',Q'\) be two strictly positive complementary pairs, with mean one for every row. The products normalized to probability are \(d_i=P_iQ_i/n\) and \(d_i'=P_i'Q_i'/n\). Set \(\gamma_i=\frac12\log(P_i/Q_i)\) and define \(\gamma'_i\) the same way. The first-order equations identify each pair as stationary for its own product weights. Cross pairing gives exactly
\[
 \sum_i\sqrt{d_i d_i'}\,e^{\gamma_i-\gamma'_i}=1,\qquad
 \sum_i\sqrt{d_i d_i'}\,e^{-(\gamma_i-\gamma'_i)}=1 .
\]
Write \(A=\sqrt{d_0 d'_0}\), \(B=\sum_{i\ne0}\sqrt{d_i d'_i}\), \(\eta=\gamma_0-\gamma'_0\), and \(D=1-A-B\). Then the bulk \(\sinh\) sum is \(-A\sinh\eta\), while its \(\cosh\) sum is \(1-A\cosh\eta\). Jensen's inequality for \(z\mapsto\sqrt{1+z^2}\) yields
\[
 A\cosh\eta+\sqrt{B^2+A^2\sinh^2\eta}\le1.
\]
Squaring after moving the first term to the right and using \(\cosh^2-\sinh^2=1\) gives
\[
 \boxed{\qquad
 4\sinh^2(\eta/2)\le\frac{(1-A)^2-B^2}{A}
              =\frac{D(1-A+B)}{A}.
 \qquad}                                                        \tag{1}
\]
For finite computations \(D=\frac12\sum_i(\sqrt{d_i}-\sqrt{d_i'})^2\) avoids cancellation of large terms. Equality in (1) occurs precisely when \(\gamma_i-\gamma_i'\) is constant on the bulk. Spending all of the \(\cosh\) excess on the mark alone would replace the factor \(1-A+B\) by \(2\). For two constant bulk weights with common marked weight one, (1) gives exactly \(|\eta|\le\frac12|\log(W'/W)|\), as does the marked leverage bound.

## Bulk errors at cold weights

Take unnormalized weights \(w,w'\) with \(w_0=w_0'=1\) by separate rescalings of the two products. Set \(W=\sum w,\ W'=\sum w'\), \(b=W-1,\ b'=W'-1\), and \(J_b=\sum_{i\ne0}\sqrt{w_iw'_i}\). The right side of (1) is
\[
 \frac{(\sqrt W-\sqrt{W'})^2+(bb'-J_b^2)}{\sqrt{WW'}}.             \tag{2}
\]
This separates the bulk mass mismatch from the dispersion of the bulk weight profile. In particular
\[
 |\eta|
 \le \sqrt{\max\{b/W,b'/W'\}}\ \|\sqrt w-\sqrt{w'}\|_2.
                                                                    \tag{3}
\]
Indeed the squared distance in (3) equals \((\sqrt b-\sqrt{b'})^2+2(\sqrt{bb'}-J_b)\). The first square on the numerator of (2) is bounded by the first term of this identity times \((\sqrt b+\sqrt{b'})^2/(\sqrt W+\sqrt{W'})^2\). The remaining numerator is bounded by the second term times \(\sqrt{bb'}\). Divide by \(\sqrt{WW'}\) and use \(4\sinh^2(\eta/2)\ge\eta^2\). If \(W=W'\), (2) simplifies to \((b^2-J_b^2)/W\). In particular for \(w_i=a/n\) on the bulk and \(W'=W\), an \(o(a)\) bulk weight error in counting \(\ell_1\) gives an \(o(a)\) marked error as \(a\downarrow0\).

The mixed products also bound what a good pair can say about the actual bulk. Write \(r_i=P_i/P_i'\), \(s_i=Q_i/Q_i'\). In \(d'\)-weighted counting measure,
\[
 \sum_i d_i'(\sqrt{r_i}-\sqrt{s_i})^2=2D,\qquad
 \sum_i d_i'\big((\sqrt{r_i}-1)^2+(\sqrt{s_i}-1)^2\big)\le 6D .
\]
For the second inequality use the pointwise relation for \(u=\sqrt{r_i},v=\sqrt{s_i}\)
\[
 (u-1)^2+(v-1)^2=(u-v)^2+2(uv-u-v+1)
 \le (u-v)^2+2(\sqrt{uv}-1)^2
\]
since \(u+v\ge2\sqrt{uv}\). Here \((\sqrt{uv}-1)^2=((d_i/d_i')^{1/4}-1)^2\le(\sqrt{d_i/d_i'}-1)^2\). Thus if \(d_i'\) is bounded below by a constant times \(1/n\) and \(P_i',Q_i'\) are bounded above on the bulk, the two actual rows differ from the trial rows by \(O(\sqrt D)\) in normalized bulk \(\ell_1\). The actual first mass on sites above twice the respective trial bulk upper bounds is \(O(D)\). These conclusions give no entrywise bound for the actual rows.

## Exact prefix controls

For \(v_t\) from the true zero-start Picard orbit at \(a=1/2\), set \(u_t=\Phi(v_t)\), \(v_{t+1}=Ku_t\), and take the rows proportional to \(u_t\pm v_{t+1}\). They are in complementary sectors and have equal means since \(K\mathbf1=0\). The sole positivity check is \(u_t(i)>|v_{t+1}(i)|\) at every site. Their unscaled product weights are \((u_t^2-v_{t+1}^2)/4\); the trial marked logarithm is \(\frac12\log((u_t(0)+v_{t+1}(0))/(u_t(0)-v_{t+1}(0)))\). The [Arb checker](marked-affinity-51-check.py) verifies positivity, computes (1) and compares the older bound with the marked weights scaled to one.

| Order | Prefix \(t\) | Rigorous conclusion from (1) | Older transfer bound for the same trial |
|---|---:|---:|---:|
| 97 | 9 | \(|m_{97}|<0.01469\) | upper bound exceeds \(0.022\) |
| 173 | 16 | \(0.01375<m_{173}<0.01690\) | upper bound exceeds \(0.018\) |
| 401 | 32 | \(m_{401}<-0.0184\) | still detects negative mark |
| 121, square | 16 | \(m_{121}>0.091\) | lower bound below \(0.081\) |

The four [interval records](marked-affinity-51-checks.jsonl) are finite. At prime 401 the same target tolerance actually fails. These prefixes give no uniform positivity or product-dispersion bound at the cold floor.

As a floating diagnostic, shifting \(u_t\) by a constant to match the normalized marked product exactly improved the upper estimate at \(p=173,t=15\) from about \(0.017342\) to \(0.017323\). This still exceeded the target \(0.017\). At \(p=97,t=8\) the shift slightly increased the estimate. The interval checker uses the original prefixes.

## A shorter square stencil using the new hot interval

The [real decay theorem](astra-warm-51.md) permits anchor \(T=25\) in the existing [Chebyshev stencil](astra-pick-46.md#one-explicit-extrapolation-inequality-for-the-actual-square-control). Take \(a=1/2,\ J=93\), and \(x_i=1-i/[100(J+1)]\) for \(1\le i\le J\). Each hot floor \(25\sqrt{x_i}\) exceeds \(197/8\). The hot linear combination tends to zero through squares since every coefficient is fixed. For every field, \(W_n(T)/W_n(a)\le52/3<e^3\). Therefore the analytic budget is at most \(3(49/51)^{93}<0.074\), while the square lower limit of the cold mark is at least \(\frac12\log(4/3)>0.14\). This gives a square violation of the whole-right-half-plane bound with eventual excess greater than \(0.06\), using 35 fewer hot nodes than round 47. It uses no claim of a uniform complex domain through primes. The checker emits one exact rational record for these constants.

1. For a positive prime trial at a prescribed floor, measure (2), retaining the exact mass normalization. To propagate a bound it suffices to control (2) plus the trial logarithm after the field limit. A prime subsequence with positive order-one normalized product dispersion can rule out a vanishing error from this specific comparison.
2. At colder floors with total bulk weight \(O(a)\), track the two terms in (2) separately. A balanced product with \(o(a)\) bulk \(\ell_1\) error yields \(o(a)\) marked error. An excessive bound from uncentered bulk energy can be checked against this sharper quantity, while lack of positivity invalidates the trial regardless of its reported product discrepancy.
