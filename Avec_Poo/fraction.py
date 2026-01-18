from math import lcm
class Fraction:
    def __init__(self,num,den):
        self.num = num
        self.den = den

    def __str__(self):
        return f"la fraction est {self.num}/{self.den}"

    def __repr__(self):
        return f"Fraction({self.num},{self.den})"

    def __add__(self,other):
        res_den=lcm(self.den,other.den)
        res_num=self.num*(res_den//self.den)+other.num*(res_den//other.den)
        return Fraction(res_num,res_den)

    def __neg__(self):
         if self.den > 0:
            return Fraction(-self.num, self.den)
         return Fraction(self.num, -self.den)

    def __sub__(self,other):
        return self+(-other)

    def __mul__(self,other):
        return Fraction(self.num*other.num,self.den*other.den)

    def __eq__(self,other):
        return self.num*other.den == self.den*other.num


