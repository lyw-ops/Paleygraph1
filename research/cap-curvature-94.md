# A scalar potential and the holomorphic defect of a clipped mark

The canonical marked logarithm of a genuine clipped stationary pair has an exact real potential. It satisfies one Cauchy–Riemann equation everywhere in the weak sense. The other equation has a local formula using the actual complex stationary response restricted to the positively corrected sites. If only one sign is corrected, the formula has a definite sign and is strictly nonzero whenever the marked product affects an active phase. This separates holomorphy of the physical marked scalar from the existence of a clipped row.

## A canonical differential in the cap and marked product

Use the normalized factors \(A,B\) of [round 93](rotated-cap-93.md), with marked product \(s=u+iv=n/t\) and bulk products \(q_i=1+e_i\). Let \(U_*=b+\theta,\ L_*=b-\theta\) be the unrotated phase boundaries. Write \(g_i=\frac12(\log A_i-\log B_i)\) for the physical log ratios and \(\phi_i=\Im g_i\). The positive real-part chart and phase intervals specify these lifts. The plus and minus sectors of the unrotated factors, including constants, are fixed. The common mean is \(M\).

Define the real function
\[
       \mathcal P=\sum_{i\ne0}\phi_i+\Im(sg_0).
\]
It is canonical on the genuine clipped family. Indeed the mark is fixed by the strict marked secant, and whenever two clipped factors differ at an unmarked site, their phases are the same saturated angle by the [signed rigidity argument](clipped-signs-90.md#the-exact-fourier-spaces-of-differences) in the same rotated chart. The compact chart argument of round 93 makes \(\mathcal P\) continuous locally in all of \(u,v,a=\tan\theta,\tan b\) on the open admissible set.

Complementary pairing of the tangents gives the exact identity
\[
 \sum_i (A_iB_i)\,dg_i
     =\tfrac12\sum_i(B_i\,dA_i-A_i\,dB_i)=0 .
\]
The two pairings on the right are both \(nM\,dM\). Taking imaginary parts and using the cap angles only where \(e_i>0\) proves
\[
 \boxed{\qquad
   d\mathcal P=\Im(g_0\,ds)-E_+\,dU_*-E_-\,dL_* .\qquad}            \tag{1}
\]
The formula extends across changes of active sites and nonuniqueness. For a straight line in the semialgebraic coordinates \(u,v,a,\tan b\), select genuine differentiable factors on the finite open pieces given by semialgebraic selection. Equation (1) holds there, and both its left-hand primitive and the displayed coefficients are continuous across the endpoints. Integrate piecewise and use the continuous coefficients to differentiate at arbitrary points. This gives a \(C^1\) primitive on the open admissible set, including possible breaks of the factors, and identifies its weak derivatives without choosing a single global factor branch.

For fixed caps and \(g_0=x+iy\) this says
\[
             \mathcal P_u=y,\qquad \mathcal P_v=x,\qquad x_u=y_v
\]
in the weak sense. In particular \(\partial_{\bar s}g_0\) is purely imaginary and
\[
             2\partial_{\bar s}g_0=i\Delta_s\mathcal P .             \tag{2}
\]
The primitive also retains the cap reciprocity and gives the mixed response to the true complex marked product. For example
\(\partial_u E_+=-\partial_{U_*}\Im g_0\) and
\(\partial_v E_+=-\partial_{U_*}\Re g_0\), with the lower-bound counterparts. These are distributional identities in the indicated variables.

## The true response on the corrected sites

At a genuine clipped row, temporarily regard its corrected products and \(s\) as independent complex variables. There is a genuine local holomorphic stationary branch in these products. Freeze \(b\) and use the rotated difference and sum. The derivative of the scalar product activation is \(\tanh(g_i-ib)\). Its modulus is strictly less than one at every coordinate, since all the shifted relative angles, including the marked relative angle, have magnitude at most \(\theta<\pi/4\). The linear map \(K-i\tan b\,P_1\) has complex Euclidean norm at most one, so the stationary Jacobian is invertible. The branch stays on the given local mean and log sheets.

In this local holomorphic branch let \(\mathcal A=\{i\ne0:e_i>0\}\) at the base row, and put
\[
  H_{ij}=\Im(\partial_{q_j}g_i),\quad i,j\in\mathcal A,\qquad
  c_i=\partial_s g_i=\partial_{q_i}g_0 .
\]
The complex symmetry of these derivatives follows by polarizing the two complementary tangent pairings, as in [round 93](rotated-cap-93.md#the-angular-work-inequality), now before taking imaginary parts. Thus \(H\) is real symmetric. Its entries include the true amplitudes, floor and corrected products.

At a differentiable selection of the actual clipped row at fixed caps, the variation of an uncharged \(q_i\) vanishes. Active phase derivatives vanish as well because their caps are fixed. Holding the real-axis parameter \(u\) or \(v\) in turn gives
\[
     Hq_u=-\Im c,\qquad Hq_v=-\Re c ,
\]
where \(q_u,q_v\) are restricted to \(\mathcal A\). Consequently \(c\) lies in the complexified range of \(H\), and the response of the mark is independent of the choice in its kernel. Substitution yields the local formula
\[
  \boxed{\qquad
        \Delta_s\mathcal P=-c^{*}H^\dagger c,\qquad
        \partial_{\bar s}g_0=-\tfrac{i}{2}c^{*}H^\dagger c .\qquad}   \tag{3}
\]
Here \(H^\dagger\) is the real symmetric inverse on the orthogonal complement of the kernel. In fact \(q_u+iq_v=-i H^\dagger\bar c\) up to its kernel, and the holomorphic partial derivative in \(s\) cancels from \(g_{0,u}+i g_{0,v}\). Formula (3) includes uncharged ties at the base point. On the open smooth strata the actual derivative is (3), and on their complement (2) still gives the weak equation.

Suppose all active sites have one sign \(\sigma\). Test the actual holomorphic differential with any real product perturbation \(h\) supported on \(\mathcal A\), holding \(s\) and the base rotation fixed, without imposing a cap on the perturbed row. The anisotropic loss calculation of round 93 applies to its first derivative at the base. Off \(\mathcal A\) its product derivative is zero and the scalar activation is nonexpansive there. At the active sites its phase derivative is \(Hh\); the two-sector tangent contraction then gives
\[
  -\sigma h^{\mathsf T}Hh\ \ge\
       \frac{1-a^2}{a}\sum_{i\in\mathcal A}q_i\,|(Hh)_i|^2 .
\]
Apply this to \(q_u,q_v\) and combine their equations. It follows that
\[
 \boxed{\qquad
   \sigma\Delta_s\mathcal P\ \ge\
        \frac{1-a^2}{a}\sum_{i\in\mathcal A}q_i\,|c_i|^2 .\qquad}     \tag{4}
\]
Thus the actual marked scalar is not holomorphic at a smooth one-sign row unless all the indicated sensitivities vanish. For two signs (3) instead supplies a precise signed cancellation test. Equality of the two total corrections alone gives no equality of the two signed Hessian contributions.

The sign statement has a weak form on each open region where the opposite sign is absent. Locally choose a compact coordinate rectangle within the positive chart. Each real component of the canonical marked factors is semialgebraic, by uniqueness of the marked factors and projection of the compact solution graph. Their positive real parts on the rectangle let one express the real part of \(g_0\) by logarithms of positive semialgebraic moduli and its imaginary part by differences of arctangents of real semialgebraic ratios. Along each coordinate line these functions are absolutely continuous. Indeed they are continuous and piecewise monotone and differentiable on finitely many intervals, and on each open interval the derivative integrates to the endpoint values by monotonicity and continuity. The number of pieces is locally uniformly bounded by semialgebraic cell decomposition. The resulting bounded line variations and Fubini identify the weak partial derivatives with their integrable almost-everywhere values. Hence (4) makes \(\mathcal P\) subharmonic on an upper-only region and superharmonic on a lower-only region. One can obtain the mean inequalities by mollifying on smaller rectangles and passing to the limit. If (3) vanishes almost everywhere on an open region, (2) gives distributional holomorphy of \(g_0\), hence ordinary holomorphy by the same mollification and local uniform convergence. This criterion concerns the marked scalar and allows nonzero local corrections.

## A common locally Lipschitz extension and a criterion for the theta limit

Use centered caps with \(a=1/\sqrt2\), let \(z=1/t\) so \(s=nz\), and fix the common cone \(\Omega=\{\Re z>0,\ |\Im z|<\Re z/200\}\). It satisfies the existence margin of round 93 at every field order. Write \(f_p(z)=g_0\) for its canonical clipped mark and \(P_p(z)=\mathcal P(nz)/n\) for its rescaled potential. Equation (1) becomes \(dP_p=\Im(f_p\,dz)\) at fixed caps, and
\[
                   2\partial_{\bar z} f_p=i\Delta_z P_p.            \tag{5}
\]
These extensions agree exactly with the original real positive stationary marks on the positive real axis: there \(v=0\) and the true positive pair itself is an uncorrected clipped row.

In fact \(f_p\) is uniformly bounded and Lipschitz on each compact subset of \(\Omega\), independently of the field. For boundedness use \(w_0\ge u\), the column norm bound of round 89, and its nonnegative clipped products. This gives \(\sum_B e_i\le (1+a^{-2})v^2/(4u)\). The exact mean identity \(nM^2=n-1+s+\sum_Be_i\) bounds \(|M|\) on a compact set of \(z\). With \(U=A-B\), \(S=A+B\) and zero center, \(U=KS\). All factor arguments have magnitude at most \(\theta\), including the mark. Thus \(\sum_i |S_i|\le 2n\sec\theta\Re M\) and the Jacobi entry bound gives \(|U_0/(2\sqrt s)|\le \sqrt{p/n}\sec\theta\Re M/\sqrt{|z|}\). Since \(U_0/(2\sqrt s)=\sinh g_0\) and the relative marked phase is at most \(|\arg z|/2\), the log is bounded on the compact set.

For two actual clipped rows at distinct \(z,z'\) in that set use the [centered scalar activation](astra-column-90.md#a-scalar-extension-and-fixed-point-rigidity) on the common bulk. Write \(\Delta U=U-U'\), \(\Delta S=S-S'\). Bulk nonexpansiveness and \(\Delta U=K\Delta S\) give \(|\Delta U_0|_a\le|\Delta S_0|_a\), where \(|x+iy|_a^2=a^2x^2+y^2\). Put \(m=(g_0+g'_0)/2\), \(d=(g_0-g'_0)/2\), \(A_s=(\sqrt s+\sqrt{s'})/2\), and \(e_s=(\sqrt s-\sqrt{s'})/2\), using the positive square-root sheet. The mark satisfies the exact secant identities
\[
 \Delta S_0-\tanh(m)\Delta U_0=4e_s\,\cosh d/\cosh m,\qquad
 \Delta U_0=4A_s\cosh m\sinh d+4e_s\sinh m\cosh d .                \tag{6}
\]
The anisotropic norm of multiplication by \(\tanh m\) is uniformly at most a constant \(L<1\). This follows from compactness of the marked log bounds and strict separation of the relative marked angle from the cap. The first identity implies \(|\Delta U_0|\ll |e_s|\). The second then gives \(|\sinh d|\ll |e_s|/\sqrt n\) since \(|A_s|\gg\sqrt n\) and \(|\cosh m|\) is bounded away from zero. The bounded imaginary phases give \(|d|\ll |\sinh d|\). Finally \(|e_s|/\sqrt n\ll |z-z'|\) on the compact set, proving the claim.

In particular, **distributional convergence \(\Delta_z P_p\to0\) on \(\Omega\) would prove ETH26**, without requiring exact removal of any finite-prime correction. Indeed, from any unbounded prime subsequence take a further subsequence whose marked extensions converge locally uniformly by the compact Lipschitz bounds. By (5) its limit is distributionally holomorphic and hence holomorphic. On the real interval \(0<z<1/1024\) the inherited large-floor bound makes this limit zero. The identity theorem therefore gives zero on all of \(\Omega\), and the real physical marks converge to zero at every fixed positive \(t\). The [stationary bracket](smoothing.md#fixed-point-and-a-sufficient-residual-estimate) bounds the error in the logarithm of the target ratio at that real \(t\) by \(\frac12\log(1+(1-1/n)t)\). First let \(p\to\infty\) and then \(t\downarrow0\). The distributional convergence remains unproved. The same criterion on a connected common domain reaching only one colder real interval would give vanishing marks on that interval, with the original limit requiring floors approaching zero. [Inherited hot bound](parallel-cold-complex-36.md)

On the reciprocal image \(D\) of the interior of the nominated square the [cap-independent action estimate](astra-center-94.md#oscillation-of-the-angular-action-and-the-separate-boundary-prices) gives a curvature bound in a weak norm. The action \(P_*\) from that estimate is the imaginary part of a holomorphic expression, with logs of the exact-product predictor and the unconjugated term \(\sum_iR'_i S_{Z,i}/4\). Its composition with \(t=1/z\) stays harmonic. Thus for every smooth \(\psi\) of compact support in \(D\),
\[
   \big|\langle\Delta_z P_p,\psi\rangle\big|
     \le 7\cdot10^6\sup_{z\in\operatorname{supp}\psi}
                \|R_{600}(1/z)/\sqrt{1/z}\|_{2,n}^{\,2}
                \|\Delta\psi\|_{L^1(D)} .                       \tag{7}
\]
This follows by integrating \((P_p-P_*(1/z)/n)\Delta\psi\). It gives second-order control of the true marked defect on \(D\). The current residual estimate has a fixed positive bound in the field-first limit, and \(D\) covers one cold neighborhood.

In a one-sign open patch of \(D\), (4) and (7) also give a positive sensitivity estimate. For a nonnegative smooth compactly supported test \(\psi\) in that patch, the integral against \(\psi\) of \(n(1-a^2)\sum_{i\in\mathcal A}q_i |c_i|^2/a\) is bounded by the same right side in (7). Here \(\Delta_z P_p=n\Delta_s\mathcal P\), and the weak sign conclusion before (5) permits switching sites of that sign inside the patch.

## Finite comparison and the missing prime estimate

At \(p=173\), \(t=1/50+13i/1000\), \(\tan\theta=1/\sqrt2\), \(b=0\), there is one positively corrected singleton at \(43\). The outward checker solves the underlying corrected-product holomorphic tangent equations, checks the reciprocal responses \(\partial_s g_{43}=\partial_{q_{43}}g_0\), and independently differentiates the real clipped fixed point in \(u\) and \(v\). The curvature in \(s\) lies between \(1.40892\cdot10^{-6}\) and \(1.40893\cdot10^{-6}\), proving marked nonholomorphy at a genuine prime on that small-real-part ray. The local calculation only uses the strict active branch at the sample. It makes no assertion of phase contact on the nominated cold square. [Checker](cap-curvature-94-check.py) · [Outward record](cap-curvature-94-checks.jsonl)

1. On a true balanced clipped survivor compare the two signed contributions in (3) using its actual two sign sets and the exterior minor return. Cancellation of the resulting curvature would be enough for a common marked holomorphic section without control of every factor.
2. Use (1)–(5) to estimate the normalized curvature distribution, first on one existing cold test rectangle and then on connected domains reaching the hot region and a sequence of colder real floors. The small known average correction has no proved relation to distributional vanishing throughout such domains.
