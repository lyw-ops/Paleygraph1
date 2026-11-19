# Quartic tests and the full ten-fiber compression

Use the order-five pattern of [round 48](astra-coset-48.md). Thus $b$ is odd, $C/B$ has order five, $C_j=a^jB$, $s(x)=\chi(1-x)$, and $s=\sigma$ on $B\setminus\{1\},C_1,C_4$. Define $q=(p-1)/4$, $\epsilon=(-1)^q$, $[u]_4=u^q\pmod p$, and $m=|\{x\in C_2:s(x)=-\sigma\}|$. The new prime tests are
\[
 [r]_4=(\epsilon\sigma)^{(r-1)/2}\quad(r\mid b),\qquad
 [5]_4=(-1)^m.                                                   \tag{1}
\]
In particular every divisor $r\equiv1\pmod4$ of $b$ must be quartic modulo $p$. If $[5]_4=-1$, every prime factor of $b$ is $\pm1\pmod5$. These tests apply at arbitrary subgroup orders. For instance $(p,b)=(15581,41)$ lies strictly inside the interval $1/\sqrt5<b/\sqrt n<0.46553$ and fails the quartic test for 41 regardless of $\sigma$. At $(20681,47)$ in the same interval the divisor test permits $\sigma=-1$, but $[5]_4=-1$ excludes the factor $47\equiv2\pmod5$. Both exclusions precede constructing the subgroup or inspecting its signs.

For any odd $r\mid |C|$ choose one representative from each inverse pair in $\mu_r\setminus\{1\}$, in a set $U$. Pairing factors in $r=\prod_{x\in\mu_r\setminus\{1\}}(1-x)$ gives $r=(-1)^{(r-1)/2}(\prod_{x\in U}x^{-1})(\prod_{x\in U}(1-x))^2$. Every element of $C$ is a fourth power, by odd order, so $[r]_4=\epsilon^{(r-1)/2}\prod_{x\in U}s(x)$. This proves the first test. For $r=5b$ take the representatives from $B$ together with all of $C_1$ and $C_2$. Dividing by the formula for $r=b$ leaves precisely $(-1)^m$, since the half-size difference is $2b$.

When $5\nmid b$ write $C=\mu_5\times B$ and choose $\lambda\in\mu_5\cap C_1$. For every $v\in B\setminus\{1\}$, the five factors $s(\lambda^j v)$ have product $s(v^5)=\sigma$. The three central and adjacent factors equal $\sigma$, so
\[
 d(v):=\sigma s(\lambda^2v)=\sigma s(\lambda^{-2}v)=d(v^{-1}).
\]
At $v=1$ inversion gives the identity directly. Thus $[5]_4=d(1)$ by (1) and inverse pairing. If $r\mid b$ is a prime congruent to $\pm2\pmod5$, take the product of $s(\xi\lambda)$ over $\xi\in\mu_r\subset B$. This gives $s(\lambda^r)=\sigma^r=\sigma$, hence $d(1)=+1$. If $5\mid b$, (1) at $r=5$ already gives $[5]_4=+1$. This proves the restriction on the prime divisors of $b$.

## A limitation of enlarging the compression to individual points

For $5\nmid b$, all $10b$ points in $C\cup(-C)$ give a group convolution matrix for the additive Paley kernel restricted to these points: $\chi(x-y)=s(x/y)$ since $y$ and $-1$ are squares. In the coordinates $(\pm, j,v)\in\{\pm1\}\times\mathbb Z/5\times B$, the five positive-half kernel rows, as functions of $v$, are
\[
 \sigma(1,1,d(v),d(v),1),
\]
with the center value at $v=1$ changed to zero. The negative-half rows are
\[
 (1,d(v^2),d(v),d(v),d(v^2)),
\]
with the center value at $v=1$ changed to $\chi(2)$. This follows from $s(-x)=s(x)s(x^2)$ for $x\ne1$. In particular Fourier testing every one of the $10b$ characters adds at most a constant times the maximum of the nontrivial Fourier coefficients of $d$ on $B$, plus three, on the new modes. Here the Fourier transform is unnormalized and squaring permutes these characters. The modes trivial on $B$ are exactly those in round 48.

There are abstract sign kernels of precisely this form with full norm $c_5 b+O(\sqrt{b\log b})$, where $c_5$ is the sharp scalar constant of round 48. For any odd $b$ coprime to five, set $d(1)$ to either prescribed sign, and choose independent random signs of mean $t_*=(k-4)/(k+6)$ on the other inverse pairs, $k=(3+\sqrt5)/2$. Each Fourier coefficient is a sum of independent real variables with coefficients bounded by two, because each pair contributes twice a real character value. Hoeffding's inequality and a union bound give a choice with all nontrivial coefficients $O(\sqrt{b\log b})$ and the trivial coefficient $bt_*+O(\sqrt{b\log b})$. The exact correction at the two center entries costs at most three in norm. The trivial-on-$B$ spectrum then gives the claimed asymptotic norm and the remaining spectrum is $o(b)$. This works even with $d(1)$ fixed to impose the mismatch parity in (1). In particular along prime orders $b>5$ the full principal norm, the paired diagonal signs and the square identity alone still permit $1/\sqrt5<b/\sqrt n<\sqrt2/c_5$ in an abstract model. These matrices have no asserted embedding in a prime Paley field. We did not obtain extra zero multiplicities from the equality of diagonal signs in the Hanson–Petridis auxiliary polynomial: the translated factors differ when differentiated. The project's earlier [shifted-prime divisor bound](coset-progression-gap.md) already covers the density-one consequence of $b\asymp\sqrt p$.

The [integer checker](astra-odd-49-check.py) verifies (1) on all 270 odd patterns with $b\ge3$ through the previous cutoff 200000, including 249 pointwise reflection checks for $5\nmid b$, and supplies the quartic exclusion above. Replay with `.venv/bin/python -B research/astra-odd-49-check.py`. The [record](astra-odd-49-checks.jsonl) concerns finite identities. No supercritical prime family or all-primes exclusion is known here.

1. On the remaining prime divisors, exploit the exact equality of the two diagonal signs via their ratio $(1-\lambda^2v)/(1-\lambda^{-2}v)$. First seek an individual-prime cancellation bound strictly below $b$ for the sum of its quadratic character on $B$, uniformly when $5\nmid b$ and $5b^2\ge(1+\delta)n$. Here the denominator is always nonzero. An unbounded sequence with that character identically one on $B$ refutes this proposed strict bound, even without the other signs. The $5\mid b$ branch requires separate input.
2. For the full ten-fiber eigenvectors attaining the scalar bound, estimate the squared norm of their additive Paley image on the exterior. A certificate with interior Rayleigh value $\Lambda$ and exterior squared norm greater than $p-\Lambda^2$ for a unit eigenvector rules out that hypothesis by $T^2=pI-J$. An actual supercritical family with compatible exterior masses defeats a universal exclusion by this mechanism. The abstract kernels above rule out relying solely on more interior twists.
