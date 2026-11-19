# A contact projection for fourth moments, and an unavoidable unsigned baseline

**Status: two finite-field lemmas, not a proof or refutation of ETH Problem 26.** The main new lemma converts peaks of the **actual** complementary QP spectra into a lower bound for the centered fourth moment. It also subtracts the part of the signed covariance explained by those peaks, with a rigorous bound using only the remaining variance. At the actual square QP $q=49,r=1/28$, three subfield contacts explain more than $96.5\%$ of that variance; the new certificate alone proves $S_+-S_->0.08$.

A second, unconditional result rules out a stronger interpretation of the requested fourth-moment target: the unsigned Cauchy–Schwarz majorant integrated over the **whole** interval $[\kappa/\sqrt p,1]$ has lower limit at least 2, even through genuine primes. This does **not** rule out the small-width, integrable-envelope condition (22) in [astra-convolution-11.md](astra-convolution-11.md). That condition already separates the fixed-width signed argument from the small-width tail.

Only this note and [astra-fourth-12.py](astra-fourth-12.py) were written. The starting sources were [the quadratic QP](quadratic-theta.md), [the prime phase-packing argument](astra-quadratic-10.md), [the cross-convolution identities](astra-convolution-11.md), and [the quadratic path limit](parallel-quadratic-limit-9.md). The [ETH statement](https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/) was checked on 2026-11-17: the field orders in the conjecture are primes. None of the lemmas below supplies a new prime-specific character-sum estimate.

## 1. Normalization

Let $q\equiv1\pmod4$, $n=(q-1)/2$, and $N=n-1$. Use the actual normalized QP pair

\[
 x=A_+(r),\qquad y=A_-(r),\qquad
 y=Q_+(r)x,\qquad x_i y_i=\mathbf1_{i=0},
 \qquad x_0=a,\quad y_0=a^{-1}.
\]

Both vectors are nonnegative and inversion-even, by uniqueness and reflection symmetry. Write

\[
 c=\frac{\sum_i x_i}{\sqrt n}=\frac{\sum_i y_i}{\sqrt n},
 \quad b=1-c^2=S_++S_-,\quad g=S_+-S_-,\quad
 d=\frac{1-r}{1+r}.
\]

For the probability spectra $\mu_+=x/(c\sqrt n)$, $\mu_-=y/(c\sqrt n)$, let $f_\pm$ be their positional characteristic functions. Put

\[
 B=B_{+,4}+B_{-,4},\qquad
 F=\sum_{t\ne1}|f_+(t)f_-(t)|^2=r^2B,
 \qquad \pi(t)=c^2 f_+(t)\overline{f_-(t)}.
\]

Thus $\pi\ge0$, $\sum_t\pi(t)=1$, $\pi(1)=c^2$, and $g=\sum_t s(t)\pi(t)$, where $s(t)=\chi(1-t)$. The centered variance and covariance from the preceding note are

\[
 V=\sum_{t\ne1}\left(\pi(t)-\frac bN\right)^2
   =c^4r^2B-\frac{b^2}{N},\qquad
 \mathcal C=g+\frac bN.
 \tag{1}
\]

Define the cross-correlations and the normalized coordinate heights by

\[
 R_\eta=\sum_i x_i y_{i+\eta},\qquad
 h_\eta=\frac{x_\eta}{a}+a y_\eta\quad(\eta\ne0),\qquad
 \tau=\frac{nc^2-1}{N}=c^2-\frac bN.
 \tag{2}
\]

Here $0\le h_\eta\le1$: at a bulk coordinate at most one summand can be positive, and the maximum-at-mark property bounds it by one. Also $\tau\ge0$, since the common sum of $x,y$ is at least $\max(a,a^{-1})\ge1$.

Two terms of the correlation sum, at $i=0,-\eta$, give

\[
 \boxed{R_\eta\ge h_\eta\quad(\eta\ne0).}
 \tag{3}
\]

Evenness is used for $x_{-\eta}=x_\eta$. The terms are distinct for every nonzero shift, including a shift of order two.

## 2. The contact-projection lemma

Let $I\subseteq G\setminus\{0\}$ be any set of $k<N$ shifts satisfying $h_\eta>\tau$. Set

\[
 w_\eta=h_\eta-\tau\quad(\eta\in I),\qquad
 W=\sum_{\eta\in I}w_\eta,
 \qquad
 L_I=\sum_{\eta\in I}w_\eta^2+\frac{W^2}{N-k}.
 \tag{4}
\]

For the empty set take $W=L_I=0$. Define a vector on the nonzero shifts by

\[
 v_\eta=
 \begin{cases}
 w_\eta,&\eta\in I,\\
 -W/(N-k),&\eta\notin I.
 \end{cases}
 \tag{5}
\]

Finally let $\lambda_\eta=\sum_{t\in Q}s(t)\eta(t)=nK_{\eta0}$ be the real Jacobi eigenvalue in the present convention, and put

\[
 \mathcal C_I=\frac1n\sum_{\eta\ne0}\lambda_\eta v_\eta.
\]

**Lemma.** At every positive width, including a support change,

\[
 \boxed{\begin{aligned}
 nV&\ge L_I,\\
 \left|\mathcal C-\mathcal C_I\right|
 &\le\sqrt{\left(N-\frac1N\right)
                  \left(V-\frac{L_I}{n}\right)}.
 \end{aligned}}
 \tag{6}
\]

In particular,

\[
 \boxed{
 n c^4r^2B\ge\frac{n b^2}{N}+L_I.}
 \tag{7}
\]

**Proof.** The transform of $\pi$ is $R$. Its root is $R_0=1$, and

\[
 \sum_{\eta\ne0}R_\eta=nc^2-1=N\tau.
\]

The transform of the reference measure having mass $c^2$ at 1 and mass $b/N$ elsewhere is 1 at shift zero and $\tau$ at every other shift. Parseval therefore gives the exact identity

\[
 \Delta_\eta=R_\eta-\tau\quad(\eta\ne0),\qquad
 \sum_\eta\Delta_\eta=0,\qquad
 \|\Delta\|_2^2=nV.
 \tag{8}
\]

By (3), $\Delta_\eta\ge w_\eta$ on $I$. The vector $v$ has zero sum and squared norm $L_I$. Moreover,

\[
 \langle v,\Delta-v\rangle
 =\sum_{\eta\in I}
       \left(w_\eta+\frac{W}{N-k}\right)(\Delta_\eta-w_\eta)
 \ge0.
\]

Consequently

\[
 \|\Delta-v\|_2^2\le nV-L_I.
 \tag{9}
\]

This is the Euclidean projection of zero onto the mean-zero vectors obeying the selected contact lower bounds. It does not assume that any of those bounds is attained.

Fourier inversion and the reference measure give

\[
 \mathcal C=\frac1n\sum_{\eta\ne0}\lambda_\eta\Delta_\eta.
\]

The elementary identities $\lambda_0=-1$, $\sum_\eta\lambda_\eta=0$, and $\sum_\eta\lambda_\eta^2=nN$ imply

\[
 \sum_{\eta\ne0}\left(\lambda_\eta-\frac1N\right)^2
   =n\left(N-\frac1N\right).
\]

Because $\Delta-v$ has zero sum, Cauchy–Schwarz with this **centered** Jacobi vector and (9) proves (6). Equation (7) follows from (1). No approximation of the optimizer, support stability, or prime-power transfer is used. \$\square$

### Consequences at a moving width

If $k$ bulk coordinates have $h_\eta\ge\tau+\delta$, then

\[
 nV\ge\frac{Nk}{N-k}\delta^2,\qquad
 k\le\frac{N nV}{nV+N\delta^2}.
 \tag{10}
\]

Thus, at $r=\kappa/\sqrt q$, a set of order $\sqrt n$ coordinates with a fixed positive excess over $\tau$ forces $B=\Omega_\kappa(\sqrt n)$. Conversely $B=o(\sqrt n)$ excludes such a set. This is a statement about the actual two spectra and their root-normalized heights; it is not a statement about an arbitrary compressed eigenspace.

There is also a signed decomposition with a smaller error than the original variance bound:

\[
 g=-\frac bN+\mathcal C_I+e_I,\qquad
 |e_I|\le
 \sqrt{\left(N-\frac1N\right)\left(V-\frac{L_I}{n}\right)}.
 \tag{11}
\]

For any choice of $I=I(r)$, the same formula can be integrated against $dr/r$. Its use is that a concentrated component need not be charged again to the error: its Jacobi-weighted contribution is explicit. On the square control that contribution has the obstructing positive sign. When $I$ is empty, this reduces to the preceding Cauchy–Schwarz estimate and gives no additional cancellation.

In particular this lemma does **not** exclude the dispersed large-energy case in which all heights remain below $\tau$. The arithmetic required to handle that case has not been proved here.

## 3. An unavoidable total-energy and fourth-moment baseline

The following lower bound is valid for the actual QP at every order, with no character-sum estimate:

\[
 \boxed{b(r)\ge\frac{4r}{(1+r)^2}
                    \left(1-\frac1{\sqrt n}\right)^2.}
 \tag{12}
\]

To prove it, put $u=x+y$, $z=x-y$. Complementarity and the reciprocal metric give

\[
 u=|z|+\epsilon e_0,\quad 0<\epsilon\le2,\qquad
 z=dKu,\qquad \|z\|_2^2=\|u\|_2^2-4.
\]

Since $K^2=I-J$ and $Ju=2cj$,

\[
 \|z\|_2^2=\frac{4d^2b}{1-d^2}.
\]

Let $T=\sqrt{b/(1-d^2)}$ and $\alpha=n^{-1/2}$. The mass and the inequality $\|z\|_1\le\sqrt n\|z\|_2$ imply $c\le dT+\alpha$. Thus the triangle inequality in $\mathbb R^2$ gives

\[
 1=\sqrt{c^2+b}
 \le\sqrt{(dT+\alpha)^2+(1-d^2)T^2}
 \le T+\alpha.
\]

Hence $T\ge1-\alpha$, proving (12) because $1-d^2=4r/(1+r)^2$.

Let

\[
 H_q(r)=c(r)^2\sqrt{nB(r)}
\]

be the uncentered fourth-moment density used to majorize $g(r)/r$. Cauchy–Schwarz on the $N$ nonidentity positions gives

\[
 b=r c^2\left(\sum_{s(t)=+1}|f_+(t)|^2
                    +\sum_{s(t)=-1}|f_-(t)|^2\right)
 \le r c^2\sqrt{NB}.
\]

Consequently, for $0<r_0<R\le1$,

\[
 \boxed{
 \int_{r_0}^{R}H_q(r)\,dr
 \ge4\sqrt{\frac nN}\left(1-\frac1{\sqrt n}\right)^2
       \left(\frac1{1+r_0}-\frac1{1+R}\right).}
 \tag{13}
\]

This gives, for **every fixed** $\kappa>0$,

\[
 \boxed{
 \liminf_{\substack{p\to\infty\\p\equiv1\ (4)\ \mathrm{prime}}}
 \int_{\kappa/\sqrt p}^{1}c_p(r)^2\sqrt{nB_p(r)}\,dr\ge2.}
 \tag{14}
\]

There is no assumption here about fixed-width convergence of $m_p$. The same calculation gives a lower limit of 2 for $\int b_p(r)\,dr/r$. Thus neither total energy nor its uncentered fourth-moment majorant can have a vanishing whole-interval integral, even if the signed integral does vanish.

This obstruction does not apply to the intended small-width condition: with upper endpoint $R=\varepsilon$, the limiting lower bound in (13) is only $4\varepsilon/(1+\varepsilon)$, which tends to zero. It also does not give a lower bound for the **centered** covariance majorant. The correct distinction is explicit in

\[
 H_q(r)^2=\frac n{r^2}V(r)+\frac{n b(r)^2}{N r^2}.
\]

## 4. Actual-QP replay and the square sign certificate

The script checks 47 small numerical QPs at primes

\[
 13,17,29,41,61,97,173,257,401
\]

and squares $7^2,11^2,13^2$, with $\kappa=1/16,1/4,1,4$, omitting widths above one. The optional large run adds $97^2$ and (9413) at $\kappa=1/4$. It checks (3), (8), (6), (12), and the pointwise density bound underlying (13). These are numerical checks, not proofs of an asymptotic statement.

At scaled width $1/4$, the positive contact set in the table is all shifts with $h_\eta>\tau$:

| Order | $B_{+,4}+B_{-,4}$ | $nV$ | Number of contacts | $L_I/(nV)$ |
|---:|---:|---:|---:|---:|
| 49 | 5.05516738 | 0.07199803 | 3 | 0.965964 |
| 97 | 0.68940200 | 0.00721113 | 0 | 0 |
| 169 | 10.99595693 | 0.18702871 | 6 | 0.988361 |
| 401 | 0.24926151 | 0.00350858 | 0 | 0 |
| $97^2$ | 94.58792086 | 1.85696417 | 48 | 0.991027 |
| 9413 | 0.01404767 | 0.00022372 | 0 | 0 |

The square rows identify the nonzero subfield-annihilator coordinates. The absence of contacts in these prime rows is **not** evidence that (6) controls every dispersed profile.

For $q=49,r=1/28$, the 192-bit Arb replay certifies the actual orthant with positive bulk coordinates $\{4,6,12,18,20\}$. It verifies every strict orthant sign and $|\gamma|<1$, as in the existing damped fixed-point certificate. Selecting just $I=\{6,12,18\}$ gives rigorous enclosures

\[
 \begin{aligned}
 nV&=0.07199802886346927877\ldots,\\
 L_I&=0.06954750149455585553\ldots,\\
 \mathcal C_I&=0.14198087598715252071\ldots,\\
 \sqrt{(N-1/N)(V-L_I/n)}
    &=0.04841469509043505422\ldots.
 \end{aligned}
\]

It therefore proves, using (11) rather than directly evaluating the signed energy,

\[
 \boxed{S_+-S_-\ge
 \mathcal C_I-\sqrt{(N-1/N)(V-L_I/n)}-b/N
 >0.08586>0.08.}
 \tag{15}
\]

The same certificate gives $B>5$ and $L_I/(nV)>0.965$. This is a strict square-control check of the **sign** retained by the new projection, not merely a fourth-moment magnitude check. A separate strict actual-prime orthant at $p=13,r=1/4$ checks the normalizations; its selected contact set is empty.

Reproduce from the repository root:

```sh
.venv/bin/python -B research/astra-fourth-12.py --certificate
.venv/bin/python -B research/astra-fourth-12.py --large
```

The 49 numerical rows had largest checked discrepancy below $3\cdot10^{-15}$ and largest QP residual below $1.9\cdot10^{-11}$. No finite sample is used to infer the prime limit. The proved deliverables are the contact projection (6) and the genuine-prime obstruction (14); the requested prime small-width fourth-moment upper bound and signed cancellation remain unproved.
