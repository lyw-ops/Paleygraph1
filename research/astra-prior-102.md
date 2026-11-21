# Independent trials for the prior and the final signed increment

On the original bounded recurrent list, a law can price the genuine preceding exterior and a **different** law can price just the last actual increment. Both trials retain the shrinking root floor. The predecessor price can be signed, or it can be upper-bounded using the nonnegative prior with the entire original block removed. A cheap prior and small original triangular forcing force a positive order-$J^3$ terminal increment price for **every** eligible law. The head of this new signed test has relative size $O((\log J)^2/J^4)$.

## Splitting the exact triangle at its last nonzero step

Keep the prime, zero start, original candidate $C,L$, companion sign $\sigma$, actual recurrent masks, positive candidate-root filter, $m=|L|\asymp\sqrt n$, $|\lambda|\le\kappa_*<1$ and predetermined $J=\lfloor D(p)/8\rfloor$ of [round 98](astra-quotient-98.md). A trial is a nonnegative probability in the identity and companion Fourier sector of $G/L$, lifted uniformly on each block when paired on $G$. Its root $w$ is its mass on $L$. Put $T=J-2$, $h=2/[J(J-1)]$, $\rho=Jh$, and $\omega_j=h(J-1-j)$ for $0\le j\le T$. Write
\[
 a_j=\mathbb E_L |Y_j|,\quad c_j=\beta_j\sqrt n/m,\quad
 f_j=\sigma\mathbb E_L K(1_{L^c}|Y_j|),\qquad F=\sum_{j=0}^T\omega_j f_j .
\]
For a trial $q$, write $e_j(q)=\langle q,1_{L^c}|Y_j|\rangle$, $d_j(q)=\sigma\langle q,1_{L^c}Y_j\rangle$ in the physical lift convention. With roots $w=q(L)$ and $v=r(L)$ define
\[
 P(q)=\frac{\sum_{j=0}^T e_j(q)}{Jw},\qquad
 S(q)=\frac{\sum_{j=0}^T d_j(q)+d_T(q)}{Jw},\qquad
 I(r)=\frac{d_{T+1}(r)-d_T(r)}{v}.
\]
In particular $P$ is the [genuine preceding absolute history](prior-minority-101.md) *without* its root. The signed version $S$ counts its last predecessor twice. With independent trials at $w,v\ge A/J$, $A=8/c_0$ from the [original shrinking-root estimate](quotient-floor-99.md), recurrence forces
\[
 \begin{split}
 F+\rho S(q)+hI(r)&\ge c_0J-4/\min(w,v)-o(1),\\
 F+2\rho P(q)+hI(r)&\ge c_0J/2-o(1).                         \tag{1}
 \end{split}
\]
One may take the infimum of each price separately. At $q=r$ and before measurement erasures, $\rho S(q)+hI(q)=\rho\sum_{j<J}d_j(q)/(Jw)$ recovers the old signed flat price.

Indeed, the true one-step comparison is
\[
 f_j=(1-\sigma\lambda)(a_j+c_j)+(e_j(q)-d_{j+1}(q)-2g_j)/w .
\]
Use $q$ at $j<T$. The flat slope of the truncated weights is $h$ up to $T-1$, and the drop from $\omega_{T-1}=2h$ to zero gives **two** copies of $d_T$. Since $d_0=0$,
\[
 \sum_{j<T}\omega_j f_j+\rho S(q)
  =\sum_{j<T}\omega_j\big[(1-\sigma\lambda)(a_j+c_j)
                         +(e_j(q)-d_j(q)-2g_j)/w\big].
\]
At the last step the separate law $r$ gives exactly
\[
 f_T+I(r)=(1-\sigma\lambda)(a_T+c_T)
                       +(e_T(r)-d_T(r)-2g_T)/v.                   \tag{2}
\]
Multiply (2) by $h$ and add. All original source weights are restored, including the terminal one. Each $e_j-d_j$ and the marked contribution are nonnegative. The same $c_0$ applies because the full recurrent source is retained, and $2\sum\omega_jg_j\le4$. Finally $S(q)\le2P(q)$. This proves (1).

Independent permitted exterior erasures may be used in the triangle, each predecessor price and each endpoint measurement, keeping the original block denominator. The round-95 first-mass bound changes each $f_j$ by $O(\varepsilon_p)$ and each unnormalized $d_j,e_j$ by $O(\varepsilon_p)$, $\varepsilon_p=o(1)$. The corresponding errors in (1) are $O(\varepsilon_p[1+\rho/w+h/v])=o(1)$. The measurements leave the cold update unchanged.

## The required final increment and its measured head

If $F\le o(J)$ and one law has $P(q)=o(J^2)$, the second inequality in (1) gives $I(r)\ge(c_0/4-o(1))J^3$ for every eligible $r$. The same follows from a signed $S(q)\le o(J^2)$ by the first inequality. This tests both earlier expense mechanisms: a negative flat original-block mean and a large triangular wrong-sign occupation still have their [distinct consequences](prior-minority-101.md), but neither requires an upper on the original-block prior in (1).

The negative single-time forcing can be seen directly if $c_0$ is taken from the retained visits in the round-98 proof: they are bounded a fixed fraction of $J$ away from the endpoint, hence already give $(1-\sigma\lambda)\sum_{j<T}\omega_j a_j\ge c_0J$ eventually. The truncated identity then gives $F-hf_T+2\rho P(q)\ge c_0J-4/w-o(1)$. Under the small-$F$, cheap-prior hypotheses it forces $f_T\le-(c_0/4-o(1))J^3$. Equation (2) converts this kick to the positive terminal increment. The combined estimate (1) itself uses the full recurrent source.

To test $I$, let $u_R$ be the measured $\sigma$-signed mean of $Y_{T+1}-Y_T$ on each exterior block, and $u_0=0$. The true map applies $K$ after coordinatewise absolute value off the physical mark and $y\mapsto\sqrt{4n+y^2}$ there. Both scalar maps are 1-Lipschitz, and $K$ contracts counting $\ell^2$. The first increment has normalized second norm at most two; therefore $\|Y_{T+1}-Y_T\|_{2,n}\le 2$. All signed increments have global mean zero. With a common erasure of the two endpoint states, Jensen and the positive-part bound give
\[
 b^{-1}\sum_R u_R^2\le4,\qquad b^{-1}\sum_R(u_R)_+\le1,\qquad b=n/m .
\]
If endpoint erasures differ, the new block means differ from the unerased means by $O(\varepsilon_p)$ uniformly, since the removed first mass is $O(\sqrt n\,\varepsilon_p)$ and $m\asymp\sqrt n$. The respective bounds become $4+o(1)$ and $1+o(1)$.

Take $s=AJ^2/\log J$ and $H=\{R:u_R>s\}$. Then $|H|/b\le(4+o(1))/s^2$. If **one** eligible terminal law obeys $r_R\le d/b$ on $H$ with $d=o(J^2)$, then
\[
 I(r)\le [s(1-v)+(1+o(1))d]/v=o(J^3)
\]
as a one-sided upper. It may differ from the prior trial. The centered projection and cap dual of [round 101](astra-price-101.md) can be applied directly to this smaller measured head. This head estimate uses the authentic velocity of the nonlinear cold map. The round-101 prescribed hot interior activation cannot be substituted in the derivation of (1) or the nonexpansive velocity bound.

At $p=769$, $J=16$, $m=8$, $\sigma=+1$, the true signed increment head above $1/5$ is exactly $\{2,8,40,46\}$ under a common endpoint erasure at site 39. The order-six frequency subgroup gives an admissible law supported on the eight multiples of six; its root is $1/8$, it avoids the entire head, and its terminal increment price is in $[-0.358404986,-0.358404985]$. The distinct six-point clique law from round 98 has measured positive predecessor-exterior price in $[11.182873062,11.182873064]$. The measured full triangle lies in $[0.259599450,0.259599451]$ and the terminal forcing is positive at this prime. The [384-bit checker](astra-prior-102-check.py) verifies the truncated and endpoint identities on the physical cold orbit, with separate measurement rows. Its [replay](astra-prior-102-checks.jsonl) uses a fixed finite cutoff and makes no recurrence assumption here.

1. On actual filtered candidates with small measured $F$, test the exterior-only predecessor price (or its signed doubled-endpoint version) and independently price the terminal increment. A subcubic upper for one terminal law removes the endpoint alternative whenever the predecessor is cheap.
2. Where the endpoint head fails its cap test, measure the last signed exterior forcing and the true root, exterior wrong-sign and scalar contributions in (2). A large positive increment in one trial does not establish its lower bound for all trials. The genuine triangular upper, through-primes trial estimates, escaped branch and ordinary theta limit remain open.
