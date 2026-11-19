# First bulk angle contact on the genuine floor branch

At a first bulk tie, the two signed total clipping corrections have one-sided derivatives along every differentiable floor path. A linear complementarity problem on the tied sites computes both derivatives. Its symmetric part is positive semidefinite and controls the sum on each sign separately, with an absolute constant after scaling by the total real weight. At the prime 173 and real part \(1/50\), the first true tie occurs at one site. The unaveraged total correction then has right derivative between 678 and 679. First contact on the nominated cold square remains possible at unbounded primes.

## Real differential with the marked product held fixed

Use the real positive pair and weighted reflection \(J=J_w\) of [round 89](real-phase-projection-89.md). Work in the full counting norm. Write
\[
 \nu=\sqrt w,\quad W=\|\nu\|^2,\quad c=Je_0,\quad
 u+iv=n/t,\quad b=v/(2\nu_0),\quad P=b/\nu_0,\quad z=bc,\quad D_i=z_i/\nu_i .
\]
Thus \(\nu_i^2+z_i^2=q_i\) on the bulk, where \(q_i=1+e_i\) is the local product, and \(\nu_0^2+z_0^2=u+b^2\). At the mark \(D_0=Pc_0\). On the bulk \(z_i=\sqrt{q_i}\sin\phi_i\), with \(\phi_i\) the normalized plus factor's phase. Take \(a=1/\sqrt 2\) and \(|D_i|\le a\) on the bulk. Put \(T_0=D_0/(1+P^2)\), \(\mu=|D_0|/\sqrt{1+P^2}\). Below assume \(\mu\le a/2\), as holds on the cold square since \(\nu_0^2\ge u\) and \(|P|\le |v|/(2u)\).

In a real weight variation \(x=\dot\nu\), write \(r=Jx\). The weighted speed is \(\dot\gamma_i=r_i/\nu_i\), with \(\gamma_i=\tfrac12\log(\alpha_i/\beta_i)\). The [reflection differential](response-locality.md#contraction-and-response-derivative) gives \(\dot J=J\,\operatorname{diag}(\dot\gamma)J-\operatorname{diag}(\dot\gamma)\), since the true real stationary diagonal is \(\tanh\gamma\). At fixed marked product \(u+iv\), differentiation of \(z=bJe_0\) gives
\[
 \dot z=A x,\qquad A=J\operatorname{diag}(D)J-P(e_0c^{\mathsf T}+ce_0^{\mathsf T}),\qquad x_0=-T_0\dot z_0 .
\]
For a moving floor add \(c\dot v/(2\nu_0)\) to \(\dot z\), and add \((\dot u+P\dot v)/(2\nu_0(1+P^2))\) to \(x_0\). These terms retain both components of \(n/t\).

For arbitrary real bulk input \(h=x_B\), put \(k_B=D_Br_B\), \(\ell=Jk\) and impose at the mark
\[
 \binom{k_0}{x_0}=T_0
 \begin{pmatrix}1&P\\P&-1\end{pmatrix}\binom{r_0}{\ell_0}.                 \tag{1}
\]
Indeed \(k_0=D_0r_0-Px_0\) and \(\dot z_0=\ell_0-Pr_0\). These are the preceding fixed-product equations. The map in (1) has norm \(\mu\). Write \(Lh=\ell_B=\dot z_B\). Since \(J^2=I-\hat\nu\hat\nu^{\mathsf T}\) with \(\hat\nu=\nu/\sqrt W\),
\[
 a^2\|h\|^2-\|\ell_B\|^2
 \ \ge\ a^2|\hat\nu^{\mathsf T}x|^2+(a^2-\mu^2)(r_0^2+\ell_0^2).       \tag{2}
\]
Use \(\|\ell_B\|^2\le a^2\|r_B\|^2+k_0^2-\ell_0^2\), then bound \(a^2x_0^2+k_0^2\) by (1). For \(h=0\), (2) forces the marked entries to vanish. Hence the scalar elimination is invertible. With \(B\) the bulk indices,
\[
 L=A_{BB}-\frac{T_0 A_{B0}A_{0B}}{1+T_0 A_{00}},\qquad
 L=L^{\mathsf T},\qquad \|L\|\le a .                                      \tag{3}
\]
In matrix products \(D_B\) denotes the bulk diagonal. At fixed bulk products \(x_B=-D_B\dot z_B\), so feedback has norm at most \(a^2=1/2\), independently of all real amplitudes. The real weight equations therefore have invertible Jacobian in the weights at a tie. The implicit function theorem gives a smooth perturbed-product response, using analyticity of the real positive pair at positive weights. At fixed floor its differential is
\[
 \dot z_B=H\,\operatorname{diag}(1/(2\nu_B))\,\dot q_B,\qquad
 H=(I+LD_B)^{-1}L=L(I+D_BL)^{-1}=H^{\mathsf T}.                          \tag{4}
\]
For a moving floor at fixed bulk products put \(f=c\dot v/(2\nu_0)\) and \(g=(\dot u+P\dot v)/(2\nu_0(1+P^2))\). Then the incoming velocity on the physical branch is explicitly
\[
 \dot z_B=(I+LD_B)^{-1}
       \left(f_B+A_{B0}\frac{g-T_0 f_0}{1+T_0 A_{00}}\right).            \tag{4a}
\]
On a fixed real-part vertical ray use \(\dot u+i\dot v=-in/t^2\). The real starting row has \(z_B=0\), so the first bulk tie is the first path integral of (4a) with a coordinate of absolute value \(1/\sqrt3\). This retains the two actual source columns \(c_B,A_{B0}\) and the changing bulk diagonal.

## The signed contact matrix

Let \(C_\sigma\) consist of bulk sites at a true tie \(D_i=\sigma a\), \(\sigma=\pm1\), and \(C=C_+\cup C_-\). At zero correction, \(\nu_i=\sqrt{2/3}\) on \(C\). The clipped inequalities are exactly \(q_i\ge1,\ q_i-3z_i^2\ge0,\ (q_i-1)(q_i-3z_i^2)=0\). The derivative on \(C\) of \(q-3z^2\) with respect to products on \(C\), holding the floor and the other products fixed, is
\[
            M=I-3a\,\operatorname{diag}(\sigma)H_{CC}.                    \tag{5}
\]
The opposite-sign blocks are skew transposes. For every real \(f\) on \(C\),
\[
 f^{\mathsf T} M f\ \ge\
 \frac{8}{63W}\left[\left(\sum_{i\in C_+}f_i\right)^2+
                     \left(\sum_{i\in C_-}f_i\right)^2\right].           \tag{6}
\]
These are sums over individual sites; an even restriction uses the orbit-weighted inner product and sums.

For the proof put \(\eta=\hat\nu_B\). By (1), \(|x_0|^2\le\mu^2(r_0^2+\ell_0^2)\). Weighted Cauchy–Schwarz on \(\eta^{\mathsf T}h=\hat\nu^{\mathsf T}x-\hat\nu_0x_0\) in (2) gives \(a^2\|h\|^2-\|Lh\|^2\ge ka^2|\eta^{\mathsf T}h|^2\), with \(k=(1+a^2\hat\nu_0^2\mu^2/(a^2-\mu^2))^{-1}\ge6/7\). Expanding \(\|Lh\mp ah\|^2\) gives \(\pm L\preceq aI-\delta\eta\eta^{\mathsf T}\) for \(\delta=ka/2\).

For symmetric \(X,T\) of norms at most \(a\), \(G_T(X)=(I+XT)^{-1}X\) is increasing in Loewner order. Along a segment its derivative is \((I+XT)^{-1}\dot X(I+TX)^{-1}\). Apply this to \(X=\sigma L,\ T=\sigma D_B\), so \(G_T(X)=\sigma H\). The difference \(G_T(aI)-G_T(aI-\delta\eta\eta^{\mathsf T})\) equals
\[
 \frac{\delta R\eta\eta^{\mathsf T}R}{1-\delta\eta^{\mathsf T}RT\eta},
 \qquad R=(I+aT)^{-1}.
\]
The denominator is positive by invertibility along the rank-one segment and at most \(1+\delta a/(1-a^2)\le 3/2\). On \(C_\sigma\), \(R\) acts by \(1/(1+a^2)\). As \(3a=(1+a^2)/a\), the corresponding sign block of (5) dominates \((2k/9)\eta_{C_\sigma}\eta_{C_\sigma}^{\mathsf T}\). Substituting \(\eta_i=\sqrt{2/(3W)}\) proves (6). Only vectors with both signed-set sums zero can be null directions of the symmetric part. The quadratic form is strictly positive on each nonzero nonnegative vector.

In fact a same-sign block \(M_{C_\sigma C_\sigma}\) is singular exactly when \(C_\sigma\) supports a nonzero native mean-zero eigenrow of \(K\) in either sector. To see this, extend a null vector \(f\) by zero on the bulk complement of \(C_\sigma\). With \(X=\sigma L\), \(T=\sigma D_B\) and \(R=(I+aT)^{-1}\), the positive semidefinite difference \(G_T(aI)-G_T(X)\) has zero quadratic form on \(f\), so it kills \(f\). This difference is \((I+XT)^{-1}(aI-X)R\) and \(Rf=f/(1+a^2)\). Thus \(Lf=\sigma af\). Equality in (2) gives \(x_0=r_0=\ell_0=0\) and \(x\perp\nu\). As \(\langle x,\ell\rangle=\langle Jx,k\rangle=\sum_{i\ne0}D_i r_i^2=\sigma a\|r\|^2\), the row \(r=Jx\) is supported on \(C_\sigma\). The nonzero rows among \(x\pm Jx\) belong to the weighted sectors, and unweighting preserves their support. Conversely, a supported native eigenrow gives a supported weighted \(x\) with \(Jx=\pm x\). Taking \(k=\sigma a Jx\), \(\ell=\sigma a x\) satisfies (1) and proves \(Lx=\sigma ax\) on the bulk. Substitution in \(G_T\) gives a null vector of the sign block. In particular, \(|C_\sigma|<n/\sqrt p\) suffices for positive definiteness there, by the entry bound for \(K\). When both signs meet the support test, the whole symmetric part is positive definite and (7) determines the coordinate correction uniquely.

## What grows when a true phase crosses

Take a differentiable floor path with forward parameter \(s\), through a zero-correction tie at \(s=0\). Holding \(q=1\), compute the true derivative and put
\[
 d_i=6z_i\dot z_i^{\,\mathrm{true}}=2\sqrt2\,\sigma_i\dot\phi_i^{\,\mathrm{true}}
 \quad(i\in C).
\]
Let \(E_\sigma(s)\) denote the unaveraged total correction on sign \(\sigma\). Solve the monotone linear complementarity problem
\[
     \lambda\ge0,\qquad M\lambda-d\ge0,\qquad
     \lambda_i(M\lambda-d)_i=0\quad(i\in C).                              \tag{7}
\]
Then \(E_\sigma'(0+)=\sum_{C_\sigma}\lambda_i\) for every solution of (7). A positive outward velocity at any true tie forces a positive first-order total correction. If all \(d_i\le0\), both derivatives vanish.

At each fixed field the clipped weights remain in a common compact positive box near the contact. Every accumulation point there is clipped by continuity of the real positive pair. It has zero total correction by the [mean rigidity argument](astra-column-90.md) since the true row itself meets the cap. The argument applies wherever \(|\arg t|/2<\arctan a\), including the finite ray below: the marked tangents \(P(1\pm c_0)\) have the same sign, which bounds the marked relative phase by \(|\arg t|/2\). This makes the exact marked secant strict in the anisotropic norm of round 90. The bulk nonexpansiveness and the same Hilbert identity give mean rigidity without a field-size constraint. Every accumulation point is then unforced. Its secant to the true row is strictly contractive in the ordinary complex Euclidean norm at each site, with multiplier \(\tanh((g+g'+i(\phi+\phi'))/2)\) of modulus less than one since \(|\phi+\phi'|\le2\arctan a<\pi/2\). Thus it equals the true row. All clipped weights converge to the true weights and eventually only sites in \(C\) can have corrections, with their original signs.

For \(e=q_C-1\ge0\), the clipped conditions imply orthogonality to the nonnegative slack \(Me-sd+o(\|e\|+s)\). If \(\|e\|/s\) were unbounded along a sequence, a normalized nonnegative limit would contradict (6). Thus \(e=O_p(s)\), and subsequential limits of \(e/s\) solve (7). This also proves existence. For two solutions \(\lambda,\lambda'\), their cross inner products with the nonnegative slacks give \((\lambda-\lambda')^{\mathsf T}M(\lambda-\lambda')\le0\). Equation (6) forces equal totals on each sign. This proves the derivative assertion without choosing a differentiable clipped row. For \(d\le0\), zero solves (7); otherwise zero is infeasible. Also \(\sum_C\lambda_i\le(63W/4)\max_i(d_i)_+\) follows from (6) and \(\lambda^{\mathsf T}M\lambda=\lambda^{\mathsf T}d\). Reversing the floor direction computes the other one-sided derivative.

At a single tied site, \(M_{ii}>0\) and \(\lambda=(d_i)_+/M_{ii}\). For a single inversion orbit of an even row, use its constant-direction entry in the even restriction and multiply the common per-site price by the orbit size for the total. The strict lower bound \(8/(63W)\) for a single site's denominator may decay with the field order.

## Higher-order and tangent contacts

In a possibly field-dependent neighborhood of a zero-correction tie, put \(\omega=\max_{i\ne0}(3(z_i^{\,\mathrm{true}})^2-1)_+\) for the actual local unforced solution at the new floor. The total clipping correction obeys the two-sided bound
\[
      \frac{\omega}{5}\ \le\ E_++E_- \ \le\ \frac{63W}{2}\,\omega,       \tag{8}
\]
where \(W\) is evaluated at the tie. To verify this, work on the original tied sites, since every other site stays strictly below the cap for both the true and clipped rows. The slack difference between bulk corrections \(e\) and \(0\) at the new floor equals \(\bar M e\), for the integral of the smooth slack Jacobian along the product segment from \(1\) to \(1+e\). Compactness and uniqueness above give \(\bar M\to M\). At contact \(\|M\|\le1+3a^2/(1-a^2)=4\) by (4). Thus \(\|\bar M\|\le5\) locally, and a true violated slack of size \(\omega\) requires \(5\|e\|_1\ge\omega\). Shrink the neighborhood so \(\|\bar M-M\|\le2/(63W)\). For nonnegative \(e\), (6) then gives \(e^{\mathsf T}\bar M e\ge2\|e\|_1^2/(63W)\). Complementarity bounds the same form above by \(\omega\|e\|_1\), proving (8). In particular exact feasibility of the true row is equivalent to zero correction there, including at tangent contacts.

On a real analytic ray starting from the tie, either \(\omega(s)=0\) for all sufficiently small \(s>0\), or \(\omega(s)/s^k\) has a positive finite limit at some integer \(k\ge1\). This follows from the finitely many analytic true slacks and the sign of each leading nonzero coefficient. In the latter case discard any site where \(d_i(s)=3(z_i^{\,\mathrm{true}}(s))^2-1\) has negative leading term of order less than \(k\). Its true slack dominates \(s^k\), and \(\bar M e=O_p(s^k)\) by (8), forcing \(e_i=0\) there. At every remaining site take \(d_i^{[k]}=\lim_{s\downarrow0}d_i(s)/s^k\). The limits are finite, including at identically tied sites, and at least one is positive. Apply (7) on this remaining set with the corresponding principal submatrix and \(d^{[k]}\). The subsequence and signed-sum argument now proves that \(E_\sigma(s)/s^k\) converges to the corresponding signed-set sum of any solution. Their combined limit is strictly positive. The neighborhood used for (8) and this order classification can shrink through primes.

## First tie at a genuine prime

For \(p=173,\ t=1/50+iy\), the first true bulk tie of \(|\tan\phi_i|=1/\sqrt2\) along \(y\ge0\) satisfies
\[
              0.01294720<y_*<0.01294721 .
\]
Only \(i=43\) is tied, on the positive sign. This site is fixed by inversion. On the contact bracket, 128-bit Arb gives \(44.08<\partial_y\phi_{43}<44.10\) and \(-0.06501<\partial_{q_{43}}\phi_{43}<-0.06497\) at \(q=1\). At the tie \(M_{43,43}=-2\sqrt2\,\partial_{q_{43}}\phi_{43}\in(0.1837,0.1840)\). The total positive correction has right derivative \(-\partial_y\phi_{43}/\partial_{q_{43}}\phi_{43}\in(678,679)\). The negative total is locally zero. The direct complex Jacobian uses the derivative of \(\sqrt{t/n}\) for the floor direction and puts the local product variation only at \(43\). At the lower rational endpoint, a separate computation of (4) and (4a) reconstructs \(J\) from both true even Fourier sectors. Its enclosures of the two phase derivatives overlap their direct complex Jacobian enclosures. [Checker](astra-contact-91-check.py) · [Outward records](astra-contact-91-checks.jsonl)

1. On the nominated cold ray apply (3) and (4) to the incoming physical derivative on actual largest signed coordinates. A prime-uniform pointwise bound on its path integral could preclude first contact. The Hilbert bound permits a large coordinate.
2. For near ties sharing a sign, test the compression in (5) on its zero-sum space. This identifies modes that can redistribute first corrections while preserving both totals. A cold section through all primes still requires an actual phase or higher-order contact bound.
