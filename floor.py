'''
Defining class Floor which contains all info for a single floor
'''
from build import Build


class Floor:
    '''a floor is initally a dict of strings, when loaded, it is a dict of
    different types of Objs, could be Item or Character'''

    def __init__(self, n, *args):
        self._num = n
        self._floor = {}
        for point, item in args:
            self.set_floor(*point, item)
        self._active = False

    def set_floor(self, i, j, item):
        self._floor[(i, j)] = item

    def get_floor(self, i, j):
        return self._floor.get((i, j))

    def del_floor(self, i, j):
        self._floor.pop((i, j))

    def get_item(self, name):
        for (i, j), item in self._floor.items():
            if (isinstance(item, str) and item == name) or \
                    (isinstance(item, Build) and item.get_name() == name):
                return i, j

    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, value):
        self._active = value

    @property
    def floor(self):
        return self._floor

    @property
    def num(self):
        return self._num

    def __str__(self):
        return ''.join([str((point, item))if isinstance(item, str)
                        else str((point, item.get_name())) for point, item in self._floor.items()])

    def __iter__(self):
        for point, item in self._floor.items():
            yield (point, item)

    def save_floor(self):
        with open('floor.flo', 'w') as file:
            for point, item in self._floor.items():
                file.write(str((point, item)))
