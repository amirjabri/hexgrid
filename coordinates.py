#playing with coordinates
# x,y x=colums , y = rows , a=terrain, b=resource,c=characters on hex
#  create list of lists


#hexagon list plus other contents
def generateHexList(x,y):
        hexList=[]
        for x in range(8):
	
	        if x==0 or x%2==0:
		        y=0
		        while y <= 10:
			        hexList.append([x,y,0,0,0,0,0]) 
			        y+=2
	        if x%2==1:
		        y=1
		        while y < 12:
			        hexList.append([x,y,0,0,0,0,0])
			        y+=2
        return hexList

Hex1 = generateHexList(8,12)
print(Hex1)

#setup characters


def getIndexFromXY(list):
	for i in range(len(hexList)):
		if list == hexList[i][0:2]:
			return i

def indexFromChar(char,list):
	for i in range(len(list)):
    		if char == list[i][2]:
        		return i
def addXY(vec1,vec2):
    	vec3 = [vec1[0] + vec2[0], vec1[1] + vec2[1]]
    	return vec3

#check moves and get neighbor hex
#    

def moveCharDir(char,list, dir):
    
	dirList = ((1,1),(0,2),(-1,1),(-1,-1),(0,-2),(1,-1))

	oldIndex = indexFromChar(char,list)
	
	hexList[oldIndex][2] = 0
	hexList[getIndexFromXY(addXY(hexList[oldIndex][0:2], dirList[dir]))][2] = char
	
	



