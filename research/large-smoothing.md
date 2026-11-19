# A uniform bound for large smoothing weights

This argument uses the [local-inertia closure rules](iteration-parity.md) and keeps track of heterogeneous ranks, including bad Mellin characters. It proves $\|v^*\|_2\le6$ and $|v^*_0|\le6/\sqrt n$ for $\tau\ge1024$ and $n\ge\tau$. The bound holds over all odd field orders $q\equiv1\pmod4$. The theta bracket has width $\log(1+\tau)$ at these weights, so the result identifies a regime of uniform control for the smoothing equation. The range $\tau\downarrow0$ needed for Conjecture 26 remains open.

## An exact bound for even products

Keep $q=2n+1$, $K=F\operatorname{diag}(s)F^{-1}$ and $x=Fs/\sqrt n$. Write $\mathcal A(M)$ for the average of the two Mellin lifts on $\widehat Q$, as in the [fixed-depth argument](iteration-parity.md#uniform-fixed-expression-trace-estimates). For a negative-type $M$ of generic rank $r$, its convolution dimension is $r$, since it is tame and its sole interior singularity has no invariant stalk. In particular $|\mathcal A(M)(k)|\le r$ at every character by the compact-support trace bound. Define a norm on the span of these functions by

$$\|f\|_{\mathcal N}=\inf\left\{\sum_j|a_j|r_j^2:f=\sum_j a_j\mathcal A(M_j),\ r_j=\operatorname{rank}(M_j)\right\}.$$

This is a norm on a finite-dimensional subspace of $\mathbb C^n$ and dominates the supremum norm. The rank-one quadratic Kummer object gives $\|x\|_{\mathcal N}\le\sqrt{q/n}$. Its multiplicative-character twists give $\|K\delta_h\|_{\mathcal N}\le\sqrt{q/n}/\sqrt n$ for every coordinate vector $\delta_h$. Indeed $K\delta_h$ is the translate of $x/\sqrt n$, and translating the Mellin character twists the sheaf by a Kummer sheaf unramified at $1$.

Let $M,N$ be factors of one of the two types used in the closure rules, and let $d_M,d_N$ be their convolution dimensions. For factors with generic ranks $r_M,r_N$, their middle convolution has generic rank at most

$$r_M d_N+r_N d_M.$$

For two nonpunctual factors, a generic multiplicative fiber has the two different singular points $1$ and $a$. The rank drops there are $d_M r_N$ and $r_M d_N$ by the tame Euler characteristic formula. Its $H_c^2$ vanishes: a common constituent of the associated dual and translated local systems would have to have singularities both at $1$ only and at $a$ only. A constituent lisse on the entire multiplicative group and tame at both boundaries is Kummer and is excluded by the convolution category. Thus the compactly supported $H_c^1$ has that sum as its dimension, which bounds the generic rank of the middle convolution. Punctual summands at $1$ contribute their convolution dimensions times the other's generic rank, giving the stated bound for mixed factors. The convolution dimension of a product is the product of the dimensions. Iterating the rank bound by pairing negative factors first and then convolving the positive outputs shows that the even convolution of $m$ negative factors of ranks $r_j$ has generic rank at most $m\prod_j r_j$. This argument uses the generic fiber, so the punctual part has rank zero. [Katz, Chapters 2 and 19](https://web.math.princeton.edu/~nmk/mellin331.pdf) · [Rojas-León, Section 5](https://arxiv.org/pdf/1106.1398)

For an even product of $m\ge2$ negative fields, expand the two lifts using the $2^m$ choices of twisting the inputs by the quadratic character of $a$. Each twist preserves ranks and types. Each expanded product agrees with the Mellin trace of its middle convolution at characters good for the direct sum of its factors. The product of lift averages equals the average of these convolved lift averages, up to error on the projections of the bad characters. For each term there are at most $2\sum_j r_j$ bad full characters, or at most $4\sum_j r_j$ as a conservative count after averaging the two lifts. The error is bounded by $2\prod_j r_j$ per exceptional frequency. These bounds hold separately for each of the averaged products. [Katz, Chapter 1](https://web.math.princeton.edu/~nmk/mellin331.pdf)

Applying $K$ to an even convolution field twists the nonpunctual part by $\chi(1-a)$, yielding a negative object of rank at most $m\prod_j r_j$, and kills the punctual part. Applying $K$ to the error uses the bound on $K\delta_h$ above. Thus

$$\left\|K\prod_{j=1}^m\mathcal A(M_j)\right\|_{\mathcal N}
\le\left(m^2+\frac{8\sqrt{q/n}}{\sqrt n}m\right)\prod_{j=1}^m r_j^2.$$

Here $(\sum_j r_j)\prod_j r_j\le m\prod_j r_j^2$ since all $r_j\ge1$. The bound applies to every even $m$ after distributing finite linear combinations and taking infima. In particular for $n\ge1024$,

$$\|K f^{2\ell}\|_{\mathcal N}\le 2(2\ell)^2\|f\|_{\mathcal N}^{2\ell}.$$

The exceptional frequencies are included explicitly in this inequality. No approximation in $q$ is needed.

## Applying the bound to the full iteration

Use $V_t=\sqrt n\,v^{(t)}$, $V_0=0$ and the exact recurrence

$$V_{t+1}=b_t x+K\sqrt{V_t^2+4\tau},\qquad b_t=\sqrt{4+(v^{(t)}_0)^2}-\sqrt{(v^{(t)}_0)^2+4\tau/n}.$$

If $n\ge\tau$, then $0\le b_t\le2$. Assume inductively $\|V_t\|_{\mathcal N}\le6$. Set $z=9/\tau$. For $\tau\ge1024$, the binomial series for the activation converges pointwise absolutely on this range. After applying $K$, it converges absolutely in $\mathcal N$ by the even-product estimate. The constant term vanishes. Using $\sum_{\ell\ge1}|\binom{1/2}{\ell}|z^\ell=1-\sqrt{1-z}$ gives

$$\left\|K\sqrt{V_t^2+4\tau}\right\|_{\mathcal N}
\le 4\sqrt\tau\sum_{\ell\ge1}(2\ell)^2|\tbinom{1/2}{\ell}|z^\ell
=4\sqrt\tau\frac{z(2-z)}{(1-z)^{3/2}}<2.4.$$

The forcing contributes at most $2\sqrt{q/n}<2.84$, so the radius $6$ is invariant. At each fixed $q$ the exact Picard iteration converges, since its componentwise activation has derivative strictly smaller than $1$ in absolute value on bounded sets and $\|K\|_{2\to2}\le1$. The bound $\sqrt n\,\|v^*\|_\infty\le6$ follows on taking the limit. It yields both claimed estimates. This majorant uses the Taylor radius set by the branch points $\pm2i\sqrt\tau$. It leaves open whether a different norm or a prime-field estimate can reach smaller smoothing weights.
