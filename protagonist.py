'''Defining class Protagonist, which is the main character of the game. It can move, interact with
other Items and Characters.'''

import ele_lib
from character import Character
from plot import Plot
from trigger import Trigger

exec('from enhancement import Enhancement')
exec('from floor import Floor')
exec('from hallow import Hallow')
exec('from mob import Mob')
exec('from build import Build')
exec('from collection import Collection')


class Protagonist(Character):
    '''Main character'''

    def __init__(self, name, tower, **kargs):
        self._tower = tower
        for key, value in kargs.items():
            exec('self._' + key + '=' + value)
        Character.__init__(self, self._i, self._j, name, tower.current)

    def move(self, di, dj):
        "move the Protagonist and interact with other Items and Characters"

        temp_i = self._i + di
        temp_j = self._j + dj

        self._floor = self._tower.current
        attempt = self._floor.get_floor(temp_i, temp_j)

        if attempt and not isinstance(attempt, str):
            print(attempt.get_value('name'))
        self._moved = False
        self._interacted = False
        self._case = False

        if isinstance(attempt, Trigger):

            self._case = attempt.get_value('case')
            # print(attempt.__dict__)
            attempt = eval(type(ele_lib.LIB[
                attempt.get_value('obj')]).__name__ + '(temp_i, temp_j, attempt._obj, self._floor)')

        if attempt and not isinstance(attempt, str):
            attempt.interact(self)

        else:
            self._moved = True
        if not self.get_value('magic_defense') and self._floor.num > 40:
            for (i, j) in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                test = self._floor.get_floor(temp_i + i, temp_j + j)
                if test and not isinstance(test, str):
                    if 'pri_witch' in test.get_value('name'):
                        self.add_value('hp', -100)
                    elif 'pro_witch' in test.get_value('name'):
                        self.add_value('hp', -200)
                    elif 'magic_guard' in test.get_value('name'):
                        oppo_test = self._floor.get_floor(
                            temp_i - i, temp_j - j)
                        if oppo_test and not isinstance(oppo_test, str) \
                                and 'magic_guard' in oppo_test.get_value('name'):
                            self.set_value('hp', self.get_value('hp') // 2)
                            break
        if self._moved and 0 <= temp_i < 11 and 0 <= temp_j < 11:
            self._i, self._j = temp_i, temp_j

        if self._interacted:
            self._floor.del_floor(self._i, self._j)

        if self._case:
            if self._floor.num == 3:
                self._floor = self._tower.previous_floor()
                self.move_to(2, 7)
                self._hp = 400
                self._attack = 10
                self._defense = 10
            else:
                Plot(self._floor, self._case, self)

    def __str__(self):
        if not self.get_value('hallows'):
            hallows = 'set()'
        else:
            hallows = self.get_value('hallows')
        return '/'.join([str(a) for a in [
            self._i, self._j, self.get_value('hp'), self.get_value('attack'),
            self.get_value('defense'), self.get_value(
                'gold'), self.get_value('floor').num,
            self.get_value('yellow_key'), self.get_value(
                'blue_key'), self.get_value('red_key'),
            self.get_value('shop'), self.get_value(
                'cross'), self.get_value('lucky_coin'),
            self.get_value('dragon_dagger'), self.get_value(
                'magic_defense'), hallows
        ]])
