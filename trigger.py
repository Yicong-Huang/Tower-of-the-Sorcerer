from item import Item

from ele_lib import *
from mob import Mob
from build import Build
class Trigger(Item):
    def __init__(self,i,j,name,floor):
        Item.__init__(self,i,j,name,floor)
        self._obj=lib[name].name.replace('_trigger2','').replace('_trigger','')
        self._case=lib[name].case
    
    def display(self, canvas,tick):
        self._tick=tick
        self._canvas=canvas
        self._item=eval(type(lib[self._obj]).__name__+'(self._i,self._j,self._obj,self._floor)')
        self._item.display(canvas,tick)

    