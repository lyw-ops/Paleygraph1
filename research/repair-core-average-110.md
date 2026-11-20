# Averaged Jacobi balance on a persistent repair core

The actual core of the negative repair obeys an exact averaged linear equation. Its local opposite-sector projection is smaller by a factor \(n^{-1/4}\) than the global projection estimate. A near-unit compression can also be restricted to this persistent core, with an explicit loss from low amplitudes and temporal support flips.

Use the [genuine marked obstruction and critical cap-rate hypotheses](persistent-repair-deficit-109.md) at fixed \(t,M\). In its late block, put \(P=(I-\epsilon K+J_0)/2\). Then \(b^{j+1}=b^j+P h_j\), \(h_j=(b^j)_-\), and \(m_j=\mathbb E_n h_j\asymp n^{-1/2}\). All vector norms below are normalized. Fix sufficiently small \(\eta>0\) and then a sufficiently small positive constant \(\kappa\) depending on \(\eta\). Take \(\kappa\) small enough that the flip coefficient \(C_\eta\sqrt\kappa\) below is at most \(\eta\) and less than half the fixed lower coefficient for the high set size. Choose a contiguous interval \([i,l]\) of length \(L=l-i\asymp\kappa\sqrt n\) inside the late block. Apply the [common-threshold selection](repair-carrier-109.md) at one \(s\in[\eta,2\eta]\), with sets \(S_j(s)=\{h_j>s\}\), and set
\[
 C=\bigcap_{j=i}^{l}S_j(s),\qquad H=\bigcup_{j=i}^{l}S_j(s).
\]
Thus \(|C|\gtrsim\sqrt n\), \(|H|=O_\eta(\sqrt n)\), and \(|H\setminus C|\le C_\eta \sqrt{\kappa}\sqrt n\). The last inequality follows since every element of the union outside the intersection causes at least one adjacent support flip.

## The time-averaged equation on the core

On \(C\), the two consecutive \(b\)-rows are both strictly negative, so the actual repair has the exact linear restriction
\[
 1_C(h_{j+1}-h_j)=-1_C P h_j.
\]
With \(\bar h=L^{-1}\sum_{j=i}^{l-1}h_j\) and \(\bar m=\mathbb E_n\bar h\), summing gives
\[
 1_C P\bar h=L^{-1}1_C(h_i-h_l),\qquad
 \|1_C P\bar h\|_{2,n}\le O((nL)^{-1/2}).                         \tag{1}
\]
For the bound use Cauchy–Schwarz in time and the exact summed square difference \(O(n^{-1})\) from the previous round. The saving in (1) is local to \(C\). On the full group one still has only \(\|P\bar h\|_{2,n}=O(n^{-1/2})\) from the late block.

Equivalently, every real \(v\) supported on \(C\) satisfies
\[
 \left|\epsilon\langle v,K\bar h\rangle_{2,n}
           -\langle v,\bar h\rangle_{2,n}-\bar m\mathbb E_n v\right|
   \le O((nL)^{-1/2})\|v\|_{2,n}.                               \tag{2}
\]
The sign of the constant term follows by expanding \(2P=I-\epsilon K+J_0\). For \(v=1_C\), the error is \(O_{\eta,\kappa}(n^{-1})\) when \(L\asymp\kappa\sqrt n\), whereas \(\langle 1_C,\bar h\rangle_{2,n}\gtrsim_\eta n^{-1/2}\). This gives a more precise signed transport against the actual persistent core. Equation (2) retains the full averaged source \(\bar h\), including its exterior mass.

## Compression to the same persistent core

For every \(i\le j\le l\),
\[
 \|1_{C^c}h_j\|_{2,n}^2
     =O\big((\eta+C_\eta\sqrt\kappa)n^{-1/2}\big).
\]
Indeed off \(S_j(s)\) the squared mass is bounded by \(2\eta m_j\), and \(S_j(s)\setminus C\) has size at most \(|H\setminus C|\) with uniformly bounded amplitudes. Hence the same bound holds for \(\bar h\) by the triangle inequality. On \(C\) one has \(\bar h\ge s\), which bounds \(\|1_C\bar h\|_{2,n}^2\) below by a positive constant depending on \(s\) times \(n^{-1/2}\). For sufficiently small \(\eta\) followed by sufficiently small \(\kappa\), one can take the latter constant independent of \(\eta,\kappa\): \(\|h_i\|_{2,n}^2\gtrsim n^{-1/2}\), while
\(\|\bar h-h_i\|_{2,n}\le O(\sqrt\kappa\,n^{-1/4})\) by the same time telescope, and the exterior squared norm is as bounded above.

Let \(B=I-\epsilon K\). This is positive semidefinite and bounded by \(2I\), and \(\|B^{1/2}h_j\|_{2,n}^2=O(n^{-1})\) on the late block. The seminorm triangle inequality and the exterior bound show that the signed Rayleigh loss of \(1_C\bar h\) is \(O(\eta+C_\eta\sqrt\kappa+n^{-1/2})\), with constants from the fixed obstruction parameters. Thus one can have both the core-localized compression and the more accurate balance (2) for the full source at the same genuine \(\bar h\).

The remaining prime-specific question is whether the full source and its actual small-amplitude exterior can satisfy (2) at this accuracy on a persistent core while maintaining the true marked pairing. Small exterior squared mass alone does not replace the full \(\bar h\) in (2) at the \(n^{-3/4}\) scale, since a bounded second-norm operator only preserves its \(O(\sqrt\eta\,n^{-1/4})\) norm estimate.

1. Test arithmetic on the persistent core using both the signed balance (2) and the actual low-source contribution. Do not silently replace the latter by zero.
2. Retain the size parameter of \(C\) and the separate critical cap-defect premise. At fixed small \(\eta\), the proof gives neither the minimum-support equality nor an upper bound on the near-unit compression.
