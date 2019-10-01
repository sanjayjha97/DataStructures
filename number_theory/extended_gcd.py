# Extended Euclid's Algorithm : If d divides a and b and d = a*x + b*y for integers x and y, then d = gcd(a,b)


def extended_gcd(a, b):
    assert a >= 0 and b >= 0

    if b == 0:
        d, x, y = a, 1, 0
    else:
        (d, p, q) = extended_gcd(b, a % b)
        x = q
        y = p - q * (a // b)

    assert a % d == 0 and b % d == 0
    assert d == a * x + b * y

    return (d, x, y)


# Other form - When you want only output x and y not d = gcd(a,b)

def ExtendedEuclid(a, b):
    if b == 0:
        return (1, 0)
    (x, y) = ExtendedEuclid(b, a % b)
    k = a // b
    return (y, x - k * y)