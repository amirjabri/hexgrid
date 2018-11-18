import coordinates as cd
import inout as io
import characterItem as ci

#import io engine and other stuff
#
hexList = cd.generateHexList(6,8)
#print(hexList)

char1 = ci.charClass('@',[2,2])
#print(char1.symbol)
#print(char1.xy)

char1.updateXY([3,3])
#print(char1.xy)

char1.updateXY(cd.newCharXY(char1,0))
#print(char1.xy)

mapList1 = io.genMapList()
#io.printMap(mapList1)
#print(io.hexToMap[tuple(char1.xy)])




turn=0
while turn < 10:
	#print(chr(27) + "[2J")
	print('which dir')
	dir = int(input())
	char1.xy = cd.newCharXY(char1,dir)
	io.updateMap(mapList1, char1)
	io.printMap(mapList1)
	print('next turn press 1')
	next = input()
	print(chr(27) + "[2J")
	turn+=1

# main game loop class spit out txt file for map for each turn.
