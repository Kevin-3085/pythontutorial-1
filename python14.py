import math

class Rational:
    def __init__(self, num, den):
        self.num = num
        self.den = den
        self.reduce()

    def reduce(self):
        gcd = math.gcd(self.num, self.den)
        self.num //= gcd
        self.den //= gcd

    def __str__(self):
        return f"{self.num}/{self.den}"

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

    def __add__(self, other):
        return Rational(self.num*other.den + other.num*self.den,
                        self.den * other.den)

    def __sub__(self, other):
        return Rational(self.num*other.den - other.num*self.den,
                        self.den * other.den)

    def __mul__(self, other):
        return Rational(self.num * other.num,
                        self.den * other.den)

    def __eq__(self, other):
        return self.num == other.num and self.den == other.den

    def __lt__(self, other):
        return self.num * other.den < other.num * self.den

    def __gt__(self, other):
        return self.num * other.den > other.num * self.den


# Example
r1 = Rational(2, 4)
r2 = Rational(3, 5)

print("Add:", r1 + r2)
print("Sub:", r1 - r2)
print("Mul:", r1 * r2)
