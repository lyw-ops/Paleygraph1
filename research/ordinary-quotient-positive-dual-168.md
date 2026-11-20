# A nonnegative dual for the genuine positive-first quotient

Use the least-bulk-energy ordinary optimizer \(F\), its true zero set \(U\), the minimum-support real complementary optimum \(R\), its positive bulk support \(A\subset U\), and the actual centered pure projector \(P_0\) of [Rounds 164–167](ordinary-zero-block-low-rank-leakage-167.md). The physical \(e_0\), sector and optimum \(q\) are unchanged. Put
\[
 F_*=\mathbf1+(q-1)P_\epsilon e_0/d,\qquad
 \mathcal W_A=\operatorname{im}P_0\cap\{v:v_A=0\}.
\]
Let \(h_A\) be the minimal norm representer of the centered constraints on \(A\), and \(F_A=F_*-\sqrt n\,h_A\). The affine space of real sector vectors of mass \(n\), mark \(q\), and zero restriction on \(A\) is \(F_A+\mathcal W_A\), with \(F_A\perp \mathcal W_A\). In fact \(F_*\perp\operatorname{im}P_0\), and the equations \(F_A|_A=0\) are precisely \(E_A^*h_A=c_{0,A}\).

Write \(d_A^{\rm phys}=F-F_A\). The true \(F\) is the squared-norm minimizer among nonnegative vectors in this affine space: each such vector is feasible in the normalized sector and has the same optimal mark \(q\). Moreover \(F\) is already the unconstrained minimum with zeros on \(U\), by the actual distance-representer identity of [Round 162](ordinary-zero-set-leakage-162.md). Hence
\[
 \|d_A^{\rm phys}\|_2^2=\|F\|_2^2-\|F_A\|_2^2=n C_{\rm q}(A).
\]

For \(i\in U\setminus A\) let \(v_i=P_{\mathcal W_A}e_i\). For every \(u\in\mathcal W_A\) with \(u_i\ge0\) at these active coordinates, \(F+\tau u\) is nonnegative for small \(\tau>0\). Optimality gives \(\langle d_A^{\rm phys},u\rangle\ge0\). The finite polyhedral dual cone is exactly the nonnegative span of the \(v_i\), so there is a real \(\mu\ge0\) on \(U\setminus A\) with \(d_A^{\rm phys}=\sum_i \mu_i v_i\). This does not require a strictly feasible point. It gives
\[
 n C_{\rm q}(A)=\sup_{\lambda\ge0}
 \left(-2\sum_{i\in U\setminus A}\lambda_i (F_A)_i
       -\left\|\sum_{i\in U\setminus A}\lambda_i v_i\right\|_2^2\right).
\]
Indeed \((F_A)_i=-\langle v_i,d_A^{\rm phys}\rangle\) on the true active coordinates. The expression equals \(\|d_A^{\rm phys}\|^2-\|d_A^{\rm phys}-\sum_i\lambda_i v_i\|^2\), with equality at the nonnegative \(\mu\). In particular, nonnegativity of \(F_A\) on \(U\setminus A\) alone forces the dual value to be zero. For any \(\mu\) representing a nonzero correction, normalizing to a probability displays an actual one-sided obstruction
\[
 \pi\ge0,\quad \operatorname{supp}\pi\subset U\setminus A,\quad
 s=-\langle F_A,\pi\rangle>0,\qquad
 C_{\rm q}(A)=\frac{s^2}{n\|P_{\mathcal W_A}\pi\|_2^2}.
\]

Finally one can take the nonzero coefficients of \(\mu\) on linearly independent \(v_i\): given a dependence, decrease along it until a positive coefficient reaches zero while all are still nonnegative. Extend this independent subset to a basis of the full quotient span using additional actual columns in \(U\setminus A\). Such a basis together with \(A\) gives a full independent \(JE_i\) extension, since the centered images of \(A\) have one relation and its actual lift through \(JE_i\) is nonzero in the mark direction by the complementary interpolant. This identifies a genuine extension \(B\) for which \(S_B^{-1}c'_B=-\mu_B/\sqrt n\) is coordinatewise nonpositive. It does not assert there is a gain from arbitrarily choosing a basis. A one-sided lower bound for \(\|P_{\mathcal W_A}\pi\|\) relative to the actual negative forcing would control the quotient. Neither that prime-uniform estimate nor the positive-support cost \(C_+(A)\) is established.
