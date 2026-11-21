# A charge-reducing autocorrelation repair on the true signed quotient

The genuine signed flat objective admits trials obtained by subtracting a certified part of an autocorrelation while retaining nonnegativity and the original positional sign constraint. The subtraction can use a signed combination of translates of one legal quotient law. A separate exact dual characterizes the full soft objective at a specified root. Both tests keep the original candidate list, genuine time weights and erasures.

Fix the setting of [round 99](quotient-floor-99.md). For the original filtered block \(L\), let \(X=G/L\), \(b=|X|\), and let \(\mathcal P\) be the real nonnegative quotient probabilities admitting only the positional identity and sign \(\sigma\). Use the actual signed flat price \(v_R\) with \(v_0=0\) from the [signed quotient head](astra-quotient-99.md). All convolutions are counting convolutions on \(X\) and \(\check q(x)=q(-x)\). The normalized price of a law \(u\) with root \(u_0>0\) is \(\langle v,u\rangle/u_0\).

## Subtracting selected autocorrelation charges

Take any \(q\in\mathcal P\) with \(\kappa=\sum_x q_x^2\). For a row \(a\) with \(0\le a_x\le q_x\), form
\[
 P_a=(q-a)*(\check q-\check a)-a*\check a
     =q*\check q-q*\check a-a*\check q.                            \tag{1}
\]
For each opposite frequency \(\widehat q=0\), so the two autocorrelations on the left have equal Fourier coordinates \(|\widehat a|^2\) there. Hence \(P_a\) has only allowed Fourier support. Its mass is \(1-2\sum_x a_x\), and its root before normalization is \(\kappa-2\sum_x q_x a_x\). If \(P_a\ge0\) has positive mass and root at least \(\eta(1-2\sum a_x)\), its normalized row gives a legal trial at floor \(\eta\). The inequalities \(P_a\ge0\) are linear in the mask \(a\), as are the mass, the root condition and \(\langle v,P_a\rangle\le \xi P_a(0)\) at a specified price threshold \(\xi\). The sign constraint uses exact Fourier zeros, independently of where the mask is placed.

There is an explicit test with a single atom. Fix \(x\), write \(d=q_x\), and let \(a=(T/2)\delta_x\) with \(0\le T\le 2d\) and \(T<1\). Then \(a*\check a\) is supported only at the root, so positivity outside zero is automatic. At zero require \(\kappa-Td\ge\eta(1-T)\). Thus, if \(\kappa\ge\eta\) and \(d>\eta\), the cap on \(T\) is \(\min(2d,(\kappa-\eta)/(d-\eta))\), subject to \(T<1\); when \(d\le\eta\) the cap \(2d\) suffices. Put
\[
 C=\langle v,q*\check q\rangle,\qquad
 B_x=\frac12\sum_R v_R(q_{x+R}+q_{x-R}).
\]
Then the trial's exact normalized price is
\[
            \frac{C-TB_x}{\kappa-Td}.                             \tag{2}
\]
Over its feasible interval this improves as \(T\) increases precisely when \(\kappa B_x>d C\). An equivalent constructive upper test for price \(s\) is \(C-s\kappa\le T(B_x-sd)\) for one feasible \(T\). The latter still works when cancellation takes place across many high blocks.

In the even case \(x=0\), suppose \(d=q_0\) stays in a fixed compact subinterval of \((0,1/2)\) and \(\kappa\le2d^2\). For sufficiently small \(\eta>0\), the choice \(T=(\kappa-\eta)/(d-\eta)\) attains the prescribed root. It is legal since \(\kappa-\eta\le2d^2-\eta\le2d(d-\eta)\) and \(2d<1\). The price becomes
\[
        \frac{B_0}{d}+
        \frac{C-(\kappa/d)B_0}{\eta(1-T)} .                         \tag{3}
\]
This isolates an actual signed gap between the original law and its autocorrelation. For example, if \(\eta=A/J\), the triangular estimate is \(o(J)\) from above, and \(B_0\ge0\), the sufficient gap bound
\[
 C-(\kappa/d)B_0\le -\eta B_0/d+o(\eta J^2)
\]
gives the required one-sided \(o(J^2)\) normalized price by (3), since \(1-T\ge1-2d\) stays positive uniformly.

The gap in (3) also has a formula in the actual previous absolute states. Before erasures write \(y_R=(\sigma/J)\sum_{j<J}\mathbb E_R Y_j\), \(A_R=J^{-1}\sum_{j<J-1}\mathbb E_R|Y_j|\), \(b_0=\sqrt n/(mJ)\sum_{j<J-1}\beta_j\), and \(\mu=(2/J)\sum_{j<J-1}g_j\). Averaging the true update on each quotient block, then convolving with a legal probability \(q\), gives
\[
 q*y=q*A+b_0 q-\mu\mathbf1.
\]
Indeed \(Y_0=0\), the quotient image of the marked input is \((\sqrt n/m)K_Be_0\), and \(\sigma K_B q=q-\mathbf1/b\). The constant contribution is \(\mu\) because \(2g_j=\mathbb E_G|Y_j|+\beta_j/\sqrt n\). At the prescribed horizon \(v\) removes \(y_0\delta_0\) and the actual per-time erased entries. The latter change a pairing against *any translate* of a quotient probability by \(O(\varepsilon_p)\), using the lifted pointwise cap \(1/m\) and the removed first mass from [round 99](quotient-floor-99.md). For even \(q\), applying the identity to \(q\) and \(u=q*\check q\) at zero yields
\[
 C-(\kappa/d)B_0
 =\langle A,u-(\kappa/d)q\rangle+(\kappa/d-1)\mu+O(\varepsilon_p).
\]
The marked term and the deleted original-block mean cancel exactly because the indicated signed test has zero root. Thus the same gap can be estimated directly on the genuine absolute orbit before the last update, with the remaining measurements and time horizon fixed. The gap has no established upper through primes.

## The full soft dual

The normalized price over all \(u\in\mathcal P\) with root at least \(\eta>0\), when feasible, equals
\[
 \min\{\langle v,f\rangle:\ f\ge0,\ f(0)=1,\ \sum_R f_R\le1/\eta,\
                       f\text{ has allowed Fourier support}\}.
\]
The constraints follow by taking \(f=u/u_0\), and every such \(f\) normalizes back to an allowed probability with the same quotient price. Finite linear programming duality gives the attained maximum
\[
 \max\left\{\lambda-\frac{\gamma}{\eta}:\ \gamma\ge0,\
     v+\gamma\mathbf1+g\ge\lambda\,\mathbf1_{\{0\}},\
     g\in V_{-\sigma}(B)\right\}.                                 \tag{4}
\]
The multiplier \(g\) is a real mean-zero row in the opposite positional sign and may include both sine and cosine coordinates. The inequality is on every quotient coordinate. Testing (4) against \(f\) proves weak duality, and the finite primal is compact. The earlier sparse-avoidance dual only tests whether a law can vanish at the high head. Formula (4) instead prices the actual signed value even at those blocks.

## A finite certificate on the genuine orbit

Use the same \(p=769,L,J=16\), signed data and erasures \(2+2j\) as round 99. The six-point trial of [round 98](astra-quotient-98.md#finite-physical-replay-and-next-estimates) has root \(1/8\). Its exact \(\kappa=19/288\) follows from the clique's counting difference energy divided by \(b|D|^2\). Use \(x=0,T=1/4\), subtracting the whole original root atom in the autocorrelation difference. The resulting normalized law has root \(5/108>1/25\). Its normalized signed price is in \([1.796814795,1.796814796]\), whereas that of its unrepaired autocorrelation is in \([2.255343363,2.255343364]\). This tests the explicit construction on the actual erased orbit. The positivity and spectrum follow from (1) with one removed atom; the interval computation establishes the numerical comparisons. [Arb384 checker](quotient-soft-100-check.py) · [Replay](quotient-soft-100-checks.jsonl)

1. On the actual filtered sequence, test the sign and size of \(C-(\kappa/d)B_0\) for a trial with \(\kappa\le2d^2\), or use the general mask and compare its signed price against \(o(J^2)\) at the smaller trial root.
2. Use the same true data in the soft dual and the one-sided triangular estimate on the original block. A failure of exact avoidance leaves the signed price test open, as do the escaped branch and ordinary theta limit.
