import coordinates as cd

hexToMap = {(0,0):(5,3), (0,2):(5,7), (0,4):(5,11), (0,6):(5,15), (0,8):(5,19), (0,10):(5,23),
	    (1,1):(12,5),(1,3):(12,9),(1,5):(12,13),(1,7):(12,17),(1,9):(12,21),(1,11):(12,25),
	    (2,0):(19,3),(2,2):(19,7),(2,4):(19,11),(2,6):(19,15),(2,8):(19,19),(2,10):(19,23),
            (3,1):(26,5),(3,3):(26,9),(3,5):(26,13),(3,7):(26,17),(3,9):(26,21),(3,11):(26,25),
            (4,0):(33,3),(4,2):(33,7),(4,4):(33,11),(4,6):(33,15),(4,8):(33,19),(4,10):(33,23),
            (5,1):(40,5),(5,3):(40,9),(5,5):(40,13),(5,7):(40,17),(5,9):(40,21),(5,11):(40,25),
            (6,0):(47,3),(6,2):(47,7),(6,4):(47,11),(6,6):(47,15),(6,8):(47,19),(6,10):(47,23),
            (7,1):(54,5),(7,3):(54,9),(7,5):(54,13),(7,7):(54,17),(7,9):(54,21),(7,11):(54,25)}

def genMapList():

        path = './hexgrid.txt'
        hexMap = open(path,'r')
        return hexMap.read().splitlines()

def printMap(list):
        for i in range(len(list)):
                print(list[i])

def insertChar(str, char, x):        
        return str[:x-1] + char + str[x:] 

def updateMap(hexList, plainMap, char):
        mapXY = hexToMap[cd.getXYfromIndex[cd.indexFromChar(hexList, char)]]
        newMap = plainMap
        newMap[mapXY[1]]= insertChar(mapXY[1],'@',mapXY[0])
        return newMap
        printMap(newMap)
