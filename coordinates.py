import characterItem as ci

dirList = ((1, 1), (0, 2), (-1, 1), (-1, -1), (0, -2), (1, -1))
# generate coordinates for rectangular shape


def generateHexList(height, width):
    hexList = []
    x = 0
    while x < width:
        if x == 0 or x % 2 == 0:
            y = 0

            while y <= (height*2-1):
                hexList.append([x, y])
                y += 2
            if x % 2 == 1:

            y = 1

            while y < height*2:
                hexList.append([x, y])
                y += 2
        x += 1
    return hexList
# to do: generate coordinates for other shapes.


def getIndexFromXY(hexCoordList, XY):
    for i in range(len(hexCoordList)):
        if XY == hexCoordList[i][0:2]:
            return i


def calcNewXY(vec1, vec2):
    return [vec1[0] + vec2[0], vec1[1] + vec2[1]]


def newCharXY(charObj, direction):
    return calcNewXY(charObj.xy, dirList[direction])
