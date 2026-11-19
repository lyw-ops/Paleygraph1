# Sparse weights: eliminate collisions and freeze the mass profile

Let $F=F_+-F_-$ and $a_k$ be as in the [random-weight expansion](random-weight-ranks.md). For $1\le k\le n$, define $b_k$ by the same experiment as $a_k$, with the $k$ labels now a uniform ordered injection into the $n$ frequencies. Define $B_k$ using that injection with the **deterministic** normalized masses
$$
w_j=\frac{x_{j,k}}{k},\qquad x_{j,k}=H_k-H_{k-j},\qquad j=1,\ldots,k.
$$
The $x_{j,k}$ are the expected exponential order statistics and sum to $k$. The following bounds hold at both prime and prime-square orders (they only need the complementary entropy identity and the rank bound):
$$
\begin{split}
\left|G_n(t)-\mathbb E b_{1+\operatorname{Bin}(n-1,\rho)}\right|
  &\le Cc^2,\qquad c=t/n\in(0,1/2],\quad \rho=1-e^{-c},\\
|a_k-B_{k^\circ}| &\le C\big((k/n)^2+k^{-1/2}\big)+H_{k^\circ}/k^\circ,\qquad
 k^\circ=\left\lceil n(1-e^{-k/n})\right\rceil,\\
|a_k-B_k| &\le C(k/n+k^{-1/2})+H_k/k,\qquad 1\le k\le n/2.
\end{split}
$$
Here $G_n(t)=t^{-1}\mathbb EF(Z)$ uses the independent compound Poisson inputs. Thus all growing sparse scales reduce to a random injection with no mass randomness. For instance at $k=\lfloor n/\log\log n\rfloor$, the comparison with $B_{k^\circ}$ has error $O((\log\log n)^{-2})$, even though the probability of a collision-free iid list tends to zero. Fixing any desired accuracy also permits a finite palette of masses bounded above and away from zero after scaling by $k$, with deterministic multiplicities.

These are reductions for the signed **mean**; they do not give sign balance for the simplified input. The square-order example below shows that a mark-only Gram estimate cannot give uniform deterministic sign balance, even with these same regularized weights.

## A conditional entropy comparison

Work with unnormalized vectors, and put $\phi(x)=x\log x$, $\phi(0)=0$. For any integrable nonnegative random weight vector $X$ with finite coordinate $x\log x$ moments, let $U=\mathbb E[X\mid\mathcal G]$ for some revealed data $\mathcal G$. Convexity of $F_\sigma$ makes the conditional Jensen gaps $J_\sigma=\mathbb E[F_\sigma(X)\mid\mathcal G]-F_\sigma(U)$ nonnegative. The complementary entropy identity gives, with $W_X=\sum_i X_i$,
$$
|\mathbb E[F(X)\mid\mathcal G]-F(U)|\le J_++J_-
=\sum_i\big(\mathbb E[\phi(X_i)\mid\mathcal G]-\phi(U_i)\big)
 -\big(\mathbb E[\phi(W_X)\mid\mathcal G]-\phi(W_U)\big).
$$
The last term subtracted is nonnegative. The bound works on boundary weights as well. If $X,Y$ are coupled with the same conditional mean vector $U$, apply it to each separately and add. For a scalar $T\ge0$ of mean $m>0$, the coordinate entropy gap is at most $\operatorname{Var}(T)/m$, since
$$
x\log(x/m)-x+m\le (x-m)^2/m.
$$

## At matched occupancy, Poisson collisions cost only $O(c^2)$

Let $N\sim\operatorname{Poisson}(c)$, $\rho=1-e^{-c}$ and $m=c/\rho$. Given an occupied site, the normalized compound mass $X=Z/m$ and a single exponential $Y$ both have mean one. Their densities $g_c$ and $f(x)=e^{-x}$ on $x>0$ satisfy
$$
|g_c(x)-f(x)|\le Cc^2(1+x^2)e^{-x/2}\qquad (0<c\le 1/2).
$$
This holds uniformly in the extreme tails. Write $\pi_j=c^j/[j!(e^c-1)]$ for the conditional multiplicity probabilities. The $j=1,2$ terms of $g_c$ are
$$
A e^{-mx}(1+Bx),\quad
A=m\pi_1=\left(\frac{c}{2\sinh(c/2)}\right)^2=1+O(c^2),\qquad B=cm/2.
$$
Since $a=m-1=c/2+O(c^2)$ and $B=a+O(c^2)$, use
$0\le1-e^{-ax}(1+ax)\le (ax)^2/2$ and $e^{-ax}\le1$ to bound the difference of these two terms from $e^{-x}$. For $j\ge3$, each gamma density $e^{-y}y^{j-1}/(j-1)!$ is at most $2^{j-1}e^{-y/2}$. At $y=mx$, summing gives at most $m e^{-x/2}\sum_{j\ge3}2^{j-1}\pi_j=O(c^2e^{-x/2})$. In particular the possible double marks have no first-order effect on the *mean-one conditional law*. Their first-order effect on the *number* of occupied sites is retained through $\rho$.

For the coupling, use a common independent Bernoulli-$\rho$ occupancy mask. At each occupied site use the overlap with density $\min(f,g_c)$ to generate a shared value; reveal it on that event. Otherwise reveal only that the site is in the residual case, and sample from the respective residual density. The two residuals have equal mass $\eta$ and equal first moment, because both original means are one. Hence the two scalar conditional means agree on the residual case as well. Use independent copies of this coupling across the sites. Each residual contribution to the conditional entropy gap averaged over its event is at most
$$
\int_0^\infty (x\log x)_+\,|g_c(x)-f(x)|\,dx+\eta/e=O(c^2),
$$
since $\phi\ge-1/e$; here $\eta\le\int|g_c-f|$. The resulting difference between the two unnormalized signed expectations is $O(n\rho c^2)$. Homogeneity gives $G_n(t)=(n\rho)^{-1}\mathbb EF(Z/m)$.

For the exponential-on-occupancy vector, conditional on $M=\#\text{occupied}$, the total is independent of the normalized weights and has mean $M$. Thus its expectation divided by $n\rho$ is $\mathbb E b_{M^\star}$, where $M^\star=1+\operatorname{Bin}(n-1,\rho)$ is the size-biased $M$. This proves the first bound.

For $k=t$ an integer, the [existing Poisson estimate](rank-partitions.md#independent-input-for-the-remainder) gives $a_k=G_n(k)+O(k^{-1/2})$. The rank integration by parts from the [random-weight expansion](random-weight-ranks.md#an-integral-identity-for-finitely-many-labels) also applies to ordered injections: deleting one of a uniform injection remains a uniform injection. Therefore $|b_{j+1}-b_j|\le1/(j+1)$ for $1\le j<n$. As $c\le1/2$, $n\rho\ge3k/4$. The binomial variance is at most $k$, and the mean of $M^\star$ is within one of $k^\circ=\lceil n\rho\rceil$. The event $M^\star<k/2$ has probability $O(e^{-k/24})$ by the binomial lower-tail bound. On its complement the harmonic modulus costs at most $2|M^\star-k^\circ|/k$; on the event itself it costs at most $1+\log k$. Averaging gives $\mathbb E b_{M^\star}=b_{k^\circ}+O(k^{-1/2})$. Finally $0\le k-k^\circ\le k^2/(2n)$, so $|b_{k^\circ}-b_k|=O(k/n)$.

## Deterministic masses and a bounded finite palette

Given an injected support, assign the sorted iid exponential masses to an independent uniform ordering of it, and condition on that ordering. The conditional mean is $x_{j,k}$ on the $j$-th site. This representation generates the same independent exponential law on the support before conditioning. The exponential spacings are independent with rates $k,k-1,\ldots,1$, by the memoryless property. Therefore
$$
\frac{\operatorname{Var}(E_{(j)})}{x_{j,k}}=
  \frac{\sum_{\ell=k-j+1}^k\ell^{-2}}{\sum_{\ell=k-j+1}^k\ell^{-1}}
  \le (k-j+1)^{-1}.
$$
The entropy comparison, followed by division by $k$, proves $|b_k-B_k|\le H_k/k$. This also gives
$$
0\le \mathbb E[E\log E]-D_k\le H_k/k,\qquad D_k=\frac1k\sum_j\phi(x_{j,k}),\quad E\sim\operatorname{Exp}(1).
$$

Here is a further simplification if the remaining problem needs uniform bounds on nonzero masses. Choose $0<\delta<1$, $L\ge1$, $0<h<1$. Split the sorted profile into the low bin $x<\delta$, geometric bins between $\delta$ and $L$ with endpoint ratio at most $1+h$, and the upper bin $x\ge L$. Replace each nonempty bin by its within-bin mean. Interpret this operation as conditioning on the sites assigned to each bin, without revealing within-bin permutations. The resulting model still uses a uniform injection, with deterministic multiplicities and at most $2+\lceil\log(L/\delta)/\log(1+h)\rceil$ mass levels. If $B_k^{\delta,L,h}$ is its mean signed optimum, the entropy comparison gives
$$
|B_k-B_k^{\delta,L,h}|\le \delta^2+h^2+2e^{-L}/L.
$$
Indeed, $x_{j,k}\ge j/k$ gives a low-bin fraction at most $\delta$; the low-bin variance divided by its mean is at most $\delta$ because $x^2\le\delta x$ there. The geometric-bin bound is $h^2$ times its mean. For the upper bin the mean is at least $L$; its variance is bounded by the mean of $(x-L)^2$ in that bin. Conditional Jensen with the ordered exponential sample gives $k^{-1}\sum_j (x_{j,k}-L)_+^2\le\mathbb E(E-L)_+^2=2e^{-L}$.

These new levels lie in $[\delta/4,L+1]$. For the lower endpoint, $x_{j,k}\le j/(k-j+1)$, so if the low bin contains $s>0$ terms, $s+1\ge \delta k/(1+\delta)$. Its mean is at least $(s+1)/(2k)$. For the other endpoint, the last $s$ terms have average $H_k-H_s+1$. When $s<k$, the first term immediately before them is $H_k-H_s<L$; when $s=k$ the mean is one. This handles both tails without assuming no extreme exponential jump in the sample.

Consequently one can first prove the injection comparison only for these deterministic palettes (with each palette parameter triple fixed as $n\to\infty$). Taking $\delta,h\downarrow0$ and $L\uparrow\infty$ then recovers the original $a_k$ on any growing sparse scale. The palette proof does not reduce the problem to equal masses: the entropy difference between the exponential law and the constant mean-one profile tends to $1-\gamma$, which is too large to discard.

## What the square control excludes

The reduction works over squares. For fixed $k=2$, $b_2=a_2+O(1/n)$ because the collision event has probability $1/n$ and $|a_1-b_2|\le 1/2$. In square order the exact single-mark value $a_1=\log(2(r-1)/(r+1))$ and the rank bound imply $\liminf b_2\ge\log2-1/2$. Thus decolliding the labels itself does not force sign balance.

There is also a growing square counterexample to a uniform bound over *every* legal injection of the harmonic profile. Let $q=r^2$, $r\equiv1\pmod4$ prime, and use the subfield and norm-one frequency grid of [sparse-mark geometry](sparse-mark-geometry.md#the-entropy-carried-by-exact-coset-collisions). Choose $j$ rows and $j$ columns, $k=j^2$, and place each consecutive block of $j$ increasing $x_{\ell,k}/k$ in one column. Write $R,C$ for the row and column of a mark drawn according to these masses. If $\mu_\ell$ is the unnormalized mean of column $\ell$, put
$$
D_C=\log j-\mathsf H(C)=j^{-1}\sum_{\ell=1}^{j}\phi(\mu_\ell),\qquad
D_R=\log j-\mathsf H(R),\qquad \Delta=D_k-D_C.
$$
The difference $\Delta=D_R+I(R;C)$ is the information lost by making the weights constant within each column. It is at most $H_k/j$: on each column the entropy gap is at most its variance divided by its mean, which is bounded by its range since $x^2\le (\max x)x$; the sum of the ranges of consecutive blocks is at most $H_k$. The square-grid estimate
$|F-[a_1-\mathsf H(R)+\mathsf H(C)]|\le I(R;C)$ now gives
$$
0\le F(w)-(a_1-D_k)\le2\Delta.
$$
The same argument works for a monotone binned profile, with $D_k$ replaced by its entropy moment and the sum of ranges bounded by $L+1$; the change in $D_k$ is bounded by the palette error above.

Take $j=\lfloor n^{1/8}\rfloor$. Then $k\asymp n^{1/4}$, and these **distinct** profiles have
$$
F(w)\longrightarrow \log2-\mathbb E[E\log E]=\log2-1+\gamma>0.
$$
At the same supports the Jacobi entry bound gives $\|K_{S,S}\|_{2\to2}\le k\sqrt q/n=o(1)$. The two Fourier projectors compressed to the marks both approach $I_S/2$, since they are $(I_S+J_{S,S}\pm K_{S,S})/2$. Thus uniform cancellation cannot follow from that convergence alone. These grid placements are prescribed and not uniform injections. They do not give a nonzero $B_k$ or $a_k$ on the growing square scale.

## Verification and remaining comparison

The [replay script](../parallel_sparse_check.py) integrates the positive and negative density residuals for six Poisson intensities from $10^{-4}$ to $1/2$. It checks that their masses and first moments agree and evaluates the entropy bound on the residual events; this is a floating-point check of the coupling, not the proof of the uniform rate. It also builds the square profiles by the Chinese remainder theorem and evaluates the signed objective using the existing projected FFT intervals with floor mass $10^{-4}$. Run:

~~~sh
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python parallel_sparse_check.py
~~~

The residual masses and first moments agreed within $6.2\times10^{-13}$; the sum of the residual entropy gaps divided by $c^2$ ranged from $0.0398$ to $0.0470$. The four objective intervals were contained in the corresponding square bounds:

| $r$ | $k$ | Analytical interval | Projected FFT interval | $\|K_{S,S}\|$ |
|---:|---:|---:|---:|---:|
| 13 | 9 | [0.214812, 0.310761] | [0.306974, 0.307152] | 0.5477 |
| 29 | 25 | [0.242781, 0.303572] | [0.301747, 0.301935] | 0.5245 |
| 37 | 36 | [0.246261, 0.296459] | [0.289437, 0.289626] | 0.5025 |
| 97 | 100 | [0.261562, 0.289857] | [0.282738, 0.282934] | 0.4602 |

The FFT stationary residuals were below $8\times10^{-10}$. These finite orders use larger rectangles than $j=\lfloor n^{1/8}\rfloor$ for a more informative numerical comparison. The norm limit for the stated sequence follows from the Jacobi bound, independently of these numbers.

The outstanding estimate is sign balance for the geometry of a uniform injection with prescribed masses. The reductions remove arbitrary collision multiplicities and unbounded or very small jumps from that estimate. They do not constrain the optimizers' mass on unmarked frequencies. The square calculation shows why that exterior geometry, or some other information beyond the mark compression, is needed. Separately, reducing $a_k$ to zero at a growing scale would control the rank expansion's tail at that scale; one would still need the accumulated signed rank terms below it for Conjecture 26.
