# A regular completed character test for the physical slope collision

Use the actual square pair levels, cap and slope counts of [Round 165](ordinary-physical-collision-two-copy-165.md).

## A completed nonnegative majorant and a regular character collision test

Let \(g=|f|^2\) on \(Q\), extended by zero at other field elements. It is the full-lift characteristic row of the law \(\omega\) obtained from \(\nu*\check\nu\) by distributing weights equally over the two lifts. Write \(\kappa=\max\omega\), which is \(O(p^{-1/2})\) by the true cap. The two fixed positive physical thresholds give a genuine positive upper
\[
 N_t\le (a^2b^2)^{-1} P_t\qquad(t\in D),
\]
where \(P_t\) sums the four nonnegative \(g(A_x),g(C_x),g(A_y),g(C_y)\) factors over \(u\in Q\setminus\{1\}\) and the full \(z\)-variable at slope \(t\). This completes only the two physical inputs' square masks in a positive majorant. It retains the actual law, actual \(u\)-mask and original slope set \(D\). Zero denominators contribute zero. Any physical zero \(x=0\) or \(y=0\) added by this completion can be removed at pointwise \(O(\sqrt p)\) cost: for \(z=1\) or \(tz=1\), the other vertex has \(A\) a nonconstant injective fractional-linear function of \(u\) off its poles, and \(\sum_A g(A)g(t^{\pm1}A)\le\sum_A g(A)\ll\sqrt p\).

For independent \(\alpha,\beta,\gamma,\delta\) drawn under \(\omega\), opening the four factors and putting \(z=u\xi\) gives
\[
 P_t=\frac12\sum_{i=0}^1\mathbb E_\omega
      \left[J(\overline{\alpha\gamma}\chi^i,\alpha\beta\gamma\delta)
                  \mathscr T(t)\right],
\quad
 \mathscr T(t)=\delta(t)\sum_\xi
       (\beta\delta)(\xi)\,\overline{\alpha\beta}(\xi-1)\,
                        \overline{\gamma\delta}(t\xi-1).
\]
Here \(J\) uses \(1-u\) in its second slot and all characters, even trivial ones, vanish at zero. In fact the vertex arguments are \((1-u)/(z-u)\) and \((1-u)z/(z-u)\) at \(x\), and replace \(z\) by \(tz\) at \(y\). Their product separates exactly into the stated \(u\)-Jacobi and three-root trace. This identity concerns the completed positive upper, not a Fourier clean-cut approximation to the original signed weighted sum.

There is a pointwise \(O(\sqrt p)\) cost on \(t\ne0,1\) for removing all tuples with any trivial root character in either factor, including the infinity characters of both factors. The two infinity relations are \(\beta\delta=\chi^i\) for the outer factor and \(\alpha\gamma=1\) for the inner. A single trivial-character relation costs \(O(\kappa)\) in probability. Away from the two large cases described below, the two individual bounds are \(O(\sqrt p)\) and the product costs \(O(p)\). The large outer Jacobi case imposes \(\alpha\gamma=\chi^i\) and \(\beta\delta=\chi^i\), two independent constraints of probability \(O(\kappa^2)\). With a nonconstant inner trace this costs \(O(p^{3/2}\kappa^2)\). The inner trace can have size \(p\) only if all three root characters are trivial, since its roots \(0,1,t^{-1}\) are distinct. This gives three independent constraints of probability \(O(\kappa^3)\), costing at most \(O(p^2\kappa^3)\) even with a large outer Jacobi factor. The nonconstant inner bound is the three-root Weil bound, with an \(O(1)\) correction for roots belonging to trivial characters. Thus the total exceptional cost is \(O(p\kappa+p^{3/2}\kappa^2+p^2\kappa^3)=O(\sqrt p)\).

For a fixed genuine moderate band \(D\), Parseval gives \(|D|=O(\sqrt p)\). The exceptional error just obtained has counting squared mass \(O(p^{3/2})\) there. So it suffices to control the regular completed character sum's squared mass on \(D\) at that scale. This is a genuine sufficient bound on a positive majorant after removing the controlled exceptional terms.

For the elementary \(\mathscr T\) alone on all nonzero slopes before deleting \(t=1\), its exact unnormalized minus Mellin transform is
\[
 \widehat{\mathscr T}(\psi)
 = (\overline{\alpha\beta\gamma\delta})(-1)
     J(\delta\bar\psi,\overline{\gamma\delta})
     J(\beta\psi,\overline{\alpha\beta}).
\]
Change variables \(w=t\xi\) to obtain the two Jacobi factors. For a transform after removing \(t=1\), subtract the actual \(\mathscr T(1)\) from each coefficient. The completed collision estimate still needs a weighted bound across the regular tuples with the true \(\omega\), and the genuine moderate mask cannot be replaced by its size alone.

On a regular tuple both fixed second Jacobi slots are nontrivial. The Mellin factors can drop from modulus \(\sqrt p\) to modulus \(1\) only at
\(\psi\in\{\delta,\bar\gamma,\bar\beta,\alpha\}\).
The entire inverse transform contribution of those at most four frequencies, including the actual regular outer Jacobi factor, is \(O(1)\) pointwise: each product costs at most \(p\) and inversion divides by \(p-1\). This applies to the full transform prior to restricting \(t\) to \(D\). Let \(P_{\rm gen}\) denote the expectation of the remaining regular products after inversion, with the same outer lifts. Then \(P_t-P_{\rm gen}(t)=O(\sqrt p)\) at \(t\ne1\) by the preceding exceptional estimates.

## A genuine weight that removes the identity slope

On a fixed moderate band \(D=\{t\in Q:s_0\le|f(t)|^2\le s_1\}\) with \(0<s_0\le s_1<1\), one has \(g(t)(1-g(t))\ge s_0(1-s_1)\). Any further favorable mask only restricts this set. Since \(g(1)=1\), the exact nonnegative multiplier \(g(1-g)\) kills the identity slope, including in the full transform before puncturing. Thus a sufficient next estimate is
\[
 \sum_{t\in\mathbb F_p^\times}g(t)(1-g(t))\,|P_{\rm gen}(t)|^2=O(p^{3/2}).
\]
This weight is built from the actual \(f\) and has no contribution outside \(Q\).

Write \(\ell=\omega-\omega*\omega\) on full characters. Its total mass is zero, it is symmetric by inversion, it has counting first norm at most \(2\), and its maximum modulus is \(O(p^{-1/2})\). With the unnormalized minus Mellin transform and \(m=p-1\), orthogonality gives the exact quadratic form
\[
 \frac1m\sum_{\psi,\psi'}\widehat{P_{\rm gen}}(\psi)
     \overline{\widehat{P_{\rm gen}}(\psi')}\,\ell(\psi'/\psi).
\]
This equals the preceding nonnegative physical weighted sum. In particular the genuine \(\omega\) and its convolution enter with opposite signs in a way that annihilates the contribution of the identity slope. The regular three-Jacobi covariance with this actual weight still requires a prime-uniform estimate.
