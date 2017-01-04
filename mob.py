'''Defining class Mob which can attack or be attacked by Protagonist'''
import ele_lib
from character import Character


class Mob(Character):
    '''A Mob interacts with Protagonist. It first calcultes the harm and then
    fight with Protagonist. Its information is stored in ele_lib and will be
    displayed by Hallow info'''

    def __init__(self, i, j, name, floor):
        Character.__init__(self, i, j, name, floor)
        values = ele_lib.LIB[name]
        self._attack = values.attack
        self._defense = values.defense
        self._hp = values.hp
        self._gold = values.gold

    def interact(self, prot):
        self.fight(prot)

    def fight(self, prot, attack_first=False):
        "fight with the Protagonist, when in mode attack_first, it attacks once more"
        attack = ((prot.get_value('cross') and ('zombie' in self._name
                                                or 'vampire'in self._name))
                  or(prot.get_value('dragon_dagger')
                     and ('dragon' in self.get_value('name'))) + 1)\
            * prot.get_value('attack')
        if attack > self.get_value('defense'):
            harm = self.calculate_harm(prot, attack_first)
            print(harm)
            if prot.get_value('hp') > harm:
                prot.add_value('hp', -harm)
                prot.add_value('gold', (prot.get_value(
                    'lucky_coin') + 1) * self._gold)
                self.disappear()
                prot.set_value('moved', True)
            else:
                print('hp will get too low')
        else:
            print('defense too high for attack')

    def calculate_harm(self, prot, attack_first=False):
        "returns the damage the Mob made to the Protagonist"
        attack = ((prot.get_value('cross') and ('zombie' in self._name
                                                or 'vampire'in self._name))
                  or(prot.get_value('dragon_dagger')
                     and ('dragon' in self._name)) + 1)\
            * prot.get_value('attack')
        if attack_first:
            hp = self._hp + prot.get_value('attack')
        else:
            hp = self._hp
        if attack > self._defense:
            harm = 0
            while hp > 0:
                hp -= attack - self._defense
                if hp > 0:
                    harm += self._attack - prot.get_value('defense')
            harm = max(harm, 0)
        else:
            harm = 'N.A'
        return harm
