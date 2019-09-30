# Euclid's Lemma :  d divides a and b, if and only if d divides a-b and b

# Euclid's Algorithm

def gcd(a, b):
    if a < b:
        a, b = b, a

    while a % b != 0:
        a, b = b, a % b

    return b


# Recursive Euclid's Algorithm

def recursive_gcd(a, b):
    if b == 0:
        return a
    return recursive_gcd(b, a % b)