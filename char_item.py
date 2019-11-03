''' this module define classes for characters
    CharClass: '''


class charClass:

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


class boxClass:
    '''class for box to push around and block doors and enemies'''

    def __init__(self, box_symbol, box_coords):
        self.box_symbol = box_symbol
        self.box_coords = box_coords

    def update_box_coords(self, new_box_coords):
        '''method docstring'''
        self.box_coords = box_coords


class ratClass:
    '''class for rat enemy'''

    def __init__(self, rat_symbol, rat_coords):
        self.rat_symbol = rat_symbol
        self.rat_coords = rat_coords
        
'''
class guardClass:

class switchClass:

class trapClass:

class hackingClass:

class trapDoorClass:

class portalClass:

class rolling landmine robots:

class hacking terminals:
'''
