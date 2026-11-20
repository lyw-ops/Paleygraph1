# A common carrier for the genuine near-edge repair window

On the marked obstruction and at the critical cap rate, the actual negative repair rows share a high-amplitude carrier of size \(O(\sqrt n)\) across a window of order \(\sqrt n\). This uses the summed squared changes of the negative parts, not the sum of the separate adjacent upper bounds. The outside low layer has uniformly small relative squared mass.

Use \(b^j,h_j,m_j,P,\epsilon\) and the fixed-floor, critical-rate obstruction assumptions of [the persistent repair block](persistent-repair-deficit-109.md). All vector norms and pairings are normalized. Write \(I\) for its contiguous late block and define \(\Delta_j=h_{j+1}-h_j\). At each \(j\in I\), \(\|h_j\|_{2,n}^2\asymp n^{-1/2}\), \(m_j\asymp n^{-1/2}\), and \(\|P h_j\|_{2,n}^2=O(n^{-1})\). In particular \(\|h_j\|_\infty=O(1)\) follows without a truncation. Indeed \(\|K h_j\|_\infty\le\sqrt p\,m_j=O(1)\), and \(\|h_j-\epsilon K h_j\|_\infty\le\sqrt n\|h_j-\epsilon K h_j\|_{2,n}=O(1)\).

## Exact telescoping bound and a common threshold

The independent reviewer observed that the scalar negative-part map, applied coordinatewise, gives
\[
 \|\Delta_j\|_{2,n}^2
 \le -\langle\Delta_j,b^{j+1}-b^j\rangle_{2,n}
 =-\langle\Delta_j,P h_j\rangle_{2,n}.
\]
The scalar inequality holds by monotonicity and 1-Lipschitz continuity of the negative of the negative-part map. Expanding the right side twice and using \(\|P\Delta_j\|_{2,n}\le\|\Delta_j\|_{2,n}\) gives
\[
 \|\Delta_j\|_{2,n}^2
 \le \|P h_j\|_{2,n}^2-\|P h_{j+1}\|_{2,n}^2 .
\]
Consequently
\[
 \sum_{j=i}^{l-1}\|\Delta_j\|_{2,n}^2
             \le \|P h_i\|_{2,n}^2=O(n^{-1})                    \tag{1}
\]
for any contiguous subblock \([i,l]\) of \(I\). This also implies that the consecutive normalized correlations of the \(h_j\) are at least \(1-O(n^{-1/2})\), since the squared norm difference of two neighboring rows is \(O(n^{-1})\) and their norms squared are comparable to \(n^{-1/2}\).

For fixed small \(\eta>0\), write \(S_j(s)=\{x:h_j(x)>s\}\), \(s\in[\eta,2\eta]\). Uniformly in the block, these sets have size between \(c_1\sqrt n\) and \(C_\eta\sqrt n\) for suitable positive constants. The upper follows from \(m_j\), while the lower uses \(\|h_j\|_\infty=O(1)\) and the low squared mass at most \(2\eta m_j\). For adjacent times the union \(\{x:\max(h_j(x),h_{j+1}(x))>\eta\}\) has size \(O_\eta(\sqrt n)\). Thus
\[
 \int_{\eta}^{2\eta}|S_j(s)\mathbin{\triangle}S_{j+1}(s)|\,ds
     \le C_\eta n^{3/4}\|\Delta_j\|_{2,n}.
\]
Here layer cake integrates at most \(|\Delta_j(x)|\) per coordinate, and the displayed factor converts the normalized second norm to a counting first norm on the union. Summing and using (1) shows that some common \(s\in[\eta,2\eta]\) on the entire subblock has total support flips
\[
 \sum_{j=i}^{l-1}|S_j(s)\mathbin{\triangle}S_{j+1}(s)|
       \le C'_\eta n^{1/4}\sqrt{l-i}.                             \tag{2}
\]
In particular, on the full late block there is a union \(H=\bigcup_{j\in I}S_j(s)\) of size \(O_\eta(\sqrt n)\), since its size is no more than the first support size plus the total flips. On any subblock \(l-i=o(\sqrt n)\), a possibly different common threshold makes the intersection have size at least \(c_1\sqrt n-o(\sqrt n)\). Even for a sufficiently small fixed multiple of \(\sqrt n\) steps, (2) gives a common intersection of size at least \(c_1\sqrt n/2\), by choosing that multiple in terms of \(C'_\eta,c_1\). All threshold choices can depend on the observed prime and subblock.

## A shared compression on the genuine carrier

For \(u_j=1_H h_j\), the discarded squared mass is at most \(2\eta m_j=O(\eta n^{-1/2})\) uniformly. The self-adjoint form \(I-\epsilon K\) is positive semidefinite with norm at most two, and its value on \(h_j\) is \(O(n^{-1})\) by the persistent block. The seminorm triangle inequality gives
\[
 \big\langle u_j,(I-\epsilon K)u_j\big\rangle_{2,n}
                 =O(n^{-1}+\eta n^{-1/2}).
\]
For sufficiently small fixed \(\eta\), \(\|u_j\|_{2,n}^2\gtrsim n^{-1/2}\), so the signed Rayleigh quotient of every \(u_j\) is at least \(1-C\eta-O(n^{-1/2})\). The constant is independent of sufficiently small fixed \(\eta\) in the low-layer estimate. The size budget for \(H\) does depend on \(\eta\). This provides a common genuine carrier for testing both the arithmetic and the time evolution. A prime-uniform estimate excluding that carrier is still needed.

1. Use (1)–(2) to test the Jacobi compression on the actual common carrier, or analyze a persistent intersection where the exact affine repair update is valid at every step.
2. Seek the small initial critical cap bound or exploit the true marked factor together with the common carrier. Single-row estimates at the minimum entry-scale support require an additional extremality premise.
