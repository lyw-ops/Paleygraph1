# One-sided bounds from the averaged smoothing iteration

Use the [complementary spectra](marked-response.md#weighted-complementary-projections) $A,B$ at fixed positive weights $w_0=1$ and $w_i=\tau/n$ for $i\ne0$. Put $W=\sum_iw_i$, $u=\Phi(v)$, $v=A-B$, and $P_\perp=I-J$. The normalized spectra $\sqrt{n/W}\,A,\sqrt{n/W}\,B$ are feasible for the two Fourier LPs. Write $A_+=A$ and $A_-=B$.

For the averaged iteration $z_0=0$, $z_{t+1}=(z_t+K\Phi(z_t))/2$, define

$$\gamma_i(x)=\operatorname{arsinh}\frac{x_i}{2\sqrt{w_i}},\qquad
H(x)=\sum_i w_i\gamma_i(x),\qquad \overline H_T=\frac1T\sum_{t<T}H(z_t).$$

At the exact solution $H(v)=m_p(\tau)+\tau g_p(\tau)$ in the [weight-path notation](bulk-logarithm.md). The exact integral and its endpoint bound give, for $0<\tau\le n$,

$$\left|H(v)-\log\frac{\vartheta(\overline H_p)}{\sqrt n}\right|
\le \mathcal E(\tau):=\tfrac12\big((1+\tau)\log(1+\tau)-\tau\log\tau\big).$$

## Two signed comparison inequalities

Put $S_t=\sum_i\Phi_i(z_t)/\sqrt n$, $M_T=\sqrt W\sum_{t<T}S_t/(2T)$, and $d_\sigma(T)=\sigma\langle z_T,A_\sigma\rangle/T$. Then

$$M_T+d_\sigma(T)\ge W\exp\!\left(\frac{\sigma(H(v)-\overline H_T)}{W}\right),\qquad \sigma=\pm1.$$

To check the sign, let $A_t=(\Phi(z_t)+z_t)/2$ and $B_t=(\Phi(z_t)-z_t)/2$. For $r_t=z_t-K\Phi(z_t)$, symmetry of $K$ and $KA=A-\sqrt{W/n}\,\mathbf1$, $KB=-B+\sqrt{W/n}\,\mathbf1$ give

$$\begin{aligned}
\langle r_t,A\rangle&=\sqrt W S_t-2\langle B_t,A\rangle,\\
\langle r_t,B\rangle&=2\langle A_t,B\rangle-\sqrt W S_t.
\end{aligned}$$

Summing $r_t=2(z_t-z_{t+1})$ proves $T^{-1}\sum_{t<T}\langle B_t,A\rangle=M_T+d_+(T)$ and $T^{-1}\sum_{t<T}\langle A_t,B\rangle=M_T+d_-(T)$. The two products are $\sum_i w_i e^{\gamma_i(v)-\gamma_i(z_t)}$ and $\sum_i w_i e^{\gamma_i(z_t)-\gamma_i(v)}$, respectively. Jensen's inequality over the weights $w_i/(WT)$ and the $T$ times gives the bounds.

The [averaged norm identity](iteration-parity.md#a-criterion-involving-only-the-iterates) implies $M_T\le W$ and $\|z_T\|_2^2\le2WT$. Thus a simpler one-sided estimate is

$$\sigma\log\frac{\vartheta(\overline H_p)}{\sqrt n}
\le\mathcal E(\tau)+\sigma\overline H_T+d_\sigma(T).$$

This estimates the upper limit with the plus spectrum and the lower limit with the minus spectrum. Fixed-depth parity gives $\overline H_T=o(1)$ for every fixed $T$, using the marked cancellation and the bulk odd Lipschitz logarithm. For example, if $\limsup_{p\to\infty}\|A_+\|_2<\infty$ at each fixed $\tau$ in a sequence decreasing to zero, then $d_+(T)\le\sqrt{2W/T}\,\|A_+\|_2$ gives the upper half of Conjecture 26. The corresponding condition on $A_-$ gives the lower half. The norms on the two sides can be investigated independently. The arithmetic premise in this limit argument is the same fixed-depth proof draft used for the unsigned discrepancy.

## What a persistent deviation implies

Suppose along a field subsequence $\sigma\log(\vartheta(\overline H)/\sqrt n)\ge\delta>0$ and fix $\tau$ with $\mathcal E(\tau)<\delta/4$. At each fixed $T$, for large fields in the subsequence the signed drift with the mark removed is at least $\delta/2$. Here $\overline H_T=o(1)$ by parity and the removed term is $o(1)$ by boundedness of the exact marked entry and fixed-depth cancellation of $(z_T)_0$.

More generally, whenever the bulk drift is at least $\eta>0$, put $y_i=\sigma\sqrt n(z_T)_i/T$ and

$$S_{T,\sigma}=\{i\ne0:y_i>\eta/(2\sqrt W)\}.$$

The complement of $S_{T,\sigma}$ contributes at most $\eta/2$ to the bulk drift because $A_\sigma$ is positive with sum $\sqrt{nW}$. The energy bound on $z_T$ then gives

$$\frac{|S_{T,\sigma}|}{n}\le\frac{8W^2}{\eta^2T},\qquad
\frac1{\sqrt n}\sum_{i\in S_{T,\sigma}} y_i(A_\sigma)_i\ge\frac\eta2,\qquad
\|(A_\sigma)|_{S_{T,\sigma}}\|_2\ge\frac{\eta\sqrt T}{2\sqrt{2W}}.$$

The size bound is Markov's inequality applied to $\sum y_i^2/n$. The last bound uses Cauchy–Schwarz in the original coordinates. These constraints locate the necessary energy on explicit high coordinates of a fixed-depth iterate with the specified sign. They leave open the shape of those coordinates at prime order.

## A linear-program test independent of the stationary solve

The stationary correlation $d_\sigma(T)$ is bounded by the support function

$$d_\sigma^{\rm LP}(T)=\frac{\sqrt{W/n}}T\max_{P\ge0,\ P\in U_\sigma,\ \overline P=1}\langle \sigma z_T,P\rangle.$$

This is the same real nonnegative Fourier cone as the ordinary theta LP with the even cost replaced by $\sigma z_T$. Equivalently, the maximum inside this expression is $\min\sum_i Q_i$ over $Q\in U_{-\sigma}$ with $Q_i\ge\sigma(z_T)_i$ everywhere. The dual follows from the constraints on the mean and the orthogonality of $P$ to $V_{-\sigma}$. Both sides are feasible and the primal is compact, so linear programming duality applies. One can average under frequency inversion on both sides. A small-mass majorant on the opposite support certifies the sufficient bound without knowing the exact stationary spectra.

For the first iteration, $z_1=(1-\sqrt{\tau/n})Ke_0$. Its LP value (for $\tau\le n$) is exactly $(1-\sqrt{\tau/n})\sqrt{W/n}(\theta_\sigma-1)$ because $KP=\sigma(P-\mathbf1)$. At larger fixed depths, the general-cost LP must explicitly constrain the marked coordinate to be nonnegative. In the usual marked-objective LP the constant feasible vector and the objective already ensure this constraint at the optimum.

There is also a direct necessary lower bound for the LP test. For any feasible $P\in U_\sigma$ of mean one, the same telescoping calculation gives

$$M_T+\frac{\sqrt{W/n}}T\langle \sigma z_T,P\rangle
=\frac{\sqrt{W/n}}T\sum_{t<T}\langle A_{t,-\sigma},P\rangle,$$

where $A_{t,+}=A_t$ and $A_{t,-}=B_t$. Keep the marked summand and take $P$ maximizing $P_0=\theta_\sigma$. This gives

$$M_T+d_\sigma^{\rm LP}(T)\ge \sqrt{W/n}\,\theta_\sigma\,\frac1T\sum_{t<T}(A_{t,-\sigma})_0.$$

The last factor tends to one in the field-first limit by fixed-depth marked cancellation. At square orders the explicit [subfield spectrum](square-order-control.md#the-fourier-frequencies-carrying-the-discrepancy) attains $\theta_+=\sqrt q-1$, so for every fixed $T$ and $0<\tau<1$ the plus LP satisfies $\liminf_{q}\,d_+^{\rm LP}(T)\ge\sqrt{2(1+\tau)}-(1+\tau)>0$. This obstruction is independent of the exact stationary diagonal.

## Numerical comparison

The [probe](../signed_drift.py) compares both stationary drift terms, their LP upper bounds on smaller fields, and the exact mixed-product identities used in the inequalities. The [public Jig attempt](https://jig.so/p/7?s=1) gives a different conditional route through spreading of actual complex Hessian null vectors. The real inequalities here identify the sign and concentration of the necessary pairing through explicit averaged iterates.

The [96 recorded rows](../data/signed-drift.csv) cover six prime and six square orders, two weights, and four depths. The stationary residuals are below $10^{-10}$, and both mixed-product identities agree numerically to within $4.5\times10^{-10}$. Forty-eight rows include the two LP extrema. At $\tau=0.05$ and $T=128$ the comparison is

| Field order | $d_+$ | $d_-$ | $d_+^{\rm LP}$ | $d_-^{\rm LP}$ |
| ---: | ---: | ---: | ---: | ---: |
| $1997$ | $0.01894$ | $0.01965$ | $0.02024$ | $0.02106$ |
| $43^2$ | $0.24302$ | $0.00933$ | $0.26863$ | $0.01196$ |
| $151337$ | $0.02080$ | $0.02098$ | | |
| $389^2$ | $0.37363$ | $0.01274$ | | |

At $T=512$ the prime $151337$ has drifts $0.00520$ and $0.00524$. The square $389^2$ has drifts $0.33385$ and $0.00292$. The negative-side correlation decays in both examples, and the square retains a large positive-side correlation. The numerical LP upper bounds are floating-point checks at the listed finite orders.

The first-step formula was checked independently at four smaller fields, at both weights and both signs. Direct LPs for the opposite-support majorant at those fields also agreed with the primal values for arbitrary even costs to within $6\times10^{-13}$.
