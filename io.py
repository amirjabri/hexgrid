import coordinates as cd
'''
grid spaces: x=e5,o12,e19,o26,e33,o40,e47,o54, 
yeven=3,7,11,15,19 yodd=5,9,13,17,21
'''
hexToMap = {(0,0):(5,3), (0,2):(5,7), (0,4):(5,11), (0,6):(5,15), (0,8):(5,19), (1,}
print(hexToMap[(0,10)])

def generatePlainMap():

        path = './hexgrid.txt'
        hexMap = open(path,'r')
        plainMapList = hexMap.read().splitlines()
        return plainMapList

def printMap(list):
        for i in range(len(list)):
                print(list[i])

def insertChar(str, char, x):        
        return str[:x-1] + char + str[x:] 

def updateMap(hexList, plainMap, char):
        xy = cd.getXYfromIndex[cd.indexFromChar(hexList, char)]
        



