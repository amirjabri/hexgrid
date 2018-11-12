data = [[1,1,0], [1,3,0], [2,2,0],[1,3,0]]
search = [1,3]
for i in range(len(data)):
    print(data[i])
for i in range(len(data)):
    
    if data[i][0:2]==search:
        print(i)


