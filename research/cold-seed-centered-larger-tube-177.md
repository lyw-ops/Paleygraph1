# Ten actual cold steps at the same logarithmic cutoff

Keep the original closed square, the true height-602 row, both lifts and \(t_0=n\). The radius-\(0.05\) estimate of [Round 174](cold-first-prefix-step-174.md) used scalar curvature about \(V_{602}\). Seed-centered geometry gives a radius \(3/8\) about the same center with the counting contraction needed for the same cutoff.

## Scalar derivative on the enlarged tube

The physical radius bound through height 600 in [Round 88](astra-source-88.md) and the next two actual increment bounds of [Rounds 126 and 162](cold-height-602-frozen-kernel-162.md) give, for the real Jacobi seed \(S=2\sqrt nK e_0\),
\[
 \|S\|_\infty<s_*=2.828428,\qquad
 \|V_{602}-S\|_\infty<1.94+0.011+0.012=1.963
\]
for all sufficiently large eligible primes. At any point \(z=x+iy\) in a coordinate disk of radius \(3/8\) about \(V_{602,i}\), we have \(|z-S_i|\le B=2.338\). Put \(u=\sqrt{1-y^2/B^2}\) and
\[
 A(u)=s_*^2+B^2+2s_*Bu,\quad
 C(u)=N-2B^2(1-u^2),\quad N=4(2031/128-2^{-17}).
\]
Then \(|z|^2\le A(u)\) and \(\Re(4t_i+z^2)\ge |z|^2+C(u)>0\), including the mark since \(t_0=n\). The squared derivative is at most \(A/(A+C)\). As in Round 88,
\[
 A'C-AC'\ge 2s_*B(N-2B^2)-4B^2(s_*+B)^2>0 .
\]
The maximum is at \(u=1\), where \((s_*+B)^2/(N+(s_*+B)^2)<(0.545)^2\). Thus the exact nonlinear map has counting Lipschitz rate at most \(q=0.545\) on this convex polydisk, using \(\|K\|_{2\to2}\le1\). The physical sheets extend on the disks by the positive radicand margin. The exact inequality \(q^8<2^{-7}\) preserves the conditional tail after \(602+\lceil(4/7)\log_2 n\rceil\).

## The true first ten displacements

Write \(U_j=V_{602+j}-V_{602}\). When \(P_{5000}(U_j)\le3/8\), the Round 174 post-\(K\) Taylor estimate has dimension at most \(M=4.823+3/8=5.198\) through the segment. Setting \(x_*=M^2/N<1\), the rational check
\[
 4(1+x_*/2)^2<(1.22)^2N(1-x_*)^5
\]
bounds the leading coefficient of \(P_{5000}(U_j)^2\) by \(1.22\) with strict slack. Absorb the vanishing bad-character and physical mark corrections of the same estimate for all sufficiently large eligible primes. The known outgoing source and frozen linear price give
\[
 P_{5000}(U_{j+1})<0.01272+1.066P_{5000}(U_j)+1.22P_{5000}(U_j)^2 .
\]
Starting at zero and rounding upward, the rational upper bounds in units of \(10^{-5}\) are
\[
 1272,\ 2648,\ 4181,\ 5943,\ 8039,\ 10631,\ 13984,\ 18565,\ 25268,\ 35998.
\]
All the inputs are inside the radius \(3/8\), and the packet bounds dominate coordinate displacement. Thus the true fixed prefix through \(V_{612}\) stays inside these disks with uniform clearance. In particular a fixed-strict upper \(\|R_{611}\|_2<0.0556556=(3/8-0.25268)(1-q)\) in the unnormalized counting second norm would close the subsequent tail directly by the same first-exit argument. This source bound, the actual growing prefix, and signed derivative transfer still need proof. The fixed-depth mathematical estimate uses rational comparisons, with no new outward interval computation.
