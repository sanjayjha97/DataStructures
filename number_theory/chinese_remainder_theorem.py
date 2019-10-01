# Chinese Remainder Theorem:

# If GCD(a,b) = 1, then for any remainder ra modulo a and any remainder rb modulo b there exists integer n,
# such that n = ra (mod a) and n = ra(mod b).  If n1 and n2 are two such integers, then n1=n2(mod ab)

# Algorithm :

# 1. Use extended euclid algorithm to find such x,y that a*x + b*y = 1
# 2. Take n = ra*by + rb*ax

from extended_gcd import ExtendedEuclid
from modular_division import InvertModulo


# Uses ExtendedEuclid to find inverses
def ChineseRemainderTheorem(n1, r1, n2, r2):
    (x, y) = ExtendedEuclid(n1, n2)
    m = n1 * n2
    n = r2 * x * n1 + r1 * y * n2
    return ((n % m + m) % m)


# Same a above using InvertingModulo
def ChineseRemainderTheorem2(n1, r1, n2, r2):
    x, y = InvertModulo(n1, n2), InvertModulo(n2, n1)
    m = n1 * n2
    n = r2 * x * n1 + r1 * y * n2
    return (n % m + m) % m