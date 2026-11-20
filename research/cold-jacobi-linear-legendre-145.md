# A contracting selected Jacobi and linear Legendre block on the cold square

Let \(D^{\rm J}_i=d_{t_i}(S_i)\) and \(D^{\rm L}_i=\alpha Y_i d'_{t_i}(S_i)\), with \(d_t(v)=v/\sqrt{4t+v^2}\), \(S=s_n C_1\), \(s_n=2\sqrt{p/n}\), and \(|\alpha|<1\) as in [the actual mixed action](cold-mixed-seed-column-141.md). The square is centered at \(2031/128\) with real and imaginary halfwidth \(2^{-17}\), and \(t_0=n\) at the mark. Use the \(P_{5000}\) class of [Round 96](shifted-resolvent-96.md#the-two-estimates-for-one-physical-derivative-step), with the base pair and at most one added pair, including the unshifted class. Uniformly in those data and for all sufficiently large eligible primes,
\[
 \|K D^{\rm L}\|_{P_{5000}}<0.487,\qquad
 \|K(D^{\rm J}+D^{\rm L})\|_{P_{5000}}<0.959.
\]
The statements refer to the actual finite-field diagonal multipliers. The second comparison adds both positive column-price bounds before taking a supremum over the input weight. It does not use cancellation between different arithmetic factors. This improves the result on a canonical input to a price on the whole specified packet class.

Combining the first bound with the [actual pure Jacobi rate](cold-pure-seed-134.md) gives
\[
 \|KD^{\rm J}KD^{\rm L}+KD^{\rm L}KD^{\rm J}\|_{P_{5000}}<0.515.
\]
In particular it applies to the canonical unshifted \(C_1\) of price at most one. The selected one-step sum has square rate below \(0.920\). Higher powers in the Legendre insertion, other physical centers, the nonlinear invariant and the original marked continuation are outside these estimates.

## Bulk coefficients and the marked restoration

Use \(z=s_n^2/(4t)\), \(u=s_n/(2\sqrt t)\), \(v=1/(2\sqrt t)\), and \(b_k=4^{-k}\binom{2k}{k}\). The two diagonal expansions before \(\alpha\) are
\[
 u\sum_{k\ge0}(-1)^k b_k z^k C_1^{2k+1},\qquad
 vY\sum_{k\ge0}(-1)^k(2k+1)b_k z^k C_1^{2k}.
\]
The complex factors appear here before absolute values. Truncate both sums at \(k=5\). In \(C_1^d\), the harmonic coefficient at positive \(j\equiv d\pmod2\) is \(2^{1-d}\binom{d}{(d-j)/2}\), and at zero it is \(2^{-d}\binom{d}{d/2}\) for even \(d\). The same harmonic is a common Jacobi line and its dual through all retained orders. Pool its signed polynomial coefficient at \(z_\ast=0.12605\), then add a bound on its variation before taking its contribution to the fiber measure. The exact check uses \(|z-z_\ast|<10^{-5}\), \(|z|<\rho=0.1261\), \(|u|<0.356\) and \(|v|<1/7.96\) for \(n\ge10^8\). From \(s_n^2/4=2+1/n\) and \(|t-2031/128|\le2\cdot2^{-17}\), these are rational inequalities, with a squared comparison for \(|u|\) and \(|v|\). The variation of each \(z^k\) is bounded by \(k\rho^{k-1}10^{-5}\).

A harmonic \(C_j\) gives symmetric mass at \(\pm j\), of total one. In the linear Legendre multiplier convolve this measure with the measure of \(Y\), which is one mass at zero and half a mass at each of \(\pm2\). Independence here is of the two full lift choices, not a probabilistic hypothesis about trace values. In each fixed fiber the \(Y\) lift average weights the two lists \(0^2\) and \((-2,2)\) equally. This can therefore act as a symmetric multiplier against either full input fiber. At the extra pair it has only zero weights. This accounts for the constants as well as the nonzero harmonics.

For a folded multiplier majorant \(h_k\), including \(h_0\), set \(m=\sum h_k\) and \(\nu=\sum h_k\pi(k)\). Base source columns of weight \(j\ge1\) have rate
\[
 \frac{(j-1)\nu+\sum_k h_k\bigl(\pi(j+k)+\pi(|j-k|)\bigr)/2}{\pi(j)},
\]
and an off-base column has rate \(m+\nu/5000\). Once all the arguments of \(\pi\) lie in its affine tail the first ratio is affine over affine, with positive denominator and limit \(m+\nu/\pi'_\infty\). The finite check includes an endpoint of that region and the limit. Thus the two retained majorants can be summed before computing the rates, with \(|\alpha|\le1\).

For an analytic tail order \(k\), the unpriced dimensions and largest base first moments before the next transport are \((1,2k+1)\) and \((2,4k+2)\) for the pure and Legendre factors. The two-moment comparison with \(\pi(j)\le2j\) bounds their unscaled operator rates by \(4(k+1)\) and \(8(k+1)\). This also bounds the off-base rates, since their added base charge is at most twice the multiplier moment per unit of off-base first moment. Summing these order bounds from \(k=6\) with \(b_k\le1\) gives a geometric series times a linear or quadratic polynomial. The first six orders and these tails give geometric rates below \(0.4866\) for the Legendre piece and \(0.9579\) for the sum.

For the finite-field operator the analytic absolute coefficient times dimension is summable. By Round 96 the compact/fiber lift discrepancies have physical price \(O_{5000}(n^{-1/2})\) times the input price, including the marked and extra quotient coordinates. The actual diagonal changes only at the mark when the common bulk square-root factors are restored to \(t_0=n\). Its change is bounded uniformly, and after \(K\) is a multiple of the exact \(Ke_0\) of price \(O(n^{-1/2})\). The trace and repair comparisons can be made at finite truncations and passed to the limit in the closed representation space. The strict rational margins thus absorb the uniform corrections at all translated coordinates; they do not require an explicit finite prime threshold.

Replay the [exact rational checker](cold-jacobi-linear-legendre-145-check.py) with Python 3. It reads the fixed price list from the Round 130 checker as literal data and reproduces [one record](cold-jacobi-linear-legendre-145-checks.jsonl).
