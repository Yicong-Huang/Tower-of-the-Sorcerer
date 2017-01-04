'''Defining the base class of Collection, Hallow, and Enhancement. When interacts,
the Item will disappear, as the Item has been picked up'''
from display import Display


class Item(Display):

    def interact(self, prot):
        self.disappear()
        prot.set_value('moved', True)
