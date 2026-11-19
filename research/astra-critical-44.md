# A collision cost for every rooted critical probability

A nonempty critical shell at any fixed positive floor forces **every** probability on it to have normalized collision excess at least
\[
  [4(\sqrt{1+\tau}-1)-o(1)]\,D(q),
\]
where \(D(q)\sim\log_2^*q\) is the [proved marked window](vanishing-floor-38.md). This holds on eligible primes and square fields. It uses the fact that the sector, positivity and specified root of the test do not tie it to an orbit at that same floor. Testing the row against the **actual zero-floor** Picard trajectory gives a pointwise Fourier majorant for the root with one same-sector error term. Completing the square gives an exact finite certificate for a quadratic penalty. The conclusion on collision cost does not upper-bound the unpenalized positive-floor shell score.

## Finite identity and a structured majorant

Let \(\mu\ge0\) have sum one on the \(n\) frequency indices and belong to \(\mathbb R1+V_\sigma\). Write \(j=\mathbf1/\sqrt n\), \(x=\sqrt n\,\mu\), \(d=x-j\in V_\sigma\), and \(\alpha=x_0\). Its collision excess is \(L=\|d\|^2=n\sum_i\mu_i^2-1\) in counting norm. Use the actual, undamped cold orbit from \(v_0=0\),
\[
 v_{s+1}=K\phi_s,\quad
 \phi_s=|v_s|+b_s e_0,\quad
 b_s=\sqrt{4+v_s(0)^2}-|v_s(0)|,\quad
 g_s=\langle j,\phi_s\rangle/2 .
\]
Set \(B_T=\sum_{s<T}(2-b_s)\), \(A_T=\sum_{s<T}(1-g_s)^2\), \(H_T=\sum_{s<T}\langle x,|v_s|-\sigma v_s\rangle\ge0\), \(C_T=\langle v_T,Kv_T\rangle\), and \(P=P_\sigma\).

The exact **pointwise** identity is
\[
 (2T-B_T)e_0+\sum_{s<T}(|v_s|-\sigma v_s)
 =2\Big(\sum_{s<T}g_s\Big)j+\sigma Pv_T+w_T,
 \qquad w_T=\sigma P_{-\sigma}v_T+2\sum_{s<T}P_{-\sigma}\phi_s.       \tag{1}
\]
Indeed \(\sigma K\phi_s=(I-J)\phi_s-2P_{-\sigma}\phi_s\). Subtract \(\sigma v_s\), sum and split the mean-zero terminal vector. Removing the nonnegative sum on the left makes the right a majorant. The term \(w_T\) lies exactly in the opposite nonconstant sector.

Pair (1) with \(x\), using \(\langle j,x\rangle=1\), and the cold norm telescope
\[
 2\sum_{s<T}(1-g_s)=\|v_T\|^2/4+A_T.
\]
Using \(\|Pv_T\|^2=(\|v_T\|^2+\sigma C_T)/2\) yields
\[
 \boxed{\ (2T-B_T)\alpha-2T
   =\tfrac12 L-\tfrac12\|d-\sigma Pv_T\|^2
      +\tfrac14\sigma C_T-A_T-H_T.\ }                              \tag{2}
\]
This identity controls each row with the same actual, sign-specific direction \(\sigma Pv_T\). It retains its signed mismatch, the mean loss and the wrong-sign occupation. Even before applying arithmetic, a nonempty shell at mark \(\alpha\) has minimum collision excess at least
\[
 \max_{1\le t\le T}
 \left[2((2t-B_t)\alpha-2t+A_t)-\sigma C_t/2\right].                \tag{3}
\]
One can also keep the squared distance in (2) and lower-bound it by the squared distance from \(j+\sigma Pv_t\) to the nonnegative orthant with the prescribed root. This requires only replacing the root by \(\alpha\) and clipping the remaining coordinates at zero.

## The signed correction in the actual marked window

Uniformly for \(1\le T\le D(q)\), round 38 gives \(0\le B_T\le\sum_{s<T}|v_s(0)|=o(1)\). For \(Y_s=\sqrt n v_s\), the equation \(Kv_T=(I-J)\phi_{T-1}\) gives
\[
 C_T=\mathbb E[Y_T|Y_{T-1}|]+b_{T-1}v_T(0).
\]
The first term is \(o(1)\) by the [signed history estimate](astra-completion-40.md) with \(Y_0=0\) and the even 1-Lipschitz test \(|Y_{T-1}|\); the second is \(o(1)\) by the same marked window. The constants in the window can ensure any prescribed fixed inverse power for these errors. All feasible marks are uniformly bounded since \(\mu_0-1/n=\sigma (K\mu)_0\) and \(\max_i|K_{0i}|\le\sqrt q/n\). Thus (2) proves
\[
 L\ \ge\ 4T(\alpha-1)+\|d-\sigma Pv_T\|^2+2(A_T+H_T)-o(1) .         \tag{4}
\]
In fact the right without the last error differs from \(L\) by \(o(1)\) in absolute value. For the positive-floor shell take \(\alpha=\sqrt{1+(1-1/n)\tau}\) here. At varying floors \(\tau\downarrow0\) with \(T\tau\to\infty\), the same bound gives \(L\ge(2-o(1))\tau T\). The coefficient four in (4) is supplied by signed sector splitting. Sharpness among actual positive rows is open.

For the larger-theta sign take the minimum-norm optimal \(x\) on each prime and \(T=D(p)\). A bound \(L=o(D(p))\) forces \(\alpha=1+o(1)\), whence the opposite normalized mark also tends to one by the complementary product. The [moving-width work](parallel-complexity-14.md) already has a log-star allowed-energy criterion at the moving quadratic width. Equation (4) gives a direct row-by-row collision cost at every mark, with a finite error and three explicit reserves. Neither an endpoint energy bound through primes nor a prime-uniform signed endpoint upper bound is established here. On a square \(q=r^2\) the exact plus optimum has \(L=r-2\), \(\alpha\to\sqrt2\). Its mixture with uniform to a fixed critical mark strictly between one and \(\sqrt2\) has \(L=\lambda^2(r-2)\) for a mixing parameter \(\lambda\to\sqrt{(1+\tau)/2}\). This is compatible with (4).

## The direction required at a high mark

The collision cost has a one-dimensional strengthening. Put \(u_t=\sigma P_\sigma v_t\) and
\[
  L_t^{\rm dir}(x)=
   \frac{\langle d,u_t\rangle_+^2}{\|u_t\|^2}
\]
when \(u_t\ne0\), and zero otherwise. The numerator takes the positive part before squaring. Since
\(\langle d,u_t\rangle-\|u_t\|^2/2\le L_t^{\rm dir}(x)/2\),
the proof of (2) gives the stronger necessary inequality
\[
 L_t^{\rm dir}(x)\ \ge\ 2((2t-B_t)\alpha-2t+A_t+H_t)-\sigma C_t/2.    \tag{5}
\]
In particular every fixed positive-floor critical probability must pay the same log-star lower bound **in this one explicit direction**, simultaneously for every growing depth within the proved window. Large collision energy in unrelated Fourier directions gives no credit. At the square plus endpoint (5) yields \(\liminf L_T^{\rm dir}/T\ge4(\sqrt2-1)\). For measuring (5) on the least-norm exact endpoint with support \(S\), the [kernel formula](endpoint-norm.md) gives \(\langle d,u_t\rangle=\alpha\langle\Pi_N e_0,(u_t)|_S\rangle/\|\Pi_Ne_0\|^2\), \(N=\ker(P_{-\sigma} E_S)\); here \(\langle j,u_t\rangle=0\). The induced estimate for the constrained shell is one-sided and tests the cold orbit. It need not estimate the positive-floor score itself.

## Replay and two next tests

Run `.venv/bin/python -B research/astra-critical-44-check.py` to reproduce the [six 512-bit interval records](astra-critical-44-checks.jsonl). They use the [strict prime witness](astra-rooted-43.md) at \(p=101\) and the exact square subfield witness at \(q=49\), both mixed to the exact positive-floor mark at \(\tau=1/4\). On their zero-floor orbits the completed-square identity encloses zero with radius below \(10^{-55}\). At depth three the finite lower bound (3) using that depth alone exceeds 1.91318 at the prime and 2.06996 at the square. The values of \(L\) for these specific rows are 2.27801 and 3.96826 to five decimals. Formula (3) holds with no requirement of identifying the minimum-norm critical witness.

1. Test the [marked kernel atom](endpoint-norm.md) on the actual support of the least-norm larger-theta endpoint. With \(\omega=\|\Pi_{\ker(P_{-\sigma}E_S)} e_0\|^2\) one has \(L+1=\alpha^2/\omega\). A prime-uniform lower bound with \(D(p)\omega\to\infty\) closes the ordinary-theta limit by (4). A certified sequence on which \(D(p)\omega\) stays bounded rules out that sufficient condition. Finite plots do not settle either direction.
2. When the full norm is large, estimate the single directional energy \(L_t^{\rm dir}\) in (5), including the sign at the actual endpoint. It suffices to find one growing depth \(t\le D(p)\) on each prime at which \(L_t^{\rm dir}=o(t)\) on the larger-theta side. A uniform positive lower bound for \(L_t^{\rm dir}/t\) throughout every such choice on a prime subsequence rules out this sufficient test. Compare with the square plus lower bound above; a large full norm by itself does not rule it out.
