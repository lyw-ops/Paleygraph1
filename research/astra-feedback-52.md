# A second Mellin moment for the actual smoothed mark

For all eligible primes and prime squares, the actual real mark satisfies the following uniform power estimates. Here \(n=(q-1)/2\).

| Closed interval of floors \(t\) | Bound for \(\sup_t \lvert m_q(t)\rvert\) |
|---|---|
| \([145/8,73/4]\) | \(O(n^{-1/28000})\) |
| \([73/4,19]\) | \(O(n^{-1/5600})\) |
| \([19,197/8]\) | \(O(n^{-1/1200})\) |

Together with [round 51](astra-warm-51.md), the real decay interval on compact sets now starts at \(145/8=18.125\). Four polynomial updates also give a strict eventual marked tolerance of 0.017 through primes from floor 141/16 and through primes and squares from 79/8. The ordinary prime theta limit remains open.

## Reading rank from two Mellin characters

Work in the same pure, weight-zero middle convolution category as in the [local inertia argument](iteration-parity.md). We first work with the geometric part of the Laurent recursion, postponing corrections at exceptional Mellin characters. All its objects are tame and have only the eigencharacters \(1,\chi\) at the two boundaries \(0,\infty\). Here \(\chi\) denotes the quadratic tame character. We justify closure below.

For an object \(M\) of convolution dimension \(d\), let \(\mu_\alpha(M)\) count the signed Frobenius weights of the eigenvalues in the **fiber functor** of \(M\otimes\mathcal L_\alpha\) at the trivial character. This fiber functor exists at bad Mellin characters, too. It is not the compact-support Mellin trace there. Take \(\alpha=1,\chi\) and put \(\mu(M)=(\mu_1+\mu_\chi)/2\). By Katz, Theorem 16.1, each nonzero weight \(-e\) corresponds to a size-\(e\) Jordan block with matching character at zero, and \(+f\) to a size-\(f\) block at infinity. All remaining weights are zero. The statement extends by additivity to direct sums, and a pure weight-zero punctual object contributes only zero weights. One may extend the base field to split constituents and tame eigencharacters. Weights and geometric block lengths used here are unchanged. [Katz, Chapters 3 and 16](https://web.math.princeton.edu/~nmk/mellin331.pdf)

It follows, writing \(r\) for the generic rank, that
\[
 \int 1\,d\mu=d,\qquad \int w\,d\mu=0,\qquad \int |w|\,d\mu=r .
\]
Each boundary contributes its full rank divided by two to the absolute moment. On a negative field \(d=r\). For a fixed full twist, tensor compatibility of the fiber functor makes the weight measure of a middle convolution the ordinary additive convolution of the weight measures. The inputs to a product of lift averages are independently twisted by \(1\) or \(\chi\). Thus their *averaged* pre-activation measure is the additive convolution of their individual pooled measures. Indeed, conditioning on the common output twist permutes the two equiprobable choices independently for each input. This applies linearly with positive absolute coefficient weights. For any other geometric tame character, all twisted input weights are zero, since they have no matching blocks at either boundary. Their sums are zero as well. Theorem 16.1 applied after twisting back then excludes any new boundary character. This proves closure under convolution, starting from the Jacobi object with boundary characters \(1,\chi\).

Applying \(K\) discards punctual summands and twists the remaining generic local system by \(\chi(1-a)\). This leaves the zero boundary alone and interchanges the two possible eigencharacters at infinity. Consequently it preserves the entire pooled measure on *nonzero* weights, including its second moment. The new negative object's dimension is the old generic rank, hence the absolute moment of the input measure. Explicitly a node sends an input measure \(\nu\) to a measure with the same masses away from zero and new mass \(\sum_{w\ne0}(|w|-1)\nu(w)\) at zero. A rank-one invertible Jacobi convolution power and its inverse in \(T_k(S/s)\) give the input measure \((\delta_k+\delta_{-k})/2\), including at \(k=0\). This follows from the weights \(-1,+1\) of the two seed twists and tensor compatibility. The choice of overall trace sign has absolute magnitude one.

For example the first nonconstant quadratic feedback \(K T_2(S/s)\) has measure \(\delta_0+(\delta_2+\delta_{-2})/2\) for its geometric part. Multiplying by the first seed mode and applying \(K\) costs rank three. The old mixed bound charged four. In geometric terms this is the twisted Legendre family, whose rank-two unipotent blocks at zero and infinity are described in Katz, Chapter 15. Equivalently the convolution of the two untwisted quadratic seed trace functions at \(a\ne0,1\) is proportional to \(\sum_u\chi(u(u-1)(u-a))\), and applying \(K\) supplies its \(\chi(1-a)\) twist. The two inverse seed squares differ by a quadratic Kummer twist before restriction to squares. [Katz, Chapter 15](https://web.math.princeton.edu/~nmk/mellin331.pdf)

## Two radii for the whole recursion

Use the coefficients \(c_{jk}\), Jacobi seed \(S\), limiting scale \(s\to2\sqrt2\), and auxiliary equation from [round 51](astra-warm-51.md):
\[
 R(z)=K\sum_{j,k\ge0} c_{jk}z^{k+1}T_k(S/s)R(z)^j .
\]
An absolute-coefficient sum of negative inputs with total mass \(b\) and second moment \(c\) has mean zero and first absolute moment \(b\). The convolution of \(j\) copies and the seed mode has mass \(A=b^j\) and second moment \(E=k^2 A+J\), where \(J=j c b^{j-1}\) (zero for \(j=0\)). The post-\(K\) mass is bounded by
\[
 G_{jk}(b,c)=\min\left\{(k+j)A,\sqrt{AE},\ kA+J/(4k)\right\},
\]
with the last term omitted for \(k=0\). The first bound is the triangle inequality and the second Cauchy–Schwarz. For the last, average over the seed sign to obtain \((|k+w|+|-k+w|)/2=\max(k,|w|)\le k+w^2/(4k)\). Its second moment after \(K\) is exactly \(E\). These positive bounds increase with \(b,c\), so upper enclosures can be substituted throughout.

The [Arb checker](astra-feedback-52-check.py) certifies strict bounds for the sums of \(|c_{jk}|\rho^{k+1}\) times \(G_{jk},E\) at the following radii. It also verifies the old coarse rank sum at auxiliary radius \(1/2\), using \(b\) as the feedback radius.

| Floors | \(b,c,\rho\) | Upper bounds on mass, second moment, coarse mass |
|---|---|---|
| \([145/8,73/4]\) | \(1.740,3.700,1.0002\) | \(1.739,3.688,0.523\) |
| \([73/4,19]\) | \(1.700,3.620,1.001\) | \(1.698,3.598,0.506\) |
| \([19,197/8]\) | \(1.650,3.490,1.005\) | \(1.631,3.439,0.479\) |

The checker combines signed Laurent coefficients through Taylor order 28 before taking absolute values. In the tail of even arity \(m=2\ell\), the rank charge is at most \(m\) times the substituted mass. The second-moment charge is at most \(m^2+m c/b\) times that mass. The remaining summation is geometric with ratio \((s\rho+b)^2/(4t)<1\), since cosine-power coefficients are nonnegative and sum to one. The same tail dominates the coarse rank tail. Closed Arb floor slabs and the seed enclosure are as in round 51. The first three [records](astra-feedback-52-checks.jsonl) certify these universal scalar inequalities.

Starting from zero, bound the weighted coefficient sums over all recursion trees at \(z=\rho\) by induction on iteration. Taking absolute coefficients before summing allows all the convolutions and positive weight measures above. The strict pair of radii propagates. Every fixed degree stabilizes, so the ideal geometric terms through any degree have total weighted mass at most \(b\), uniformly in the field.

## Exceptional characters and positive factors

The output on exceptional characters is repaired with exact translated \(K\)-columns as in [the seed calculus](seed-majorant-47.md). Those columns can have boundary characters outside \(\{1,\chi\}\). To include them use the *coarse* rank calculus for every tree containing such a correction. For a given tree assign the unreduced majorant \(M\) recursively by the factor \((k+j)\prod_i M_i\) at every node, without the exact circle weights. Absolute Laurent coefficients multiply separately. The term \(k=j=0\) vanishes. Through degree \(D=\lfloor\log_2(n)/8\rfloor\), all individual ranks are at most \(2^{D}\), including corrected terms, by the degree induction of round 51. At a node on arbitrary negative inputs the extra rank cost of its exceptional columns is at most \(\epsilon_n (k+j)\prod r_i\), with \(\epsilon_n=O(2^D/\sqrt n)\), by the bad-character estimate there. This estimate uses no boundary-character restriction.

For a fixed tree of \(h\le D\) nodes the terms containing at least one correction have total rank cost at most \(((1+\epsilon_n)^h-1)M\). Indeed at each node one can designate either its generic part or its correction, bounding the latter by \(\epsilon_n\) times that node's coarse cost and bounding both types of descendants in the same calculus. Sum over nonempty sets of designated nodes. Since the whole undecorated coarse tree majorant at \(z=1/2\) stays below \(b\), the sum of all terms with a correction, through degree \(D\) at \(z=\rho\), is at most
\[
 b(2\rho)^D\big((1+\epsilon_n)^D-1\big)=o(1).
\]
Thus for the *exact* truncated vector, \(\sum_{d\le D}\rho^d\|R_d\|_\infty\le b+o(1)\). This step does not equate the fiber functor with the compact-support Mellin trace at exceptional frequencies.

Set \(V=S+R_{[D]}(1)\) and let \(U\) be the matching degree truncation in the equation before applying \(K\). Then \(KU=V-S\), and the full substituted series has bounded absolute coefficient sum at \(\rho\) since \(s\rho+b+o(1)<2\sqrt t\). Evaluating the omitted degrees at one gives \(\|U-H_t(V)\|_\infty=O(\rho^{-D})\). Use \(u_0=2,\ u_i=U_i/\sqrt n\) otherwise and \(v=Ku\). At every site \(\sqrt n\,v=V-U_0 K e_0\), so these scaled entries are bounded by \(2\sqrt2+1.740+o(1)\). As \(H_t(V)\ge2\sqrt{145/8}\), both \((u\pm v)/2\) are positive. Their marked log ratio divided by two is \(O(n^{-1/2})\). After dividing by the marked product, their bulk weights have scaled defect \(O(\rho^{-D}+n^{-1/2})\). Square-root weight stability gives the same bound for the actual marked scalar. Each advertised exponent denominator \(e\) satisfies \(\rho^e>256\). [Positive-factor identification](astra-warm-51.md) · [Weight stability](marked-response.md)

## Positive four-step trials below ten

Use exactly the four degree-28 polynomial updates and the sharp square-root transfer of [round 51](astra-warm-51.md#a-sharper-square-root-comparison). At each of the four finite steps, form new radii by summing the two bounds \(G_{jk},E\) against \(|c^{[14]}_{jk}|\) at \(\rho=1\) starting from zero. With fixed polynomial depth, the aggregate of exceptional-column terms is \(O(n^{-1/2})\) uniformly on these compact floor intervals. Thus the same radii, up to vanishing errors, bound the sup norm of each vector correction. Denote the full vector bound at step \(i\) by \(B_i=s+b_i\), and the Taylor remainder bound there by \(e_i\).

For primes the first update has normalized squared increment bounded by the variance of the polynomial in the seed, since \(K\) kills constants and is an \(L^2\) contraction. The limiting prime Jacobi angle is uniform. Orthogonality of the cosine modes evaluates that limiting variance as \(\tfrac12\sum_{k>0}|c^{[14]}_{0k}|^2\). Uniformity in \(t\) follows from the finitely many fixed moments of the seed and bounded coefficient functions on the compact interval. For all fields the corresponding increment is bounded instead by half the range of the true activation, plus its truncation error, namely \((\sqrt{4t+s^2}-2\sqrt t)/2+e_0\). The later increment bounds follow by the previous Lipschitz and Taylor-remainder recurrence. On every slab the checker verifies \(B_4<2\sqrt t-e_3\) with strict slack, ensuring positivity of both actual trial factors for sufficiently large fields. The sharp transfer with these bounds gives
\[
 \limsup_{p\to\infty}\sup_{141/16\le t\le10}|m_p(t)|<0.017,\qquad
 \limsup_{q\to\infty}\sup_{79/8\le t\le11}|m_q(t)|<0.017
\]
in the second case for primes and eligible prime squares. The final two interval records verify these claims. The earlier intervals continue up to 25. These are fixed tolerances, and the decay theorem above starts at its separately stated higher floor.

1. Propagate the full pooled integer-weight distribution instead of its first two moments, bounding the omitted histogram by a weighted exponential moment. A strict invariant positive distribution below \(145/8\) extends the real decay range. Monotone iteration from zero exceeding any entry of a proposed invariant majorant refutes that majorant.
2. Test a lower-floor positive prefix by retaining the full fourth-step weight histogram and its sharper rank in the positivity and mark estimates. The success conditions are positivity at every site in the uniform argument and a transfer bound smaller than the chosen tolerance. A failed scalar upper bound rejects only that certificate. A certified nonpositive trial entry on unbounded primes rejects its eventual positivity.
