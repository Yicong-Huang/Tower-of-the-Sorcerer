'''Defining class Collection, which mainly includs keys'''
from item import Item


class Collection(Item):

    def interact(self, prot):
        exec('prot._' + self._name + '+=1')
        Item.interact(self, prot)
        #self.playsound('src/sound/Sound 2 at frame 0.mp3')
