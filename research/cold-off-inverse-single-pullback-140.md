# One signed pullback on the full parameter line

Use the [actual pairing](cold-same-row-involution-139.md), with \(x,y\in G=\mathbb F_p^{\times2}\), \(c=xy\ne1\), and \(z_c(r)=(r^2-c)/(r^2-1)\). Suppose \(F\) is the symmetric weight on \(G\) with \(F(c/z)=F(z)\). The square-difference weight has this symmetry. The anticommutator weight may first be averaged with its image under \(z\mapsto c/z\), because the sign mask is invariant under that exchange. Let \(\widetilde F\) be any extension to \(\mathbb F_p^\times\) with the same symmetry. Then the exact signed sum is
\[
 \sum_{z\in G}(s(z)+s(c/z))F(z)
  =s(c)F(1)+s(c)\sum_{r\in\mathbb F_p,\,r^2\notin\{1,c\}}
       \chi(r^2-1)\widetilde F(z_c(r)).                             \tag{1}
\]
In particular the ordinary trace functions for the two derivative rows can be extended to the full multiplicative line for this calculation, without extending the weight by zero on nonsquares.

To prove (1), in the two-branch formula from Round 139 replace the zero extension by \(\widetilde F\). The bracket \(\chi(r^2-1)+\chi(r^2-c)\) already vanishes whenever \(z_c(r)\) is nonsquare. For nonzero \(r\) make the bijective substitution \(r\mapsto\sqrt c/r\) on the allowed parameter set. It exchanges \(\chi(r^2-1)\) and \(\chi(r^2-c)\) because \(\chi(-1)=1\), and sends \(z_c(r)\) to \(c/z_c(r)\). The two branches therefore give equal sums on nonzero parameters. At \(r=0\) both signs are \(+1\), \(z_c(0)=c\), and the terms are again equal. The original exceptional term at \(z=1\) is unchanged.

For symmetric extensions the nonsquare weights cancel inside the single pullback through this parameter involution. The formula does not infer any reduction of conductor or physical packet price from the equality of the two branches. It removes the square cutoff in the signed weighted sum and expresses the remaining task on one ordinary rational pullback, with the \(c=1\) inverse line still separate.
