def generateHexList():
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




def getIndexFromXY(list1, list2):
	for i in range(len(list2)):
		if list1 == list2[i][0:2]:
			return i

def indexFromChar(char,list):
	for i in range(len(list)):
    		if char == list[i][2]:
        		return i
def addXY(vec1,vec2):
    	vec3 = [vec1[0] + vec2[0], vec1[1] + vec2[1]]
    	return vec3
def getXYfromIndex(list,i):
    return list[1][0,2]
def moveCharDir(char,list, dir):
    
	dirList = ((1,1),(0,2),(-1,1),(-1,-1),(0,-2),(1,-1))
	oldIndex = indexFromChar(char,list)
	list[oldIndex][2] = 0
	list[getIndexFromXY(addXY(list[oldIndex][0:2], dirList[dir]),list)][2] = char
        return list
