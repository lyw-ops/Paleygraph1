# Actual-orbit switching loss and logarithmic mass control

This does **not** prove or disprove [ETH Problem 26](https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/). It gives a new unconditional estimate for the genuine averaged iteration, a restricted field-first negative-pairing theorem using the existing fixed-depth arithmetic input, and an interval-certified prime example ruling out one tempting strengthening.

The main unconditional estimate is

\[
 \frac1n\sum_{i\ne0}\sqrt n\,(H_{\sigma,T,i})_-
 \le \frac{m_T}{T}
 \le \frac{\sqrt W}{T}
       \left(\sqrt2+\frac{\lceil\log_2T\rceil}{2}\right),
 \qquad T\ge1.                                                   \tag{1}
\]

It holds at **zero bulk floor**, and also at positive floors. In particular the unweighted negative cost is \(O(\log T/T)\), not merely the \(O(T^{-1/2})\) obtained from the terminal norm. The new ingredient is an exact two-time loss identity, used at every dyadic time scale. It includes the loss from opposite signs at two times, rather than discarding that loss in the nonexpansiveness estimate.

The restricted arithmetic conclusion is this: at zero floor, for each fixed depth, every probability whose inverse Fourier coefficients have bounded absolute sum sees the same negative cost as uniform measure, up to \(o_p(1)\). The bound on that sum may depend arbitrarily on the depth. Such tests consequently have vanishing field-first negative pairing by (1). The arithmetic input is the finite-expression Mellin approximation from [iteration-parity.md](iteration-parity.md); the argument below states explicitly what is inherited from that draft. It does not establish an estimate for the full opposite cone. In particular, the trace argument used here is also valid over extension fields, so it is **not** the missing prime-only input.

## 1. Setup and an exact two-time identity

Let \(j=\mathbf1/\sqrt n\), \(J=jj^{\mathsf T}\), and suppose

\[
 K=K^{\mathsf T},\qquad Kj=0,\qquad K^2=I-J.
\]

Allow arbitrary nonnegative weights \(w_i\), with \(W=\sum_iw_i>0\). Put

\[
 u_t=\Phi(z_t),\quad \Phi_i(x)=\sqrt{x_i^2+4w_i},\quad
 z_0=0,\quad z_{t+1}=\frac{z_t+Ku_t}{2},\quad
 d_t=z_t-z_{t+1},\quad m_t=\frac{\langle j,u_t\rangle}{2}.
\]

All \(z_t\) have mean zero. The usual one-time norm identity is

\[
 \|z_{t+1}\|^2=\|z_t\|^2+2W-2m_t^2-\|d_t\|^2.
                                                                    \tag{2}
\]

Consequently

\[
 \sum_{t<N}m_t^2\le WN,\qquad \|z_N\|^2\le2WN.                    \tag{3}
\]

For two times \(s,t\), define the nonnegative scalar

\[
 Q_{s,t}=\sum_i\big(u_{s,i}u_{t,i}-z_{s,i}z_{t,i}-4w_i\big).
                                                                    \tag{4}
\]

The summands are nonnegative: for \(w_i>0\), write
\(z_{t,i}=2\sqrt{w_i}\sinh\gamma_{t,i}\); the summand becomes
\(4w_i[\cosh(\gamma_{s,i}-\gamma_{t,i})-1]\). At \(w_i=0\) it is
\(|z_{s,i}z_{t,i}|-z_{s,i}z_{t,i}\).

**Two-time loss identity.** For all \(s,t\ge0\),

\[
\begin{split}
 \|z_{t+1}-z_{s+1}\|^2
 &+\|d_t-d_s\|^2+Q_{s,t}+2(m_t-m_s)^2\\
 &=\|z_t-z_s\|^2.                                                 \tag{5}
\end{split}
\]

**Proof.** Set \(v=z_t-z_s\), \(a=u_t-u_s\). The two vectors in the first two squared norms are \((v+Ka)/2\) and \((v-Ka)/2\). Their squared norms sum to

\[
 \tfrac12\|v\|^2+\tfrac12\|Ka\|^2
 =\|v\|^2-\tfrac12(\|v\|^2-\|a\|^2)
             -\tfrac12\langle j,a\rangle^2.
\]

Coordinatewise expansion gives \(\|v\|^2-\|a\|^2=2Q_{s,t}\), and
\(\langle j,a\rangle=2(m_t-m_s)\). This proves (5), including zero weights.

At zero floor, \(w_0=1\), \(w_i=0\) for \(i\ne0\), the bulk part of (4) is exactly

\[
 Q^{\rm bulk}_{s,t}
   =2\sum_{i\ne0}|z_{s,i}z_{t,i}|
                  \mathbf1_{\{z_{s,i}z_{t,i}<0\}}.                 \tag{6}
\]

Thus (5) checks genuine consistency between two whole time slices. It is stronger than checking the averaged recurrence, reciprocal inequality, and final norm separately.

## 2. Every lag has a finite loss budget

Apply (5) at the pair \((k,k+\ell)\) and sum over \(0\le k<N\). Then

\[
\begin{split}
 &\sum_{k<N}\left(
   \|d_{k+\ell}-d_k\|^2+Q_{k,k+\ell}
          +2(m_{k+\ell}-m_k)^2\right)\\
 &\hspace{1cm}=\|z_\ell\|^2-\|z_{N+\ell}-z_N\|^2
 \le2W\ell.                                                       \tag{7}
\end{split}
\]

All summands on the left are nonnegative. Therefore one may also restrict their sum to any interval of starting times. In particular, for every \(a\ge0\) and \(N,\ell\ge1\),

\[
 \sum_{k=a}^{a+N-1}(m_{k+\ell}-m_k)^2\le W\ell.                    \tag{8}
\]

At zero floor this gives the independent switching budget

\[
 \sum_{k<N}\sum_{i\ne0}|z_{k,i}z_{k+\ell,i}|
            \mathbf1_{\{z_{k,i}z_{k+\ell,i}<0\}}\le\ell.          \tag{9}
\]

Neither (8) nor (9) contains a stationary vector. The bounds are uniform in field order and in the length \(N\) of the observed orbit.

There is also a useful temporal variance consequence. For any interval \(I\) of \(L\) consecutive times,

\[
 \frac1L\sum_{t\in I}(m_t-\overline m_I)^2
 =\frac1{L^2}\sum_{s<t\in I}(m_s-m_t)^2
 \le\frac{W(L-1)}{2L}<\frac W2.                                  \tag{10}
\]

Indeed group pairs by their lag \(1\le\ell<L\) and use (8), obtaining
\(L^{-2}\sum_{\ell=1}^{L-1}W\ell\). This bounds the variance on **every** temporal interval, not just the initial interval in (3).

## 3. A logarithmic bound for instantaneous mass

Fix \(T\ge1\), and write

\[
 A_r(T)=2^{-r}\sum_{k=T}^{T+2^r-1}m_k.
\]

Comparing the two adjacent blocks of length \(2^r\), Cauchy--Schwarz and (8) give

\[
\begin{split}
 |A_{r+1}(T)-A_r(T)|
 &=\left|\frac1{2^{r+1}}
       \sum_{k=T}^{T+2^r-1}(m_{k+2^r}-m_k)\right|\\
 &\le\frac{\sqrt W}{2}.                                          \tag{11}
\end{split}
\]

Let \(r_T=\lceil\log_2T\rceil\) and \(L=2^{r_T}\). The initial energy budget (3) gives

\[
 A_{r_T}(T)\le
 \left(\frac1L\sum_{k=T}^{T+L-1}m_k^2\right)^{1/2}
 \le\sqrt{W(1+T/L)}\le\sqrt{2W}.
\]

Telescope (11) from \(A_0(T)=m_T\) to obtain the slightly sharper version of (1):

\[
 \boxed{\quad
 m_T\le\sqrt W\,L_T,\qquad
 L_T=\sqrt{1+T/2^{r_T}}+\frac{r_T}{2}
       \le\sqrt2+\frac{r_T}{2}.
 \quad}                                                          \tag{12}
\]

The proof uses future times only to bound the already defined quantity \(m_T\); it does not modify the iteration or the trial. There is no limit interchange or regularity assumption at zero floor.

## 4. Consequences for the actual negative pairing

Use the trial from [negative-pairing.md](negative-pairing.md):

\[
 H_{\sigma,T}
 =\frac{I+\sigma K}{2}\bar u_T
 =\frac1T\sum_{t<T}A_{\sigma,t}+\frac{\sigma z_T}{T},\qquad
 A_{\sigma,t}=\frac{u_t+\sigma z_t}{2}\ge0.
\]

Set \(g_i=\sqrt n(H_{\sigma,T,i})_-\) off the mark and \(g_0=0\). Then

\[
 0\le g_i\le\frac{\sqrt n}{T}(-\sigma z_{T,i})_+.
\]

Because \(\sum_i z_{T,i}=0\),

\[
 \sum_i(-\sigma z_{T,i})_+=\frac12\|z_T\|_1
          \le\frac12\sum_i u_{T,i}=\sqrt n\,m_T.
\]

This proves (1). Together with the terminal energy bound it gives

\[
 \overline g\le
    \min\{\sqrt{2W/T},\sqrt W L_T/T\},\qquad
 \|g\|_{2,n}^2\le2W/T.                                          \tag{13}
\]

At zero floor there is an exact occupation formula, rather than just this upper bound:

\[
 g_i=\frac1T
   \left(-\sigma Y_{T,i}-\sum_{t<T}(\sigma Y_{t,i})_+\right)_+,
 \qquad Y_t=\sqrt n z_t,\quad i\ne0.                              \tag{14}
\]

For the zero-floor opposite test \(B\ge0\), \(\sum B=\sqrt n\), put
\(\rho_i=\sqrt n B_i\), so \(\overline\rho=1\). Its cost is
\(\langle(H_{\sigma,T})_-,B\rangle_{i\ne0}=\overline{\rho g}\).
For every height cutoff \(M>0\), (13) yields

\[
 \overline{\rho g}\le \frac{M L_T}{T}
                +\overline{\rho g\,\mathbf1_{\{\rho>M\}}}.        \tag{15}
\]

Consequently the low-height part is negligible uniformly over the **full** opposite cone whenever \(M_T=o(T/\log T)\). For example \(M_T=\sqrt T\) gives an unconditional low-height contribution \(O(\log T/\sqrt T)\). This is stronger than the zero-floor cutoff range supplied by the terminal \(\ell_2\) estimate alone. It also improves the bounded-height contribution at positive floors: after restoring the normalization \(\rho=\sqrt{n/W}B\), its bound is \(WM L_T/T\).

A sufficient remaining prime estimate is the vanishing of the supremum of the last term in (15), with such a cutoff, in the field-first limit. This is a restriction of the cost that remains to be bounded; (15) does not prove that tail estimate. In particular, the cost on a set cannot be discarded merely because its unweighted density is small.

## 5. A genuine-history Fourier mixing lemma

Here is a distinct consequence of using an actual finite-depth trajectory. This section inherits the fixed-expression trace approximation of [iteration-parity.md](iteration-parity.md#uniform-fixed-expression-trace-estimates). It does not claim a new independent proof of that sheaf-theoretic input.

Write \(Q=(\mathbb F_p^\times)^2\), and index the frequency coordinates by \(k\in\widehat Q\). For a frequency function \(f\), use

\[
 \widehat f(a)=\frac1n\sum_k f(k)\overline{k(a)},\qquad a\in Q.
\]

The needed arithmetic input has the following precise form. Any fixed finite polynomial in the bounded negative Mellin fields approximating finitely many iterates can be written as a finite sum of Mellin traces, plus an error supported on boundedly many characters with bounded amplitudes. The associated nonpunctual objects have bounded ranks and are lisse away from \(a=1\), and punctual summands are supported at \(1\). Therefore, at every \(a\ne1\), the inverse coefficient of that polynomial is

\[
                O_{\text{expression}}(p^{-1/2}),                  \tag{16}
\]

uniformly in \(a\). To check this step, invert a Mellin trace: its inverse coefficient is its sheaf trace at \(a\); the nonpunctual trace there has size at most rank times \(p^{-1/2}\). A punctual summand contributes only at \(1\). A bounded exceptional-character error contributes \(O(p^{-1})\) to every inverse coefficient. Mixed products use closure under convolution and lissity away from \(1\), not just cancellation of odd products at \(1\). These are the same local convolution facts used in the earlier draft; see [Rojas-León, Section 5](https://arxiv.org/pdf/1106.1398).

**Finite-history mixing lemma.** Fix a finite depth \(T\), zero floor, and a fixed globally Lipschitz function \(F:\mathbb R^{T+1}\to\mathbb R\). For
\(f_p(k)=F(Y_{0,k},\ldots,Y_{T,k})\),

\[
      \sup_{a\ne1}|\widehat f_p(a)|\longrightarrow0.              \tag{17}
\]

The same conclusion holds after changing the marked value by a quantity that is \(o(\sqrt n)\).

**Proof with the limits in order.** First fix an approximation accuracy. Replace the zero-floor trajectories by trajectories at a small fixed positive auxiliary floor \(\tau\). Nonexpansiveness and the common-input activation bound give

\[
 \|Y_t^{(\tau)}-Y_t^{(0)}\|_{2,n}
       =\|z_t^{(\tau)}-z_t^{(0)}\|_2\le t\sqrt\tau.               \tag{18}
\]

Lipschitz continuity of \(F\) controls the resulting normalized \(\ell_2\) error. At this fixed \(\tau\), use the existing fixed-depth argument to approximate the finitely many \(Y_t^{(\tau)}\) simultaneously in normalized \(\ell_2\) by bounded finite sums of negative Mellin fields. Replace \(F\) on the bounded range of these approximants by a fixed polynomial, with a uniformly small error. The resulting polynomial has (16). No polynomial is applied to the uncontrolled error in the original fields: Lipschitz continuity is used **before** polynomial approximation.

Every inverse Fourier coefficient of an error is at most its normalized \(\ell_2\) norm. Hence the limsup in (17) is at most the chosen approximation error. Take the field limit with the auxiliary floor and all expressions fixed, then send that error and the auxiliary floor to zero. A change of size \(o(\sqrt n)\) at one frequency has normalized \(\ell_2\) norm \(o(1)\). This proves the final assertion.

Apply this to the globally Lipschitz occupation function in (14). At the mark its artificial value is at most \(|Y_{T,0}|/T=o(\sqrt n)\), by the established fixed-depth marked cancellation. Resetting it to zero is therefore allowed. Thus the **actual** clipped cost satisfies

\[
 \gamma_{p,T}:=\sup_{a\ne1}|\widehat g_{p,T}(a)|\longrightarrow0
                    \quad\text{for every fixed }T.              \tag{19}
\]

This is an all-location inverse-Fourier assertion, rather than only an unweighted odd-moment assertion. It also applies to other fixed Lipschitz functions of the entire trajectory. No rate uniform in \(T\) is asserted.

## 6. A proved restricted field-first pairing branch

For a probability \(\mu\) on \(\widehat Q\), define

\[
 \beta_\mu(a)=\sum_k\mu_k k(a),\qquad
 \mathcal A(\mu)=\sum_{a\in Q}|\beta_\mu(a)|.
\]

Here \(\beta_\mu(1)=1\). Fourier inversion gives the exact comparison

\[
 \left|\sum_k\mu_k g_k-\overline g\right|
   \le(\mathcal A(\mu)-1)\gamma_{p,T}.                            \tag{20}
\]

This does not need sector feasibility. For opposite-feasible tests use
\(\mu=B/\sqrt n\), so their original negative pairing is exactly
\(\sum\mu_k g_k\).

Fix **any** function \(M:\mathbb N\to[1,\infty)\) with finite values; there is no growth restriction in \(T\). Combining (12), (19), and (20) proves

\[
 \limsup_{p\to\infty}
 \sup_{\substack{B\ge0,\ B\in U_{-\sigma},\ \sum B=\sqrt n\\
                  \mathcal A(B/\sqrt n)\le M(T)}}
       \langle(H_{\sigma,T})_-,B\rangle_{i\ne0}
 \le \frac{L_T}{T}.
                                                                    \tag{21}
\]

The right side vanishes as \(T\to\infty\), independently of how rapidly \(M(T)\) grows. A pointwise height bound alone would instead pay that growing constant. The coefficients and locations in \(\beta_\mu\) may vary with the prime; only their total absolute sum is restricted. More generally, (20) permits a field-dependent allowance whenever \(M_{p,T}\gamma_{p,T}\to0\) at each fixed \(T\).

There is a genuine limitation. A marked theta optimizer has

\[
 \mathcal A(\mu)\ge\left|\sum_a\beta_\mu(a)\right|
                      =n\mu_0=\theta_{-\sigma}.                  \tag{22}
\]

The elementary theta witnesses already make the last quantity \(\gg\sqrt p\). Thus (21) does not include the tests that directly certify the sharp theta upper bound. Also, (19) is an \(o(1)\) result, not a rate which could be multiplied by \(\sqrt p\). The unresolved prime step is control of these growing-complexity tests, or of the high-height cost in (15), using additional prime arithmetic. Neither the switching budget nor fixed-expression trace bounds supply that step.

## 7. A certified counterexample to instantaneous mass at most one

One might try to strengthen (12) to \(m_T\le\sqrt W\) by asserting that the orbit's squared norm is nondecreasing. This assertion already fails for the **actual zero-floor prime orbit**.

At \(p=401\), \(n=200\), \(T=32\), a 512-bit Arb interval evaluation of the genuine recurrence gives

\[
 \frac{100245}{100000}<m_{32}<\frac{100246}{100000},
 \qquad
 m_{32}=1.0024516543992949749278121966848\ldots .                   \tag{23}
\]

Here \(W=1\). By (2), (23) also proves
\(\|z_{33}\|^2<\|z_{32}\|^2\). This is a counterexample only to the proposed instantaneous mass bound and norm monotonicity, **not** to Problem 26 or to an asymptotic mass bound.

The following reproduces the rational enclosure from the repository root, without writing an output file. `paley_sign` generates the integer character mask by modular arithmetic. DFT and square roots below use interval arithmetic; the final assertions compare enclosures to rational numbers.

```python
from flint import arb, acb, ctx
from theta import paley_sign

ctx.prec = 512
s = list(map(int, paley_sign(401)))
n = len(s)
z = [arb(0) for _ in range(n)]
for t in range(32):
    u = [abs(x) for x in z]
    u[0] = (z[0] * z[0] + 4).sqrt()
    fv = acb.dft([acb(x) for x in u])
    back = acb.dft([fv[i] * s[i] for i in range(n)])
    z = [(z[i] + back[(-i) % n].real / n) / 2 for i in range(n)]
u = [abs(x) for x in z]
u[0] = (z[0] * z[0] + 4).sqrt()
m = sum(u) / (2 * arb(n).sqrt())
assert m > arb(100245) / 100000
assert m < arb(100246) / 100000
print(m)
```

The interval output had radius less than \(1.8\cdot10^{-81}\). Low precision is inappropriate for this naive repeated interval DFT because interval widths accumulate; the stated check used 512 bits.

## 8. Other checks and the remaining boundary

In-memory floating-point checks used the actual zero-floor orbits at
\(p=101,401,1997,9413,37253,153649,1000033\). There were 413 individual checks of (5) at lags 1 and 4, with their telescopes and the occupation formula also checked. The largest absolute error across these identities was below \(5.8\cdot10^{-15}\).

The temporal variance and logarithmic bounds were additionally tested on 280 independently generated real symmetric reflections on \(\mathbf1^\perp\), in dimensions \(3,4,5,8,12,20,40\), with both a single nonzero weight and general positive weights. All 2,240 sampled instantaneous-mass inequalities passed. These are checks of the general algebra, not substitutes for its proof.

For the actual negative-sign cost at \(T=32\), the following measurements check the normalization in (19) and (20):

| Prime | \(\overline g\) | \(\max_{a\ne1}|\widehat g(a)|\) |
| ---: | ---: | ---: |
| 1,997 | 0.0289658864 | 0.00400935195 |
| 9,413 | 0.0293814773 | 0.00239617289 |
| 37,253 | 0.0297084254 | 0.00134605304 |
| 153,649 | 0.0297827869 | 0.000678718895 |
| 1,000,033 | 0.0298556049 | 0.000303225224 |

These measurements are not a rate theorem and do not give the full LP supremum. The exact results established independently of arithmetic are (5)--(15) and the certified failure (23). The restricted limit (21) additionally uses the explicitly stated fixed-depth trace input. The full \(\liminf_T\limsup_p D_{p,T}=0\), a prime-only estimate on the remaining tests, and Problem 26 remain unproved here.
