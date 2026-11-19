# Thirty true marked returns on the common disk and a wider stationary rectangle

Put \(a=2031/128\), \(D_r=\{|t-a|<r\}\), and \(n=(q-1)/2\) for eligible primes or prime squares. For \(n\ge10^{14}\), the actual seed Picard orbit on \(D_{1/4}\) satisfies \(\|V_4\|_\infty<3.938\) and \(\|V_j\|_\infty<5\) for every \(0\le j\le30\). On \(D_{1/128}\) the cap 5 holds through step 64. All these estimates include coordinate zero with its actual activation. They improve the fourth-coordinate bound 6.37 in [round 74](astra-reachable-74.md).

The actual stationary branch is holomorphic on the **whole** respective disks for the finite size ranges below. For unbounded field size a different argument proves \(|m_q|\le3/\sqrt n\) on the union of the following two open rectangles, where the horizontal interval is given in units of \(2^{-20}\).

| Horizontal interval in units of \(2^{-20}\) | Imaginary half-width | Real slices |
|---|---:|---:|
| \((16640296,16640308)\) | \(2^{-10}\) | 12 |
| \((16640292,16640308)\) | \(2^{-11}\) | 16 |

The previous [round-64](astra-joint-64.md) lower edge is \(16640304/2^{20}\). The wider rectangle increases the imaginary half-width on the overlap by a factor 1024. The other lowers the real edge by \(12/2^{20}\). The center \(a=16637952/2^{20}\) is outside the two new rectangles. The center's all-prime stationary continuation and the ordinary cold theta limit remain open.

## The true full-site iterations

Write \(S=sX=2\sqrt n K e_0\), \(s=2\sqrt{q/n}=\sqrt{8+4/n}\), and \(F_t(x)=\sqrt{4t+x^2}\). Denote the coordinatewise activation with \(t\) replaced by \(n\) at zero by \(\Phi_t\). Then \(V_0=S\), \(V_{j+1}=K\Phi_t(V_j)\). With \(R_j=V_j-S\), the exact recursion reads
\[
 R_{j+1}=K F_t(S+R_j)+
  [F_n(V_{j,0})-2\sqrt n-F_t(V_{j,0})]K e_0 .
\]
The absolute normalized Jacobi mass of \(Ke_0\) is \(\sqrt q/n\) in the first packet. All the roots are the power-series branches that are positive on positive real floors.

For each of the first 14 even powers of the binomial series for \(F_t(sX+y)\), expand in \(T_k(X)y^j\) and **add coefficients with the same \((j,k)\) before taking moduli**. For fixed \((j,k)\) use the common upper envelope across a rectangular subdivision of the square circumscribing the disk. Conjugation permits computing just its upper half. The [pooled Mellin rule](astra-feedback-52.md) convolves the input packet distribution \(j\) times with the symmetric weight shift \(\pm k\). Each preactivation atom pair of total coefficient \(h\) at \(\pm d\), \(d>0\), becomes \(h Q_d\) where \(Q_d=(\delta_{-d}+\delta_d)/2+(d-1)\delta_0\). The output mass is a coordinate cap in the physical trace representation. The [16-packet calculation](astra-histogram-53.md) charges both mass and second moment for all higher packets and every descendant involving them. The unexpanded binomial orders from 30 onward use the same geometric mass and second-moment tails with \(r=(s+b)^2/(4\inf |t|)\), where \(b\) is the incoming feedback mass bound. All packet computations here use auxiliary radius one.

For explicit finite-size bounds, when \(s+b<5\) the absolute coefficient sum prior to transport, with each arity charged by \(b^j\), is at most
\[
  2\sqrt{\sup|t|}\bigl(2-\sqrt{1-r}\bigr)<17 .
\]
This follows by taking the raw powers before Chebyshev collection. The [uniform two-character correction](marked-domain-53.md) costs at most twice this coefficient sum times \(\sqrt q/n\) in the first packet, at all orders. The displayed marked discrepancy costs at most \(11\sqrt q/n\), since \(|F_n(x)-2\sqrt n|\le25/(2\sqrt n)\) by rationalization and \(|F_t(x)|\le\sqrt{4\sup|t|+25}\). For \(n\ge10^{14}\), \((34+11)\sqrt q/n<10^{-5}\). The checker adds this whole allowance to packet one after **every** step. The positivity of the cap propagation and absolute convergence extend the finite monomial bounds to the exact nonlinear activations. The seed enclosure contains every actual \(s\) in this size range.

There is a shorter rational proof of the fourth cap alone. Use \(s<2.83\), \(4|t|>62.4\), \(2\sqrt{|t|}<8.1\), and let \((b,c)\) enclose the feedback mass and second weight moment. At Taylor orders \(2\ell=2,4\), for each \(0\le j\le2\ell\) and \(0\le v\le(2\ell-j)/2\), put \(k=2\ell-j-2v\), \(A=b^j\), \(J=jcb^{j-1}\) (zero at \(j=0\)). The positive rational coefficient before transport is bounded by
\[
 W=8.1\,|\tbinom{1/2}{\ell}|\,62.4^{-\ell}\binom{2\ell}{j}
        (2.83/2)^{2\ell-j}\binom{2\ell-j}{v}(1+\mathbf1_{k>0}).
\]
Multiply by \(k^2A+J\) for the moment and by \(\min((k+j)A,kA+J/(4k))\) for the mass, omitting the second option when \(k=0\). Indeed the paired seed signs give \(\max(k,|w|)\le k+w^2/(4k)\). All later orders have binomial magnitude at most \(1/16\). Put \(r=(2.83+b)^2/62.4\); add \((8.1/16)\sum_{\ell\ge3}r^\ell(2\ell)\) for the mass and \((8.1/16)\sum_{\ell\ge3}r^\ell(4\ell^2+2\ell c/b)\) for the moment, with \(c/b=0\) at the zero input. These bounds use the triangle mass estimate and the second moment of additive convolution. Each tail is rational by differentiating the geometric series. Adding \(10^{-5}\) to both outputs for the true corrections gives, starting at zero, successive strict upper pairs
\[
       (0.56,1.16),\quad (0.96,2.14),\quad(1.35,3.21),\quad(1.82,4.73).
\]
Consequently \(\|V_4\|_\infty<2.83+1.82=4.65\) already follows by ordinary inequalities and rational arithmetic. The full packet calculation improves this to 3.938.

Let \(d_j=n^{-1/2}\|V_j-V_{j-1}\|_2\). If adjacent inputs lie in \(|x|\le M\), \(|\Im x|\le b\), on their entire coordinatewise segments, then with \(L=\inf\Re t\)
\[
 |F_t'(x)|\le \frac{M}{\sqrt{4L-2b^2+M^2}}
 \quad (4L>2b^2).
\]
Indeed \(\Re(4t+x^2)\ge4L+|x|^2-2b^2\) and the resulting bound increases with \(|x|\). The same inequality holds at the large marked floor. Since the seed is real, a feedback mass bound \(b\) gives the required imaginary cap as well as \(M=s+b\). Use running upper bounds to enclose both inputs. Counting contraction of \(K\) then propagates \(d_j\) from the first feedback mass. At real \(t\) one may set the imaginary cap in the derivative to zero.

| Disk radius | Depth \(h\) | \(\|V_4\|_\infty\) | \(\|V_h\|_\infty\) | Real \(d_h\) | Whole-disk stationary range for \(n\) |
|---|---:|---:|---:|---:|---:|
| \(1/4\) | 30 | \(<3.938\) | \(<4.960\) | \(<4\cdot10^{-10}\) | \([10^{14},10^{16}]\) |
| \(1/128\) | 64 | \(<3.911\) | \(<4.977\) | \(<14\cdot10^{-21}\) | \([10^{14},10^{36}]\) |

In each listed finite interval the *complex* derivative product certifies \(d_h\sqrt n<1/4\). Within the closed counting ball of radius \(1/2\) about \(V_h\), all coordinates have modulus at most 5.5 and imaginary part at most 2.7. The same bounds enclose the segment from \(V_{h-1}\) to \(V_h\). The displayed derivative is then less than \(2/3\). Thus the residual at \(V_h\) is below \(1/6\), the ball maps into itself, and locally uniform Picard convergence gives the holomorphic fixed point for each such field. Its factors on the real interval are positive, since \(\Phi_t(V)_i>|V_i|\) for a real fixed point, and identify the physical germ. The mark \(m_q=\operatorname{arsinh}(V_0^{\rm stat}/(2\sqrt n))\) has modulus at most \(3/\sqrt n\) there, using \(\|V^{\rm stat}\|_\infty\le5.5\) and the derivative bound for the inverse hyperbolic sine near zero. The size ranges follow from scalar inequalities for every eligible field in the intervals; there was no enumeration of fields.

At real floors there is also an unconditional stationary-*tolerance* consequence for unbounded field size. Use the strictly positive trial factors \((\Phi_t(V_{h-1})\pm V_h)/(2\sqrt n)\). They belong to the physical complementary spaces with equal means, so they are stationary for their product weights. The bulk products multiplied by \(n\) are \(t+(V_{h-1,i}^2-V_{h,i}^2)/4\ge t-25/4\). The marked product is \(1+O(1/n)\), and its trial mark is \(O(n^{-1/2})\). After scaling by the marked product the counting distance between the two bulk square-root weight rows is at most
\[
 \frac{10d_h}{4(\sqrt{L-25/4}+\sqrt L)}+O(n^{-1})<0.4d_h+O(n^{-1}).
\]
The [marked square-root weight inequality](marked-response.md) gives a uniform limsup of \(|m_q|\) at most \(1.6\cdot10^{-10}\) on the wider disk's real interval and \(5.6\cdot10^{-21}\) on the narrower one. A fixed positive tolerance alone gives no decay rate as \(n\to\infty\).

## The common stationary rectangles for unbounded field size

Use the nine-center seed and its complete degree-28 upper kernels from [round 65](astra-joint-65.md). To the seven-center seed this adds \(v(U+U')\), the two rank-four symplectic outputs of the fourth Jacobi mode. The exact preactivation amendment is \(-2v T_4(X)\) together with its bounded exceptional coefficient on \(Ke_0\). In particular the coefficient \(2(1-8/q+7/q^2)\) in the round-65 transport identity is retained with its corresponding signed coefficient. The two added objects together have the same weight measure \(6\delta_0+\delta_4+\delta_{-4}\) and dimension eight as the old dual pair together. Consequently, for the untouched analytic tail and the physical coordinate cap, one can feed \(|w|+|v|\) into the old dual-pair slot. The degree-28 kernels themselves use the new subtraction and translation in full. The older exceptional corrections, including the mark, remain in packet one.

On closed real slices of width \(2^{-20}\) and the listed closed imaginary bands we enclose every polynomial upper kernel and each distinguished amplitude. The replay takes the componentwise envelope over each family of slices. Apply the [round-64 weighted invariant](astra-joint-64.md) with \(\eta=1/5\), 50 frozen integer packet caps in units \(10^{-14}\), and weighted residual allowance \(\epsilon=10^{-7}\). The zero atom from the residual costs at most \(2.8\epsilon\); the inherited \(10^{-8}\) safety term is included. The off-zero excess, with mixed residual descendants and the entire analytic tail, is below \(81\cdot10^{-9}\) and \(98\cdot10^{-9}\), respectively. Both are strictly below \(\epsilon\). The coordinate bounds are below 4.654. The uniform \(O(n^{-1/2})\) first-packet discrepancies fit in the strict slack for all sufficiently large fields. Iterating from the nine-center seed now gives exact physical updates inside this invariant. The bulk and marked derivatives are below \(3/4\) on the full coordinate disk. The locally uniform limit identifies the same stationary branch by positivity on the real overlap. This proves the two common rectangles.

[Replay code](astra-fourth-75-check.py) · [One rational and four interval records](astra-fourth-75-checks.jsonl). The orbit, contraction, and identification arguments are ordinary inequalities using previously established arithmetic transport identities. The independent two-moment fourth-step bound uses rational arithmetic. The inequalities in the tables and the two weighted invariants use outward-rounded Arb enclosures at 160 and 192 bits. Floating fits proposed the 50 rational caps on each rectangle. Only the frozen integers enter the verification. There are no new exact finite-field enumerations.

1. At \(a\), seek a signed multi-level invariant for the whole residual. The unbounded-size rectangle proof supplies an actual branch for comparison; the known one-vertex escape at \(a\) persists for this nine-center choice. Any candidate should certify the weighted complement including the fourth-mode exceptional column and the physical mark.
2. On the wider disk, bound the true signed activation beyond step 30, or certify a single holomorphic predictor with counting residual \(<1/6\) inside the displayed contraction tube. A logarithmic horizon with constants uniform in the field size would remove the finite upper size restriction. The 64-step result concerns the smaller disk.
