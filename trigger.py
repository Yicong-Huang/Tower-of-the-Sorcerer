'''Defining class Trigger, which is an Item, has a Mob or Build _obj representing
itself.'''
from item import Item

from ele_lib import LIB
exec('from mob import Mob')
exec('from build import Build')

class Trigger(Item):
    '''A Trigger refers to a Plot by its floor num and case num'''
    def __init__(self, i, j, name, floor):
        Item.__init__(self, i, j, name, floor)
        self._obj = LIB[name].name.replace('_trigger2', '').replace('_trigger', '')
        self._case = LIB[name].case

    def display(self, canvas, tick):
        self._tick = tick
        self._canvas = canvas
        self._item = eval(type(LIB[self._obj]).__name__+
                          '(self._i, self._j, self._obj, self._floor)')
        self._item.display(canvas, tick)
