# Repairing a quotient law with the kernel on the measured head

Use the original filtered list, companion sign and good-terminal recurrence of [round 98](astra-quotient-98.md), the actual signed exterior block prices of [round 99](astra-quotient-99.md) and the [shrinking-root inequality](quotient-floor-99.md). In particular the original list still has its fixed positive root filter. For each candidate let $b=|G/L|$, $J=\lfloor D(p)/8\rfloor$, $A=8/c_0$, $s=AJ/\log J$, and $S=\{R:v_R>s\}$ for the flat signed prefix, using the original block denominator and legal per-time erasures. Write $0$ for the root on the quotient. The following trial takes two linear solves on the head and scans the original quotient. On a measured finite head it gives a root that exceeds every allowed-clique projection.

## A repair using two columns

Let $P$ be the real orthogonal Fourier projector on the identity and the allowed companion frequencies in $B=L^\perp$, with counting inner product on the quotient. In additive notation its entries are $P_{rt}=b^{-1}\sum_{z\ \mathrm{allowed\ or\ identity}}(r-t)(z)$, real by inversion. The head itself need not be symmetric. Put
\[
 G=P_{SS},\qquad Q=P-P_{:S}G^\dagger P_{S:},\qquad h=Q\mathbf1 .
\]
Then $Q$ projects onto the allowed sector with exact zeros on $S$. Indeed $P_{:S}$ has Gram matrix $G$, and its orthogonal complement inside the range of $P$ consists precisely of allowed vectors vanishing on $S$. The Moore–Penrose inverse covers singular Gram matrices, and the empty head uses $Q=P$.

Take $k=Qe_0$, or $k=Qu$ for an original allowed unit-mass law of fixed root. For any desired positive floor $\eta$, test whether a real scalar $t$ satisfies
\[
 k_r+t h_r\ge0\quad(r\notin S),\qquad
 k_0+t h_0>0,\qquad
 k_0+t h_0\ge \eta(\langle\mathbf1,k\rangle+t\|h\|_2^2).              \tag{1}
\]
This is an interval intersection, including zero slopes. A successful test gives a legal probability by dividing $k+th$ by its positive counting mass. The mass formula uses $Q^2=Q$. Explicitly $h=\mathbf1-P_{:S}G^\dagger\mathbf1_S$; the second right-hand side in the Gram solve is $P_{S0}$ for the root column and $u_S$ for an original law. The background can have negative entries. Formula (1) retains all those inequalities.

Here is one quantitative target for applying the second version through primes. Suppose there are fixed constants $c,C>0$ with $c\le h_r\le C$ off the true head, $k_0\ge c$, and the maximum negative part of $k$ is $o(J/b)$. Take $t=\|k_-\|_\infty/c$. Positivity holds, the root is at least $c$ before normalization, and the mass is at most $C+tb=o(J)$ since $\langle\mathbf1,k\rangle=\langle h,u\rangle\le C$ and $\|h\|_2^2\le b$. Thus the normalized root exceeds $A/J$ eventually. These bounds on the repaired columns are sufficient hypotheses; (1) also works at mixed-sign backgrounds. At $\eta=A/J$ success of either version bounds the flat price divided by the root by $J^2/\log J$. The independent one-sided triangular bound is still needed, with the actual weights $2(J-1-j)/(J(J-1))$ and its own permitted erasure.

## Finite separation from all allowed cliques

At $p=769$, $m=8$, $b=48$, $J=16$, the actual plus signed prefix with $A_j=\{2+2j\}$ has $S=\{10,12,36,38\}$ at cutoff $6/5$. Here $k=Qe_0$ and $t=27/100$ give a strictly positive law off the head with normalized root in $[0.036664706,0.036664707]$. The best root among **all** individual allowed-clique squares vanishing on this same head is below $0.022777$. The bound extends to mixtures of clique squares because each nonnegative component must vanish on every deleted site. Thus the two-column test can certify a floor, for instance $1/32$, beyond that entire class.

The [384-bit checker](astra-root-100-check.py) first replays the true orbit and rounded dual of round 99. It solves the four-by-four Gram system and checks every off-head sign. Head zeros follow exactly from the projection. To bound all clique trials translate any positional clique to contain the identity, which leaves its optimal root unchanged by the common phase of each head evaluation. A recursion enumerates all 828 such nonempty cliques. For each $D$, the numerator of [round 99, (3)](astra-quotient-99.md) is the squared distance from the constant vector on $D$ to the span of the head waves. Testing one rounded complex linear combination gives an outward upper for this distance, including singular cases. Separately, the true head here is symmetric, so inversion orbit masses with forbidden cosine moments zero give actual probabilities. The checker selects a square moment basis numerically, solves its exact trigonometric system with Arb, and verifies strictly positive orbit masses. This gives
\[
             0.076455042 < C(S) < 0.076456
\]
where the upper is the previous full-sector dual. [Replay record](astra-root-100-checks.jsonl)

Every positive-root avoiding law in this example also has support generating the full quotient. A proper supporting subgroup is contained in one of orders 16 and 24. In subgroup coordinates $j\mapsto48j/d$, every forbidden position imposes a zero on its residue modulo $d$. At $d=16$ the only surviving frequencies are 0 and 8. A law has equal values at 0 and at the deleted $j=4$.

At $d=24$ the surviving frequencies up to inversion are $0,4,5,8,10$, and the deleted indices are $\pm5,\pm6$. Use an even test supported at $0,\pm1,\pm5,\pm6,\pm11$, with respective values
\[
 1,\quad a,\quad -1/\sqrt3,\quad -1/2,\quad d',
 \qquad a+d'=1/\sqrt3,\quad
 a-d'=\frac{2\cos(\pi/12)/\sqrt3-1}{2\cos(5\pi/12)} .
\]
Both $a,d'>0$. Its cosine sums at all five surviving frequencies are zero: at 0,4,8 this uses $a+d'=1/\sqrt3$; at 10 the sum is $2-2=0$; at 5 it vanishes by the specified difference. Its pairing with a supported avoiding law is therefore zero but dominates that law's root. This proves the subgroup assertion. The finite cutoff tests the construction; it is not an asymptotic $AJ/\log J$ calculation.

1. On each original candidate evaluate (1) on its genuine $AJ/\log J$ head, using the original optimizing law as well as the root column. A through-prime lower $A/J$ removes the signed flat obligation in the small-triangular branch. An empty interval rules out only that chosen family.
2. Test the one-sided opposite-sign triangular sum on the same recurrent block. Neither its through-prime upper nor general retention of the shrinking floor follows here. The finite-power escaped branch and the ordinary theta limit remain open.
