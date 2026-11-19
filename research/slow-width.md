# A quantified extension of fixed-width balance

The [weighted marked contraction](parallel-complexity-14.md) improves the cutoff below to every $s_q$ with $s_q\log_2^*q\to\infty$ and improves the sufficient one-width energy condition to $o(\log_2^*p)$. The original cutoff argument is recorded here.

The [fixed-width proof](parallel-fixed-width-13.md) also gives a slowly moving-width statement. Write $L(q)=\log_2^*q$ for the number of successive binary logarithms needed to reach at most one, and $T=\lfloor L(q)/10\rfloor$. For all sufficiently large field orders $q\equiv1\pmod4$,

$$\boxed{\displaystyle
\sup_{4\log(T)/T\le r\le1}|\log M_{q,\sigma}(r)|=O(T^{-2})
}\tag{1}$$

on either sign. Here $\log(T)$ is natural. This very slow cutoff is independent of the characteristic. In particular the result is consistent with the square-field boundary and leaves the scale $q^{-1/2}$ open.

## Quantifying a single even-polynomial step

Use the negative Mellin expressions, bad-character count, and rank estimate from [the fixed-width proof](parallel-fixed-width-13.md#2-mellin-traces-and-the-two-needed-estimates). Say an expression has complexity at most $N$ if it is the real part of at most $N$ terms $c_i A(M_i)$, with $|c_i|$, the generic ranks and convolution dimensions all at most $N$. Its pointwise absolute value is then at most $N^3$. Tate normalizations and the quadratic twists in the two lifts do not increase ranks or convolution dimensions.

Fix a target iteration depth $T\ge2$ and put $\varepsilon=T^{-3}$. Suppose $N\ge T^3$ and $B$ is a real negative approximation of complexity $N$. Let $R=N^3$. Rescale $u=(x+R)/(2R)$ and use the polynomial

$$
P_D(x)=R\sum_{j=0}^D |2j/D-1|\binom Dj u^j(1-u)^{D-j},
\qquad D=\lceil R^2/\varepsilon^2\rceil.
$$

It is even by reversing $j$. The binomial expectation and its variance bound its error on $[-R,R]$ by $R/\sqrt D\le\varepsilon$. Its sum of absolute monomial coefficients in $x$ is at most $R2^D$, since the corresponding sums for $u$ and $1-u$ are each at most one. In particular $D\le2N^8$.

In expanding $P_D(B)$, taking real parts and the two lifts adds at most a fixed factor per input. At degree $j\le D$, the number of terms is at most $(4N)^j$. The convolution dimension and generic rank of a word are bounded by $(2N)^j$, using the product dimension and the rank estimate inductively on their sum. The same rank bound holds after applying the quadratic twist that changes the local sign, and its new dimension is at most that rank. Replacing the scalar products of Mellin values by their convolution values costs at most $O(jN)$ exceptional characters per word, with pointwise error at most a constant times $(2N)^j$ there. This also accounts for replacing conjugates by Mellin duals. Projection from the full character group to the two-lift averages does not increase these support counts by more than a constant. The normalized $\ell_2$ error of this replacement is therefore bounded by $\exp(CD\log(N+1))/\sqrt q$ after summation with coefficients. The operator $K$ has normalized $\ell_2$ norm at most one. All these bounds use only the fixed-word inputs of the fixed-width proof.

It follows that for a universal $N_*$, if $N\ge\max(T^3,N_*)$, then $KP_D(B)$ is within $2^{2^N}/\sqrt q$ in normalized $\ell_2$ of a real negative expression of complexity at most $2^{2^N}$. This double-exponential allowance can absorb adding the bounded marked forcing and multiplying by the damping. The same allowance bounds the odd test

$$
\left|\frac1n\sum_k x_kP_D(B_k)\right|
\le\frac{2^{2^N}}{\sqrt q},\qquad x=\sqrt n K e_0.
\tag{2}
$$

Indeed, it adds one negative factor of bounded complexity to each even word. The odd-word trace at $1$ and exceptional characters have the same two error bounds as above. The universal $N_*$ absorbs the fixed constants in these estimates. No absolute-value operation in the rank-weighted representation algebra is used.

## Keeping the arithmetic error below the iteration error

Choose $N_0=\max(T^3,N_*)$ and $N_{j+1}=2^{2^{N_j}}$. For all sufficiently large $q$ with $T=\lfloor L(q)/10\rfloor$,

$$L(N_{T+2}^4)\le L(N_0)+2(T+2)+2<L(q),$$

where $x^4\le 2^{2^x}$ for $x\ge2$. Thus $N_{T+2}<q^{1/4}$. In particular the arithmetic error at every step and in the final odd test is at most $q^{-1/4}$.

Let $Y_t=\sqrt n\,v_t$ be the scaled damped Picard orbit from zero at $d=(1-r)/(1+r)$. The [exact separated recursion](parallel-fixed-width-13.md#3-direct-passage-through-absolute-value-with-the-marked-input-separated) is

$$Y_{t+1}=d(b_t x+K|Y_t|),\qquad b_t\in[0,2].$$

The Lipschitz constant of the absolute value and $\|K\|\le1$ imply inductively that $Y_t$ has a negative approximant of complexity $N_t$ and error at most $t(\varepsilon+q^{-1/4})$ in normalized $\ell_2$ for $t\le T$. At $t=T-1$, apply (2) after replacing $|Y_{T-1}|$ by the even polynomial of its approximant. Since $\|x\|_{2,n}\le1$, this shows $|(v_T)_0|=O(T^{-2}+Tq^{-1/4}+1/n)=O(T^{-2})$, uniformly over $d\in[0,1]$.

For $r\ge4\log(T)/T$ the fixed-point error is at most $2d^{T+1}/\sqrt{1-d^2}$. The bounds $d\le e^{-2r}$, $\sqrt{1-d^2}\ge\sqrt r$ give $O(T^{-2})$ in this range. The marker formula and reciprocity prove (1).

## Consequence for the one-width energy test

In the [two-width comparison](quadratic-fourth.md#a-one-sided-single-width-criterion), one may now take $s_p=4\log(T)/T$ and $r_p=p^{-1/3}$. On the larger-theta side it would suffice to prove

$$A_\sigma(r_p)=o(T/\log T).$$

The larger-width value balances by (1), the energy times $s_p-r_p$ tends to zero, and $r_p n^{1/4}\sqrt{A_\sigma(r_p)}$ tends to zero. This allows slow divergence at the smaller width and leaves its actual arithmetic estimate open. The complexity allowance is far above the sizes of the numerical fields, so (1) is an asymptotic proof and gives no effective numerical accuracy for those samples.
