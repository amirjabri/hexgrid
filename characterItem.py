#define class for characters

class charClass:
	def __init__(self,symbol, x, y):
        	self.symbol = symbol
        	self.x = x
        	self.y = y

	def updateXY(self,newX,newY):
		self.x = newX
		self.y = newY
