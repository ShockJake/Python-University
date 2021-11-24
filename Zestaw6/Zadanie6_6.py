class Poly:
    def __init__(self, c=0, n=0) -> None:
        self.size = n + 1
        self.a = self.size * [0]
        self.a[self.size - 1] = c

    def __str__(self):
        return str(self.a)

    def __add__(self, other: object):
        if not isinstance(other, Poly):
            raise Exception("Trying to add two different objects")
        first_length = self.size
        second_length = other.size
        if first_length >= second_length:
            for i in range(first_length):
                self.a[i] += other.a[i]
            return self
        elif first_length < second_length:
            for i in range(other.size):
                other.a[i] += self.a[i]
            return other

    def __sub__(self, other: object):
        if isinstance(other, Poly) == False:
            raise Exception("Trying to add two different objects")
        if self.size >= other.size:
            newPoly = Poly(self.size)
        if self.size < other.size:
            newPoly = Poly(other.size)
        for i in range(newPoly.size):
            newPoly.a[i] = self.a[i]
        for i in range(newPoly.size):
            newPoly.a[i] -= other.a[i]
        return newPoly

    def __mul__(self, other):
        if isinstance(other, Poly) == False:
            raise Exception("Trying to add two different objects")
        if self.size < 1 or other.size < 1:
            raise Exception("There are empty Polynomals")
        result = Poly()
        for i in range((self.size - 1) + (other.size - 1) + 1):
            result[i] = 0
        for i in range(self.size):
            for j in range(other.size):
                result[i+j] += self.a[i] * other.a[j]
        return result

    def mul(self, n):
        for i in range(self.size):
            self.a[i] *= n
        return self

    def __pos__(self):
        for i in range(self.size):
            if self.a[i] < 0:
                self.a[i] *= -1
        return self

    def __neg__(self):
        for i in range(self.size):
            if self.a[i] > 0:
                self.a[i] *= -1
        return self

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Poly) == False:
            raise Exception("Trying to add two different objects")
        if self.size != other.size:
            return False
        for i in range(self.size):
            if self.a[i] != other.a[i]:
                return False
        return True

    def __ne__(self, other: object) -> bool:
        if isinstance(other, Poly):
            raise Exception("Trying to add two different objects")
        if self.size != other.size:
            return True
        for i in range(self.size):
            if self.a[i] != other.a[i]:
                return True
        return False

    def eval(self, x):
        result = 0
        for i in range(self.size - 1, -1, -1):
            result = self.a[i] + (x * result)
        return result

    def __pow__(self, n):
        if n == 0:
            return 1
        if n == 1:
            return self
        return (self * self.__pow__(self, n - 1))

    def dif(self):
        if self.size - 1 != 0:
            for i in range(self.size - 1):
                self.a[i] = (i + 1) * self.a[i + 1]
                self.a[i + 1] = 0
            return self
        return self
    
    def combine(self, other : object):
        if isinstance(other, Poly):
            raise Exception("Trying to add two different objects")
        result = Poly(self.size)
        for i in range(self.size):
            if i == 0:
                result.a[i] = self.a[i]
            else:
                wsp = pow(other, i)
                wsp.mul(self.a[i])
    # ----------------------------------
        
