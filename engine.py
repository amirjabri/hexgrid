import tcod as libtcod
from input_handlers import handle_keys
from entity import Entity
from render_functions import clear_all, render_all, grid_gen
from map_objects.game_map import GameMap

def main():
    screen_width = 120
    screen_height = 70
    map_width = 120
    map_height = 70

    colors = {
        'dark_wall': libtcod.Color(0, 0, 100),
        'dark_ground': libtcod.Color( 50, 50, 150)}


    player = Entity(0, 0, '@', libtcod.white)
    npc = Entity(5, 2, '$', libtcod.yellow)
    entities = [npc, player]    

    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

    libtcod.console_init_root(screen_width, screen_height, 'libtcod hexmod', False)
    con = libtcod.console_new(screen_width, screen_height)

    game_map = GameMap(map_width, map_height)
    
    key = libtcod.Key()

    mouse = libtcod.Mouse()

    grid_gen(con, screen_width, screen_height, colors)

    while not libtcod.console_is_window_closed():
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)

        render_all(con, entities, game_map, screen_width, screen_height, colors)
        libtcod.console_flush()
        clear_all(con, entities)
        action = handle_keys(key)
 
        move = action.get('move')
        exit = action.get('exit')


        if move:
            dx, dy = move
            if not game_map.is_blocked(player.x + dx, player.y + dy):
           
                player.move(dx,dy)

        if exit:
            return True


if __name__ == '__main__':
    main()






