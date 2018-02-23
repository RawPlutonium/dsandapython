class LogicGate(object):
	"""docstring for LogicGate"""
	def __init__(self, n):
		self.label = n
		self.output = None

	def getLabel(self):
		return self.label

	def getOutput(self):
		self.output = self.performGateLogic()
		return self.output
	def __str__(self):
		return str(self.getOutput())

class BinaryGate(LogicGate):
	"""docstring for BinaryGate"""
	def __init__(self,n):
		super().__init__(n)
		self.pinA = None
		self.pinB = None

	def getPinA(self):
		if self.pinA == None:
			return int(input("Enter Pin A input for gate "+ self.getLabel()+" --> "))
		else:
			return self.pinA.getFrom().getOutput()

	def getPinB(self):
		if self.pinB == None:
			return int(input("Enter Pin B input for gate "+ self.getLabel()+" --> "))
		else:
			return self.pinB.getFrom().getOutput()

	def setNextPin(self,source):
		if self.pinA == None:
			self.pinA = source
		else:
			if self.pinB == None:
				self.pinB = source
			else:
				raise RuntimeError("Error: NO EMPTY PINS")

class UnaryGate(LogicGate):
	"""docstring for UnaryGate"""
	def __init__(self,n):
		super().__init__(n)
		self.pin = None

	def getPin(self):
		if self.pin == None:
			return int(input("Enter Pin input for gate "+self.getLabel()+" --> "))
		else:
			return self.pin.getFrom().getOutput()

	def setNextPin(self,source):
		if self.pin == None:
			self.pin = source
		else:
			raise RuntimeError("Error: NO EMPTY PINS")


class AndGate(BinaryGate):
	"""docstring for UnaryGate"""
	def __init__(self,n):
		super().__init__(n)

	def performGateLogic(self):
		a = self.getPinA()
		b = self.getPinB()
		if a == 1 and b == 1:
			return 1
		else:
			return 0

class OrGate(BinaryGate):
	"""docstring for OrGate"""
	def __init__(self,n):
		super().__init__(n)

	def performGateLogic(self):
		a = self.getPinA()
		b = self.getPinB()
		if a == 1 or b == 1:
			return 1
		else:
			return 0 

class NotGate(UnaryGate):
	"""docstring for NotGate"""
	def __init__(self, n):
		super().__init__(n)
	
	def performGateLogic(self):
		a = self.getPin()
		if a == 1:
			return 0
		else:
			return 1

class Connector(object):
	"""docstring for Connector"""
	def __init__(self, fgate, tgate):
		self.fromgate = fgate
		self.togate = tgate

		tgate.setNextPin(self)

	def getFrom(self):
		return self.fromgate

	def getTo(self):
		return self.togate


		

g1 = AndGate("G1")
g2 = AndGate("G2")
g3 = OrGate("G3")
g4 = NotGate("G4")
c1 = Connector(g1,g3)
c2 = Connector(g2,g3)
c3 = Connector(g3,g4)
print(g4)
		

		
		
	