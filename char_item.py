''' this module define classes for characters
    CharClass: '''


class CharClass:

    '''class for character'''

    def __init__(self, char_symbol, char_coords, char_items):
        self.char_symbol = char_symbol
        self.char_coords = char_coords
        self.char_items = char_items

    def update_char_coords(self, new_char_coords):
        ''' method docstring '''
        self.char_coords = new_char_coords

    def update_char_items(self, new_char_items):
        ''' method docstring'''
        self.char_items = self.char_items + new_char_items


''' class boxClass:

class guardClass:

class switchClass:

class trapClass:

class hackingClass:

class trapDoorClass:

class portalClass:

class rolling landmine robots:

class hacking terminals:
'''
