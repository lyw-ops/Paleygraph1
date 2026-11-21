# Counting control of the actual inverse line

Use the Fourier correspondence of [the same-row pairing](cold-same-row-involution-139.md). Let \(D_1,D_2\) be any of the two actual frozen derivatives at \(601,602\) or the pure-seed derivative on the original square. For any \(x,y\in G\) with \(y\ne1\), the actual position kernel satisfies
\[
 |(K D_1 K D_2)(x,y)|\ll p^{-1/2}
\]
uniformly through sufficiently large eligible primes. The estimate uses the original marked floors. The position identity column \(y=1\) does not occur on the mean-zero frequency domain.

## The normalized inverse Fourier rows

Write \(d_i\) for the full inverse Fourier row of \(D_i\) on \(G\). Expanding the odd analytic bulk derivative, each word corresponds at good full Mellin characters to the compact Mellin trace of its odd middle convolution. The quotient lift average is exactly the Fourier transform of the restriction of its position trace to \(G\). The product-lift discrepancies in this expansion are confined to the base pair. The [odd arity rank and parity estimates](cold-actual-first-insertion-126.md#uniform-word-cost-and-the-two-translated-columns) give a row representation
\[
 d_i(a)=\sum_{u} c_u t_u(a)+e_i(a),\qquad
 \sum_u |c_u|r_u=O(1),\qquad \|e_i\|_{\infty}=O(p^{-1}).       \tag{1}
\]
Here \(t_u\) is the trace of a nonpunctual pure weight-zero perverse middle extension with ordinary lisse rank \(r_u\). It is tame, lisse away from \(1\) on the multiplicative line, and its ordinary sheaf has weight \(-1\). Local convolution preserves tameness and confines the finite singularities to \(1\). Odd arity excludes punctual summands at \(1\), so \(|t_u(a)|\le r_u/\sqrt p\) also at \(a=1\) by the middle-extension stalk weight bound. [Local convolution, Corollaries 5.3 and 5.9](https://arxiv.org/pdf/1106.1398) · [Inherited trace and parity conventions](iteration-parity.md)

For (1), the rank at order \(m=2\ell+1\) is priced by \(m\) times the product of convolution dimensions. The absolute sum is bounded by a constant times \(\sum_\ell (2\ell+1)(4.8/\sqrt N)^{2\ell+1}\), with \(N=4\inf_Q\Re t>(4.8)^2\). The endpoint budgets below \(4.8\) come from the [height-601 prefix](cold-combined-height-130.md) and the [verified height-602 update](cold-resummed-136-check.py). The pure seed has smaller budget. The bad-lift errors have summable frequency amplitudes on the one quotient coordinate of the base pair. Restoring the bounded marked diagonal difference adds a term on that same coordinate. The inverse transform of this point mass has constant modulus of order \(1/n\). This accounts for \(e_i\) while keeping the exact physical operator.

## A nontrivial inertia in the intermediate variable

The case \(x=1\) vanishes from the outer \(s(x)\). Fix \(x,y\ne1\). For two single traces in (1), write the spatial kernel sum as
\[
 s(x)\sum_{z\in G}s(z)t_u(x/z)t_v(z/y).
\]
On the open subset of \(\mathbb P^1\) obtained by deleting \(0,\infty,1,x,y\), the product inside this sum is the trace of a tame local system of ordinary weight \(-2\), up to the two perverse shift signs which cancel. Insert the square indicator \((1+\chi(z))/2\) to give two sums over full nonzero \(z\). The extra Kummer twist is unramified at \(1\). At \(z=1\) both pulled-back factor sheaves are lisse since their arguments are \(x\) and \(1/y\). The \(s(z)\) factor has nontrivial scalar quadratic inertia, so the tensor product has no geometric coinvariants. Thus \(H_c^2=0\) for either twisted sum. Tame Euler–Poincaré bounds \(\dim H_c^1\le3r_u r_v\), including the case \(x=y\) with fewer punctures. The weight bound for \(H_c^1\) gives \(O(r_u r_v/\sqrt p)\) for the open sum. Deleted nonzero points contribute \(O(r_u r_v/p)\) by the stalk bound. [Deligne, Weil II, §3.3](https://www.numdam.org/item/PMIHES_1980__52__137_0.pdf)

The row errors in (1) change the kernel by \(O(p^{-1/2})\) using only \(\|d_i\|_\infty=O(p^{-1/2})\) and \(|G|=n\). The finite uniform rank sums permit summation over all analytic words. This proves the asserted kernel estimate.

In particular the operator supported on the inverse line \(y=x^{-1}\) of the actual square difference has counting operator norm \(O(p^{-1/2})\). Each row has at most one such entry and inversion permutes the input. On inversion-even inputs the line is simply a position multiplier. The full kernel estimate controls entries, and the inverse-line estimate controls counting norm. Neither gives an upper in the translated physical packet price. The remaining inverse-line task is to represent that position multiplier on the actual translated packet class with a small price.
