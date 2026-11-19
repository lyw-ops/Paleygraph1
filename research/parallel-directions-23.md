# Diagonal pencils and the affine vacancy test

For [ETH Randomstrasse101 Problem 26](https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/), this continues [Round 22](parallel-crossratio-22.md). The inverse projective map gives an exact decomposition of the restricted direction count and a power saving for its one parallel pencil. The order-two twist yields a separate necessary condition: affine ratios must give an almost perfect cover on the three character sectors outside the all-square sector. A fixed positive density of nonsquare vacancies would rule out twisted saturation. I do not prove that lower bound or the finite-index Lorentz estimate for the original averaged ratio. The norm-one group over a square field satisfies the affine condition exactly and fails the original Lorentz bound.

## 1. Exact count through the diagonal

Let the field have odd order \(P\equiv1\pmod 4\), let \(B\) be an even-order subgroup of the nonzero squares, and write \(b=|B|\), \(D=\{(x-1)^{-1}:x\in B\setminus\{1\}\}\), and \(n_D=|D|=b-1\). Inversion on \(B\) induces \(z\mapsto-1-z\) on \(D\). After reflecting the second coordinate, the map to the projected grid of Round 22 is
\[
[Z:W:H]\longmapsto[-Z-H:W:Z-W].
\]
The domain is \(D^2\) off the diagonal. The direction at infinity with slope \(m=-t/(t+1)\) has preimage \((t,t)\). Setting \(t=(a-1)^{-1}\) gives \(m=-1/a\), so \(B\setminus\{-1\}\) corresponds bijectively to the \(n_D\) finite diagonal centers. The slope \(-1\) corresponds to \([1:1:0]\), the infinite point of the diagonal.

For \(u\ne0,1\) let \(r_t(u)\) count distinct \(z,w,t\in D\) with \(z-t=u(w-t)\), the overlap of [Round 21](parallel-crossratio-21.md) at \(t=(a-1)^{-1}\). Put \(A_D(\delta)=\#\{(z,w)\in D^2:z-w=\delta\}\). Counting ordered distinct pairs in the inverse pencils gives
\[
\boxed{J_B(\mathcal P)=2n_D(n_D-1)(n_D-2)
+\sum_{\delta\ne0}A_D(\delta)(A_D(\delta)-1)
+\sum_{t\in D}\sum_{u\ne0,1}r_t(u)(r_t(u)-1).} \tag{1}
\]
For a finite center the horizontal and vertical lines each have \(n_D-1\) off-diagonal points; the diagonal has none. The infinite center supplies the parallel lines \(z-w=\delta\ne0\). Every counted chord selects just one pencil since it is not the diagonal.

For primes with \(b\asymp\sqrt p\), the middle term is \(O(b^{8/3})\), improving the trivial \(O(b^3)\) for that direction. For \(\delta\ne0\), write \(w=(x-1)^{-1}\) and \(z=w+\delta\). This requires \(x\) and \(h(x)=((1+\delta)x-\delta)/(\delta x+1-\delta)\) in \(B\). The off-diagonal entries of \(h\) are nonzero and its diagonal entries cannot both vanish. Thus it is neither a dilation nor a scaled inversion. Apply [Corvaja–Zannier, Theorem 2](https://ems.press/content/serial-article-files/31918) to \(x^b,h(x)^b\): each has degree \(b\) and nonzero differential, and their zeros and poles occupy at most four places. They are multiplicatively independent since their zero-pole sets differ. This gives \(A_D(\delta)\ll b^{2/3}+b^2/p\); sum using \(\sum_{\delta\ne0}A_D(\delta)=n_D(n_D-1)\).

Also \(\sum_{t,u}r_t(u)=n_D(n_D-1)(n_D-2)\). Thus \(J_B=O(b^3)\) would bound the normalized **second** moment of the joint overlaps and, by Jensen, of their anchor average, directly from (1). The bound for the infinite pencil leaves the finite-pencil sum open.

## 2. The twist thins rich affine cells at nonsquare slopes

Put \(Y=(1-B)\setminus\{0\}\) and use the **affine** histogram \(R(u)=|Y\cap uY|\), distinct from the original average \(\bar r\). Throughout take \(u\ne0,1\). Suppose \(\chi(1-x)=\sigma d(x)\) on \(B\setminus E\), where \(\sigma=\pm1\), \(1\in E\), \(e=|E|\), and \(d\) is the nontrivial quadratic character on \(B\).

For each \(u\) set \(\alpha=(1-u)^{-1}\), \(\beta=-u/(1-u)\). This is a solution of \(\alpha+\beta=1\) in the cell \((\alpha B,\beta B)\). If a cell has \(N\) solutions \((\alpha_i,\beta_i)\), each determines a distinct \(u_i\) with \(R(u_i)=N-1\). The other solutions correspond to the pairs \(x=\alpha_j/\alpha_i,y=\beta_j/\beta_i\) with \(u_i=(1-x)/(1-y)\). In a cell with \(\chi(\alpha)\chi(\beta)=-1\), label solution \(i\) by \(c_i=d(\alpha_i/\alpha_0)d(\beta_i/\beta_0)\). For \(i\ne j\), if both relative ratios avoid \(E\), the equality \(\alpha_i-\alpha_j=-(\beta_i-\beta_j)\) shows that \(1-\alpha_j/\alpha_i\) and \(1-\beta_j/\beta_i\) have opposite quadratic characters. Hence \(c_i c_j=-1\). For \(N\ge3\) there are at least \(N(N-2)/2\ge N(N-1)/4\) same-label ordered distinct pairs, all of which have an exception. Across all cells each exceptional pair is specified by its \((x,y)\), since those determine \(u_i\) and hence the base solution. There are at most \(2eb\) such pairs. Therefore
\[
\boxed{\sum_{\chi(u)=-1,\ R(u)\ge2}R(u)\le 8eb.} \tag{2}
\]
On the original grid \(B^2\), the ordered pairs on lines of nonsquare slope with at least three points number at most \(8eb^3\): each cell gives \(b^2\) lines \(\alpha x+\beta y=1\), and a line of nonsquare slope through the origin has no points of \(B^2\). This is an affine-grid bound, not a count of the projected chords in (1).

The total nonsquare ratio mass is \(2|Y\cap Q||Y\setminus Q|=b^2/2+O(b+e^2)\) by balance of \(d\). The number of nonsquare ratios is \((P-1)/2\), so (2) gives
\[
\sum_{\chi(u)=-1}|R(u)-1|\ll eb+b+|b^2-P|. \tag{3}
\]
Also \(R(u)=R(1-u)=R(u^{-1})\): on pairs \((x,y)\) for the ratio \((1-x)/(1-y)\), use \((x/y,1/y)\) or swap \(x,y\). Thus (3) bounds the error over all \(U=\{u\ne0,1:(\chi(u),\chi(1-u))\ne(+1,+1)\}\) up to a factor two. If \(b\sim\sqrt P\) and \(e=o(b)\) the error is \(o(P)\). In prime fields the [Mit'kin tail from Round 20](parallel-rectangle-20.md#2-shifted-subgroup-correlations-and-an-additive-gap), \(\#\{u\ne0,1:R(u)\ge t\}\ll p/t^2\), further gives \(\|(R-1)\mathbf1_U\|_{L^{s,q}}\to0\) for \(1<s<2,\ 1\le q<\infty\) under measure \(1/p\). For each fixed positive threshold the tail measure tends to zero by (3); the Lorentz distribution integral is dominated at high thresholds by the uniform \(t^{-2}\) tail.

A uniform positive lower bound on \(p^{-1}\#\{u:\chi(u)=-1,\ R(u)=0\}\), along critical prime families \(b/\sqrt p\to1\), would exclude twisted saturation by (3). A uniform positive lower bound for the normalized left side of (2) would likewise suffice. Either would force a fixed fraction of exceptions in a sufficiently small fixed neighborhood of the critical size. The affine rich-cell tail is an upper bound and proves neither lower bound.

## 3. Partition and orientation

The original two-anchor fibers satisfy
\[
R(u)=\sum_{a\in B\setminus\{1\}}\mathbf1_{X_a}(u),\qquad
X_a=\{(x-a)/(x-1):x\in B\setminus\{1,a\}\}.
\]
Indeed \((x-a)/(x-1)=(1-a/x)/(1-1/x)\), and the affine pair determines \(a,x\). For an affine pair \((x,y)\) with \(x,y,x/y\notin E\) its ratio has
\(\chi(u)=d(x)d(y)\) and \(\chi(1-u)=d(x)\), using \(1-u=(x-y)/(1-y)\). There are \(O(eb)\) other pairs. As the fiber of an affine pair is indexed by \(a=x/y\), the fibers with \(d(a)=-1\) can be made into a disjoint partition of all but \(O(eb+b+|b^2-P|)\) nonsquares by deleting at most that many incidences. This approximation controls overlaps between distinct fibers at the same point; it does not bound intermediate overlaps within a fiber under multiplication.

For the directed histogram \(\rho(u)=\#\{(v,w)\in(Y\setminus Q)\times(Y\cap Q):v/w=u\}\) this also gives
\[
\sum_{\chi(u)=-1}|\rho(u)-\mathbf1_{\{\chi(1-u)=-\sigma\}}|
\ll eb+b+|b^2-P|. \tag{4}
\]
For a good pair the numerator \(v=1-x\) lies in the nonsquares precisely when \(d(x)=-\sigma\). At every nonsquare \(u\), \(R(u)\) is the sum of the two directed counts, so (4) follows from (3) and the total orientation errors.

## 4. A spectral consequence of the orientation constraint

There is also a necessary law for the two shifted indicators along twisted saturation. For primes with \(b\sim\sqrt p\), \(e=o(b)\), fix \(\sigma\) along a subsequence. Choose a nonsquare \(\xi\). Use counting unitary Fourier transforms \(V_j,W_j\) of the indicators of \(Y\cap Q\) and \(\xi^{-1}(Y\setminus Q)\) on \(Q\), respectively, with \(n=|Q|\). In this basis the additive Paley convolution compressed to the nonzero elements has blocks
\[
K_j=\begin{pmatrix}k_j&c_j\\ \overline{c_j}&-k_j\end{pmatrix},
\quad
k_j=\frac1{\sqrt p}\sum_{x\in Q}\chi(1-x)j(x),\quad
c_j=\frac1{\sqrt p}\sum_{x\in Q}\chi(1-\xi x)j(x).
\]
For \(j\ne0\) the additive mean is zero, and the omitted zero coordinate is identically zero on the corresponding invariant subspace. Thus \(K_j^2=I\) and \(|c_j|^2=1-k_j^2\). Also \(c_0=0\) since \(\sum_{u\notin Q,\,u\ne0}\chi(1-u)=0\). For all but \(O(eb+b)\) ordered pairs in \(Y^2\),
\(\chi(v-w)=\sigma\chi(v)\chi(w)\), by applying the twist to the two preimages and their relative ratio. So the signed indicator of \(Y\) has Rayleigh quotient \(\sigma+o(1)\). By the unit norm of the full Paley convolution and contraction under restriction, \(\sum_j\|(K_j-\sigma I)(V_j,-W_j)\|^2=o(b)\).

For a fixed real polynomial \(\varphi\) let \(b_\varphi\) denote the kernel with multiplier \(\varphi(k_j)c_j\) under the convention \(h(x)\mapsto\sum_{u\in Q}b_\varphi(u)h(xu)\). Uniformly in \(u\), \(b_\varphi(u)=O_\varphi(p^{-1/2})\). Indeed for a lift \(\eta\) of \(j\), put \(z_\eta=J(\eta,\chi)/\sqrt p=k_j+\eta(\xi)c_j\). Fourier inversion over both lifts writes \(b_\varphi(u)\) as the average of \(\varphi(k_j)(z_\eta-k_j)\overline{\eta(\xi u)}\) over full characters. The two nonexceptional lifts give conjugate unit values, so the factor before the character is a fixed Laurent polynomial in \(z_\eta\). Apply the twisted moment bound (2) of [Round 20](parallel-rectangle-20.md#1-a-smooth-jacobi-cap), from [Xi, Lemma 2.2](https://arxiv.org/pdf/1809.04286); the twist parameter \(\xi u\) is never 1. The two exceptional characters cost \(O_\varphi(p^{-1})\).

Pair this kernel with the directed histogram in (4). Its error is \(o(p)\) in counting \(\ell^1\); the kernel bound makes the error in the pairing \(o(b)\). As \(\sum b_\varphi=0\) and the kernel for the constant test \(1\) is \(\chi(1-\xi u)/\sqrt p\), Parseval gives
\[
\sum_j\varphi(k_j)\Re(c_j W_j\overline{V_j})
=-\frac{\sigma\sqrt p}{2n}\sum_j\varphi(k_j)|c_j|^2+o(b).
\]
In bounded weighted sums, the near eigenvector equations replace \(2\sigma\Re(c_jW_j\overline{V_j})\) by \(-(1-k_j^2)(|V_j|^2+|W_j|^2)\) with error \(o(b)\). To see this, multiply the two scalar residual equations by \((k_j+\sigma)\overline{V_j}\) and \((k_j-\sigma)\overline{W_j}\), respectively, take real parts and add. The errors are bounded by Cauchy–Schwarz. Consequently for \(\mu_p=b^{-1}\sum_j (|V_j|^2+|W_j|^2)\delta_{k_j}\),
\[
\int \varphi(t)(1-t^2)\,d\mu_p(t)
=\frac{\sqrt p}{bn}\sum_j\varphi(k_j)|c_j|^2+o(1).
\]
By [Xi, Theorem 1.1](https://arxiv.org/pdf/1809.04286) the empirical law of \(k_j=\Re z_\eta\) tends to the arcsine law \(\omega\). By polynomial approximation every weak limit of \(\mu_p\) agrees with \(\omega\) in \((-1,1)\); its total mass is one, hence there is no additional endpoint mass. The scalar residual equations also give \(|V_j|^2-|W_j|^2=\sigma k_j(|V_j|^2+|W_j|^2)\) up to \(o(b)\) in counting \(\ell^1\), by multiplying by \(\overline V_j,\overline W_j\), taking real parts and adding. Thus the individual measures \(b^{-1}\sum_j |V_j|^2\delta_{k_j}\) and \(b^{-1}\sum_j |W_j|^2\delta_{k_j}\) converge to \((1+\sigma t)\omega/2\) and \((1-\sigma t)\omega/2\). This is a restriction on the affine shift across the Jacobi symbol, not an estimate of the original pinned ratios. The argument uses the field order in the character-sum estimates and does not distinguish primes from squares.

## 5. Exact square comparison

Take \(P=\ell^2\) and \(B=\{x:x^{\ell+1}=1\}\), where \(\ell\) is an odd prime power. The twist is exact away from 1 with \(\sigma=(-1)^{(\ell+1)/2}\) by [Round 21](parallel-crossratio-21.md#4-uniform-individual-saving-and-the-square-order-check). Here \(D=\{z:z^\ell+z=-1\}\), an affine \(\mathbb F_\ell\)-line missing zero. Inversion and scaling identify the multiplicative overlap sizes of \(D\) and \(Y\). Thus for \(u\ne0,1\) we have \(R(u)=1\) if \(u\notin\mathbb F_\ell^\times\) (distinct directions) and \(R(u)=0\) otherwise (parallel distinct lines). The missing ratios all belong to the all-square sector. Consequently the nonsquare vacancies, the error over \(U\) in (3) and the error in (4) are identically zero.

For each finite center \(t\), \(r_t(u)=\ell-1\) for \(u\in\mathbb F_\ell^\times\setminus\{1\}\), and zero for all other \(u\ne0,1\). Counting the horizontal and vertical lines, each finite pencil contributes \(\ell(\ell-1)(\ell-2)\) to \(J_B\). The parallel pencil contributes \(\ell(\ell-1)^2\), since each of the \(\ell-1\) nonzero differences in the direction space of \(D\) has \(\ell\) representations. Thus
\[
J_B(\mathcal P)=\ell^2(\ell-1)(\ell-2)+\ell(\ell-1)^2.
\]
The support of \(\bar r\) has measure \((\ell-2)/\ell^2\), and its \(L^{3/2,q}\) norm grows as \(\ell^{1/3}\) for every fixed finite \(q\) and for \(q=\infty\). Dropping the two zero-entry ratios at each anchor only affects the ratio \(-1\), since \(B\cap\mathbb F_\ell^\times=\{1,-1\}\). The affine tests therefore do not on their own imply any bound at the pinned endpoint.

## 6. Reproducible checks

[The standard-library script](parallel-directions-23-check.py) checks (1) by independently constructing the projected grid and counting in the chosen directions. It checks (2), the affine symmetries, the fiber identity, and the orientation estimate, and compares the square formulas to exact finite counts. The prime vacancy fractions are finite diagnostics only.


| Prime \(p\) | \(b\) | Nonsquare vacancies | Parallel-pencil contribution to \(J_B\) |
|---:|---:|---:|---:|
| 97 | 12 | 12 / 48 | 180 |
| 1,153 | 32 | 244 / 576 | 1,596 |
| 4,177 | 72 | 544 / 2,088 | 10,332 |
| 10,193 | 98 | 2,196 / 5,096 | — |
| 40,801 | 200 | 7,664 / 20,400 | — |
| 252,001 | 500 | 46,512 / 126,000 | — |

At \(\ell=7,11,13,31\) the square checks found zero nonsquare vacancies and matched both terms in the stated square formula for \(J_B\).
