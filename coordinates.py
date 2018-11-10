#playing with coordinates
# x,y x=colums , y = rows , a=terrain, b=resource,c=characters on hex
#  create list of lists
hexlist =[]
x=0

while x <= 7:
	
	if x==0 or x%2==0:
		y=0
		while y <= 10:
			hexlist.append([x,y,0,0,0]) 
			y+=2
	if x%2==1:
		y=1
		while y < 12:
			hexlist.append([x,y,0,0,0])
			y+=2
	x+=1
print(hexlist)
hex = hexlist[7]
print(hex)

hex[2] = '@'
print(hex)
hexlist[7] = hex
print(hexlist)
print(hex)
hex = hexlist[13]
print(hex)

moveOne = ((1,1),(0,2),(-1,1),(-1,-1),(0,-2),(1,-1))
'''def getindex(x,y,dir):
    for i in range(len(hexlist)):
        if '''

#prototype for pulling list of hex you need and then moving a character from that hex list to an adjacent list.
# want to move character one hex from x=1, y=3 in the up right direction (moveOne[5])
print('character is @ hex 1,3 and will move up right direction')

for a in range(len(hexlist)):
    hex = hexlist[a]
    if hex[2]== '@':
    	position = hex[0:2]
    	hex[2] = 0
    	hexlist[a] = hex
    	move = moveOne[5]
	newposition = [0,0]
    	newposition[0] = position[0] + move[0]
    	newposition[1] = position[1] + move[1]
    	hexindex = newposition[0]*6 + (newposition[1]/2)
    	newhex = hexlist[hexindex]
    	newhex[2] = '@'
    	hexlist[hexindex] = newhex
print(hexlist)    
    
print('print x, y from the list')

#dr,d,dl,ul,u,ur
#moveOne = ((1,1),(0,2),(-1,1),(-1,-1),(0,-2),(1,-1))
#print(moveOne)


