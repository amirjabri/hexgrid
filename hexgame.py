import coordinates as cd
import io
#import io engine and other stuff

hexList =[]
hexList = cd.generateHexList() #eventually arbitrary size grid could be added
#print(hexList)


hexList[7][2] = '@'
#print(hexList)
updatedHexList = cd.moveCharDir('@', hexList, 0)

plainMapList = io.generatePlainMapList()

updatedMapList = io.updateMap(updatedHexList, plainMapList, '@')

io.printMap(updatedMapList)



#io.printMap(plainMapList)
# def class main loop
