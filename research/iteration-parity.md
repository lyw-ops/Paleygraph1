# Inertia at 1 and fixed-depth smoothing

This gives a proof draft that $v^{(t)}_0\to0$ through primes $p\equiv1\pmod4$ for every fixed smoothing weight $\tau>0$ and every fixed number of Picard updates $t$. It uses the local multiplicative convolution formula at $1$. The estimate needed to let the iteration depth grow with $p$ remains open.

## Types of local inertia

Work on $\mathbb G_m/\mathbb F_p$ in Katz's pure weight-zero middle-convolution category. Let $T$ denote the quadratic twist by $\mathcal L_{\chi(1-a)}$ on $U=\mathbb G_m\setminus\{1\}$, followed by middle extension and the same shift. Keep the following two types of geometrically semisimple objects, allowing direct sums.

- The negative type consists of nonpunctual middle extensions, tame everywhere and lisse on $U$, with only the eigenvalue $-1$ on semisimplified geometric tame inertia at $1$.
- The positive type has a nonpunctual part of the same form with inertia eigenvalue $+1$ only, and may also have punctual summands at $1$.

Objects are considered over the finite field for traces and over its algebraic closure for types. Negligible Kummer objects are excluded as usual by the convolution category. The convolution dual of a negative object is negative, since it applies linear duality and multiplicative inversion, and both preserve this inertia eigenvalue. Twisting by $T$ converts the nonpunctual part of a positive object to a negative object. Its stalk at $1$ vanishes. Thus its trace function over the whole multiplicative group equals multiplication of the positive object's trace function by $s(a)=\chi(1-a)$, including $s(1)=0$ which kills the full punctual part.

Two negative factors have a positive middle convolution. Two positive factors also have a positive middle convolution. For the nonpunctual factors, Rojas-León's finite-point formula (Theorem 5.1) leaves only the contribution from the pair $(1,1)$ because both boundary monodromies are tame. Corollary 5.7 gives this contribution on vanishing cycles as the tensor product of the two tame vanishing-cycle representations. For a middle extension, vanishing cycles at $1$ are a quotient of the generic inertia representation by the invariant stalk. For the two types above the resulting eigenvalues are thus respectively $-1$ only or $+1$ only, whenever the quotient is nonzero. For either pair of equal types, its tensor product has only eigenvalue $+1$. The specialization exact sequence in Lemma 5.5 shows that the remaining contribution to generic inertia at $1$ has trivial action, coming from the special stalk. This yields unipotent inertia for the nonpunctual part of the middle convolution, which is a subquotient of compactly supported convolution. Corollaries 5.3 and 5.9 give lissity off $1$ and tameness. Applying the same lissity statement to the forget-supports image puts any punctual part at $1$. The punctual factors in the positive-positive case act as the convolution unit geometrically. [Rojas-León, Section 5](https://arxiv.org/pdf/1106.1398) · [Katz, Chapters 2 and 19](https://web.math.princeton.edu/~nmk/mellin331.pdf)

An even number of negative factors therefore has positive middle convolution by pairing the factors first. An odd number has no geometric $\delta_1$ summand. For one factor this is immediate. For more factors, write the product as one negative factor times the positive product of the others. A $\delta_1$ summand would give a morphism from the negative factor's convolution dual to the positive product. It is excluded by the lisse inertia eigenvalues and the absence of a punctual constituent of the negative factor. This uses the middle-convolution tensor category for the duality and ordinary lisse inertia to exclude the morphism. It allows non-self-dual factors.

Equivalently, the geometric convolution group of any fixed direct sum of negative objects contains the simultaneous scalar $-I$. The preceding vanishing applies also to mixed tensors of a direct sum and its dual, since the dual is negative. Scalar $-I$ fixes all invariant tensors of even total degree, and the odd invariant spaces vanish. Tannakian reconstruction identifies the group as the stabilizer of these tensors in the direct sum representation.

## Uniform fixed-expression trace estimates

Let $m_M(\psi)=\sum_{a\ne0}\psi(a)t_M(a)$ be the full Mellin trace of an object $M$, with $t_M$ its perverse trace function. Let

$$\mathcal A(M)(k)=\frac{m_M(\psi)+m_M(\psi\chi)}2,$$

where $\psi$ is a lift of $k\in\widehat Q$. The negative rank-one Kummer object $\mathcal L_{\chi(1-a)}(1/2)[1]$ gives $x=-\sqrt{p/n}\,\mathcal A(M)$ exactly with the Fourier convention in [the smoothing note](smoothing.md). The lift average is half the Mellin trace of $M\oplus(M\otimes\mathcal L_{\chi(a)})$. Twisting by $\chi(a)$ preserves both types, since it is unramified at $1$.

With any fixed expression, the ranks, convolution dimensions and completeness exceptions are bounded independently of $p$. For the rank bound at one convolution, the generic fiber is controlled by $H_c^1$ on $\mathbb G_m$ with at most two interior singularities. For lisse generic ranks $r_M,r_N$ and convolution dimensions $d_M,d_N$, tame Grothendieck–Ogg–Shafarevich gives $\dim H_c^1\le r_M d_N+r_N d_M+r_M r_N$. Here the first two terms bound the conductor at the two interior points and the last bounds $H_c^2$. Punctual contributions are bounded by their convolution dimensions times the other generic rank. The tensor-category dimensions multiply under convolution, and a Kummer twist keeps the generic rank with the new dimension bounded by the rank, by tameness and the single interior singularity. This bounds each step in a fixed expression. The finite set of bad Mellin characters for the input objects is bounded by their boundary ranks, and adding the other lifts at most doubles its size. [Katz, Chapters 4, 5 and 19](https://web.math.princeton.edu/~nmk/mellin331.pdf)

Outside these characters, multiplication of Mellin traces is middle convolution. At every character the trace is bounded by the convolution dimension using Katz Lemma 2.1 and the weights at most zero on the compactly supported cohomology in degree zero. Thus replacing a fixed product by its convolution trace incurs an error supported at $O(1)$ full characters, bounded there by $O(1)$. A fixed odd product of negative traces has normalized mean $O(p^{-1/2})$ by character orthogonality. The average of its convolution trace over every full character is the trace at $1$, where the $\delta_1$ multiplicity is zero and ordinary middle-extension stalks have weight at most $-1$. Bad characters contribute $O(p^{-1})$. The same estimate applies to an odd product of lifts averaged to $\widehat Q$ by expanding into the two Kummer twists before taking the mean.

For a fixed even polynomial $P$ in fields of the form $\mathcal A(M_i)$, replace each monomial by the average of the trace of its positive middle convolution, up to an error on $O(1)$ frequencies. A constant is represented by $\delta_1$. Fourier inversion of the lift average is the original trace function restricted to $Q$, with the factor $1/(2n)=1/(p-1)$. Consequently applying $K$ to the polynomial replaces each positive object by the twist of its nonpunctual part. The result is a finite linear combination of negative fields up to $O(p^{-1/2})$ in normalized $\ell_2$, since $\|K\|_{2\to2}\le1$. The same error bound holds pointwise for the exceptional-character correction by $\max_{j,k}|K_{j,k}|\le\sqrt p/n$. Coefficients may vary within a bounded set, since the estimates apply to each fixed monomial separately.

## Application to the Picard iterates

Set $\phi(y)=\sqrt{y^2+4\tau}$, let $W_0=0$, and use the bulk model

$$W_{t+1}=2x+K\phi(W_t).$$

For fixed $t$ and a chosen approximation accuracy, each $W_t$ can be approximated in normalized $\ell_2$ by a bounded linear combination of negative fields. Inductively start with the zero combination. Given a bounded approximation to $W_t$, approximate the even function $\phi$ on the bounded range of that approximation by a fixed even polynomial. The Lipschitz bound for $\phi$ and the $\ell_2$ bound for $K$ control the two approximation errors. The even polynomial rule gives the next approximation, whose pointwise bound is finite and uniform in $p$ for that choice of accuracy and depth. All odd moments of the approximating fields are $O(p^{-1/2})$ at fixed complexity. Apply this to the odd function $x\phi(W_t)$ by approximating $\phi$ once again on the bounded approximant and using boundedness of $x$. Taking $p\to\infty$ and then the approximation error to zero yields

$$\frac1n\sum_k x_k\phi(W_{t,k})\longrightarrow0\qquad\text{for every fixed }t.$$

For the actual iteration $v^{(t+1)}=K\Phi(v^{(t)})$ with $v^{(0)}=0$, put $V_t=\sqrt n\,v^{(t)}$ and $a_t=v^{(t)}_0$. The exact bulk recurrence, including the exceptional coordinate, is

$$V_{t+1}=b_t x+K\phi(V_t),\qquad b_t=\sqrt{4+a_t^2}-\sqrt{a_t^2+4\tau/n}.$$

In particular $a_{t+1}=n^{-1}\sum_k x_k\phi(V_{t,k})-b_t/n$. Induction using the empirical cancellation, Lipschitz continuity of $\phi$, and $\|K\|_{2\to2}\le1$ proves both $a_t=o(1)$ and $\|V_t-W_t\|_{2,n}=o(1)$ for fixed $t$.

The same arithmetic argument gives cancellation for the quadratic proxy $n^{-1}\sum x[K(2x+K T_2(\lambda/\sqrt p))^2]^2$, which is an odd polynomial after the inner even feedback is replaced by negative fields. It also gives cancellation of the differential of the fourth update. The derivative at $\alpha=0$ of $n^{-1}\langle x,\phi(2x+\alpha K\phi(W_2))\rangle$ equals $n^{-1}\langle K[x\phi'(2x)],\phi(W_2)\rangle$. The first factor comes from an even function of $x$ and the second is even in $W_2$. The full fourth update is included in the fixed-depth argument above. The [FFT probe](../data/fourth-step.csv) records these separate quantities at finite primes.

## The remaining analytic limit

The order of limits in the proof fixes the polynomial approximations and iteration depth before taking $p\to\infty$. Their pointwise bounds, ranks, and errors can depend on depth. One sufficient analytic estimate is

$$\limsup_{p\to\infty}\|v^*_{p,\tau}\|_2<\infty$$

for each fixed $\tau$ in a sequence tending to zero, where $v^*_{p,\tau}$ is the exact interior fixed point. To see this, use the averaged iteration $z^{(t+1)}=(z^{(t)}+K\Phi(z^{(t)}))/2$ starting at zero. The same fixed-depth argument applies, since all new terms are linear combinations of the existing iterate and the even feedback. Set $r_t=z^{(t)}-K\Phi(z^{(t)})$. Nonexpansiveness and the parallelogram identity give

$$\|z^{(t+1)}-v^*\|_2^2\le\|z^{(t)}-v^*\|_2^2-\tfrac14\|r_t\|_2^2.$$

The $\|r_t\|_2$ are nonincreasing because the averaged update is nonexpansive and $r_t=2(z^{(t)}-z^{(t+1)})$. Hence $\|r_t\|_2\le2\|v^*\|_2/\sqrt{t+1}$ and $\|z^{(t)}\|_2\le2\|v^*\|_2$. The deterministic residual certificate then gives a log-theta error at most $\frac12\log W+\sqrt5\|v^*\|_2(t+1)^{-1/4}$ around $\operatorname{arsinh}(z^{(t)}_0/2)$. First let $p\to\infty$ at fixed $t$, then $t\to\infty$ at fixed $\tau$, then $\tau\downarrow0$. This criterion would prove Conjecture 26. The elementary bound from the entries of $K$ gives $\|v^*\|_2=O_\tau(p^{1/4})$, leaving the needed uniform estimate open. [Chen et al., Proposition 4.3](https://arxiv.org/html/2610.22971v1#S4)

In the [floating-point norm probe](../data/smoothing-norms.csv), four primes from $10009$ through $1000033$ give $\ell_2$ norms between $2.27$ and $2.36$ for trial values $\tau=0.05,0.01$, with residuals at most $10^{-8}$ for the numerical iterates. These are measurements of the iterates at the sampled primes. If the residual is enclosed rigorously, a finite-prime distance certificate follows from the scalar secant formula. For a candidate $v$, let $A=2\sqrt{pW/n}$ and set

$$\eta=\frac{\min_i(\Phi_i(v_i)-|v_i|)}{A+\|v\|_\infty+4\sqrt{\max_i w_i}}.$$

Since $\|v^*\|_\infty\le A$, the identity for the difference of square roots gives $|\Phi_i(v_i)-\Phi_i(v_i^*)|\le(1-\eta)|v_i-v_i^*|$. Applying the nonexpansive $K$ and the triangle inequality shows $\|v-v^*\|_2\le\|v-K\Phi(v)\|_2/\eta$. The uniform-in-prime bound in the criterion remains a separate estimate.

### A criterion involving only the iterates

Let $D_t$ be the relative discrepancy of $z^{(t)}$ in Proposition 4.3 and $S_t=n^{-1/2}\sum_k\Phi(z^{(t)})_k$. Since $K^2=I-J$ and $\|\Phi(z)\|_2^2=\|z\|_2^2+4W$, the averaged update satisfies

$$\|z^{(t+1)}\|_2^2=\|z^{(t)}\|_2^2+2W-\tfrac12 S_t^2-\tfrac14\|r_t\|_2^2.$$

Summing from zero gives $T^{-1}\sum_{t<T} S_t^2\le4W$, hence $T^{-1}\sum_{t<T}S_t\le2\sqrt W$. The exact discrepancy identity (4.13) now telescopes using $r_t=2(z^{(t)}-z^{(t+1)})$:

$$0\le\frac1T\sum_{t<T}D_t\le\frac{\langle z^{(T)},v^*\rangle}{T}.$$

The entry bound from the smoothing note gives $|v^*_0|\le2\sqrt{pW/n}$ and $\|v^*\|_1\le2\sqrt{nW}$. Thus a different sufficient condition, using only averaged iterates, is

$$\lim_{T\to\infty}\frac1T\limsup_{p\to\infty}\sqrt n\max_{k\ne0}|z^{(T)}_k|=0$$

at fixed $\tau$ along a sequence tending to zero. At fixed $T$, the marked term of the pairing tends to zero. A discrepancy no greater than the average occurs at some $t<T$. All the finitely many marked coordinates $z^{(t)}_0$ tend to zero, so (4.15) yields the same limit after $T\to\infty$ and $\tau\downarrow0$. This criterion calls for a growth estimate on the extreme scaled bulk entries, and the fixed-depth moment proof does not give that estimate. [Chen et al., Proposition 4.3](https://arxiv.org/html/2610.22971v1#S4)

The [square-order control](square-order-control.md) gives an exact obstruction to deducing either criterion solely from these fixed-depth estimates and the deterministic identities. The same tame inertia argument applies over quadratic extensions, where the subfield clique forces a different asymptotic theta constant.

The [marked-response criterion](marked-response.md) replaces the full fixed-point norm estimate with a scalar identity for the derivative in the marked weight. It also checks the first three odd spectral moments of the corresponding linearization at fixed iteration depth.

The [one-sided comparison](signed-drift.md) applies the telescope separately to the positive spectra $A$ and $B$. This gives an upper-half and a lower-half test with explicit cost functions for the two Fourier LPs.

The [uniform fixed-depth draft](uniform-fixed-depth.md) strengthens the fixed-depth approximation to a sup bound with explicit control on the exceptional-character errors. Its constants may still grow with depth.

### Residual decay without an estimate on the fixed point

The averaged iteration from zero satisfies, at every field order,

$$\|r_t\|_2\le 2(1+\sqrt2)\sqrt W\,(t+1)^{-1/4}.$$

To see this, write $Tz=(z+K\Phi(z))/2$, $z_t=T^t0$, and $d_t=z_t-z_{t+1}=r_t/2$. Since $T$ is firmly nonexpansive, comparing the orbit with its shift by $s$ gives

$$\|z_{k+s+1}-z_{k+1}\|_2^2+\|d_{k+s}-d_k\|_2^2\le \|z_{k+s}-z_k\|_2^2.$$

Summing over $0\le k<N$ yields $\sum_{k<N}\|d_{k+s}-d_k\|_2^2\le\|z_s\|_2^2\le2Ws$, by the averaged norm identity. Average over $0\le s<L$ and pick $k<N$ with $L^{-1}\sum_{s<L}\|d_{k+s}-d_k\|_2^2\le W(L-1)/N$. The average of $d_{k+s}$ telescopes to $(z_k-z_{k+L})/L$, whose norm is at most $\|z_L\|_2/L\le\sqrt{2W/L}$ by nonexpansiveness of $T^k$. The step norms are nonincreasing, so

$$\|d_{N-1}\|_2\le\|d_k\|_2\le\sqrt{W(L-1)/N}+\sqrt{2W/L}.$$

Take $L=\lceil\sqrt N\rceil$. The residual thus tends to zero in the field-first limit even at square orders. Transferring the marked value still requires a bound on the stationary pairing $\langle r_t,v^*\rangle$, or a different estimate of the relative discrepancy. The [low-spectrum calculation](stationary-tails.md) gives restrictions on the stationary mass that can contribute to the marked response.

For example, at $\tau=0.05$ and depth $1024$ the measured averaged residual at $q=97^2$ is $2.05\times10^{-7}$ with marked coordinate $0.63503$. At $p=9413$ the corresponding residual is $1.04\times10^{-15}$ with marked coordinate $0.00081$.
