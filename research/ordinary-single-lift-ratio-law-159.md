# One regular rank-two lift and its exact ratio law

Use the genuine selected short block and full favorable-sector completion of [Round 156](ordinary-sign-selective-completion-156.md), the five-character kernel of [Round 157](ordinary-five-root-trivial-slices-157.md), and all nine exclusions of [Round 158](ordinary-five-root-clean-locus-158.md). The signed desired \(O(p)\) upper is equivalent, up to an additive \(O(p)\), to its \(q=i=0\), last-sign-twisted rank-two formulation. The genuine coupled ratio law can be written explicitly.

## The nonsquare outer lifts cost \(O(p)\)

For all \(u\ne0,1\), write \(F(x)=f(1-vx)\), \(A_u(x)=F(ux)\overline{F(x)}\). Push \(A_u\) forward by \(r_u(x)=(1-vux)/(1-vx)\) onto \(Q\) on contributing terms, retaining the zero physical coordinate which has image \(1\) and coefficient \(1\). This map is injective. For nonsquare \(u\), the nonzero part of \(A_u\) satisfies
\[
  \sum_{\chi(u)=-1}\|1_{x\ne0}A_u\|_2^2
    =2\|F|_Q\|_2^2\,\|F|_{\chi=-1}\|_2^2=O(\sqrt p)
\]
by the actual pin. Take \(h(t)=f(t)\chi(1-t)\), \(f(t)1_{t\ne1}\), or \(f(t)1_{t\ne1,\chi(1-t)=\rho}\). On \(Q\), the multiplicative convolution by \(h\) has operator norm \(O(\sqrt p)\). This follows by expanding \(f\) in the true law and the quadratic mask in two-lift Jacobi sums, using the true cap for the unmasked term. Also \(\|h\|_2=O(p^{1/4})\).

For pairs with both physical arguments nonzero, the \(h\)-weighted sum for all nonsquare \(u\) therefore costs \(O(\sqrt p\,\sqrt p)=O(p)\). For the cross terms with one argument zero use \(\|T_h\delta_1\|_2=\|h\|_2\) for the same convolution and
\[
 \sum_{\chi(u)=-1}\|1_{x\ne0}A_u\|_2
       \le \sqrt n\,O(p^{1/4}).
\]
Their total is \(O(p)\) as well. The zero-zero diagonal vanishes for the off-diagonal weights. A further multiplier of Mellin coefficient sum \(K\) changes these bounds at most by a factor \(K\): it modulates and averages the complete coefficients and has supremum at most \(K\).

It follows that the \(i=0\) and \(i=1\) full \(u\) lifts of each assembled sign term agree at absolute \(O(p)\) scale, since their difference is twice the nonsquare portion. The \(q=0\) and \(q=1\) slope lifts are exactly equal by simultaneously replacing \(T\) with \(T\chi\) and \(q\) by \(q+1\) modulo two. The characters \(A,D\) and all regular exclusions are unchanged. Finally on square \(u\) the untwisted slope sum and \(\rho\) times its \(\chi(1-t)\)-twist differ by \(O(p)\) from the wrong-sector pin, with the same control after lifting by Round 156. Thus, with \(T,U,V,U',V'\) independent under the true \(w\),
\[
 S_{\rm fav}
  =\rho\,\mathbb E_w\bigl[1_{\rm reg}
       J(V/V',L)\,\mathscr K_{q=0}\bigr]+O(p).
\]
The factors of two from opening both square restrictions cancel by the agreements just proved. The diagonal in the twisted form is killed by \(\chi(z-y)\). Any real part in this formula can be taken at the end. Hence the remaining upper concerns one actual signed weighted expectation, with no need for separate absolute estimates of every lift.

## The four-ratio pushforward and a uniform obstruction to smoothing

Use coordinates \((\alpha,\alpha\beta,C^{-1},\delta)\), with \(L=(\beta C)^{-1}\) redundant. Writing \(x=U'\), the probability at these four ratios is
\[
   P(\beta,C,\alpha,\delta)=
     \sum_x w(x)\,w(\alpha x)\,w(\beta\alpha x)\,w(x/C)\,w(\delta x).
\]
It has total mass one and pointwise cap \((\max w)^4\). The map consists of a common-shift fiber and four independent relative coordinates. In the displayed relative-coordinate order the normalized Fourier coefficients are
\[
     \prod_{j=1}^4\widehat w(\xi_j)\,
          \widehat w((\xi_1\xi_2\xi_3\xi_4)^{-1}),
\]
with the plus transform on the character group. Here \(\widehat w=f\) on \(Q\) and vanishes off \(Q\). If \(R=w*\check w\), exactly \(\sum P^2=\sum_d R(d)^5\): expand the square over two common-shift variables and sum out each relative coordinate. For a fixed common-shift ratio \(d\) the four sums each give \(R(d)\), and the remaining two-variable sum gives the fifth. Common shifts of the whole tuple change none of the kernel values.

The true near-flat set from Round 152 puts \(1-o(1)\) of \(w\) on \(O(\sqrt p)\) values, including both lifts. Its five-fold product therefore puts \(1-o(1)\) of the joint ratio law on \(O(p^{5/2})\) values in a space of size \((p-1)^4\). Its total variation distance to uniform tends to one.

The gap against convolution replacement is also present at every fixed degree \(k\ge2\). On the quotient by the lifts, compare the \(\alpha\) marginal \(\nu*\check\nu\) with its \(k\)-fold convolution. Their difference in expected \(\rho k(a)\) (here \(k(a)\) denotes the Jacobi eigenvalue multiplier) is
\[
  p^{-1/2}\sum_{y\in Q}\rho\chi(1-y)|f(y)|^2(1-|f(y)|^{2k-2}).
\]
The wrong-sign mass is \(O(1)\) and \(y=1\) contributes zero. For a fixed \(\lambda_*<1\) sufficiently close to one, [Round 158](ordinary-prime-near-unit-slope-spread-158.md) puts at most \(\sqrt p/4\) points above \(\lambda_*\), so a fixed positive fraction of the total \(|f|^2\) mass is below \(\lambda_*\) and on the favorable sign. There \(1-|f|^{2k-2}\ge1-\lambda_*^2\). Thus the expectation difference is bounded below by a positive constant, uniformly for all integer \(k\ge2\) and sufficiently large primes on the branch. This gives a fixed total variation separation between the original ratio law and the ratio law from smoothed draws, by boundedness of the Jacobi test and contraction of total variation under a marginal. The comparison leaves open a transfer for this particular signed rank-two trace.
