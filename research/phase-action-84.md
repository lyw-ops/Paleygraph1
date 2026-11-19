# Relative-phase action along the true cold forcing segment

On the complex square about \(2031/128\), start the forcing homotopy at the actual height-600 physical predictor. Along its real forcing parameter, up to exit from the relative-phase tube, an exact secant identity controls the accumulated phase excursion uniformly through primes. The limiting fraction of bulk sites that ever reach relative phase magnitude \(\pi/6\) is below \(3.1\cdot 10^{-414}\) on this segment. This is a statement about normalized counting measure. A set of vanishingly small fixed upper density can still contain sites where the section cannot continue.

## Exact secant comparison in logarithmic coordinates

Let \(t\) belong to the closed round-83 square \(Q\), and let \(n\ge10^{30}\). Put \(t_0=n\), and \(t_i=t\) on the bulk. Write \(K\) for the actual physical coisometry, \(\mathbb E\) for the counting mean, and \(\|\cdot\|_2\) for the normalized counting second norm. Use \(X=V_{600}(t)\), \(R=K\Phi_t(X)-X\) and the actual equation
\[
 U(\lambda)=K\Phi_t(U(\lambda))-(1-\lambda)R,\qquad U(0)=X.
\]
At the root of this homotopy the derivative of the activation in each coordinate has modulus below \(0.55\), so the local branch exists. Work on its maximal initial real parameter segment within \(0\le\lambda\le1\) and the tube
\[
 z_i=\operatorname{arsinh}\bigl(U_i/(2\sqrt{t_i})\bigr),\qquad
 |\phi_i|<\pi/4,\qquad \phi_i=\Im z_i.
\]
Here \(\sqrt{t_i}\) has positive real part and the branch of \(z\) starts from the bounded predictor. In the tube \(U_i=2\sqrt{t_i}\sinh z_i\) and \(\Phi_t(U)_i=2\sqrt{t_i}\cosh z_i\) on the continuing branches. This is the relative factor coordinate \(z_i=\log((\Phi_t(U)_i+U_i)/(2\sqrt{t_i}))\).

The actual predictor estimates give \(\|X\|_\infty<4.768\), \(\|\Im X\|_\infty<2\), and \(\|R\|_\infty<0.011\). The first two are the height-600 packet bounds of round 76. For the last use the interval bound for \(V_{601}-V_{600}\) in the physical norm of round 82, which dominates the coordinate sup. No finite-field size upper bound is used in these three estimates. [Actual predictor](astra-predictor-76.md#a-finite-comparison-for-the-complete-nine-center-predictor) · [Outgoing residual record](astra-adjoint-82-checks.jsonl)

Put \(w_i=z_i(0)\). For every coordinate, \(|\sqrt{t_i}|>3.98\), \(|\arg\sqrt{t_i}|<10^{-6}\), \(|\sinh w_i|<0.6\), and \(|\Im w_i|<0.26\). Indeed the branch at zero has imaginary part in \((-\pi/2,\pi/2)\) and
\[
 |\sin\Im w_i|\le |\Im(X_i/(2\sqrt{t_i}))|
      \le (2+4.768\cdot10^{-6})/(2\cdot3.98)<\sin(0.26).
\]
The last strict inequality follows already from \(\sin x\ge x-x^3/6\) on this real interval. Also \(e^{|\Re w_i|}\le\sqrt{1+0.6^2}+0.6<1.77\). On the tube, for \(\Delta=U-X\), the exact coordinatewise secant is
\[
 \Phi_t(U)_i-\Phi_t(X)_i=D_i\Delta_i,\qquad
 D_i=\tanh\bigl((z_i+w_i)/2\bigr).
\]
The hyperbolic addition formulas prove this also when a secant denominator vanishes. Now \(\cos(\Im z_i+\Im w_i)>1/2\) since \(0.26<\pi/12\), and
\[
 \begin{split}
 1-|D_i|^2
 &=\frac{\cos(\Im z_i+\Im w_i)}
          {|\cosh((z_i+w_i)/2)|^2}\\
 &\ge\frac{1}{10+|\Delta_i|}.
 \end{split}
\]
For the last inequality, bound the denominator above by
\(e^{|\Re w_i|}e^{|\Re z_i|}\le1.77[1+(4.768+|\Delta_i|)/3.98]\).
In particular \((1-|D_i|^2)|\Delta_i|^2\ge \min(|\Delta_i|^2,|\Delta_i|)/11\).

Subtract the two physical equations and use \(K^*K=I-J\), with \(J\) the mean projector. At \(h\in[0,1]\) in the segment this gives
\[
 \mathbb E(1-|D|^2)|\Delta|^2+|\mathbb E(D\Delta)|^2
       =2h\Re\mathbb E(\overline\Delta R)-h^2\|R\|_2^2 .
 \tag{1}
\]
On \(|\Delta|\le1\), bound the first term on the right sitewise by
\(|\Delta|^2/22+22h^2|R|^2\). On \(|\Delta|>1\), use
\(2h\|R\|_\infty|\Delta|\le|\Delta|/22\).
Subtracting the negative squared forcing term gives
\[
             \mathbb E\min(|\Delta|^2,|\Delta|)\le 462 h^2\|R\|_2^2.       \tag{2}
\]
This is a prime-uniform complex secant bound on the remaining genuine forcing path and also holds on the unconstrained real path, where the phase is zero.

## Integrated tangent action and the sites that ever reach a large phase

Let \(H=\partial_\lambda U\). Differentiate the actual equation to get \(H-K\Phi'_t(U)H=R\). Apply \(K^*K=I-J\) again, and use \(\Phi'_t(U)_i=\tanh z_i\) and \(H_i=2\sqrt{t_i}\cosh z_i\,z_i'\). The exact identity is
\[
 \mathbb E\,4|t_i|\cos(2\phi_i)|z_i'|^2+
       |\mathbb E(\Phi'_t(U)H)|^2
       =2\Re\mathbb E(\overline H R)-\|R\|_2^2 .
 \tag{3}
\]
Integrate over \(0\le\lambda\le h\). On the right the first term integrates to \(2\Re\mathbb E(\overline{\Delta(h)}R)\). By (2) the absolute value of \(\mathbb E(\overline{\Delta(h)}R)\) is at most
\[
       (\sqrt{462}+0.011\cdot462\,h)h\|R\|_2^2 ,
\]
by applying Cauchy--Schwarz below \(|\Delta|=1\) and the sup bound on \(R\) above it. Thus the integrated left side of (3) is at most \(54 h\|R\|_2^2\). In particular, since \(4\inf_i |t_i|>54\),
\[
        \mathbb E\int_0^h\cos(2\phi_i)|z_i'|^2\,d\lambda
                     \le h\|R\|_2^2.                       \tag{4}
\]
Write \(L(\phi)=\int_0^\phi\sqrt{\cos(2u)}\,du\). It is real and increasing in the tube. At each site and for every real \(\lambda\le h\),
\[
 |L(\phi_i(\lambda))-L(\phi_i(0))|^2
      \le h\int_0^h\cos(2\phi_i)|z_i'|^2\,d\lambda .
\]
The same estimate therefore holds for the maximum over the segment at this site. The increase in \(L\) between \(0.26\) and \(\pi/6\) is at least \((\pi/6-0.26)/\sqrt2\), whose square exceeds \(1/32\). Consequently the **union over the whole segment** satisfies
\[
 \frac{\#\{i:\sup_{0\le\lambda\le h}|\phi_i(\lambda)|\ge\pi/6\}}{n}
                     \le 32 h^2\|R\|_2^2 .                \tag{5}
\]
The limiting complex normalized residual of this actual predictor is uniformly below \(3.06\cdot10^{-208}\) on \(Q\) by the angular prime-aspect estimate in round 80. Thus the limsup of (5), over primes and uniformly over the available initial segments and \(t\in Q\), is below \(3.1\cdot10^{-414}\). The estimate uses the field-first residual proof, with no effective field threshold from its improved rate. [Actual angular residual estimate](astra-dissipation-80.md#the-nonlinear-nine-center-secants)

The root has extra leverage in (3) because \(|t_0|/n=1\). Its integrated action is at most \(13.5 h\|R\|_2^2\), while \(|\phi_0(0)|<2/\sqrt n\). The same Cauchy--Schwarz argument shows that the root cannot reach \(0.05\) in absolute phase on this segment: the required change in \(L\) exceeds \(0.049\), while \(\sqrt{13.5}\|R\|_2\le\sqrt{13.5}\cdot0.011<0.041\). Since \(\cos(2\phi_0)>0.99\), it also gives
\[
          |z_0(h)-z_0(0)|\le4h\|R\|_2 .
\]
This part is a bound on the genuine continued marked log in the tube, distinct from the counting estimate on bulk sites.

## What the action leaves to prove

For each fixed field, (2) gives a finite coordinate cap as long as the trajectory stays in the tube. If an initial segment ends before \(\lambda=1\), any cluster point strictly inside the tube would admit the local implicit continuation, since then \(\|\Phi'_t(U)\|_\infty<1\). Thus a failure to continue inside the tube must meet its boundary. This also justifies the whole real-segment assertion when \(t\) is positive real. The initial row and all local real-parameter continuations are real, so their relative phases stay zero.

At a boundary cluster point the derivative still has modulus at most one. If \(I-K\operatorname{diag}\Phi'_t(U)\) is singular there, equality in the Euclidean contraction implies its kernel vector is supported on the sites \(S\) with \(|\phi_i|=\pi/4\). Its restriction solves the corresponding equation with the compressed matrix \(K_{SS}\). In particular singularity requires \(\|K_{SS}\|_{2\to2}=1\), and the elementary Jacobi coherence bound gives \(|S|\ge n/\sqrt p\). These sites belong to the union in (5). The upper fraction in (5) is a fixed positive tolerance and allows this many exceptional sites at arbitrarily large \(n\).

The action and the marked bound leave continuation at the original \(\lambda=1\) open. The exact identities apply to any recentering with the stated three physical caps, including when its actual normalized residual is much smaller than the bound used for the sup of the forcing.

1. Use (5) to estimate the actual compressed return on the union of sites approaching the critical phase. Compare its spectral radius in the signed linear equation to the loss of the good coordinates. The absolute number of exceptional sites can grow with \(n\).
2. Recenter at a predictor whose normalized residual tends to zero through primes while maintaining the bounded initial log phase and the small forcing sup. Then use (1) and (3) to track whether remaining singular behavior is confined to an independently controllable set.
