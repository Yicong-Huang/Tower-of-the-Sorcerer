'''Defining class Enhancement which will affect Protagonist's data'''
import ele_lib
from item import Item


class Enhancement(Item):
    '''If interacted, it will increase some part of Protagonist'''

    def __init__(self, i, j, name, floor):
        Item.__init__(self, i, j, name, floor)
        self._kind = ele_lib.LIB[name].kind
        self._value = ele_lib.LIB[name].value

    def interact(self, prot):
        if '_' in self._name:
            self._value = ((self._floor.num - 1) // 10 + 1) * self._value
        exec('prot._' + self._kind + '+=' + str(self._value))
        print(prot.__dict__)
        if self._name == 'shield5':
            prot.set_value('magic_defense', True)
        Item.interact(self, prot)
