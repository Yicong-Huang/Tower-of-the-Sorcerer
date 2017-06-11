'''The main model controled by the controller. Set the game to run, display, load and save'''


from tkinter import messagebox

import controller
from ele_lib import LIB, set_image
from hallow import Hallow
from tower import Tower

exec('from enhancement import Enhancement')
exec('from collection import Collection')
exec('from character import Character')
exec('from build import Build')
exec('from trigger import Trigger')
exec('from mob import Mob')

T, PROT = Tower.load_tower('all_floors.flo')
F = T.current
CHECK = True
MAIN = None

def world():
    return (controller.THE_CANVAS.winfo_width(), controller.THE_CANVAS.winfo_height())


def save():
    messagebox.showinfo('Tower of the Sorcerer', 'Saved!')
    T.save_tower(PROT)


def load():
    "Loads the game, including tower and PROT form save file"
    global T, F, PROT, MAIN
    messagebox.showinfo('Tower of the Sorcerer', 'Loaded!')
    for hallow in PROT.get_value('hallows'):
        controller.THE_CANVAS.delete(hallow)
    T, PROT = Tower.load_tower('game1.sav')

    F = T.current
    display_all(controller.TICK)

    for hallow in PROT.get_value('hallows'):
        hallow = Hallow(0, 0, hallow, F)
        set_image(hallow)
        hallow.interact(PROT)


def show_info():
    return Hallow(0, 0, 'info_book', None).clicked(PROT, None)


def next_floor():
    T.next_floor()


def previous_floor():
    T.previous_floor()


def arrow_direction(direction):
    PROT.move(*{'left': (-1, 0), 'right': (1, 0),
                'up': (0, -1), 'down': (0, 1)}[direction])


def display_all(tick):
    "Display all game elements on the game board that needs to be updated"
    global MAIN, CHECK, F
    MAIN = controller.THE_CANVAS
    F = T.current
    CHECK = False

    MAIN.delete('redraw')

    for (i, j), item in F:
        if isinstance(item, str):
            item = eval(type(LIB[item]).__name__ + '(i, j, item, F)')
            F.set_floor(i, j, item)
        item.display(MAIN, tick)

    PROT.display(MAIN, tick)

    MAIN.create_text(79, 87, text=PROT.get_value('hp'), tag='redraw')
    MAIN.create_text(79, 111, text=PROT.get_value('attack'), tag='redraw')
    MAIN.create_text(79, 135, text=PROT.get_value('defense'), tag='redraw')
    MAIN.create_text(79, 159, text=PROT.get_value('gold'), tag='redraw')
    MAIN.create_text(65, 57, text='Floor %s' %
                     PROT.get_value('floor._num'), tag='redraw')

    MAIN.create_text(560, 155, text='       *    %s' %
                     PROT.get_value('yellow_key'), tag='redraw')
    MAIN.create_text(560, 175, text='       *    %s' %
                     PROT.get_value('blue_key'), tag='redraw')
    MAIN.create_text(560, 195, text='       *    %s' %
                     PROT.get_value('red_key'), tag='redraw')
