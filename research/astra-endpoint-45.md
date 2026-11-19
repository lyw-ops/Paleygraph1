# Exact cold scores with different collision energies at every large prime

At every sufficiently large eligible prime, both Paley signs admit nonnegative spectra whose mark and all prescribed linear statistics agree exactly with those of the uniform spectrum, while their squared norms grow. The statistics may depend on the field, the actual least-norm endpoint and the entire cold Picard orbit. This gives an obstruction to estimating the endpoint collision from measured directions and approximate optimality. It allows even rows and a quantitative error in the optimal mark. The argument uses logarithmic monochromatic runs on the **actual prime mask**. It does not supply a small marked atom on the exact optimal face.

## A uniform prime estimate for the measurement fibers

Use counting norm, $j=\mathbf1/\sqrt n$, $n=(p-1)/2$, and real even feasible rows $z\ge0$ in $U_\sigma$ with $\langle j,z\rangle=1$. Fix any $k\ge0$ real linear tests on these rows. Put $m=\lfloor\log_2(p)/4\rfloor$. There exists an even feasible $Z$ satisfying every test exactly as $j$ does, such that
\[
 \|Z\|^2\ \ge\ \frac{2(m+1)^2+1}{6(m+1)(k+1)}.                       \tag{1}
\]
The bound holds for either sign, even when the tests are chosen after the true endpoint is known.

Indeed, the [prime logarithmic-run lemma](quadratic-fourth.md#unbounded-allowed-energy-with-vanishing-residual) supplies $t\in Q$ of order exceeding $2m$ with $\chi(1-t^a)=\sigma$ for $1\le a\le m$. Its proof counts admissible $t$ by expanding the simultaneous sign constraints. The largest selected exponent has a primitive root of unity which occurs simply only in its factor. Thus the character sum bound applies with error $O(m^2\sqrt p)$ against a main term $p/2^{m+1}$. Lower orders remove only $O(m^2)$ choices. Inversion gives the same signs at the negative powers. Let
\[
 F_i=\frac{1}{\sqrt n(m+1)}
       \left|\sum_{a=0}^m\eta_i(t)^a\right|^2 .
\]
Feasibility follows from its displayed square and its positional support. Since the $2m+1$ powers are distinct, Parseval gives
\[
 \|F\|^2=1+2\sum_{a=1}^m(1-a/(m+1))^2
        =\frac{2(m+1)^2+1}{3(m+1)}.
\]
The even translates $F_h=(T_hF+T_{-h}F)/2$ average to $j$. Positivity gives $\|F_h\|^2\ge\|F\|^2/2$ for **every** $h$. By Carathéodory's theorem in the space of test values, a convex combination $Z=\sum_{a=1}^s b_aF_{h_a}$ with $s\le k+1$ realizes the test values of $j$. All cross inner products are nonnegative. Thus $\|Z\|^2\ge(\|F\|^2/2)\sum b_a^2\ge\|F\|^2/[2(k+1)]$. If strict positivity is desired, replacing $Z$ by $(Z+j)/2$ preserves all the equalities and a quarter of $\|Z\|^2-1$.

## What fails near the actual least-norm endpoint

Let $X$ be the actual least-norm endpoint on the larger-theta side, $\alpha=X_0$. Include the marked coordinate and the test $z\mapsto\langle X,z\rangle$ in the budget $k$. For $0<\epsilon<1$ define
\[
 X^{\rm unif}=(1-\epsilon)X+\epsilon j,\qquad
 X^{\rm alt}=(1-\epsilon)X+\epsilon Z.
\]
Their common mark is $\alpha-\epsilon(\alpha-1/\sqrt n)$. They give exactly the same answers to **every** chosen test. Their probabilities are each at total variation distance at most $\epsilon$ from $X/\sqrt n$. Furthermore,
\[
 \|X^{\rm alt}-j\|^2-\|X^{\rm unif}-j\|^2
 =\epsilon^2(\|Z\|^2-1).                                                \tag{2}
\]
Indeed $Z-j$ is orthogonal to $j$ and $X$. This removes the cross term even if the true endpoint energy diverges.

Take all signed cold projections $u_t=\sigma P_\sigma v_t$ and wrong-sign sums $\sum_{s<t}(|v_s|-\sigma v_s)$ for $1\le t\le D(p)$, as well as the two tests above. Then $k\le2D(p)+2$. The two rows have identical signed directional energies and identical wrong-sign occupations simultaneously throughout the proved window. Their squared mismatch terms in [the completed-square identity](astra-critical-44.md) differ by the full collision difference. At $\epsilon=m^{-1/4}$ the mark loss and probability distance tend to zero, and (1)–(2) give a collision difference of order **at least** $\sqrt{\log p}/D(p)\gg D(p)$. More generally growth beyond the window follows if $\epsilon^2\log p/((k+1)D(p))\to\infty$. The strict positive variant obeys the same asymptotic lower bounds up to an absolute factor.

If a fixed floor $0<\tau<1$ has a supercritical subsequence $\alpha\ge a_p+\delta$, with $a_p=\sqrt{1+(1-1/n)\tau}$ and $\delta>0$, set $\epsilon=(\alpha-a_p)/(\alpha-1/\sqrt n)$. This fraction is bounded below since $\alpha$ is uniformly bounded by the Jacobi entry estimate. Both rows are now on the **exact same critical slice** and still agree in every specified cold statistic. Their collision difference is $\gg\log p/(k+1)$. The premise about that prime subsequence is conditional. The near-optimal construction above has no such premise.

Equations (1)–(2) obstruct an upper bound on the full collision of **every row in these fibers**. They preserve the one-dimensional score upper route itself and the exact identity $\omega=\alpha^2/\|X\|^2$ for the unique least-norm selection. In particular the construction makes no pair of optimizers with different least norms. At the optimal mark, complementary positivity imposes exact zeros on the opposite support. A vanishing mass error or finitely many orbit projections permits the perturbations above.

## A finite critical-slice certificate

The [384-bit Arb replay](astra-endpoint-45-check.py) uses the [strict minus row](astra-rooted-43.md) at $p=101$ and its exact dilution to the $\tau=1/4$ mark. The starting row here is a certified supercritical feasible row; the finite calculation does not require an identified theta optimum. With $m=4$ the shifts $3,4,23,24$ of the even Fejér row have a positive combination matching the uniform mark, the true cold depth-three score and the pairing with the strict row. The weights solve the exact four-by-four real linear system with the mass constraint included. Arb certifies invertibility and the positive weights. Substitution gives positive rows with the common critical normalized mark $1.11579568\ldots$, common signed cold score $2.27269716\ldots$, and collision difference strictly greater than $0.00006193$. The exact score equality follows from the defining linear system and sector orthogonality. The [record](astra-endpoint-45-checks.jsonl) encloses all reported values.

## Ranked next tests

1. Keep the actual endpoint support $S$ in any atom certificate. On its bulk $I=S\setminus\{0\}$, use [the exact centered-sampling formula](parallel-kernel-11.md#centering-on-the-actual-bulk-support). With $b=X/\alpha$, $\ell=\sqrt n/\alpha-1$, the reciprocal atom equals $1+\ell^2/|I|+\|b_I-(\ell/|I|)\mathbf1_I\|^2$. Proving both nonconstant terms $o(D(p))$ on the larger side closes the atom route. A prime subsequence on which either term is $\Omega(D(p))$ refutes this sufficient condition and identifies whether support size or the variation of its weights causes failure.
2. For the directional route, keep the sign and use the actual $X$ in $E_t=\langle X-j,u_t\rangle_+^2/\|u_t\|^2$, taking zero at vanishing direction. One growing $t\le D(p)$ per prime with $E_t/t\to0$ suffices by round 44. A subsequence with a common positive lower bound for every growing choice of $t$ excludes that route. The construction above allows large collision changes with identical $E_t$ at every tested depth. Thus if the atom test fails, these directional measurements retain information that a collision upper bound can discard.
