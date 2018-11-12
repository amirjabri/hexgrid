#this program will be used as practice for the game

hex = [ ' /     ',
	'/      ',
	'\      ',
	' \_____',]

for i in range(25):
	print((hex[i%4] + hex[i%4-2])*5 + hex[i%4] )
     	
