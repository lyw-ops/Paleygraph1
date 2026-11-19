# Fourier repairs with point and coset mass bounds

Use the [signed iterate LP](signed-drift.md#a-linear-program-test-independent-of-the-stationary-solve) for sign $\sigma$. Write its probability spectrum as $\mu=P/n$, where $P\in U_\sigma$ has mean one and is nonnegative. The [point repair](iterate-majorants.md) uses only $\mu_i\le1/h$, where $h$ is the marked value of the basic opposite-support witness $L$. A subgroup gives a second constraint on the total mass of a coset.

## The exact mass of a coset

Let $B\le Q$, $b=|B|$, and $A=B^\perp\le\widehat Q$. Define $\theta_\pm(B)$ by the same two Fourier LPs on the positional group $B$ using $s|_B$. These are the ordinary theta values for the two complementary induced graphs on $B$. Then on either sign support,

$$\max_{\mu}\mu(i+A)=\theta_\sigma(B)/b=1/\theta_{-\sigma}(B).$$

To prove this, translate to $A$ and then average the spectrum over translations by $A$. The average leaves its coset mass unchanged, preserves nonnegativity and kills exactly the positional Fourier coefficients outside $B$. Its profile on $\widehat Q/A\cong\widehat B$ is therefore an arbitrary feasible spectrum for the restricted mask, normalized to mean one. The coset mass is the marked profile divided by $b$. Conversely every feasible quotient profile lifts to a feasible full spectrum by repeating it over each frequency coset. The second equality is the complementary theta identity on the vertex-transitive graphs on $B$. Translation of a real nonnegative spectrum need not preserve evenness, but inversion averaging at the quotient mark restores evenness without changing the marked value. For the original even LP, the exact formula holds on the unshifted coset; the upper bound holds on every translate.

In particular, a cost proportional to $\mathbf1_A$ has an exact signed LP determined by the opposite-support theta of the smaller graph on $B$. If $b$ is larger than the [Hanson–Petridis bound](https://arxiv.org/abs/1905.09134), both signs occur on $B\setminus\{1\}$ at prime order. An all-plus mask would make $B$ a clique. An all-minus mask would make a nonsquare multiple of $B$ a clique. So $\theta_{-\sigma}(B)\ge2$ in this range, giving an upper bound $1/2$ on the coset mass. At square order with $B=\mathbb F_{\sqrt q}^\times$ and $\sigma=+1$, the whole coset mass can be one. An unbounded opposite theta on comparable prime-order subgroups would strengthen this exclusion to vanishing mass.

For a simple sufficient arithmetic condition, put $J_B=\max_{\psi\ne1}|\sum_{a\in B}\psi(a)s(a)|$ and $F(B)=\sum_{a\in B}s(a)$. The constant witness on the allowed support gives

$$\theta_\epsilon(B)\ge1+\frac{b-1+\epsilon F(B)}{1+J_B}.$$

The usual completion bounds $|F(B)|$ and $J_B$ by $\sqrt p$, so this yields growth when $b/\sqrt p\to\infty$. At the critical scale $b\asymp\sqrt p$, a uniform strong bound on $F(B)$ is already a shifted-subgroup character-sum problem. The simple sufficient estimate above also involves the twisted sums. [Bourgain's question and the elementary square-root estimate](https://arxiv.org/pdf/1401.4618)

## An explicit repair that uses both bounds

Let $L_B$ be a nonnegative opposite-support witness on the quotient $\widehat Q/A$, of mean one and marked value $h_B\ge1$. For the mean-zero cost $C=\sigma P_\sigma z_T/T$, choose a constant $\beta$ and nonnegative coset heights $\gamma_a$, and put $e_i=(C_i-\beta-\gamma_{[i]})_+$. The opposite-support majorant

$$\beta\mathbf1+\frac{L*e}{h}+\operatorname{lift}\!left(\frac{L_B*\gamma}{h_B}\right)$$

dominates $C$ pointwise by the diagonal contributions of the two convolutions. Its mean is $\beta+\sum_i e_i/h+\sum_a\gamma_a/h_B$. This is the dual of the relaxation retaining just $\sum_i\mu_i=1$, $0\le\mu_i\le1/h$, and $\mu(a+A)\le1/h_B$. One can therefore optimize the repair by sorting. In units of weight $1/h$, keep the top $h/h_B$ entries in each coset, allowing a fractional last entry and capping at the coset size. Among these entries keep the top $h$ units of weight globally. This is the optimal mean when the two kinds of translates are used through their guaranteed diagonal contributions. Optimizing their off-diagonal contributions can yield a lower mean. The coefficients for the diagonal construction follow by taking $\beta$ at the global threshold and $\beta+\gamma_a$ at the per-coset threshold whenever this raises $\beta$. If the per-coset cap is inactive, set $\gamma_a=0$. Symmetric costs also permit inversion averaging of any majorant.

For a plateau of scaled height bounded at fixed depth above a small constant baseline, covering it by $o(h_B)$ cosets makes its contribution to the normalized LP cost vanish. This does not require small pointwise occupancy of the cosets. For more dispersed high frequencies the per-coset restrictions can be inactive, even with a large $h_B$.

## Enforcing the entire quotient mask

The vector of coset masses $\nu_a=\mu(a+A)$ belongs to the allowed quotient Fourier space $U_\sigma(B)$ by the same translation average. This gives a stronger relaxation than keeping only $\nu_a\le1/h_B$. Its dual minimizes

$$\overline u+\frac1h\sum_i(C_i-u_{[i]})_+\qquad(u\in U_{-\sigma}(B)).$$

Indeed the quotient orthogonality constraints supply the profile $u$, and the pointwise probability bound supplies the nonnegative excess. If $u$ is such a profile, $\operatorname{lift}(u)+L*(C-\operatorname{lift}(u))_+/h$ is a valid opposite-support majorant with this mean. The epigraph on each coset uses the maximum of the prefix sums of sorted $C_i-u_a$. The probe optionally solves this sparse LP and reprojects the resulting profile before using the point repair. On the square control with $B=\mathbb F_{\sqrt q}^\times$, the positive-side quotient profile is forced to be constant, so the stronger relaxation still gives exactly the point bound. On the negative side, the quotient constraint forces uniform primal coset mass and the pair of point and optimal coset caps already imposes it.

## Finite-order comparisons

The [probe](../coset_majorants.py) compares the repairs on a centered single-coset plateau of height $1/\sqrt n$ and on actual averaged iterate costs. On the plateau the normalized LP bounds at $\tau=0.05$ are

| Field order | $b$ | Sign | Point bound | Combined bound |
| ---: | ---: | ---: | ---: | ---: |
| $9601$ | 96 | $+$ | $1.014016$ | $0.245499$ |
| $153649$ | 388 | $+$ | $1.022054$ | $0.045469$ |
| $1000033$ | 947 | $+$ | $1.023613$ | $0.029027$ |
| $389^2$ | 388 | $+$ | $1.022054$ | $1.022054$ |
| $389^2$ | 388 | $-$ | $1.022054$ | $0$ |

The [70 rows](../data/coset-majorants.csv) include 48 interval-checked rational upper bounds from repaired iterate spectra and 40 comparisons with the whole quotient mask. The majorant slacks and costs elsewhere in the CSV are floating-point diagnostics. At depth $512$ the per-coset caps are largely inactive at the matched primes. The full quotient mask gives a smaller residual gain. For instance the negative-side drift bound at $9601$ goes from $0.010574$ to $0.010543$ with the caps and to $0.010072$ with the mask. At $389^2$ the caps reduce the negative-side drift bound from $0.010615$ to $0.007985$, while the positive-side drift bound remains $0.368600$. Independent primal LPs at four small group–subgroup pairs agree with both dual constructions to within $2\times10^{-15}$.

The single-coset test shows what the method could gain if actual costly frequencies lie on appropriate cosets. Establishing such localization through primes, or controlling more dispersed supports, remains open.
