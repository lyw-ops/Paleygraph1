# The forbidden autocorrelation of a rooted prime witness

A prime witness at the round-42 critical mass must cancel a positive amount of autocorrelation on its forbidden positional differences, in **every** decomposition into Fourier squares. The lower bound tends to at least $\sqrt{1+\tau}-1$ at each fixed positive floor. A strictly positive critical square-field witness can have zero such cancellation. This excludes the cancellation-free construction uniformly through primes at positive floors.

At $p=101$ a strictly positive, exactly critical prime witness singles out the distinguished root as the **only** translation above an explicit true endpoint threshold. At that same prime a uniform interval of floors around $1/20$ admits a complete classification at all depths: both true averaged proposals admit simultaneous strictly positive mark-preserving completions exactly at the integers $T\ge7$. The classification concerns one field, including infinitely many depths there. It gives no uniform prime window or ordinary-theta limit.

## A prime obstruction for all Fourier-square factorizations

Write $Q=(\mathbb F_p^\times)^2$, $n=|Q|=(p-1)/2$, $s(t)=\chi(1-t)$ and $\mathcal F$ for unitary Fourier transformation on $Q$. For a normalized frequency probability $\mu$, let $M=n\mu(0)$, $\alpha=M/\sqrt n$. Consider any finite factorization
\[
 \mu(h)=\sum_j |\mathcal F b_j(h)|^2,\qquad b_j:Q\to\mathbb C.
\]
One always exists by inverse transforming $\sqrt\mu$. Parseval gives $\sum_j\|b_j\|_2^2=1$, and at the root $M=\sum_j|\sum_x b_j(x)|^2$. With ordered pairs, put
\[
 c(t)=\sum_{j,x}b_j(tx)\overline{b_j(x)},\qquad
 C=\sum_{s(t)=-\sigma}\sum_{j,x}|b_j(tx)b_j(x)|,
 \qquad L=\sum_{s(t)=-\sigma}|c(t)|.
\]
Exact sector feasibility is equivalent to $L=0$ because $c$ is the inverse Fourier transform of $\mu$ up to the normalization and the Fourier sign. Thus all the absolute mass $C$ on forbidden ratios cancels in this case. The estimate also applies to a numerically proposed row with $L>0$.

Let $\omega$ be the clique number of the graph on $Q$ with distinct $x,y$ adjacent when $s(y/x)=\sigma$. Then
\[
               M\le\omega+\omega L+(\omega-1)(C-L).                 \tag{1}
\]
To see this, let $B=\sum_j(\sum_x|b_j(x)|)^2$. For nonnegative graph vertex weights $a_x$ of sum one, the ordered edge mass is at most $1-1/\omega$. Indeed among maximizers pick one of minimum support. If two nonadjacent vertices have positive weights, move their combined weight to whichever has larger weighted neighbor sum. This preserves or improves the objective and reduces the support. A clique-supported vector has ordered edge mass $1-\sum a_x^2\le1-1/\omega$. Apply this inequality separately with $a_x\propto|b_j(x)|$ and sum, ignoring zero factors. The diagonal squared mass across factors is one, so $B/\omega\le1+C$. Also $B-M$ sums the nonnegative quantities $|b_j(y)b_j(x)|-\operatorname{Re}(b_j(y)\overline{b_j(x)})$ over ordered pairs. Retaining only forbidden pairs gives $B-M\ge C-L$. The two estimates give (1).

Put $h_p=\lfloor(1+\sqrt{1+4n})/2\rfloor$. Hanson and Petridis give $\omega\le h_p-1$ for $\sigma=+$, since adjoining the field element $0$ to an allowed clique gives a Paley clique of size $\omega+1$. For $\sigma=-$, scaling the clique by a nonsquare gives a Paley clique, so $\omega\le h_p$. Here $\chi(y-x)=s(y/x)$ for $x,y\in Q$, using $\chi(-1)=1$. The input is the prime-field clique bound. [Hanson and Petridis](https://arxiv.org/abs/1905.09134)

In particular, writing $H=h_p-\mathbf1_{\sigma=+}$, every actual feasible witness with $H>1$ satisfies
\[
                      C\ge ((M-H)/(H-1))_+.                              \tag{2}
\]
For $H=1$, (1) itself gives $M\le1$ at $L=0$. At $\alpha\ge\sqrt{1+(1-1/n)\tau}-o(1)$ and fixed $\tau>0$, (2) forces $\liminf C\ge\sqrt{1+\tau}-1$. If $\tau\to0$, $\tau\sqrt n\to\infty$, and the mass error is $o(\tau)$, it gives $\liminf C/\tau\ge1/2$. For a near-sector row with $L=o(\tau)$ in this latter regime, (1) gives the same lower bound on $(C-L)/\tau$. These are absolute ordered autocorrelation budgets for factors of total squared norm one. Their fraction of all off-diagonal mass need not be bounded below.

At $C=0$ the support of each factor is an allowed clique. Conversely the normalized indicator of any maximum clique used as a single factor gives an exact feasible probability with $M=\omega$. Thus the cancellation-free subclass has exact rooted optimum $\omega$. This includes arbitrary sums of clique-supported Fourier squares with complex amplitudes. The restriction $C=o(1)$ has not been proved for a factorization of an arbitrary high-mark witness. Taking absolute values of a complex factor increases forbidden autocorrelations and can destroy sector feasibility.

At $q=r^2$, the [subfield plus witness](square-order-control.md) has a single positional factor $\mathbf1_{\mathbb F_r^\times}/\sqrt{r-1}$, all of whose nonidentity ratios are allowed. It has $C=0$, $M=r-1$. The uniform frequency probability also has $C=0$, using one positional delta. Mixing both probabilities via their separate scaled factors keeps $C=0$ and can make the probability strictly positive and exactly critical at each fixed $0<\tau<1$ for all sufficiently large squares. This uses $(r-1)/\sqrt n\to\sqrt2$.

## A prime where the critical probability selects the exceptional root

The [checker](astra-rooted-43-check.py) gives rational cosine coefficients for mean-one strictly positive rows $A_\sigma$ at $p=101$, $n=50$. Their nonconstant coefficients have the prescribed positional sign, by checking $s(4^j)$ directly. The minima exceed $9\cdot10^{-8}$; their root values divided by $\sqrt n$ are in $(0.88957645,0.88957647)$ and $(1.12413026,1.12413029)$ respectively. Linear programming proposed the coefficients. Their exact feasibility only uses the saved integers and Arb enclosures of every cosine.

At $\tau=1/4$ the minus row normalized to probability is supercritical by more than $0.00833$ in $\alpha-\sqrt W$, $W=1+(1-1/n)\tau$. Equation (2) forces $C>0.15813$ for this row in every factorization. Take
\[
 \lambda=(\sqrt{n W}-1)/(A_-(0)-1),\qquad
 \mu=(1+\lambda(A_--1))/n .
\]
Here $0<\lambda<1$ and $\sqrt n\mu(0)=\sqrt W$ exactly. Using the [round-42 scores](astra-witness-resume-42.md) and the actual zero-start undamped Picard recurrence, 256-bit interval evaluation gives
\[
 Q_7(0)\in(0.27055,0.27057),\qquad
 \max_{x\ne0} Q_7(x)\in(0.26738,0.26740).
\]
Thus the distinguished root is the unique shift with $Q_7(x)>(77/2000)7$. This is an explicit finite example for a single depth and threshold. It makes no asymptotic claim about the size of a prime root score.

## Simultaneous positive completion at every depth from seven onward

Fix $p=101$ and any real $|\tau-1/20|\le10^{-8}$. Take the actual proposals $X_{\sigma,T}$ and means $M_T$ from [round 35](averaged-mark-35.md). Write $z_\sigma=X_{\sigma,T}(0)/M_T$. For $T\le6$, $z_+>n/A_-(0)$, which is impossible for any nonnegative plus row of mean one by complementary-sector orthogonality with $A_-$. For every $T\ge7$, $1<z_\sigma<A_\sigma(0)$ holds for both signs. Therefore the explicit row
\[
 M_T\left[1+\frac{z_\sigma-1}{A_\sigma(0)-1}(A_\sigma-1)\right]
\]
has the required mean, sector and root and is strictly positive everywhere. This checks an exact mark and mean of the unrounded orbit at each real floor in the interval.

Here is how the finite replay proves the infinite tail. At each time $t$ the instantaneous contribution is $x_{\sigma,t}=g_t+(P_\sigma a_{\sigma,t})(0)$, with $g_t=n^{-1}\sum_i\phi_t(i)/2$, $a_{\sigma,t}=(\phi_t+\sigma v_t)/2$, in unscaled units. Consequently $z_\sigma=\sum_{t=1}^T x_{\sigma,t}/\sum_{t=1}^T g_t$. At the central floor the checker iterates midpoint approximations $u_t$ in counting Euclidean norm. The input-floor perturbation in the activation at a common vector is at most $e=2(\sqrt{1/20}-\sqrt{1/20-10^{-8}})<4.48\cdot10^{-8}$. If $\|v_t-u_t\|\le d$, then nonexpansiveness bounds the next radius by $d+e$ plus the Euclidean norm of the coordinate rounding radii. The errors in $g_t$ and $x_{\sigma,t}$ are bounded by $(d+e)/(2\sqrt n)$ and $d+e+(d+e)/(2\sqrt n)$ respectively, since $\|P_\sigma\|\le1$. This permits outward interval tests on every prefix through $T=300$. The smallest certified upper-bound violation on the first six prefixes exceeds $0.00047$ in the mean-one root. The smallest gap below the respective witness root from $T=7$ through $300$ exceeds $0.0107$.

At time 300 the true state is within $1.35\cdot10^{-5}$ of $u_{300}$ uniformly in floor. On its closed Euclidean ball of radius $r=10^{-3}$, the activation has Lipschitz constant at most $0.98885$ by maximizing $|z|/\sqrt{z^2+4w_i}$ coordinatewise over $|z|\le|u_{300,i}|+r$, using the smallest allowed $w_i$. At the center the central-floor one-step displacement is below $1.86\cdot10^{-6}$. Thus $0.98885r+e+1.86\cdot10^{-6}<r$, proving invariance. Throughout this entire ball the same evaluation bounds certify $g_t<x_{\sigma,t}<g_t A_\sigma(0)$ for both signs. Summing these inequalities with the strict prefix proves the all-depth assertion.

Run `.venv/bin/python -B research/astra-rooted-43-check.py` for the [nine records](astra-rooted-43-checks.jsonl). The all-depth proof uses a field-specific invariant ball. Its contraction or the favorable root margins have not been proved uniformly through primes. Equation (2) is uniform and constrains root behavior via positional autocorrelation, but supplies no upper bound on that cancellation. The corresponding all-prime completion in the log-star window and ETH Problem 26 remain open.
