import coordinates as cd
import inout as io
import char_item as ci

# import io engine and other stuff

hexList = cd.generateHexList(6, 8)

Char1 = ci.charClass('@', [2, 2], [])

for i in range(100):
    print('which dir')
    dir = int(input())
    Char1.char_coords = cd.newCharXY(Char1, dir)
    print(chr(27) + "[2J")
    io.printMap(io.updateMap(io.genMapList(), Char1))

# planning for main game loop class spit out txt file for map on turn.
