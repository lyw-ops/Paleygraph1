# Four linear/cubic returns in the physical iteration

The unforced nine-center Picard iteration has a common holomorphic physical stationary row on a colder open rectangle, for every eligible prime \(p=2n+1\) with \(n\ge10^{30}\).

## A common cubic coefficient

Write the last four signed inputs as \(\delta G,zR,w(D+D^\vee),v(U+U')\), with the [rank-five determinant convention](astra-ranknext-58.md), the independent mixed symplectic standard \(R\), the dual pair \(D,D^\vee\), and the two independent symplectic standards \(U,U'\). Put
\[
     Q=\delta^2/16+z^2+2w^2+2v^2 .
\]
For each of the sixteen summands of \(16G\), its own two-standard/one-dual balanced words give two contractions in each of three orders. For each of the other seven factors, inserting that standard and its dual contributes one contraction in six orders. All 48 copies have exactly the same rational general-linear signature as the chosen linear summand, including the arithmetic determinant. After the two additional factors of \(1/16\), their multiplier is \(48/16^2=3/16\). The checker independently counts these 48 signatures on the eight factors of dimensions \(6,6,5,5,5,5,7,7\).

In each of the other three systems the selected cube returns respectively 3, 6, and 6 copies of each linear constituent with its own arithmetic character. For \(R\) and either symplectic standard, the three contractions come from the three pairings. The standard square in either symplectic dimension four or eight has three distinct self-dual summands, so these three pairings are independent. For \(U\) the other three copies come from choosing the \(U'^2\) unit in its three positions, and conversely for \(U'\). In the dual pair there are the two balanced contractions in three orders. Its additional *shifted* determinant return is left separately charged. For a cube with one child from the chosen family and two from any other family, the latter pair contributes its unit in each of three positions. Thus in every family the selected cubic coefficient is \(3Q\) times its own linear amplitude. Mixed monomials of type \((2,1)\) use the unit in the factor having degree two, so their final label singles out the degree-one family. [Mixed symplectic cube](astra-legendre-63.md) · [Dual cube and determinant shift](astra-joint-64.md) · [Later quadratic units](astra-paired-96.md)

Use the signed rank-three prefix \(C_{r,a,u,b,e}\) of round 95 on every derived label \(a\) of degrees through four, with the actual older amendments, source Jacobi mode at most nine, \(u+b\le5\), and free arity at most eight. Set an absent source to zero. For a fixed \(a,u,b\) form the scalar rank-four coefficient
\[
 A_{r,e}= C_{r,e}+\binom{r+2}{2}\frac{\gamma^2}{8}C_{r+2,e}
 +\binom{r+4}{4}\frac{\gamma^4}{4096}
   (196C_{r+4,e}+2C_{r+4,e-2}+2C_{r+4,e+2}).
\]
Use the union of the attainable exponents including endpoints. At residual arity \(0\le j\le5\), retain the cancellation between \((j+1)A_{j+1,e}\) and \(3\binom{j+3}{3}Q A_{j+3,e}\). At \(j=0\), omit both single-Legendre labels with \(a\) trivial and \(e=0\). The omitted labels contain the native mixed-symplectic and dual-pair linear/cubic root subtractions. The other native root amendments select zero later inputs or the old rank-four standard. Weight the saving by the Legendre and rank-three boundary measures, using site \(w_3-2u+4i-e\) for \(0\le i\le u\) and multiplicity \(b+1\) times the rank-three multiplicity. Take the smaller lower saving on reflected sites and convolve with the absolute sum of the four linear boundary measures. This includes the normalization of \(G\). Exchange of factors and of the two Legendre labels preserves the entire selection.

In the linear resource the native extracted scalar and the earlier zero/two rank-four pool can already be combined. Every such pool at fixed inner label and final exponent uses only summands of the displayed \(A\), including both shifted quartic constituents of the extracted scalar. Hence the charge remaining even after the one-child debit of round 99 dominates \(|A|\) by the triangle inequality. The complementary round-99 and round-100 rank-three sources have different *input* indices. The repeated-shift rank-four shapes selected by round 100 are nontrivial, whereas the displayed \(A\) uses only the rank-four scalar. The old two-child debit has zero or two later children, whereas the linear/cubic debit has one or three. The original nonselected Taylor coefficients, exceptional column and unextracted terms on the same output labels retain their charges. [Round-99 one-child construction](astra-cold-99.md#propagation-to-one-later-child) · [Round-100 shape and source selections](astra-return-100.md)

For an explicit pure rank-five test, take \(j=0\), all inner derived and Legendre labels trivial, and \(e=1\). Before convolving with the normalized \(G\) boundary measure, the triangle saving between \(\delta A_{1,1}\) and \(3\delta^3 A_{3,1}/16\) exceeds \(3.57\cdot10^{-10}\) throughout the first comparison box. This is an identifiable cubic saving even without the three mixed families.

## Two later children with nontrivial joint label

Let \(S_r\) be the existing symmetric lower saving of round 99 for zero-later-input pools, before its propagation to one child. The checker captures the very same six polynomials in the evaluation of that propagation. Write \(P\) for the sum of the four single-child boundary measures times the respective lower absolute amplitudes. At residual arity \(j=r-2\), \(2\le r\le6\), the additional saving is
\[
 \binom r2 S_r *\left(P^{*2}-
   (d^2/16+z_0^2+2w_0^2+2v_0^2)\,\delta_0\right),
\]
where \(d,z_0,w_0,v_0\) are those same lower absolute amplitudes and \(\delta_0\) is the point mass. Expanding before rounding gives a positive combination of the remaining quadratic constituents. The subtracted units are exactly the two-later-input labels used in round 96. The old one-child and the present linear/cubic counts use different later input degrees. None of the native distinguished root subtractions uses two later children. The zero-later source \(S_r\) excludes the rank-three complement and the new round-100 repeated shapes. This proves disjointness also after propagating to the final boundary.

## Slabs and remaining obligations

In units of \(2^{-20}\), the three closed real intervals are \([16640184,16640186]\), \([16640183.25,16640184.25]\), and \([16640183,16640183.5]\). They use four, six, and four real cells, respectively, with one upper imaginary cell of height one and its conjugate. Adjacent intervals overlap on open real segments. With forcing one and the full \(10^{-12}\) exceptional-column allowance, the [Arb192 checker](astra-rank-101-check.py) applies the same 58-packet image to the [frozen integer caps](astra-rank-101-caps.json). The tilted excess is below \(1.85\cdot10^{-10}\) against the budget \(2\cdot10^{-10}\). The previous map overruns packet two of the first cap by more than \(5.28\cdot10^{-9}\). [Replay records](astra-rank-101-checks.jsonl)

Consequently the physical stationary row exists on
\[
    16640183<2^{20}\Re t<16640186,\qquad 2^{20}|\Im t|<1 .
\]
The coordinate bound is below \(4.654\). The derivative bound on each genuine iteration segment is below \(.526\), including the mark, and the normalized residual is at most \(9.308(.526)^h\). The limit has \(|m_p|<3/\sqrt n\), agrees with the physical real row, and its action is harmonic on the reciprocal image. It agrees on the open overlap \(16640185<2^{20}\Re t<16640186\) with round 100. The left edge moves two units colder, leaving \(2223/2^{20}\) to the right boundary of the nominated square. For the finitely many smaller fields the prior compactness argument applies after shrinking the imaginary thickness on closed real subintervals. The nominated square, the two real tail estimates, and the ordinary theta limit remain open. [Fieldwise convergence and physical identification](astra-depth-95.md#field-first-decay-and-harmonic-action)

From the repository root run

    PYTHONPATH=. .venv/bin/python -B research/astra-rank-101-check.py

1. For the two one-sided log tails on the actual pre-exit orbit, bound both signed cut sums by \(.00139\) with the same per-time deletion of at most \(\lfloor\sqrt n/6000\rfloor\) sites. This would exclude real first exits on the nominated interval. [Real first-exit test](astra-exit-98.md)
2. At the dual pair \(D,D^\vee\), collect the extra determinant-shifted cubic from the opposite standard with its full current linear/cubic sum at the matching final exponent. The shifts have magnitude four, and each shifted copy has multiplicity one. Keep the native root omission and all reflected sites. A strict overlapping slab left of \(16640183/2^{20}\) would advance the common complex continuation.
