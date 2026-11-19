# Cyclotomic tests for rational endpoint candidates

The [multi-reference endpoint test](endpoint-mixture.md) can return a bulk vector with only a few nonintegral coordinates. For a rational vector of this kind, Galois conjugation adds constraints to the possible Fourier support. On primes whose group order has a large prime factor, it forces a short period for every exactly feasible rational spectrum. For low-denominator approximations it gives an explicit lower bound on forbidden energy.

## Pure order layers determine rational feasibility

Let $p\equiv1\pmod 4$ be prime, $Q=\mathbb F_p^{\times2}$, $n=|Q|$, and $s(t)=\chi(1-t)$. Fix a generator $g$ of $Q$. Index a real frequency vector by the $n$ characters with values $\zeta_n^{ij}$ on $g^j$. Its unnormalized Fourier values on $Q$ are

$$F_b(g^j)=\sum_{i=0}^{n-1} b_i\zeta_n^{ij}.$$

On the order-$d$ layer $\{t\in Q:\operatorname{ord}(t)=d\}$, these values are Galois conjugates when $b$ is rational. Vanishing on one member of the layer forces vanishing on all of it. Thus for $P_{-\sigma}b=0$, all nonconstant Fourier values of a rational $b$ lie in layers on which $s$ is identically $\sigma$. Conversely one can prescribe rational Fourier subspaces on any such layers. The rational polynomial $\sum_i b_i X^i$ must be divisible by the product of the $\Phi_d$ for all deleted layers, so the rational dimension is $1+\sum_d\varphi(d)$ over the pure layers. The least common multiple of their orders bounds the period of $b$.

For the subgroup of order $e$ in $\mathbb F_p^\times$, the sum of $\chi(1-t)$ over it is the average of the Jacobi sums $J(\psi,\chi)$ over characters trivial on that subgroup. Each term has magnitude at most $\sqrt p$, with magnitudes one in the degenerate cases. Möbius inversion on orders gives

$$\left|\sum_{\operatorname{ord}(t)=d}s(t)\right|\le2^{\omega(d)}\sqrt p.\tag{1}$$

For $d>1$ both signs therefore occur when $\varphi(d)>2^{\omega(d)}\sqrt p$. [Jacobi sum conventions and bounds](https://arxiv.org/html/2303.16475#S3.SS2)

Write $n=m\ell$ with $\ell$ prime and $\ell-1>4\sqrt p$. Then $\ell\nmid m$. For $d=\ell e\mid n$, the bound $2^{\omega(e)}/\varphi(e)\le2$ follows factor by factor. Consequently every layer whose order contains $\ell$ has both signs. Any rational feasible $b$ on either side now has period dividing $m$. If it is nonnegative and anchored at one, its total mass is at least $\ell$. In particular it cannot satisfy the endpoint box with any fixed target root $t$ when $\ell/\sqrt n\to\infty$. This restriction concerns the rational test vectors; the actual endpoint minimizer can have algebraic coordinates.

## Quantitative exclusion using a cyclotomic norm

Suppose $b_0=1$, $0\le b_i\le1$, $w_i=Db_i\in\mathbb Z$, and $k=\sum_i b_i$, with positive integer $D$ and $Dk<\ell$. Fold the scaled weights modulo $\ell$ by $c_i=\sum_{j\equiv i\bmod\ell} w_j$. Set

$$W(X)=\sum_{i=0}^{\ell-1}c_i X^i,\quad
R=\left|\operatorname{Res}(\Phi_\ell,W)\right|,\quad
S=\ell\sum_i c_i^2-(Dk)^2.$$

Since $W$ has nonnegative integer coefficients and sum $0<Dk<\ell$, it cannot be a multiple of $\Phi_\ell$. Thus $R\ge1$. The sum of the squared magnitudes of its values at nontrivial $\ell$th roots is the exact integer $S$ by Parseval. These values are $D$ times the original Fourier values on the primitive $\ell$ layer. Let $a$ and $f$ count the allowed and forbidden positions in that layer for the sign under test. When both are positive, let $S_f$ and $S_a$ be the separate energies of the scaled values. Arithmetic–geometric mean gives

$$R^2\le (S_f/f)^f(S_a/a)^a\le (S_f/f)^f(S/a)^a.$$

Dropping the forbidden modes outside that layer gives the explicit lower bound

$$\boxed{\displaystyle
\|P_{-\sigma}b\|_2^2\ge\frac{f}{nD^2} R^{2/f}\left(\frac{a}{S}\right)^{a/f}.}\tag{2}$$

If $\ell\ge p^{1/2+\epsilon}$ with fixed $\epsilon>0$, then $a,f=(\ell/2)(1+O(p^{-\epsilon}))$ by the subgroup bound and the zero at the identity. The cap $c_i\le mD$ gives $S\le\ell mD^2 k$. Since $Dk<\ell$, the effect of replacing $a/f$ by one in the lower bound that uses $R\ge1$ is $1+o(1)$, uniformly in these denominators and masses. Therefore

$$\|P_{-\sigma}b\|_2^2\ge \frac{1-o(1)}{4m^2D^4 k}.\tag{3}$$

For bounded $m,D$ and $k=O(\sqrt n)$ this is a lower bound of order $n^{-1/4}$ for the norm. At $r=p^{-1/3}$, if the opposite allowed energy is $O(\log_2^*p)$ then the anchored actual optimizer has forbidden norm $O(r\sqrt{\log_2^*p})$ by reciprocal complementarity and the uniform root cap. In that case (3) rules out approximating its whole vector to $o(p^{-1/4})$ in ordinary $\ell_2$ by such bounded-denominator rooted vectors. The norm estimate does not transfer to an arbitrary few fractional coordinates, where the denominators may be large or the entries irrational.

For the consecutive indicator $b=\mathbf1_{\{0,\ldots,k-1\}}$ with $1\le k<\ell$, the product has exactly $R=1$ since $W(\zeta)=(1-\zeta^k)/(1-\zeta)$ and powering by $k$ permutes the primitive roots. This limits the norm-only strengthening in (2). An adaptive indicator chosen from the largest reference defects can have a much larger $R$. At square order $q=h^2$, the exact subfield witness $b=\mathbf1_{(\mathbb F_h^\times)^\perp}$ is integral, has mass $(h+1)/2$ and has zero forbidden energy on the plus side.

## A determinant that cancels fractional coordinates

Let $b$ be real, $b_0=1$, $0\le b_i\le1$, and $k=\sum_i b_i$. Suppose its fractional coordinates meet only $h$ residue classes $e_1,\ldots,e_h$ modulo a prime $\ell>h+1$. Write its folded polynomial as $U(X)+\sum_j\alpha_j X^{e_j}$, where $U=\sum_d u_d X^d$ has integer coefficients and $\alpha_j$ are real. For $h+1$ signed integers $t_i$ distinct and nonzero modulo $\ell$ define the Laurent polynomial

$$
\mathcal D(Z)=\det\left[\left(Z^{t_i e_j}\right)_{i,j}\ \bigg|\ \left(U(Z^{t_i})\right)_i\right].
$$

Adding the fractional part to the last column leaves the determinant unchanged. Choose the $t_i$ from $1,-1,2,-2,\ldots$ in that order and put $d_h=\lceil(h+1)/2\rceil$. A sufficient nonvanishing condition at a primitive $\ell$th root is

$$\sum_d u_d\prod_{j=1}^h(d-e_j)\not\equiv0\pmod\ell.\tag{4}$$

To prove this, expand the monomial determinant with the last exponent equal to $d$ using $Z=\exp X$. The lowest possible power is $H=h(h+1)/2$, since every term in the determinant needs $h+1$ distinct degrees. Its coefficient is the product of the two Vandermondes in the $t_i$ and the exponents $(e_1,\ldots,e_h,d)$ divided by $\prod_{j=0}^h j!$. The coefficient for $\mathcal D$ is therefore a nonzero fixed factor times the sum in (4) modulo $\ell$, for sufficiently large $\ell$. Substituting $X=\log Z$ preserves the leading coefficient at $Z=1$. Dividing by $(Z-1)^H$ and reducing at $Z=\zeta_\ell$ modulo $\zeta_\ell-1$ now gives a nonzero residue. One can also check $\mathcal D(\zeta_\ell)\ne0$ directly by exact resultant.

Let $G$ be the set of nonidentity points $v$ of the positional subgroup of order $\ell$ for which every $v^{t_i}$ has forbidden sign. Since $s(v^{-j})=s(v^j)$, this takes only $d_h$ sign tests, at powers $1,\ldots,d_h$. Expanding the sign indicators and averaging over characters trivial on the subgroup gives

$$|G|=2^{-d_h}(\ell-1)+O_h(\sqrt p).\tag{5}$$

For each nonempty subset of powers, the corresponding product of $1-X^j$ has a simple nonzero root of order its largest included $j$. Twisting by a subgroup character preserves nontrivial quadratic inertia at that root, so the complete twisted character sum has the $O_h(\sqrt p)$ Weil bound. [Character sum estimates](https://arxiv.org/html/2303.16475#S3.SS2.SSS0.Px1)

If $\mathcal D(\zeta_\ell)\ne0$, the absolute product of its conjugates is at least one. Identify $v=g^{m j}$ with $\zeta_\ell^j$. After replacement of the last column by the true fractional Fourier values, Hadamard's inequality bounds the sum of $|\mathcal D|^2$ over $G$ by $C_h$ times the layer's forbidden energy, with $C_h=(h+1)^{h+1}$. Indeed each column other than the last has squared norm $h+1$ and each power map is injective. Over the complementary points the same bound is at most $C_h\ell m k$ by Parseval and the cap $m$ on the folded weights. For $0<g_0=|G|<\ell-1$, set $b_0'=\ell-1-g_0$. The product and arithmetic–geometric mean give

$$\boxed{\displaystyle
\|P_{-\sigma}b\|^2\ge \frac{g_0}{nC_h}\left(\frac{b_0'}{C_h\ell m k}\right)^{b_0'/g_0}.}\tag{6}$$

For fixed $h$, $\ell\ge p^{1/2+\epsilon}$, this has order at least $m^{-1}(mk)^{-(2^{d_h}-1)}$, with a constant permitted to depend on $h$. In the single-fraction case, inversion pairs share their sign and the exponent stays one. The determinant is

$$Z^{e_1} U(Z^{-1})-Z^{-e_1}U(Z),$$

which vanishes at $\zeta_\ell$ exactly when the integer part is symmetric around $e_1$ modulo $\ell$. Indeed the reduced coefficients have zero sum, so a vanishing polynomial of degree at most $\ell-1$ has all coefficients zero. In the nonsymmetric case the norm bound remains of order $n^{-1/4}$ for bounded $m$ and $k=O(\sqrt n)$, with arbitrary real fractional value. The determinant condition and the exponent in (6) limit the extension to general almost integral spectra.

### An unconditional bound for a fixed number of fractional classes

Assume $h$ is fixed, $\ell\ge p^{1/2+\epsilon}$ and $k=O(\sqrt n)$. The determinant can instead be chosen by averaging over arbitrary distinct powers. Suppose first that the integer part has some nonzero coefficient outside the $h$ fractional residue classes. Take $t_1,\ldots,t_{h+1}$ uniformly without replacement from the nonzero residues modulo $\ell$. Given the first $h$ rows, their square minor in the fractional columns is invertible by the prime cyclic Fourier minor theorem. There is a unique combination of the fractional columns that subtracts these first $h$ values of $U$. The resulting nonzero folded vector has support at most $k+h$. The prime uncertainty principle allows at most $k+h-1$ zero Fourier coefficients, so the probability of a zero augmented determinant is $O((k+h)/\ell)=o(1)$. [Prime Fourier minors and uncertainty](https://arxiv.org/abs/math/0308286)

For each fixed nonzero multiplier $j$, the probability that all $g^{m j t_i}$ are forbidden is $(f)_{h+1}/(\ell-1)_{h+1}$, where $(x)_a=x(x-1)\cdots(x-a+1)$ and $f$ is the primitive forbidden count. Thus the expectation of $|G|$ is $(2^{-(h+1)}+o(1))\ell$. The degenerate tuples account for $o(\ell)$ of this expectation, so one nondegenerate tuple has $|G|\ge(2^{-(h+1)}-o(1))\ell$. Each tuple uses the same Hadamard estimate in (6). Also $|G|\le f$, so its complement has size comparable to $\ell$. The resulting lower bound is

$$\|P_{-\sigma}b\|^2\ge \frac{c_h}{m}\,(m k)^{-(2^{h+1}-1+o(1))}.\tag{7}$$

The error in this exponent is $O_h((k+h)/\ell+\sqrt p/\ell+1/\ell)$, so replacing it by zero changes the bound by a bounded factor. If the integer part is supported on the fractional residue classes, the entire folded vector is supported on at most $h$ points. The primitive forbidden Fourier Gram matrix on those points has diagonal $f$ and off-diagonal entries bounded by $(1+\sqrt p)/2$ in modulus. This follows by writing the negative-sign indicator as half the difference of the constant and signed characters, with the identity omitted. The Jacobi average for each nontrivial subgroup character gives the stated bound. Thus its quadratic form is at least $(f-(h-1)(1+\sqrt p)/2)$ times the folded squared norm, which is at least one from the anchor. This yields forbidden energy $\gtrsim1/m$ in this case.

Formula (7) applies to arbitrary real values in the fractional classes. It retains a polynomial loss for each fixed number of classes, including nonsymmetric endpoint tests, and is too weak to give a uniform positive margin for the mixed-reference certificate.

Exact feasibility alone gives a separate support bound even without rationality or a limit on the number of fractional classes. If $P_{-\sigma}b=0$, all $f$ primitive forbidden values of the folded vector vanish. A nonnegative anchored $b$ has a nonzero folded vector. The prime uncertainty principle then forces at least $f+1$ occupied classes modulo $\ell$.

## Exact finite-order comparisons

The [replay](../rational_endpoint.py) uses exact cyclotomic resultants and Arb outward rounding. For each prime it compares the consecutive indicator with an indicator at the most negative coordinates of the projected reference at $s=p^{-1/6}$. Both are anchored and take at most $\lfloor0.97\sqrt n\rfloor$ coordinates. With `--one-fraction`, the next coordinate provides the remaining fractional mass. The determinant bound uses $k+1$ as a mass upper bound and holds for any value of that coordinate in $[0,1]$. The reference selection and measured forbidden energies are floating point. The lower bounds use the selected positions, integer weights and sign layer.

The [51 recorded rows](../data/rational-endpoint.csv) include 36 rational trials, 12 single-fraction trials and three exact square subfield controls. All consecutive indicators with denominator one have cyclotomic norm one. Eleven of the single-fraction rows obtain a strictly positive bound from the reciprocal determinant. The determinant vanishes on the $p=29$ plus row. This is a finite instance of the symmetry condition before (7). At $p=9533$ the pure-layer period bounds are one and two on the plus and minus sides respectively.

| Plus side at $p=9533$ | Measured forbidden layer energy | Bound using norm at least one | Bound using exact norm |
|---|---:|---:|---:|
| Consecutive indicator | 14.53160 | 0.001748 | 0.001748 |
| Reference-defect indicator | 13.43791 | 0.001643 | 0.835189 |
| Reference-defect row with one fractional coordinate | 13.45992 | 0.000049 | 0.018682 |

Bounds are rounded downward in the table.

~~~sh
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python rational_endpoint.py 29 173 509 1109 2693 9533 --square-characteristics 11 43 97 --one-fraction
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python rational_endpoint.py 173 509 2693 --denominator 3
~~~
