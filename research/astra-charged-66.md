# One later signed mean controls the earlier whole-pair cost

Let $D=D(p)$ be the [marked prime window](vanishing-floor-38.md) and $L=\lceil D/2\rceil$. There is an exact simplification of the asymptotic full-face test on its original integer window. If the minimum charged cost divided by time has nonpositive limsup at some choice of time in $[L,D]$ through primes, it does so at **the predetermined time $L$**. If the good time is later than $L$, two independent signed-mean minimizers give a single feasible pair there. The same pair works at all earlier times proportional to the good time. The implication uses the exact cold increment and the terminal energy.

A single constant survival price at $L$ also gives an obstruction test. A positive lower margin $\eta L$ for that price on unbounded primes implies a margin of at least $(\eta/3-o(1))t$ for the full optimum at every $t\in[L,D]$. The estimates below do not determine which regime occurs through primes.

## Two independent whole marginal solves

Use the [full true faces](astra-tail-53.md) $F_s$ for $s=+1,-1$, including the optimal root $\gamma_s/\sqrt n$, nonnegativity, mass, exposed support and all forbidden Fourier equations. Let $\alpha=\max_s\gamma_s\ge1$, $\beta=1/\alpha$, and label the two sides by their actual marks when convenient. For the undamped zero-floor trajectory put
\[
 Y_j=\sqrt n v_j,\quad E_j=\|v_j\|^2,\quad
 b_j=\sqrt{4+v_j(0)^2}-|v_j(0)|,\quad
 g_j=\frac1{2\sqrt n}\sum_i (|v_j(i)|+b_j\mathbf1_{i=0}).
\]
Write
\[
 m_{s,j}(q_s)=\mathbb E_{q_s}sY_j,\quad
 a_{s,j}(q_s)=\mathbb E_{q_s}|Y_j|,\quad
 J_j(q)=\int_0^1\max_s Q_{s,j}(u)\,du-E_j/4,
\]
where $Q_{s,j}$ is the increasing quantile of $sY_j$ under the *whole* $q_s$. Set $J_j^*=\min_q J_j(q)$ and
\[
 k_j=\max_s\min_{q_s\in F_s} m_{s,j}(q_s)-E_j/4 \ \le J_j^*.
 \tag{1}
\]
In the [paired survival dual](astra-charged-65.md), the optimum over profiles constant in score is exactly $k_j$. A constant share $\lambda$ prices a convex combination of the two marginal means, and the marginal minima separate. An endpoint share 0 or 1 attains the maximum. Choose a minimizer $q_s^t$ of each mean at the same time $t$. No genericity or tie breaking is required.

Define
\[
 A_j=\sum_{i<j}(1-g_i)^2,\quad B_j=\sum_{i<j}(2-b_i),\quad
 H_{s,j}(q_s)=\sum_{i<j}\mathbb E_{q_s}(|Y_i|-sY_i).
\]
The sums start at 0. These three quantities are nondecreasing. The [signed reserve](astra-critical-44.md), its one-step increment before summing, and the cold energy telescope give respectively
\[
 \begin{split}
 m_{s,j}-E_j/4&=2j(\gamma_s-1)-\gamma_s B_j+A_j+H_{s,j},\\
 a_{s,j}&=m_{s,j+1}-\gamma_s b_j+2g_j,\\
 (E_{j+1}-E_j)/4&=1-g_j^2,\qquad
 E_j/4=2\sum_{i<j}(1-g_i)-A_j .
 \end{split} \tag{2}
\]
Indeed $q_s$ is in the prescribed Fourier sector, so $sKq_s=q_s-\mathbf1/n$. Pairing with $|v_j|+b_j e_0$ gives the second identity. Sum it and use the energy telescope for the first one. In the marked window $B_D=o(1)$, and the pointwise Jacobi bound controls $\alpha$ uniformly.

Set $T_t=k_t+\alpha B_t$. On the larger minimizer the first identity gives
\[
 T_t\ge 2t(\alpha-1)+A_t+H_{\mathrm{large},t}(q^t_{\mathrm{large}})\ge0.
 \tag{3}
\]
For each $j\le t$, subtract (2) at $t$ and $j$, retaining the same terminal minimizer on each side. Monotonicity gives
\[
 m_{s,j}(q_s^t)-E_j/4
 \le T_t+2(t-j)(1-\gamma_s)_+
 \le \begin{cases}
 T_t & (\gamma_s=\alpha),\\
 (2-j/t)T_t & (\gamma_s=\beta).
 \end{cases} \tag{4}
\]
Here $2t(1-\beta)\le 2t(\alpha-1)\le T_t$. In particular the estimate controls both marginals without any assumption on endpoint collision or on the size of the exposed face. Also, for $j\le t$,
\[
 E_j/4\le 2\sqrt{jA_j}-A_j\le2\sqrt{jT_t}.
 \tag{5}
\]

## The earlier primal pair and the one-time barrier

For $0\le r<t$, the elementary inequality $\max(x,y)\le |x|+|y|$ on the actual common quantile coupling and (2) give
\[
 J_r(q^t)
 \le \sum_s m_{s,r+1}(q_s^t)-E_{r+1}/4
       +1-g_r^2+4g_r-b_r(\alpha+\beta).
\]
The last scalar correction is at most 5 since $g_r\ge0$, $b_r\ge0$. Inserting (4) with $j=r+1$ gives the finite bound
\[
 \boxed{\displaystyle
 J_r^*\le J_r(q^t)
 \le (3-(r+1)/t)T_t+2\sqrt{(r+1)T_t}+5 .}
 \tag{6}
\]
At the immediate predecessor one can replace the first term by $2k_t$, and replace the square-root term by $E_t/4$. In particular, if $T_t/t\le1$, its latter contribution per step is at most $2\sqrt{T_t/t}-T_t/t$, by (5)'s first inequality and monotonicity of $2\sqrt x-x$ on $[0,1]$. Thus a small normalized **lower** price at $t$ supplies a genuine small charged **upper** certificate one step earlier. Its rate is at most $T_t/t+2\sqrt{T_t/t}+5/t$ there, using divisor $t$. A positive margin $\eta$ for $J_{t-1}^*/t$ forces $\liminf T_t/t\ge(\sqrt{1+\eta}-1)^2$ along a growing sequence, for $0<\eta\le3$, by taking subsequences in the preceding rate bound.

The endpoint conventions in the following consequences matter.

* For any $L\le t\le D$, $k_t,J_t^*\ge-\alpha B_D$. If $\limsup_p\min_{L\le t\le D}J_t^*/t\le0$, choose a minimizing $t$ for each prime. When $t=L$, the same-time full minimizer already works there. When $t>L$, (1) makes $T_t=o(t)$, and (6) gives $J_L(q^t)=o(L)$ in the upper sense because $t/L\le2$. Conversely $L$ is an admissible time. Thus the full window test is **equivalent to $J_L^*/L\to0$** without changing either endpoint. This does not assert that signed means priced only at $L$ resolve $J_L^*$.
* If the only input is $k_t/t\to0$ at some $L\le t\le D$, the constructed pair has upper cost $o(r)$ simultaneously at every $r<t$ with $r/t$ bounded below. In particular $r=L-1$ always works, and $r=L$ works whenever $t\ge L+1$. The single test $k_{L+1}/(L+1)\to0$ suffices in the original window. If the signed-price hit occurs only at $t=L$, the proved target time is $L-1$. This still proves the ordinary-theta limit by (2)–(3) since the time grows. No assertion about $L+1$ follows from that boundary hit.
* Taking a further marginal minimum in (4) gives $k_u\le(2-u/t)T_t$ for $u\le t$. Hence for $L\le t\le D$,
\[
      J_t^*/t\ \ge k_t/t\ \ge \frac{k_L}{2t-L}-\frac{\alpha B_t}{t}.
 \tag{7}
\]
If $k_L/L\ge\eta>0$ on an unbounded prime subsequence, the right side is at least $\eta/3-o(1)$ uniformly, since $D\le2L$. A certified dual bound on one sign's linear objective at one time suffices for this obstruction. The converse obtained from a full-window margin locates the constant-price certificate at $L+1$, using the immediate-predecessor estimate.

## A modification of the chord trial with a uniform guarantee

At the target time $r$ take the original [range-chord sharing fractions](astra-charged-65.md), or any common survival profile $0\le\lambda\le1$. Extend it to the interval containing zero and the scores, taking any allowed slope on a new part, and define the two scalar price functions by $f_+(0)=f_-(0)=0$, $f'_+=\lambda$, $f'_-=1-\lambda$. They sum to the identity. On **each** true face minimize the linear cost
\[
          c_s(i)= f_s(sY_r(i))+|Y_r(i)|.
\]
Call the independent whole minimizers $b_s$. The additional linear price can equally be implemented by $sY_{r+1}$, by (2) and its face-constant offset. For all real $z$,
\[
                  z_+\le f_s(z)+|z|\le2|z|.
\]
Consequently, for every reference pair $q$,
\[
 J_r(b)\le \sum_s\min_{F_s}\mathbb E c_s-E_r/4
       \le 2\sum_s a_{s,r}(q_s)-E_r/4. \tag{8}
\]
With $q=q^t$, (2), (4), and (5) give an $o(r)$ upper cost whenever $T_t=o(t)$, $r<t$ and $r/t$ is bounded below: (4)–(5) give $m_{s,r+1}=o(t)$ from above, and $g_r\le\sqrt{r+1}$ from the energy increment and $E_r\le4r$. Thus the modified chord trial itself works at $L$ if a signed-price hit occurs in $[L+1,D]$, uniformly over the original chord ambiguity and all ties. The unmodified chord minimizers have no such bound here. A simpler additive upper price minimizes $(sY_r)_+$ on each face. Its objective before minimization equals $(m_{s,r}+m_{s,r+1}-\gamma_s b_r+2g_r)/2$, with both signed means under the same row.

## What remains on the two genuine endpoint faces

Exactly,
\[
 k_t=A_t+\max_s\left[2t(\gamma_s-1)-\gamma_s B_t+
                        \min_{q_s\in F_s}H_{s,t}(q_s)\right].
\]
Thus a signed-mean minimizer is also a minimizer of the entire wrong-sign occupation on its own sign. An $o(t)$ upper bound just for the larger side's charged mean already implies $\alpha\to1$, independently of the second side. To obtain the whole-pair conclusion by (6), the remaining smaller-side input can be stated as a single signed pairing. Write $P_s=(I-J+sK)/2$, $j=\mathbf1/\sqrt n$ with $J$ the constant-vector projector, and decompose $x=\sqrt n q_s=j+cP_s e_0+R$ with $c=(\gamma_s-1/\sqrt n)/(P_s)_{00}=O(1)$. The residual lies in the sign sector and vanishes at the mark. Then
\[
 m_{s,t}(q_s)=\frac c2\big[s v_t(0)+(Kv_t)(0)\big]+
                    \langle R,sP_s v_t\rangle .
\]
Here $(Kv_t)(0)=\sqrt{4+v_{t-1}(0)^2}-2g_{t-1}/\sqrt n=2+o(1)$ uniformly in the marked window for $t\ge1$. An upper $o(t)$ estimate on this signed residual pairing for any one actual smaller row suffices after the larger-side estimate. Neither a small residual norm nor a two-sided correlation estimate is required. No all-prime estimate of either marginal minimum is obtained.

There is an exact-family control for which the winning constant price can be identified throughout the full arithmetic window. At $q=h^2$, $h$ an odd prime, the [known complementary optima](square-endpoint-uniqueness.md) give $\alpha=(h-1)/\sqrt n\to\sqrt2$, and the feasible smaller minus row is $x=j+\alpha P_- e_0$. Its signed mean is $\alpha[(Kv_t)(0)-v_t(0)]/2=\alpha+o(1)$ uniformly for $1\le t\le D(q)$. The larger plus minimum is at least $2t(\alpha-1)+E_t/4-o(1)$ by (2), uniformly. For all $t\ge2$ this exceeds the displayed smaller-row mean eventually since $4(\sqrt2-1)>\sqrt2$. At $t=1$ the larger mean is exactly $2(\alpha-1/\sqrt n)$ by the sector identity. Therefore at **every** $1\le t\le D(q)$ for all sufficiently large prime squares, the best constant price selects only the larger sign, and the normalized late $k_t/t$ is at least $2(\sqrt2-1)-o(1)$. This comparison uses a feasible smaller row and covers its entire face in the required direction. The squares give an exact family outside the prime target.

1. At the single prime time $L+1$, upper-bound the two signed marginal minima after charging, or equivalently the two occupation LPs with the displayed offsets. A nonpositive normalized limsup passes and supplies whole pairs at $L$, including the modified chord pair. A positive lower margin at $L+1$ on a prime subsequence rejects this sufficient test.
2. For a full-window lower obstruction, certify $k_L\ge\eta L$ on unbounded eligible primes using one sign and its full Fourier face. This rejects the full one-time charged upper estimate on that subsequence by (7). An $o(L)$ upper certificate for both marginal minima after charging excludes this particular lower obstruction and gives a genuine whole-pair upper test at $L-1$.
