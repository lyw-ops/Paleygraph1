# Fourier optimization and a limitation on two character weights

Let $Q=\mathbb F_p^{\times 2}$ and write $n=|Q|$, $s(x)=\chi(1-x)$ on $Q$, with $\chi(0)=0$. Write $D_\sigma=\{x\in Q:s(x)=\sigma\}$, for $\sigma\in\{+1,-1\}$. The two graph sides are $\theta_+=\vartheta(\overline H)$ and $\theta_-=\vartheta(H)$.

Use the unnormalized transform $\widehat f(k)=\sum_{x\in Q} f(x)\eta_k(x)$, where $\eta_k(g^{2j})=\exp(2\pi i k j/n)$ for a primitive root $g$ modulo $p$. For real inversion-even functions the transform equals the cosine transform. Averaging a feasible theta SDP matrix over multiplication by $Q$ produces a matrix $X_{a,b}=f(b/a)/n$. The trace and zero conditions become $f(1)=1$ and $\operatorname{supp}(f)\subseteq\{1\}\cup D_\sigma$. Positive semidefiniteness is exactly $\widehat f(k)\ge0$ for every $k$, and the objective is $\widehat f(0)$. This is the ordinary theta LP of [Magsino–Mixon–Parshall, Proposition 2](https://arxiv.org/html/1907.05971). The graph is vertex-transitive, so [Lovász's product identity](https://arxiv.org/html/2610.22971v1#S3.E9) gives $\theta_+\theta_-=n$. A lower certificate for each side therefore gives an interval for both sides.

## Opposite-point correction

**Claim.** For either sign, restrict the LP to

$$f_{a,b}=\delta_1+p^{-1/2}1_{D_\sigma}(a+b\chi(1+x)),\qquad a,b\in\mathbb R.$$

The maximum in this family divided by $\sqrt n$ tends to $1/\sqrt2$ through primes $p\equiv 1\pmod4$. The coefficients may depend arbitrarily on $p$. This rules out reaching the conjectured constant with this two-parameter family.

### Fourier formulas

Write $\lambda_k=\widehat s(k)$ and $c=s(-1)$. Both $s(x)$ and $s(-x)$ are inversion-even on $Q$. We have $s(x²)=s(x)s(-x)$, since $1-x²=(1-x)(1+x)$. Thus

$$2,1_{D_\sigma}=1+\sigma s-\delta_1,\qquad 2,1_{D_\sigma}s(-x)=s(-x)+\sigma s(x²)-c\delta_1.$$

For $k=2\ell\ne 0$ in $\mathbb Z/n\mathbb Z$, the transform of $s(-x)$ is $\lambda_k$. The transform of $s(x²)$ is $\lambda_\ell+\lambda_{\ell+n/2}$. Indeed, $x\mapsto x²$ is two-to-one onto the subgroup on which $1+\eta_{n/2}=2$, and $\eta_{2\ell}(x)=\eta_\ell(x²)$. At such $k$,

$$
2\widehat f_{a,b}(2\ell)=2+(\sigma a+b)\frac{\lambda_{2\ell}}{\sqrt p}
   +\sigma b\frac{\lambda_\ell+\lambda_{\ell+n/2}}{\sqrt p}
   -\frac{a+bc}{\sqrt p}.
$$

### Joint distribution on the even modes

Extend $\eta_\ell$ to a character $\psi$ on $\mathbb F_p^\times$. Let $\rho$ have order four, so $\rho^2=\chi$ and $\rho|_Q=\eta_{n/2}$. All characters take value zero at the field element zero. With the standard additive character, use $G$ for the Gauss sum and $G(\chi)=\sqrt p$. Away from the four characters $1,\rho,\chi,\rho\chi$, the Jacobi-sum identity gives

$$\lambda_\ell/\sqrt p=\tfrac12\left(G(\psi)/G(\psi\chi)+G(\psi\chi)/G(\psi)\right).$$

The same formula holds for $\lambda_{\ell+n/2}$ with $\psi\rho$ and for $\lambda_{2\ell}$ with $\psi^2$. The excluded characters account for all exceptions, including when $\psi^2\in\{1,\chi\}$. In particular all nonzero $k$ satisfy $|\lambda_k|\le\sqrt p$. At $k=0$, $J(1,\chi)=J(\chi,\chi)=-1$, so $\lambda_0=-1$. The second equality follows by using the bijection $x\mapsto x/(1-x)$ from $\mathbb F_p\setminus\{1\}$ to $\mathbb F_p\setminus\{-1\}$, and $\chi(-1)=1$.

Write $(A,B,C,D)$ for the Gauss sums at $(\psi,\psi\chi,\psi\rho,\psi\rho\chi)$ divided by $\sqrt p$. For a nonexceptional character $\alpha$, counting the solutions of $4x(1-x)=t$ shows $J(\alpha,\alpha)=\bar\alpha(4)J(\alpha,\chi)$. The Gauss/Jacobi relation yields $G(\alpha)G(\alpha\chi)=\bar\alpha(4)G(\alpha^2)G(\chi)$. Taking the quotient for $\alpha=\psi$ and $\alpha=\psi\rho$ gives

$$\frac{G(\psi^2)}{G(\psi^2\chi)}=\rho(4)^{-1}\frac{AB}{CD}.$$

[Katz, Theorem 9.5](https://web.math.princeton.edu/~nmk/Katz-GKM.pdf) gives convergence of $(A,B,C,D)$ to Haar measure on the four-torus as $\psi$ runs over the nonexceptional characters. The map $(A,B,C,D)\mapsto (AB/(CD), A/B, C/D)$ is onto the three-torus. Its exponent rows are linearly independent, so every nontrivial target character pulls back nontrivially. The factor $\rho(4)^{-1}=\chi(2)$ preserves Haar measure for either value (one can take subsequences of each sign). Taking real parts shows that the normalized triples $(\lambda_{2\ell},\lambda_{\ell},\lambda_{\ell+n/2})/\sqrt p$ have limiting law given by three independent arcsine variables. All eight cube corners have positive mass in every neighborhood. The individual Gauss/Jacobi computation also appears in [Kunisky, Section 5](https://arxiv.org/html/2303.16475#S5).

### Feasible parameters and objective

Fix $0<\epsilon<1/2$. For all sufficiently large $p$ there is a nonzero even mode within $\epsilon$ of each of the eight corners. For a given $(a,b)$ use the corner with signs opposite to the three coefficients in the display for $2\widehat f(2\ell)$ (choose either sign for a zero coefficient). Put $L=|\sigma a+b|+2|b|$. Feasibility implies $(1-\epsilon)L\le 2+(|a|+|b|)/\sqrt p$. Since $|a|+|b|\le L$, we have $L\le 2/(1-\epsilon-1/\sqrt p)$ on the entire feasible region. Letting $p$ tend to infinity and then $\epsilon$ to zero gives $\limsup L\le 2$ uniformly in the choice of $(a,b)$.

At the trivial mode, $|D_\sigma|=(n-1-\sigma)/2$, and $2\sum_{D_\sigma}s(-x)=\lambda_0+\sigma(\lambda_0+\lambda_{n/2})-c=O(\sqrt p)$. Hence $\widehat f_{a,b}(0)/\sqrt n=a/(2\sqrt2)+o(1)$ uniformly for bounded parameters. This proves the upper bound on the restricted family. For the lower bound take $b=0$ and $a=2\sqrt p/(\sqrt p+1)$, which is feasible by $|\lambda_k|\le\sqrt p$. Its normalized objective tends to $1/\sqrt2$.

The optimization in `witnesses.py` uses $1/\sqrt n$ in the basis. This is a change of parameter scaling, so it tests the same family. The doubling identity also shows that adding $s(x²)$ alone to this basis gives no new direction on either allowed support.

The [joint Legendre calculation](parallel-witness-6.md) extends this asymptotic obstruction to the family with an added triangle-weighted column. The triangle column can still strictly improve the optimal constant row at finite primes.
