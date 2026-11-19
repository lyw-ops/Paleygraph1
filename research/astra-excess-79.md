# Compact triangular and flat windows at a fixed fraction of marked depth

Let \(p\equiv1\pmod4\) be prime, \(n=(p-1)/2\), \(\Lambda=\log_2^*p\), and take the proved marked depth \(D=D(p)\) with a fixed power of marked accuracy greater than two. Put \(d=\lfloor D/4\rfloor\). There are two actual projected profiles on precisely the first \(d\) positive times, one triangular and the other flat. On every bulk coordinate they satisfy
\[
                R_s^\omega+d^{-1}R_{-s}^\nu\ge0.                    \tag{1}
\]
Consequently a supercritical complementary probability must pay order \(D\) in the flat opposite height on the triangular deficit mask. This survives arbitrary deletion of a number of sites growing as a tower of height proportional to \(\log_2^*p\), divided by the squared exterior clipped mass. Both the linear depth and the deletion scale use compact time support. The two profiles in (1) use different weights.

## Endpoint cancellation and the true marks

Use the actual orbit, one-time marks, mean directions and sign projections of [round 69](timed-pinning-69.md). On \(1\le j\le d\) set
\[
 \omega_j=\frac{2(d-j)+1}{d^2},\qquad \nu_j=1/d,\qquad \theta=1/d,
\]
extending both probabilities by zero. For an array \(v\), write \(A_j(v)=(2v_j+v_{j-1}+v_{j+1})/4\) and \(B_j(v)=(v_{j-1}-v_{j+1})/4\). The [bulk identity](relative-window-77.md#paired-rows-with-a-nonnegative-bulk-constant) expresses the projected row as the constant \(c_v=\frac12\sum_j(v_j-v_{j+1})g_j\) plus \(\sum_j[A_j(v)u_{s,j}-B_j(v)u_{-s,j}]\), where \(u_{s,j}=(sY_j)_+\) and \(Y_j=\sqrt n\,v_j^{\rm orbit}\). Both constants are nonnegative. Indeed the sole negative difference is at \(j=0\), every \(g_j\ge g_0=1/\sqrt n\) by the marked activation, and the differences sum to zero.

For either set of weights \(v\) the energy telescope gives
\[
 G_v^2\le\sum_jv_jg_j^2
 =1+\tfrac14[v_1 E_1+\sum_{j=2}^{d}(v_j-v_{j-1})E_j-v_d E_{d+1}]
 \le1+v_1,
\]
where \(G_v=\sum v_jg_j\) and \(E_j=\|v_j^{\rm orbit}\|_2^2\), with \(E_1\le4\). The genuine weighted marks \(m_{s,v}=Z_{s,v}(0)/\sqrt n\) satisfy \(1+o(d^{-1})\) uniformly for these weights by the positive-time marked bound through \(D\). With \(\epsilon=4/d\) the increment \([(1+\epsilon)m_{s,v}-G_v]b_s\) is nonnegative on the bulk for either profile for all sufficiently large primes. It pins the mean to \((1+\epsilon)m_{s,v}\), leaves the true sector and root intact, and adds a bounded bulk constant term. [Marked estimate](vanishing-floor-38.md#1-uniformity-of-the-marked-arithmetic-as-the-floor-vanishes)

Write \(a_j=\omega_j+\theta\nu_j\), \(b_j'=\omega_j-\theta\nu_j\). Then \(b_j'\ge0\), \(a_j=b_{j-1}'\) for \(2\le j\le d\), and \(b_d'=0\). In particular \(a_j\ge b_{j-1}'\) on the full integer line. Four times the coefficient of \(u_{-s,j}\) in the paired row (1) is
\[
 4[\theta A_j(\nu)-B_j(\omega)]
   =(a_j-b_{j-1}')+(a_{j+1}-b_j')\ge0.
\]
Four times the coefficient of \(u_{s,j}\) is \(a_j+a_{j+1}+b_j'+b_{j-1}'\ge0\). The first formula includes the extra endpoint \(d+1\), where the coefficient vanishes exactly. This proves (1).

Let \(r=(R_s^\omega)_-\). We have \(\|r\|_{1,n}\ll1/d\) and \(\|r\|_{2,n}\ll1/\sqrt d\), with normalized counting norms. For the first bound use \(r\le\sum_j B_j(\omega)_+u_{-s,j}\). All positive coefficients are at most \(1/d^2\), while \(\sum_{j=0}^{d+1}g_j\le d+2\) by prefix energy, and the normalized bulk mean of each \(u_{-s,j}\) is at most \(2g_j\). For the second, use the exact projection defect, subtract \(Y_1\) from each first-difference term, and apply \(\|Y_j-Y_1\|_{2,n}\le 2\sqrt{j-1}\). The total variation of these weights is \(2\omega_1\le4/d\). Raw rows and pin increments are nonnegative. [Projection defect and time-shift estimate](smooth-windows-72.md#both-defect-norms-for-the-same-profile)

## A tower-sized family of deletions on the actual mask

Fix \(\delta>0\), \(B\ge0\) with \(B=o(d)\), and a feasible sign-\((-s)\) probability \(q\) with \(\sqrt n q_0\ge1+\delta\). Let \(A\) be any set of at most \(c\sqrt n\) sites with \(c\) sufficiently small, and set \(M_E=\sum_{i\notin A}(q_i-B/n)_+\). Put \(u=\delta/8\). With a sufficiently small \(c_\delta>0\) use the true joint set
\[
 I=\{i\ne0:\ R_s^\omega(i)<-u,\ R_{-s}^\nu(i)>du,\
          c_\delta d<nq_i\le 2C_0\sqrt n M_E\}.
\]
The constant \(C_0\) is that of the [exterior Schur cap](astra-schur-77.md#a-cap-set-by-the-exterior-clipped-mass). Orthogonality gives \(\sum_{i\ne0}q_ir(i)\ge m_{s,\omega}(\sqrt n q_0-1-\epsilon)\). The sites with \(r\le u\) cost at most \(u\) and the low-density sites cost at most \(c_\delta d\|r\|_{1,n}\). The sites above the Schur cap cost \(O(\sqrt{B/d})\) by the capped second-moment estimate. Inequality (1) gives the height threshold everywhere on the remaining deficit mask. Hence \(\sum_Iq_i r(i)\gg_\delta1\).

Write \(T_0=1,\ T_{k+1}=2^{T_k}\) and \(H=T_{\lfloor\Lambda/2\rfloor}\). Then for **every** set \(K\) of at most \(H^2/M_E^2\) sites,
\[
 \sum_{I\setminus K}q_ir(i)\gg_\delta1,\qquad
 \sum_{I\setminus K}q_iR_{-s}^\nu(i)\gg_\delta d,\qquad
 n\sum_{I\setminus K}q_i^2\gg_\delta d.                           \tag{2}
\]
The choice of the largest prices, or any other choice made after seeing both rows and \(q\), is permitted. For this same \(d\), the conclusion also holds whenever \(\log_2^*H\le(3/4-\xi)\Lambda\) for any fixed \(0<\xi<3/4\) and \(H\ge2\).

Indeed the [trimmed-depth bound](trimmed-mellin-77.md#statement) gives \(\log_2^*\max(2,n^{1/4}M_E)\ge\Lambda-O_\delta(1+B)=(1-o(1))\Lambda\). Thus \(M_E>0\) and \(H/M_E\le n^{1/4}\) eventually at every stated scale. The cap defining \(I\) gives
\[
 n\sum_{I\cap K}q_i^2\ll H^2,\qquad
 \sum_{I\cap K}q_i\ll H\sqrt{|K|/n}\ll H n^{-1/4}.
\]
Apply the [actual Mellin approximation](trimmed-mellin-77.md#the-cold-approximation-at-the-shorter-horizon) with step tolerance \(e=(H+D)^{-4}\). The tower base of the dominating recursion has iterated logarithm \(\le\max(\log_2^*H,\log_2^*D)+O(1)\); each time costs one further level. Through \(d+1\), the resulting total is at most \((1-\xi/2)\Lambda\) eventually (using, for instance, \(\xi=1/8\) for the displayed \(H\)). Its resource bound is consequently at most \(\log_2\log_2 p\). The actual marked source at every step is retained. Approximating the bulk positive parts in the finite row using the approximate \(Y_j\), and retaining the pin and constant, gives a bulk function \(F\) of sup norm \(O(1+\log_2\log_2 p)\) with \(\|R_s^\omega-F\|_{2,n,\rm bulk}\ll D(e+p^{-3/8})=o(1/H)\). This uses only Lipschitz positive parts and the bounded sum of the absolute time coefficients. There is no later-time contribution. The price on \(I\cap K\) is therefore bounded by
\[
 \|F\|_\infty\sum_{I\cap K}q_i+
 \|R_s^\omega-F\|_{2,n,\rm bulk}
       \left(n\sum_{I\cap K}q_i^2\right)^{1/2}=o(1).
\]
Here \(H\le\log_2\log_2p\) eventually at the stated scales. Subtract the removed price, use (1), and use the normalized second norm of \(r\) to obtain (2).

The same argument gives a concentration alternative independent of the upper cap inside \(I\). On any subset \(K'\subset I\) with \(n\sum_{K'}q_i^2\le H^2\), its price is \(O((1+\log_2\log_2p)H\sqrt{|K'|/n})+o(1)\). In particular if the entire collision on \(I\) is at most \(H^2\), the actual joint set must contain \(\gg_\delta n/[H(1+\log_2\log_2p)]^2\) sites. This is \(n^{1-o(1)}\) even at the stated tower scales.

## Why an unweighted approximation of the joint indicator does not bound its price

For the separate arithmetic test one can use a soft cutoff \(\ell(x)=\min(1,\max(0,x-1))\). The exact weight \(\ell(r/u)\ell(R_{-s}^\nu/(du))\) equals one where \(r\ge2u\), by (1), and vanishes outside the stated height and deficit tests. Both finite rows have bulk approximants as above. Applying the Lipschitz cutoffs to them approximates this weight to \(o_\delta(1/H)\) in normalized bulk second norm. Bounded real polynomial cutoffs are available at the same precision: approximate positive parts on the bounded intermediate ranges first, then use Bernstein polynomials for each clipped factor on its resulting range. Bernstein averages preserve the range \([0,1]\) of the clipped factors. This involves finitely many additional polynomial operations after the time recursion. On the bulk the mean direction is a constant plus a multiple of the Jacobi column, since its diagonal delta is absent. These operations give bounded combinations of products of the actual approximating Mellin fields, with the two full-character lifts identified at evaluation on \(G=\widehat Q\).

For a proposed bounded test \(f\) on \(G\) extended to the mark, the exact endpoint pairing is
\[
 \sum_i q_i\overline{f(i)}=n^{-1}\sum_{t\in\{1\}\cup D_{-s}}
       \widehat q(t)\overline{\widehat f(t)}.
\]
The transforms here are unnormalized on \(G\). A bulk-only price omits the separate root term. A full character and its quadratic twist give the same frequency on \(Q\), so the transform and its allowed support in this identity are those of the square subgroup. An unweighted moment controls the coefficient at \(t=1\); the other allowed coefficients are still tested against the true endpoint. The bulk price is nevertheless positive, so approximation under the true weighting gives the following alternative even when the global primary collision is arbitrarily large.

## Allowed Fourier correlation or concentrated approximation failure

Fix \(H\) at one of the permitted scales. On the full frequency group construct one nonnegative bounded Mellin test \(f\) from the compact triangular profile, independently of the primary row. Write \(P_i=(r(i)-u)_+\) on the bulk. There are absolute constants in the bound
\[
 \|P-f\|_{2,n,\rm bulk}\le\tau=C D[(H+D)^{-4}+p^{-3/8}],\qquad
 0\le f\ll 1+\log_2\log_2p,\qquad n^{-1}\sum_i f(i)\ll 1/d.
\]
Indeed, before the positive-part operations replace every orbit input by its actual bounded field approximant. On its sup range approximate each positive part to uniform error at most \(e\) by a real polynomial. Using a Bernstein polynomial keeps the output between zero and the largest possible positive part on that interval. On the full group extend the bulk pin by its constant and Jacobi-column terms (omit the diagonal delta). Form the resulting bounded finite linear combination, and apply one last Bernstein approximation of \(x\mapsto(-x-u)_+\) on its range to error \(e\). Each approximation here is pointwise polynomial evaluation on bounded fields; no further cold iteration or projector is applied. The Lipschitz error transfer uses the bounded sum of time coefficients. This produces the asserted nonnegative test with the same bulk accuracy. Its uniform mean bound follows from \(P\le r\), the normalized bulk first norm of \(r\), Cauchy–Schwarz and the single coordinate contribution \(f(0)/n\).

Define a set determined solely by the true cold profiles and the chosen approximant, and a scalar tested on the ordinary primary endpoint,
\[
 E_f=\{i\ne0:r(i)>2u,\ f(i)<P_i/2\},\qquad
 C_q(f)=n^{-1}\operatorname{Re}\sum_{t\in D_{-s}}\widehat q(t)\overline{\widehat f(t)}.
\]
Then \(|E_f|\le 4n\tau^2/u^2\). For all sufficiently large eligible primes either \(C_q(f)\ge\delta/16\), or **every** deletion \(K\) allowed in (2) leaves
\[
 n\sum_{E_f\cap(I\setminus K)}q_i^2\gg_\delta \tau^{-2},\qquad
 \sum_{E_f\cap(I\setminus K)}q_i R_{-s}^\nu(i)\gg_\delta d.           \tag{3}
\]
At the displayed tower choice of \(H\), small allowed correlation forces a tower-scale collision on high-height sites occupying at most \(O_\delta(\tau^2)\) of the full frequency group. The collar \(r>2u\) ensures this set is small in counting measure, with no hypothesis on the distribution of the unweighted profile at an exact threshold.

To prove this, in the derivation of (2) take the low-density price at most \(u\). The original price is at least \(\delta-o(1)\). Paying at most \(2u\) for the initial density and deficit exclusions, \(o(1)\) for the cap and deleted sites, and another \(2u\) for passing to \(P\mathbf1_{r>2u}\) leaves at least \(\delta/3\) of this latter price on \(I\setminus K\). If \(C_q(f)<\delta/16\), Fourier support and the uniform mean bound give \(\sum q_i f(i)\le\delta/12\) eventually. The part of the retained price outside \(E_f\) is at most twice this, by global nonnegativity of \(f\). On \(E_f\), \(P_i\le 2|P_i-f(i)|\), which gives the collision bound by Cauchy–Schwarz. There \(|P_i-f(i)|>u/2\), giving the count. Finally (1) gives the height claim. The estimates permit both alternatives on the same sequence. An upper on the allowed correlation alone leaves the explicit concentration in (3) to control.

## Finite profile check

The [checker](astra-excess-79-check.py) verifies the integer time coefficients through length 512, including both endpoint indices. On four certified complementary even endpoints it then encloses the finite orbit, both true projections, the marked complementary pairing and the minimum paired bulk value using Arb384. For these diagnostics the pin increment is the positive part of the difference between mark factor and mean. The deficit cutoff is 0.01 and no density cutoff is imposed.

| Prime | Length | Deficit sites | Minimum opposite height on deficit sites | Deficit price | Opposite height price |
|---:|---:|---:|---:|---:|---:|
| 101 | 4 | 13 | 1.58549 | 0.09589 | 1.82312 |
| 257 | 5 | 22 | 1.90590 | 0.10757 | 1.67188 |
| 409 | 6 | 44 | 1.15581 | 0.08945 | 1.89910 |
| 769 | 7 | 64 | 1.94723 | 0.06294 | 1.59149 |

Every paired bulk value exceeded 0.16588 across the four cases. The displayed values are rounded summaries of the [outward intervals](astra-excess-79-checks.jsonl).

## Ranked next tests

1. On the compact flat companion, restrict the true primary row to the surviving triangle-deficit and density mask. Test whether its signed height price is \(o(D)\) for one optimizer; the time horizon is deterministic and only \(d+1\) iterates enter the two bulk formulas.
2. For the bounded nonnegative excess test, evaluate the nonconstant allowed correlation against the actual endpoint. An upper below \(\delta/16\) forces the much larger collision in (3) on the explicit underestimate set. To exclude supercriticality in that case, bound its actual surviving collision by \(o(\tau^{-2})\), or show that the retained-diagonal Schur price of that smaller set has a fixed fractional saving.
