import coordinates as cd
import inout as io
import characterItem as ci
import os
import random
import curses
from cursed import CursedApp, CursedWindow

#import io engine and other stuff
#


hexList = cd.generateHexList(6,8)

char1 = ci.charClass('@',[2,2], [],[])

def getMap:
	for i in range(100):
		print('which dir')
		dir = int(input())
		char1.xy = cd.newCharXY(char1,dir)
		print(chr(27) + "[2J")
		return io.updateMap(io.genMapList(), char1)

# eventually planning for  main game loop class spit out txt file for map for each turn.
#!/usr/bin/env python

app = CursedApp()

'''
class MainWindow(CursedWindow):

    X, Y = 0, 0
    WIDTH, HEIGHT = 5, 5
    BORDERED = True

    @classmethod
    def update(cls):
        cls.write(
          
        cls.trigger('quit')

'''

class MainPad(CursedWindow):

    X, Y = 0, 0
    WIDTH, HEIGHT = 'max', 'max'
    PAD = True
    PAD_WIDTH, PAD_HEIGHT = len(io.genMapList()[0]), len(io.genMapList()) 
    PAD_X, PAD_Y = 0, 0

    MAP = generate_map(PAD_WIDTH, PAD_HEIGHT)

    @classmethod
    def update(cls):
        key = cls.getch()
        if key is not None:
            if key == curses.KEY_UP:
                cls.PAD_Y = max(cls.PAD_Y - 1, 0)
            elif key == curses.KEY_DOWN:
                cls.PAD_Y = min(
                    cls.PAD_Y + 1,
                    cls.PAD_HEIGHT - (cls.HEIGHT + 1)
                )
            elif key == curses.KEY_LEFT:
                cls.PAD_X = max(cls.PAD_X - 1, 0)
            elif key == curses.KEY_RIGHT:
                cls.PAD_X = min(
                    cls.PAD_X + 1,
                    cls.PAD_WIDTH - (cls.WIDTH + 1)
                )
            elif key == ord('q'):
                cls.trigger('quit')
        for y in range(cls.PAD_Y, cls.PAD_Y + cls.HEIGHT):
            s = cls.MAP[y][cls.PAD_X:cls.PAD_X + cls.PAD_HEIGHT]
            s = ''.join(x for x in s)
            cls.addstr(s, cls.PAD_X, y)
        cls.refresh()


result = app.run()
result.unwrap()
