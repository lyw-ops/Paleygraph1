# Consecutive negative rows: corrected API calculation

The [returned Astra draft](api-astra-overflow-109.txt) derives an exact formula on the active set of the projected repair. [Completion receipt](api-astra-109-receipt.json)

Write \(S_j=\{x:b^j_x<0\}\), \(r_j=(I-P)h_j=(h_j+\epsilon K h_j-m_j\mathbf1)/2\). On \(S_j\), \(b^j=-h_j\) so \(h_{j+1}=(r_j)_+\). Outside \(S_j\), \(h_{j+1}\le(r_j)_+\). Two formulas in the draft need correction:

- The squared normalized norm of \(r_j-h_j=-Ph_j\) is \((\|h_j\|_{2,n}^2-\epsilon\langle h_j,Kh_j\rangle_{2,n}+m_j^2)/2\). In a numerator over four the coefficient of \(m_j^2\) is two.
- For \(x\in S_j\), the condition to remain strictly negative at the next step is \(\epsilon(Kh_j)(x)>m_j-h_j(x)\). Leaving \(S_j\) is the opposite weak inequality. The draft has \(m_j+h_j(x)\) instead.

The positive-part formula and its pointwise Lipschitz estimate are valid. The [global telescope](repair-carrier-109.md) gives a stronger quantitative statement on all consecutive rows, including newly negative sites. It budgets their summed squared differences by \(O(n^{-1})\) on the late block. This yields a common high-amplitude carrier and, on a short enough block, an actual persistent core. The draft's proposed character test with the incorrect threshold does not constrain departures.

The returned suggestions were a sign test for departure and an iterated overlap test with the marked factor. These are retained with the exact departure threshold and the common-carrier conclusion. Neither the draft nor the global telescope gives a prime-specific exclusion of the resulting genuine near-eigenrows.
