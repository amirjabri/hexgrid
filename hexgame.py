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

io.updateMap(mapList1, char1)
io.printMap(mapList1)

'''
while z < 10:
	print('which dir')
	dir = int(input())
	char1New = cd.newCharXY(char1,dir)
	io.updateMap(mapList1, '@', char1New)
	io.printMap(mapList1)
	z+=1


hexList[7][2] = '@'
#print(hexList)
updatedHexList = cd.moveCharDir('@', hexList, 0)

plainMapList = io.genMapList()
print(plainMapList)
print(plainMapList[2])
print(plainMapList[6])
print(plainMapList[10])
updatedMapList = io.updateMap(updatedHexList, plainMapList, '@')

io.updateMap(hexList,plainMap,'@')

'''

#io.printMap(plainMapList)
# main game loop class
