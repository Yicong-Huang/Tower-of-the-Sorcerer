'''Defining class Build, which contains all doors, stairs and walls'''
from item import Item
from dialogs import ShopDialog

LIB = {(5, 3, 19):((5, 2), 'cross'),
       (9, 0, 12):((10, 0), 'merchant'),
       (9, 10, 16):((10, 10), 'st_water'),
       (8, 1, 41):((9, 1), 'pro_witch_trigger2'),
       (10, 1, 41):((9, 1), 'pro_witch_trigger2')}

class Build(Item):
    def interact(self, prot):
        if self._name in ('hidden_door', 'background'):
            entry = LIB.get((prot.get_value('i'), prot.get_value('j'), self._floor.num))
            if entry:
                prot.get_value('floor').set_floor(*entry[0], entry[1])
                if prot.get_value('floor').num == 41 and not prot.get_value('magic_defense'):
                    prot._hp -= 200
            else:
                super().interact(prot)

        elif self._name == 'hidden_wall':
            prot.get_value('floor').set_floor(*self.get_position(), 'wall')

        elif self._name == 'upstairs':
            prot.set_value('floor', prot.get_value('tower').next_floor())

            prot.move_to(*prot.get_value('floor').get_item('downstairs') or (5, 10))


        elif self._name == 'downstairs':
            prot.set_value('floor', prot.get_value('tower').previous_floor())
            prot.move_to(*prot.get_value('floor').get_item('upstairs'))

        elif self._name in ('yellow_door', 'blue_door', 'red_door'):
            if eval('prot._'+self._name[:-4]+'key'):
                exec('prot._'+self._name[:-4]+'key'+'-=1')
                super().interact(prot)
            else:
                print('need key!')
        elif self._name == 'shop_mid':
            ShopDialog(prot)
