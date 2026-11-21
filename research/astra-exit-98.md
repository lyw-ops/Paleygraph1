# Positive defects on the actual real pre-exit orbit

On the real interval of half-width \(2^{-17}\) around \(2031/128\), a first entry of the actual nine-center Picard orbit into \(\|V\|_\infty\ge4\sqrt t\) forces a signed response greater than **9.5** to nonnegative defects. The test survives independent deletion of \(\lfloor\sqrt n/6000\rfloor\) sites at every time. A single realized level set at one pre-exit time must give a positive signed cut, and one of the two one-sided log tails must also do so. These are necessary conditions at sufficiently large eligible primes \(p=2n+1\). The [finite real two-step theorem](astra-incoming-97.md) already excludes a slow projection for \(n\ge10^{30}\), \(p\le4\cdot10^{695}\).

## A bounded initial lag in the physical packet norm

Use \(X=V_{100}\), \(W=V_{600}\), \(D=\Phi'_t(X)\), \(T=KD\), and write \(R_a=V_{a+1}-V_a\). The [height-dependent packet estimates](astra-adjoint-82.md#physical-packet-prices-for-the-actual-derivative) give \(\|W-X\|_\pi<1.011\) as follows. For fixed field and floor let \(b_h\) be the running maximum up to height \(h\) of the physical packet operator norm of the derivative on the real segments \([V_{k-1},V_k]\), \(1\le k\le h\). The positive packet envelopes in the height calculation increase coordinatewise. Its rate at each checked height consequently bounds every such earlier derivative. In particular the right endpoint of each five-step block after height 300 bounds all five running maxima in that block. Thus \(P_h=\|R_0\|_\pi\prod_{k=1}^h b_k\) bounds \(\|R_h\|_\pi\) and is in turn bounded by the cumulative upper products in that calculation. If an initial rate vanishes, all subsequent actual increments are zero and the lag estimate is immediate. Otherwise \(P_h\) is log convex since the \(b_k\) are nondecreasing. At heights \(100,250,275,300,600\), the recorded endpoint bounds are respectively \(.001180,.000343,.000322,.000312,.010955\). On each interval \([a,b)\) with upper endpoints \(x,y\), sum \(x(y/x)^{(h-a)/(b-a)}\) over the integers. The four sums total less than \(1.011\). This uses the [actual cumulative residual bounds](astra-adjoint-82-checks.jsonl) and does not interpolate the observed coordinate values.

## An affine recurrence with a nonnegative source

Put \(Y_j=V_{600+j}\) and \(f_i(y)=\sqrt{4t_i+y^2}\), where \(t_i=t\) except \(t_0=n\). Define the tangent defect
\[
 B_i(y)=f_i(y)-f_i(X_i)-D_{ii}(y-X_i)
       =4\sqrt{t_i}\,\operatorname{sech}(v_i)\sinh^2((z-v_i)/2),
 \quad v_i=\operatorname{arsinh}(X_i/(2\sqrt{t_i})),\quad
 z=\operatorname{arsinh}(y/(2\sqrt{t_i})).
\]
In particular \(B_i\ge0\) on both sides of the reference. Iterating the exact affine equation from the actual \(W\) gives
\[
 Y_m-X=T^m(W-X)+\sum_{\ell<m}T^\ell R_{100}+
        \sum_{\ell<m} T^\ell K B(Y_{m-1-\ell}).                 \tag{1}
\]
The first two terms have combined coordinate cap below \(1.011+.001180/(1-.984138)\). At a first exit choose a hitting site \(i\) and \(\sigma=\operatorname{sgn}(Y_{m,i})\). In the last term all actual inputs precede the exit. Since \(\|X\|_\infty<4.768\), its signed total exceeds \(4\sqrt{2031/128-2^{-17}}-4.768-1.011-.001180/(1-.984138)>10.07\).

All its source entries satisfy \(0\le B_x(Y_{j,x})<19.17\). For the bulk, at fixed \(y\), the derivative of the tangent defect with respect to its reference \(w\) is \(f''(w)(w-y)\). Convexity in \(y\) and this derivative maximize the defect on the input and reference intervals at opposite endpoints. For \(y=4\sqrt t\), \(w=-4.768\), this maximum equals \(\sqrt{20t}-\sqrt{4t+4.768^2}+4.768(4\sqrt t+4.768)/\sqrt{4t+4.768^2}\). At the mark use \(f_0''\le1/(2\sqrt n)\).

## Deleting a growing number of sites and recovering one signed cut

For real \(t\) put \(b'_\ell=\sqrt n\max_{j,x}|(T^\ell K)_{jx}|\). Eventually, uniformly in \(t\),
\[
                    \sum_{\ell\ge0} b'_\ell < 178.              \tag{2}
\]
Here the maximum occurs *inside* the sum. To verify this order, use the two-component [translated-column comparison](shifted-resolvent-96.md#the-two-estimates-for-one-physical-derivative-step) with \(q=.984138\), multiplier mass \(m_0\le q\), and cross entry \(\nu\le2(q-m_0)\). Per unit seed the coincident-source price is at most \(q^\ell\), and the distinct-source price is at most \(m_0^\ell+\nu\sum_{j<\ell}q^{\ell-1-j}m_0^j\le2q^\ell-m_0^\ell\), including \(m_0=q\). Hence the uniform majorant is one at zero and \(2q^\ell\) afterwards. The finite-field comparison adds entrywise \(O(n^{-1/2})\) to the nonnegative triangular matrix \(M\). Its summed excess in powers is \((I-M-H)^{-1}H(I-M)^{-1}=O(n^{-1/2})\) for a common nonnegative perturbation bound \(H\). Both inverses are uniformly bounded by the triangular estimate and a small-perturbation geometric series. Multiplying by \(\sqrt{p/n}\) gives a limsup at most \(\sqrt2(2/(1-q)-1)<178\).

Delete any independently chosen sets \(S_j\) with \(|S_j|\le\lfloor\sqrt n/6000\rfloor\). By (2) their total unsigned debit is at most \(178(19.17)/6000\). The signed last term in (1) on the surviving sites still exceeds \(9.5\), using the unrounded entrance and initial lag bound. For \(b'_\ell>0\) let \(C_{\ell,ix}=(T^\ell K)_{ix}/b'_\ell\); skip zero matrices. This row sums to zero on all sites, since \(K1=0\), and \(|C_{\ell,ix}|\le1/\sqrt n\). The layer-cake formula for the nonnegative defect now implies that some \(\ell<m\), \(j=m-1-\ell\), and \(s\in[0,19.17)\) satisfy
\[
              \sigma\sum_{x\notin S_j:\ B_x(Y_{j,x})>s}
                              C_{\ell,ix} > 0.00278 .                 \tag{3}
\]
Indeed the opposite inequalities would bound the signed response by \(178(19.17)(.00278)<9.5\). The cut therefore has more than \(.00278\sqrt n\) surviving sites. Moreover its two pieces \(z_{j,x}>v_x\) and \(z_{j,x}<v_x\) are explicit selected log tails because of the displayed formula for \(B\). At least one gives signed response greater than \(.00139\). The erasures may depend on the entire orbit, the tested row and the sign. Ruling out (3) for the physical cuts would exclude every such exit and hence every incoming two-step projection above \(0.8\). The cancellation on these actual cuts remains open.

## Two quadratic rank-four returns in the unforced complex invariant

Let \(F\) be the normalized sum of the eight rank-four standards and duals, with signed amplitude \(\gamma\). Use the [arithmetic Pieri tables](astra-rankfour-57.md) for \((8F)^h\) and the same [inner rank-three coefficients](astra-depth-95.md#eight-further-signed-rank-three-labels) \(C_{r,a,u,v,e}\) on all rank-three labels of degrees through four. Here \(r\le8\), the Jacobi input mode is at most 9, and the Legendre labels have \(u+v\le5\). The determinant-corrected exponent of the inner coefficient is \(e\). Fix its three derived labels when comparing different exponents or arities. Both collections below have zero inputs from the four later centers.

In \((8F)^2\) two nontrivial shapes occur at two determinant shifts each. These are the second exterior powers of the first two standard factors. Their shift pairs are \(\{-2,0\}\) and \(\{0,2\}\), and their multiplicities are one at each shift. At free arity \(j\le6\), for a pair \(d_1<d_2\) and each common output exponent \(e+d_1\), collect
\[
  \binom{j+2}{2}\frac{\gamma^2}{64}
       \left(C_{j+2,a,u,v,e}+C_{j+2,a,u,v,e+d_1-d_2}\right).
\]
This combines two quadratic terms by their signed inner coefficients. Skip the entire trivial rank-three and Legendre sector in this calculation, which contains the older extracted scalar exponent pool. Elsewhere those two inputs were charged separately. Each occurrence of a coefficient at either shift contributes at only one output exponent for that shift, although it can appear at a second output via its other, independently charged constituent.

For every nontrivial quadratic shape with *unique* shift \(d\), the quartic table contains at least 48 times its quadratic multiplicity at that same arithmetic label and shift. Its normalized square-fiber coefficient therefore pairs
\[
  \binom{j+2}{2}\gamma^2 C_{j+2,a,u,v,e}
  +\tfrac34\binom{j+4}{4}\gamma^4 C_{j+4,a,u,v,e},
               \qquad 0\le j\le4 .
\]
The factor \(3/4=48/8^2\) retains a common portion of the quartic term at each quadratic constituent. In the old extracted scalar sector a nontrivial unique-shift shape at a fixed final exponent has exactly one source exponent at quadratic degree. Its diagonal quadratic charge is thus available even there; the old quartic extraction in that sector used only the scalar lines. The other previous zero-later-degree pools at rank four used the quadratic unit or the linear and cubic standard. The two new shape families omit the unit and are disjoint from one another. All later-center unit returns of [round 96](astra-paired-96.md) used two previously independent later inputs. The later root amendments selected a linear rank-four label or a scalar. Hence those debits remain intact.

For the two-shift term use the actual fiber at the common exponent; for the unique-shift term sum the weighted fibers with quadratic multiplicity divided by 64. The latter has total dimension \(992/64\) and the same symmetric weight polynomial at both twists. The two exterior squares are exchanged under the twist, which also exchanges the two Legendre and rank-three factors and reflects the determinant exponent. The selected full index set is stable under that exchange. As before, compute nonnegative triangle savings on each arithmetic label and debit at most the smaller certified saving at the two reflected sites. Unselected charges and the physical exceptional-column budget are retained.

In units of \(2^{-20}\) the four closed real intervals are \([16640194,16640197]\), \([16640196,16640201]\), \([16640199,16640212]\) and \([16640210,16640217]\), all with imaginary half-width one and original forcing parameter one. The upper-half meshes have respectively 12, 5, 6 and 7 real cells and one imaginary cell. The [outward checker](astra-exit-98-check.py) tests the inherited 58-packet map at the [integer caps](astra-exit-98-caps.json), including the actual exceptional allowance. The excess is below \(2\cdot10^{-10}\). The [same physical convergence argument](astra-depth-95.md#field-first-decay-and-harmonic-action) yields a coordinate cap below \(4.654\) at every height, residual bound \(9.308(0.526)^h\), and a holomorphic genuine stationary row with \(|m_p|<3/\sqrt n\) on the open rectangle, for every eligible \(n\ge10^{30}\). It identifies the physical harmonic action there and overlaps the previous domain on \((16640216,16640217)\) in these units. The left edge advances 22 units; the remaining gap to the right edge of the nominated square is 2234 units. The results for smaller primes on shrunken closed real subintervals follow as in round 95. The [six replay rows](astra-exit-98-checks.jsonl) include a comparison with the previous map at the new coldest cap.

1. Test the two one-sided actual log tails in (3) after deleting the strongest favorable sites of the signed frozen row. A uniform upper bound of \(.00139\) on each surviving one-sided sum excludes all first exits and slow incoming projections on the real interval.
2. At the two duplicated exterior-square determinant shifts, retain the quartic constituents at their actual shifted exponents too. This tests the remaining signed debit on the same complex rectangle construction. The common stationary section on the nominated square and the ordinary theta target stay open.
