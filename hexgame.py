import coordinates as cd
import inout as io
import characterItem as ci

#import io engine and other stuff
#
hexList = cd.generateHexList(6,8)

char1 = ci.charClass('@',[2,2], [],[])

for i in range(100):
	print('which dir')
	dir = int(input())
	char1.xy = cd.newCharXY(char1,dir)
	print(chr(27) + "[2J")
	io.printMap(io.updateMap(io.genMapList(), char1))

# eventually planning for  main game loop class spit out txt file for map for each turn.
