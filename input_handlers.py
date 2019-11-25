import tcod as libtcod

def handle_keys(key):
    key_char = chr(key.c)

    if key_char == 'l':
        return {'move': (1,1)}
    elif key_char == 'k':
        return {'move': (0,2)}
    elif key_char == 'j':
        return {'move': (-1,1)}
    elif key_char == 'u':
        return {'move': (-1,-1)}
    elif key_char == 'i':
        return {'move': (0,-2)}
    elif key_char == 'o':
        return {'move': (1,-1)}

    if key.vk == libtcod.KEY_ESCAPE:
        return {'exit': True}

    return {}

