'''
Defining class Floor which contains all info for a single floor
'''
from floor import Floor
from protagonist import Protagonist


class Tower():
    '''containing all methods for tower, which contains mutilble Floors. And
    also includes methods for loading and saving game.'''

    def __init__(self, floors: list):
        self._tower = floors
        self._height = len(floors)
        self._current = floors[0]

    def add(self, floor):
        self._tower.append(floor)

    def go_to(self, num):
        self._current = self._tower[num]

    @property
    def tower(self):
        return self._tower

    @property
    def current(self):
        return self._current

    @current.setter
    def current(self, value):
        self._current = value

    @staticmethod
    def load_tower(flo, newgame=True):
        with open(flo, 'r') as file:
            temp_tower = []
            if newgame:
                pass
            for n, line in enumerate(file, 0):
                if n != 51:
                    temp_floor = {}
                    line = line.strip('\n').strip('(').strip(')').split(')((')
                    for entry in line:
                        point, item = entry.split('), ')
                        i, j = point.split(', ')

                        temp_floor.update({(int(i), int(j)): item.strip("'")})
                    temp_tower.append(Floor(n, *temp_floor.items()))

                else:
                    tower = Tower(temp_tower)
                    tower.current = tower.tower[
                        int(line.strip('\n').split('/')[6])]
                    temp = zip(['i', 'j', 'hp', 'attack', 'defense', 'gold',
                                'num', 'yellow_key', 'blue_key', 'red_key',
                                'shop', 'cross', 'lucky_coin', 'magic_defense',
                                'dragon_dagger', 'hallows'],
                               line.strip('\n').split('/'))
                    prot = Protagonist('protagonist', tower,
                                       **dict([i for i in temp]))
            return tower, prot

    def save_tower(self, prot):
        with open('game1.sav', 'w') as file:
            for floor in self._tower:
                file.write(str(floor) + '\n')
            file.write(str(prot))

    def __iter__(self):
        for floor in self._tower:
            yield floor

    def get_num(self, floor):
        return self._tower.index(floor)

    def check_active(self, direction):
        return self.tower[self.get_num(self.current) + {'up': 1, 'down': -1}[direction]].active

    def next_floor(self):
        "sets and returns the current to the next floor"
        if self.current != self._tower[-1] and self.current.num != 43:
            self.current = self._tower[self.get_num(self.current) + 1]
        elif self.current.num == 43:
            self.current = self.tower[self.get_num(self.current) + 2]
        self.current.active = True
        return self.current

    def previous_floor(self):
        "sets and returns the current to the previous floor"
        if self.current != self.tower[0] and self.current.num != 45:
            self.current = self.tower[self.get_num(self.current) - 1]
        elif self.current.num == 45:
            self.current = self.tower[self.get_num(self.current) - 2]
        return self.current
