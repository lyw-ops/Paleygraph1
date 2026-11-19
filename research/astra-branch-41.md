# A two-moment constraint on the actual real branch

Write $P_+,P_-$ for the positive mean-one stationary spectra, $n=(q-1)/2$, $c=1-1/n$, $W=1+ct$, and $m_q(t)=\log(\sqrt{W/n}P_{+,0})$. The [stationary reciprocity](marked-response.md) is $P_{+,i}P_{-,i}=t/W$ off the mark and $P_{+,0}P_{-,0}=n/W$. Let $E h=n^{-1}\sum_{i\ne0}h_i$, and let $k_i=\lambda_i/\sqrt q$ be the signed Jacobi real part. The [single-column trials](astra-scalar-40.md) $l_\sigma$ have mark $L_\sigma=1+(n-1-\sigma)/(\sqrt q+1)$ and bulk $r(1+\sigma k_i)$, with $r=\sqrt q/(\sqrt q+1)$. The bulk law of $k$ converges to the arcsine distribution in both field families. All limits here concern real positive floors.

## Reciprocal moments and their scalar bounds

Orthogonality gives $L_{-\sigma}P_{\sigma,0}/n+rE[(1-\sigma k)P_\sigma]=1$. Thus the following two moments are known *exactly* from the single physical mark:
$$
 E P_\sigma=1-P_{\sigma,0}/n,qquad
 \sigma E kP_\sigma=1-P_{\sigma,0}/n-(1-L_{-\sigma}P_{\sigma,0}/n)/r.             \tag{1}
$$
For arbitrary affine $f,g\ge0$ on $[-1,1]$, reciprocal Cauchy–Schwarz gives
$$
 E[f(k)P_+]\ E[g(k)P_-]\ \ge\ (t/W)(E\sqrt{f(k)g(k)})^2.                    \tag{2}
$$
No comparison of different floors or different optimal faces is involved. For fixed $t>0$, let $m$ be any subsequential value of the physical mark, $s=\sqrt{t/(1+t)}$, and $A=1/\sqrt{2(1+t)}$. In the limit the masses in (1) are one and the first moments are $Ae^m,-Ae^{-m}$. Consequently, writing $f=f_0+f_1 k, g=g_0+g_1 k$, one obtains
$$
 (f_0+f_1 Ae^m)(g_0-g_1 Ae^{-m})\ge s^2\left(\int\sqrt{fg}\,d\nu\right)^2,   \tag{3}
$$
where $\nu$ is the arcsine probability. Both factors are nonnegative. These are unconditional constraints at *each* cold prime floor.

A simple explicit version follows by testing the exact same-side trial in the stationary first-order equation:
$$
 (L_\sigma/P_{\sigma,0}-1)/t=c-E[l_\sigma/P_\sigma].
                                                                    \tag{4}
$$
Cauchy–Schwarz with $EP_\sigma\le1$ bounds the last expectation below by $(E\sqrt{l_\sigma})^2\to8/\pi^2$. Since $L_\sigma/\sqrt n\to1/\sqrt2$, every fixed-floor limiting mark satisfies
$$
 |m|\le \log\frac{\sqrt2[1+(1-8/\pi^2)t]}{\sqrt{1+t}}.                     \tag{5}
$$
For example the bound at $t=1$ is less than $0.174$. Neither mark is normalized by a proxy optimum in this calculation.

## A joint cold estimate, including arbitrarily fast vanishing floors

Let $q=h^2$ be prime squares tending to infinity, and let $t_q>0$ be *any* sequence tending to zero. Then the true minus mark satisfies
$$
 0\le\liminf \frac{\log(\theta_-/P_{-,0}(t_q))}{t_q}
 \le\limsup \frac{\log(\theta_-/P_{-,0}(t_q))}{t_q}
 \le 1-\frac{I(3/4)^2}{1-3/8}<0.112,                                    \tag{6}
$$
with
$$
 I(b)=\frac{\sqrt2}{\pi}\left[\sqrt{1+b}+
 \frac{1-b}{\sqrt{2b}}\operatorname{arsinh}\sqrt{\frac{2b}{1-b}}\right].
$$
Indeed $L_-=\theta_-=(h+1)/2$. Equation (4) implies $P_{-,0}/\theta_-\to1$ uniformly on such sequences, so (1) gives $E kP_-\to-1/2$. By Cauchy–Schwarz,
$$
 E[l_-/P_-]\ge (E\sqrt{l_-(1+bk)})^2/E[(1+bk)P_-].
$$
The denominator tends to $1-b/2$. The numerator tends to $I(b)^2$ by bounded continuous arcsine equidistribution, which needs no joint rate in the floor. Substituting $k=\cos x$ gives $I(b)=(2\sqrt2/\pi)\int_0^1\sqrt{1-b+2bu^2}\,du$. Apply (4) and $\log(1+v)\le v$. This controls the average signed physical derivative over a shrinking real interval: for the plus mark $m_q$, its secant from zero has liminf at least $-1/2$ and limsup below $-0.388$, by reciprocity. The field-first derivative from [round 40](astra-scalar-40.md) is exactly $-1/2$; its order of limits alone gives no estimate for these moving secants.

The same upper bound in (6) applies through eligible primes on a side satisfying $\log(\theta_\sigma/L_\sigma)=o(t_q)$, with $1-\sigma bk$ in the test. This follows from (4), optimality, and (1); the added log benchmark discrepancy divided by $t_q$ vanishes. This is a conditional claim about proximity to the corresponding Jacobi extremum. The pointwise inequalities (1)–(5) themselves require no such hypothesis.

## What the first moments allow

Even exact pointwise reciprocity and the full positive affine tests in (3) allow nonzero cold marks locally around zero. To see the loss, fix $t>0$, $D=\sqrt{2/t}$, and define on the arcsine probability space
$$
 p_*=s(\sqrt{1+D^2k^2}+Dk),\qquad q_*=s(\sqrt{1+D^2k^2}-Dk).
$$
Their product is $s^2$, their first moments are $A,-A$, and their common mean $1-C=s\int\sqrt{1+D^2k^2}\,d\nu$ is strictly below one by strict Jensen and $\int k^2\,d\nu=1/2$. For any $m$ with $2A\max(|e^m-1|,|e^{-m}-1|)<C$, put
$$
 p=p_*+C+2A(e^m-1)k,\qquad q=q_*+C-2A(e^{-m}-1)k .
$$
They are positive, each has mass one, and their first moments are $Ae^m,-Ae^{-m}$, while $pq\ge s^2$. To realize *exact* reciprocity add a fair independent sign and use $P=p(1\pm\sqrt{1-s^2/(pq)})$ and $Q=s^2/P$. Their conditional means given $k$ are $p,q$, respectively. Thus every inequality (3) holds simultaneously. As $t\downarrow0$, $C\to1-2\sqrt2/\pi>0$. These constraints leave a fixed open interval of cold marks, even if every positive affine test is imposed. This is a moment-space construction. It does not obey the full Paley projector equations and does not produce a counterexample to the theta limit.

The estimates give neither common complex access at cold floors nor a prime-uniform bound on high signed stationary derivatives. ETH Problem 26 remains open.

The [192-bit checker](astra-branch-41-check.py) replays (1) and (4) for both signs at the prime-13 physical floor $30/19$. Here the even plus row is $1+\tfrac12\cos(\pi i/3)$ by the [prime-13 cubic](astra-complex-39.md). It also encloses the upper bound in (6) between $0.11166$ and $0.11167$. Run `.venv/bin/python -B research/astra-branch-41-check.py` for the [three records](astra-branch-41-checks.jsonl).
