# A prime mass gap past the square-root subgroup size

Write $n=(p-1)/2$, $Q=\mathbb F_p^{\times 2}$, $G=\widehat Q$, $s(t)=\chi(1-t)$. For a sign $\sigma$, let $D=\{s=-\sigma\}$. A feasible probability $\mu$ has positional transform $F(t)=\sum_i\mu_i i(t)$ zero on $D$. Put $\alpha=\sqrt n\,\mu_0$, so the actual endpoint mark is the normalized ordinary theta of its side. The following bounds apply on its exact complementary face, including at shared zeros.

## The marked subgroup and a reciprocal forbidden-count test

Let $B\le Q$, $b=|B|$, $H=B^\perp$, $m=|H|=n/b$, and $h=\lfloor(1+\sqrt{1+4n})/2\rfloor$. If $b>h/2$ and $\alpha\ge1+\delta$ for a fixed $\delta>0$, then, uniformly through all sufficiently large eligible primes,
\[
                         \mu(G\setminus H)\gg_\delta 1.                 \tag{1}
\]
This reaches all marked subgroup sizes $m<2n/h\sim 2\sqrt n$, including the interval above the square-root size. Previous [phase alignment bounds](parallel-stationary.md) allow several cosets with total size bounded away below $\sqrt n$. Here the subgroup contains the distinguished mark.

Indeed set $e=1-\mu(H)$. If $e<1/2$, every $t\in B$ has $\operatorname{Re}F(t)\ge1-2e>0$. Hence $B\setminus\{1\}$ is monochromatic of sign $\sigma$. Its distinct differences have the same quadratic sign; after a nonsquare dilation if necessary, it is a Paley clique. Thus $b\le h$. Moreover each coset $C\ne B$ meets $D$. Otherwise each difference between $C$ and $B$ would have the allowed sign, as do differences within the two sets since $C$ is a square dilation of $B$. Their union would give a clique of size $2b>h$. The prime input is [Hanson and Petridis, Theorem 1.2](https://arxiv.org/abs/1905.09134).

The next step controls the price of assigning equal total weight to each of these forbidden fibers. Let $k_C=|C\cap D|$ and, for $i\notin H$, put
\[
 T_i=\sum_{C\ne B}\frac1{k_C}\sum_{t\in C\cap D}i(t).
\]
On each $C$ the transform from the $H$-frequencies is constant and equals minus the forbidden average of the transform of the remaining frequencies. Summing over $C\ne B$ and using quotient orthogonality gives the **exact** marked identity
\[
 m\mu_0=\mu(H)-\sum_{i\notin H}\mu_i T_i.                             \tag{2}
\]
In particular the outside mass bounds error at the mark without discarding its sign.

Uniformly for every individual $i\notin H$,
\[
 |T_i|\le C_b:=(\sqrt p+1)/b+10p/b^2.                                  \tag{3}
\]
To prove this, let $a_C=\sum_C s(t)$, $d_C=\sum_C i(t)s(t)$. Quotient Parseval gives $\sum_C |a_C|^2\le p$ and $\sum_C|d_C|^2\le p$. Each is the average of squared full Jacobi coefficients with a quotient twist, each bounded by $p$, including trivial characters. On $C\ne B$, $2k_C=b-\sigma a_C$ and the unweighted forbidden sum is $U_C=-\sigma d_C/2$, since $i|_B$ is nontrivial. Replacing $1/k_C$ by $2/b$ gives main term bounded by $(1+\sqrt p)/b$ from the full Fourier coefficient of $2\mathbf1_D=1-\delta_1-\sigma s$; $B\cap D$ is empty. Where $|a_C|\le b/2$, the absolute replacement error is at most $2|a_C d_C|/b^2$, summing to $2p/b^2$. There are at most $4p/b^2$ remaining cosets, each with replacement error at most two by $|U_C|\le k_C$ and $2|U_C|=|d_C|\le b$. This proves (3). See the [Jacobi normalization](fourier.md).

Equations (2)–(3) give $\alpha\le(b/\sqrt n)[1+(C_b-1)e]$. In the case $e<1/2$ under consideration, $h/2<b\le h$, so $C_b=O(1)$ and $b/\sqrt n\le1+O(n^{-1/2})$. This proves (1). In particular, a feasible row supported on such an $H$ is flat on $H$: its transform outside $B$ vanishes because it is constant on each coset containing a forbidden point, and its transform on $B$ equals one. Its mark is exactly $b/\sqrt n$.

## Effective support of the exterior, even with arbitrarily small weights

For a union $K$ of $r\ge1$ cosets of one frequency subgroup $H$, with fixed $r$, every complex exact sector row $z$ satisfies the uniform inequality
\[
 \boxed{\quad \|z_{K^c}\|_2^2\ll_r p^{-1/2}\|z_{K^c}\|_1^2.\quad}      \tag{4}
\]
It also applies over eligible odd prime powers with $p$ replaced by field order. Thus it controls the weight variation of the actual exterior as well as its cardinality; it cannot distinguish squares on its own. The subgroup, its index and the cosets may vary with the field.

Write the cosets as $i_j H$. Choose $v_1,\ldots,v_r$ independently and uniformly in $B=H^\perp$. Multiply the $i$-th frequency by
\[
 w_i=\prod_{j=1}^r (i(v_j)-i_j(v_j)).
\]
It annihilates $K$; off $K$ one has $\mathbb E|w_i|^2=2^r$ by character orthogonality. The positional transform of $wz$ is a linear combination of at most $2^r$ translates of $F_z$. It vanishes on the set $A$ where $s(at)=-\sigma$ for all the distinct subset products $a$ of the $v_j$, including the identity. With $k\le2^r$ distinct shifts the indicator expansion gives
\[
 |A|=n2^{-k}+O(k\sqrt p+k),\qquad
 \max_{i\ne0}|\widehat{\mathbf1_A}(i)|\le k\sqrt p+k .
\]
Repeated shifts are deleted before expanding. The terms with a nonempty set of shifts have the [twisted translate bound](parallel-torus-8.md#a-uniform-bound-for-twisted-translate-correlations) and the at most $k$ exceptional roots change the sum by at most $k$. Expanding $0=\sum_A|F_{wz}(t)|^2$ now bounds $\|wz\|_2^2\ll_r p^{-1/2}\|wz\|_1^2$. Average and use $|w_i|\le2^r$ to obtain (4); finitely many smaller orders are absorbed in the constant.

Consequently, on a supercritical prime sequence, the *actual* positive support outside every marked $H$ of the sizes in (1) has at least $c\sqrt p$ members. Moreover its normalized mass is bounded below by (1), even when $H$ is larger than $\sqrt n$. For every fixed union in (4), the alternatives are zero exterior or exterior effective support $\|z_{K^c}\|_1^2/\|z_{K^c}\|_2^2\gg_r\sqrt p$. This rules out leakage consisting solely of a handful of tiny positive entries. At square order $q=u^2$ the true plus endpoint is flat on a subgroup of size $(u+1)/2$, with zero exterior and mark tending to $\sqrt2$. The doubled clique exclusion uses primality. [Square endpoint](square-endpoint-uniqueness.md)

## Finite certificates

The [192-bit Arb checker](astra-face-46-check.py) verifies every forbidden fiber and the full transform of its reciprocal-count tag at six primes through 1289. It reuses the certified complementary active systems at 41 and 101 to evaluate (2) on actual endpoints. At 101 the larger, minus endpoint has mark between 1.12413 and 1.12414, exterior mass between 0.46426 and 0.46428, and exterior effective support between 10.49 and 10.50 for the subgroup of index five. Thus the subgroup actually carries a majority of the endpoint mass. Four of the six records certify only the test column. Floating LP solves propose supports in the two endpoint records. All reported enclosures follow from the verified systems. The [six records](astra-face-46-checks.jsonl) replay from the repository root with the script and its bundled Python environment.

## What remains

The exterior effective-support scale is still $\sqrt p$, whereas the [endpoint atom](endpoint-direction-45.md) requires effective support $\gg n/D(p)$ for the *full* probability in the sense $n\|\mu\|_2^2=o(D(p))$. A row distributing constant mass over multiple clouds of size comparable to $\sqrt p$ could meet (1) and (4) with collision much larger than $D(p)$. This describes the loss of the inequalities, without constructing a prime endpoint. Neither result bounds collision on a general positive-density, highly nonuniform support.

1. Test the exact column $T_i$ in (2) weighted by the actual complementary-face row. When $B$ is monochromatic and has $h/2<b\le h$, the upper bound $-\sum_{i\notin H}\mu_i\operatorname{Re}T_i\le1-\mu(H)+o(1)$ forces $\alpha\le1+o(1)$. A fixed excess over the right side on unbounded primes refutes this estimate. The sup-norm bound (3) gives only a constant. A family of suitable monochromatic subgroups for all primes has not been established.
2. For an exact optimal face, seek an adaptive cover $K$ by a bounded number of cosets for which $n\|\mu_K\|_2^2=o(D(p))$ and the exterior effective support is $\gg n\mu(K^c)^2/D(p)$, with diverging ratio when the exterior is nonzero. Such estimates would close the atom route. The exterior theorem guarantees only order $\sqrt p$; an unbounded sequence with $n\|\mu_{K^c}\|_2^2/D(p)$ bounded below defeats this proposed cover. The case $K=G$ provides no exterior information.
