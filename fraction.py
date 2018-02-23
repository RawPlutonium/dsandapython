class Fraction(object):
	"""docstring for Fraction"""
	def __init__(self,top,bottom):
		self.num = top
		self.den = bottom
	def __str__(self):
		return str(self.num)+"/"+str(self.den)
	def gcd(self,m,n):
		while m%n != 0:
			oldm = m
			oldn = n
			m = oldn
			n = oldm%oldn
		return n
	def __add__(self,otherfraction):
		newnum = self.num*otherfraction.den + self.den*otherfraction.num
		newden = self.den*otherfraction.den
		common = self.gcd(newnum,newden)
		return Fraction(newnum//common,newden//common)
	def __eq__(self,other):
		firstnum = self.num * other.num
		secondnum = other.num * self.den
		return firstnum == secondnum


f1 = Fraction(5,5)
f2 = Fraction(5,5)
f3 = f1+f2
print(f3)
