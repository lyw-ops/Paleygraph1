# The leading mixed block on the actual Jacobi column

Use \(S=s_nC_1\) and the actual Legendre center \(Y\) from [Round 55](astra-rankthree-55.md#exact-feedback-and-arithmetic-weights). Let \(B_S=K\,\operatorname{diag}(S_i/(2\sqrt{t_i}))\) and \(B_Y=K\,\operatorname{diag}(\alpha Y_i/(2\sqrt{t_i}))\), where \(\alpha\) is the fixed coefficient of \(Y\) in the actual cold center prescription. The marked floor is \(t_0=n\); all other floors are \(t\) on the original square. On the actual seed column \(C_1\), the exact sign computation with the bulk derivative factors gives
\[
 (B_SB_Y+B_YB_S)C_1
 = \frac{\alpha s_n}{4t}
       \left(F_4+\frac{D+D^\vee}{8}+\frac R4\right)
       +O_{P_{5000}}(n^{-1/2}),                                  \tag{1}
\]
uniformly for sufficiently large eligible primes. Here \(F_4\) is the earlier rank-four field, \(D,D^\vee\) are the subsequent rank-four dual pair and \(R\) is the mixed Legendre field. They are the actual fields of the cold prefix.

For the computation first use the uniform bulk denominator on every coordinate. The bracket before the two factors of the denominator is
\[
 K\left[C_1K(C_1Y)+Y K(C_1^2)\right].
\]
By the actual feedback, \(K(C_1Y)=W+C_1/p\) and \(K(C_1^2)=Y/2-C_1/\sqrt p\). The first order of the mixed sum therefore contributes \(K(C_1W)\) up to vanishing terms, and the second contributes \(K(Y^2)/2\). The [rank-four feedback](astra-rankfour-57.md#third-distinguished-subtraction) makes the former \(F_4\), up to a bounded multiple of \(Ke_0\). Writing \(Y=(A+B)/2\) gives \(Y^2=(S_A+S_B)/4+(AB)/2+1/2\). Thus the [exact quadratic feedback](astra-joint-64.md#exact-physical-feedback-on-both-lifts) gives \(K(Y^2)/2=(D+D^\vee)/8+R/4\) up to a bounded multiple of \(Ke_0\). This computation uses the full feedback rows including the exceptional frequency.

To restore the actual marked denominator in each step, a difference at zero gives a bounded coefficient times the input's zeroth coordinate times \(Ke_0\). This costs \(O_{P_{5000}}(n^{-1/2})\) relative to the input price. Each adjacent bulk leading step has bounded packet price by the one-word translated estimate, and \(C_1\) has bounded price. This absorbs both marked restorations. All other feedback corrections above are either such multiples of \(Ke_0\) or bounded-price fields with \(O(p^{-1/2})\) scalar coefficient. [Translated-column repair](shifted-resolvent-96.md#the-two-estimates-for-one-physical-derivative-step)

The \(F_4\) constituents and those of the newer \(D,D^\vee,R\) fields have distinct derived types by the [independent group calculations](two-node-groups-59.md) and [mixed Legendre independence](astra-rankeight-60.md). Thus the two main responses on this input column have no equal arithmetic labels to pool with opposite signs. Equation (1) concerns the selected leading mixed block on one genuine input, with the inverse line included. It gives neither a bound on all translated packets nor a lower on the full signed square rate.
