import controller, sys,view,model, ele_lib 

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
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global F
    controller.the_canvas.delete('redraw')

    F=Floor(1)
    

#start running the simulation
def save ():
    F.save_floor()
    
def load():
    global T,F
    T=Tower.load_floor('floor.flo')
    F=T.current_floor()
    display_all(1)

    
def next ():
    T.next_floor()
    
def previous():
    T.previous_floor()

def mouse_click(x,y):
    global F
    item=view.variable.get()
    i=round((x-35-125)/32)
    j=round((y-41)/32)
    F.set_floor(i,j,item)
    item=eval(type(ele_lib.lib[item]).__name__+'(i,j,item,F)')
    item.display(controller.the_canvas,0)
    print([f for f in F])


def arrow_direction(direction):
    prot.move(*{'left':(-1,0),'right':(1,0),'up':(0,-1),'down':(0,1)}[direction])





T=Tower.load_floor('all_floors.flo')
prot=Protagonist(5,10,'protagonist',T)
check=True
def display_all(tick):
    main=controller.the_canvas
    floor = T.current_floor()
    global check
    while floor._num!=T._height and check:
        floor=T.next_floor()
    check=False

    main.delete('redraw')

    
    for (i,j),item in floor:
        if isinstance(item, str):
            print(item)
            item=eval(type(ele_lib.lib[item]).__name__+'(i,j,item,floor)')
            floor.set_floor(i,j,item)
        item.display(controller.the_canvas,tick)
    prot.display(controller.the_canvas,tick)
    
    
    main.create_text(79,87,text=prot.get_value('hp'),tag='redraw')
    main.create_text(79,111,text=prot.get_value('attack'),tag='redraw')
    main.create_text(79,135,text=prot.get_value('defense'),tag='redraw')
    main.create_text(79,159,text=prot.get_value('gold'),tag='redraw')
    main.create_text(65,57,text='Floor %s'% prot.get_value('floor._num'),tag='redraw')
    
    main.create_text(560,155,text='       *    %s'% prot.get_value('yellow_key'),tag='redraw')
    main.create_text(560,175,text='       *    %s'% prot.get_value('blue_key'),tag='redraw')
    main.create_text(560,195,text='       *    %s'% prot.get_value('red_key'),tag='redraw')
   


