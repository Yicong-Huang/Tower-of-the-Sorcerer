'''Defining class Plot which runs the case in the PLOT_LIB, detecting Triggers.'''
from tkinter import messagebox
from mob import Mob
from trigger import Trigger


PLOT_LIB = {
    22:([(5, 1), (7, 1)], [(4, 4), (4, 7), (4, 10), (8, 4), (8, 7), (8, 10)]),
    81:([(8, 4), (10, 4)], [(9, 3)]),
    101:([], [(1, 2), (9, 3), (9, 2), (8, 2), (2, 2), (10, 2), (1, 3), (0, 2)],
         [((6, 4), 'skeleton_trigger'), ((5, 0), 'skeleton_captain_trigger'),
          ((5, 5), 'skeleton_soldier_trigger'), ((4, 5), 'skeleton_trigger'),
          ((4, 4), 'skeleton_trigger'), ((6, 3), 'skeleton_trigger'),
          ((5, 6), 'special_door'), ((4, 3), 'skeleton_trigger'),
          ((5, 2), 'special_door'), ((6, 5), 'skeleton_trigger'),
          ((5, 3), 'skeleton_soldier_trigger')]),
    102:([(4, 3), (5, 3), (6, 3), (4, 4), (4, 5), (5, 5), (6, 5), (6, 4)], [(5, 2)]),
    103:([(5, 0)], [(3, 3), (7, 3), (5, 6)],
         [((0, 2), 'red_gem'), ((1, 2), 'red_gem'), ((2, 2), 'red_gem'),
          ((0, 3), 'blue_blood'), ((1, 3), 'blue_blood'), ((2, 3), 'blue_blood'),
          ((8, 2), 'blue_gem'), ((9, 2), 'blue_gem'), ((10, 2), 'blue_gem'),
          ((8, 3), 'yellow_key'), ((9, 3), 'yellow_key'), ((10, 3), 'yellow_key'),
          ((5, 10), 'upstairs')]),
    111:([(0, 4), (2, 4)], [(1, 3)]),
    144:([(0, 0), (1, 1), (2, 0)], [(0, 2)], [((0, 2), 'red_key')]),
    151:([], [], [((5, 8), 'special_door')]),
    152:([(5, 4)], [(5, 8), (5, 2)], [((5, 3), 'pickaxe')]),
    171:([(0, 7), (2, 7)], [(1, 6)]),
    172:([(0, 4), (2, 4)], [(1, 3)]),
    173:([(8, 7), (10, 7)], [(9, 6)]),
    174:([(8, 4), (10, 4)], [(9, 3)]),
    201:([], [(4, 4), (4, 5), (4, 6), (5, 4), (5, 6), (6, 4), (6, 5), (6, 6)],
         [((5, 5), 'vampire_trigger'), ((5, 8), 'special_door')]),
    202:([(5, 5)], [(5, 8), (5, 2)],
         [((5, 0), 'upstairs'), ((4, 3), 'yellow_key'), ((5, 3), 'yellow_key'),
          ((6, 3), 'yellow_key'), ((3, 4), 'red_gem'), ((3, 5), 'red_gem'),
          ((3, 6), 'red_gem'), ((7, 4), 'blue_gem'), ((7, 5), 'blue_gem'),
          ((7, 6), 'blue_gem'), ((4, 7), 'blue_blood'), ((5, 7), 'blue_blood'),
          ((6, 7), 'blue_blood')]),
    301:([], [], [((5, 3), 'special_door'), ((5, 6), 'special_door')]),
    302:([(2, 4), (3, 4), (4, 4), (6, 4), (7, 4), (8, 4)],
         [(5, 3), (5, 6)], [((5, 0), 'upstairs')]),

    322:([(0, 9), (2, 9)], [(1, 8)]),
    331:([], [], [((9, 3), 'special_door'), ((9, 7), 'special_door')]),
    332:([(8, 4), (8, 6), (10, 4), (10, 6)], [(9, 3), (9, 7)]),
    342:([(4, 3), (6, 3), (8, 3), (10, 3), (4, 7), (6, 7), (8, 7), (10, 7)], [],
         [((0, 4), 'yellow_key'), ((2, 4), 'yellow_key'), ((0, 6), 'yellow_key'),
          ((2, 6), 'yellow_key'), ((1, 5), 'red_key')]),
    351:([(5, 5)], [(5, 2)],
         [((5, 4), 'ice'), ((4, 3), 'blue_blood'), ((5, 3), 'blue_blood'),
          ((6, 3), 'blue_blood')]),
    381:([(1, 5)], [], [((1, 4), 'wall')]),
    382:([(0, 9), (2, 9)], [], [((1, 8), 'hidden_door')]),
    392:([((3, 1), (5, 3)), ((1, 1), (5, 1), (1, 3), (3, 3), (1, 5), (3, 5), (5, 5))],
         [], [((3, 3), 'fly_oppo')]),
    402:([], [], []),
    413:([(1, 1)], [(9, 1)], [((9, 1), 'hidden_door')]),
    412:([(9, 1)], [(4, 6), (6, 6)],
         [((5, 4), 'fly_down'), ((5, 5), 'wall'), ((4, 5), 'wall'), ((6, 5), 'wall')]),
    422:([], [], [((4, 7), 'magic_guard'), ((6, 7), 'magic_guard'),
                  ((5, 6), 'magic_guard'), ((5, 8), 'magic_guard')]),
    423:([], [(4, 7), (6, 7), (5, 6), (5, 8), (5, 5)]),
    441:([(4, 8), (6, 8)], [(5, 7)], []),
    452:([(4, 8), (4, 10)], [(3, 9)]),
    454:([(7, 8), (7, 10)], [(6, 9)]),
    491:([], [],
         [((5, 6), 'special_door'), ((4, 1), 'magic_guard_trigger'),
          ((4, 3), 'magic_guard_trigger'), ((6, 1), 'magic_guard_trigger'),
          ((6, 3), 'magic_guard_trigger'), ((4, 2), 'magic_guard_trigger'),
          ((6, 2), 'magic_guard_trigger'), ((5, 1), 'magic_guard_trigger'),
          ((5, 3), 'magic_guard_trigger'), ((5, 2), 'fake_lord1')]),
    492:([(4, 7), (6, 7)], [(5, 6)]),
    493:([(4, 9), (6, 9)], [(5, 8)]),
    494:([((4, 2), (6, 2), (5, 1), (5, 3)), ((4, 1), (4, 3), (6, 1), (6, 3))], [(5, 2)],
         [((5, 2), 'fake_lord2_trigger')]),
    495:([], [(4, 1), (4, 3), (6, 1), (6, 3), (5, 6)],
         [((4, 1), 'red_key'), ((6, 1), 'dragon_dagger'), ((1, 3), 'red_gem'),
          ((2, 3), 'red_gem'), ((3, 3), 'red_gem'), ((7, 3), 'blue_gem'),
          ((8, 3), 'blue_gem'), ((9, 3), 'blue_gem'), ((4, 4), 'blue_blood'),
          ((5, 4), 'blue_blood'), ((6, 4), 'blue_blood')])}

class Plot:
    '''run case in the PLOT_LIB'''
    def __init__(self, floor, case, prot):
        self._floor = floor
        self._case = self._floor.num*10+case
        self._prot = prot
        self.run(self._case)

    def run(self, case):
        if case == 321:
            self._floor.set_floor(5, 8, Mob(5, 8, 'golden', self._floor))
            golden = self._floor.get_floor(5, 8)
            messagebox.showinfo('golden', 'Haha, you made it here! Ger ready to die!')
            golden.fight(self._prot, True)
            golden.move_to(5, 8)
            messagebox.showinfo('golden',
                                'It seems like that I am not ready now. \
                                I will see you at floor 40 and beat your ass off!')
            golden.disappear()
        elif case == 401:
            messagebox.showinfo('golden', 'You dare come here! I have been waitting for ages!')
            messagebox.showinfo('golden', 'Go ghost soldiers!')
            for i, j in [(2, 3), (3, 3), (4, 3)]:
                ghost_soldier=self._floor.get_floor(i, j)
                ghost_soldier.move_to(5, 5)
                messagebox.showinfo('ghost soldier', 'Fight!!!')
                ghost_soldier.fight(self._prot, True)
            messagebox.showinfo('golden', 'Go soldiers!')
            for i, j in [(6, 3), (7, 3), (8, 3)]:
                soldier=self._floor.get_floor(i, j)
                soldier.move_to(5, 5)
                messagebox.showinfo('soldier', 'Fight!!!')
                soldier.fight(self._prot, True)
            messagebox.showinfo('golden', 'Go swords man!')
            for i, j in [(1, 1), (2, 1), (3, 1)]:
                swords_man=self._floor.get_floor(i, j)
                swords_man.move_to(5, 5)
                messagebox.showinfo('swords man', 'Fight!!!')
                swords_man.fight(self._prot, True)
            messagebox.showinfo('golden', 'Go knights! End him!')
            for i, j in [(7, 1), (8, 1), (9, 1)]:
                knight=self._floor.get_floor(i, j)
                knight.move_to(5, 5)
                messagebox.showinfo('knight', 'Fight!!!')
                knight.fight(self._prot, True)
                knight.disappear()
            messagebox.showinfo('golden', "Now you must be weak! Let me end you!")
            golden=self._floor.get_floor(5, 0)
            golden.move_to(5, 5)
            golden.fight(self._prot, True)
            messagebox.showinfo(
                'golden',
                "I ... I'm not ready again ... I won't give you any chance next time!")
            golden.move_to(5, 3)
            messagebox.showinfo('golden', "You are a dead man walking!")
            self._floor.set_floor(5, 0, 'upstairs')
            golden.disappear()
            self.run(402)
        elif case == 421:
            messagebox.showinfo('golden', "You again??? I'm not ready today!")
            golden=self._floor.get_floor(5, 8)
            golden.move_to(5, 7)
            messagebox.showinfo('Lord', "COWARD!")
            self.run(422)
            messagebox.showinfo('Lord', "Kill this useless coward!")
            golden.disappear()
            messagebox.showinfo('Lord', "And I will see you later, Bravo!")
            self.run(423)

        elif isinstance(PLOT_LIB[case], tuple):
            if self.detect(PLOT_LIB[case][0]):
                for i, j in PLOT_LIB[case][1]:
                    if self._floor.get_floor(i, j):
                        self._floor.del_floor(i, j)
                if len(PLOT_LIB[case]) > 2:
                    for (i, j), item in PLOT_LIB[case][2]:
                        self._floor.set_floor(i, j, item)

    def detect(self, positions):
        print('detecting!!!')
        return True if not positions\
            else all([not isinstance(self._floor.get_floor(i, j), Trigger)for i, j in positions[0]
                     ] + [isinstance(self._floor.get_floor(i, j), Trigger)for i, j in positions[1]
                     ]) if isinstance(positions[0][0],tuple)\
            else all([not isinstance(self._floor.get_floor(i, j), Trigger)for i, j in positions])
