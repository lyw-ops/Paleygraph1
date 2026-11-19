# A prime gap for nonalternating coset rectangles

For [ETH Problem 26](https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/), the nonalternating part of the bounded-coset branch of [Round 19](parallel-cap-19.md) has a fixed prime-field gap. This includes the unshifted single-coset branch, with qualitative slack rather than the earlier inverse-logarithmic size window. The new input is a bound for a smooth Jacobi cap on a shifted multiplicative subgroup. A rich-intersection estimate controls the large correlations in ℓ¹, while a pointwise bound for the cap's Fourier coefficients makes those large correlations inexpensive. The total multiplicative energy, which costs a logarithm, is not needed.

## 1. A smooth Jacobi cap

Let $p\equiv1\pmod4$ be prime, $Q=(\mathbb F_p^\times)^2$, $G=\widehat Q$, $n=(p-1)/2$, $m_0=n/\sqrt p$, and $s(x)=\chi(1-x)$ on $Q$. Write $k(j)=p^{-1/2}\sum_{x\in Q}s(x)j(x)$. The Jacobi bound gives $|k|\le1$. Define $P_{M,\rho}(u)=((1+\rho u)/2)^M$ for integer $M\ge1$ and sign $\rho=\pm1$, and its inverse Fourier coefficients

$$a_M(x)=\frac1n\sum_{j\in G}P_{M,\rho}(k(j))\overline{j(x)},\qquad x\in Q.$$

Uniformly in $p,M,\rho$,

$$|a_M(1)|\ll M^{-1/2}+p^{-1/4},\qquad
  \|a_M\|_2\ll M^{-1/4}+p^{-1/8},\qquad
  |a_M(x)|\le \sqrt{M/(2p)}+4/(p-1)\quad(x\ne1).\tag{1}$$

Here and below norms over finite sets use counting measure. To prove (1), lift each $j$ to its two full characters $\eta,\eta\chi$. Except for $\eta=1,\chi$, put $z_\eta=J(\eta,\chi)/\sqrt p$. The two lifts give conjugate unit numbers and $k(j)=\Re z_\eta$, by the [Jacobi lift identity](critical-sets.md#repeated-differences-are-necessary). For $|z|=1$,

$$P_{M,\rho}(\Re z)=4^{-M}\sum_{\ell=-M}^M \binom{2M}{M+\ell}\rho^\ell z^\ell.$$

The absolute coefficients sum to one. For $\ell>0$ the normalized moment with a factor $\overline{\eta(x)}$ satisfies

$$\left|\frac{1}{p-1}\sum_{\eta\ne1,\chi}z_\eta^\ell\overline{\eta(x)}\right|\le \ell p^{-1/2}+\frac{2}{p-1}\qquad (x\ne1).\tag{2}$$

Indeed extend $z_\eta$ to the two omitted characters by the Gauss expression $\tau(\eta)\overline{\tau(\eta\chi)}/p$, of magnitude at most one. Open the $2\ell$ Gauss factors and sum over $\eta$. Orthogonality imposes $\prod u_i=x\prod v_i$ with multiplicative weight $\prod\chi(v_i)$ and additive phase $\psi(\sum u_i-\sum v_i)$. Its unnormalized hypergeometric sum has absolute value at most $\ell p^{(2\ell-1)/2}$: the two parameter lists are $\ell$ trivial and $\ell$ quadratic characters, disjoint. This is Katz's bound as stated in [Xi, Lemma 2.2](https://arxiv.org/pdf/1809.04286), with the extra $\overline{\eta(x)}$ changing the hypergeometric parameter from $1$ to $x$. Conjugation and inversion give the negative powers. The same error bound for $\ell=0$ follows from character orthogonality, and the missing trivial character of $Q$ costs at most $1/n$. The weighted sum of $|\ell|$ is at most $\sqrt{M/2}$ by the binomial variance, giving the off-identity bound in (1).

At $x=1$, Xi's interval discrepancy (Theorem 1.1) gives the circle average up to $O(p^{-1/4})$: integrate the superlevel sets of $P_{M,\rho}(\cos\theta)$, which are arcs, in a range of levels of length one. The circle average is the constant term $4^{-M}\binom{2M}M\ll M^{-1/2}$. Parseval gives $\|a_M\|_2^2=n^{-1}\sum_j P_{2M,\rho}(k(j))$, yielding the second bound in (1).

## 2. Shifted-subgroup correlations and an additive gap

Fix comparison constants $0<c<C<\infty$. Suppose $B\le\mathbb F_p^\times$, $b=|B|\in[c\sqrt p,C\sqrt p]$, and let $Y=(1-B)\setminus\{0\}$. For $u\ne0$ write $r(u)=|Y\cap uY|$. There are constants depending only on $c,C$ such that

$$|\{u\ne1:r(u)\ge t\}|\ll_{c,C} p/t^2\qquad(t\ge1).\tag{3}$$

To see this, for $u\ne1$ write $\alpha=1/(1-u)$ and $\beta=-u/(1-u)$. The equation $1-x=u(1-y)$ for $x,y\in B$ is $\alpha x+\beta y=1$. It counts $r(u)+1$ solutions, the extra one being $(1,1)$. Group the pairs $(\alpha,\beta)$ by their two $B$-cosets and put $N(D,E)=|\{v\in D,w\in E:v+w=1\}|$. A cell with $N$ solutions contains exactly $N$ values of $u\in\mathbb F_p^\times\setminus\{1\}$, since $\alpha+\beta=1$ and the correspondence is bijective. The [Mit'kin bound as stated in Macourt–Shkredov–Shparlinski, Lemma 2.1](https://arxiv.org/pdf/1701.06192) gives $\sum_{(D,E)\in\Theta}N(D,E)\ll (b|\Theta|)^{2/3}$ for $|\Theta|\le\min(b^2,p^3/b^4)$. This cutoff is $\gg_{c,C}p$, whereas the number of cells with $N\ge t$ is at most $(p-2)/t$ by $\sum_{D,E}N(D,E)=p-2$ (and $p\asymp_{c,C}b^2$). Thus above a fixed $t_0(c,C)$ the bound applies to all rich cells and yields $|\Theta_t|\ll b^2/t^3$. Summing $N$ on those cells gives (3) for $t\ge t_0$; the range below $t_0$ is trivial. In particular,

$$\sum_{u\ne1:r(u)\le R}r(u)^2\ll_{c,C}p\log(2R),\qquad
\sum_{u\ne1:r(u)>R}r(u)\ll_{c,C}p/R\quad(R\ge1).\tag{4}$$

The same estimates hold for any nonzero scalar multiple of $Y$, since scaling does not change $r$.

Let $\mathcal T$ be additive Paley convolution on $\mathbb F_p$, with matrix $p^{-1/2}\chi(x-y)$. It has norm one and $\mathcal T^2=I-J_{\rm add}$ by the quadratic-character correlation identity. The compression to $Q$ is diagonal in multiplicative Fourier coordinates, with multiplier $k(j)$ (put $y=xv$ in the convolution). For any complex $g$ supported in $Q\cap vY$ with $v\ne0$, $|g|\le1$, we obtain

$$\begin{split}
\sum_{j\in G}P_{M,\rho}(k(j))|\widehat g(j)|^2
&\le |a_M(1)|\|g\|_2^2+O_{c,C}\!\left(\|a_M\|_2\sqrt{p\log(2R)}+\frac{\sqrt{Mp}}{R}\right),\tag{5}
\end{split}$$

where $\widehat g$ is the unitary transform on $Q$. Indeed the left side is the pairing of $a_M$ (up to inversion) with the correlations $\sum_xg(ux)\overline{g(x)}$, bounded by $r(u)$ in absolute value. Use Cauchy–Schwarz on $u\ne1$ with $r(u)\le R$ and the uniform bound in (1) on the rest. The $x=1$ term is separate; (3) would be false there at the stated scale.

If $\|g\|_2^2\ge c'\sqrt p$, set $R=M$ in (5). With $M$ fixed when taking $p\to\infty$, the limsup of the normalized left side is

$$O_{c,C,c'}\big(M^{-1/2}+M^{-1/4}\sqrt{\log(2M)}\big).\tag{6}$$

Choose a sufficiently large fixed $M$ so this is less than $1/4$. For large $p$, the left side of (5) is at most $\|g\|_2^2/2$. By $1-((1+\rho u)/2)^M\le M(1-\rho u)/2$ on $[-1,1]$, this proves

$$\boxed{\qquad \langle g,(I-\rho\mathcal T)g\rangle\ \ge\ M^{-1}\|g\|_2^2 .\qquad}\tag{7}$$

The same result holds for a shift of a multiplicative coset in place of $Y$ if its shift is a member of that coset, by scaling. Both signs in (7) use the same constants. Only (3) needs the prime field. On squares, for example, $B=\mathbb F_{\sqrt q}^\times$ gives roughly $\sqrt q$ coefficients $r(u)\asymp\sqrt q$ and violates (3).

## 3. Consequence for within-set rectangles

Suppose $U\subset G$ is a union of at most $r_0$ cosets of a common subgroup $H$, for fixed $r_0$, and $m=|U|\sim m_0$. A within-set signed rectangle cannot have

$$ d_\sigma(U)=m^{-2}\sum_{i,j\in U}(1-\sigma k(i-j))\longrightarrow0.\tag{8}$$

Choose an anchor $i_0\in U$ whose row deficit is at most (8), and set $f(x)=m^{-1}\sum_{j\in U}(j-i_0)(x)$ on $Q$, zero off $Q$. It satisfies $|f|\le1$, $\|f\|_2^2=n/m\sim\sqrt p$, and is supported on $B=H^\perp$ with $|B|\asymp_{r_0}\sqrt p$. The compression formula bounds $\langle f,(I-\sigma\mathcal T)f\rangle/\|f\|_2^2$ by the anchor deficit, hence by $o(1)$. The other defect uses the *same* within-set average:

$$\frac{\sum_{x\in Q}(1-\sigma s(x))|f(x)|^2}{\|f\|_2^2}=1-\frac m{m_0}(1-d_\sigma(U))=o(1).\tag{9}$$

Indeed expand $|f|^2$ and use the definition of $k$. Choose $a\ne0$ with $\chi(a)=\sigma$. The affine reflection $Rf(x)=f(1-ax)$ obeys $\mathcal T R=\sigma R\mathcal T$. Put $g=\mathbf1_Q Rf$. The discarded squared mass is at most $1+\tfrac12 o(\|f\|_2^2)$ by (9): the term $1$ is at the image of the identity, and all other discarded points have the wrong sign. Thus $\|g\|_2^2\sim\sqrt p$, $|g|\le1$, and $g$ is supported on $Q\cap a^{-1}Y$. The seminorm from $I-\mathcal T$ satisfies the triangle inequality and its operator norm is at most two. Therefore $\langle g,(I-\mathcal T)g\rangle=o(\|g\|_2^2)$, contrary to (7).

In particular there exist $\epsilon(r_0),\eta(r_0)>0$ such that for large enough primes, $|m/m_0-1|<\eta(r_0)$ forces $d_\sigma(U)\ge\epsilon(r_0)$ on such unions. Otherwise take a sequence with both errors tending to zero. The conclusion is stable under $o(m_0)$ perturbations of either set, by $|k|\le1$. Thus Round 19's high-energy branch is excluded when $A,T$ themselves overlap in $(1-o(1))m_0$ points, or when their displacement lies in the common stabilizer. The high-energy reduction alone does not require either. The result also gives a fixed gap in the single-coset formula for $d|_B=1$ of Round 19, independent of its additional parity restrictions.

## 4. The twisted coset becomes a pinned cross-ratio question

Let $A,T$ be distinct single frequency cosets of $H$ satisfying Round 19's flat near-unit hypotheses. Let $d$ be their displacement restricted to $B=H^\perp$. The remaining twist has $d^2=1$, $d\ne1$, $b\sim\sqrt p$, and $\chi(1-x)=\sigma d(x)$ off an exceptional $o(b)$ subset of $B$. Equivalently, the matrix $\chi(x-y)$ on $B^2$ agrees with $\sigma d(x)d(y)$ on all but $o(b^2)$ pairs, including the negligible diagonal in the exceptions. The affine reflection used in §3 sends approximately half the mass to each square class in this case, so restricting to $Q$ does not give a near-eigenfunction.

There is a way to place all but $o(b)$ points in one square class, using a fractional linear map with two anchors. Choose any $a\in\ker d\setminus\{1\}$ and write $\phi_a(x)=(x-a)/(x-1)$. For all but $o(b)$ points of $B$ other than $1,a$,

$$\chi(x-1)=\sigma d(x),\qquad \chi(x-a)=\sigma d(x),\qquad \chi(\phi_a(x))=1.$$

The exceptions for the second equality are the multiplicative translates by $a$ of the first ones, so the errors are uniform over $a$. Moreover for $x,y\ne1$,

$$\chi(\phi_a(x)-\phi_a(y))=\chi(a-1)\,\chi(x-y)\chi(x-1)\chi(y-1).$$

Thus $X_a=\phi_a(B\setminus\{1,a\})$ is almost all squares and almost all its differences have sign $\rho_a=\sigma\chi(a-1)$. The flat function $g_a=\mathbf1_{Q\cap X_a}$ has $\|g_a\|_2^2\sim\sqrt p$ and $\langle g_a,(I-\rho_a\mathcal T)g_a\rangle=o(\|g_a\|_2^2)$, just by the pair count. This avoided needing covariance at the pole of the map.

Any uniform bound $|\{u\ne1:|X_a\cap uX_a|\ge t\}|\ll p/t^{1+\delta}$ for some fixed $1/2<\delta\le1$ and a choice of $a\in\ker d\setminus\{1\}$ would likewise close the twisted branch. When $\delta<1$, the normalized low-correlation term in (6) would instead be $O(M^{-1/4}R^{(1-\delta)/2})$, and the high term $O(\sqrt M R^{-\delta})$. Both tend to zero for $R=M^\gamma$ with $1/(2\delta)<\gamma<1/(2(1-\delta))$; the $\delta=1$ bound is (6). This estimate alone does not cover smaller $\delta$. In the needed range the arithmetic question is a bound on pinned cross ratios of $B$:

$$(x-a)(y-1)=u(x-1)(y-a),\qquad x,y\in B\setminus\{1,a\},\quad u\ne1.$$

Unlike the corresponding equation for $Y=1-B$, this has a genuine $xy$ term. The rich **line** estimate in §2 does not prove the required bound for this family. No twisted gap is claimed here.

## 5. A fixed number of returns alone permits alternation

The clipped recurrence itself cannot add an obstruction to a hypothetical flat pair at any fixed number of steps. This statement concerns the algebra of the recurrence; its initial residual below is not asserted to come from the canonical reciprocal pair of Round 17.

In the notation of [Round 18](parallel-tail-18.md#2-the-actual-excess-follows-a-scalar-recurrence), let $Z=I-\alpha P$, $h=h_*\sim m_0$, $X_{2j}=A$, $X_{2j+1}=T$. Suppose $|A|,|T|\sim m_0$ and the signed rectangle deficit tends to zero. Then, for every $j$,

$$\|Z\mathbf1_{X_j}-\mathbf1_{X_{j+1}}\|_2=o(\sqrt h).\tag{10}$$

Use Round 19's near transport in both directions, $\alpha\to2$, and $Z=(1-\alpha/2)I+(\alpha/2)(\sigma K+J)$, with $\|J\mathbf1_{X_j}\|_2=|X_j|/\sqrt n=O(1)$. Initialize from the nonnegative algebraic floor $D=b_0\mathbf1+\mathbf1_A$ off the mark, $D_0=0$, with shadow $A_0=b_0\mathbf1$ for bounded $b_0\ge0$. Then $r_0=\mathbf1_A+O_{\ell_2}(1)$. The map $F(r)=Zr_++\min(r,0)$ is $\sqrt2$-Lipschitz in $\ell_2$: $\|Z\|\le1$ and the sum of the two squared clipping differences is at most the original squared difference, coordinatewise. Since $F(\mathbf1_{X_j})=Z\mathbf1_{X_j}$, induction from (10) gives $\|r_j-\mathbf1_{X_j}\|_2=o(\sqrt h)$ uniformly over any fixed number of steps.

For a fixed prefix choose $t_p\downarrow0$ slowly enough that all those errors are $o(t_p\sqrt h)$. Take the mark as the only exception. The supports of $e_j=\mathbf1_{\{0\}^c}(r_j-t_p)_+$ differ from $X_j$ by $o(h)$ points, by counting coordinates with error at least $t_p$ (and taking $t_p<1/2$). Consequently $\|e_j-\mathbf1_{X_j}\|_1=o(h)$, by the support bound, the $\ell_2$ error, and the loss $t_p$ on $X_j$. The loads all tend to one. Off the mark $C_j=\min((r_j)_+,t_p)$ has norm $o(\sqrt h)$ by comparison with $t_p\mathbf1_{X_j}$; at the mark $(r_j)_0=O(1)+o(\sqrt h)$. The core injection obeys $I_j\le |\operatorname{supp}(e_{j+1})|^{1/2}\|Z C_j\|_2/h=o(1)$, since the other two terms of $f_j$ are nonpositive. So the hypothetical pair gives all of the near-tight inequalities of Round 19 on this prefix. A three- or four-step argument needs a property of the reciprocal floor or a new prime-field rectangle bound. This construction says nothing about whether the near-unit pairs exist on primes or arise from that floor.

As a normalization check, at $p=101,401,9413,1000033$ direct FFTs for $M=1,4,16,64$ and both signs met the off-identity bound in (1). Exact integer counts at the same orders verified $r(u)+1=N(D,E)$ for all $u\ne0,1$ at the first three orders and 4096 sample ratios at the largest. These checks concern the identities, not a numerical estimate of the asymptotic gap.
