import coordinates as cd
import io as io
#import io engine and other stuff

hexList =[]
hexList = cd.generateHexList(8,12)
#print(hexList)






hexList[7][2] = '@'
#print(hexList)
updatedHexList = cd.moveCharDir('@', hexList, 0)

plainMapList = io.generatePlainMap()

updatedMapList = io.updateMap(updatedHexList, plainMapList, '@')

io.printMap(updatedMapList)



#io.printMap(plainMapList)
# def class main loop
