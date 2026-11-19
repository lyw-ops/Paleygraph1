# A bulk excess recurrence for the actual clipped repair

For [ETH Problem 26](https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/), the upper tail of the four-step repair can be controlled by three quantities: the cost of finitely many exceptional entries, transfer between sets above a cutoff, and new excess injected by the part below the cutoff. The exceptional cost is \(O(\sqrt{s})\) for a fixed number of entries, uniformly in the field and the repair depth. The transfer is bounded by a weighted distribution of Jacobi differences; a dispersed distribution can give contraction even when the receiving set is larger than the Jacobi height. On square plus orders the actual tail retains an order-one load on the subfield annihilator. The resulting field-first criterion is conditional: the prime estimates on the new excess and the initial load still need proof.

## 1. Separate the exceptional entries at no field-dependent cost

Use the actual reciprocal pair \(x,y\) and the [clipped iteration](parallel-repair-17.md#setup-and-explicit-formula). In particular
\[
  H=(J+P)y,\quad a=H_0,\quad c=\langle j,y\rangle,\quad
  D=\sqrt n\,(-H)_+,\quad B=1-c,\quad n=(q-1)/2 .
\]
Here \(P=P_{-\sigma}\), and the repair runs from \(A_0=b\mathbf1\) at \(0\le b\le B\), with \(b=3B/4\) in the replay. Write \(h=h_*\), \(\kappa=P_{00}\), \(\omega=\max_{i\ne j}(-P_{ij})\), \(\alpha=\min(2,1/(\kappa+\omega))\), and \(Z=I-\alpha P\). Its real circulant column is \(z=Ze_0\), with
\[
  d_0=z_0=1-\alpha\kappa,\qquad
  (z_d)_+\le\alpha\omega\quad(d\ne0),\qquad
  \alpha\omega h\le 1.
\]
Set \(r_k=D-A_k,\ E_k=(r_k)_+\). The exact update and the energy estimate from Round 17 are
\[
  r_{k+1}=Z E_k+\min(r_k,0),\qquad \|E_k\|_2\le\|E_0\|_2 .
\]

The energy can pay for a few coordinates **at the tail scale**, without paying the factor \(h^{1/2}\) of a bulk Cauchy–Schwarz estimate. In fact \(H=y-su\) for \(u=P_\sigma x\), and the [reciprocal metric identity](parallel-transport-15.md#frozen-trials-at-long-ratios) gives \(s\|u\|_2^2\le1-c^2\). Nonnegativity of \(y\) and \(b\ge0\) imply
\[
  \|E_0\|_2^2\le\|D\|_2^2\le ns(1-c^2).
\]
For any cutoff \(t_k\ge0\) and set \(J_k\) of at most \(L\) exceptions, the charge
\[
  Q_k=\frac1h\sum_{i\in J_k}(r_{k,i}-t_k)_+
  \ \le\ \frac{\sqrt L}{h}\|E_0\|_2
  \ \le\ \sqrt{2Ls(1-c^2)}                                           \tag{1}
\]
is uniform in \(k\). The last inequality uses \(h\ge h_J\ge\sqrt q/2\) for \(q\ge9\), since \(\kappa\ge1/2-1/n\). The set can always include the mark and can change with \(k\). Alternatively, one may put every entry with \(E_{k,i}\ge v h\) in \(J_k\): their number is at most \(2s(1-c^2)/v^2\), and their total charge is at most \(2s(1-c^2)/v\). For example \(v=s^{3/4}\) gives \(O(s^{-1/2})\) entries and charge \(O(s^{1/4})\). This controls spikes at scale \(h\); it leaves peaks spread over order \(h\) sites to be treated separately.

## 2. The actual excess follows a scalar recurrence

For each step set
\[
\begin{split}
  e_k&=\mathbf1_{J_k^c}(r_k-t_k)_+,\qquad
  L_k=\|e_k\|_1/h,\qquad C_k=E_k-e_k,\\
  f_k&=ZC_k+\min(r_k,0)-t_{k+1}\mathbf1,\qquad
  T=\operatorname{supp}(e_{k+1}).
\end{split}
\]
The core \(C_k\) includes all exceptional entries and is clipped at \(t_k\) elsewhere. In particular its action includes the actual wave from the mark. Define \(I_k=h^{-1}\sum_{i\in T}(f_{k,i})_+\). If \(e_k\ne0\), use its normalized weights \(w_k=e_k/\|e_k\|_1\) and put
\[
  g_k=\sum_j w_{k,j}\sum_{i\in T}(z_{i-j})_+ .
\]
Take \(g_k=0\) if the source or target is empty. Then
\[
  \boxed{\quad L_{k+1}\le g_k L_k+I_k,\qquad
          h^{-1}T_h(r_k)\le t_k+Q_k+L_k.\quad}                     \tag{2}
\]
On \(T\), \(e_{k+1,i}=(f_{k,i}+(Ze_k)_i)_+\); subadditivity of the positive part proves the first inequality after summing. The second is the order-statistic variational formula evaluated at \(t_k\). It bounds the **signed** upper tail used by the finished correction, although the bound can lose the negative slack below the cutoff.

There is a prospective version using only the current shadow, before applying the signed transfer \(Ze_k\). Since \(d_0\ge\alpha\omega\), the guard
\[
  Y_k=\{i:f_{k,i}+(d_0-\alpha\omega)e_{k,i}
                 +\alpha\omega h L_k>0\}                           \tag{3}
\]
contains \(T\): the expression is an entrywise upper bound on \(f_k+Ze_k\). If a fixed set of exceptions is known to be paid at the next step, it can be removed from \(Y_k\). Replacing \(T\) by \(Y_k\) in both \(g_k,I_k\) is a valid bound. The guard can be much larger than the actual receiving set; the replay measures both. All sums can be computed by FFT and clipping, without an endpoint solve. In particular the inequality is useful with an independent bound on the guard and the core injection, rather than assuming an upper bound on the next tail.

## 3. A weighted Jacobi criterion for transfer

When \(e_k\) and \(T\) are nonempty, let \(\pi_k\) be the probability law of \(i-j\) for independent \(i\) uniform on \(T\) and \(j\) distributed as \(w_k\). Its collision statistic is \(\mathcal E_k=n\sum_d\pi_k(d)^2\), equal to one for uniform differences. Let \(W_d=(z_d)_+/(\alpha\omega)\) for \(d\ne0\), \(W_0=0\), with uniform mean \(m_W\) and standard deviation \(s_W\). For \(0<\nu<1\), use the cap \(\mathcal C_\nu=\{d\ne0:W_d\ge 1-\nu\}\). Since \(g_k=|T|(d_0\pi_k(0)+\alpha\omega\sum_d W_d\pi_k(d))\) and \(|T|\pi_k(0)\le1\), we get
\[
\boxed{\quad
 g_k\le d_0+\alpha\omega |T|
  \min\!\left\{1,\ 1-\nu+\nu\,\pi_k(\mathcal C_\nu),\
                   m_W+s_W\sqrt{\mathcal E_k-1}\right\},\qquad
 \pi_k(\mathcal C_\nu)\le
          \sqrt{|\mathcal C_\nu|\mathcal E_k/n}.
 \quad}                                                          \tag{4}
\]
The bound with the cap splits the off-diagonal coefficients at \(1-\nu\). The bound with the moments is Cauchy–Schwarz after subtracting both uniform means. Either also applies to the guard with its own difference law. The volume bound \(g_k\le d_0+|T|/h\) suffices for small receiving sets; (4) can still give contraction for \(|T|>h\). The weighted rather than worst-column criterion keeps rare differences from deciding the estimate.

For comparison, the two lifts of a nontrivial frequency have conjugate quadratic Jacobi sums, so \(\lambda_d/\sqrt q\) is the real part of a unit normalized Jacobi sum (see [critical sets](critical-sets.md#repeated-differences-are-necessary)). [Xi, Theorem 1.1](https://arxiv.org/pdf/1809.04286) then gives both-sign convergence of \(\omega/\omega_J\) to one and the limiting law \((\cos\theta)_+\) for \(W\) with \(\theta\) uniform. Thus \(d_0\to0\), \(m_W\to1/\pi\), and \(s_W^2\to1/4-1/\pi^2\). For example, \(|T|\le1.2h,\ \mathcal E_k\le2\) gives \(g_k<0.85\) for all sufficiently large orders. At \(|T|\le h\), even a fixed larger bound \(\mathcal E_k\le M\) gives a uniform, possibly weak gap: choose a fixed \(\nu>0\) small enough that \(|\mathcal C_\nu|/n<1/(4M)\) for large orders, using convergence to the cosine law. Then \(g_k\le 1-\nu/2+o(1)\). These character-sum conclusions also hold on squares. The field-dependent question is where the differences of the **actual** peaks land. Global cap counts alone do not bound their mass under \(\pi_k\).

There is an inverse test for a transition that barely shrinks. Suppose \(L_k>0\), \(L_{k+1}\ge(1-\epsilon)L_k\), \(I_k\le\epsilon L_k\), and \(|T|\le(1+\zeta)h\) with \(\epsilon,\zeta\ge0\). Then \(g_k\ge1-2\epsilon\), so (4) gives
\[
  (1+\zeta)\nu\big(1-\pi_k(\mathcal C_\nu)\big)
           \le d_0+\zeta+2\epsilon .
\]
If \(v=d_0+\zeta+2\epsilon<1/2\), take \(\nu=2v>0\) to get cap mass at least \(1/2\). In fact \(|\mathcal C_\nu|/n\ll \sqrt{\nu}+q^{-1/4}\) uniformly: the discrepancy bound from Xi first supplies a phase within \(O(q^{-1/4})\) of either desired extremum, so \(\max_{d\ne0}\sigma\lambda_d/\sqrt q\ge1-O(q^{-1/2})\). Thus the normalized cap condition implies \(\sigma\lambda_d/\sqrt q\ge1-O(\nu+q^{-1/2})\); apply the discrepancy bound again on this arc. Combining with (4) gives
\[
       \mathcal E_k\gg \big(\sqrt{d_0+\zeta+2\epsilon}+q^{-1/4}\big)^{-1}.
\]
So persistence near or below the critical receiving size with little new injection forces a concentrated difference law. Dispersed persistence must use a wider receiving set or a larger injection.

## 4. A sufficient field-first split

Here is one form with a uniform depth, and all hypotheses refer to the actual clipped iteration on each sign. For each sufficiently small fixed \(s>0\), suppose there are integers \(k_0(s),L(s)\), constants \(M(s)<\infty,\ \delta(s)\in(0,1)\), and a scale \(\eta(s)>0\). Assume \(sL(s)\to0,\ \eta(s)\to0\). For all sufficiently large primes suppose:

1. The starting bulk load at depth \(k_0\) is at most \(M(s)\).
2. With at most \(L(s)\) exceptions per row, on the next \(N(s)\) transitions the gain is at most \(1-\delta(s)\) and the core injection is at most \(\delta(s)\eta(s)\). The volume, cap or moment thresholds in (4) can be used in place of a bound on the gain itself.
3. The cutoff at the finishing depth satisfies \(t_{k_0+N}\le u(s)\) for some \(u(s)\to0\).

Choose the window with \(N(s)\ge\delta(s)^{-1}\log^+(M(s)/\eta(s))\), taking at least one step. Iterating (2) gives \(L_{k_0+N}\le (1-\delta)^NM+\eta\le2\eta\). The actual signed tail average is at most
\[
  u(s)+\sqrt{2L(s)s}+2\eta(s).
\]
Products of the actual gains and weighted sums of the injections can replace the uniform hypotheses, by expanding (2). In particular a startup phase with large gains need not be charged at the contraction rate; it does need a bound on its ending load. The positive excess of the Round 17 finish over the available budget is bounded by this same expression, since \(b\le B\). By the [fixed-width theorem](parallel-fixed-width-13.md) and the [endpoint pairing](parallel-repair-17.md#setup-and-explicit-formula), \(a\to1/(1+s)\) at fixed \(s\), and both limiting endpoint marks are bounded below by \(1\) on sending \(s\downarrow0\). Reciprocity then gives the asserted prime asymptotic in Problem 26, **conditional on the split**.

The two inputs beyond gain control matter. At a low cutoff, a positive fraction of the field above the cutoff can already make \(L_{k_0}\) grow. The background can also keep feeding the peaks when the transfer alone contracts. Neither the \(q\)-uniform energy estimate nor an unweighted Jacobi phase count bounds these inputs. The split conditions are sufficient, and can be stronger than necessary for a small signed top-\(h\) tail.

## 5. Exact square control

For \(q=\ell^2,\sigma=+\), the subfield annihilator \(I\) has \(|I|=h=(\ell+1)/2\). On every nonzero difference in \(I\), \(z_d=\alpha\omega\). The choice of \(\alpha\) gives \(d_0=\alpha\omega=1/h\), hence \(Z_{II}=\mathbf1_I\mathbf1_I^\mathsf{T}/h\) on \(I\). If a source lies in \(I\) and \(T=I\setminus J_{k+1}\), its weighted gain is exactly \(|T|/h\), regardless of its weights. Its differences have \(\mathcal E_k\ge n/h\) by Cauchy–Schwarz, and its cap mass is at least \(1-1/|T|\). Removing finitely many exceptions therefore leaves a near-unit gain from the subfield. None of this depends on a limiting optimum of the repair iteration.

In fact for the actual sequence and at **every** \(k\), \(\sum_I A_k=hb\) by complementary support. Consequently
\[
  L_k\ge h^{-1}\sum_{i\in I}D_i-b-t_k-Q_k
     \ge B-b+\frac{a}{m_0^{\rm sq}}-1-t_k-Q_k,\qquad
             m_0^{\rm sq}=h/\sqrt n .
\]
The first inequality uses \((r-t)_+\ge r-t\) on \(I\), subtracting the exception charge. The second is the [square mass obstruction](parallel-repair-17.md#square-comparison-at-every-depth). Since \(a\to1/(1+s)\) at fixed width, this is an order-one lower bound in the square-first, small-width limit for \(t_k+\sqrt{sL}\to0\). It rules out the sufficient split for square plus, uniformly in depth. The square minus side remains a control for a field of square order without this obstruction.

## 6. Replay

The [FFT replay](parallel-tail-18.py) uses the exact Round 17 update with the numerical reciprocal fixed point as input. It checks the transfer recurrence, the phase-cap and moment bounds, guard inclusion and the tail bound at every step. It keeps the mark and the seven largest other cutoff excesses as exceptions in the [main sweep](parallel-tail-18.csv), and keeps only the mark at \(s=1/64\) in the [smaller-width sweep](parallel-tail-18-small-width.csv). Both sweeps run twelve steps with cutoffs \(t=\sqrt{s}/8\) and \(t=B/5\). The comparisons below use \(t=B/5\); the relevant budget is \(B/4\). The CSV's guard bound uses the guard for the bulk recurrence and the measured exception charge. For a prospective bound on that charge use (1). These are floating-point tests of the split, separate from [Round 17's interval certificates](parallel-repair-17-certified.jsonl).

| Order, plus side | Width | Step | Receivers | Actual gain | Difference energy | Actual tail | Split bound | Tail budget |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| \(1000033\) | \(1/16\) | 3 | 595 | 0.39712 | 1.624 | 0.03739 | 0.05393 | 0.03776 |
| \(1000033\) | \(1/16\) | 4 | 129 | 0.08921 | 22.327 | 0.03236 | 0.03416 | 0.03776 |
| \(153649\) | \(1/64\) | 5 | 26 | 0.05950 | 126.519 | 0.00845 | 0.00944 | 0.01052 |
| \(389^2\) | \(1/64\) | 5 | 194 | 0.99487 | 388.000 | 0.38467 | 0.38467 | 0.01390 |

The transfer into depth three at \(1000033,+,s=1/16\) has \(|T|/h=1.189\), so the volume test alone does not show contraction. The cap bound at \(\nu=1/4\) is \(0.96611\), and the centered moment bound is \(0.74276\). At the next step the receiving set shrinks and the volume bound suffices even though the difference law is less flat. The plus-side square receiver at \(389^2,\ s=1/64\) is precisely \(I\setminus\{0\}\) by the reported gain and support check. Its gain is \(194/195\); normalized bulk load stays above \(0.3715\), as opposed to below \(0.00011\) at step five on the nearby prime plus row. The coarse guard is often unhelpful in the first two or three steps on primes, and can cover almost the whole field on square plus rows.

~~~sh
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 \
  .venv/bin/python -B research/parallel-tail-18.py > research/parallel-tail-18.csv
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 \
  .venv/bin/python -B research/parallel-tail-18.py --fixed-only --width 0.015625 \
  --primes 9413 37253 153649 --square-roots 97 193 389 --exceptions 1 \
  > research/parallel-tail-18-small-width.csv
~~~

The next arithmetic target is a depth independent of \(p\) at which the bulk load is bounded, together with a bound on the core positive injection for a subsequent window. On steps with about \(h\) recipients, weighted difference dispersion is a separate, testable way to certify the gain. A prime-aspect theorem for these inputs has not been established.
