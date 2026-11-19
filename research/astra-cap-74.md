# Opposite Fourier fibers restrict periodic caps on the true primary face

Let \(Q\) be the square subgroup, \(G=\widehat Q\), and \(n=(p-1)/2\). For a sign \(\sigma\) write \(D=\{x\in Q:\chi(1-x)=-\sigma\}\). Its feasible probabilities have positional transform zero on \(D\). Write \(q_*\) for the maximal root probability and choose an actual opposite optimal probability \(r\). Reciprocity gives \(nq_*r_0=1\). The opposite transform is supported on \(D\cup\{1\}\). If \(q\) is primary optimal, \(\sum_i q_i r_i=1/n\) gives \(q_i r_i=0\) off the root. [Translated budgets](astra-localized-71.md)

## A count obstruction using every positional coset

Take any proper subgroup \(B<Q\) of prime size \(b\), put \(P=B^\perp\), and write \(H=G/P=\widehat B\). Set \(k_0=|B\cap D|\) and \(k_C=|C\cap D|\) for every exterior coset \(C=tB\). If the cap sites of an actual primary optimum contain \(P\), then
\[
 k_0+1=\big|\operatorname{supp}_H\bar q\big|
       \ \le\ \min_{C\ne B} k_C .                                    \tag{1}
\]
Here \(\bar q\) is the average of the translates by \(P\). This is necessary for any such period of the least-norm optimizer. It also applies when a noncanonical optimizer has a cap containing a translated coset of \(P\), by translating a cap point to the root before averaging.

Indeed \(\bar q\) stays optimal and is constant on each \(P\)-coset. Its positional transform on \(B\) vanishes at the \(k_0\) forbidden sites. Prime cyclic uncertainty gives its quotient support \(J\subset H\) size at least \(k_0+1\). For each \(t\in Q\) form a complex row on \(H\) by putting
\[
 U_t(j)=\sum_{i\in j} r_i\,i(t)/r_0 ,
\]
where \(j\) denotes a coset of \(P\) in \(G\). Its Fourier evaluation at \(v\in B\) equals \(\widehat r(tv)/r_0\), with \(\widehat r(z)=\sum_i r_i i(z)\). Thus its Fourier support lies in \(K_t=\{v\in B:tv\in D\cup\{1\}\}\). Complementarity with \(\bar q\) gives \(U_t(0)=1\) and \(U_t(j)=0\) on \(J\setminus\{0\}\). A nonzero function with Fourier support of size \(|K_t|\) on a group of prime size has at most \(|K_t|-1\) zeros. Consequently \(|J|\le |K_t|\) for every fiber, including \(t=1\) where \(|K_1|=k_0+1\). This proves (1) and forces both central transforms to occupy all their allowed positions. [Tao, prime cyclic uncertainty](https://arxiv.org/abs/math/0308286)

In this periodic case there is only one optimal quotient row. Any quotient optimum lifts to a feasible full row with this optimal mark. The midpoint of two such lifts is periodic and optimal, and its quotient support is their union. By (1) the two supports and their union all have size \(k_0+1\), so the supports coincide. On that support the \(k_0\) forbidden Fourier equations have rank \(k_0\) by the same nonvanishing minors. Normalization fixes the remaining scalar. Reflecting the quotient row gives another optimum, so the unique row is inversion-even.

Even without a period, let \(q\) be a true optimizer and \(J\) its occupied \(P\)-cosets. If \(r(P\setminus\{0\})<r_0\), every \(U_t(0)\ne0\). Each fully occupied nonroot coset of \(q\) still gives a zero of every \(U_t\). Its average \(\bar q\) is feasible, so \(|J|\ge k_0+1\) regardless of its mark. Therefore the number of nonroot cosets containing both a positive and a zero coordinate of \(q\) is at least
\[
 \left(k_0+1-\min_{C\ne B} k_C\right)_+ .                           \tag{2}
\]
For \(p=4b+1\) with \(b\) an odd prime there are two frequencies per coset. If the opposite optimizer has a singleton cap, the strict inequality on its mass is automatic. Thus (2) can force genuine support mismatches in pairs on the other primary face. It gives no lower weight on the occupied member.

## A weighted inequality and its high-density limitation

The following estimate allows any subgroup size, any sign-feasible \(q\) and arbitrary mark loss. Write \(v_j=\bar q_i\) for the per-site average on coset \(j\), so \(|P|\sum_jv_j=1\). Orthogonality of \(\bar q\) and \(r\) after removing their means gives
\[
 E=q_*-v_0=\sum_{i\ne0} v_{[i]}\,r_i/r_0 .                         \tag{3}
\]
In particular \(v_0>q_*/2\) implies \(r(P\setminus\{0\})<r_0\). For \(J\subset H\) containing zero let \(\mathcal V_t\) be the complex row space on \(H\) with Fourier support in \(K_t\). Define
\[
 d_t(J)=\inf_{f\in\mathcal V_t}\sum_{j\in J}|\mathbf1_{j=0}-f(j)|.
\]
If every \(v_j\ge u>0\) in \(J\), the row \(U_t\) has total error on \(J\) at most \(\sum_{[i]\in J,\,i\ne0}r_i/r_0\) by the triangle inequality. Hence
\[
 q_* - v_0\ \ge\ u\max_t d_t(J).                                    \tag{4}
\]
The bound can keep all weights by replacing \(u d_t(J)\) by the infimum of \(\sum_{j\in J}v_j|\mathbf1_{j=0}-f(j)|\).

There is an exact limitation on applying (4) only on the growing density tail from [the smooth windows](smooth-windows-72.md). If \(b\) is prime and \(b\ge(1+\eta)\sqrt p\) for fixed \(\eta>0\), every \(K_t\) has at least \(c_\eta b\) sites at sufficiently large primes. Indeed the sum of \(\chi(1-x)\) on any coset of \(B\) has magnitude at most \(\sqrt p\), by expanding the coset indicator in multiplicative characters and applying the complete Jacobi bound. The possible identity costs at most one in the sign counts. If \(J\) consists of any sites with \(nv_j>L\) together with the root, then \(|J|\le1+b/L\). For \(L\to\infty\) eventually \(|J|\le |K_t|\) in every fiber. All square minors of the prime cyclic Fourier matrix are nonzero, hence \(\mathcal V_t|_J=\mathbb C^J\). Both interpolation errors vanish exactly. This covers the prime-order quotient of any putative larger-side least-norm period in (1), because [the canonical cap mass bound](astra-face-54.md) yields \(b\ge2\sqrt n\) for sufficiently large \(p\). The whole-support count obstruction can survive even where this high-density test costs zero. Independent complex interpolation on the fibers discards positivity and the requirement that all \(U_t\) arise from one \(r\).

A mark-doubling test applies if an exterior translate of the actual central Fourier support fits the tested sign. For any subgroup size, if \(t\notin B\) and \(t\operatorname{supp}\widehat{\bar q}\subset Q\setminus D\), then \(q_*\ge2v_0\). Multiply \(\bar q_i\) by \(1+\operatorname{Re}i(t)\). It stays nonnegative with mass one because \(\widehat{\bar q}\) is supported in \(B\). Its two new support translates avoid \(D\) by the hypothesis, reality of \(\bar q\), and inversion symmetry of \(D\). Its root doubles. The condition can also be checked on \(t(B\setminus D)\) independently of the central coefficients. This can apply to approximate caps and other subgroup orders. For an exact prime-quotient candidate satisfying (1), the central support has size \(b-k_0\) while the exterior has at most \(b-k_0-1\) allowed sites, so containment is already ruled out.

## Exact finite sieve and remaining tests

The [integer checker](astra-cap-74-check.py) enumerates eligible primes through 20000 and proper prime divisors \(b\mid n\) with \(b^2\ge4n\), testing both signs. It counts the forbidden positional mask on each coset without an endpoint solve. Of 964 sign-and-divisor cases, 698 violate (1) and 266 survive. For example the plus side at \(p=53,b=13\) has \(k_0=8\) and minimum exterior count 5. The minus side at \(p=137,b=17\) has 10 and 7. These are finite period exclusions. A surviving test gives no optimizer existence or asymptotic frequency. [Exact replay record](astra-cap-74-checks.jsonl)

1. On surviving prime-order quotient candidates, use inversion symmetry, \(|J|=k_0+1\) and central Fourier minors to reconstruct candidate quotients, then impose simultaneous compatibility and positivity of the exterior fibers on the entire occupied support. For approximate caps, test the weighted defect in (4) or mark-doubling containment where available.
2. For singleton peaks retain the common positive opposite row in (3), including occupied sites below the density cutoff. On two-site fibers (2) gives exact mismatches when the opposite cap is isolated. To affect the marked-window hinge one needs to control their weights and their intersection with the marked negative set. The all-prime ordinary theta limit remains open.
