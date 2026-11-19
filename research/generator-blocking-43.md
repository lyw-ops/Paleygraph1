# Near-minimal prime support has high additive energy

Let \(p=2n+1\equiv1\bmod4\) be prime. In the cyclic frequency group \(G=\widehat Q=\mathbb Z/n\), let \(S\) be the exact support of a nonzero affine Paley spectrum of either sign. The spectrum may be complex and need not be positive. There is an absolute \(c>0\) such that if

\[
|S|=m\le\sqrt n+c n^{1/4},
\]

then, as \(p\to\infty\),

\[
E(S)=\sum_{h\in G}|S\cap(S-h)|^2\ge n^{3/2-o(1)}.
\]

Moreover \(n\) has a divisor \(d_*\) satisfying \(d_*=n^{1/2+o(1)}\). Under the stricter slack \(m\le\sqrt n+o(n^{1/4})\), all but \(o(m^2)\) ordered pairs in \(S^2\) have differences of order at most \(n^{1/2+o(1)}\) in \(G\). These conclusions restrict exact optimal supports and exclude low additive energy in the stated width. They do not bound the ordinary theta value.

## Blocking intervals in all unit directions

The [prime affine rank theorem](parallel-low-energy-7.md#a-missing-interval-and-an-affine-rank-bound) shows that \(S\) meets every interval of length \(m+1\) in every generating direction. The unit dilations needed here are guaranteed by the cyclotomic Galois argument in that theorem. Thus after multiplying \(S\) by any unit \(u\) modulo \(n\), its \(m\) consecutive cyclic gaps \(g_i\) all satisfy \(g_i\le m+1\). Write \(R=m(m+1)-n\ge0\), take \(1\le L<n/2\) with \(L<m+1\), and put

\[
k=\left\lfloor R/(m+1-L)\right\rfloor.
\]

At most \(k\) of the gaps of \(uS\) can be at most \(L\), since all gap deficits are nonnegative and sum to \(R\). If \(k<m\), the short gaps form disjoint consecutive runs on the circle. Every ordered pair at forward separation at most \(L\) has its entire forward path inside one of these runs. A run of \(a\) gaps accounts for at most \(a(a+1)/2\) pairs, uniformly in the gap lengths. Summing gives at most \(k(k+1)/2\) such pairs for every \(u\). For any one fixed separation \(j\in[1,L]\), the stronger single-shift bound is \(k\), since each such pair starts at a short gap and a start determines its endpoint.

## Average over the unit directions

Define the elementary factors

\[
A_n=2^{\omega(n)+1}n/\varphi(n),\qquad
\mathcal D=\{h\in G:\operatorname{ord}(h)<A_n n/L\}.
\]

For a nonzero difference \(h\) let \(d=\gcd(h,n)\) and \(M=n/d\). Uniform \(u\) among the units modulo \(n\) makes \(uh\) uniform on the \(\varphi(M)\) residues \(d a\) with \(a\) a unit modulo \(M\). The reduction from units modulo \(n\) onto units modulo \(M\) is surjective by prime-power decomposition. Inclusion–exclusion gives

\[
\Pr(uh\in[1,L])
=\frac{\#\{1\le a\le L/d:(a,M)=1\}}{\varphi(M)}
\ge \frac Ln-\frac{2^{\omega(M)}}{\varphi(M)}.
\]

If \(h\notin\mathcal D\), so \(d\le L/A_n\), the second term is at most \(L/(2n)\). Indeed \(\varphi(M)/M\ge\varphi(n)/n\), and \(L/d\ge2^{\omega(n)+1}n/\varphi(n)\). Thus the uniform short-pair bound yields

\[
\#\{(i,j)\in S^2:j-i\notin\mathcal D\}
\le \frac{n}{L} k(k+1).                                       \tag{1}
\]

Also every nonzero \(h\) with \(\gcd(h,n)\le L\) obeys \(|S\cap(S-h)|\le k\), by a unit carrying \(h\) to the integer \(\gcd(h,n)\) and the fixed-separation estimate above.

Take \(L=\lfloor m/2\rfloor\). In the range of the theorem, \(m\sim\sqrt n\), \(R\le(2c+o(1))n^{3/4}\), and \(k\le(4c+o(1))n^{1/4}\). For example, \(c=1/16\) makes the upper bound in (1) at most \(m^2/2\) for all sufficiently large \(n\). Under slack \(o(n^{1/4})\) it is \(o(m^2)\).

The elementary divisor bounds \(A_n,\tau(n)=n^{o(1)}\) are enough now. The first uses \(\omega(n)!=O(n)\) and \(n/\varphi(n)\le2^{\omega(n)}\). For the second, for every \(\epsilon>0\) use \(a+1\le\ell^{\epsilon a/2}\) on prime factors \(\ell\) above the fixed threshold \(2^{2/\epsilon}\). The remaining primes give at most a fixed power of \(1+\log n\). Counting by exact orders shows

\[
|\mathcal D|
=\sum_{d\mid n,\ d<A_n n/L}\varphi(d)
\le \tau(n)\, A_n n/L
=n^{1/2+o(1)}.
\]

Since at least half the ordered pairs have difference in \(\mathcal D\), Cauchy–Schwarz gives \(E(S)\ge m^4/(4|\mathcal D|)\). Moreover some individual first coordinate of a pair has at least \(m/2\) second coordinates with differences in \(\mathcal D\), so \(|\mathcal D|\ge m/2\). There must be a divisor of \(n\) between \(m/(2\tau(n))\) and \(A_n n/L\). This proves all the assertions.

## Consequence for a moving stationary floor

If a candidate high set of the actual prime stationary row has size \(m\le\sqrt n+\tfrac1{16}n^{1/4}\) and its energy is at most \(n^{3/2-\epsilon}\) for some fixed \(\epsilon>0\), it must miss a generator interval of length \(m+1\), by the combinatorial proof. This conclusion no longer requires knowing which direction contains the gap. For the normalized stationary probabilities and fixed high threshold \(\rho<1\), the [cyclotomic leakage estimate](parallel-low-energy-7.md#quantitative-exterior-mass-and-the-true-stationary-high-set) then excludes such a high set at floors \(t_p\le\exp(-p^2)\). Indeed its lower exterior \(L^2\) bound is \(n^{-m\varphi(n)/2}\|\mu_S\|_2^2\), while the stationary exterior upper bound is \(O_\rho(t_p/n)\) and \(\mu(S)\to1\). This transfers the geometry to actual positive floors in a very small regime. There is no transfer here to a fixed floor, nor is a sufficiently small high set known to capture the relevant critical witness.

The [finite exact replay](generator-blocking-43-check.py) checks the oriented-gap counts for blocking masks, counts the unit orbit of each difference directly, and includes true affine supports obtained as annihilators of monochromatic subgroups. The low-energy exclusion above rests on the proof.
