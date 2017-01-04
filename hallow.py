'''Defining class Hallow and LIB that contains infomation about Hallows'''
import ele_lib
import view
from dialogs import Infobox
from item import Item

LIB = {'transmit': [(33, 200), (33, 216)],
       'cross': [(33, 336)],
       'pickaxe': [(97, 208)],
       'st_water': [(97, 272)],
       'lucky_coin': [(97, 336)],
       'info_book': [(65, 208)],
       'ice': [(97, 304)],
       'earthquake': [(97, 240)],
       'key': [(33, 304)],
       'boom': [(65, 240)],
       'fly_up': [(33, 240)],
       'fly_down': [(33, 272)],
       'fly_oppo': [(65, 272)],
       'message': [(65, 304)],
       'dragon_dagger': [(65, 336)]}


class Hallow(Item):
    '''Hallows are special items that will help Protagonist. Some Hallows have usage limitations.
    Hallows can be collected and cliked on the left of the game frame.'''

    def __init__(self, i, j, name, floor):
        Item.__init__(self, i, j, name, floor)
        self._useable = True

    def interact(self, prot):
        Item.interact(self, prot)
        [view.MAIN.tag_bind(view.MAIN.create_image(
            i, j, image=image, tag=self._name), '<ButtonRelease>',
            lambda event: Hallow.clicked(self, prot, event))
            for image, (i, j) in zip([view.TRANSMIT_UP_ICON, view.TRANSMIT_DOWN_ICON]
                                     if self._name == 'transmit'
                                     else [ele_lib.LIB[self._name].image], LIB[self._name])]
        prot.get_value('hallows').add(self._name)
        if '_' + self._name in prot.__dict__:
            exec('prot._' + self._name + '=True')
        self._useable = True
        if self._name == 'fly_oppo':
            view.MAIN.create_text(75, 280, text='3')

    def clicked(self, prot, event):
        "use the Hallow when clikced in the GUI"
        print('clicked')
        print(self._useable, self._name)
        if self._useable:
            if self._name == 'info_book':
                Infobox(prot)
            elif self._name == 'transmit':
                def search_stairs(prot):
                    return any(type(prot.get_value('floor').get_floor(
                        prot.get_value('i') + i, prot.get_value('j') + j)).__name__ == 'Build'
                        and 'stairs' in prot.get_value('floor').get_floor(
                            prot.get_value('i') + i, prot.get_value('j') + j).get_value('name')
                        for i in [-1, 0, 1] for j in [-1, 0, 1])

                if search_stairs(prot) and event.y <= 208 and prot.get_value(
                        'tower').check_active('up'):
                    prot.set_value('floor', prot.get_value(
                        'tower').next_floor())
                    print(prot.get_value('floor').num)
                    if prot.get_value('floor').get_item('downstairs'):
                        prot.move_to(
                            *prot.get_value('floor').get_item('downstairs'))
                    else:
                        prot.move_to(5, 10)
                elif search_stairs(prot) and event.y > 208 and prot.get_value(
                        'tower').check_active('down'):
                    prot.set_value('floor', prot.get_value(
                        'tower').previous_floor())
                    prot.move_to(*prot.get_value('floor').get_item('upstairs'))
            elif self._name == 'earthquake':
                for i in [i for i in prot.get_value('floor').floor.values()
                          if i.get_value('name') == 'wall']:
                    i.disappear()
                # self._useable=False
            elif self._name == 'fly_down':
                prot.get_value('tower').current = prot.get_value('tower').tower[
                    prot.get_value('tower').get_num(prot.get_value('tower').current) - 1]
                # self._useable=False
            elif self._name == 'fly_up':
                prot.get_value('tower').current = prot.get_value('tower').tower[
                    prot.get_value('tower').get_num(prot.get_value('tower').current) + 1]
                # self._useable=False
            elif self._name == 'fly_oppo':
                prot.move_to(10 - prot.get_value('i'),
                             10 - prot.get_value('j'))
                # self._useable=False
            elif self._name == 'key':
                for i in [i for i in prot.get_value('floor').floor.values()
                          if 'yellow_door' in i.get_value('name')]:
                    i.disappear()
                # self._useable=False
            elif self._name == 'ice':
                self.selecting_remove(prot, ('lava'))
                # self._useable=False
            elif self._name == 'pickaxe':
                print('here', prot)
                self.selecting_remove(prot, ('wall'))
                # self._useable=False
            elif self._name == 'boom':
                self.selecting_remove(
                    prot, ('great_magic', 'fake_lord1',
                           'fake_lord2', 'dragon'),
                    mode=False, move_type='Mob')
                # self._useable=False

    def selecting_remove(self, prot, name, mode=True, move_type=None):
        print('removing')
        for (i, j) in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            test = prot.get_value('floor').get_floor(
                prot.get_value('i') + i, prot.get_value('j') + j)

            if test:

                if (test.get_value('name') in name) == mode:
                    if move_type:
                        if type(test).__name__ == move_type or\
                            (type(test).__name__ == 'Trigger'
                             and type(test.get_value('item')).__name__ == move_type):
                            hp, attack, defense, gold =\
                                prot.get_value('hp'), prot.get_value('attack'), prot.get_value(
                                    'defense'), prot.get_value('gold')
                            prot._attack *= 1000
                            prot._defense *= 1000
                            prot.move(i, j)
                            prot.move(-i, -j)
                            prot.set_value('hp', hp)
                            prot.set_value('attack', attack)
                            prot.set_value('defense', defense)
                            prot.set_value('gold', gold)
                    else:
                        print('disappearing', test)
                        test.disappear()
