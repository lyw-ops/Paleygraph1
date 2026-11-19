# Explicit Fourier majorants for the signed iterate costs

Write $J$ for the projection onto the constant frequencies and $P_\sigma=(I+\sigma K-J)/2$ for the mean-zero sign projection. The [signed drift LP](signed-drift.md#a-linear-program-test-independent-of-the-stationary-solve) for sign $\sigma$ asks for a small-mean majorant of $\sigma z_T/T$ in $U_{-\sigma}=\mathbb R\mathbf1\oplus V_{-\sigma}$. Its only part outside $U_{-\sigma}$ is

$$C=\frac{\sigma P_\sigma z_T}{T}.$$

The following construction supplies such a majorant from the order statistics of $C$. It also produces a feasible theta spectrum without solving the stationary equation.

## Repair with translated witnesses

For the opposite sign, take the elementary Fourier spectrum

$$L=F\left(\delta_1+\frac{2}{\sqrt q+1}\mathbf1_{\{s=-\sigma\}}\right).$$

Its mean is one and its marked value is $h=L_0=1+(n-1+\sigma)/(\sqrt q+1)$. At nontrivial frequencies $L_k=1+(-\sigma\lambda_k-1)/(\sqrt q+1)\ge0$ by the Jacobi entry bound. The marked value is positive. Translation of $L$ in the frequency group still lies in $U_{-\sigma}$, since it modulates the positional row without changing its support.

For any real threshold $b$, let $c_i=(C_i-b)_+$ and take the unnormalized cyclic convolution $L*c$. The spectrum

$$Q=b\mathbf1+\frac{L*c}{h}$$

belongs to $U_{-\sigma}$. Since $L\ge0$, its $i$th entry is at least $b+c_i\ge C_i$. If $C$ is even, the complete convolution also is even. Adding the $V_{-\sigma}$ part of $\sigma z_T/T$ gives a majorant of the full cost with the same mean.

The mean of $Q$ is $b+h^{-1}\sum_i(C_i-b)_+$. With $C_{(1)}\ge\cdots\ge C_{(n)}$ and $r=\lfloor h\rfloor$, its minimum over $b$ is

$$\mathcal M_\sigma=\frac1h\left(\sum_{j=1}^r C_{(j)}+(h-r)C_{(r+1)}\right).$$

For $h=n$ interpret the last summand as zero and take $b=C_{(n)}$. This is the piecewise-linear threshold minimum, attained at $b=C_{(r+1)}$ when $r<n$. Consequently $d_\sigma^{\rm LP}(T)\le\sqrt{nW}\,\mathcal M_\sigma$. The order-statistic formula can also be obtained by replacing the LP cone with the entrywise constraint $0\le P_i\le n/h$ and mean one. The entrywise constraint follows by pairing $P$ with every translate of $L$ and keeping the term corresponding to the translated mark. The convolution construction gives the dual majorant realizing this upper bound.

As $h\sim\sqrt q/2$, a sufficient estimate is a vanishing sum of the largest $O(\sqrt q)$ positive entries of $\sigma P_\sigma z_T/T$ in the field-first, depth-second limit. The marked entry can be left out of this sum at a cost $O_\tau(T^{-1/2})$ in the resulting bound, by $\|z_T\|_2^2\le 2WT$. Thus the test tolerates isolated peaks of small total amplitude. For the square-order plus test, [the subfield witness](signed-drift.md#a-linear-program-test-independent-of-the-stationary-solve) already forces $d_+^{\rm LP}(T)$ to stay bounded below at each fixed $T$ for $\tau<1$. In the explicit construction the opposite witness vanishes on every unmarked frequency of the subfield annihilator, since there $\lambda_k=\sqrt q$. Repairs centered at two frequencies in the same coset of that annihilator give no help at each other's center.

## A feasible theta row obtained from the same repair

Let $F=T^{-1}\sum_{t<T}A_{t,-\sigma}$, with $A_{t,-\sigma}=(\Phi(z_t)-\sigma z_t)/2$. The averaged update gives $P_\sigma A_{t,-\sigma}=\sigma P_\sigma(z_{t+1}-z_t)$. Hence $P_\sigma F=C$, and

$$\widetilde L_{-\sigma}=F-C+Q\in U_{-\sigma},\qquad \widetilde L_{-\sigma}\ge F>0.$$

After normalizing by its mean, its marked value lower-bounds $\theta_{-\sigma}$. Complementary theta gives the upper bound $\theta_\sigma/\sqrt n\le\sqrt n\,\overline{\widetilde L_{-\sigma}}/(\widetilde L_{-\sigma})_0$. This uses the mark actually reached by the repaired row, which can exceed $F_0$. Two simpler repairs use the constant $\max_i C_i$, or the constant $\max_{i\ne0}C_i$ supplemented with a multiple of $L$ to repair the mark alone.

The [probe](../iterate_majorants.py) compares the three repairs. For its certified entries, it only uses the numerical iterations to propose a row. It rounds that row on the permitted positional support and checks its Fourier nonnegativity with interval arithmetic through the [existing verifier](../smoothing.py). The exact upper bound is the rational complementary bound. The intermediate slack and drift values in the CSV are floating-point diagnostics.

The [128 recorded rows](../data/iterate-majorants.csv) cover five prime and three square orders, two weights, four depths, and both signs. There are 96 rational upper bounds. The projection and telescope agree to within $2.9\times10^{-15}$ over the sweep. At $\tau=0.005$ and $T=512$ the following repaired values are rounded for display. Only the orders marked as certified have completed interval checks in the sweep.

| Field order | Top-sum bound $+$ | Top-sum bound $-$ | Upper for $\theta_+/\sqrt n$ | Upper for $\theta_-/\sqrt n$ | Certified |
| ---: | ---: | ---: | ---: | ---: | :---: |
| $151337$ | $0.01268$ | $0.01265$ | $1.009283$ | $1.011277$ | yes |
| $1000033$ | $0.01327$ | $0.01336$ | $1.011706$ | $1.010133$ | |
| $389^2$ | $0.39192$ | $0.01129$ | $1.410846$ | $0.907662$ | yes |

At $151337$ the constant-only normalized upper bounds are about $1.53$ for both signs, and the mark-only upper bounds are about $1.012$ and $1.015$. The translated repair gives a finite certificate from a prescribed number of iterations. The [stationary-spectrum certificates](../data/smoothing-certified.csv) give tighter bounds at their recorded primes.

There is a distinction between the fixed-depth limit and these finite-order comparisons. Under the [uniform fixed-depth argument](uniform-fixed-depth.md#the-two-largest-coordinate-repair-costs-at-fixed-depth), the two top-sum repair costs approach each other when $q\to\infty$ at each fixed $T$. The [additional 70 rows](../data/majorant-depth-control.csv) hold the depth fixed while increasing the square order. At depth $32$, the signed difference still measures about $0.268$ at $1999^2$. These orders do not give a rate for the field-first approximation. A prime-specific control of the large-depth repair costs remains open.

The [coset repair](coset-majorants.md) strengthens the probability relaxation underlying the top sum. It imposes coset mass bounds or the full Fourier constraints of a quotient before sorting the remaining point masses.
