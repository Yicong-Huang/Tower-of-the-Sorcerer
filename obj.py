'''
Defining the base class Obj for all classes
'''
class Obj:
    '''everything of the game is a Obj object.'''
    side = 32
    def __init__(self, i, j):
        self._i, self._j = i, j
    def get_position(self):
        "returns the i,j position of the Obj"
        return self._i, self._j
    def set_position(self, i, j):
        "sets the i,j position of the Obj as provided"
        self._i, self._j = i, j
