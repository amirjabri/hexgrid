import coordinates as cd
import inout as io
import characterItem as ci

#import io engine and other stuff
#
hexList = cd.generateHexList(6,8) #eventually arbitrary size grid could be added
print(hexList)

char1 = ci.charClass('@',3,1)
print(char1.symbol)
print(char1.x)
print(char1.y)

char1.updateXY(2,2)

print(char1.x)
print(char1.y)

char1New = cd.newCharXY(char1,0)
print(char1New)
mapList1 = io.genMapList()
io.printMap(mapList1)
io.updateMap(mapList1, '@', char1New)
io.printMap(mapList1)
z = 0

while z < 10:
	print('which dir')
	dir = int(input())
	char1New = cd.newCharXY(char1,dir)
	io.updateMap(mapList1, '@', char1New)
	io.printMap(mapList1)
	z+=1

'''
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
# def class main loop
