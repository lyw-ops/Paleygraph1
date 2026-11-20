# The actual outgoing cold insertion at height 600

Use the original complex square \(Q\) centered at \(2031/128\) with half-width \(2^{-17}\) and the physical nine-center Picard rows. Put \(V=V_{600}\), \(R=V_{601}-V_{600}\), \(D=\operatorname{diag}\Phi_t'(V)\), and \(A_j=(KD)^j K\). The actual [physical packet bounds](astra-adjoint-82.md) give total absolute coefficient times dimension less than \(4.8\) for \(V\), and price less than \(0.010955\) for \(R\), on \(Q\). The price dominates that dimension cost and the coordinate norm. In both cases the negative fields use only the base pair of boundary characters. Use \(\varepsilon=0.011\), \(M=4.811\), and \(N=4(2031/128-2^{-17})\). Thus \(M^2<N\). As in the cited packet construction the bounds apply to absolute sums and their limits in the represented finite-field spaces.

For \(0\le s\le1\), let \(E_s=\operatorname{diag}(\Phi_t'(V+sR)-\Phi_t'(V))\) on the actual sheets. The first averaged secant difference is \(\bar E=\int_0^1 E_s\,ds\). Here the height-601 endpoint is the actual \(V+R\). Its own packet estimate is unnecessary for this representation.

## Uniform word cost and the two translated columns

For a product of \(k\) negative Mellin fields of convolution dimensions \(d_1,\ldots,d_k\), whose boundary characters lie in a common set \(S\) stable under the lift twist, the generic rank of the middle convolution is at most \(k\prod_j d_j\). For a fixed full character, the normalized fiber weights under convolution add in law. Sum their first absolute moments over the twists in \(S\). By the triangle inequality the result is at most the sum of the first absolute moments of the inputs in normalized weights. By Katz's Theorem 16.1 each input contributes \(2r_i/d_i=2\), where \(r_i=d_i\) for negative fields. On the output the sum is \(2r/\prod_j d_j\): each tame block is counted once at its matching twist and the two boundary ranks both equal \(r\). Punctual constituents contribute only weight zero. The same fiber statement excludes any new boundary character. [Katz, Chapters 3 and 16](https://web.math.princeton.edu/~nmk/mellin331.pdf) · [Rank from the boundary fibers](astra-feedback-52.md)

For odd \(k\) the middle convolution has no punctual term at \(1\) by the [negative-parity rule](iteration-parity.md). Its mean Mellin trace is therefore at most \(k\prod_j d_j/\sqrt p\) in modulus, by the weight bound at the middle-extension stalk. Replacing the exact product by the convolution trace costs at most \(2\prod_j d_j\) per bad full character. There are at most \(|S|\) such characters, independently of \(k\). Expansion of the lift averages is an average over twists and does not add a factor exponential in \(k\). This proves the normalized estimate \(O((k/\sqrt p+|S|/p)\prod_j d_j)\). The uniformity in the number of factors is needed for the analytic series below. [Local convolution and parity at \(1\)](https://arxiv.org/abs/1106.1398)

On the bulk use the positive-real bulk derivative \(d_t(z)=z/\sqrt{4t+z^2}\). Write \(c_\ell=\binom{2\ell}{\ell}/4^\ell\). Its analytic difference is the absolutely summable series
\[
 \sum_{\ell\ge0}\frac{(-1)^\ell c_\ell}{(4t)^{\ell+1/2}}
       \big[(V+sR)^{2\ell+1}-V^{2\ell+1}\big].
\]
Telescoping each power gives \(2\ell+1\) products with one explicit factor \(sR\) and the other factors from \(V\) or \(V+sR\). They are products of \(2\ell+1\) negative fields. Their total dimension bound before applying the coefficient is at most \(s\varepsilon(2\ell+1)M^{2\ell}\). Even with an additional cost \(2\ell+3\), the summed bound is
\[
 C_{\rm odd}(s):=\frac{3s\varepsilon}{\sqrt N}
                       (1-M^2/N)^{-5/2}.
 \tag{1}
\]
This follows by summing \(c_\ell(2\ell+1)(2\ell+3)(M^2/N)^\ell\). At the mark the actual derivative difference differs from the bulk difference by \(O(s\varepsilon)\), using the distinct physical radicand \(4n+z^2\). Its diagonal contribution can be added directly.

For the two endpoint columns of \(A_u E_s A_v\), [Round 96](shifted-resolvent-96.md) gives dimension prices at most \(C n^{-1/2}(1.048)^u\) and \(C n^{-1/2}(1.048)^v\) for all powers at this fixed reference. The matrices \(A_j\) are transpose symmetric. At most six full characters occur in the union of the base pair and the two translated pairs. The odd word estimate, (1), and multiplication by \(n\) to turn the mean into the physical insertion give
\[
 \|A_u E_s A_v\|_{\max}\ll
   s\varepsilon n^{-1/2}(1.048)^{u+v}.
 \tag{2}
\]
The separate marked term costs \(O(s\varepsilon n^{-1}(1.048)^{u+v})\). These estimates hold for the exact derivative difference or its actual secant average. They do not require a dimension budget proportional to the much smaller normalized second norm of \(R\).

Independently the counting norm gives \(\|A_u E_s A_v\|_{\max}\ll s\varepsilon(0.514)^{u+v}\). Splitting at total power \(u+v=\lfloor\log n/(2\log(1.048/0.514))\rfloor\), and retaining its multiplicity \(u+v+1\), gives a bound \(O(s\varepsilon(1+\log n)n^{-\beta_*})\) for the whole sum over \(u,v\ge0\), where \(\beta_*=-\log(0.514)/(2\log(1.048/0.514))>0.467\) by the [outward replay of Round 96](shifted-resolvent-96-check.py). In particular,
\[
 \sum_{u,v\ge0}\|A_u E_s A_v\|_{\max}=O(s\varepsilon n^{-0.467}).
 \tag{3}
\]
The strict exponent margin absorbs the logarithm. This verifies the whole frozen signed first-insertion budget for this actual transition on \(Q\) at sufficiently large primes.

## A second genuine outgoing counting step

For an unshifted negative input with the base pair, multiply the same odd series by the input and apply \(K\). Each word now has even length \(2\ell+2\). Transport kills its punctual term and gives a negative field with dimension equal to the pre-transport generic rank. The original unshifted price is at most twice that rank by \(\pi(k)\le2k\). Hence the geometric price per unit-priced input for \(KE_s\) is at most \(2C_{\rm odd}(s)\), bounding \(2\ell+2\) by \(2\ell+3\) in (1). Missing full-character products and the marked derivative difference occur only at the physical base coordinate. They contribute an additional \(O(s\varepsilon n^{-1/2})\) in price after transport by \(Ke_0\), by the dimension bounds above and the fixed size of the base pair.

The rational inequality \(2 C_{\rm odd}(1)<0.026\) then yields a price below \(1.074\), for sufficiently large primes, for the first **outgoing** actual secant \(K(D+\bar E)\) on the unshifted class. The inherited \(1.046434\) rate is used only for the frozen \(KD\). Thus \(R_{601}=V_{602}-V_{601}=K(D+\bar E)R\) has sup norm below \(1.074(0.011)<0.012\). This argument supplies coordinate control of the actual second outgoing segment.

Every point on the segment from \(V_{601}\) to \(V_{602}\) lies within \(0.011+0.012\) of \(V_{600}\) and has modulus less than \(4.791\). The bulk radicand stays in the right half-plane, and the curvature on these segments and the lines from \(V_{600}\) is below \(0.248\), by \(4\sup_Q |t|/(N-4.791^2)^{3/2}<0.248\); the marked curvature is smaller for large \(n\). Integrating the derivative difference along the second actual secant bounds its counting operator norm by
\[
 0.51358+0.248(0.011+0.012/2)<0.518 .
\]
The first outgoing counting step is below \(0.515\) by [Round 122](api-astra-review-122.md). Thus the actual two-step counting contraction from \(R_{600}\) to \(R_{602}\) on \(Q\) is below \(0.267\) for sufficiently large eligible primes. These are fixed-height consequences of the older outward inputs and exact inequalities. They do not give a growing-depth confinement bound or a compatible small residual for the quadratic varying-kernel estimate of Round 124.

## An all-column estimate at the new fixed endpoint

The same geometric perturbation estimate works for the translated price \(P_\Lambda\) of Round 96, with \(\Lambda=5000\). For a negative input of dimension \(d\), write \(b\) for its off-base first boundary moment. Each factor of the derivative-difference word has only the base pair. Thus at each character of the input's translated pair outside the base pair, the off-base weights of every multiplier factor are zero. The output off-base moment, after the \(K\) twist, is bounded by \(b\) times the word's product dimension \(d_{\rm word}\). The base price is at most \(2k d\,d_{\rm word}\) for a product of total length \(k=2\ell+2\), by the generic rank bound. Since \(P_\Lambda\ge d,\Lambda b\), the combined cost is at most \((2k+1)d_{\rm word}P_\Lambda\), which fits under \(2(2\ell+3)d_{\rm word}P_\Lambda\). At bad full characters the correction is supported on the base and that single translated pair. Its post-transport price is \(O_\Lambda(s\varepsilon n^{-1/2})\) per unit-priced input. The estimate therefore adds at most \(0.026+O_\Lambda(n^{-1/2})\) to the height-600 translated rate.

At the actual height-601 endpoint this gives translated price rate below \(1.075\) for sufficiently large primes, using the old upper \(1.048\). Independently \(\|K\Phi_t'(V_{601})\|_{2\to2}<0.517\) by the curvature bound and \(\|R\|_\infty<0.011\). Applying the counting and packet split to the new frozen powers gives
\[
 \sum_{j\ge0}\left\|\big(K\Phi_t'(V_{601})\big)^jK\right\|_{\max}
 =O(n^{-0.45}).
\]
In fact \(-\log(0.517)/(2\log(1.075/0.517))>0.45\), which follows from the exact rational comparison \(0.517(1.075)^9<1\). The translated bound is weaker than the original height-600 exponent and holds at a genuine updated endpoint. It does not preserve the exponent \(0.467\) for the full new inverse, even though the signed linear part of that transfer has the stronger bound (3).
