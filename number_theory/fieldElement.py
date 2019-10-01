# The class represents an element in a Field Fprime.

class FieldElement:
    ''' Constructing a Finite Field :
            A finite field is defined as a finite set of numbers and two operations + (addition) and ⋅ (multiplication) that satisfy the following:
                       1. If a and b are in the set, a + b and a ⋅ b are in the set. We call this property closed.
                       2. 0 exists and has the property a + 0 = a. We call this the additive identity.
                       3. 1 exists and has the property a ⋅ 1 = a. We call this the multiplicative identity.
                       4. If a is in the set, –a is in the set, which is defined as the value that makes a + (–a) = 0. This is what we call the additive inverse.
                       5. If a is in the set and is not 0, a–1 is in the set, which is defined as the value that makes a ⋅ a–1 = 1. This is what we call the multiplicative inverse
            In math notation the finite field set looks like this:
                        | Fp = {0, 1, 2, ..., p–1} |
                     For Finite Field Order 11 : F11 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
                     For Finite Field Order 17 : F17 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}
        '''

    def __init__(self, num, prime):
        if num < 0 or num >= prime:
            ''' Checking num is between 0 and prime-1 inclusive
                            If not, we get an invalid Field Element and we raise ValueError 
            '''
            raise ValueError("Number {} not in field range 0 to {}.".format(num, prime - 1))

        self.num = num
        self.prime = prime

    def __repr__(self):
        return "FieldElement_{}({})".format(self.prime, self.num)

    def __eq__(self, other):
        ''' __eq__ method checks equality of two objects of class FieldElement.
                    This is only true when the num and prime properties are equal.
        '''
        if other is None:
            return False

        return self.num == other.num and self.prime == other.prime

    def __ne__(self, other):
        ''' __ne__ method checks not equality of two objects of class FieldElement.
        '''
        if other is None:
            return False

        return not (self == other)

    def __add__(self, other):
        '''Finite Field Addition a+fb belongs to F_{p} i.e., (a+b)%p
                 Addition in a finite field is defined with modulo operator(%)
                 We have to return an instance of the class, which we can conveniently access with self.__class__.
        '''
        if self.prime != other.prime:
            raise TypeError("Cannot add two numbers in different fields")

        num = (self.num + other.num) % self.prime
        return type(self)(num, self.prime)

    def __sub__(self, other):
        '''Finite Field Subtraction a-fb belongs to F_{p} i.e., (a-b)%p
         Similarly, Subtraction in a finite field is defined with modulo operator(%)
        '''
        if self.prime != other.prime:
            raise TypeError("Cannot subtract two numbers in different fields")

        num = (self.num - other.num) % self.prime
        return type(self)(num, self.prime)

    def __mul__(self, other):
        if self.prime != other.prime:
            raise TypeError("Cannot multiply two numbers in different fields")

        num = (self.num * other.num) % self.prime
        return type(self)(num, self.prime)

    def __pow__(self, exponent):
        ''' Fermat’s little theorem that: a**(p–1) = 1
                a**(–3) = a**(–3) ⋅ a**(p–1) = a**(p–4)
                n = exponent
                while n < 0:
                    n += self.prime - 1
                We already know how to force a number out of being negative, using our familiar friend %!
        '''
        n = exponent % (self.prime - 1)
        num = pow(self.num, n, self.prime)

        return type(self)(num, self.prime)

    def __truediv__(self, other):
        ''' Use Fermat's little theorem:
            self.num**(p-1) % p == 1
            this means: 1/n == pow(n, p-2, p)
            we return an element of the same class
            In Python3, division is separated into __truediv__ and __floordiv__.
            The first does normal division(10/3 = 3.333) and the second does integer division(10/3 = 3).
        '''
        if self.prime != other.prime:
            raise ValueError("Cannot divide two numbers in different fields.")

        num = (self.num * pow(other.num, self.prime - 2, self.prime)) % self.prime
        return type(self)(num, self.prime)

    def __rmul__(self, coefficient):
        num = (self.num * coefficient) % self.prime

        return type(self)(num, self.prime)