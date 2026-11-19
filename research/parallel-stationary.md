# A prime-field mass gap for one-sided stationary sets covered by cosets

The true stationary spectrum of either sign must leave a positive amount of mass on high coordinates outside every union of at most three frequency cosets of total size at most $(1-\kappa)\sqrt n$, at sufficiently small positive smoothing weight. This includes unions at the critical size $m_0=n/\sqrt p\sim\sqrt{n/2}$ when $0<\kappa<1-1/\sqrt2$. The number of exceptional exterior high coordinates must be of order at least $\sqrt n$. In particular, a critical stationary slow-band configuration whose one-sided high set is covered up to $o(\sqrt n)$ points by such a union is impossible through primes. The bound does not require the union size to agree with $m_0$ up to the error scale in [signed coset bands](signed-coset-bands.md).

## The prime-field mass gap

Let $Q=(\mathbb F_p^\times)^2$, $n=|Q|$, $s(x)=\chi(1-x)$, and let $\mu$ be a probability on $\widehat Q$ such that

$$f(x)=\sum_k\mu(k)k(x)=0\quad\text{if } x\ne1\text{ and }s(x)\ne\sigma,$$

where $\sigma=\pm1$. This is the inverse Fourier support condition on either positive spectrum, normalized to have mass one. Fix $0<\kappa<1$. Let $U$ be the union of $r\in\{1,2,3\}$ cosets of a common subgroup $G\le\widehat Q$, with $r|G|\le(1-\kappa)\sqrt n$. Uniformly for all sufficiently large primes, there is an $\varepsilon_\kappa>0$ such that

$$\mu(U)\le1-\varepsilon_\kappa. \tag{1}$$

To see this, write $B=G^\perp$, $b=|B|=n/|G|$, and $M=\mu(U)$. If $M>0$, the contribution from $U$ to $f(x)$ on $B$ is exactly $M\sum_{j=1}^r a_j\gamma_j(x)$, where $\gamma_j$ is the restriction of a representative of the $j$-th coset to $B$ and $a_j$ is that coset's fraction of $M$. Order the $a_j$ decreasingly. The exterior contribution has magnitude at most $1-M$ pointwise. For $r=1$ the normalized contribution from $U$ has magnitude one everywhere on $B$. This is the [single-coset majority argument](translation.md#a-prime-field-exclusion-for-subgroup-cosets); the fixed size slack permits applying it to either sign.

For $r=2,3$, set $L_r=(1-\kappa/2)2\pi/r$. Average arcs of length $L_r$ around the unit circle for the character $\gamma_1/\gamma_2$ on $B$. Some arc captures a set $T\subseteq B$ of size at least $bL_r/(2\pi)$. For $x=t/t'$ with $t,t'\in T$, the arguments of $\gamma_1(x)$ and $\gamma_2(x)$ differ by at most $L_r<\pi$ modulo $2\pi$. Projecting their weighted sum onto its angle bisector and bounding the other terms by their total weight gives

$$\left|\sum_j a_j\gamma_j(x)\right|
\ge (a_1+a_2)\cos(L_r/2)-(1-a_1-a_2)
\ge \delta_r,\qquad
\delta_r=\frac2r\cos(L_r/2)-\left(1-\frac2r\right)>0.$$

Take $T=B$ and $\delta_1=1$ in the one-coset case. If $M>1/(1+\delta_r)$, the exterior cannot cancel the contribution from $U$ at any ratio $t/t'$. Thus $\chi(t'-t)=\sigma$ for all distinct $t,t'\in T$, since $t'\in Q$. If $\sigma=-1$, multiply $T$ by a fixed nonsquare. In either case this produces a Paley clique of size $|T|$. The [Hanson–Petridis prime-field bound, Corollary 1.5](https://arxiv.org/pdf/1905.09134) gives $|T|(|T|-1)\le n$. But for $r=2,3$,

$$|T|\ge bL_r/(2\pi)\ge\frac{1-\kappa/2}{1-\kappa}\sqrt n,$$

and for $r=1$, $b\ge\sqrt n/(1-\kappa)$. Each contradicts the clique bound for sufficiently large $p$. This proves (1) with $\varepsilon_\kappa=\min_{1\le r\le3}\delta_r/(1+\delta_r)$. The use of the two heaviest cosets avoids an assumption on the orders of the quotient characters or on the relative coset masses. For four equal masses, two heavy cosets alone cannot give a uniform positive lower bound on the full sum by this argument.

## Transfer to the actual stationary diagonal

Use $v=K u$, $u_i=\sqrt{v_i^2+4w_i}$, $D_i=v_i/u_i$, $w_0=1$, $w_i=\tau/n$ for $i\ne0$, and $W=1+(1-1/n)\tau$. Set $A_\sigma=(u+\sigma v)/2$ and $\mu_\sigma=A_\sigma/\sqrt{nW}$. The exact identities give

$$A_{+,i}A_{-,i}=w_i,\qquad (I-\sigma K)A_\sigma=\sqrt{W/n}\,{\bf1}.$$

In particular $\mu_\sigma$ meets the support condition in (1). Also $\|A_\sigma\|_\infty\le \sqrt{W/n}(1+\sqrt p)$ by the Jacobi entry bound and positivity. For $0\le\rho<1$ let $S_\sigma=\{i:\sigma D_i>\rho\}$. The reciprocal product identity gives the pointwise estimate

$$A_{\sigma,i}^2=w_i\frac{1+\sigma D_i}{1-\sigma D_i}
\le w_i\frac{1+\rho}{1-\rho}\quad(i\notin S_\sigma).$$

Consequently, at every $U$ in (1),

$$\mu_\sigma(S_\sigma\setminus U)
\ge \varepsilon_\kappa-\sqrt{\frac{\tau(1+\rho)}{W(1-\rho)}}-\frac{1+\sqrt p}{n}. \tag{2}$$

The last summand allows the marked point outside $U$ and outside $S_\sigma$. Choose, for example, $0<\tau\le \tau_0=\min\{1,\varepsilon_\kappa^2(1-\rho)/(16(1+\rho))\}$. Then the right side is at least $\varepsilon_\kappa/2$ for all sufficiently large $p$. By the point cap on $\mu_\sigma$ this requires $|S_\sigma\setminus U|\ge (\varepsilon_\kappa/2)n/(1+\sqrt p)$. The opposite diagonal is unrestricted. One may also take $\rho=1-C\tau$ as $\tau\downarrow0$ with $C$ sufficiently large in terms of $\kappa$ (and $C\tau\le1$), to test coordinates of that sign whose activation approaches one. Both (1) and (2) are deterministic; the fixed-depth cancellation is not used.

This rules out a narrow band on the sign $\sigma$ **when the proposed geometry describes its whole one-sided high set up to $o(\sqrt n)$ exceptions**, whether or not the band couples to the mark. A near-mode in a prescribed compression may persist even when (2) holds. Compared with the stationary leakage bound in [signed coset bands](signed-coset-bands.md#a-stationary-mass-test-without-an-eigenvalue-hypothesis), (2) forces positive normalized exterior mass for up to three cosets at small smoothing weight and needs no estimate on the coset-sum deficit.

### A consequence for near-critical sets with high additive energy

Fix $\rho$ and $0<\kappa<1-1/\sqrt2$, and allow $0<\tau\le\tau_0$ as above. Suppose a sequence of the actual one-sided high sets satisfies $|S_\sigma|\le(1+o(1))m_0$. Then

$$|S_\sigma|\sim m_0,\qquad E(S_\sigma)\le(5/8+o(1))|S_\sigma|^3. \tag{3}$$

For the first assertion, (2) or its global non-high mass estimate gives $\mu_\sigma(S_\sigma)\gg1$. Thus $\|\mathbf1_{S_\sigma} A_\sigma\|_2^2\gg m_0$ by Cauchy–Schwarz. With $z=\mathbf1_{S_\sigma^c}A_\sigma$, one has $\|z\|_2^2\le W(1+\rho)/(1-\rho)=O_\rho(1)$ by the product identity. Expand the nonnegative form $I-\sigma K$ on $A_\sigma-z$, using $(I-\sigma K)A_\sigma=\sqrt{W/n}\,{\bf1}$:

$$\big(1-\lambda_{\max}(\sigma K_{S_\sigma S_\sigma})\big)\|\mathbf1_{S_\sigma}A_\sigma\|_2^2
\le W-2\sqrt{W/n}\sum_i z_i+\langle z,(I-\sigma K)z\rangle=O_\rho(1).$$

The entry bound gives $\lambda_{\max}(\sigma K_{S_\sigma S_\sigma})\le |S_\sigma|/m_0$, proving $|S_\sigma|\sim m_0$ and a compression gap at most $O_\rho(1/m_0)$, without assuming an eigenvalue of $H$.

For the second assertion, let $S=S_\sigma$ and $m=|S|$. Use the [translation rounding estimate](signed-coset-bands.md#turning-overlap-into-a-coset-cover-at-the-required-precision) with $a=(|m-m_0|+1)/m_0+1-\lambda_{\max}(\sigma K_{SS})=o(1)$. The estimate before the prime coset argument works for any such $a=o(1)$: for fixed $1/2<c<1$, the shifts of overlap more than $cm$ form a subgroup $G$, rounding changes $O_c(ma)=o(m)$ points, and $E(S)/m^3\le c+(1-c)|G|/m$. If $E(S)/m^3\ge5/8+\alpha$ for any fixed $\alpha>0$ on a subsequence, choose $c>1/2$ close enough to $1/2$ that $(5/8+\alpha-c)/(1-c)>1/4$. This gives $|G|/m$ bounded above $1/4$, so the rounded cover of size $m+o(m)$ uses at most three cosets. Its size is at most $(1-\kappa)\sqrt n$ eventually, and only $o(\sqrt n)$ points of $S$ lie outside it, contradicting (2). This proves (3). The $5/8$ bound is weaker than the $1/2+o(1)$ bound of the signed coset argument with $m\le m_0+o(\Delta_p)$, but here $m/m_0\to1$ suffices with no leeway required at the scale $\Delta_p$.

## Exact square-order checks

At $q=\ell^2$, let $B=\mathbb F_\ell^\times\le Q$ and $G=B^\perp$. The probability $\mathbf1_G/|G|$ is feasible on the plus support: its inverse Fourier transform is $\mathbf1_B$, and $s=+1$ on $B\setminus\{1\}$. It has full mass on a single coset with $|G|/\sqrt n\to1/\sqrt2$. The group $B$ itself is a clique of size $\ell-1$, so the specific use of the prime clique bound fails. The [exact square theta value](square-order-control.md) is $\vartheta(\overline H_{\ell^2})=\ell-1$. In particular the nonzero stationary mark at fixed $0<\tau<1$ is forced by the theta bracket, even though fixed-depth cancellation applies in this family.

For an exact example with the actual uniform bulk weights, take $q=25$ and $n=12$. Use the generator $1+2t$ of $\mathbb F_{25}^{\times}$ with $t^2=2$ over $\mathbb F_5$. In cyclic order of its squared powers, the sign and Fourier eigenvalue vectors are

$$s=(0,-1,1,1,-1,-1,1,-1,-1,1,1,-1),\qquad
\lambda=(-1,1,-3,-5,5,1,3,1,5,-5,-3,1).$$

The first follows by taking the character of the norm of each $1-x$; the second follows by the order-$12$ cosine transform. Here $G=\{0,4,8\}$. The exact minus witness $L_-$ of mean one from the square theta certificate satisfies $L_-(0)=3$, $L_-(4)=L_-(8)=0$, and $L_-(i)=(5-\lambda_i)/6\ge1/3$ outside $G$. Complementary supports give $\sum_i\mu_+(i)L_-(i)=1$. The theta bracket gives $\mu_+(0)\ge 4/(12W)$, so

$$\mu_+(G^c)\le3\big(1-3\mu_+(0)\big)\le3(W-1)/W.$$

At $\tau=1/20$ this gives $\mu_+(G)\ge218/251>1/2$ for the exact stationary solution. For fixed $q=25$ and $\tau\downarrow0$, it gives $A_{+,i}=O(\tau)$ off $G$, and the product relation implies $D_i\to-1$ there. To check the plus shell, the normalized plus witness $4\mathbf1_G$ gives $\sum_{i\in G}A_{-,i}=\sqrt{12W}/4$. Since the normalized stationary plus mark is bounded by its theta optimum $4$, $A_{-,0}=1/A_{+,0}\ge\sqrt{12/W}/4$. Therefore $A_{-,i}=O(\tau)$ and $D_i\to+1$ for $i\in G\setminus\{0\}$. In particular for any fixed threshold $0\le\rho<1$ and sufficiently small $\tau$, the true plus high set lies entirely in $G$. This check uses neither a prescribed diagonal nor a floating-point stationary solve. It does not assert that $G$ is the entire plus-optimal support at every growing square order.

## Remaining gap for the marked limit

An arbitrary strongly marked band at width $O(p^{-1/2})$ only forces stationary tail mass by [the source identity](stationary-tails.md#a-strongly-coupled-narrow-band-forces-stationary-mass). It does not imply an approximate three-coset cover of the one-sided high set, or that the exterior mass required by (2) couples to that band. At the smallest support size (3) still allows intermediate energy; it gives no exclusion for substantially larger high sets. To use this route for the limit, one needs a bound on marked spectral mass allowing the exterior same-sign tail, or an arithmetic argument that forces any strongly coupled configuration to violate (2). Controlling the retained signed response in the [resolvent criterion](resolvent-sum-rule.md#using-the-signed-stationary-spectrum) remains separate.

At the critical size the [finite-phase follow-up](critical-coset-phases.md) extends the exterior mass bound to seven cosets for general feasible spectra and ten for the even stationary spectra. It improves the stationary energy bound to $6/11+o(1)$ and gives a compression gap when the relative order of any coset displacement tends to infinity. The [response comparison](coset-activation.md) identifies the cross terms needed to control coupling between a cover and its exterior.
