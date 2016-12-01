from item import Item

class Collection(Item):
    def interact(self,prot):
        exec('prot._'+self._name + '+=1')
        Item.interact(self,prot)