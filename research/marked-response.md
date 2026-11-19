# A marked-response criterion for the theta limit

The positive smoothing pair gives an exact derivative of the marked coordinate with respect to the weights. Integrating that derivative yields the normalized theta value. The criterion below only calls for control of a scalar response. It also identifies the part of the linearized solution that becomes large in the [square-order control](square-order-control.md).

## Weighted complementary projections

Let $V_\pm$ be the $\pm1$ eigenspaces of $K$ in the real, mean-zero frequency vectors, and put $U_\pm=\mathbb R\mathbf1\oplus V_\pm$. For positive coordinate weights $w$, write $W=\sum_i w_i$. Let $P$ maximize $\sum_i w_i\log P_i$ over positive $P\in U_+$ of mean $1$. The constant vector is feasible, all nonnegative vectors of mean $1$ form a compact set, and the log objective tends to $-\infty$ at any zero coordinate. Strict concavity gives a unique positive maximizer. The first-order condition gives $(w_i/P_i)_i\in U_-$. Since the mean-zero parts of $U_+$ and $U_-$ are orthogonal, its mean is $W/n$, and $Q_i=nw_i/(WP_i)$ is the maximizer for the minus space with mean $1$. These maximizers depend smoothly on positive weights by the implicit function theorem, since the log Hessian restricted to $V_+$ or $V_-$ is negative definite. For even weights the maximizers are even by uniqueness. The actual smoothing pair is $A=\sqrt{W/n}\,P$, $B=\sqrt{W/n}\,Q$, so $A_iB_i=w_i$ and $v^*=A-B$.

Write $\nu_i=\sqrt{w_i}$, $\gamma_i=\frac12\log(P_i/Q_i)=\operatorname{arsinh}(v^*_i/(2\sqrt{w_i}))$, and let $\Pi_\pm$ be the orthogonal projectors onto

$$E_+=\operatorname{diag}(\nu/P)V_+,\qquad E_-=\operatorname{diag}(\nu/Q)V_-.$$

Both spaces are orthogonal to $\nu$ by the first-order conditions. They are orthogonal to each other because $w_i/(P_iQ_i)=W/n$. They have combined dimension $n-1$ and therefore decompose $\nu^\perp$. If the weights vary along a differentiable path, then $\nu\dot{\log P}\in E_+$ and $\nu\dot{\log Q}\in E_-$. The logarithmic derivative of $P_iQ_i=nw_i/W$ identifies their sum as $2\operatorname{proj}_{\nu^\perp}\dot\nu$. Consequently

$$\nu\dot\gamma=(\Pi_+-\Pi_-)\dot\nu,\qquad
\sum_i w_i\dot\gamma_i^2=\|\operatorname{proj}_{\nu^\perp}\dot\nu\|_2^2.$$

For two choices of positive weights with the same marked weight $w_0$, interpolate linearly between their square roots. The marked value obeys the dimension-free estimate

$$|\gamma_0(w')-\gamma_0(w)|\le\frac{\|\sqrt{w'}-\sqrt w\|_2}{\sqrt{w_0}}.$$

This bound applies to nonuniform changes of the smoothing weights. For example, changing weights on a set of small total weight has small effect when the relative changes there are bounded.

## An integral for the conjectured limit

Vary $w_0=s$ with the bulk weights fixed, and differentiate in $\log s$. Put $\ell_\pm=(\Pi_\pm)_{00}$. The derivative identity gives

$$2\frac{d\gamma_0}{d\log s}=\ell_+-\ell_-,\qquad \ell_++\ell_-=1-\frac{s}{W},\qquad \ell_\pm\ge0.$$

Scaling all weights leaves $\gamma$ and the two projectors unchanged. Thus on the original family $w_0=1$, $w_i=\tau/n$ for $i\ne0$, we have $-2\,d\gamma_0/d\log\tau=\Delta(\tau)$ where $\Delta=\ell_+-\ell_-$. At $\tau=n$, all weights are equal and $\gamma_0=0$. At $\tau\downarrow0$, the [theta bracket](smoothing.md) gives $\gamma_0\to\log(\vartheta(\overline H)/\sqrt n)$. Hence the exact identity is

$$\log\frac{\vartheta(\overline H)}{\sqrt n}=\frac12\int_0^n \Delta(\tau)\,\frac{d\tau}{\tau}.$$

Both endpoints of this integral can be bounded uniformly through field orders $q=2n+1$. At the small endpoint $|\Delta|\le1-1/W\le\tau$. At the large endpoint, take $0<T\le n$. All entries of $u=\Phi(v^*)$ are at least $2\sqrt{T/n}$ at weight $T$, and $\sum u_i=2\sqrt{nW}$. Because $K$ annihilates constants and $|K_{ij}|\le\sqrt q/n$,

$$|\gamma_0(T)|\le |v_0^*(T)|/2
\le\sqrt{q/n}(\sqrt W-\sqrt T)
=\sqrt{q/n}\,\frac{1-T/n}{\sqrt W+\sqrt T}
\le\frac{\sqrt3}{2\sqrt T}.$$

For $0<\varepsilon<T\le n$ this proves

$$\left|\log\frac{\vartheta(\overline H)}{\sqrt n}-\frac12\int_\varepsilon^T\Delta(\tau)\,\frac{d\tau}{\tau}\right|
\le\frac{\varepsilon}{2}+\frac{\sqrt3}{2\sqrt T}.$$

In particular, proving pointwise balance $\Delta_p(\tau)\to0$ for each fixed $\tau>0$ would suffice by dominated convergence. This uses the exact marked values at the endpoints and no uniform $\ell_2$ bound on the fixed points.

## A symmetric operator for the response

Let $P_\perp=I-J$, with $J$ projecting onto constants. Write $u=\Phi(v^*)$, $D_i=v_i^*/u_i$, and use $D$ as a diagonal matrix. On the mean-zero space put

$$H=K-P_\perp D P_\perp,\qquad e=P_\perp e_0,\qquad x=H^{-1}e.$$

This is a symmetric invertible operator: $K$ is an isometry on that space and $\|D\|<1$. Differentiating $v^*=K\Phi(v^*)$ in $\log s$ with fixed bulk weights gives $\dot v=2s x/u_0$. The marked response obeys

$$\Delta=(1-D_0^2)\langle e,H^{-1}e\rangle-D_0.$$

The full weighted speed identity also gives

$$\sum_i(1-D_i^2)\left(x_i-\frac{v_0^*u_0}{4s}\mathbf1_{i=0}\right)^2=\frac{1-s/W}{1-D_0^2}.$$

Indeed $\dot\gamma_i=(\dot v_i-\tfrac12 v_0^*\mathbf1_{i=0})/u_i$, and $\sum_i w_i\dot\gamma_i^2=s(1-s/W)/4$. The identity bounds the unweighted response on the part of the spectrum where $|D_i|$ is separated from $1$. Large responses can come from frequencies with nearly saturated $|D_i|$.

There is a parallel bound on the spectral measure of $H$ at $e$. For $y$ in the spectral subspace $|H|\le\eta$, $\|D y\|_2^2\ge\|(K-H)y\|_2^2\ge(1-2\eta)\|y\|_2^2$. Thus $(1-D_0^2)|y_0|^2\le2\eta\|y\|_2^2$. Apply this to the projection of $e$ onto this spectral subspace, for which $y_0=\|y\|_2^2$. If $\mu_{p,\tau}$ is the spectral measure at $e$, then

$$\mu_{p,\tau}([-\eta,\eta])\le\frac{2\eta}{1-D_0^2}.$$

This linear bound does not give uniform integrability against $1/|\lambda|$ at zero. To use weak convergence of the spectral measures to estimate the resolvent, a stronger bound at zero or a signed cancellation is needed.

The [stationary equation gives a sharper bound](stationary-tails.md) of order $\eta^2\|v^*\|_2^2+\tau\eta$ for the marked spectral mass. With decreasing weights it controls the absolute inverse contribution below the square-root width, and a strongly coupled band at that width forces a large stationary tail.

For a width $\eta>0$, use the regularized signed response $m_\eta=\int \lambda/(\lambda^2+\eta^2)\,d\mu(\lambda)$. The linear spectral-mass bound gives $\int\eta^2/(\lambda^2+\eta^2)\,d\mu=O_\tau(\eta)$ by summing over $|\lambda|\le\eta$ and the dyadic annuli outside it. Cauchy–Schwarz therefore gives

$$|m_p-m_\eta|\le O_\tau(\sqrt\eta)\,\|H^{-1}e\|_2.$$

Thus a uniform norm bound for the *response to the marked input* would justify removing this regularization. This calls for a local solve, rather than a bound on the norm of every smoothed vector. Both quantities can be compared in the same experiment.

The [stationary resolvent sum rule](resolvent-sum-rule.md) gives another transfer estimate, using only the positive part of the mixed correlation $\langle u,\eta^2(H^2+\eta^2)^{-1}e\rangle$. This controls the signed cutoff at decreasing smoothing weights even without a rate condition of the form $\tau\log q\to0$.

One sufficient target is $m_p(\tau)=\langle e,H^{-1}e\rangle\to0$ for each fixed $\tau>0$. It would follow from a symmetric weak limit of $\mu_{p,\tau}$ and uniform integrability against $1/|\lambda|$. To see that it suffices, write $D_0=\tanh\gamma_0$ in the derivative formula to obtain

$$\frac{d}{d\log\tau}\left(\frac{\sinh\gamma_0(\tau)}{\sqrt\tau}\right)
=-\frac{m_p(\tau)}{2\sqrt\tau\cosh\gamma_0(\tau)}.$$

On any fixed compact weight interval in $(0,\infty)$, $m_p$ is uniformly bounded by the leverage and elementary marked bounds. Dominated convergence would identify the left-hand function at any two fixed positive weights in the limit. Sending the larger weight to infinity uses $\gamma_0(T)=O(T^{-1/2})$ and forces the limit to be zero everywhere. The theta bracket would then finish the conjecture.

### Relative diagonal stability

The scalar response formula is the diagonal of an operator identity. Put $S=\operatorname{diag}(\sqrt{1-D_i^2})$ and extend $H^{-1}$ by zero on constants, writing the extension as $\mathcal I=H^{-1}P_\perp$. Differentiate in $\log w_j$ alone. The fixed point gives $\dot v=(2w_j/u_j)\mathcal I e_j$, while the hyperbolic formula gives $\dot\gamma_i=(\dot v_i-\frac12v_i\mathbf1_{i=j})/u_i$. Combining these with the weighted projection derivative yields

$$S\mathcal I S=\Pi_+-\Pi_-+D,\qquad \|S\mathcal I S\|_{2\to2}\le2.$$

The bound holds at the true stationary diagonal even when the unweighted inverse is large. It also gives an explicit perturbation estimate. For another real diagonal $D'=D+E$ put $\kappa=\max_i |E_i|/(1-D_i^2)$. If $2\kappa<1$, the perturbed inverse extension $\mathcal I'=(K-P_\perp D'P_\perp)^{-1}P_\perp$ exists. Indeed with $Y=S\mathcal I S$ the resolvent identity reduces to inversion of $I-Y(S^{-1}ES^{-1})$, whose Neumann series converges. It gives

$$\|S(\mathcal I'-\mathcal I)S\|_{2\to2}\le \frac{4\kappa}{1-2\kappa},\qquad
|m(D')-m(D)|\le\frac{4\kappa}{(1-2\kappa)(1-D_0^2)}.$$

For $D'_i=\tanh\gamma'_i$, a sup error $\max_i|\gamma'_i-\gamma_i|\le\delta$ implies $\kappa\le(e^{2\delta}-1)/2$ by the addition formula. This supplies a criterion to transfer the marked inverse using relative accuracy at saturated coordinates. The available fixed-depth approximations are in normalized $\ell_2$ and do not yet give that relative accuracy.

[A localized comparison](response-locality.md) uses the exact differential equation for $S\mathcal I S-D$. It controls arbitrary changes confined to a bulk set when the reference compression has a gap and the marked column has small mass there.

## What fixed-depth parity gives for the symmetric operator

This calculation uses the [fixed-depth parity draft](iteration-parity.md) with $v^*$ replaced by any fixed Picard iterate $v^{(t)}$ to form $D$, and keeps $t$ fixed as $p\to\infty$. Let $X=Fs/\sqrt n$ and form $H=K-P_\perp D P_\perp$ as above. The marked entry $D_0=o(1)$ and $\|D\|\le1$ give $He=X/\sqrt n+o_{\ell_2}(1)$. On the bulk, $D$ is approximated in normalized $\ell_2$ by odd polynomials of negative trace fields: apply the bounded odd activation $z/\sqrt{z^2+4\tau}$ to the bounded expression approximants in the fixed-depth proof. Products with the uniformly bounded $X$ preserve this approximation. In particular, $D X^2$ has mean $o(1)$ and $F=D X$ is approximated by even polynomials.

The first spectral moment at $e$ tends to zero, since $K_{00}=-1/n$ and $D_0=o(1)$. The third is $\langle He,H He\rangle$, whose limit is zero by $KX=\sqrt n e$, the bound on $X_0$, and the odd mean of $DX^2$. For the fifth, $H^2 e=e-G+o_{\ell_2}(1)$ with $G=P_\perp F/\sqrt n$. In $\langle e-G,H(e-G)\rangle$ the cross term tends to zero by the same odd mean. The last term is $n^{-1}\langle F,KF\rangle-n^{-1}\sum_i D_i(F_i-\overline F)^2$. Both tend to zero by the fixed-depth trace rules. The first pairing applies $K$ to an even field, giving a negative field, and the second expression has odd total parity. Thus the first, third and fifth moments vanish in this fixed-depth limit.

For the seventh, put $g=D(F-\overline F)$, which has odd polynomial approximants and mean $o(1)$. Then $H^3e=(X-KF+g)/\sqrt n+o_{\ell_2}(1)$. Write $Y=X-KF+g$. In the expression $n^{-1}\langle Y,KY\rangle-n^{-1}\sum_i D_iY_i^2$, the last term is odd and tends to zero. In the first term, the pairings involving $X$ or $KF$ vanish by $KX=\sqrt n e$, $K^2F=P_\perp F$, and even-odd orthogonality. This leaves the reduction

$$\langle e,H^7e\rangle=n^{-1}\langle g,Kg\rangle+o(1).$$

After just one Picard update, $D$ is, up to an $o(1)$ correction in normalized $\ell_2$, the bounded odd function $X/\sqrt{X^2+\tau}$ of $X$. The same holds for $g$ with a bounded mean coefficient. The [Chebyshev compression bound](smoothing.md#compression-to-functions-of-the-first-fourier-field) therefore gives a vanishing seventh moment at this depth. At later depths $g$ includes iterated feedback. The existing inertia rules control $K$ applied to even polynomials, while the reduced term tests $K$ between two odd fields. That term at later depths and the transfer to the stationary diagonal $D$ remain unresolved.

## Prime versus square response

The [42-run response sweep](../data/marked-response.csv) computes $H^{-1}e$ by MINRES after the smoothing solve. At $\tau=0.5$ the prime $151337$ gives $\Delta\approx-0.00102$ and $\|x\|_2\approx1.20$, while $389^2$ gives $\Delta\approx0.324$ and $\|x\|_2\approx13.32$. In the square case about $99.6\%$ of the response's squared norm is on the unmarked frequencies trivial on the subfield clique. At $\tau=2$ the square case has $\|x\|_2\approx1.15$ and $\Delta\approx0.00915$. These are numerical comparisons on the recorded cases. They distinguish the size of the local response from the size of the full fixed point. Residuals of both solves are recorded, and small cases were cross-checked against dense weighted projectors and finite differences.

The [regularized runs](../data/marked-response-cutoff.csv) further separate the slow contribution. At $\tau=0.5$ over $389^2$, the inverse entry is about $0.476$. Regularization at width $0.01$ changes it to $-0.0446$, even though the corresponding filtered spectral mass $\int\eta^2/(\lambda^2+\eta^2)\,d\mu$ is only $0.00184$. At the nearby prime $151337$, the two entries are $-0.0013536$ and $-0.0013523$. These quantities were cross-checked against dense spectral decompositions for small graphs. Integrating the measured leverage difference at small orders reproduces the independent Fourier LP value up to the omitted low-weight endpoint.
