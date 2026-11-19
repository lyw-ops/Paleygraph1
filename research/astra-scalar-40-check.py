"""Exact independent low-floor checks on two accepted stationary curves."""
import json

import sympy as sp


def report(q, side, active, inactive, first, second):
    print(json.dumps(dict(field=q, side=side, active_bulk=active,
                          inactive_bulk=int(inactive), derivative=str(first),
                          second_derivative=str(sp.radsimp(second))), sort_keys=True))


def main():
    t, r = sp.symbols('t r')
    # Differentiate the independent elimination polynomial at its physical root.
    cases = [
        (13, 6, 'plus', sp.Integer(1),
         (6+5*t)*r**3+(t-6)*r**2-(24+8*t)*r+24-4*t,
         1+r),
    ]
    f25 = ((5*t**2+12*t)*r**5+(-4*t**2+36*t+144)*r**4
           +(-34*t**2-384*t-864)*r**3+(-20*t**2+144*t+1152)*r**2
           +(21*t**2+360*t-432)*r+16*t**2-192*t)
    L = 12-t-(12+t)*r
    numerator = -r*L-8*t*(1-r**2)
    denominator = r*L-3*(4+t)*(1-r**2)
    h = (7+sp.sqrt(13))/18
    cases.append((25, 12, 'minus', sp.simplify(1/h-1), f25,
                  sp.cancel(3*(1+r)*denominator/(denominator+numerator))))
    for q, n, side, root, polynomial, mark in cases:
        def at(expr):
            return sp.simplify(expr.subs({t: 0, r: root}))
        assert at(polynomial) == 0 and at(polynomial.diff(r)) != 0
        slope = -at(polynomial.diff(t))/at(polynomial.diff(r))
        accel = -at(polynomial.diff(t, 2)+2*slope*polynomial.diff(t, r)
                    +slope**2*polynomial.diff(r, 2))/at(polynomial.diff(r))
        dm = at(mark.diff(t)+slope*mark.diff(r))
        ddm = at(mark.diff(t, 2)+2*slope*mark.diff(t, r)+slope**2*mark.diff(r, 2)
                 +accel*mark.diff(r))
        if q == 13:
            g = [sp.Rational(i, 2) for i in (2, 1, -1, -2, -1, 1)]
            endpoint = [1+x for x in g]
            transversal = [-x/3 for x in g]
        else:
            B = [2, 0, 1, 0, -1, 0, -2, 0, -1, 0, 1, 0]
            endpoint = [3, 3*(1-h)/2, 3*(1-h), 3*h, 0, 3*(1-h)/2,
                        3*(2*h-1), 3*(1-h)/2, 0, 3*h, 3*(1-h), 3*(1-h)/2]
            transversal = [-sp.Rational(i, 4) for i in B]
            assert sp.simplify(-6/(1-h)+2/h+2/(2*h-1)) == 0
        active = [i for i in range(1, n) if endpoint[i] != 0]
        b = sp.Rational(n-1-len(active), n)
        c = sp.Rational(n-1, n)
        first = c/2-b
        second = sp.simplify(b*b-c*c/2-2*sum(transversal[i]/endpoint[i] for i in active)/n)
        assert sp.simplify(at(mark)-endpoint[0]) == 0
        assert sp.simplify(dm/at(mark)+c/2-first) == 0
        assert sp.simplify(ddm/at(mark)-(dm/at(mark))**2-c*c/2-second) == 0
        report(q, side, len(active), n*b, first, second)


if __name__ == '__main__':
    main()
