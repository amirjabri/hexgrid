#define class for characters

class charClass:
	def __init__(self,symbol, xy):
        	self.symbol = symbol
        	self.xy = xy
        	
	def updateXY(self,newXY):
		self.xy = newXY
