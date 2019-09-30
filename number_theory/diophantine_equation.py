# Diophantine Equation : Given integers a,b,c ( at least one of a and b != 0), the diophantine equation
# a*x + b*y = c has a solution (where x and y are integers) iff gcd(a,b) divides c.


from euclids_algorithm import gcd
from extended_gcd import extended_gcd


def diophantine(a, b, c):
    assert c % gcd(a, b) == 0

    (d, x, y) = extended_gcd(a, b)
    r = c / d
    return (r * x, r * y)


# Lemma : if n|ab and gcd(a,n) = 1, then n|b.

# Finding All solutions of Diophantine Equations:

# Theorem : Let gcd(a,b) = d, a = d*p, b = d*q. If (x0,y0) is a solution of Diophantine Equation a*x + b*y = c.
# a*x0 + b*y0 = c, then all the solutions have the form a(x0 + t*q) + b(y0 - t*p) = c, where t is an arbitrary integer.

# n is the number of solution you want, n = 2 by default

def diophantine_allsoln(a, b, c, n=2):
    (x0, y0) = diophantine(a, b, c)
    d = gcd(a, b)
    p = a // d
    q = b // d

    for i in range(n):
        x = x0 + i * q
        y = y0 - i * p
        print(x, y)