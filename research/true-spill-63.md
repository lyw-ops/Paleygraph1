# Signed pinned repair on the actual zero-floor orbit

For the unrounded zero-floor Picard orbit, the pinned reflection completes both prescribed marks at \(p=9413\) with extra scaled mean \(4/(3T)\), and at \(p=153649\) with \(3/(2T)\). Each check uses the depths \(T=32,64,128\). The signed worst-site test succeeds even though the absolute coherence envelope cannot certify the chosen allowance. In each sign and at each of those depths one fixed site rules out the same reflection simultaneously for every allowance \(0\le s\le1/T\). At the square order \(97^2\) the exact complementary theta value gives a lower bound on the mean needed by **any** nonnegative completion of the minus row's actual mark. These are finite interval results on the mathematical orbit.

## The signed and absolute tests

Write \(n=(q-1)/2\). Take the true zero-floor orbit \(v_0=0\), \(v_{j+1}=K\phi_j\), with \(\phi_j(0)=\sqrt{4+v_j(0)^2}\) and \(\phi_j(i)=|v_j(i)|\) for \(i\ne0\). Let \(X_{\sigma,T}\) denote the unscaled [round-35 average](averaged-mark-35.md), \(Z=\sqrt n X_{\sigma,T}\), and \(G\) its mean. For the sign \(\sigma\) put \(P=P_\sigma\), \(\ell=Pe_0\), \(a=\ell(0)\), \(L=P-\ell\ell^{\mathsf T}/a\), and \(b=\mathbf1-\ell/a\).

For an extra scaled mean \(s\), set \(Y=Z+sb\), \(d_0=0\), \(d_i=(s/4-Y_i)_+\) off the mark, and \(R=2L-I\). The true repaired row is
\[
 F=Y+2Ld=Y+d+Rd .
\]
It has mark \(Z(0)\), mean \(G+s\) and Fourier sector \(\sigma\) exactly. For bulk sites, \(Y+d\ge s/4\), so the one-sided spill condition \(\min_{i\ne0} (Rd)_i\ge-s/4\) suffices for nonnegativity when the original mark is positive. The signed spill in the checker is
\[
 (Rd)_i=\sigma(Kd)_i-\overline d-2\ell_i\langle\ell,d\rangle/a .
\]
For comparison the absolute envelope is \((2b_J+2b_J^2/a)\sum_i d_i\), where \(b_J=(1+\sqrt q)/(2n)\). The certificate encloses this *envelope* from below and proves it exceeds \(s/4\) at all accepted prime inputs. This comparison only rejects use of that absolute sufficient test on the same inputs. [Pinned reflection and absolute envelope](astra-conic-primal-34.md) · [Signed spare mean](astra-positive-39.md#1-a-positive-completion-with-an-explicit-price-at-each-time)

## Whole intervals of failing reserves

For any fixed site \(i\ne0\), define \(u=Ts\). Its exact tested value times \(T\) is
\[
 T F_i(u/T)=T Z_i+b_i u+
     \sum_{j\ne0}2L_{ij}\big(-T Z_j-(b_j-1/4)u\big)_+ .
\]
Here \(b_j>1/2\) off the mark in all the tested fields. This is a piecewise affine function of \(u\). In a bounded nonnegative interval of \(u\), replace each signed hinge by an outward upper hinge using the interval endpoints of the coefficient, height and slope. If the coefficient upper endpoint is nonnegative, use the upper height and lower positive slope. If it is negative, use the lower height and upper slope. In both cases the coefficient itself is replaced by its upper endpoint. This is a pointwise upper bound, including at an undecided hinge or coefficient sign. All substituted numbers are exact dyadics. Sort their positive breakpoints inside the reserve interval as rational numbers and check the two ends and each breakpoint. The resulting upper bound is valid for every real reserve in the interval. The checker selects a site from the right endpoint and certifies the entire interval at that site, without assuming that the repaired row depends monotonically on the reserve.

At the square order the exact minus theta is \((\sqrt q+1)/2\). A nonnegative minus row of scaled mean \(G+s\) has marked entry at most \((G+s)(\sqrt q+1)/2\). Hence every completion preserving the given mark needs
\[
 s\ge \frac{2Z(0)}{\sqrt q+1}-G.
\]
This lower bound is attained if positive, by scaling a mean-one minus optimizer to the prescribed mark. Thus the obstruction applies to arbitrary corrections in the same sector. [Square endpoint values](square-order-control.md)

## Norm shadowing of the unrounded input

The FFT in ordinary floating arithmetic supplies only a rational trial trajectory in the format of the [earlier orbit certificate](harmonic-orbit-27.md#1-norm-shadowing-avoids-exploding-coordinate-intervals). Consecutive centers have denominator \(2^{60}\). The interval transforms enclose the exact image of each center with the true zero-floor activation. Since that map is Euclidean nonexpansive, the sum of local Arb norm bounds encloses the counting Euclidean error of the whole actual trajectory. The hash in each record identifies its rational prefix. The exact DFT sign masks come from the prime or square field routines.

To form the average with one further transform, put
\[
 S_T=\tfrac14\Big(2\sum_{j=1}^T\phi_j+\phi_0-\phi_T\Big) .
\]
The exact sum and difference identities give
\[
 T X_{\sigma,T}=S_T+\sigma K S_T
      +\tfrac14(\overline{\phi_T}-\overline{\phi_0})\mathbf1 .
\]
Write \(e_j\) for the counting norm shadowing error at time \(j\). The activation error is at most \(e_j\). The trapezoidal weights give error at most \(\sum_{j=1}^T e_j/2\) in \(S_T\). Applying \(I+\sigma K\) at most doubles this bound. The constant term adds counting norm at most \(e_T/4\). The checker therefore encloses every entry of \(T Z\) with this norm error multiplied by \(\sqrt n\), in addition to the outward transform error. It then encloses the hinges, pinning term and actual reflected row. The sectors and the marked preservation are exact from the projector identity, while numerical identities in the replay check the normalization.

| Field | Verified extra scaled mean on both signs | Lowest successful \(T(\min_{i\ne0}(Rd)_i+s/4)\) | Uniform upper bound at the failing site for \(0\le s\le1/T\) on \(TF_i\) |
| --- | ---: | ---: | ---: |
| \(9413\) | \(4/(3T)\) | \(>0.035\) | \(<-0.166\) |
| \(153649\) | \(3/(2T)\) | \(>0.107\) | \(<-0.245\) |

At \(97^2\), the plus row passes with \(3/(2T)\), and the minus completion of any kind requires extra scaled mean strictly above \(0.337\) at the three tested depths. The ratios recorded on the finite primes are lower bounds for the corresponding theta signs. Ordinary complementary reciprocity yields the other interval endpoint at each field. The table concerns finite tested integers. The [checker](true-spill-63-check.py) and [18 records](true-spill-63-checks.jsonl) retain the signed spill, the absolute envelope and the square bound separately.

## A necessary whole-prefix energy bound for order \(1/T\) allowance

Consider an actual zero-floor pair through any sequence in the proved marked window with \(T\to\infty\). Put \(g_j=\sqrt n\mu_j\), \(E_j=\|v_j\|^2\), and \(G=T^{-1}\sum_{j=1}^Tg_j\). If both original marks can be completed by any nonnegative rows with common scaled mean \(G+s\), the complementary pairing and the inherited marked bounds give \(G+s\ge1-o(T^{-1})\). One can take the log-star constant for any fixed inverse-power accuracy greater than two. This uses the exact condition \((G+s)^2\ge X_{+,T}(0)X_{-,T}(0)\). No restriction on the choice of correction is imposed in this paragraph.

Keeping the full terminal term in the [exact mean identity](vanishing-floor-38.md#2-a-necessary-mean-margin-at-the-true-marks) gives
\[
 2Ts+o(1)\ \ge\ 2T(1-G)
 =\sum_{j=1}^T(1-g_j)^2+\frac{E_{T+1}-E_1}{4}.
\]
The last energy difference is at least \(-o(1)\) uniformly in the window, since the marked summand alone gives \(E_{T+1}\ge(2-2\mu_T)^2\) for large fields and \(E_1=4(1-1/n)\). Thus \(P_T=\sum_{j=1}^T(1-g_j)^2\le 2Ts+o(1)\) and \(E_{T+1}\le E_1+8Ts+o(1)\). Moreover, for \(1\le a\le b\le T\), the same energy telescope between times \(a,b+1\) and Cauchy--Schwarz give
\[
 |E_{b+1}-E_a|\le8\sqrt{(b-a+1)P_T}+4P_T.
\]
Here \(1-g_j^2=2(1-g_j)-(1-g_j)^2\). In the upper direction from the start the negative quadratic term can be dropped, giving \(E_{b+1}\le E_1+8\sqrt{bP_T}\). In particular \(s\le C/T\) with fixed \(C\) requires a bounded terminal energy and bounds the maximum energy throughout the prefix by \(O_C(\sqrt T)\). It also requires an \(O_C(1/T)\) normalized \(L^2\) negative-part bound at the selected endpoint by the [exact projected endpoint formula](astra-positive-39.md#1-a-positive-completion-with-an-explicit-price-at-each-time). These estimates give independent rejection tests for an order \(1/T\) budget when either the terminal energy or the sum of squared mean errors is unbounded along the selected schedules. They give no sufficient worst-site estimate.


The sum \(P_T\) is increasing in \(T\). To reject a fixed \(C/T\) allowance throughout the late window on a prime sequence, it suffices to prove on that sequence a lower bound exceeding \(2C\) already from a fixed prefix \(1,\ldots,L\). Eventually \(D(p)/2\ge L\). If the lower bounds obtainable this way grow without bound as \(L\) grows, every fixed \(C\) is excluded along that sequence. This is a finite-depth limit test with the field limit taken before increasing \(L\).

For varying floors \(0\le\tau\le1\), the same proof replaces \(2Ts\) in the budget by \(2Ts+T(1-1/n)\tau\). The energy increment on an interval of \(k\) times has the additional term \(4k(1-1/n)\tau\). In particular the bounded terminal energy, bounded sum of squared mean errors and \(O(\sqrt T)\) prefix energy conclusion all hold for a successful allowance when both \(Ts\) and \(T\tau\) are bounded.
