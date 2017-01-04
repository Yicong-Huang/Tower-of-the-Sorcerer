'''
Defining class Display for all Objs to display on tkinter
'''
from ele_lib import LIB, set_image
from obj import Obj


class Display(Obj):
    '''relating methods for Obj display'''
    tick = True

    def __init__(self, i, j, name, floor):
        super().__init__(i, j)
        self._name = name
        self._floor = floor

    def get_location(self):
        "returns the position x, y of the Obj"
        self._x, self._y = self._i * Obj.side + 35 + 125, self._j * Obj.side + 41
        return self._x, self._y

    def display(self, canvas, tick):
        "displays the Obj on the game board"

        set_image(self)
        self._image = LIB[self._name].image[tick] \
            if isinstance(LIB[self._name].image, tuple)\
            else LIB[self._name].image
        self._tag = canvas.create_image(*self.get_location(),
                                        image=self._image, tag='redraw')

    def disappear(self):
        "makes the Obj disappear from the game board"
        try:
            if self._name in self._floor.get_floor(self._i, self._j).get_name():
                self._floor.del_floor(self._i, self._j)
        except:
            pass

    def move_to(self, i, j):
        "moves the Obj to the given position"
        if type(self).__name__ != 'Protagonist':
            self.disappear()
            self._floor.set_floor(i, j, self._name)
        self._i, self._j = i, j

    def get_name(self):
        return self._name
