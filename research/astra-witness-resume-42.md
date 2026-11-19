# Concentrated feasible tests of the true Picard endpoint

There are two uniform restrictions on any positive sector probability. Its normalized signed endpoint response is small simultaneously at every late depth outside an explicit exceptional set of its cyclic translates. At a critical marked mass, its rooted response has a stronger lower bound than round 41, with coefficient multiplied by $3\pi^{2/3}$. The latter follows from a finite inequality which remains meaningful at shrinking positive floors. The former does not exclude the distinguished root from the exceptional set.

Use [round 41](astra-repair-41.md) notation throughout. In particular $\mu$ is any nonnegative probability in $\mathbb R1+V_\sigma$, $Y_t=\sqrt n\,v_t$ is the actual undamped zero-start orbit, and $W=1+(1-1/n)\tau$. All finite statements hold at eligible primes and squares. They use real sector probabilities and the true orbit; no limiting random-field model enters.

## A translated maximal bound uniform in the entire future

Let $\mu_x(i)=\mu(i-x)$ on cyclic frequency indices and let
\[
 m_t(x)=\sigma\sum_i\mu_x(i)Y_t(i),\qquad Q_t(x)=m_{t+1}(x)-m_1(x).
\]
Translation preserves positivity, mass and Fourier sector. If inversion-even tests are required, average each translate with its inversion; its mark and all these pairings are unchanged since the orbit is even. For $0\le\tau\le1$, $0<\eta\le1$, and every integer $L\ge1$ one has
\[
 \frac1n\#\{x:\exists t\ge L,\ Q_t(x)>\eta t\}
 \ \le\ \frac{10^4 W^2}{\eta^4 L}.                                      \tag{1}
\]
The reverse sign is bounded pointwise at *every* translation by
$-Q_t(x)\le 2(g_t-g_0)\le2\sqrt{W(t+1)}$. Indeed the centered-source identity of [round 40](astra-completion-40.md) gives $Q_t(x)=\sum_i\mu_x(i)S_t(i)-E S_t$ with $S_t=\sqrt n(\phi_t-\phi_0)\ge0$. Its mean is $2(g_t-g_0)$.

For the positive direction, Jensen in the spatial average, translation invariance, and nonexpansiveness give
\[
 E_x Q_t(x)^2\le\|v_{t+1}-v_1\|^2\le E_t\le4Wt .
\]
The actual one-step formula gives $m_{j+1}(x)\ge m_j(x)-2g_j$, since $\sum\mu_x f(Y_j)\ge m_j(x)$ and the true marked contribution is nonnegative. Thus on $L\le s\le t\le 2L$,
\[
 Q_s(x)\le Q_t(x)+2\sqrt{(t-s)\,W(2L+1)}.
\]
Here $\sum_{j=0}^{2L}g_j^2\le W(2L+1)$ by the exact energy telescope. Assume $L\ge128W/\eta^2$ (otherwise (1) is trivial) and use a grid on $[L,2L]$ of integer spacing $h=\lfloor\eta^2L/(64W)\rfloor$, including both endpoints. Every value $Q_s>\eta s$ forces $Q_t>\eta L/2$ at its next grid point. The grid has at most $2+128W/\eta^2$ points and each exceptional fraction is at most $32W/(\eta^2L)$. Sum the bounds for $L,2L,4L,\ldots$ to get (1). The constants are absolute. This applies also when choosing the test after the field and the orbit are known, with the exceptional set depending on that test. It does not permit choosing a different test at each translation. In particular (1) controls the whole log-star window at once as $L\to\infty$.

## A finite critical-mass inequality

At the distinguished root write $m_t=m_t(0)$, $\alpha=\sqrt n\mu_0$, $\gamma=\alpha-\sqrt W$, $f(y)=\sqrt{y^2+4\tau}$, $b_j=\sqrt{4+v_j(0)^2}-\sqrt{4\tau/n+v_j(0)^2}$, and
\[
 R_t=\alpha\sum_{j<t}(2-b_j),\quad
 F_t=2\sum_{j<t}(\sqrt W-g_j),\quad
 H_t=\sum_{j<t}(\sum_i\mu_i f(Y_j(i))-m_j).
\]
For $0<\tau\le1$ define $a=1/(4\sqrt W)$, $b=2\tau$, $U=F_T+H_T$, and
\[
 d=U+2T\gamma_++\sqrt\tau+2W^{1/4}\sqrt U .
\]
Every positive integer $T$ satisfies
\[
 U+4\sqrt{ab}\big(\sqrt d+\sqrt{d+F_T}\big)
 \ \ge\ 3(\pi^2a b^2T)^{1/3}.                                         \tag{2}
\]

Indeed the round-41 identities give $m_j=2\gamma j+F_j+H_j-R_j$, $R_j\ge0$, $H_j$ nondecreasing from zero, and $\sqrt W F_j=E_j/4+\sum_{i<j}(\sqrt W-g_i)^2$. Interpolate the **actual** $F_j$ linearly to a nonnegative path $F$ on $[0,T]$. Its kinetic energy satisfies $a\int F'^2\le F_T$. Each increment of $F$ is at most $2W^{1/4}\sqrt U$ in absolute value. Therefore on $[j,j+1]$ one has $(m_j)_++\sqrt\tau\le F+d$ using $H_j\le U$. Jensen's bound $H_{j+1}-H_j\ge b/((m_j)_++\sqrt\tau)$ now gives
\[
 U\ge\int_0^T \left(aF'^2+\frac b{F+d}\right)dt .
\]
Put $z=F+d$, $M=\max z$. Complete the square to bound the integrand below by $b/M+2\sqrt{ab}|z'|\sqrt{1/z-1/M}$. On the way from $d$ to the maximum and then to $d+F_T$, the weighted variation integrates over both ranges at least once. The integral from zero to $M$ of $\sqrt{1/y-1/M}$ is $\pi\sqrt M/2$, and the part from zero to any $u\le M$ is at most $2\sqrt u$. Hence
\[
 U+4\sqrt{ab}(\sqrt d+\sqrt{d+F_T})\ge bT/M+2\pi\sqrt{abM}.
\]
Minimizing over $M>0$ proves (2).

For any sequence $T\to\infty$, even allowing $\tau\downarrow0$, if $\gamma_+=o((\tau/T)^{1/3})$, the finite estimate implies
\[
 \liminf\frac{m_T+R_T-2\gamma T}{(\tau^2T/\sqrt W)^{1/3}}
 \ \ge 3\pi^{2/3}.                                                    \tag{3}
\]
The numerator is exactly $U$. To verify the vanishing-floor uniformity, write $c=(\tau^2 T)^{1/3}$ and consider subsequences with $U=O(c)$. The squared boundary error in (2) is $O(\tau(c+T\gamma_++\sqrt\tau+\sqrt c))=o(c^2)$. The respective ratios to $c^2$ are $O((\tau/T)^{1/3})$, $o(1)$, $O(\tau^{1/6}T^{-2/3})$, and $O(T^{-1/2})$. Since $1\le W\le2$, this proves (3). For a zero-boundary bridge on $[0,1]$, equality in the action minimization is realized by an increasing half-path with $dt/dz=\sqrt{a/b}(1/z-1/M)^{-1/2}$, followed by its time reversal. Its half-length is $\pi M^{3/2}\sqrt{a/b}/2$, so the choice $M^3=b/(\pi^2a)$ gives the prescribed unit length. This proves sharpness for the scalar action. Equality for an actual orbit is not established.

## What this says at the square root and at a prime root

At $q=r^2$, $\tau=1$, the exact subfield-annihilator probability has $\alpha^2=2(r-1)/(r+1)$. In the round-38 marked window, $T|\gamma|+R_T=o(1)$ uniformly for growing depths by round 41. Hence its signed terminal mean obeys
\[
 \liminf \frac{m_T}{T^{1/3}}\ge 3\pi^{2/3}2^{-1/6}.
\]
The same lower coefficient holds after removing the mark, since the removed term is $o(1)$. At the same floor it also applies to the mean of the unmarked terminal excess $S_T$ on the annihilator with the original denominator, since $f(y)-2\ge y-2$. At fixed floors below one the very same square probability gives linear rooted growth from round 41. Thus an upper bound that allowed an exceptional set of translations, even for the true positive test and the entire future as in (1), does not yield the required rooted upper bound. At prime order (2) and (3) apply to every actual test meeting the stated mass condition. Existence of a prime critical witness and the necessary prime rooted upper estimate remain unresolved.

Run `.venv/bin/python -B research/astra-witness-resume-42-check.py` from the repository root to reproduce the six [256-bit records](astra-witness-resume-42-checks.jsonl). The accompanying [Arb replay](astra-witness-resume-42-check.py) tests (2), the actual translated-score/source identity and the centered translation second-moment bound on prime and square orbits. Its finite examples are separate from the all-field proofs.
