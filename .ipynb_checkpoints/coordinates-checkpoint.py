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

#dr,d,dl,ul,u,ur
moveOne = ((1,1),(0,2),(-1,1),(-1,-1),(0,-2),(1,-1))
print(moveOne)


