from item import Item
import ele_lib

class Enhancement(Item):
    def __init__(self,i,j,name,floor):
        Item.__init__(self,i,j,name,floor)
        self._kind=ele_lib.lib[name].kind
        self._value=ele_lib.lib[name].value
        
    def interact(self,prot):
        if '_'in self._name:
            self._value=((self._floor._num-1)//10+1)*self._value
        exec('prot._'+self._kind +'+='+str(self._value))
        print(prot.__dict__)
        Item.interact(self,prot)