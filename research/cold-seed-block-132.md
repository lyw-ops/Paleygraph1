# The seed–seed contribution to the genuine two-step derivative

On the original square \(Q\), the physical nine-center row \(C\) contains the designated Jacobi seed \(S=2\sqrt n\,Ke_0\). The genuine positive-square-root derivative is \(z/\sqrt{4t+z^2}\) off the mark. Its linear term in \(z\) is \(z/(2\sqrt t)\). Thus one specific contribution to the two-step derivative is
\[
 B_{\rm seed}=K D_{\rm seed} K D_{\rm seed},
 \qquad D_{\rm seed}=\operatorname{diag}(S/(2\sqrt t)).
\]
This first writes that linear contribution with the bulk floor at every site. The actual marked seed coefficient is restored below.

Let \(Q_p=\mathbb F_p^{\times2}\) and \(s(x)=\chi(1-x)\) on \(Q_p\). Use the unitary Fourier transform from \(Q_p\) to its character group. Under its inverse, \(K\) is multiplication by \(s\), and \(D_{\rm seed}\) is convolution by \(s/\sqrt{nt}\) with the unnormalized sum over \(Q_p\). This follows from \(S=2\widehat s/\sqrt n\) with the unnormalized transform of the [ordinary Fourier formulation](fourier.md), using \(s(x^{-1})=s(x)\). Consequently the exact position-side matrix of this contribution is
\[
 (B_{\rm seed}^{\rm pos})_{xz}
   =\frac{s(x)}{nt}
       \sum_{y\in Q_p}\chi\bigl((1-y)(y-x)(z-y)\bigr).
                                                               \tag{1}
\]
The intermediate variable is summed with its sign before taking a modulus. In particular the row \(x=1\) vanishes.

If \(1,x,z\) are distinct, expansion of the square indicator over \(\mathbb F_p^\times\) writes twice the inner sum as two complete quadratic character sums, with polynomials of degrees three and four, up to the omitted term at \(y=0\). Their roots are distinct, including the extra zero root in degree four, because \(x,z\) are nonzero. The classical Weil character-sum bound therefore gives an \(O(\sqrt p)\) upper uniformly in \(x,z\). For \(x\ne1\) and \(z=x\) or \(z=1\), the repeated root instead gives the exact sum \(-1-s(x)\). For \(z=x\) the squared factor removes just \(y=x\) from \(\sum_{y\in Q_p}\chi(1-y)=-1\). For \(z=1\) remove \(y=1\) from \(\sum_{y\in Q_p}\chi(y-x)=-1\), which follows by multiplication by the square \(x^{-1}\). Thus
\[
 \|B_{\rm seed}^{\rm pos}\|_{\max}=O(n^{-1/2}),\qquad
 (B_{\rm seed}^{\rm pos})_{xx}=(B_{\rm seed}^{\rm pos})_{x1}
       =-\frac{1+s(x)}{nt}\quad(x\ne1).
\]
The estimates are uniform on the whole floor square.

The marked first coefficient changes \(D_{\rm seed}\) by
\[
 \delta e_0 e_0^{\mathsf T},\qquad
 \delta=S_0\left(\frac1{2\sqrt n}-\frac1{2\sqrt t}\right).
\]
Here \(S_0=-2/\sqrt n\), so \(\delta=O(n^{-1/2})\). In position coordinates this correction is \(\delta J_0\), with \(J_0\) the averaging projection. Write \(T_s\) for convolution by \(s/\sqrt{nt}\), whose counting operator norm is \(O(1)\), and \(M_s\) for multiplication by \(s\). Changing \(M_sT_s M_sT_s\) to \(M_s(T_s+\delta J_0)M_s(T_s+\delta J_0)\) contributes two linear terms in \(\delta\) and one quadratic term. The former have entries \(O(n^{-1})\) by the counting norm and the norms \(n^{-1/2}\) of all columns and rows of \(J_0\). The latter is \(O(n^{-2})\) entrywise by multiplying the two averaging projections and using \(|s|\le1\). Thus both marked corrections preserve the \(O(n^{-1/2})\) position-entry upper.

## All the linear-in-each-predictor terms

The same entry bound holds for the entire degree-\((1,1)\) composition, with each \(S\) replaced by the corresponding actual predictor \(V_{602}\) or \(V_{601}\). Both have negative-field representations of total dimensional cost below \(4.8\), by the [physical prefix bounds](cold-positive-block-131.md). Include all bad-lift and marked contributions already inserted into these representations. It suffices by linearity and absolute summability to treat one negative object \(M\) from the first row and one negative object \(N\) from the second. Inverse Fourier transformation takes their lift-average Mellin traces to the restrictions of their normalized perverse trace functions \(t_M,t_N\) to \(Q_p\). The position entry is consequently a coefficient times
\[
 s(x)\sum_{y\in Q_p}s(y)t_M(x/y)t_N(y/z).
\]
The two trace functions are from tame local systems of weights at most \(-1\) at smooth sites and ranks \(d_M,d_N\) in the negative class. On the complement of \(\{0,\infty,1,x,z\}\), the inner product is the trace of their pulled-back tensor with the quadratic local system for \(s(y)\). Among the points \(1,x,z\), counted with multiplicity, at least one distinct point occurs an odd number of times. At that point the semisimplified tensor inertia has only eigenvalue \(-1\). Thus it has no geometrically trivial quotient, including after twisting by \(\chi(y)\), which is unramified there. This removes \(H_c^2\) in both complete sums arising from the square indicator. Tame Euler characteristic gives an \(O(d_Md_N)\) dimension bound on \(H_c^1\) with this bounded number of punctures. The tensor weight at most \(-2\) bounds the complete signed sum by \(O(d_Md_N/\sqrt p)\). Any removed finite stalk contributes \(O(d_Md_N/p)\). These estimates also apply when the three points coincide in any pattern.

After summing the two actual coefficient representations, the entire linear-in-each-predictor position matrix therefore has \(\max\)-entry norm \(O(n^{-1/2})\) uniformly on \(Q\). The direct linear coefficient correction of the floor at the mark is now \(O(1)\) times \(e_0e_0^{\mathsf T}\), since the fully marked predictor amplitude is bounded. In position coordinates it is \(O(1)J_0\). The two linear perturbation entries are \(O(n^{-1/2})\) by the same counting argument, and the product of the two corrections is \(O(n^{-1})\), so the full degree-\((1,1)\) estimate is unchanged. The proof uses genuine negative-type inertia for the two linear predictor representations. Absence of a punctual summand for a higher odd middle convolution by itself does not give that inertia.

## The full actual block on the physical mean-zero space

For the full analytic derivatives the position estimate still holds after restricting to the mean-zero space \(X\) in the physical frequency coordinates. The corresponding position space consists exactly of the rows \(f\) with \(f(1)=0\). Thus only \(z\ne1\) is needed. The row \(x=1\) vanishes because \(K\) is the outer operator. For \(x,z\ne1\), both translated or inverted sheaves in the preceding position kernel are lisse at \(y=1\), so only the quadratic twist for \(s(y)\) has nontrivial inertia there. This again rules out a trivial quotient, irrespective of the inertia of the two underlying sheaves at their own translated singularities.

To apply this to the actual derivatives, use the odd expansions in [Round 126](cold-actual-first-insertion-126.md#uniform-word-cost-and-the-two-translated-columns) on the two dimensional representations with cost less than \(4.8\). At arity \(k=2\ell+1\), the middle-convolution word in the two independent lift twists is a tame nonpunctual object lisse off \(1\) on \(\mathbb G_m\). Its generic rank is at most \(k\) times the product of the input dimensions. Its trace has weight at most \(-1\) as an ordinary local-system trace. Those facts are sufficient at \(x,z\ne1\), since the twist for \(s(y)\) already supplies the odd inertia at \(y=1\). For two words of respective arities \(k,l\), the preceding Euler characteristic and Frobenius argument bounds the signed entry by \(O(kl\,p^{-1/2})\) times the product of all input dimensions. The binomial series for the two derivatives sums this bound uniformly because \(4.8^2<4\inf_Q\Re t\).

The Mellin lift-product comparison can differ from the actual word only on the base boundary coordinate. Before applying \(K\), the absolute coefficient sum of these differences is bounded, by the same summable dimension budget. The actual marked derivative contributes another bounded scalar at that coordinate. Thus for either derivative all these corrections form a bounded multiple of \(e_0e_0^{\mathsf T}\), which becomes a bounded multiple of \(J_0\) in position coordinates. The uncorrected convolution operators are uniformly bounded in counting norm by the summed Mellin dimension bounds, so the position entry costs of the corrections are \(O(n^{-1/2})\) as above.

Consequently the actual \(KD_{602}KD_{601}|_X\), in the position basis indexed by \(Q_p\setminus\{1\}\), has every entry \(O(n^{-1/2})\), uniformly on the closed cold square through sufficiently large eligible primes. This includes the higher powers and both marked events. On \(X\) the counting norm is invariant under the unitary change of basis. A bound of order \(n^{-1/2}\) on the entries in position coordinates does not give a contraction in maximum norm or in the physical packet price. Bridging to that ball comparison or obtaining a small actual residual is still needed.
