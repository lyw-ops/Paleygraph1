# Additive Paley compression on two-vertex sign sets

Let $q\equiv1\pmod4$ be an odd prime power, $Q=(\mathbb F_q^\times)^2$, $n=|Q|$, and $m_0=n/\sqrt q$. Write $\chi$ for the quadratic character and $s(x)=\chi(1-x)$ on $Q$. For $\sigma=\pm1$ define

$$ C_\sigma=\{x\in Q:s(x)=\sigma\},\qquad
T_{xy}=\chi(x-y)/\sqrt q,\qquad
\beta_\sigma=\lambda_{\max}(\sigma T_{C_\sigma,C_\sigma}). $$

Assume the sign set is nonempty. The character correlation gives $T^2=I-q^{-1}\mathbf1\mathbf1^*$ and $T=T^*$. Thus $A_\sigma=I-\sigma T\succeq0$, $\|A_\sigma\|\le2$, and

$$ \|A_\sigma^{1/2}g\|_2^2\ge (1-\beta_\sigma)\|g\|_2^2
   \quad\text{for } \operatorname{supp}g\subseteq C_\sigma. \tag{1} $$

## Any feasible probability with a large squared norm

For a feasible sign-$\sigma$ Fourier probability $\mu$ on $\widehat Q$, let $f(x)=\sum_h \mu_h h(x)$ on $Q$ and extend it by zero. Feasibility gives $f(1)=1$ and $\operatorname{supp}f\subseteq C_\sigma\cup\{1\}$. Use the normalized Jacobi coefficients $k(h)$ and write

$$ d_0=\sum_h \mu_h(1-\sigma k(h))=1+q^{-1/2}-m_0\mu_0,
   \qquad 0\le\mu_h\le L=(1+\sqrt q)/n. $$

The rooted identity follows by evaluating the support condition in multiplicative Fourier, as in [the reflected endpoint note](parallel-extreme-6.md). The same note diagonalizes the compression of $T$ to $Q$. With $g=f-\mathbf1_{\{1\}}$, it gives

$$ \|A_\sigma^{1/2}f\|_2^2=n\sum_h\mu_h^2(1-\sigma k(h))\le nL d_0,
   \qquad \|g\|_2^2=n\|\mu\|_2^2-1. $$

Since the diagonal of $T$ is zero, $\|A_\sigma^{1/2}\mathbf1_{\{1\}}\|_2=1$. Apply (1) and the triangle inequality to obtain the explicit bound

$$ \boxed{\quad (1-\beta_\sigma)(n\|\mu\|_2^2-1)
       \le \big(\sqrt{(1+\sqrt q)d_0}+1\big)^2.\quad} \tag{2} $$

In particular, if $d_0=o(1)$ and a set of $O(m_0)$ frequencies carries mass bounded below, Cauchy–Schwarz gives $m_0\|\mu\|_2^2\gg1$, and (2) forces $\beta_\sigma\to1$. Conversely, a uniform gap $1-\beta_\sigma\ge c>0$ forces $m_0\|\mu\|_2^2=O_c(d_0+q^{-1/2})$ for all feasible probabilities. This bounds the mass of any set of size $O(m_0)$ by $O_c(\sqrt{d_0+q^{-1/2}})$, regardless of its additive energy. The estimate leaves open near-endpoint probabilities that are diffuse in this sense and gives no direct bound of the required sharp size on theta.

## Flat near-minimum sets, including low-energy sets

An exact support assumption is unnecessary for a flat trial on a frequency set. Let $U\subseteq\widehat Q$, $|U|=m$, and $d=m^{-2}\sum_{i,j\in U}(1-\sigma k(j-i))$. Choose an anchor whose average deficit is at most $d$ and take the anchored uniform Fourier profile $f$. Its squared norm is $n/m$, its root value is one, and $\|A_\sigma^{1/2}f\|_2^2\le d\|f\|_2^2$. The mean wrong-sign defect is, as in [the signed flatness computation](parallel-extreme-6.md#a-prime-gap-for-bounded-coset-covers),

$$ v=1-\frac{m}{m_0}(1-d)\ge0. $$

Now let $g=\mathbf1_{C_\sigma}f$. Since $s$ equals $0$ only at the root, $\|f-g\|_2^2=(v\|f\|_2^2+1)/2$. Apply (1) and $\|A_\sigma\|\le 2$ to get

$$ (1-\beta_\sigma)\bigl(1-(v+m/n)/2\bigr)
       \le \bigl(\sqrt d+\sqrt{v+m/n}\bigr)^2. \tag{3} $$

Thus a uniform positional gap would exclude *every* flat $U$ with $m/m_0\to1$ and $d\to0$. In particular it would exclude the [near-minimum stationary high sets with mass bounded below](parallel-half-arithmetic-5.md#which-jacobi-endpoint-information-survives-at-each-size), with no coset-cover, energy, or logarithmic-rate hypothesis. The earlier reflected-energy route establishes a prime-field bound for coset covers without assuming a spectral gap. Equations (2) and (3) reduce the complementary shape-free argument to an extreme eigenvalue problem in additive coordinates.

## What is known about the gap

For each prime $p$, $\beta_\sigma<1$. Indeed, equality in (1) gives a nonzero additive Paley eigenfunction of sign $\sigma$ supported on $C_\sigma$. The additive Fourier multiplier has $n$ entries of each sign and one zero, so the sum of the two support sizes would be at most $|C_\sigma|+n\le p-1$. This contradicts the prime cyclic [uncertainty principle of Tao, Theorem 1.1](https://arxiv.org/abs/math/0308286). The strict inequality at each order supplies no uniform constant. In projection language, with $P_\sigma$ the additive spectral projection onto the $\sigma$ eigenspace of $T$ and $E$ the coordinate projection onto $C_\sigma$, the operator satisfies

$$ E\sigma T E=2 E P_\sigma E-E+q^{-1}E\mathbf1\mathbf1^*E. $$

At $q=r^2$ the indicator of $\mathbb F_r^\times\setminus\{1\}$ is supported in $C_+$. Its Rayleigh quotient is $(r-3)/r$, giving $\beta_+\to1$ along square controls.

## A conditional gap from the adjacency conjecture

The positive sign set is the complement counterpart of the common nonneighbors of a nonadjacent pair in [Kunisky's extreme-edge conjecture, Conjecture 1.9](https://arxiv.org/html/2303.16475#S1.SS4). For the negative sign set, $x\mapsto1/(1-x)$ sends it bijectively to the common nonneighbors of the adjacent pair $0,1$. Both denominators have character $-1$, so it preserves the Paley sign of pair differences. In either case $\sigma T_{C_\sigma,C_\sigma}$ is permutation-similar to $(-T)_{D,D}=(J-I-2A_D)/\sqrt p$, where $D$ is the corresponding common-nonneighbor set and $A_D$ its ordinary adjacency matrix. The least adjacency eigenvalue bounds the compression to vectors orthogonal to the constant vector. Kunisky's stated degree-two conjecture gives the bound $\sqrt3/2+o(1)$ there for the positive sign. The extension in Remark 1.11 gives the same conditional bound for the negative sign.

The constant direction can be controlled using just two row-sum moments. For $x\in C_\sigma$ expand the indicator of $C_\sigma$ as $(1+\chi(y))(1+\sigma\chi(1-y))/4$ with the two endpoints removed. The quadratic correlations and the endpoint terms give, uniformly in $x$,

$$ \sigma (T\mathbf1_{C_\sigma})(x)=\frac{S(x)}{4\sqrt p}+O(p^{-1/2}),
   \qquad S(x)=\sum_y\chi\bigl(y(1-y)(x-y)\bigr). $$

For $x\ne0,1$, $-S(x)$ is the trace of the Legendre elliptic curve $Y^2=y(y-1)(y-x)$. Over $U=\mathbb P^1\setminus\{0,1,\infty\}$ the Legendre rank-two sheaf has geometric monodromy $\mathrm{SL}_2$ and is tame away from characteristic two. [Katz, Chapter 15](https://web.math.princeton.edu/~nmk/mellin324book.pdf). Its symmetric square has trace $S(x)^2-p$ and has no geometric invariants, as does the rank-two sheaf. Twisting either by the characters of $x$, $1-x$ or $x(1-x)$ preserves absence of invariants, since passage to the kernel of a finite character preserves the connected monodromy. The Grothendieck–Lefschetz trace formula and the weight bound on $H_c^1$ give a total $O(p)$ for the trace of each twisted rank-two sheaf and $O(p^{3/2})$ for each twisted symmetric square. The conductor is bounded uniformly since the sheaves are tame on the same triply punctured line. [Deligne, Weil II](https://numdam.org/articles/10.1007/BF02684780/). Expanding the two sign indicators then yields

$$ \frac1{|C_\sigma|}\sum_{x\in C_\sigma} \frac{S(x)}{\sqrt p}=O(p^{-1/2}),
   \qquad
   \frac1{|C_\sigma|}\sum_{x\in C_\sigma} \frac{S(x)^2}{p}=1+O(p^{-1/2}). $$

Thus for the normalized constant vector $e$ and $B=\sigma T_{C_\sigma,C_\sigma}$, $\langle e,Be\rangle=o(1)$ and $\|Be\|_2=1/4+o(1)$. If the largest Rayleigh quotient of $B$ on $e^\perp$ is at most $a+o(1)$, the variational principle applied to $\mathbb C e\oplus e^\perp$ gives

$$ \limsup_{p\to\infty}\beta_\sigma\le
   \lambda_{\max}\begin{pmatrix}0 &1/4\\ 1/4 &a\end{pmatrix}
   =\frac{a+\sqrt{a^2+1/4}}2. $$

In particular, any $a<15/16$ suffices for a uniform gap. At the conjectured adjacency edge, $a=\sqrt3/2$ gives $(2+\sqrt3)/4<1$ and makes both (2) and (3) quantitative for the corresponding sign. Weak convergence of the empirical eigenvalue measures permits isolated eigenvalues and does not imply the required bound on $e^\perp$.

## Split and nonsplit cyclic representations

Both signed compressions admit a cyclic matrix with two copies of one kernel. Write $x(z)=(z+z^{-1}+2)/4$. For the positive branch take the group $G_+=Q$ and omit $z=\pm1$. The map $z\mapsto x(z)$ is two-to-one onto $C_+$, with fibers $\{z,z^{-1}\}$. In fact for $z=t^2$, $x(z)=(t+t^{-1})^2/4$ and $x(z)-1=(t-t^{-1})^2/4$. Conversely, if $x\in C_+$, choose $a^2=x$ and $b^2=x-1$. Then $t=a+b$ has inverse $a-b$. Put $s_+(z)=\chi(1-z)$ on $G_+$.

For the negative branch choose a nonsquare $d\in\mathbb F_q$ and work temporarily in $\mathbb F_{q^2}$. Take $G_-$ to be the subgroup of squares of the norm-one torus, of odd order $(q+1)/2$, and omit $z=1$. For the unique square root $t(z)$ of $z$ in $G_-$, $t(z)+t(z)^{-1}\in\mathbb F_q$ and $(t(z)-t(z)^{-1})/\sqrt d\in\mathbb F_q$. Thus $x(z)$ is a nonzero square and $1-x(z)$ is nonsquare for $z\ne1$. Conversely, for $x\in C_-$ choose $a^2=x$ and $b^2=x-1$ with $a\in\mathbb F_q$ and $b^q=-b$. Then $t=a+b$ has norm one, and $z=t^2\in G_-$ maps to $x$. This map again has fibers $\{z,z^{-1}\}$. Put $s_-(z)=\chi((t(z)-t(z)^{-1})/\sqrt d)$ on $G_-$.

In both cases a direct factorization gives

$$ \sigma\chi(x(z)-x(w))=s_\sigma(z/w)s_\sigma(zw). $$

For the plus branch, use $4(x(z)-x(w))=(z-w)(zw-1)/(zw)$, with $z,w$ squares. For the minus branch, taking the product of the two arguments of $\chi$ in the kernel gives $4(x(z)-x(w))/d$. So $\sigma T_{C_\sigma,C_\sigma}$ is unitarily equivalent to the matrix $(2\sqrt q)^{-1}(s_\sigma(z/w)s_\sigma(zw))_{z,w}$ restricted to inversion-invariant functions, with the endpoints omitted. The isometry pulls a value back to its two preimages and divides by $\sqrt2$.

With the endpoints kept and $m_\sigma=|G_\sigma|$, put $\widehat s(\eta)=m_\sigma^{-1}\sum_z s_\sigma(z)\overline{\eta(z)}$. In a unitary cyclic Fourier basis the full matrix has entry at output $\ell$, input $h$ equal to

$$ \frac{m_\sigma}{2\sqrt q}\sum_{b^2=\ell/h}\widehat s(bh)\widehat s(b). $$

Expand the two kernel factors and sum over $w$ using character orthogonality. On the nonsplit group the sum has one term. The endpoint compression corresponds to imposing zero values at the omitted points in positional coordinates. Both positional factorizations were checked on every pair in the corresponding cyclic groups at $p=13,41,101$. This identity supplies an alternative matrix for a moment or norm estimate.

## FFT comparison

[The experiment](../neighbor_compression.py) evaluates the additive operator by cyclic FFT over the prime field or by a two-dimensional FFT over the quadratic extension, then uses a real symmetric Lanczos solve. Every reported vector has its residual checked. The small cases are also checked against the dense character matrices. The [first runs](../data/neighbor-compression.csv) and [million-order pair](../data/neighbor-compression-large.csv) give the following matched comparison.

| Prime $p$ | $\beta_+(p)$ | $\beta_-(p)$ | Square $q$ | $\beta_+(q)$ | $\beta_-(q)$ |
|---:|---:|---:|---:|---:|---:|
| 401 | 0.800866 | 0.847476 | 361 | 0.975956 | 0.854346 |
| 9413 | 0.875747 | 0.867522 | 9409 | 0.994321 | 0.867561 |
| 37253 | 0.873181 | 0.866121 | 37249 | 0.997105 | 0.867503 |
| 153649 | 0.866344 | 0.865390 | 151321 | 0.998595 | 0.866179 |
| 1000033 | 0.867508 | 0.866265 | 994009 | 0.999452 | 0.866703 |

The prime samples are consistent with a gap and with the rescaled law's edge $\sqrt3/2$. At $p=1000033$, the constant-vector image has norms $0.249888$ and $0.250039$ on the two signs. These are floating-point eigenvalue estimates, and residuals validate the reported approximate eigenpairs without certifying global upper bounds. The square positive branch exhibits the subfield obstruction, while the square negative estimates stay close to the prime ones.
