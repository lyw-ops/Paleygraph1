# Audit of Fable's Problem 26 response

[Fable 5.2](https://claude.ai/chat/60001a8c-ef24-46e7-b6f7-1e21a326cf5a) independently tested the cross-floor moment identity and the prime and square theta LPs. It reported no proof or counterexample to the ETH conjecture. The positive square equality and the two-floor identity agree with the existing derivations. Its claim about the full square saturation set fails on two small exact examples.

## A strict finite-prime inequality

Use $Q$ for the squares, $s(x)=\chi(1-x)$, $n=|Q|$, and $M=\max_{h\ne0}\sum_{x\in Q}h(x)s(x)$. For the minus sector put $C_-=\{x\in Q:s(x)=-1\}$. The row

$$ f=\delta_1+\frac{2}{1+M}\mathbf1_{C_-} $$

has nonnegative Fourier spectrum. Indeed the nontrivial coefficient of $\mathbf1_{C_-}$ is $-(1+\widehat s(h))/2$, by the support indicator on $Q\setminus\{1\}$. The coefficient at the mark is $1+n/(1+M)$ since $|C_-|=n/2$. Reciprocity yields

$$ \theta_+\le \frac{n(1+M)}{n+1+M}\le\sqrt q-1. $$

For a nontrivial $h$ on $Q$, the [Jacobi formula](fourier.md#joint-distribution-on-the-even-modes) identifies $\widehat s(h)$ with the real part of $J(\psi,\chi)$ for a lift $\psi$, with absolute Jacobi value $\sqrt q$. If $q=p$ is prime, equality at $\widehat s(h)=\sqrt p$ forces $J(\psi,\chi)=\sqrt p$. The Jacobi sum lies in $\mathbb Q(\zeta_{p-1})$, and the quadratic Gauss sum puts $\sqrt p$ in $\mathbb Q(\zeta_p)$. The two cyclotomic fields have trivial intersection by multiplicativity of the cyclotomic degree at the relatively prime conductors. Thus $M<\sqrt p$ and $\theta_+<\sqrt p-1$ at every prime. This gives strictness at each order without a uniform saving in the limit.

## Corrections and scope

- Over $q=r^2$ every nontrivial member of the subfield annihilator has $\widehat s(h)=r$. The converse stated by Fable is false. Exact reduction modulo the cyclotomic polynomial gives the additional frequency indices $4,20$ when $r=7$ and $6,18,42,54$ when $r=11$, in the generator convention of [the square sign generator](../square_control.py). These counts were independently replayed from [the affine-rank note](parallel-low-energy-7.md#square-control-and-exact-arithmetic-checks). Neither extra set changes the exact square theta value.
- The two-floor equation gives an upper bound on the product of exponential moments, so the proposed **asymptotic lower bound** reaching it would prove vanishing of the marked change. It is a saturation target with the same asymptotic difficulty. The equivalence and its square obstruction are already derived in [the two-floor note](parallel-floor-8.md#one-pair-an-exact-deficit-for-two-sampled-coordinates).
- A near-maximal theta value alone does not establish a support of size $O(\sqrt n)$ for the Fourier spectrum. The [compression argument](additive-neighbor-compression.md#any-feasible-probability-with-a-large-squared-norm) yields such a test conditional on mass concentration. The diffuse case still needs an estimate.
- There are 222 primes congruent to one modulo four below 3200, including $5$. The reported 221-case sweep may have omitted $5$. Its individual solver outputs were not independently replayed in this audit.
