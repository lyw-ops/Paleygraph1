# Finite phase reduction for critical coset unions

Let $p\equiv1\pmod4$ be prime, $Q$ the nonzero squares, $n=(p-1)/2$, $s(x)=\chi(1-x)$ on $Q$ and $m_0=n/\sqrt p$. A feasible spectral probability $\mu$ is a nonnegative probability on $\widehat Q$ with $f_\mu(x)=\sum_k\mu_k k(x)=0$ when $x\ne1$ and $s(x)\ne\sigma$, for a fixed sign $\sigma$. In particular each of the two normalized stationary spectra is such a probability.

For both signs there are constants $\epsilon,c>0$ such that, for all sufficiently large primes, a union $U$ of at most eight cosets of one frequency subgroup with $|U|\le(1+c)m_0$ satisfies $\mu(U)\le1-\epsilon$. For even feasible spectra, including the stationary pair, the conclusion extends to eleven cosets. The cases through five have a direct cyclic construction. The higher ranks use the exact finite verification below. The earlier [argument for at most three cosets](parallel-stationary.md#the-prime-field-mass-gap) has a larger stated size range and does not require a compactness step.

## From all the mass to an exact finite quotient

The Jacobi entry bound and $\sigma K\mu=\mu-\mathbf1/n$ give $\mu_k\le(1+\sqrt p)/n$. Suppose along a sequence of orders that $U$ is a union of a fixed number $r$ of cosets of $G$, $|U|\le(1+o(1))m_0$ and $\mu(U)\to1$. The point cap forces $|U|\sim m_0$ and $\|\mu-\mathbf1_U/|U|\|_1=o(1)$. Indeed the positive part of its difference with the uniform probability on $U$, inside $U$, has sum at most $[(1+\sqrt p)|U|/n-1]_+=o(1)$, and the total exterior mass is $o(1)$.

Put $B=G^\perp$, $b=|B|\sim r\sqrt p$. Restricted to $B$ the uniform probability on $U$ has Fourier transform $r^{-1}\sum_{j=1}^r \gamma_j(x)$ for the $r$ distinct restricted coset characters. Divide by $\gamma_1$ so that $\gamma_1=1$, which preserves the nonvanishing condition. Send $x\in B$ to its relative phases $(\gamma_2(x),\ldots,\gamma_r(x))\in\mathbb T^{r-1}$. Write $\nu_p$ for the resulting Haar probability on the finite subgroup $L_p$, and $\omega_p$ for the pushforward of the same uniform measure weighted by $\sigma s(x)$. Extract simultaneous weak limits $\nu,\omega$. Each Fourier coefficient of $\nu_p$ is zero or one. The indices whose coefficients are eventually one form a subgroup $\Lambda\le\mathbb Z^{r-1}$, so $\nu$ is Haar probability on $L=\Lambda^\perp$. The coordinate characters remain distinct on $L$ because each of their nontrivial pairwise quotients has mean zero at every order.

For every fixed character $\xi$ of the torus, its pullback to $B$ extends to $Q$. Averaging the full Jacobi bound over the annihilator $G$ gives $|\widehat\omega_p(\xi)|\le\sqrt p/b$, hence $|\widehat\omega(\xi)|\le1/r$. With $F=\sum_{j=1}^r\gamma_j$ as a function of the phases, we also have $\int|F|^2\,d(\nu-\omega)=0$. At finite order, $\nu_p-\omega_p$ is positive, and at any point contributing to it other than the identity of $B$ the normalized modulus $|F|/r$ is bounded by $\|\mu-\mathbf1_U/|U|\|_1$, by feasibility. The single exceptional identity contributes only $O(r^2/b)$. Thus $0\le\nu-\omega\le2\nu$ and it is supported on the zero set of $F$.

Partition the $r$ coordinate characters by equality of their restrictions to the identity component $L^0$ of $L$. For any class $I$, set $F_I=\sum_{j\in I}\gamma_j$. On each connected component of $L$, the zero set of the real-analytic function $F$ has Haar measure zero unless $F$ vanishes identically on the component. In the latter case all the class sums $F_I$ vanish there by independence of distinct characters on $L^0$. Thus each $F_I$ vanishes $(\nu-\omega)$-almost everywhere. Orthogonality on $L$ and the Fourier bound give

$$|I|=\int|F_I|^2\,d\nu=\int|F_I|^2\,d\omega\le |I|^2/r.$$

This forces just one class. Since the first character is trivial and the others give the torus coordinates, $L^0$ is trivial, so $L$ is finite. A finite generating list for $\Lambda$ is eventually trivial on the approximating groups $L_p$, hence $L_p\subseteq L$ eventually. Convergence of the Haar probabilities on this finite set forces $L_p=L$ for all sufficiently large members of the subsequence. In particular $L$ is cyclic and its order is bounded along the subsequence.

The finitely many nonzero values of $|F|$ now have a positive minimum. The uniform approximation by $f_\mu$ shows that $s(x)=\sigma$ holds **exactly** whenever $x\ne1$ in $B$ and its phase belongs to $\{F\ne0\}$. In particular the kernel of the phase map is a monochromatic multiplicative subgroup of order comparable to $\sqrt p$. The signed limit also satisfies $\widehat\omega(\gamma_i/\gamma_j)=1/r$ for each pair, since $\int|F|^2d\omega=r$ saturates the sum of the $r^2$ Fourier bounds. These reductions hold for arbitrary bounded $r$.

### An explicit bound on the finite quotient

The exact feasible-mass case even gives a common finite set of possible orders at each $r$. For a prime $\ell$, let $k_\ell$ be the least positive integer with $\ell^{k_\ell}>2r$. Then the order $d$ of the finite phase group satisfies

$$v_\ell(d)\le k_\ell-\mathbf1_{\ell>r}.$$

Write $F(t)=\sum_j\gamma_j(t)$ on $\mathbb Z/d\mathbb Z$. For $\ell\le r$, partition the characters by whether their ratio has $\ell$-primary order at most $\ell^{k_\ell}$. For $\ell>r$ use the threshold $\ell^{k_\ell-1}$. If $v_\ell(d)$ already meets the stated bound there is nothing to show. Otherwise the event $\ell^{k_\ell}\mid t$ has probability $\ell^{-k_\ell}$ under Haar measure. At any zero outside this event, decompose the vanished sum into minimal zero subsums. By [Mann's theorem](https://doi.org/10.1112/S0025579300005210) the ratios of terms in any minimal subsum have squarefree orders with all prime factors at most $r$. Across the character classes, evaluating at such a $t$ leaves a factor $\ell^2$ in the order of the ratio when $\ell\le r$, or a factor $\ell$ when $\ell>r$. Hence each minimal subsum stays within one class and every class polynomial $F_I$ vanishes there.

Integrate $|F_I|^2$ against $\nu=\omega+(\nu-\omega)$. The Fourier bound gives at most $|I|^2/r$ from $\omega$. The other contribution is supported on zeros divisible by $\ell^{k_\ell}$ and is at most $2|I|^2/\ell^{k_\ell}$. Consequently $|I|\le |I|^2(1/r+2/\ell^{k_\ell})$, so every class has more than $r/2$ characters. There is just one class. Since the characters generate the dual of $L$, this proves the bound. In particular primes exceeding $2r$ do not divide $d$. Together with the exact sign lift, this reduces the remaining fixed-$r$ coset problem to a finite family of cyclic tests for each rank, with a cutoff independent of the field order.

In fact no prime larger than $r$ divides $d$ when $r\ge3$. If such a prime $\ell$ divides $d$, the preceding bound gives $v_\ell(d)=1$. Partition the characters by their $\ell$-primary part. Each class polynomial vanishes on the zeros with $\ell\nmid t$, again by Mann's theorem. The same integral bound with $2/\ell$ in place of $2/\ell^{k_\ell}$ forces each class to have more than $r/3$ characters, and there must be at least two classes since the characters generate. Write $I,J$ for the two classes. On the remaining zeros $F_J=-F_I$. With the cross Fourier coefficients saturated at $1/r$, orthogonality gives

$$\frac{|I||J|}{r}=-\int F_I\overline{F_J}\,d(\nu-\omega)\le\frac2\ell\min(|I|,|J|).$$

The last bound holds because on the subgroup $\ell\mid t$ the characters within each class are still distinct, so its normalized squared sum there equals the class size. Thus $\ell\max(|I|,|J|)\le2r$, impossible since $\ell>r$ and one of the classes has size at least two. The replay below uses the earlier, larger modulus so this sharpening is optional for its coverage.

## Finding a clique in the finite quotient for up to five phases

Write the quotient additively as $\mathbb Z/d\mathbb Z$ and its distinct characters as $\gamma_j(t)=\exp(2\pi i a_jt/d)$. We show that there is a subset $T$ of size at least $d/r$ with $F(t-t')\ne0$ throughout $T\times T$. Its inverse image in $B$ then has size at least $b/r\sim\sqrt p$. Distinct points of the inverse image have differences of Legendre sign $\sigma$, since $\chi(x-y)=s(x/y)$ for $x,y\in Q$. Scaling by a nonsquare for the negative sign turns this into a Paley clique. The [Hanson–Petridis inequality, Corollary 1.5](https://arxiv.org/pdf/1905.09134) bounds its size $h$ by $h(h-1)\le n$, giving a contradiction. In the mass-gap statement, uniform constants $c,\epsilon>0$ follow by contradiction, by choosing each at most $1/j$ along a hypothetical violating sequence with $p\to\infty$.

For $r=1$ take the whole quotient. For $r=2,3$, every vanishing sum of the $r$ unit vectors is a regular $r$-gon. In the cyclic image of any pairwise quotient of order $d'$, choose $\lceil d'/r\rceil$ consecutive residues and take their inverse image. Their phase differences have absolute argument less than $2\pi/r$, so cannot occur in a regular $r$-gon at two different vertices.

There is also a clique of size at least $d/r$ for any $r$ if all zero orders of $F$ are prime powers, in particular when $d$ is a prime power. If $F$ vanishes at a primitive $\ell^j$th root, the mask polynomial $\sum_i X^{a_i}$ is divisible by $\Phi_{\ell^j}(X)$. The product of these distinct monic factors divides the mask, so at $X=1$ the product of one factor $\ell$ per zero order divides $r$. For every such order, fix the base-$\ell$ digit at position $v_\ell(d)-j$. Differences of selected elements cannot have any of the forbidden orders. The Chinese remainder theorem gives density equal to the reciprocal of the product of the $\ell$ factors, at least $1/r$.

For $r=4$, any vanishing sum splits into opposite pairs. Indeed two unit vectors with a given nonzero sum are unique up to exchange, as the endpoints of the chord with that midpoint. Apply this to one pair and the negatives of the remaining pair. If the first pair is already opposite then so is the other. For any viable pairing, let $m_{ij}$ be the order of one paired quotient. The condition $\gamma_i(t)/\gamma_j(t)=-1$ imposes $t\equiv m_{ij}/2\pmod{m_{ij}}$, so $v_2(t)=v_2(m_{ij})-1$. Both pairs must give the same valuation. At most two distinct valuations can arise among the viable pairings. If all three pairings are viable, the three edges on vertices $1,2,3$ represent them. Their order valuations have maximum attained at least twice, because the corresponding exponent differences have minimum $2$-adic valuation attained at least twice. Now fix the binary digit of $t$ at each of the at most two forbidden valuations. Two such elements cannot have their first differing binary digit at one of the fixed positions. This gives $|T|\ge d/4$ by the Chinese remainder theorem, including all odd parts of $d$.

For $r=5$, a vanishing sum is either a regular pentagon or a pair of opposites together with an equilateral triple. For completeness, [Mann's theorem on irreducible relations](https://doi.org/10.1112/S0025579300005210) puts the ratios of terms of a minimal sum of length five in the group of $30$th roots. Write the sum as a polynomial in a primitive fifth root with coefficients in $\mathbb Q(\zeta_6)$. The fifth cyclotomic polynomial remains irreducible there, so all five coefficients are equal. If a factor of order five occurs in a ratio, more than one coefficient class is nonempty, and no nonempty class can sum to zero by minimality. All five classes are then singletons with equal coefficients, giving the pentagon. Without the factor five a rotation puts all terms among sixth roots. Writing them as signed third roots gives a vanishing pair or triangle, since the three net coefficients must be equal. A reducible sum of length five necessarily splits into a pair and a triple.

All pair-and-triple zeros have $v_2(t)$ equal to the same value $h$, if any exist. To see this, put $a=v_2(d)$ and $\ell=a-v_2(t)$. The three exponents of the triple coincide modulo $2^\ell$, while the other two are distinct siblings modulo $2^\ell$ with equal residue modulo $2^{\ell-1}$. The multiplicities at this level are $(4,1)$ or $(3,1,1)$. At every coarser level the multiplicities are $(5)$ or $(3,2)$, which cannot give a pair and triple. At any finer level the triple must still come from the only class of size at least three at level $\ell$, leaving two residues in different level-$\ell$ classes. Those two can no longer be siblings. This proves uniqueness of $h$.

If a pentagon zero exists, every pairwise quotient has the same nontrivial $5$-primary order $5^g$, since all these quotients at a pentagon have order five. The pentagon zeros require $v_5(t)=g-1$. If both types of zero occur, pentagon zeros also require $2^{h+1}\mid t$, since the original opposite pair had quotient with $2$-primary order $2^{h+1}$. Conversely the pair-and-triple zeros require $5^g\mid t$ because the quotient for an opposite pair must lose its $5$-part. Now let $T$ consist of residues whose base-five digit at position $g-1$ is their binary digit at position $h$, taking the latter as $0$ or $1$. This has density $1/5$. For two such residues with equal binary digits, their difference either has $5$-adic valuation below $g-1$ or is divisible by $5^g$, excluding a pentagon. Their equal binary digits also exclude the pair-and-triple valuation $h$. With different binary digits, the difference is divisible by neither $2^{h+1}$ nor $5^g$, so again neither zero is possible. If only pair-and-triple zeros occur, fix the one binary digit. If only pentagon zeros occur, fix the one base-five digit.

## Finite exclusion for six through eight phases

Use the Fourier bound on $\omega=g\nu$ and the fact that it equals $\nu$ off the zero set of $F$. For a unit $u$ modulo $d$, $F(ut)=0$ exactly where $F(t)=0$, since the polynomial has integer coefficients. Therefore $\int |F(ut)|^2d\omega=r$ for each unit. Expanding and saturating the $r^2$ bounds gives $\widehat\omega(u(a_i-a_j))=1/r$ for every $i,j,u$. Units act transitively on each set of characters of the same order. If $\mathcal D$ is the set of nontrivial orders of all pairwise differences, Parseval and $|g|\le1$ now give

$$1+\sum_{m\in\mathcal D}\varphi(m)\le r^2.$$

The trivial coefficient also gives $\int g\,d\nu=1/r$. If $Z$ is the number of zero phases, then $1/r\ge1-2Z/d$, so $2rZ\ge(r-1)d$. Both conditions are necessary for a feasible-mass limit.

The [certificate replay](../coset_phase_certificate.py) enumerates the first condition in the cyclic group of order $D_r=\prod_{\ell\le2r}\ell^{k_\ell-\mathbf1_{\ell>r}}$. All possible $d$ divide $D_r$, and the character exponent set embeds in this common cyclic group without changing any difference order. Translate a pair whose difference has maximum numerical order $m$ and multiply by a unit to send it to $0,D_r/m$. Any other exponent representative is larger than $D_r/m$ because the gcd of each exponent with $D_r$ is at least $D_r/m$. A search over increasing representatives is therefore exhaustive up to these normalizations. On each step the search adds the totients for newly seen difference orders and prunes as soon as the cost would exceed $r^2-1$. At a leaf the common gcd with $D_r$ gives the actual generated quotient and its mask.

The replay computes $Z$ by exact integer division by cyclotomic polynomials. For each distinct pair of generated quotient size and surviving zero set it finds a clique in the allowed-difference graph. Every profile below passes the stronger size test $\lceil d/r\rceil$. Consequently its preimage in $B$ contradicts Hanson–Petridis by the same argument as for up to five phases. All operations in the replay are on integers. A separate, unpruned combination enumeration through generated order 16 reproduced the normalized candidate lists for ranks four, five and six exactly.

| Rank | Common modulus | Enumerated masks | Largest generated order | Masks passing the zero-count test | Surviving profiles |
|---:|---:|---:|---:|---:|---:|
| 6 | 831,600 | 304,012 | 120 | 220 | 50 |
| 7 | 75,675,600 | 11,387,395 | 150 | 41 | 6 |
| 8 | 151,351,200 | 372,861,975 | 240 | 7,290 | 174 |

### Exponent reflection for stationary spectra

Both stationary probabilities are even, by the uniqueness of the positive log optimum and invariance of the one-mark weights under frequency inversion. If an even probability is close in $\ell_1$ to the uniform probability on $U$, then so are the two uniform probabilities on $U$ and $-U$ to each other. A union of $r$ distinct cosets that is different from its inverse has symmetric difference of at least two full cosets, so the distance is at least $2/r$. Hence any fixed-$r$ limiting obstruction for the stationary spectra has $U=-U$ eventually. Translating and rescaling the exponent mask for the certificate preserves reflection symmetry about some center, expressed as $A=c-A$. The argument applies to all even feasible probabilities.

The replay with `--symmetric --small-primes-only` uses the sharper bound on phase primes and exhausts only such masks. In the common cyclic group, the normalized mask contains $0,f$ with $f=D_r/m$ as before. A reflection $x\mapsto c-x$ must send $0$ to a member $c$ and $f$ to a member $c-f$. For each admissible $c$, the union of their two orbits forms the starting set. The remaining points are chosen as complete orbits of one or two points. Every pair order and every totient cost is checked at the step where the orbit is added. This covers every centrally symmetric normalized mask, with a repeated mask counted once for each admissible center. All the surviving profiles below also pass the stronger clique size test $\lceil d/r\rceil$.

| Rank | Common modulus | Enumerated masks with centers | Largest generated order | Masks passing the zero-count test | Surviving profiles |
|---:|---:|---:|---:|---:|---:|
| 8 | 1,058,400 | 292,671 | 210 | 1,718 | 130 |
| 9 | 1,058,400 | 622,368 | 420 | 253 | 32 |
| 10 | 1,058,400 | 17,037,524 | 504 | 4,104 | 131 |
| 11 | 128,066,400 | 45,643,533 | 840 | 379 | 38 |

The distinct masks from the reflection-orbit enumeration were also compared with direct filtering of the original enumeration at ranks two through six, using the larger modulus. The sets agreed exactly at each rank. An independent unpruned enumeration through generated order 16 reproduced all 637 and 451 normalized masks in that range at ranks eight and nine respectively.

### A necessary row constraint at any fixed rank

The signed density $g$ can be averaged over multiplication by units of $\mathbb Z/d\mathbb Z$. This preserves its values on the nonzero phases of $F$, the bound $|\widehat g|\le 1/r$, and the saturated coefficients. In particular the averaged Fourier coefficient depends only on order. Since $gF=F$, its convolution with $\mathbf1_A$ vanishes at every $b\notin A$. Let $\mathcal D_+$ be the orders in the saturated difference classes, including the trivial order. At most $r/2$ of the orders of $b-a$ for $a\in A$ can belong to $\mathcal D_+$, counting their multiplicities. Otherwise their positive coefficients cannot be canceled by all the remaining entries of magnitude at most $1/r$. At equality all the remaining orders must have coefficient $-1/r$. Their totients count toward the same total Parseval budget $r^2$. This gives more exact rejection tests for larger ranks. The replays listed above only use the positive-group budget and the phase zero count.

## Compression gaps for growing quotient orders

The finite-phase conclusion can also be obtained from the compression alone. Suppose $r$ is bounded, $|U|\le(1+o(1))m_0$, and $\|K_{UU}\|\to1$, through prime or square orders with the same Jacobi entry bound. Then the order of the subgroup of $\widehat Q/G$ generated by the coset differences stays bounded. Equivalently, a coset displacement of order tending to infinity modulo $G$ forces a uniform compression gap along such a sequence.

Use the [positional block decomposition](signed-coset-bands.md#a-union-of-frequency-cosets) on a coset $x_0B$ carrying an endpoint eigenvalue of the compression. The corresponding normalized coefficients $(\beta_j)$ give a polynomial $F_\beta=\sum_j\beta_j\gamma_j$ on $B$, after absorbing the phases from $x_0$ in the coefficients. Its sign-weighted Rayleigh quotient tends to one after choosing $\sigma$. The upper bound is $(\sqrt q/b)(\sum_j|\beta_j|)^2\le r\sqrt q/b=|U|/m_0$, so $|U|\sim m_0$ and $|\beta_j|\to r^{-1/2}$ by equality in Cauchy–Schwarz. Pass to a convergent subsequence of the coefficients. The preceding measure argument applies with the weight $\sigma s(x_0x)$, the same character-sum bound for this positional coset, and the limiting polynomial $F_\beta$. Its Rayleigh equality supplies $\int |F_\beta|^2d(\nu-\omega)=0$.

Partition the characters into classes on $L^0$ as above. Each restricted class polynomial still vanishes on the support of $\nu-\omega$ up to a set of zero measure, and orthogonality and the Fourier bound give

$$\sum_{j\in I}|\beta_j|^2\le\frac{1}{r}\Big(\sum_{j\in I}|\beta_j|\Big)^2\le\frac{|I|}{r}\sum_{j\in I}|\beta_j|^2.$$

Every class is nonzero, so $L$ is again finite and equals the phase groups on the subsequence eventually. If the orders of the groups generated by the displacements were unbounded, a subsequence of orders tending to infinity would contradict this conclusion. Via duality the bounded phase order means all the cosets in $U$ lie in a single coset of a supergroup of $G$ of bounded relative index. At some phase with $F_\beta\ne0$, the relevant positional coset is asymptotically of one sign in density. The compression argument gives this weighted average condition, while the mass argument above gives an exact sign on the nonzero fibers.

The gap persists after adding $o(m_0)$ arbitrary indices to the cover, by the entrywise bound and a Frobenius-norm comparison. The [spectral leakage bound](coset-progression-gap.md#mass-outside-the-structured-set-for-an-actual-slow-mode) then forces a positive fraction of the squared norm of any sufficiently slow unit direction outside the enlarged cover. This applies to the direction independently of how much stationary mass lies outside.

## Consequences for stationary high sets

At a fixed threshold $0\le\rho<1$, let $S_\sigma=\{i:\sigma D_i>\rho\}$ for the actual stationary diagonal. As in the [earlier stationary transfer](parallel-stationary.md#transfer-to-the-actual-stationary-diagonal), the stationary reciprocal identity gives

$$\mu_\sigma(S_\sigma\setminus U)\ge\epsilon-\sqrt{\frac{\tau(1+\rho)}{W(1-\rho)}}-O(n^{-1/2}).$$

For all sufficiently small positive $\tau$ depending on $\rho$, the eleven-coset exclusion forces $\Omega(m_0)$ same-sign high coordinates outside any tested union. If $|S_\sigma|\le(1+o(1))m_0$, the [stationary quadratic form](signed-coset-bands.md#a-stationary-mass-test-without-an-eigenvalue-hypothesis) gives $|S_\sigma|\sim m_0$ and a signed compression gap of at most $O_\rho(1/m_0)$. The [translation rounding argument](signed-coset-bands.md#turning-overlap-into-a-coset-cover-at-the-required-precision) then gives $E(S_\sigma)/|S_\sigma|^3\le a+(1-a)|G|/|S_\sigma|$ for any fixed $a>1/2$, using the subgroup of shifts with overlap ratio greater than $a$. If the energy ratio stayed above $13/24+\delta$, taking $a$ close enough to $1/2$ forces $|G|/|S_\sigma|>1/12$ by a fixed amount. Rounding would yield at most eleven cosets of total size $(1+o(1))m_0$ with only $o(m_0)$ high coordinates outside, a contradiction. Thus the energy ratio is at most $13/24+o(1)$. The size asymptotic is the same as for the earlier $6/11+o(1)$, $9/16+o(1)$, $7/12+o(1)$, and $5/8+o(1)$ bounds.

At square orders $q=r_0^2$ the uniform measure on the subfield annihilator has full mass on $|U|=(r_0+1)/2\sim m_0$. In this case the phase quotient can be trivial, and the lifted clique has size $r_0-1\sim\sqrt q$. The finite-phase part is compatible with the square witness. It is the prime-field clique bound that turns the lifted exact sign into an exclusion. For the marked response the remaining case includes larger or less structured high sets, and the new exterior mass estimate does not control their spectral coupling.

## Exact quotient checks

The [cyclic check](../coset_phase_check.py) computes the zero set by integer divisibility of the mask polynomial by cyclotomic polynomials. It then searches the allowed-difference graph for a clique of size $\lceil d/r\rceil$. An exhaustive run through $d=38$, enumerating exponent sets containing zero, found such a clique in all 73,815 four-character and 501,942 five-character masks. Of these, 16,451 and 10,077 masks respectively have some zeros. A separate arithmetic check verified the digit construction on all four-character masks at $d=16$ and all five-character masks at $d=30,60$, together with 16,000 sampled masks at $d=120$. At $d=30$ it includes 60 masks with both types of zero, such as $\{0,1,2,4,28\}$ with zero orders five and six. A further sample of 29,568 masks with six through twelve characters on eleven orders between 30 and 360 found no exception to the same finite clique size. This sample leaves the general cyclic difference problem open.

## Matched prime and square comparisons

For each row of the first table, take $U$ as $r$ frequency cosets, each of size $n/b$. Compute its compression from [the positional blocks](../coset_bands.py). The bounded-order displacements are $0,b/r,\ldots,(r-1)b/r$ in the cyclic quotient of order $b$. The large-order displacements are $0,1,\ldots,r-1$. In each square case the bounded-order union is the actual subfield annihilator and its norm is exactly $1-1/(\sqrt q-1)$. The subfield coset has sign sum $\sqrt q-2$. Every other positional coset in $Q$ has sum $-2$, by the quadratic character sum of the irreducible norm polynomial $N(1-at)$ over the subfield and subtraction of the $t=0$ term. The prime pairs have the same frequency subgroup sizes and comparable total size. The other norms are computed in floating point. Eight small-order comparisons with the direct dense compression agreed to $8.3\times10^{-16}$.

| Order | $r$ | $b$ | $\# U/m_0$ | Bounded-order norm | Large-order norm |
|---:|---:|---:|---:|---:|---:|
| $47^2$ | 2 | 92 | 1.02174 | 0.97826 | 0.47826 |
| $2161$ | 2 | 90 | 1.03304 | 0.20000 | 0.23089 |
| $47^2$ | 3 | 138 | 1.02174 | 0.97826 | 0.36451 |
| $2161$ | 3 | 135 | 1.03304 | 0.20000 | 0.32440 |
| $191^2$ | 2 | 380 | 1.00526 | 0.99474 | 0.49474 |
| $37057$ | 2 | 386 | 0.99742 | 0.18135 | 0.17043 |
| $191^2$ | 3 | 570 | 1.00526 | 0.99474 | 0.35839 |
| $37057$ | 3 | 579 | 0.99742 | 0.18135 | 0.19994 |
| $383^2$ | 2 | 764 | 1.00262 | 0.99738 | 0.49738 |
| $147457$ | 2 | 768 | 1.00000 | 0.18229 | 0.13629 |
| $383^2$ | 3 | 1146 | 1.00262 | 0.99738 | 0.35975 |
| $147457$ | 3 | 1152 | 1.00000 | 0.18229 | 0.12190 |

For the second comparison, solve the actual stationary equations at $\tau=0.01$ using [the weighted FFT solver](../poisson_weights.py). Normalize each positive spectrum to a probability. For each divisor $g$ of $n$ with $g\le1.1m_0$, sum the probability in each frequency coset by reducing the frequency index modulo $n/g$. Sum the largest $\min(5,n/g,\lfloor1.1m_0/g\rfloor)$ coset masses, and take the maximum over $g$. This compares all eligible unions for the measured stationary probability. The size cap $1.1m_0$ here fixes the finite experiment, while the proved asymptotic slack $c$ is unspecified. The residuals in these runs were below $10^{-9}$.

| Order | Max plus mass | Max minus mass |
|---:|---:|---:|
| $97^2$ | 0.98087 | 0.03195 |
| $9413$ | 0.03440 | 0.03277 |
| $193^2$ | 0.98059 | 0.01528 |
| $37253$ | 0.01007 | 0.01190 |
| $389^2$ | 0.98037 | 0.00695 |
| $153649$ | 0.00718 | 0.00702 |
