from character import Character
from pprint import pprint
import ele_lib
from floor import Floor
from plot import Plot

from enhancement import Enhancement
from collection import Collection
from character import Character
from build import Build
from hallow import Hallow
from trigger import Trigger
from mob import Mob

class Protagonist(Character):
    def __init__(self, name, tower, **kargs):

        values=ele_lib.LIB[name]
        self._tower=tower
        for key, value in kargs.items():
            exec('self._'+key+'='+value)
        Character.__init__(self, self._i, self._j, name, tower.current)



    def change_image(self, direction):

        self._image=image


    def move(self, di, dj):

        temp_i=self._i+di
        temp_j=self._j+dj

        self._floor = self._tower.current
        attempt=self._floor.get_floor(temp_i, temp_j)


        if attempt and not isinstance(attempt, str):
            print(attempt._name)
        self._moved=False
        self._interacted=False
        self._case=False

        if isinstance(attempt, Trigger):

            self._case=attempt._case
            #print(attempt.__dict__)
            attempt=eval(type(ele_lib.LIB[attempt._obj]).__name__+'(temp_i, temp_j, attempt._obj, self._floor)')



        if attempt and not isinstance(attempt, str):
            attempt.interact(self)

        else:
            self._moved=True
        if not self._magic_defense and self._floor._num>40:
            for (i, j ) in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                test=self._floor.get_floor(temp_i+i, temp_j+j)
                if test and not isinstance(test, str):
                    if 'pri_witch' in test._name:
                        self._hp-=100
                    elif 'pro_witch' in test._name:
                        self._hp-=200
                    elif 'magic_guard' in test._name:
                        oppo_test=self._floor.get_floor(temp_i-i, temp_j-j)
                        if oppo_test and not isinstance(oppo_test, str) and 'magic_guard' in oppo_test._name:
                            self._hp=self._hp//2
                            break
        if self._moved and 0<=temp_i<11 and 0<=temp_j<11:
            self._i, self._j=temp_i, temp_j

        if self._interacted:
            self._floor.del_floor(self._i, self._j)

        if self._case:
            if self._floor._num == 3:
                self._floor=self._tower.previous_floor()
                self.move_to(2, 7)
                self._hp=400
                self._attack=10
                self._defense=10
            else:
                Plot(self._floor, self._case, self)

    def __str__(self):
        if not self._hallows:
            hallows='set()'
        else:
            hallows=self._hallows
        return '/'.join([str(a) for a in [self._i, self._j, 
            self._hp, self._attack, self._defense, self._gold, 
            self._floor._num, self._yellow_key, self._blue_key, 
            self._red_key, self._shop, self._cross, self._lucky_coin, 
            self._dragon_dagger, self._magic_defense, hallows
            ]])
