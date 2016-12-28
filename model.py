'''The main model controled by the controller. Set the game to run, display, load and save'''
import controller
import view
import ele_lib

from floor import Floor
from tower import Tower

from enhancement import Enhancement
from collection import Collection
from character import Character
from build import Build
from hallow import Hallow
from trigger import Trigger
from protagonist import Protagonist
from mob import Mob

#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.THE_CANVAS.winfo_width(), controller.THE_CANVAS.winfo_height())

def save():
    T.save_tower(prot)

def load():
    "Loads the game, including tower and prot form save file"
    global T, F, prot, MAIN
    for hallow in prot.get_value('hallows'):
        controller.THE_CANVAS.delete(hallow)
    T, prot = Tower.load_tower('game1.sav')

    F = T.current
    display_all(controller.TICK)

    for hallow in prot.get_value('hallows'):
        hallow = Hallow(0, 0, hallow, F)
        ele_lib.set_image(hallow)
        hallow.interact(prot)

def show_info():
    return Hallow(0, 0, 'info_book', None).clicked(prot, None)

def next_floor():
    T.next_floor()

def previous_floor():
    T.previous_floor()

def arrow_direction(direction):
    prot.move(*{'left':(-1, 0), 'right':(1, 0), 'up':(0, -1), 'down':(0, 1)}[direction])

T, prot = Tower.load_tower('all_floors.flo')

CHECK = True
def display_all(tick):
    "Display all game elements on the game board that needs to be updated"
    global MAIN, CHECK
    MAIN = controller.THE_CANVAS
    floor = T.current

    CHECK = False

    MAIN.delete('redraw')

    for (i, j), item in floor:
        if isinstance(item, str):
            item = eval(type(ele_lib.lib[item]).__name__+'(i, j, item, floor)')
            floor.set_floor(i, j, item)
        item.display(MAIN, tick)

    prot.display(MAIN, tick)

    MAIN.create_text(79, 87, text=prot.get_value('hp'), tag='redraw')
    MAIN.create_text(79, 111, text=prot.get_value('attack'), tag='redraw')
    MAIN.create_text(79, 135, text=prot.get_value('defense'), tag='redraw')
    MAIN.create_text(79, 159, text=prot.get_value('gold'), tag='redraw')
    MAIN.create_text(65, 57, text='Floor %s'% prot.get_value('floor._num'), tag='redraw')

    MAIN.create_text(560, 155, text='       *    %s'% prot.get_value('yellow_key'), tag='redraw')
    MAIN.create_text(560, 175, text='       *    %s'% prot.get_value('blue_key'), tag='redraw')
    MAIN.create_text(560, 195, text='       *    %s'% prot.get_value('red_key'), tag='redraw')
