# Complex phases from a real marked projection

The actual unforced factors in the enlarged absolute sector determine a real positive stationary pair with depressed coordinate weights. The imaginary parts are an exact marked column of the weighted complementary projections of that real pair. Conversely the depressed weights solve a closed real system that reconstructs the complex factors. The same real reflection yields a signed Jacobian test with no hyperbolic amplitude multiplier at any bulk site. The weighted reflection and the phase mask still depend on the true row.

## The exact column and the real weight equations

Use the actual unforced factors \(A,B\) with \(A_iB_i=t\) on the bulk and \(A_0B_0=n\), in the two complementary real Fourier sectors plus constants. Write \(H_\pm\) for their mean-zero real sectors, with \(H_+\perp H_-\) and \(H_+\oplus H_-=\mathbf1^\perp\). Normalize both factors by \(\sqrt t\) and put
\[
 \mathcal A=A/\sqrt t,\quad \mathcal B=B/\sqrt t,\quad
 u+iv=n/t,\quad M=\sqrt{(n-1+u+iv)/n}.
\]
The letters \(u,v\) in this note are real scalars. Work on the positive mean sheet. For available rows in the enlarged absolute phase sector near the cold square, the real parts \(\alpha=\Re\mathcal A,\ \beta=\Re\mathcal B\) are positive. At the mark the relative phase acquires the additional common angle \(-\arg(t)/2\), which is small there. We henceforth require just positivity of these two real rows, along the chosen relative phase lifts.

Their product \(w=\alpha\beta>0\) is a real weight vector. Their means both equal \(m=\Re M>0\). They are the exact positive real stationary pair for \(w\). Indeed \(\alpha/m\) is feasible in the mean-one plus space, and the gradient of the corresponding real weighted log objective is opposite by \(w/\alpha=\beta\). Strict concavity gives uniqueness. Define
\[
 \nu_i=\sqrt{w_i},\qquad
 E_+=\operatorname{diag}(\sqrt{\beta/\alpha})H_+,\qquad
 E_-=\operatorname{diag}(\sqrt{\alpha/\beta})H_-,\qquad
 J_w=\Pi_+-\Pi_- .
\]
Here \(\Pi_\pm\) are Euclidean projections. The two spaces are orthogonal, span \(\nu^\perp\), and \(J_w\) is a real symmetric involution on \(\nu^\perp\) that kills \(\nu\). Orthogonality follows because the two diagonal scales are reciprocal. The vector \(\nu\) is orthogonal to each weighted space because the product with its diagonal scale is the opposite real sector row. This is the real weighted reflection of [the marked response](marked-response.md#weighted-complementary-projections) at the actual weights \(w\).

Write \(\mathcal A=\alpha(1+iD_A)\), \(\mathcal B=\beta(1+iD_B)\) with real diagonals, and put \(P=(D_A+D_B)/2,\ D=(D_A-D_B)/2\). On the bulk, their product is one, so
\[
 P_i=0,\qquad D_i=\tan\phi_i,\qquad w_i=\cos^2\phi_i,
\]
where \(\phi_i\) is the relative phase of the actual factor \(A_i\). At the mark \(v=2w_0P_0\). For \(\xi=\Im M/\Re M\) the imaginary rows minus \(\xi\) times the real rows are in the respective mean-zero sectors. Consequently \(\nu(P-\xi)+\nu D\in E_+\), \(\nu(P-\xi)-\nu D\in E_-\), and
\[
       \boxed{\ \nu_iD_i=\frac{v}{2\sqrt{w_0}}(J_w)_{i0}\ }.          \tag{1}
\]
Here \(\xi\) cancels under \(J_w\). In particular a bulk phase excursion is entirely a marked-column phenomenon for a real stationary problem. For \(v=0\) the phases in this positive real-part chart are zero, giving the actual real stationary pair.

Put \(c_i=(J_w)_{i0}\). Equivalently the weights of a genuine complex row solve
\[
 w_i=1-\frac{v^2}{4w_0}c_i^2\quad (i\ne0),\qquad
 w_0=\frac{u+\sqrt{u^2+v^2(1-c_0^2)}}{2}.                           \tag{2}
\]
The scalar \(u\) is positive in the right half-plane. For the marked equation use
\(u=w_0(1-P_0^2+D_0^2)\) and \(D_0=P_0c_0\). On the physical cold square the necessary tail of the actual phases is exactly the tail of \(c_i\) at thresholds proportional to \(1/(\sqrt n |\Im t|)\), by (1). This retains both signs of \(c_i\), with no absolute-value estimate on the original Jacobi kernel. At the mark,
\[
                \sin(2\phi_0)=-c_0\sin(\arg t).
\]
This follows by taking the ratio of the difference and sum of the two tangents at angles \(\phi_0-\arg(t)/2\) and \(-\phi_0-\arg(t)/2\), or directly from the real and imaginary parts of their product. The identity also holds at real \(t\) by the preceding conclusion.

Conversely, let a strictly positive real weight vector solve (2), with \(J_w\) built from its unique equal-mean positive pair \(\alpha,\beta\). Set \(P_0=v/(2w_0)\), \(P_i=0\) off the mark, and define \(D\) by (1). If \(S=\sum_iw_i\), then the column norm satisfies \(\sum_i c_i^2=1-w_0/S\), as \(J_w^2\) is the projection onto \(\nu^\perp\). Summing (2) gives
\[
                 S=n-1+u+\frac{v^2}{4S}.
\]
Thus \(m=\sqrt{S/n}=\Re M\) and \(\xi=v/(2S)=\Im M/\Re M\). The weighted vector \(\nu(P-\xi)\) belongs to \(\nu^\perp\), and \(\nu D=J_w[\nu(P-\xi)]\). Therefore \(\alpha[1+i(P+D)]\) and \(\beta[1+i(P-D)]\) are in the required sectors, have common mean \(M\), and their coordinate products are one on the bulk and \(u+iv\) at the mark. This reconstructs the normalized complex factors in the positive real-part chart. A positive solution of the real system has not been shown to exist uniformly in \(p\) at the nominated complex floors.

## An everywhere positive clipped construction

Fix \(\kappa>0\) and replace the bulk equation in (2) by
\[
       w_i=\max\{1-Bc_i^2,\ \kappa Bc_i^2\},\qquad
       B=\frac{v^2}{4w_0}.
\]
Keep the marked equation unchanged. This always has a positive solution at each field. In fact the right sides define a continuous self-map of the box
\[
 [u,(u+\sqrt{u^2+v^2})/2]\ \times\
       [\kappa/(1+\kappa),\max(1,\kappa v^2/(4u))]^{n-1}.
\]
Continuity of \(J_w\) on positive real weights follows from the strictly negative definite real log Hessian in the mean-zero sector. The marked interval is invariant since \(|c_0|\le1\). The bulk intervals use \(\min_{z\ge0}\max(1-z,\kappa z)=\kappa/(1+\kappa)\) and \(|c_i|\le1\). Apply the Brouwer fixed point theorem. The map preserves evenness, so it also has a fixed point in the even sub-box.

Write \(e_i=((1+\kappa)B c_i^2-1)_+\) on the bulk. Then
\[
       w_i+B c_i^2=1+e_i,\qquad
       \sum_{i\ne0}e_i\le(1+\kappa)B,\qquad
       \#\{i:e_i>0\}\le(1+\kappa)B.
\]
The two bounds use \(\sum_i c_i^2\le1\). The converse construction of (2) applies with the bulk products \(1+e_i\). Indeed summing gives \(S=n-1+\sum_{i\ne0}e_i+u+v^2/(4S)\), and the common mean is the positive sheet of the corresponding product sum. The physical products after multiplying both factors by \(\sqrt t\) are therefore \(t(1+e_i)\) on the bulk and \(n\) at the mark. These are exact complementary factors for this perturbed floor. By construction \(|D_i|\le\kappa^{-1/2}\) on the bulk, so the absolute bulk phase is at most \(\arctan(\kappa^{-1/2})\). On a fixed cold square, \(B\le n y^2/(4x^3)\) since \(u=n x/|t|^2\) and \(v=-n y/|t|^2\).

The floor correction vanishes if the marked column at the clipped fixed point obeys \(B c_i^2\le1/(1+\kappa)\) at every bulk site. For \(\kappa>1\) on the cold square the reconstructed original factors then have all absolute phases strictly below \(\pi/4\), including the mark since \(|D_0|,|P_0|\le |v|/(2u)\) and \(|\arg t|\) is small. If such a fixed point exists at every floor in a common open tube over a real interval, strict phase uniqueness and the regular Jacobian below glue the original factors holomorphically there. At real floors they coincide with the positive pair. In particular a prime-uniform \(O(n^{-1/2})\) bound on the bulk marked column of one clipped fixed point per floor would suffice upon narrowing the tube by a fixed amount, since \(B\ll n y^2\) on the cold square. The construction is pointwise in the floor. The marked-column upper and absence of positive corrections remain open.

## Pure phase Jacobian with an exact marked correction

Consider an unforced logarithmic kernel direction \(\omega\) at a fixed solution in this chart. Equivalently \(\mathcal A\omega\in H_+\otimes\mathbb C\), \(\mathcal B\omega\in H_-\otimes\mathbb C\), since the mean sheet is fixed. Put \(X=\nu\omega\), \(Y=(1+iP)X\). The two tangent constraints say
\[
  Y+i D X\in E_+\otimes\mathbb C,\qquad
  Y-i D X\in E_-\otimes\mathbb C.
\]
They are exactly \(Y\in\nu^\perp\otimes\mathbb C\) and \(J_wY=i D X\). Hence every kernel direction satisfies
\[
        Y=i J_w D(1+iP)^{-1}Y.                                    \tag{3}
\]
The bulk multiplier in (3) is \(\tan\phi_i\); a large real amplitude alone cannot make that multiplier large. All amplitude dependence is retained in the real orthogonal reflection, rather than in a bulk diagonal hyperbolic derivative. The argument uses the factor chart on the stated positive real-part domain.

Keep indices with \(D_i\ne0\). With \(C=|D|^{1/2}J_w|D|^{1/2}\), equation (3) forces a nonzero vector \(V=|D|^{1/2}(1+iP)^{-1}Y\) satisfying
\[
        (I+iP-i C\,\operatorname{sign}D)V=0 .
\]
Indeed if \(V=0\), (3) gives \(Y=0\). Split into the two signs of \(D\). Write
\[
 B_+=I+i(P_{++}-C_{++}),\qquad B_-=I+i(P_{--}+C_{--}).
\]
Each diagonal block is identity plus \(i\) times a real symmetric matrix, so its inverse has norm at most one. The exact Schur equation for this necessary kernel is
\[
        V_-=B_-^{-1}C_{-+}B_+^{-1}C_{+-}V_-.                       \tag{4}
\]
Thus Schur norm below one suffices for regularity of the actual factor Jacobian, including the even restriction when the actual row is even. The easier test is \(\|C_{+-}\|<1\), and a single nonempty sign block is always regular. The real diagonal \(P\) retains the full marked weight-angle defect in the blocks and incurs no norm penalty there.

In fact an eigenvalue \(1\) in (4) is equivalent to a true factor kernel. Reconstruct \(V_+=-iB_+^{-1}C_{+-}V_-\) and \(Y=iJ_w\operatorname{sign}(D)|D|^{1/2}V\). The two block equations recover \(V=|D|^{1/2}(1+iP)^{-1}Y\), so \(Y\ne0\). Put \(X=(1+iP)^{-1}Y\) and write the projection of \(DX\) on the line of \(\nu\) as \(z\nu\). Then \(Y\perp\nu\), \(J_wY=i(DX-z\nu)\), and \(Y\pm iDX=(I\pm J_w)Y\pm iz\nu\). Undoing the real diagonal scalings thus puts \(\dot{\mathcal A}=\mathcal A X/\nu\) and \(\dot{\mathcal B}=-\mathcal B X/\nu\) in the two sectors plus constants, with equal means \(izm\). Their product derivative vanishes coordinatewise. Pairing both derivatives with the true opposite factors gives \(0=2nMizm\), hence \(z=0\). This restores the exact tangent constraints. The argument also works in the even restriction.

## Comparing the real reflection with the true real floor

Write \(t=x+iy\) in the cold square and use unrotated normalized factors as above. Let \(w^0\) have bulk weights one and mark \(n/x\), and let \(J_{w^0}\) be the real weighted reflection of the genuine real stationary pair at \(x\). On the bulk \(w_i=\cos^2\phi_i\le w_i^0\). At the mark
\[
 w_0=\frac n{|t|}\cos(\phi_0-\arg(t)/2)\cos(\phi_0+\arg(t)/2)
      \le n/x.
\]
Both weights are uniformly comparable coordinatewise throughout the enlarged absolute sector of the cold square.

For a real positive pair with arbitrary positive weights, the weighted speed identity in [the marked response](marked-response.md#weighted-complementary-projections) bounds the Euclidean norm of \(\sqrt w\dot\gamma\) by \(\|\dot{\sqrt w}\|_2\), where \(\gamma=(\log\alpha-\log\beta)/2\). Apply this along the straight segment of the square roots of \(w^0,w\). Comparability of each intermediate weight to \(w^0\) yields
\[
 \|\sqrt{w^0}(\gamma(w)-\gamma(w^0))\|_{2,n}
  \ll \|\sqrt w-\sqrt{w^0}\|_{2,n}
  \ll \big(E_{\rm bulk}\sin^4\phi+|y|^4\big)^{1/2}.                 \tag{5}
\]
The last step uses \(1-\cos\phi\le\sin^2\phi/(1+\cos\phi)\) and the marked sector estimate \(\phi_0=O(|y|)\); constants are absolute on the fixed square. Off the mark \(\gamma(w)=\Re z_i(t)\). At the mark \(\gamma(w)-\Re z_0(t)\) is half the log of the displayed quotient of the two cosines, of order \(O(y^2)\). In particular (5) also bounds the actual real mark displacement from \(x\) by \(O((E_{\rm bulk}\sin^4\phi)^{1/2}+y^2)\), with a constant uniform through primes.

The same bound applies to the normalized Hilbert–Schmidt difference of the two real reflections:
\[
 n^{-1/2}\|J_w-J_{w^0}\|_{\rm HS}
       \ll (E_{\rm bulk}\sin^4\phi+|y|^4)^{1/2}.                   \tag{6}
\]
To see this, the two plus subspaces are images of each other by the positive diagonal with log \(-[\gamma(w)-\gamma(w^0)]\), and the two minus subspaces have the reciprocal diagonal. For any real diagonal \(L\) and any subspace, projection \(Q(s)\) onto its image under \(e^{sL}\) satisfies
\(Q'(s)=(I-Q(s))LQ(s)+Q(s)L(I-Q(s))\). This follows by differentiating the projection written as \(B(B^{\mathsf T}B)^{-1}B^{\mathsf T}\) for a basis \(B\) with \(B'=LB\). The Hilbert–Schmidt norm of the off-diagonal blocks is at most \(\|L\|_{\rm HS}\). Integrate and apply (5) with the lower positive floor of \(w^0\). By the actual angular budget the right side in (6) is \(O(|y|)\), and its sharper fourth-phase dependence stays visible.

There is also a rank-local version. If the relative diagonal log difference is set to zero outside a set \(S\), the projection update for either sector has range in \(\operatorname{span}\{e_i,Q(0)e_i:i\in S\}\). For a vector orthogonal to this span, both its projection and its orthogonal residual vanish on \(S\), so the first is still in the changed subspace and the second is still orthogonal to it. This can isolate the influence of actual large relative log changes when testing (4) against the real reference. No operator-norm smallness of the reflected cross compression follows from the normalized bound (6) alone.

At \(p=173\) the [outward interval checker](real-phase-projection-89-check.py) uses the real-start branch of [round 86](astra-phase-86.md). It reconstructs the real weighted reflection on the 44 even orbits from true Fourier sectors, checks the column identities and the weight equations, and certifies the even Schur norm below \(0.107\) at \(t=1/50+0.02161i\) and \(0.110\) at \(t=1/50+0.022i\). Both points are beyond first spread contact. The norm certificates use a midpoint preconditioner and explicit interval perturbation bounds. These points concern the even factor Jacobian at the stated finite prime. [Outward records](real-phase-projection-89-checks.jsonl)

1. On the positive real pair in (2) or at the clipped fixed point bound the higher moments or the large coordinates of the marked reflection column. A uniform bulk bound below the clipping threshold gives the original factor equations with a strict phase margin.
2. Test whether the rank-local update and the genuine real weighted reflection suffice to control the signed Schur return (4) on the actual opposite phase sites. The needed uniform estimate beyond first contact and the prime common domain remain open.
