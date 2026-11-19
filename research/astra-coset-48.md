# Parity and ten-coset restrictions on an order-five witness

Let $p\equiv1\pmod4$ be prime, $n=(p-1)/2$, $Q=\mathbb F_p^{\times2}$, $B\le Q$ of order $b$, and $a\in Q$ of order five modulo $B$. Put $C=\langle a,B\rangle$ and $C_j=a^jB$, indexed modulo five. Suppose $s(x)=\chi(1-x)=\sigma\in\{1,-1\}$ on $B\setminus\{1\},C_1,C_4$. Write $h_p=\lfloor(1+\sqrt{1+4n})/2\rfloor$. The [quotient lift](astra-secant-47.md) gives a feasible ordinary-theta mark $b\sqrt{5/n}$. To obstruct its strict asymptotic excess one needs $b/\sqrt n\le 1/\sqrt5+o(1)$.

## An even-order exclusion

If $b>2$ is even, then $\sigma=+1$ and $C^2$ is a Paley clique of size $5b/2$. In particular $b\le 2h_p/5$. Indeed, $-1\in B$, and $s(x^2)=s(x)s(-x)$ at every $x$. Taking $x\in B\setminus\{1,-1\}$ forces $\sigma=+1$. Taking $x\in C_{\pm1}$ forces the plus sign on the squares of both adjacent fibers. The five fibers of $C^2$ over $C/B$ consist of these two images over $\pm2$ and three fibers where the sign is already known. Thus $s=+1$ throughout $C^2\setminus\{1\}$. Each difference of unequal $x,y\in C^2$ is a square since $y\in Q$ and $\chi(-1)=1$. The prime clique bound gives the assertion. The exception $b=2$ can have $\sigma=-1$. [Hanson–Petridis, Theorem 1.2](https://arxiv.org/abs/1905.09134)

## Odd order and the signed compression on ten fibers

For odd $b$, let $t=\sigma b^{-1}\sum_{u\in C_2}s(u)\in[-1,1]$. Inversion preserves $s$ on $Q$, so $C_3$ has the same mean. Define $k=(3+\sqrt5)/2$, $c_5=10k/(6+k)$. Then

\[
 b\max\{|3+2t|+|1+4t|,\ k(1-t)\}\le\sqrt p+3,
 \qquad b\le(\sqrt p+3)/c_5. \tag{1}
\]

In particular $\limsup b/\sqrt n\le\sqrt2/c_5<0.466$ on these patterns. The previous $2b$ clique gave $1/2$. At the witness threshold $b\ge\sqrt{n/5}$, (1) requires

\[
 1-\sqrt{10}/k-o(1)\le t\le(\sqrt{10}-4)/6+o(1).
 \tag{2}
\]

The endpoints are about $-0.20788$ and $-0.13962$. Thus a critical witness requires approximately 39.6 to 43.1 percent of the points on either diagonal fiber to have the allowed sign. A fixed excess in the normalized mark tightens both inequalities.

To prove (1), the ten fibers $C_j,-C_j$ are distinct since $C$ has odd order. All their elements lie in $Q$. Compress the real symmetric matrix $T_{xy}=\chi(x-y)$ on the additive field to their ten unit indicators. The quadratic character correlation identity gives $T^2=pI-J$ with $J$ the all-ones matrix, so the compression has norm at most $\sqrt p$. Within each five-fiber half its entries form a circulant matrix with row $(\sigma(b-1),\sigma b,\sigma bt,\sigma bt,\sigma b)$. In the opposite half of each row the entries are sums of $\chi(1+x)$. For $x\ne1$ in $C$ one has $\chi(1+x)=s(x^2)s(x)$. Squaring maps each $C_j$ bijectively to $C_{2j}$ since $b$ is odd. For $j=0$ this gives $b-1+\chi(2)$, and for the other four $j$ one of $j,2j$ is an adjacent fiber while the other is diagonal. Each cross-half off-diagonal entry is $bt$. No pointwise constancy on a diagonal fiber is needed.

Replacing the two diagonal corrections by zero changes the operator norm by at most $1+|1-\chi(2)|\le3$. The corrected matrix has diagonal blocks $\sigma b A$ and off-diagonal blocks $bD$, where $A,D$ are circulants with rows $(1,1,t,t,1)$ and $(1,t,t,t,t)$. On the constant fifth mode the larger absolute eigenvalue over the two parities is $b(|3+2t|+|1+4t|)$. On the first nonconstant mode it is $bk(1-t)$, using $1+2\cos(2\pi/5)=(1+\sqrt5)/2$. The second nonconstant mode gives a smaller bound. Since $|3+2t|+|1+4t|\ge4+6t$, the maximum in (1) is at least $c_5$ by intersecting the increasing affine function $4+6t$ with $k(1-t)$. At the intersection $t_*=(k-4)/(k+6)>-1/4$ equality holds, so the uncorrected compression norm with a free diagonal mean cannot improve $c_5$. This freely chosen mean is a limitation of the test and does not assert existence at primes.

## Odd orders with prescribed factors

For any odd prime $r\mid b$ with $r\equiv\pm2\pmod5$, let $W=C_2\cap C^r$, of size $b/r$. Every element of $W$ has sign $\sigma$, since it is the $r$th power of an element of an adjacent fiber, and all its $r$ roots are in that fiber. The identity $1-x^r=\prod_{\xi\in\mu_r}(1-\xi x)$ proves this. On the entire diagonal fiber each $\mu_r$ orbit has product of signed signs $\prod_{\xi}\sigma s(\xi u)=1$ because $u^r$ lies on an adjacent fiber. Since $r$ is odd there is at least one matching sign in every orbit. If $r^2\mid b$ then $\mu_r\subset B^r$, and $W$ is a union of whole orbits. This gives

\[
 \frac{1+t}{2}\ge\frac1r+\frac{1-1/r}{r}.
\]

In particular, $9\mid b$ implies $t\ge1/9$, and (1) gives $b\le3(\sqrt p+3)/14$. This excludes a supercritical order-five witness on this class. If several distinct primes $r$ as above divide $b$, the positive sets $C_2\cap C^r$ together have relative size $1-\prod_r(1-1/r)$ by cyclicity and the Chinese remainder theorem (in an exponent coordinate each is one residue class modulo $r$). For instance $3\cdot7\cdot13\mid b$ gives positive density at least $43/91$, hence $t\ge-5/91$, also contradicting (2). The unsigned count with $3\parallel b$ alone only gives density at least $1/3$.

In fact every odd $b$ divisible by three is excluded using a character on the full set $C$. Take a character $\tau$ of order three on $C$, with kernel $C^3$. On each diagonal fiber $C_j$ the matching third $C_j\cap C^3$ has real character value one, and the rest has real character value $-1/2$. It follows that
\[
 \sum_{x\in C_j}\sigma s(x)\operatorname{Re}\tau(x)=b(1-t)/2\qquad(j=2,3).
\]
Compress $T$ to the two unit vectors proportional to $\tau$ on $C,-C$, identifying each $x$ with $-x$ in the second copy. The two identical diagonal entries are the sums of $s(x)\tau(x)$ on $C$, by substituting the ratio of two elements in the quadratic form. They are real by inversion and equal $\sigma[b(1-t)-1]$, since $\tau$ is nontrivial on $B$ and the value at 1 was removed. The cross entry is real for the same reason, and equals the sum of $\chi(1+x)\tau(x)$. Its central fiber gives $\chi(2)-1$. Each of the other four fibers gives real part $b(1-t)/2$ using $\chi(1+x)=s(x)s(x^2)$, the bijections by squaring, and $\operatorname{Re}\tau(x^2)=\operatorname{Re}\tau(x)$. Thus the larger absolute eigenvalue bounds $3b(1-t)-3$ from above. Consequently
\[
 b\max(4+6t,3(1-t))\le\sqrt p+3,\qquad b\le 3(\sqrt p+3)/10.
\]
This gives asymptotic ceiling $3\sqrt2/10<1/\sqrt5$ for $3\mid b$. The cubic density argument still strengthens this ceiling when $9\mid b$.

## Finite controls and remaining tests

The [checker](astra-coset-48-check.py) exhausts primes through $200000$ and both order-five inverse pairs for each possible $b\ge2$ after the necessary $2b\le h_p$ sieve. For each pattern it verifies all five coset sums, and either the ten-fiber entries or the even-order clique. Exact integer arithmetic found 0 patterns among the 932 choices with $5b^2>n$. Among all choices there were 1272 even and 270 odd patterns. For $(p,b)=(12781,9)$ an actual pattern has $t=1/9$, attaining the cubic density bound. The numerical constants in (1) and (2) have separate Arb 192-bit enclosures. No floating-point optimization enters the argument or sweep. The [records](astra-coset-48-checks.jsonl) replay using `.venv/bin/python -B research/astra-coset-48-check.py`.

1. On the remaining odd orders first target a uniform prime restriction on the signed diagonal mean, including the rough orders with no small prime factor. To exclude every fixed witness excess by this route, it suffices to exclude every compact subinterval in the interior of (2) when $5b^2\ge(1+\delta)n$ for fixed $\delta>0$. A family of actual primes and cosets in this range disproves the theta limit by the quotient lift. The scalar compression itself allows the interior value $t_*$, so testing more precise numerical eigenvalues of the same ten-block model does not close the gap.
2. For unrestricted theta, return to the signed one-endpoint late secant on exact optima in [round 47](astra-secant-47.md). Seek one comparable late interval on each large prime with the excess secant divided by its length $o(1)$ or negative. A positive liminf of the minimum normalized excess over all intervals in the prescribed window, through an unbounded prime subsequence, falsifies that choice of window. The subgroup argument leaves this question open even if all five-cycles are excluded.
