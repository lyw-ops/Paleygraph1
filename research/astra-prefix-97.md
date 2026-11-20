# Temporal minority bounded by one positional fiber of the real prefix

On the bounded trapped family, a recurrent mask forces either an order-$J$ first absolute moment on its original block at some prefix, or an order-$J^2$ **signed block mean** on a translate at the prescribed full prefix $J$. The second test uses only the identity positional fiber. It also has a version that keeps the original block out of the input and minimizes a linear functional over genuine companion-sector quotient probabilities. The argument gives a finite upper bound on the temporal minority on the entire original block.

Use the [bounded-family selector](astra-quotient-94.md) with fixed positive target mass, its [size filter and erasures](astra-recur-95.md), and the [signed-prefix comparison](astra-fiber-96.md). Write $G=\widehat Q$, $n=|G|$, $J=\lfloor D(p)/8\rfloor$, $C$ for the recurrent coset and $L$ for the union of $C$ and its subgroup. Set $m=|L|$, $B=L^\perp$, and let $\sigma$ be the companion (optimizer) sign. The selector supplies $w_* >0$ depending only on the target mass with $\Theta_\sigma(B)/|B|\ge w_*$. Retain this filter on the candidate list. The matrix $M=\mathsf K_{L,L}$ has first and supremum norms at most $\kappa\le\kappa_*<1$. Its signed row sum $\lambda=\sum_{i\in L}\mathsf K_{0i}$ has $|\lambda|\le\kappa$. These facts hold for the same list and sign.

Let $q$ be any probability constant on each translate $R$ of $L$, with $\mathsf Kq=\sigma(q-\mathbf1/n)$ and $q(L)=w\ge w_*$. Uniformly lifting a rooted restricted optimizer gives one such row. Write $w_R=q(R)$, $W_j=|Y_j|$ and $\overline W_h=h^{-1}\sum_{j<h}W_j$. For each $R,j$ erase any $A_{R,j}\subset R^c$ of at most $H_p^2$ coordinates within the round-95 budget, and put
\[
 U_h^R=h^{-1}\sum_{j<h}1_{(R\cup A_{R,j})^c} W_j,\qquad
 F_L=\max_{1\le h\le J}\mathbb E_L|\mathsf K U_h^L|.
\]
All transforms use the genuine unmodified cold path. Erasures can depend on that path and on $R$.

## A finite upper for all temporal minorities on the block

For $1\le k\le J-2$ let $m_i^-(k)=\min(\sum_{t=1}^k(Y_t(i))_+,\sum_{t=1}^k(-Y_t(i))_+)$. Then
\[
 \frac{1}{km}\sum_{i\in L}m_i^-(k)
 \le \frac{1}{2wk}\left(2J+\frac{J}{J-k-1}
                  \langle q,\overline W_J\rangle\right).                  \tag{1}
\]
In particular, when $k\asymp J$ and $J-k\asymp J$, an $o(J^2)$ upper on this one full-prefix quotient charge makes the normalized minority $o(J)$. One can choose $q$ after seeing the whole path.

Indeed put $D_j=\sigma\langle q,Y_j\rangle$. Moving $\mathsf K$ onto $q$ in the exact cold update with its actual scalar $\beta_j$ gives the [sector telescope](astra-critical-44.md)
\[
 D_{j+1}-D_j=2\langle q,(-\sigma Y_j)_+\rangle+
                   \beta_j\sqrt n\,q_0-2g_j.
\]
The mark term is nonnegative and the energy identity from zero gives $\sum_{j<J}g_j\le J$. For every $k+1\le t\le J-1$ one therefore has
\[
 \langle q,W_t\rangle\ge D_t
       \ge \frac{2w}{m}\sum_{i\in L}m_i^-(k)-2J.                       \tag{2}
\]
Here $q_i=w/m$ throughout $L$, and the actual $\sigma$-wrong occupation dominates the temporal minority sitewise. Sum these $J-k-1$ inequalities and keep the positive remaining inputs in the full prefix to obtain (1).

The same full-prefix charge has an exact block representation. Before erasures define $U_J^{R,0}=1_{R^c}\overline W_J$. Then
\[
 \sigma\sum_R w_R\,\mathbb E_R\mathsf K U_J^{R,0}
       =(1-\sigma\lambda)\langle q,\overline W_J\rangle
                          -\mathbb E_G\overline W_J.                     \tag{3}
\]
Indeed $\sum_R w_R\,\mathbb E_R\mathsf K\overline W_J
=\langle\mathsf Kq,\overline W_J\rangle$, and the internal column sum on each $R$ is $\lambda$. The global mean on the right is at most two. Replacing every $U_J^{R,0}$ with $U_J^R$ changes the left side by $o(1)$ uniformly, by the round-95 erasure bound and $\sum_R w_R=1$. This expresses the upper (1) using signed exterior transforms only.

## Consequences at the recurrent pin

Suppose a fixed positive fraction of $C$ belongs to the actual negative masks at $b_0J$ or more good times per site, with $b_0>0$ fixed. Then, with positive constants depending only on the fixed parameters, at least one of the following holds:

1. $F_L\ge cJ$.
2. At the **same predetermined** full prefix $J$,
   \[
    \inf_q\ \sigma\sum_R w_R\,\mathbb E_R\mathsf K U_J^R\ge c'J^2.
                                                                          \tag{4}
   \]
   The infimum ranges over all the qualified quotient rows above. In particular there is a translate $R$ with $\sigma\,\mathbb E_R\mathsf K U_J^R\ge c'J^2$. If $F_L<cJ$ for a sufficiently small choice of $c$, then also
   \[
                   \inf_q\langle q,U_J^L\rangle\ge c''J^2 .              \tag{5}
   \]
   This last lower keeps the original $L$ out of the input. Under that same bound on $F_L$, the instantaneous $q$-weighted eroded exterior on $L^c$ pays $\gg J^2$ at every time in a common terminal interval of length $\gg J$, simultaneously for all qualified $q$.

To see this, discard the last $\lfloor b_0J/8\rfloor$ possible terminal times before applying the round-96 visit argument. Each recurrent site still has at least $b_0J/2$ visits for large $J$. Its large-block alternative implies $F_L\ge\exp(c_0J)$ after decreasing $c_0>0$, by differencing two prefixes as in round 96. Otherwise there is a good $T$ with $k=T-2\asymp J$, $J-k\gg J$, and an $E\subseteq C\cap P_T$ of order comparable to $m$ satisfying round-96 (2). The signed term there has absolute upper $O(F_L)+o(1)$ by the supremum bound on the test supported on $L$. If $F_L<cJ$, the complementary minority must pay:
 \[
            \frac1m\sum_{i\in L\setminus E}m_i^-(k)\gg J^2.
 \]
Use $k\asymp J$ and $\mu m=O(1)$ to pass from the normalized charge in round 96 to this estimate. Equations (1)–(3), $w\ge w_*$ and $1-\sigma\lambda\ge1-\kappa_*$ now give (4) with the same time $J$ for all $q$.

For (5), differencing consecutive unnormalized prefixes bounds the mean absolute instantaneous eroded exterior transform on $L$ by $(2J-1)F_L$. The contracted recurrence then gives $\max_{t\le J}\mathbb E_L W_t\le O(1)+[(2J-1)F_L+o(1)]/(1-\kappa_*)$. Its $q$-weighted contribution is at most this bound. Equations (2) and the minority lower give $\langle q,W_t\rangle\gg J^2$ for every $k+1\le t<J$. Decreasing $c$ makes the internal contribution smaller than half this lower. Also $\|q\|_\infty\le1/m=O(1/\sqrt n)$, so the activations erased at any one time cost $o(1)$ against $q$ by the same bound on their first norm used in round 95. Averaging yields (5).

In counting Fourier notation the individual translated test in (4) for $R=a+L$ is
 \[
       \mathbb E_R\mathsf K U_J^R=\frac1n\sum_{z\in B}a(z)s(z)\widehat U_J^R(z).
 \]
Since its input vanishes on $R$, $\sum_{z\in B}a(z)\widehat U_J^R(z)=0$. Subtracting either constant sign isolates the opposite sign with coefficient of magnitude two, up to the identity contribution of absolute size at most two after division by $n$. In (5), $\widehat q$ is supported on the identity and the $\sigma$ part of $B$. Thus (5) depends on one fixed exterior input and is a finite quotient linear program. Uniform bounds $F_L=o(J)$ and an $o(J^2)$ trial upper in (5) would eliminate positive trapped mass at a selected pin. Alternatively one may use (4) and bound the maximum signed translated mean at the one full prefix. The prime-uniform bounds, finite-power escape and the ordinary-theta limit remain open.

## Finite check and next tests

At $p=769$, $|L|=8$, a six-point allowed clique in the order-48 positional subgroup gives an explicit plus-sector quotient law with $w=1/8$ by squaring its character sum. On the zero-start path through $J=16$, the block temporal minority at $k=8$ has mean $0.325000813\ldots$. The full and original-exterior quotient charges are $1.708637932\ldots$ and $1.499784821\ldots$. The weighted signed exterior mean in (3) is $-0.160127106\ldots$, while its largest translated value is $0.678834494\ldots$. The 384-bit computation checks the exact telescope at every step, both sides of (3), and the single-fiber formula at every translate.

For this same cutoff $w_*=1/8$, the minimum original-exterior charge over **all** qualified quotient laws is in $[1.426093543,1.426093548]$. Averaging a law with its inverse preserves the floor and the objective on this even unerased path. The finite LP therefore uses the 13 allowed real nontrivial Fourier coefficients. The checker rounds a primal row found with tightened inequalities, certifies nonnegativity and the root floor, then checks rounded nonnegative dual multipliers with every coefficient residual charged against the unit Fourier cap. The comparison is at a fixed field and horizon. [Arb checker](astra-prefix-97-check.py) · [Replay](astra-prefix-97-checks.jsonl)

1. Estimate the minimum original-exterior charge (5) at the one full prefix over quotient rows with the prescribed root block floor. A single trial row below $o(J^2)$ suffices at each qualified block.
2. Bound the original restricted absolute prefix transforms by $o(J)$ on the filtered list. The translated secondary test needs only one positional fiber, linear signed means and a quadratic threshold; all of its translations use the same terminal prefix.
