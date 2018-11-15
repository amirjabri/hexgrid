import coordinates as cd
import inout as io
#import io engine and other stuff

hexList =[]
hexList = cd.generateHexList() #eventually arbitrary size grid could be added
#print(hexList)


hexList[7][2] = '@'
#print(hexList)
updatedHexList = cd.moveCharDir('@', hexList, 0)

plainMapList = io.genMapList()

updatedMapList = io.updateMap(updatedHexList, plainMapList, '@')

io.updateMap(hexList,plainMap,'@')



#io.printMap(plainMapList)
# def class main loop
