# Folded support bounds and unstable marked sampling at prime order

For [Randomstrasse101 Problem 26](https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/), a bounded cofactor in $n=d\ell$, with $\ell$ prime, gives an improved positive density bound for the actual endpoint support. If $d=2$, its asymptotic density is at least $3/8$. The bound uses all positional cosets of the order-$\ell$ subgroup. There are also exact opposite-sector directions on genuine prime inputs with mark $-1$ and vanishing centered leakage on sets of density $8/15+o(1)$. Restriction to these sets is injective, including when they are lifted from a subgroup of fixed index. The constructed sets cannot themselves support a feasible spectrum of the required mark and mass. The centered term for the actual endpoint remains open.

## Notation

Let $p\equiv1\pmod4$ be prime, $Q=\mathbb F_p^{\times2}$ have order $n=(p-1)/2$, and $s(x)=\chi(1-x)$ on $Q$. Put $D_\tau=\{x\in Q:s(x)=\tau\}$. In the [Fourier convention](fourier.md), an affine spectrum of sign $\sigma$ has positional transform zero on $D_{-\sigma}$. The zero-mean space $V_\tau$ consists of spectra whose positional transform is supported on $D_\tau$. For the least-norm optimum $X$ of sign $\sigma$, set $\alpha=X_0$, $b=X/\alpha$, $I=\{i\ne0:b_i>0\}$, $m=|I|$, and $L=\sum_I b_i=\sqrt n/\alpha-1$. The norm problem is to bound
$$
 H=\|b_I\|_2^2=\frac{L^2}{m}+D,\qquad
 D=\sup_{v\in V_{-\sigma},\,\sum_I v_i=0,\,\|v_I\|_2\le1}(-v_0)^2 .
$$
The support and sign conditions in this identity come from the paired endpoint. [Marked kernel and centering](parallel-kernel-11.md#centering-on-the-actual-bulk-support)

## What folding says about the exact support

Suppose $n=d\ell$ with $\ell$ prime and $\gcd(d,\ell)=1$. Fix a generator $\beta$ of $Q$, write the positional point as $\beta^{\ell a+dt}$ for $a\in\mathbb Z/d$, $t\in\mathbb Z/\ell$, and index frequency coordinates by $(r,h)=(i\bmod d,i\bmod\ell)$. Let $\xi=e^{2\pi i/d}$, $\zeta=e^{2\pi i/\ell}$. For any prescribed forbidden positions, put
$$
 B_a=\{t:\beta^{\ell a+dt}\text{ is forbidden}\},\qquad
 K=\min_a |B_a|.
$$
The evaluation equations say
$$
 \sum_{r,h} b_{r,h}\xi^{ar}\zeta^{th}=0 \qquad(t\in B_a).
$$

**Rank claim.** If a frequency mask has at most $K$ coordinates in every class $r$, its columns in the forbidden-position matrix are independent over $\mathbb C$.

For each $a$, take any $K$ rows. Apply the triangular Newton divided-difference transformation to the evaluations at the distinct nodes $\zeta^t$, using their chosen order. In the resulting row of order $k$, the entry in column $(r,h)$ is $\xi^{ar}$ times the $k$-th divided difference of $z^h$, where $0\le h<\ell$. This is the complete homogeneous polynomial of degree $h-k$ in the $k+1$ nodes, or zero if $h<k$. In particular it is integral over $\mathbb Z$. Reduce the transformed entries by $\zeta\mapsto1$ and $\xi\mapsto\bar\xi$ for a primitive $d$-th root $\bar\xi$ in $\overline{\mathbb F_\ell}$. Such a reduction exists since $\mathbb Z[\xi,\zeta]=\mathbb Z[\xi\zeta]$ and $\Phi_{d\ell}(z)\equiv\Phi_d(z)^{\ell-1}\pmod\ell$. The latter congruence follows by reducing $\Phi_{d\ell}(z)\Phi_d(z)=\Phi_d(z^\ell)$. The transformed entries reduce to $\bar\xi^{ar}\binom{h}{k}$. Fourier inversion in $a$ for each $k$ splits the matrix by $r$. In a class with $q\le K$ columns, the first $q$ rows are evaluations of the polynomials $\binom{h}{k}$, $0\le k<q$, at distinct $h$ modulo $\ell$. Their leading coefficients $1/k!$ are nonzero, so the evaluation matrix is invertible. The reduced matrix therefore has full column rank, which gives full rank before reduction and before the divided differences.

A second test uses the common forbidden columns. Let $R=\{r:b_{r,\cdot}\ne0\}$, $q=|R|$, and let $C_R$ be the set of $t$ such that the rows $a$ with $t\in B_a$ have full rank on the $q$ columns $R$ of $(\xi^{ar})$. On $C_R$ each polynomial $\sum_h b_{r,h}z^h$ with $r\in R$ vanishes at $z=\zeta^t$. Prime cyclic uncertainty thus forces each active class to have at least $|C_R|+1$ nonzero coordinates. At least one class has at least $K+1$ by the rank claim. These are simultaneous bounds
$$
 |\operatorname{supp}b|
 \ \ge\ \max(K,|C_R|)+1+(q-1)(|C_R|+1).                         \tag{1}
$$
They hold also for signed and complex affine spectra. [Tao, prime cyclic uncertainty and Chebotarev's theorem](https://arxiv.org/abs/math/0308286)

For $B_a$ the Paley forbidden sets, the sign patterns across all $d$ positions in a column are equidistributed up to $O_d(\sqrt p)$ in each count. More generally, let $A\le Q$, and take distinct $c_1,\ldots,c_k\in \mathbb F_p^\times$. The number of $x\in A$ with each $\chi(1-c_jx)$ equal to a prescribed sign is
$$
 |A|\,2^{-k}+O(k\sqrt p+k).                                    \tag{2}
$$
To see this, expand the product of the $k$ sign indicators, allowing an $O(k)$ correction at the zeros of the linear factors. Average the multiplicative characters trivial on $A$ to impose the subgroup condition. For a nonempty sign subset, multiply the corresponding quadratic character factors and the subgroup character. This is the evaluation of a primitive multiplicative character at a polynomial with at most $k+1$ distinct roots, counting a possible root at zero. The multiplicity at any selected $c_j^{-1}$ is $(p-1)/2$, so the Weil bound applies uniformly to the complete sum. The trivial sign subset contributes exactly $|A|\,2^{-k}$. [Weil, *On Some Exponential Sums*](https://pmc.ncbi.nlm.nih.gov/articles/PMC1079093/)

In particular, for fixed $d$, $K=\ell/2+O(\sqrt p)$. If $q=1$, then $C_R=\bigcup_a B_a$, with count $(1-2^{-d})\ell+O_d(\sqrt p)$. For $q\ge2$, any $q$ consecutive $a$-rows have full rank on $R$ by Vandermonde, so $|C_R|\ge 2^{-q}\ell-O_d(\sqrt p)$ by (2). If the residue pattern $R$ is known, its exact asymptotic coefficient for $|C_R|$ is the fraction of subsets of the $d$ Fourier rows with full rank on $R$, again by (2).

For $d\ge2$ fixed, (1) gives the uniform estimate
$$
 m+1\ \ge\ \left(\frac12+2^{-d}\right)\ell-O_d(\sqrt p).
                                                                    \tag{3}
$$
For $q\ge2$ one can use $1/2+(q-1)2^{-q}$ in place of $1/2+2^{-d}$. For $d=2$, write $C=|B_0\cap B_1|$ and $U=|B_0\cup B_1|$. A support in one parity class has size at least $U+1$. A support in both has each parity size at least $C+1$, and at least one parity size at least $K+1$. Since $C=\ell/4+O(\sqrt p)$ and $U=3\ell/4+O(\sqrt p)$, the actual density is at least $3/8-O(p^{-1/2})$. For the plus sector in this case both parity classes must be active. Indeed $p=4\ell+1\equiv5\pmod8$ for odd $\ell$, so $s(-1)=\chi(2)=-1$. The zero equation at $-1$ makes the two parity masses equal for a nonnegative feasible spectrum. The improved density controls $L^2/m$ uniformly at fixed $d$.

There can be a genuine single-parity endpoint on the larger side at a small prime. At $p=29$ with $\beta$ the square of the least primitive root, the even bulk representatives of the minus endpoint are $2,6$, and a complementary plus optimizer uses $1,4,5,7$. Solve the anchored zero equations over $\mathbb Q[Z]/(\Phi_{14})$. The bulk values are strictly positive on these supports, their off-mark supports are disjoint and their anchored masses multiply to 14. The minus mark in sum-$\sqrt n$ normalization is about $1.12779768218912907833$, with a ball enclosure from the replay. The forbidden equations on the even allowed minus bulk $\{2,3,6\}$ have full column rank, so the displayed minus vector is the even minimum-norm endpoint. In fact any nonnegative optimizer can use only its support since its even symmetrization has that support. The four distinct folded forbidden positions then give rank four on the five support columns by prime cyclic uncertainty. This also proves uniqueness without imposing evenness. [Exact certificate replay](../parallel_sampling_12.py)

## Injective sampling with vanishing centered and one-sided leakage

The following construction applies to $A=Q$, and also to the subgroup $A\le Q$ of index $d$ with $d$ fixed and $\gcd(d,|A|)=1$. In the latter case take $N=|A|=\ell$ for the bounded-cofactor setting, though primality of $N$ is unnecessary here. Let $\tau=-\sigma$. We can take a generator $\gamma$ of $A$ with $s(\gamma)=\tau$ for all sufficiently large $p$. In fact, on each subgroup $A'\le A$, the sum of $s$ is $O(\sqrt p)$ by the character expansion for (2) with one factor. Inclusion-exclusion over the prime divisors of $N$ bounds the generator sum by $O(2^{\omega(N)}\sqrt p)$, while $\varphi(N)\ge N/2^{\omega(N)}$ and $4^{\omega(N)}=N^{o(1)}$. The last estimate follows by absorbing the factor four into $q^\epsilon$ at each sufficiently large prime $q$. Since $N\asymp p$ with $d$ fixed, both signs occur.

Take $2r+1$ to be the largest odd integer at most $(9/20)\log_2 p$. By (2) with $c_j=\gamma^j$ for $0\le j\le 2r$, there is a block $\gamma^{a-r},\ldots,\gamma^{a+r}$ of this length in $D_\tau\cap A$. The main term is $\gg_d p^{11/20}$, which dominates $O(\sqrt p\log p)$. Its reflected block is also in $D_\tau$ because $s(x^{-1})=s(x)$.

Set $\delta=7/30$, $M=\{h\in\mathbb Z/N:\delta N\le h\le(1-\delta)N\}$ in the natural representatives, and $\theta_h=2\pi h/N$. With $T_{2r}$ the Chebyshev polynomial of degree $2r$, define
$$
 E(\theta)=\frac{T_{2r}(\cos(\theta/2)/\cos(\pi\delta))}
                   {T_{2r}(\sec(\pi\delta))},\qquad
 w_h=E(\theta_h)\cos(a\theta_h).
$$
The even polynomial in $\cos(\theta/2)$ makes $E$ a trigonometric polynomial of degree $r$. Multiplying by the carrier confines the positional support to the two blocks, and $w_0=1$. For $h\in M$, $|E(\theta_h)|\le 1/T_{2r}(\sec(\pi\delta))$. Using $T_{2r}(\sec(\pi\delta))=\cosh(2r\operatorname{arcosh}(\sec(\pi\delta)))$, this bound is $O(p^{-\kappa})$ where
$$
 \kappa=\frac{9}{20}\frac{\operatorname{arcosh}(\sec(7\pi/30))}{\log 2}
       =0.52532\ldots>\frac12 .
$$
For the strict inequality, $\cos(7\pi/30)<3/4$, so the argument of the logarithm in $\operatorname{arcosh}$ is larger than $(4+\sqrt7)/3>11/5$, and $(11/5)^9>2^{10}$.

To center exactly on the sample, use $c_h=\cos(\theta_h)$ from the positional points $\gamma,\gamma^{-1}$ of the same sign. Its mean over $M$ tends to $-\sin(2\pi\delta)/(\pi(1-2\delta))\ne0$. Then
$$
 \lambda=\frac{\sum_{h\in M}w_h}{\sum_{h\in M}c_h}=O(p^{-\kappa}),
 \qquad
 v_h=-\frac{w_h-\lambda c_h}{1-\lambda}.
$$
This real even direction has $v_0=-1$, has sample sum zero, and has positional support in $D_\tau\cap A$. Lift it to the spectrum on $Q$ by restriction of characters to $A$, so that each sample is repeated $d$ times. Use $J$ for the full preimage of $M$. The lifted direction belongs to $V_\tau$. It obeys
$$
 \frac{|J|}{n}=\frac{8}{15}+o(1),\qquad
 \|v_J\|_\infty=O(p^{-\kappa}),\qquad
 \|(v_J)_+\|_2\le \|v_J\|_2=O(p^{1/2-\kappa}).
                                                                    \tag{4}
$$
The constants can depend on the fixed index. The construction and estimates hold along any sequence with the stated index and coprimality conditions.

Restriction to $J$ is injective on the **full** space $V_\tau$. Indeed, decompose the positional transform in the $d$ cosets of $A$. Since $J$ includes every $d$-residue in each sampled column, Fourier inversion in that residue separates the positional cosets. Each coset contributes a sum of $N/2+O(\sqrt p)$ exponentials in the folded frequency variable, by (2) with one sign factor. Its samples are consecutive in that variable. At least as many consecutive samples as distinct exponentials give a square Vandermonde matrix with nonzero determinant. For $d=1$ this is just the single Vandermonde argument. For $N=\ell$ prime, Chebotarev also proves injectivity in each coset whenever the sample cardinality is large enough, without consecutivity. Neither rank proof supplies a uniform marked leakage bound, by (4).

There is a marked feasibility obstruction for these same masks. If $b$ is nonnegative of sign $\sigma$, $b_0=1$, and its bulk support is contained in $J$, then orthogonality to $v$ gives
$$
 1=\sum_{j\in J} b_j v_j\ \le\ \|v_J\|_\infty\sum_{j\in J}b_j.
$$
Hence such a mask would require anchored bulk mass $\gg p^\kappa$, whereas the actual endpoint has $L=O(\sqrt p)$. More generally the endpoint must carry at least $1-o(1)$ anchored bulk mass off $J$, since $\|v\|_\infty\le(1+|\lambda|)/(1-|\lambda|)=1+o(1)$. This only forces mass on the omitted part of the mask. It does not bound the endpoint's centered energy.

## Keeping the paired constant direction alone is insufficient

There is also an exact failure of the sampling inequality on dense **subsets** of the actual $I$, even if the sample mask is required to admit the true paired constant direction $u=\sqrt n(j-Y)$. Let $W$ be the even part of $V_{-\sigma}$. The restriction to $I$ of $W$ has rank $r_I\ge (1/4-O(p^{-1/2}))m$. Indeed the compression of the orthogonal projector to $I$ has eigenvalues in $[0,1]$, so its rank is at least its trace. For the even projector its diagonal is
$$
 \tfrac12\bigl(P_{-\sigma}(i,i)+P_{-\sigma}(i,-i)\bigr).
$$
The first entry is $1/2+O(1/n)$. For $i\ne-i$ the second is $O(p^{-1/2})$ by the [Jacobi Fourier entry bound](fourier.md#joint-distribution-on-the-even-modes). The self-inverse indices have the full first entry as their diagonal.

The mark functional on $W$ is nonzero and lies in the span of the sample rows on $I$, since $-v_0=b_I^Tv_I$. Start a basis of that span with the mark and extend it using $r_I-1$ actual sample rows. Let $J'$ contain their full inversion orbits. These rows are independent of the mark, so there is $v\in W$ with $v_0=-1$ and $v_{J'}=0$. Thus $J'\subseteq I$ has size at least $2r_I-3$, positive density at bounded cofactor by (3). It belongs to the zero set of a true opposite optimum and satisfies $u_{J'}=\mathbf1$, $u_0=-L$. It still has zero centered and one-sided leakage at unit mark loss. The map is tested only on $J'$; the unsampled active coordinates of $I$ certify the mark for the full support. Together with (4) this shows why both injectivity on an arbitrary dense mask and the paired constant direction on a dense subset leave the marked question unsettled.

## Finite replay

The [replay script](../parallel_sampling_12.py) computes subgroup sign counts from integer Legendre data. It evaluates the exact arc formula in floating point and checks the mark, centering, and the FFT away from the prescribed sector. The rank column of the script uses the exact coset size criterion for the Vandermonde proof. It uses a longest available odd run for the first selected generator of the required sign. The runs in the table illustrate the construction.

| $p$ | $d$ | $\tau$ | Run length | Full sample size | $\|v_J\|_2$ | $\|v_J\|_\infty$ |
|---|---:|---:|---:|---:|---:|---:|
| 1997 | 1 | $+$ | 15 | 533 | $2.78\cdot10^{-4}$ | $2.41\cdot10^{-5}$ |
| 151337 | 1 | $-$ | 13 | 40357 | $1.22\cdot10^{-2}$ | $1.21\cdot10^{-4}$ |
| 1000033 | 1 | $-$ | 19 | 266675 | $2.44\cdot10^{-4}$ | $9.45\cdot10^{-7}$ |
| 20717 | 2 | $+$ | 11 | 5524 | $2.27\cdot10^{-2}$ | $6.11\cdot10^{-4}$ |
| 1000589 | 2 | $+$ | 15 | 266824 | $6.21\cdot10^{-3}$ | $2.41\cdot10^{-5}$ |
| 1000589 | 2 | $-$ | 13 | 266824 | $3.13\cdot10^{-2}$ | $1.21\cdot10^{-4}$ |

The endpoint replay compares the exact cardinality bounds with the numerical minimum-norm endpoints at 16 primes $p=4\ell+1$ through 4517, on both signs. Support detection uses a tolerance of $10^{-8}$. At $p=1997$, the exact support bounds including the mark are 372 and 371 on plus and minus, and the numerical sizes are 500 and 499. The numerical even/odd counts are $241,259$ and $259,240$. Both supports fold to 387 occupied residues of $\mathbb Z/499$. The numerical centered terms are $0.71839$ and $0.85013$. The largest observed centered term in these rows is $1.07794$ at $p=173,+$. The $p=29,-$ support and mark have the separate exact certificate above.

~~~sh
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python parallel_sampling_12.py \
  97 173 1997 9413 151337 1000033
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python parallel_sampling_12.py --cofactor 2 \
  173 1997 4517 20717 200909 1000589
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python parallel_sampling_12.py --endpoint-folds \
  13 29 53 149 173 269 317 389 509 1109 1229 1949 1997 4253 4493 4517
.venv/bin/python parallel_sampling_12.py --certify-p29
~~~
