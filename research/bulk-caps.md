# Capped Fourier mass and stationary high sets

Use the [stationary smoothing notation](smoothing.md). Let $q$ be the field order, $n=(q-1)/2$, $u=\Phi(v)$, and $D=v/u$ for the exact stationary field $v=Ku$. Write $A=(u+v)/2$, $B=(u-v)/2$, and $W=1+\tau(1-1/n)$. Off the mark, the scaled spectra $a_i=\sqrt n A_i$ and $b_i=\sqrt n B_i$ satisfy

$$a_i b_i=\tau,\qquad a_i=\sqrt\tau\sqrt{\frac{1+D_i}{1-D_i}},\qquad b_i=\sqrt\tau\sqrt{\frac{1-D_i}{1+D_i}}.$$

For a fixed cap $L>\sqrt\tau$, define $C_L$ off the mark by $C_{L,i}=\min(a_i,L)+\min(b_i,L)$ and set $C_{L,0}=0$. Write

$$\kappa_L=\frac{\|K C_L\|_\infty}{\sqrt n},\quad I_L=\frac1n\sum_{i\ne0}\big(\min(a_i,L)-\min(b_i,L)\big),\quad \delta_L^+=\frac1n\sum_{i\ne0}(a_i-L)_+,\quad \delta_L^-=\frac1n\sum_{i\ne0}(b_i-L)_+.$$

The relevant arithmetic tests are the supremum $\kappa_L$ and the signed scalar $I_L$. Both go to zero at fixed iteration depth with the field size. At stationarity, these tests turn the comparison into conditions on positive tail mass and its location.

## Two bounds for the exact stationary solution

Put $b_q=\sqrt{q/n}$ and $E_L=\kappa_L+b_q u_0/\sqrt n$. With the two bulk high sets $S_L^+=\{i\ne0:a_i>L\}$ and $S_L^-=\{i\ne0:b_i>L\}$, one has

$$\begin{aligned}
(\|v\|_\infty-E_L)_+&\le b_q(\delta_L^++\delta_L^-),\\
\delta_L^+-\delta_L^-&=-I_L-v_0/\sqrt n,\\
\delta_L^+\delta_L^-&\le W\,\frac{|S_L^+-S_L^-|}{n}.
\end{aligned}$$

The first bound expands $u$ into its marked entry, the capped bulk part, and the excess above the caps. Each entry of $K$ is bounded by $b_q/\sqrt n$. The second follows from $\sum_i v_i=0$. For the third, normalize $A,B$ by $\sqrt{nW}$ so both are probabilities. Their [cross-correlation is uniform](translation.md#mass-and-energy-outside-a-coset). Their mass on the two high sets is at least $\delta_L^+/\sqrt W$ and $\delta_L^-/\sqrt W$, respectively. Summing the uniform cross-correlation on the difference set gives the bound. In particular,

$$\|v\|_\infty\le E_L+b_q\sqrt{(I_L+v_0/\sqrt n)^2+4W\,|S_L^+-S_L^-|/n}.$$

These bounds also hold with $|v_0|$ in place of $\|v\|_\infty$ and $|(KC_L)_0|/\sqrt n$ in place of $\kappa_L$. The theta bracket in [the smoothing note](smoothing.md) gives $\big|\log(\vartheta(\overline H)/\sqrt n)\big|\le\operatorname{arsinh}(|v_0|/2)+\tfrac12\log W$.

For example, suppose the two cap tests go to zero at fixed $\tau$ and $L$ along a prime subsequence on which $\|v\|_\infty\ge\epsilon>0$. The tails each have mass at least $\epsilon/(2\sqrt2)-o(1)$ in the scaled units above, and the difference set has limiting lower density at least $\epsilon^2/[8(1+\tau)]$. If the two high sets lie in a common set with difference set of size $o(n)$, this rules out the subsequence. A union of a bounded number of cosets of the same subgroup of size $o(n)$ is one example of such a cover. The same conclusion follows if just one of the two tails has mass $o(1)$ at the chosen cap, because $I_L=o(1)$ and the total spectra have equal mass. With $L\to\infty$ after $q\to\infty$, uniform integrability of only one bulk spectrum suffices under the two cap tests. Uniform integrability of the total bulk spectrum needs only the $\kappa_L$ test.

## Fixed-depth cancellation and transfer

Let $V_j=\sqrt n v^{(j)}$ for the iteration from zero. At each fixed depth, the [inertia argument](iteration-parity.md) approximates $V_j$ in normalized $\ell_2$ by bounded linear combinations of negative Mellin fields, to arbitrarily small error in the field-first limit. The cap sum

$$g_L(y)=\min\big((\sqrt{y^2+4\tau}+y)/2,L\big)+\min\big((\sqrt{y^2+4\tau}-y)/2,L\big)$$

is a bounded Lipschitz even function of $y$. The cap difference is a bounded Lipschitz odd function of $y$. Approximate each function on the bounded range of a fixed negative-field approximation by a polynomial of the same parity. The odd mean estimate gives $I_L^{(j)}=o(1)$. For the even polynomial, applying $K$ gives a bounded linear combination of negative fields plus an error going to zero in normalized $\ell_2$. In general, an error of $\epsilon$ in that norm produces at most $\epsilon$ in sup norm divided by $\sqrt n$. This proves $\kappa_L^{(j)}=o(1)$, uniformly over all frequency rows of $K$. In these arguments we remove the marked entry from the cap fields at a cost of $O(L/\sqrt n)$ or smaller.

Each cap as a function of $D$ extends continuously to $[-1,1]$. The endpoint values for the plus cap are $0$ and $L$, and the minus cap reverses them. Thus a sufficient transfer estimate is

$$\lim_{j\to\infty}\limsup_{q\to\infty}\frac1n\sum_{i\ne0}|D_i-D_i^{(j)}|=0.$$

Uniform continuity transfers the caps in normalized $\ell_1$. For $I_L$ the error is at most the normalized $\ell_1$ cap-difference error. For $\kappa_L$ the entry bound on $K$ gives at most $b_q$ times the normalized $\ell_1$ cap-sum error. One can also prove the two stationary cap tests directly. They concern only bounded functions of $D$, while the tail estimates concern all the remaining mass. At a sequence of fixed weights $\tau\downarrow0$, this gives another sufficient criterion for the conjecture without requiring a bound on $\|v\|_2$. The stationary cap tests and the requisite tail control through all primes remain open.

The [weight-path identity](bulk-logarithm.md#what-fixed-depth-parity-needs-to-transfer) gives another use of the signed cap test alone. If its cancellation holds over the weight range, it controls the bulk logarithmic mean and thereby theta through integration in the smoothing weight.

## Numerical comparison

The [probe](../bulk_caps.py) compares both tests and the tail bounds on Fourier iterates from zero and at the numerical stationary solution. The CSV records the fixed-point residual alongside each row. The difference-set density is computed by rounding the FFT correlation of the two high-set indicators at $1/2$.

The [192 recorded rows](../data/bulk-caps.csv) cover eight orders, two weights, two fixed depths and the numerical stationary solution at each weight, with four caps for each iterate. All stationary residuals are below $10^{-10}$. At $\tau=0.05$ and $L=8$ the stationary comparison is

| Field order | $\lvert v_0\rvert$ | $\kappa_8$ | $I_8$ | $\delta_8^+$ | $\delta_8^-$ |
| ---: | ---: | ---: | ---: | ---: | ---: |
| $9413$ | $0.000811$ | $0.06319$ | $-0.0000118$ | $0$ | $0$ |
| $151337$ | $0.001977$ | $0.01672$ | $0.00000719$ | $0$ | $0$ |
| $1000033$ | $0.001659$ | $0.00731$ | $-0.00000235$ | $0$ | $0$ |
| $97^2$ | $0.63503$ | $0.53690$ | $-0.83821$ | $0.82895$ | $0$ |
| $389^2$ | $0.65044$ | $0.62579$ | $-0.90481$ | $0.90245$ | $0$ |

At $389^2$, the depth-32 iterate has capped imbalance $-0.04966$ and plus tail mass $0.04957$. The stationary values show that the difference-set estimate alone cannot exclude the square obstruction. The minus tail is zero and the stationary cap tests are large. At $1000033$, lowering the cap to $L=4$ leaves excesses $0.01799$ and $0.01795$ with difference-set density $1$. There the tail-mass estimate is stronger than the difference-set estimate. The two weights give the same qualitative comparison at cap $8$. These are floating-point diagnostics on the listed orders.
