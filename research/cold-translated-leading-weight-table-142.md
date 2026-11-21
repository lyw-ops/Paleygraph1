# The two boundary-weight tables on a genuinely translated Jacobi input

Use the same actual leading marked steps \(B_S=K\,\operatorname{diag}(S_i/(2\sqrt{t_i}))\) and \(B_Y=K\,\operatorname{diag}(\alpha Y_i/(2\sqrt{t_i}))\) as in [Round 141](cold-mixed-seed-column-141.md). Here \(S=s_n C_1\), \(s_n=2\sqrt{p/n}\), the actual floor is \(t_0=n\), and all bulk floors lie in the original closed cold square. Let \(X_\xi\) be the translated \(C_1\) column, whose position row is \(s(x)\xi(x)/\sqrt p\) on the squares. Choose the sign of \(\xi\) according to the Fourier convention. Its added pair of full Mellin twists is the corresponding pair from \(\xi,\chi\xi\), with inversion of both characters if needed. Suppose this pair is disjoint from the base pair.

There is one copy of the translated source in each term of the full action. With uniform bulk factors the unscaled bracket is exactly
\[
 K\bigl[Y K(C_1X_\xi)\bigr]+K\bigl[C_1 K(YX_\xi)\bigr].
\]
The outer seed multiplier is the unshifted \(C_1\). Thus only the base and the single translated pair occur, and there is no pair from \(\xi^2\). The geometric product for either order uses the independent full lifts of its three original factors.

## Weight table

The table gives the folded masses \(h_k\) at the base pair, averaging its two fibers, for the two equally weighted phase cases of each order. Zero weights are excluded from \(h_k\). In every case the off-base folded measure has mass two at \(k=1\), with off-base first moment \(b=2\).

| Order in time | Phase case | \(h_1\) | \(h_2\) | \(h_3\) | Base first moment |
| --- | --- | ---: | ---: | ---: | ---: |
| seed then \(Y\) | same active fiber | 1 | 0 | 1 | 4 |
| seed then \(Y\) | different active fibers | 2 | 2 | 0 | 6 |
| \(Y\) then seed | same sign at active negative fiber | 3 | 0 | 1 | 6 |
| \(Y\) then seed | opposite sign at active negative fiber | 4 | 0 | 0 | 4 |

For the computation, the unshifted Jacobi line has a single weight in each base fiber, with opposite weights \(-1,+1\). The translated Jacobi line has the analogous weights in the translated pair. The Legendre factor has weights \((-2,2)\) in one base fiber and two zeros in the other. The full-lift choices choose each phase independently. For each fixed fiber, multiplication convolves its weights. Transport by \(K\) retains negative weights and exchanges positive weights between the two fibers in each pair. It keeps the pooled nonzero measure and fills the remaining fiber weights at zero in the new dimension. These are the [actual two-pair weight rules](shifted-resolvent-96.md#the-two-estimates-for-one-physical-derivative-step) and the [Legendre weights](astra-signed-54.md).

If the seed acts first, the first output has dimension two. In each pair it has \((-1,1)\) in one fiber and zeros in the other. On the base pair, the next Legendre factor either has its nonzero weights at the same fiber, giving \((-3,-1,1,3)\), or has them at the other fiber. In the latter case the two fibers give \((-1,-1,1,1)\) and \((-2,-2,2,2)\). This proves the first two rows. If \(Y\) acts first, that output has dimension four. In the base pair its two fibers carry \((-2,0,0,0)\) and \((2,0,0,0)\), and at the translated pair the nonzero weights are \((-1,-1,1,1)\) in one fiber. The next Jacobi line shifts each base fiber by \(+1\) or \(-1\), with opposite shifts in the two fibers. At the fiber containing \(-2\) the shift is either \(-1\), giving one absolute weight three and three of size one, or \(+1\), giving four of size one. The other fiber is symmetric. This proves the last two rows. The quoted off-base measure follows in both orders because the unshifted factors have only zero weights in that pair.

## Physical comparison on this source

For either order the averaged base first moment is five and off-base moment is two. Since \(\pi(k)\le2k\), the sum of both outputs has comparison price at most \(20+4\Lambda\) before its common factor \(\alpha s_n/(4t)\). The exact geometric columns above omit only finite lift discrepancies on the two quotient coordinates. In each step these give bounded multiples of the appropriate \(Ke_0,Ke_a\), uniformly in the added pair. The marked denominator changes the multiplier only at zero and is priced the same way. Each adjacent selected step has bounded price for fixed \(\Lambda\); hence the total omitted cost is \(O_\Lambda(n^{-1/2})\) uniformly on this source. [Physical lift and mark repairs](shifted-resolvent-96.md#the-two-estimates-for-one-physical-derivative-step)

With \(\Lambda=5000\), the actual \(|\alpha|<1\), \(s_n<2.829\) eventually and \(\Re t>15.8\), the displayed sum costs less than \(0.180\,\Lambda\) for all sufficiently large eligible primes, with uniform slack. Here \(\Lambda\) is the canonical representation price of the input, so this is a comparison for the selected mixed action on these translated Jacobi columns. It is not an operator-norm estimate on the entire packet class. The table records weights, and does not decide equality of full arithmetic labels within the equal-rank cases. It leaves the all-order nonlinear and remaining linear mixed terms open.

## All pure Jacobi powers with one linear Legendre insertion

Let \(D^{\rm J}_i=d_{t_i}(S_i)\), \(D^{\rm L}_i=\alpha Y_i d'_{t_i}(S_i)\), and \(d_t(v)=v/\sqrt{4t+v^2}\), with the actual \(t_0=n\). On the same canonical input consider \((KD^{\rm J}KD^{\rm L}+KD^{\rm L}KD^{\rm J})X_\xi\). Put \(u=s_n/(2\sqrt{|t|})\), \(z=u^2\), and \(q_k=4^{-k}\binom{2k}{k}\). The bulk series have absolute coefficients \(u q_kz^k\) and \(|\alpha|(2k+1)q_kz^k/(2\sqrt{|t|})\) in \(C_1^{2k+1}\) and \(C_1^{2k}Y\). Their geometric dimensions are one and two, and their averaged base moments are bounded by \(2k+1\) and \(4k+2\). For the second moment bound, \(Y\) begins with base moment two and the \(2k\) Jacobi shifts each have magnitude one. Thus the absolute dimension and moment majorants \(m,a\), using \(|\alpha|<1\), are
\[
 m_{\rm J}=\frac{u}{\sqrt{1-z}},\quad a_{\rm J}=\frac{u}{(1-z)^{3/2}},\quad
 m_{\rm L}=\frac{1}{\sqrt{|t|}(1-z)^{3/2}},\quad
 a_{\rm L}=\frac{1+2z}{\sqrt{|t|}(1-z)^{5/2}}.
\]

Write \(A,b\) for the unpriced base and off-base first moments. A negative term has dimension \(A+b\). At the base pair, convolution and the triangle inequality give \(A'\le (m+a)A+ab\). At the added pair the multiplier has only zero weights, so \(b'\le mb\). In each case transport preserves the pooled absolute weights. This is the even-product rule applied to the negative input and a word with an odd number of negative factors. Both orders start at \((A,b)=(0,1)\), and their combined price divided by \(\Lambda\) is bounded by
\[
 2m_{\rm J}m_{\rm L}+\frac{4}{\Lambda}
 (a_{\rm J}m_{\rm L}+a_{\rm L}m_{\rm J}+a_{\rm J}a_{\rm L})
 +O_\Lambda(n^{-1/2}).
\]
Each step is bounded on the two-pair price class by the same inequalities. Round 96's two lift repairs sum absolutely, since their cost is proportional to dimension times absolute coefficient. The bounded marked-only differences give multiples of \(Ke_0\). These facts give the uniform error on the actual block by truncation followed by absolute summation.

Eventually \(u<.356\), \(z<.127\), \(\sqrt{1-z}>.934\), and \(|t|^{-1/2}<.252\) on the square. At \(\Lambda=5000\) these rational comparisons give \(6341456334752/26870932156095<.236\) before the repair. Hence the selected full Jacobi block costs less than \(.237\Lambda\) eventually. This is an absolute comparison on the canonical disjoint translated input. Generic arithmetic label equality and the rest of the analytic derivative remain open.
