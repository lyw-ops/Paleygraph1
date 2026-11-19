# Mixed old returns with arbitrary residual siblings

At the fixed limiting seed of round 58 and real floor \(2031/128\), a quadratic tagged return cancels part of the signed Jacobi multiplier on **every single residual sibling**. The per-sign saving per unit sibling measure is between \(39.925516\) and \(39.936273\) billionths. Allowing arbitrary sibling counts and every old return of the three independent tagged fields, including their signed Jacobi shifts, still gives an escaping packet recursion. Its certified mass exceeds 21 at height 2165 and diverges thereafter.

Independently, for every sufficiently large eligible prime and prime square the actual common stationary section extends to
\[
 1040026/65536<\Re t<1040036/65536,\qquad |\Im t|<1/1048576,
 \qquad |m_q(t)|\le 3/\sqrt n.
\]
This connects on an open overlap to round 58 at \(1040034/65536\). Its left endpoint remains above \(2031/128\).

## The signed coefficient with residual siblings

Write \(H_j=[y^j]\sqrt{4t+(V+y)^2}\) in the fully collected old arithmetic character ring, using the four distinguished amendments in \(H_0\). On odd levels identify the actual fixed arity-zero outputs
\[
 T=v(U+U')+w(D+D^\vee)+zR,\qquad B=u(A+B')
\]
with the conventions and coefficients of rounds 59 and 60. Here \(U,U'\) are the independent \(Sp_4\) standards, \(D\) is the \(SL_4\) standard on its arithmetic determinant coset and \(R\) is the \(Sp_8\) standard. Put \(p_h=\mathbb E[T^h\mid\mathrm{old}]\), a virtual character of the Jacobi torus. Fix a list of \(r\) surviving residual siblings outside the distinguished \(T\) leaves, of any origin. Collect their old multiplier from configurations with \(h\) additional tagged children **before** taking the modulus. It is
\[
 S_r=\sum_{h\ge0}{r+h\choose h}p_h H_{r+h}.
\]
Each ordered list of residual children has exactly the displayed number of interleavings with the tagged block. After pooling multiply by the unsigned boundary convolution of the \(r\) residuals, preserving the identities of the fixed tags until this operation. The residuals may include \(B\). For \(r=1\) and the specific residual \(B\), pool \(B S_1\) with \(S_0\) as in the preceding unary grouping. Other residual lists stay separately charged. For nontrivial new sectors retain the original disjoint tree charges. Apply this rule on disjoint pairs of levels.

The conditional projections have \(p_0=1\), all odd terms zero and
\[
 p_2=C=2v^2+2w^2+z^2,\qquad
 p_4=3C^2+w^4(m^4+m^{-4}).
\]
For the symplectic standards the quadratic and quartic moments are one and three. For the dual pair the six ordered balanced words each have two invariant contractions. The two pure fourth powers contribute the actual determinant and inverse determinant. Central sign symmetry and independence dispose of odd exponents. In particular for an old derived label \(\lambda\) and signed Jacobi exponent \(e\), its quartic contribution to \([\lambda m^e]S_r\) is
\[
 {r+4\choose4}\left(3C^2[\lambda m^e]H_{r+4}
      +w^4[\lambda m^{e-4}]H_{r+4}+w^4[\lambda m^{e+4}]H_{r+4}\right).
\]
Both determinant phases are positive. In higher degrees the definition pools the full arithmetic old character, including every shift. [Arithmetic groups and phases](astra-rankeight-60.md) · [Determinant of the dual pair](two-node-groups-59.md)

For \(r=1\), the trivial derived label at either \(e=\pm1\) has \([m^e]H_1>0.169624\), while the new signed evaluation gives
\[
 -0.001117085<[m^e]H_3<-0.001116787.
\]
The cubic return \(3C[m^e]H_3\) therefore cancels part of the unary Jacobi coefficient. Pooling these two channels saves exactly \(-6C[m^e]H_3\) per sign before multiplication by the residual boundary measure. This saving applies to a residual carried as an unsigned independent list. It is also a valid first grouping for the special \(B\) list. For the cubic coefficient the degree-20 polynomial extracts the signed Jacobi line by the determinant/tableau calculation of round 59. The first omitted term of the arity-three absolute Taylor majorant at seed dimension \(M\) is multiplied by \((1-\rho)^{-1}\), with \(\rho=(M^2/4t){24\choose3}/{22\choose3}<1\). Each subsequent ratio decreases. Schur orthogonality bounds an individual character coefficient by this uniform tail. [Full old character projection](astra-crossnode-59.md)

## A lower substitution that does not bound the true iterate from above

Let \(b\) denote the symmetric boundary measure associated to the retained lower packets on an odd level, and \(T_*,B_*\) the unsigned **exact** fixed tagged measures. The true previous measure dominates \(b\) and contains the disjoint tagged contributions. Its untagged part dominates
\[
 R_*=(b-T_*-B_*)_+ .
\]
Use the surrogate \(R_*+B_*+T_*\) on the grouped level. It dominates \(b\). Its residual outside \(T\) is bounded above by \(b+B_*\). After taking absolute values at the prescribed grouped multipliers the map is positive in the untagged packet measure. This proves that the surrogate gives a lower bound for the full grouped update. Atomwise thinning is legitimate at this stage because each residual list propagates by the same unsigned convolution after its multiplier is fixed. No upper bound on the true previous mass is needed.

On the surrogate, take the ordinary lower output from \(b\) through old arity nine and shifts through 18, and remove twice the following upper charges. For a residual count \(r\) remove the absolute upper measure of
\[
 \sum_{h\ge2}{r+h\choose h}H_{r+h}p_h
\]
convolved against \((b+B_*)^{*r}\). This pays once for the old projected charge previously counted in higher original arities and once for the possible reduction of its direct competitor. For \(h=2,4\), an old summand needs even multiplicity of each symplectic standard and even total dual-pair degree. Both determinant phases are positive, so each old return has constructive signs before pooling with other degrees. Thus its original separated old charge has exactly the same weight measure as the displayed positive return polynomial. At all \(h\ge6\) use the full original tagged mass, which bounds every signed collection and its separated charge. For \(r=0\), also debit the previous full unary-on-\(B\) loss. The two leading unary terms reinforce their direct competitors. These debits apply even if new terms subsequently meet those competitors. Terms with \(r>9\) occur exclusively in original arities beyond the retained range. Their whole grouped output is nonnegative and uses a separate residual list. This discards no contributor to a retained old competitor.

In the implementation, the polynomial kernels \(U_j\) are the inherited degree-28 absolute upper measures, taken per sign. For arities two and four of the tagged block use the exact shift formula above with the traced coefficient bounds. For larger even \(h\), the total charge of the polynomial remainder is bounded by
\[
 \sum_{6\le h\le 28-r,\ h\text{ even}} {r+h\choose r}\|U_{r+h}\|_1 d^h,
 \qquad d=8(|v|+|w|+|z|)<0.028.
\]
The analytic tail beyond degree 28 at auxiliary radius two has total mass \(E\) bounded by the first omitted binomial times its geometric tail at \((M+2)^2/(4t)\). Its arity-\(j\) coefficient has mass at most \(E/2^j\). For the block with \(h\ge6\) sum this using ratio bound \((d/2)(1+r/7)<1\), allowing every integer \(h\). At \(h=2,4\) use their exact return masses against the corresponding analytic arity bounds. For old root shifts outside the retained strip bound each single atom by the largest off-strip atom, then multiply by the total residual convolution mass. The residual debit is thus valid in every output bin, including when old shifts cancel large sibling weights. Finally combine the two signs, take the positive part and retain 28 packets. The Arb192 run exceeds mass 21 at height 2165.

For continued growth keep the effective \(r=2\) zero-shift atom after subtracting the complete old-return charge there from the ordinary lower atom. It still exceeds \(1/20\). This is a kernel estimate **before** convolution with the two residuals. The special unary grouping touches only residual counts zero and one. If the true previous full mass is \(b_0\), the untagged-outside-\(T\) measure has mass at least \(b_0-0.028\). Both it and the full measure are symmetric projected packet measures with first absolute moment equal to their mass. Conditional Jensen applied to two draws therefore gives next full mass at least \((b_0-0.028)^2/20\) on grouped levels and at least \(b_0^2/20\) on ordinary levels. The smaller map grows strictly above the diagonal from 21 onward and diverges there. The escape pertains to this signed propagation at the fixed limiting seed.

## The actual rectangle

For the upper rectangle use the rougher ordinary root kernels from round 58, so the positive result is independent of the lower obstruction and the mixed-sector cancellation. Fit the 50 packet coordinates by solving the finite convolution equations with their Fourier derivatives and round the fitted coordinates up to integers in units of \(10^{-14}\). Only the frozen integers enter the proof. On ten closed real intervals of width \(1/65536\), enclose the full imaginary thickness, all seed coefficients and \(s\in\sqrt8\pm10^{-12}\). The common core has off-zero excess below \(396\cdot10^{-9}\) with residual budget \(6\cdot10^{-7}\) and total coordinate cap \(4.651\). The inherited weighted tail accounts for the degree-28 analytic remainder, the omitted packet coordinates and the exceptional columns for all sufficiently large eligible fields. The Euclidean derivative is less than \(3/4\) at that cap. Uniform Picard convergence and uniqueness on the open overlap give the actual common marked bound stated above. [Upper kernel and finite-field argument](astra-ranknext-58.md#certified-upper-rectangle)

Reproduce the three proof records from the repository root with `.venv/bin/python -B research/astra-mixed-61-check.py`. The floating [cap fitter](astra-mixed-61-probe.py) only selected rational coordinates. [Arb checker](astra-mixed-61-check.py) · [Certified output](astra-mixed-61-checks.jsonl)

1. Keep the first nontrivial \(Sp_8\) sector across adjacent outer vertices and the return of its tensor square. Require an overlapping actual cap below \(2031/128\) or a lower escape with the entire retained sector debited and a surviving quadratic growth coefficient.
2. Fit distinct distinguished offsets at the new left endpoint by the *signed* Jacobi and rank-two scalar equations and certify the changed profile at its own coefficients. A strict invariant on overlapping complex slabs crossing \(2031/128\) passes. A fully debited lower escape at that floor rejects that fixed profile.
