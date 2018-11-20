import coordinates as cd
#right now this part is hard coded. Need a script to be able to
#build map text file and hash table from first principles.
#that way any arbitrary hex shape can be defined and created along
#with hash table for manipulations or potentially from the parameters
#needed to describe the creation of the hex grid.

hexToMap = {(0,0):(5,2), (0,2):(5,6), (0,4):(5,10), (0,6):(5,14), (0,8):(5,18), (0,10):(5,22),
	    (1,1):(12,4),(1,3):(12,8),(1,5):(12,12),(1,7):(12,16),(1,9):(12,20),(1,11):(12,24),
	    (2,0):(19,2),(2,2):(19,6),(2,4):(19,10),(2,6):(19,14),(2,8):(19,18),(2,10):(19,22),
            (3,1):(26,4),(3,3):(26,8),(3,5):(26,12),(3,7):(26,16),(3,9):(26,20),(3,11):(26,24),
            (4,0):(33,2),(4,2):(33,6),(4,4):(33,10),(4,6):(33,14),(4,8):(33,18),(4,10):(33,22),
            (5,1):(40,4),(5,3):(40,8),(5,5):(40,12),(5,7):(40,16),(5,9):(40,20),(5,11):(40,24),
            (6,0):(47,2),(6,2):(47,6),(6,4):(47,10),(6,6):(47,14),(6,8):(47,18),(6,10):(47,22),
            (7,1):(54,4),(7,3):(54,8),(7,5):(54,12),(7,7):(54,16),(7,9):(54,20),(7,11):(54,24)}

def genMapList():
#hardcoded map, eventually will create a routine to generate based on the dimentions
        path = './hexgrid.txt'
        hexMap = open(path,'r')
        return hexMap.read().splitlines()

def printMap(list):
        for i in range(len(list)):
                print(list[i])

def insertChar(lineToEdit, asciiChar, asciiPos):        
        return lineToEdit[:asciiPos-1] + asciiChar + lineToEdit[asciiPos:] 
#need to update map with character inserted in the correct position. get xy of character from before and use hash table to get
# corresponding value on the printed ascii map, then insert in that x,y value using string in the list index.

def updateMap(mapList, charObj):
	#mapList = genMapList()
	rowIndexToEdit = hexToMap[tuple(charObj.xy)][1]
	lineToEdit = mapList[rowIndexToEdit]
	asciiPositionToInsert = hexToMap[tuple(charObj.xy)][0]
	newLine = insertChar(lineToEdit, charObj.symbol, asciiPositionToInsert)
	mapList[rowIndexToEdit]=newLine
	return mapList
