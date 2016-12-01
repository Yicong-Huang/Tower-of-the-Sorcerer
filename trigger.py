from item import Item

import ele_lib
from mob import Mob
class Trigger(Item):
    def __init__(self,i,j,name,floor):
        Item.__init__(self,i,j,name,floor)
        self._obj=ele_lib.lib[name].obj
        self._case=ele_lib.lib[name].case
    
    