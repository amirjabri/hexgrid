import coordinates as cd
import io
import 





hexList =[]
hexList = cd.generateHexList(8,12)
print(hexList)

hexList[7][2] = '@'
print(hexList)
cd.moveCharDir('@', hexList, 0)
print(hexList)
