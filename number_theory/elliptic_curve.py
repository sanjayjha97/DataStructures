#  Elliptic curves are useful because of something called point addition.
#  Point addition is where we can do an operation on two of the points on the curve and get a third point, also on the curve.
#  It turns out that for every elliptic curve, a line will intersect it at either one point or three points, except in a couple of special cases it intersect at two points.
#  The two exceptions are when a line is exactly vertical and when a line is tangent to the curve.

#  The class represents a points in an Elliptic Curve

from fieldElement import FieldElement


class Point:
    '''Elliptic curves have a form like this:  y**2 = x**3 + ax + b
           Specifically, the elliptic curve used in Bitcoin is called secp256k1 and it uses this particular equation:
                                    ||    y**2 = x**3 + 7     ||
           The canonical form is y**2 = x**3 + ax + b, so the curve is defined by the constants a = 0, b = 7
    '''

    def __init__(self, x, y, a, b):
        self.x, self.y, self.a, self.b = x, y, a, b

        if self.x is None and self.y is None:
            return

        if self.y ** 2 != self.x ** 3 + a * x + b:
            raise ValueError("({},{}) is not on the curve.".format(x, y))

    def __repr__(self):
        if self.x is None:
            return 'Point(infinity)'
        elif isinstance(self.x, FieldElement):
            return 'Point({},{})_{}_{} FieldElement({})'.format(self.x.num,
                                                                self.y.num, self.a.num, self.b.num, self.x.prime)
        else:
            return 'Point({],{})_{}_{}'.format(self.x, self.y, self.a, self.b)

    def __eq__(self, other):
        '''Points are equal if and only if they are on the same curve and have the same coordinates.
        '''
        return self.x == other.x and self.y == other.y and self.a == other.a and self.b == other.b

    def __ne__(self, other):
        return not (self == other)

    def __add__(self, other):
        if self.a != other.a or self.b != other.b:
            raise TypeError("Points ({},{}) are not on the curve.".format(self, other))

        # self.x being None means that self is the point at infinity, or the additive identity.
        # Thus, we return other.
        if self.x is None:
            return other

        # other.x being None means that other is the point at infinity, or the additive identity.
        # Thus, we return self.
        if other.x is None:
            return self

        # Case 1: self.x == other.x, self.y != other.y
        # Result is point at infinity
        if self.x == other.x and self.y != other.y:
            return type(self)(None, None, self.a, self.b)

        # Case 2: self.x ≠ other.x
        # Formula (x3,y3)==(x1,y1)+(x2,y2)
        # s=(y2-y1)/(x2-x1)
        # x3=s**2-x1-x2
        # y3=s*(x1-x3)-y1
        if self.x != other.x:
            s = (other.y - self.y) / (other.x - self.x)
            x = s ** 2 - self.x - other.x
            y = s * (self.x - x) - self.y

            return type(self)(x, y, self.a, self.b)

        # Case 3: self == other
        # Formula (x3,y3)=(x1,y1)+(x1,y1)
        # s=(3*x1**2+a)/(2*y1)
        # x3=s**2-2*x1
        # y3=s*(x1-x3)-y1
        if self == other:
            s = (3 * self.x ** 2 + self.a) / (2 * self.y)
            x = s ** 2 - 2 * self.x
            y = s * (self.x - x) - self.y

            return type(self)(x, y, self.a, self.y)

        # Case where the tangent line is vertical
        # If the two points are equal and the y coordinate is 0, we return the point at infinity.
        if self == other and self.y == 0 * self.x:
            return type(self)(None, None, self.a, self.b)

    # __rmul__ is used to override the front multiplication
    # Binary Expansion that allow us to perform multiplication in log2(n) loops
    # Scalar Multiplication for Elliptic Curves
    # Performing scalar multiplication is straightforward, but doing the opposite point division is not
    # This is called the discrete log problem and is the basis of elliptic curve cryptography
    def __rmul__(self, coefficient):
        coef = coefficient
        current = self
        res = type(self)(None, None, self.a, self.b)

        while coef:
            if coef & 1:
                res += current
            current += current
            coef >>= 1
        return res