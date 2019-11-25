import tcod as libtcod



def grid_gen(con, screen_width, screen_height, colors):
    list1 = []
    for y in range(screen_height):
        for x in range(screen_width):
            if ((x%2 == 0 and y%2 ==0) or (x%2 == 1 and y%2 == 1)):
                list2 = [x, y]
                list1.append(list2)
    hexTuple = tuple(list1)
    for z in range(len(hexTuple)):
        libtcod.console_set_default_foreground(con, colors.get('dark_ground'))
        libtcod.console_put_char(con, hexTuple[z][0], hexTuple[z][1], '*', libtcod.BKGND_NONE)

def render_all(con, entities, game_map, screen_width, screen_height, colors):
    
   # for y in range(game_map.height*6):
      #  for x in range(game_map.width*10):

           #wall = game_map.tiles[x][y].block_sight

           # if wal
           #     libtcod.console_set_default_foreground(con, colors.get('dark_wall'))
           #     libtcod.console_put_char(con, x, y, '#', libtcod.BKGND_NONE) 
           # if ((x%2 == 0 and y%2 == 0) or (x%2 == 1 and y%2 == 1)):
           #     libtcod.console_set_default_foreground(con, colors.get('dark_ground'))
           #     libtcod.console_put_char(con, x, y, '*', libtcod.BKGND_NONE)

    for entity in entities:
        draw_entity(con, entity)

    libtcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)

def clear_all(con, entities):
    for entity in entities:
        clear_entity(con, entity)

def draw_entity(con, entity):
    libtcod.console_set_default_foreground(con, entity.color)
    libtcod.console_put_char(con, entity.x, entity.y, entity.char, libtcod.BKGND_NONE)

def clear_entity(con, entity):
    libtcod.console_put_char(con, entity.x, entity.y, '*', libtcod.BKGND_NONE)
