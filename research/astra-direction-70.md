# Marked inverse moments and the stabilizers of the two exposed supports

Use the true faces at any eligible prime, including when the late observable is taken at $t=L+1$. Below all dot products and norms are ordinary **sums**, and the primary rows have counting mean one. Write $x,q$ for primary rows of signs $\sigma,-\sigma$, respectively. Their marks obey $x_0q_0=n$. Let $I$ be the full support of the first face, $J=I^c$, so the full opposite support is $J\cup\{0\}$. Either choice of sign is possible. Use the compression $C$ on $U=\mathbf1^\perp$ from [round 69](astra-forced-69.md). Thus its quadratic form is the sum of the squared norms of $P_{-\sigma}D_Iv$ and $P_\sigma D_Jv$.

## A field-uniform inverse spectral moment at the actual mark

For every $v\in U$,

$$
 q_0 v_0=\langle  q-1,P_{-\sigma}D_Iv\rangle+
             \langle  x-1,P_\sigma D_Jv\rangle .
$$

Indeed the unrestricted inner products with $q,x$ on the two supports are $q_0v_0,0$, respectively, and the subtracted constant contributions sum to zero. Consequently for $g=e_0-\mathbf1/n$,

$$
 \langle  g,C^\dagger g\rangle
 \le [\Vert q-1\Vert ^2+\Vert x-1\Vert ^2]/q_0^2
 \le n(q_0+x_0-2)/q_0^2 \ll \sqrt n .
$$

The first identity gives orthogonality to the kernel before using the pseudoinverse. The second inequality uses the point caps, since translation of a row to any site preserves sector feasibility. The Jacobi bracket gives the last uniform constant. The two collision sums can be minimized independently over the two exact faces. In particular the mass of the marked unit coordinate in the spectral subspace of $C$ for $[0,\lambda]$ is at most $O(\sqrt n\,\lambda)$ in **squared norm**. This sees every eigenvalue, with no lower bound on the least positive one and no algebraic separation scale. It controls directions with eigenvalues $o(n^{-1/2})$ at the mark. It does not control their pairing with the full cold score.

In fact the first upper bound is an **equality after minimizing separately over the two affine hulls**, allowing signed entries. Write $Bv=(P_{-\sigma}D_Iv,P_\sigma D_Jv)$ on $U$, with codomain the indicated pair of sectors. Since $C=B^*B$, the inverse moment is the minimum of $\|u\|^2+\|w\|^2$ subject to $B^*(u,w)=g$, by the singular value decomposition. The constraint means $D_Iu+D_Jw=e_0+c\mathbf1$. Pairing with a primary first-side row gives $0=x_0+nc$, since $u$ is in the opposite sector and $x$ is supported on $I$. Thus $c=-1/q_0$. It follows that $1+q_0u$ is a mean-one opposite-sector affine row, equal to $q_0e_0$ on $I$. Similarly $1+q_0w$ is a mean-one first-sector affine row supported on $I$. Pairing the latter with the original opposite optimizer forces its mark. These affine spaces are exactly the two affine hulls since each has an optimizer positive on every allowed site; perturbations in the affine spaces near that optimizer preserve positivity. Every such pair conversely gives an adjoint certificate. Thus the nonnegative least-norm rows give the exact inverse moment whenever both affine minimizers happen to be nonnegative.

At $p=13$ the larger minus row is $(3,0,0,3,0,0)$ and the opposite certificate $1+\cos(\pi i/3)$ gives $15/4$. An independent [rational replay](astra-direction-70-check.py) constructs the compression, solves $Cv=g$ exactly and returns $\langle g,v\rangle=15/4$, with rank four.

For a real profile $f$ on $I$ perpendicular to the first facial tangent, let $g_f=P_U D_I f$ and $\mu=n^{-1}\langle x,D_I f\rangle$. This $\mu$ is independent of the primary row. The same adjoint argument gives the block separation
\[
 \langle g_f,C^\dagger g_f\rangle
 =\min_{u\in V_{-\sigma},\,u|_I=f-\mu}\|u\|^2
 +\mu^2\min_{z\in\mathrm{aff}(F_\sigma)}\|z-1\|^2 .
\]
Here $g_f$ kills the opposite tangent by support and the first tangent by hypothesis, so both minimizations have solutions. The scalar in the adjoint equation equals $-\mu$ by pairing against $x$. If $\mu=0$, the second block has zero minimizer. Otherwise $z=1+w/\mu$ converts that block to the indicated affine minimization. This isolates the only score-specific interpolation problem in the first block. No bound for this interpolation energy on the actual late profile is established.

## The marked coordinates common to an entire optimal face

Let $H$ be the set of sites where **every** optimal first-side row attains its point cap. It is the cap set of any relative interior row by linearity. It is exactly the translation stabilizer of the face: translating any such site to the root maps the face into itself, and finite order gives equality. The converse follows by evaluating at the root. This group also equals the stabilizer of $I$: the face consists of all feasible rows supported on $I$ because pairing with an opposite optimizer recovers its root by orthogonality. Thus support invariance is sufficient. Define $H'$ in the same way for the opposite face, with support $J\cup\{0\}$.

**At most one of $H,H'$ is nontrivial.** Indeed $H\subseteq  I$, $H'\subseteq  J\cup\{0\}$. If $a,b$ are nonzero elements of $H,H'$, respectively, then $a+b\in J$ by invariance of $J$ under $H$, whereas $a+b\in I\setminus\{0\}$ by invariance of the latter set under $H'$. This is a restriction on the actual exposed supports. A cap set for one least-norm optimizer can be larger than the cap set forced on the entire face; the argument uses the latter.

Writing $\tau_a q(i)=q(i-a)$, for every $a\in H$ one has $D_I\tau_a q=q_0 e_a$. The preceding inverse moment bound therefore holds at every one of these sites. More precisely replace $g$ by the centered extension of coefficients $u_a$ supported on $H$. The same proof gives the upper bound

$$
 q_0^{-2}(\Vert \sum_{a\in H}u_a\tau_a(q-1)\Vert ^2+
               |\sum_{a\in H}u_a|^2\Vert x-1\Vert ^2).
$$

Zero-sum contrasts on a nontrivial marked subgroup eliminate the entire second block. All these bounds hold for genuine larger and smaller faces, whether or not their optimal rows are unique.

## Tests remaining in order

1. For the larger sign, average any candidate primary row over its actual stabilizer $H$; the result is still primary. For the least-norm row $x$ this averaging fixes the row. Compute the signed charge against the coset-averaged cold score using this row, retaining the signed cross-coset contribution. A uniform upper $o(L)$ at $L+1$ suffices by the charged reserve. A positive normalized lower margin on an unbounded sequence rejects this specific row; trivial $H$ gives no smoothing. At most one of the two faces can give nontrivial support-stabilizer smoothing at a field.
2. On the actual larger support test the component of the restricted centered late score orthogonal to both tangents and to the marked coordinate observables. Certify a uniform bound on its inverse moment, or exhibit an unbounded sequence with divergent inverse moment in a fixed normalization. The root estimate alone removes neither that residual nor the separate facial-tangent charge. The ordinary theta limit remains open.
