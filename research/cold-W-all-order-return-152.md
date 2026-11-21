# The full alpha-free W-linear return on the genuine seed

Keep the original closed square, the physical marked floor \(t_0=n\), and the two-lift \(P_{5000}\) class. Let
\[
 J=K\operatorname{diag}(d_{t_i}(S_i)),\qquad
 M=K\operatorname{diag}(\beta W_i d'_{t_i}(S_i)).
\]
Then \(JM+MJ\) is the exact part linear in \(W\) with no \(\alpha Y\) factors in the square of the three-center row. Its eventual translated norm is less than \(0.05956\), and its price on the actual \(C_1\) column is less than \(0.04938\). These statements are uniform on the square along sufficiently large eligible primes.

On the uniform bulk floor put
\[
 D=d_t(S)=\sum_{k\ {\rm odd}}a_k C_k,\qquad
 Q=d'_t(S)=\sum_{k\ {\rm even}}b_k C_k .
\]
Write \(QC_1=\sum_{j\ {\rm odd}}u_j C_j\) and \(DC_1=\sum_{j\ {\rm even}}v_j C_j\). The signed Chebyshev product rule gives the following exact bulk expression on \(C_1\):
\[
 \beta K\!\left(
     \sum_{k,j\ {\rm odd}} a_k u_j C_k K(WC_j)
    +\sum_{k\ {\rm even},\,j>0\ {\rm even}} b_k v_j W C_k K(C_j)
 \right).
\]
The \(j=0\) term in the second sum vanishes by \(K1=0\). In the first sum \((k,j)=(1,1)\) gives \(\beta a_1(b_0+b_2/2)K(C_1F_4)\), and in the second \((k,j)=(0,2)\) gives \(\beta b_0(a_1+a_3)K(WY)/2\), up to the known \(O_{P_{5000}}(n^{-1/2})\) column corrections. These exposed tuples sum the explicit repeats across all Taylor orders of [Round 151](cold-leading-W-square-151.md#two-signed-returns-at-the-next-order). Other tuples can still have equal arithmetic constituents.

## Outward canonical and translated bounds

Use the first 14 binomial Taylor orders for \(D,Q\). Collect the signed coefficient of each harmonic in \(D,Q,DC_1,QC_1\). On each retained tuple convolve the \(C_j\) and exact \(W\) weight measures at the inner vertex. Activation preserves its nonzero weights and sets the zero weight to \(\sum_{k\ne0}(|k|-1)\mu_k\). Take the outer \(\pi\)-moment after convolving the remaining factors. The common two-fold lift symmetry allows the same measures in each base fiber.

For Taylor degrees \(r=2\ell+1\) and \(u=2m\), the sum of the two canonical word prices is at most \(12(r+1)(u+2)\) before the absolute scalar coefficient. Indeed the inner \(K\) makes the new mass and first absolute moment both equal to the input first moment. For the first order this moment is bounded by \(3(u+2)\), for the second by \(r+1\). The remaining factors then give a first moment at most \(3(r+1)(u+2)\) in each order, and \(\pi(k)\le2|k|\). The same argument upper-bounds any subset of the resulting positive harmonic envelopes when two tuples are removed. With \(z=0.356^2\), the double analytic tail is bounded by the product sums with factors \((\ell+1)z^\ell\) and \((m+1)(2m+1)z^m\), whose sums are \((1-z)^{-2}\) and \((1+3z)/(1-z)^3\). The [outward replay](cold-W-all-order-return-152-check.py) charges all terms outside the 14 by 14 Taylor truncation. The resulting tail is below \(3.44\cdot 10^{-11}\). The eventual canonical price excluding the two exposed tuples is below \(0.00768\). Separate scalar tails enclose the two whole-order coefficients, with relative moduli below \(0.837\) and \(0.863\) against their respective nonzero leading factors.

For every translated input column the \(M\)-multiplier uses the convolution of the actual \(W\) weight measure with \(\sum_{k\ {\rm even}}|\beta b_k|\mu_{C_k}\), where the \(b_k\) are first summed with signs through 14 orders. Apply the [Round 145](cold-jacobi-linear-legendre-145.md) base/off-base column formula and affine limit. In the remaining order \(m\) the absolute rate before its scalar coefficient is at most \(12(m+1)\) by the mass and first moment bounds. This gives \(\|M\|<0.0564\) with slack for actual repairs. The [Jacobi bound](cold-pure-seed-134.md) is \(\|J\|<0.528\), so \(2\|J\|\|M\|<0.05956\). This translated estimate takes separate moduli at the two vertices. Both restorations of \(t_0=n\) and the bad-lift columns retain their uniform \(O_{5000}(n^{-1/2})\) costs by absolute summability. [Saved record](cold-W-all-order-return-152-checks.jsonl)
