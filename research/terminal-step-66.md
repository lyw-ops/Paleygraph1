# A two-activation bound on the terminal energy

Through eligible primes with \(\tau_p\to0\), the scaled actual undamped orbit has
\[
\|V_{T+1}-V_T\|_{2,n}^2<0.177914+o(1),\qquad V_T=\sqrt n\,v_T/2,
\]
uniformly for \(T\ge2\). In the marked window this gives
\[
\frac{E_{T+1}-E_1}{4}\ge0.00085-o(1)\qquad (2\le T\le D(p)).
\]
An additional pairing of the two consecutive states gives a quantified improvement over the scalar last-activation bound of round 65. Put \(m=2\sqrt2/\pi\), \(\delta=1-m\), and \(L_2=\lim_p P_2\). Then for \(3\le T\le D(p)\),
\[
P_T+\frac{E_{T+1}-E_1}{4}\ge L_2+\delta^2+0.0000025-o(1)>0.022976-o(1).
\tag{1}
\]
The same lower bound applies to \(2Ts+T(1-1/n)\tau_p\) whenever both proposed marks admit nonnegative completions with extra common scaled mean \(s\). This is an ordinary proof with one outward evaluation of constants. The separate precursor test in round 65 also provides its own positive improvement. [Round-65 identities](terminal-budget-65.md) · [Actual second-step law](mean-energy-64.md)

## The early loss controls every later increment

Use normalized counting brackets and norms, and the notation \(W_t,\psi_t,a_t,x\) of round 65. In particular \(V_{t+1}=a_t x+K\psi_t\). The true undamped finite-field update is nonexpansive in Euclidean norm, so the step lengths are nonincreasing at each field, with its own floor. Put \(r=\sqrt2\), \(v=1-m^2\), and let \(Z\) have the independent symplectic series law for the second scaled state \(X+Z\). In the field limit at fixed time, \(a_2-a_1=o(1)\), and the \(K^2=I-J\) identity gives
\[
\lim_p\|V_3-V_2\|_{2,n}^2
= \operatorname{Var}(|X+Z|-|X|)
=v-(\lim_p g_2-m)^2-4\mathbb E[-X(X+Z)]_+ .
\tag{2}
\]
Here \(X=r\cos\Theta\) is independent of \(Z\), and each finite truncation and its normalized \(L^2\) limit follow from round 64. The marked contribution and the varying floor change the two activations by \(o(1)\) in normalized \(L^2\). The last equality subtracts the squared mean and uses \((|u|-|w|)^2=(u-w)^2-4(-uw)_+\).

Condition on \(Z=z\). By symmetry we may replace \(z\) by \(|z|\). The arcsine density is at least \(1/(\pi r)\), so the conditional crossing expectation is bounded below by
\[
\frac{1}{\pi r}\int_0^{\min(|z|,r)} u(|z|-u)\,du
\ge \frac{|z|^3-(9/(32r))z^4}{6\pi r}.
\]
For \(|z|\le r\) the integral is \(|z|^3/6\). Above \(r\) the omitted integral is \((|z|-r)^2(|z|+2r)/6\). With \(y=r/|z|\), the ratio of this omission to \(z^4/(6r)\) equals \(y(1-y)(1+y-2y^2)\le9/32\). Now \(\mathbb E|Z|^3\ge v^{3/2}\) and \(\mathbb E Z^4=3v^2-(2m/3)^4/8\). Inserting the lower endpoint \(g_2>0.9436066882988\) in (2) gives the upper bound
\[
I=v-(0.9436066882988-m)^2
-\frac{4}{6\pi r}\left(v^{3/2}-\frac9{32r}\big[3v^2-(2m/3)^4/8\big]\right)
<0.177914 .
\tag{3}
\]
Thus \(\|V_{T+1}-V_T\|_{2,n}\le\sqrt I+o(1)\) at all \(T\ge2\). The \(o(1)\) here comes from a single fixed-depth limit and is independent of \(T\).

## A uniform variance floor and a joint terminal bound

Let \(e=\operatorname{Var}_p(\psi_T)\), \(g=g_T\) at a marked depth. Since \(\psi_T\ge |W_T|\) and \(\langle W_T,x\rangle=1+o(1)\), the covariance inequality gives
\[
mg+\sqrt{ve}\ge 1-o(1)
\]
along any sequence with bounded \(e\) and \(g\). The next-state displacement from \(x\) has squared norm \(e+o(1)\). The current-state displacement has squared norm \(g^2+e-1+o(1)\). These identities use the mark error, \(\tau_p=o(1)\), and \(\psi_T^2=W_T^2+\tau_p\) off the mark. If \(e\le0.00085+o(1)\) along any sequence of depths, the reverse triangle inequality with (3) first bounds \(g\), then gives \(g^2-1\le I+2\sqrt{Ie}+o(1)\). The covariance inequality forces the opposite inequality with strict margin because
\[
\left(\frac{1-\sqrt{0.00085\,v}}{m}\right)^2-1-I-2\sqrt{0.00085\,I}>0.00008 .
\]
The contradiction proves the stated variance floor and hence the energy floor by the round-65 terminal identity.

For the joint bound, write \(B=\mathbb E_p(\psi_T-1)^2\), \(f=\operatorname{sgn}(x)-mx\) and \(z=Kf\), with \(\operatorname{sgn}(0)=0\). Then \(\|f\|^2\to v\), \(\langle f,x\rangle=o(1)\), \(\mathbb E_p[\operatorname{sgn}(x)f]\to v\). Moreover \(\langle z,1+\delta |x|\rangle=o(1)\), because \(K\mathbf1=0\) and \(\langle f,K|x|\rangle\to0\) by the joint law of the second-step field and \(X\). This pairing follows by first truncating the symplectic series, using the zero probability of \(X=0\), and then bounding the tail in \(L^2\). From the last activation covariance,
\[
\|\psi_T-(1+\delta|x|)\|^2\le B-\delta^2+o(1).
\]
The step estimate now constrains the linear response in the direction \(f\):
\[
\langle f,W_T\rangle
\le\langle f,V_{T+1}\rangle+\sqrt{Iv}+o(1)
\le\sqrt{v(B-\delta^2+o(1))}+\sqrt{Iv}+o(1),
\]
where the quantity under the first square root is taken with a nonnegative upper error. The second bound uses \(V_{T+1}=a_T x+K\psi_T\), the preceding pairings and \(\|z\|\le\|f\|\).

In the pointwise conjugate bound \((u-1)^2\ge Fw-|F|-F^2/4\) for \(u\ge|w|\), take \(u=\psi_T,w=W_T,F=2\delta x-\epsilon f\) with \(\epsilon=1/1000\). Put \(c=2\delta+\epsilon m\). In the limit, \(|F|\) integrates to \(2\delta m-\epsilon v+2\mathbb E(\epsilon-c|X|)_+\). The density of \(|X|\) is at most \(0.451\) through \(\epsilon/c\), so the final hinge contributes at most \(0.451\epsilon^2/c\). The squared term tends to \(\delta^2+\epsilon^2 v/4\). Therefore if \(B\le\delta^2+d+o(1)\) with \(d=0.0000025\), the conjugate bound forces
\[
B\ \ge\ \delta^2+\epsilon(v-\sqrt{Iv}-\sqrt{vd})-0.451\epsilon^2/c-\epsilon^2v/4-o(1)
>\delta^2+d+0.00000036-o(1).
\]
This contradicts the assumed upper bound. It gives the claimed joint terminal improvement by (3) of round 65 and \(P_{T-1}\ge P_2\). The implication for completion retains both marks and both sectors. It uses the exact budget telescope from round 63, which bounds \(P_T+(E_{T+1}-E_1)/4\) above by \(2Ts+T(1-1/n)\tau_p+o(1)\) for any such successful correction. [Outward checker](terminal-step-66-check.py) · [Constants](terminal-step-66-checks.jsonl) · [Exact completion budget](true-spill-63.md#a-necessary-whole-prefix-energy-bound-for-order-1t-allowance)

## Ranked next tests

1. Evaluate the strict fourth-step increment loss through all eligible primes using the actual second activation and a certified joint law for its leading feedback. A smaller upper limit for a fixed early increment feeds the terminal inequalities simultaneously at all growing marked depths. Proving a summable bound on increments in a sufficiently strong signed norm would be substantially stronger.
2. Test a signed worst-site positive repair at the matching actual depth with \(s=o(1)\). The necessary bound here can eliminate proposed small reserves before that test. A proof must bound the signed repair on both whole rows.
