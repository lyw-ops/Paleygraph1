# Constraints on bounded sign defects at prime order

Let $B\le Q\subset\mathbb F_p^\times$ have order $b$, and let $m=|Q/B|=(p-1)/(2b)$. Write $F(C)=\sum_{a\in C}\chi(1-a)$. We prove a uniform growing gap to the square-root bound:

$$\sqrt p-\max_{B\le Q,\ C\in\mathbb F_p^\times/B}|F(C)|\longrightarrow\infty.$$

In particular $b-\max_{C\in Q/B}|F(C)|\to\infty$ when $b\ge\sqrt p-O(1)$. The [annihilator calculation](unshifted-cosets.md) converts this into vanishing marked response for prescribed annihilators at the critical scale. The proof uses the quantitative idempotent theorem and reduction of Jacobi sums modulo $p$.

For an individual square coset denote its sign deficit by $k=b-|F(C)|$. In the near-square enumeration and the small-defect inequalities below, $p=b^2+jb+1$ for a bounded integer $j$ and $2m=b+j$.

## Exact correlations

In the [independent ChatGPT check](chatgpt-2026-11-17.md), the exact second moment extended to autocorrelations at every lag. For a primitive generator $g$ put $f_t=F(g^tB)$ on $\mathbb Z/(2m)\mathbb Z$. The unnormalized Fourier coefficient of $f$ at a character $\eta$ of the quotient is the Jacobi sum $J(\eta,\chi)$. Its modulus is $\sqrt p$ except at $\eta=1,\chi$, where its value is $-1$. Therefore

$$\sum_t f_t f_{t+h}=p\mathbf1_{h=0}-b(1+(-1)^h).$$

The identity follows by taking the inverse transform of the squared modulus. Also $f_{-t}=(-1)^t f_t$ by inversion, and $\sum_t f_{2t}=-1$. These equations describe all lags and the square and nonsquare parts simultaneously.

### What the correlations alone allow

ChatGPT gave an integer comparison sequence on $\mathbb Z/(2\ell)\mathbb Z$ for every prime $\ell\equiv3\pmod4$. Set $b=2\ell$ and formally set $P=b^2+1$. Give index $0$ value $b-3$, every other even index value $-2$, and odd index $t$ value $2\chi_\ell(t)$, with $\chi_\ell$ the Legendre symbol modulo $\ell$. The even and odd sums are $-1$ and $0$ respectively. Inversion leaves the even part fixed and negates the odd part. At every nonzero even lag the two parts contribute $-2b+4$ and $-4$ respectively, using quadratic autocorrelation over $\mathbb F_\ell$. Odd lags vanish by inversion, and the zero-lag sum is $P-2b$. Thus the full correlation formulas and the relevant parity and inversion constraints permit a fixed deficit of $3$. This comparison sequence is abstract, including when $P$ is prime.

For $\ell=7$, $P=197$ is prime. The even-index Fourier coefficients of the comparison sequence are rational. The cyclotomic argument below, with $d=7$, shows that no genuine coset-sum sequence over $\mathbb F_{197}$ can have those coefficients. This separates the modular constraint from the exact autocorrelation method.

## Structure after deleting a large coefficient

Suppose $C=g^{2a}B$ is a self-inverse square coset. Write $\sigma\in\{\pm1\}$ for the sign of $F(C)$ and let $u_h=\sigma f_{2h+2a}$ on $\mathbb Z/m\mathbb Z$. Then $u$ is even, $u_0=x=b-k$, and $\sum_h u_h=-\sigma$. Write $U_\ell$ for its unnormalized Fourier transform. Restricting $f$ to even indices averages $J(\eta,\chi)$ and $J(\eta\chi,\chi)$, where $\eta(g^2)=e^{2\pi i\ell/m}$. Inversion shows $f_{-t}=(-1)^t f_t$, so the two sums are complex conjugates. The shift and sign multiply their real part by a sign, since $2a=0$ in $\mathbb Z/m\mathbb Z$. In particular $U_\ell$ is real and $U_\ell\le\sqrt p$.

Set $L=\sqrt p-x$ and $r=u-x\delta_0$. Then $\widehat r_\ell=U_\ell-x\le L$ and has mean zero over $\ell$. Consequently the Fourier algebra norm of the integer vector $r$ is at most $2L$. When $k$ and $j$ are bounded, [Sanders's quantitative idempotent theorem](https://arxiv.org/abs/1610.07092) writes $r$ as a signed sum of boundedly many coset indicators in $Q/B$, with the bound independent of $b$. This is an additional necessary constraint on any bounded-defect sequence. It still allows contributions from many possible subgroups as the quotient varies.

There is also a sharp bound on each off-center entry. For $h\ne0$, Fourier inversion and $U_0=-\sigma$ give

$$\left|u_h+\frac{\sqrt p+\sigma}{m}\right|
\le \frac1m\sum_{\ell\ne0}(\sqrt p-U_\ell)
=L-\frac{\sqrt p+\sigma}{m}.$$

To see the first inequality, subtract the constant sequence $\sqrt p$ in Fourier coordinates, whose inverse transform is supported at $h=0$. All deficits at nonzero frequency are nonnegative. The center of the inequality tends to $-2$ and its radius is $k+j/2-2+o(1)$.

## A cyclotomic obstruction for small defects

For all sufficiently large orders with $j$ bounded, the following exclusions hold for self-inverse square cosets:

$$k+j/2\ge 4 \quad (b\text{ even}),\qquad
k+j/2\ge 7/2 \quad (b\text{ odd}).$$

For odd $b$, $j$ is odd since $2m=b+j$. If $k+j/2\le5/2$, the interval bound forces $u_h=-2$ for every $h\ne0$. All but possibly one of these entries, however, are odd because the corresponding cosets do not contain $1$. This gives the bound.

For even $b$, $j$ is even. If $k+j/2\le3$, the interval bound gives $u_h=-2$ whenever $h\ne0$ and $g^{2h+2a}B\ne B$, since the entries there are even. A possible odd entry away from the origin is at $h=m/2$, because $C$ is self-inverse. A vector constant away from $0$ and possibly $m/2$ has rational Fourier coefficients, so all $U_\ell$ would be rational.

To exclude this, choose a character $\eta$ of prime-power order $d\mid m$ with $d$ tending to infinity. Such a choice exists along a subsequence as $m\to\infty$, since bounded prime powers could only give finitely many $m$. View $J(\eta,\chi)$ in $\mathbb Q(\zeta_d)$, where the quadratic character takes rational values. Choose $\eta(g)=\zeta_d$ and reduce at the prime over $p$ given by $\zeta_d\mapsto g^{(p-1)/d}$. For any $t\in(\mathbb Z/d\mathbb Z)^\times$ with $1\le t<d$, the reduction of $J(\eta^t,\chi)$ equals

$$\sum_{v\in\mathbb F_p^\times} v^{t(p-1)/d}(1-v)^{(p-1)/2}.$$

The binomial expansion has no exponent divisible by $p-1$ when $t<d/2$. When $t>d/2$, it has exactly one, with a nonzero coefficient modulo $p$. Thus the reduction vanishes precisely on the lower half of the units. If the real part of $J(\eta,\chi)$ were rational, $J(\eta,\chi)$ would satisfy a rational quadratic with constant term $p$. Its Galois orbit would consist of itself and its conjugate, which have different reductions by the calculation for $t=1,-1$. The lower half of the units would then be its stabilizer, hence a subgroup. This fails for all sufficiently large prime powers. For odd $d$, the units $2$ and a unit in $(d/4,d/2)$ both lie in the lower half, but their product lies in the upper half. For $d$ a power of two, use $3$ and an odd integer in $(d/6,d/3)$. This contradiction proves the even-order bound.

The same reduction gives a degree statement for an odd prime power $d$. A unit stabilizing the real part must preserve the lower half of the units or exchange the two halves. In the preserving case, let $S$ be the sum of the lower-half units modulo $d$. Modulo the prime divisor of $d$, $S$ equals the sum of all integers from $1$ through $(d-1)/2$, which is $-1/8$ modulo that prime. Hence $S$ is a unit modulo $d$, and $tS=S$ forces $t=1$. Multiplication by $-1$ exchanges the halves, so the full stabilizer is $\{1,-1\}$. Thus the real part generates the maximal real subfield of $\mathbb Q(\zeta_d)$. In particular, a decomposition of the residual into coset indicators cannot use only bounded-index subgroups when $m$ has a growing odd prime power divisor. At characters of such an order, all bounded-index pieces have zero transform.

## Excluding every bounded deficit

Suppose for contradiction that along a sequence with $p\to\infty$, a coset has $x=|F(C)|=\sqrt p-O(1)$. The autocorrelation at zero implies that $C$ is self-inverse for all sufficiently large $p$: otherwise inversion gives two terms of this size, whose squares sum to more than $p-2b$. A self-inverse nonsquare coset has sum zero by $f_{-t}=(-1)^tf_t$, so $C=g^{2a}B$ is a square coset. Put $c=F(C)$. The inequalities $x\le b$ and $2b\le p-x^2=O(\sqrt p)$ give $b\asymp\sqrt p$ and $m\asymp\sqrt p$. Hence the same exact identity gives

$$\sum_{t\text{ odd}} f_t^2\le p-2b-c^2=O(m).$$

By the Fourier algebra argument above and Sanders's theorem, the even sequence $e_h=f_{2h}$ is of the form

$$e=c\delta_a+\sum_{i=1}^s\varepsilon_i\mathbf1_{W_i},$$

where $s$ is bounded uniformly along the sequence, $\varepsilon_i=\pm1$, and each $W_i$ is a coset of a subgroup of $\mathbb Z/m\mathbb Z$. Denote its size by $h_i$ and a representative by $a_i$. Use $\xi=g^b\in\mathbb F_p^\times$, of order $2m$, to take the Fourier transforms in $\mathbb F_p$:

$$J_t=\sum_v f_v\xi^{tv},\qquad E_t=\sum_{h\in\mathbb Z/m\mathbb Z}e_h\xi^{2th}.$$

Here $J_t=\sum_{v\in\mathbb F_p^\times}v^{bt}(1-v)^{(p-1)/2}$. The binomial expansion gives $J_t=0$ for $1\le t<m$ and $J_0=J_m=-1$. The identity $J_t+J_{m+t}=2E_t$ follows by selecting the even indices of $f$. Fourier inversion at an odd index $v$, with $Z_v=\xi^{-v}$, now gives

$$-m f_v=\sum_{t=1}^{m-1} E_t Z_v^t\quad\text{in }\mathbb F_p.$$

For one coset $W$ of size $h$ with representative $a'$, its Fourier transform on the even positions is zero unless $h\mid t$, and equals $h\xi^{2a't}$ when $h\mid t$. Its contribution to the last display is therefore

$$h\sum_{r=1}^{m/h-1}(\xi^{2a'}Z_v)^{hr}
=h\left(\frac{2}{1-(\xi^{2a'}Z_v)^h}-1\right).$$

The geometric sum uses $(\xi^{2a'}Z_v)^m=-1$ for odd $v$, so the displayed denominator is always nonzero at a tested point. The peak contributes the same expression with $h=1$, $a'=a$, and multiplier $c$.

Pass to a subsequence on which $s$ is fixed and each index $m/h_i$ is either fixed or tends to infinity. For the fixed indices let $D$ be their least common multiple, with $D=1$ when there are none. Then $D\mid m$. Restrict $v$ to the odd residue class $1\pmod{2D}$ in $\mathbb Z/(2m)\mathbb Z$. There are $m/D$ such points. All terms with fixed index become constants there, since $\xi^{h_i}$ has order $2m/h_i$. The terms whose indices tend to infinity have $h_i=o(m)$. Thus on that residue class $-mf_v$ is the value of a rational function $R(Z)$ over $\mathbb F_p$, with a denominator of degree at most $1+\sum_{i:,m/h_i\to\infty} h_i=o(m)$. For any constant $y$, a numerator of $R(Z)-y$ has degree at most the same bound.

The $O(m)$ square sum implies that a positive proportion of the $m/D$ chosen indices have $f_v$ in a fixed bounded interval of integers. Some integer value therefore occurs at $\gg m$ distinct points of the residue class. The constant may depend on the sequence through $D$ and the square-sum bound. Reducing modulo $p$, the numerator of $R(Z)-y$ for this value must have more roots than its degree, so $R$ would be constant.

However, the peak has a simple pole at $Z_0=\xi^{-2a}$, with residue $-2Z_0c$. A retained coset term of size $h_i$ has a pole there precisely when $a\in W_i$. Its residue is then $-2Z_0\varepsilon_i$, because the derivative of its denominator at the pole is $-h_i/Z_0$. The sum of the residues is

$$-2Z_0\left(c+\sum_{i:,m/h_i\to\infty,\ a\in W_i}\varepsilon_i\right)\ne0\qquad\text{in }\mathbb F_p.$$

Indeed $|c|=\sqrt p-O(1)$ and the other sum has uniformly bounded absolute value, so the integer in parentheses is nonzero and has absolute value less than $p$ for large $p$. This contradicts constancy. The proof uses a modular rational function on the nonsquare cosets and the ordinary integer second moment to force its repeated values.

In the regime $b\sim\sqrt p$ with $b\ge\sqrt p-O(1)$, this rules out an order-one marked response from a single prescribed unshifted coset at zero and clipped fixed-depth backgrounds. When $\sqrt p-b$ grows, the gap below $\sqrt p$ alone gives no growing lower bound on the sign deficit. The true stationary diagonal across all primes still needs a separate estimate.

### An explicit order of growth

The same argument gives, for any fixed $\epsilon>0$, a uniform bound

$$\sqrt p-\max_{B,C}|F(C)|\gg_\epsilon (\log\log\log p)^{1/(4+\epsilon)}.$$

Here is the quantitative choice of residue class and denominator. Put $\Delta=\sqrt p-|F(C)|$. A sequence violating this bound has $\Delta=o((\log\log\log p)^{1/(4+\epsilon)})$. In particular, the large entry again lies on a self-inverse square coset, $b\gg\sqrt p$, and $b\le\Delta\sqrt p$ by the second moment. Now $m\gg\sqrt p/(1+\Delta)$ and $\sum_{v\ {m odd}} f_v^2/m=O((1+\Delta)^2)$. Choose an integer $T\asymp 1+\Delta$ with $T^2\ge 2\sum_{v\ {m odd}}f_v^2/m$ and set $M=2T+1$.

Sanders's bound with algebra norm $2\Delta$ gives a number of coset terms $s\le\exp(O_\epsilon((1+\Delta)^{4+\epsilon}))$. Start with $D=1$ and inspect the indices $d_i=m/h_i$ in increasing order. Incorporate an index into $D$ by taking the least common multiple if $d_i\le AD$, where $A=8M(s+1)$. Stop at the first larger index. Each incorporation replaces $D$ by at most $AD^2$, so the final $D\le A^{2^s-1}$. Every remaining term has $h_i<m/(AD)$. There is an odd residue class modulo $2D$ with mean square at most the overall mean square. On it, some integer value of $f_v$ repeats at least $m/(2MD)$ times. The rational function obtained by keeping the remaining terms and the peak has numerator and denominator degrees bounded by $1+sm/(AD)$. The root count contradicts its nonzero residue as soon as $m>8MD$ and $|F(C)|>s$. The latter also ensures the residue numerator is nonzero modulo $p$ for sufficiently large $p$ in a violating sequence.

Indeed on that sequence $s=(\log\log p)^{o(1)}$ or smaller, so $\log(8MD)\le \log(8M)+2^s\log A=(\log p)^{o(1)}$ (or is bounded). Thus both inequalities hold eventually, yielding the uniform rate. The estimate controls a very small range of sizes below $\sqrt p$ as well.

## Exact prime enumeration

The [enumeration script](../coset_defects.py) tests all $2\le b\le8000$ and $|j|\le8$ with prime $p=b^2+jb+1$, $p\equiv1\pmod4$, and $b\mid(p-1)/2$. It computes the two self-inverse coset sums when both exist, using Euler's criterion and generating each coset by modular multiplication. The [recorded scan](../data/coset-defects.csv) has 12,516 cosets from 7,472 prime–subgroup pairs, with maximum prime 64,048,001.

| Subgroup range | Cosets | Smallest deficit | Largest $|F(C)|/b$ |
|---|---:|---:|---:|
| $b\ge100$ | 12,216 | 72 | 0.33333 |
| $b\ge1000$ | 10,435 | 856 | 0.14826 |
| $b\ge4000$ | 5,678 | 3,805 | 0.06735 |
| $b\ge7000$ | 1,397 | 6,749 | 0.05390 |

These are exact coset sums within the stated search range, with the last column rounded. The 253 rows at primes below 7,000 were independently checked via the full positional sign masks. The all-lag correlations and modular Jacobi reductions were checked at six prime–subgroup pairs, and the comparison sequence at seven values of $\ell$. The modular rational formula and all subgroup terms were checked at every odd index in four cases, including $p=197$ where the abstract comparison fails it at six odd indices. The asymptotic bound grows much more slowly than the gaps suggested by the scan.
