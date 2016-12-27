import controller, view, ele_lib 

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
# def reset ():
#     global F
#     controller.the_canvas.delete('redraw')
#     F=Floor(1)
#     
# 
# #start running the simulation
# def save ():
#     F.save_floor()
def save():
    T.save_tower(prot)
    
     
def load():
    global T,F,prot,main

    for hallow in prot._hallows:
        controller.the_canvas.delete(hallow)
    T,prot=Tower.load_tower('game1.sav')
    
    F=T.current_floor()
    display_all(controller.tick)
    
    for hallow in prot._hallows:
        hallow=Hallow(0,0,hallow,F)
        ele_lib.set_image(hallow)
        hallow.interact(prot)
    
    

    

def show_info():
    return Hallow(0,0,'info_book',None).clicked(prot,None)

def next ():
    T.next_floor()
     
def previous():
    T.previous_floor()



def arrow_direction(direction):
    prot.move(*{'left':(-1,0),'right':(1,0),'up':(0,-1),'down':(0,1)}[direction])




T,prot=Tower.load_tower('all_floors.flo')

check=True
def display_all(tick):

    
    global main,check
    main=controller.the_canvas
    floor = T.current_floor()
    
   
    check=False

    main.delete('redraw')


    for (i,j),item in floor:
        if isinstance(item, str):
            item=eval(type(ele_lib.lib[item]).__name__+'(i,j,item,floor)')
            floor.set_floor(i,j,item)
        item.display(main,tick)

    prot.display(main,tick)
    
    
    
    main.create_text(79,87,text=prot.get_value('hp'),tag='redraw')
    main.create_text(79,111,text=prot.get_value('attack'),tag='redraw')
    main.create_text(79,135,text=prot.get_value('defense'),tag='redraw')
    main.create_text(79,159,text=prot.get_value('gold'),tag='redraw')
    main.create_text(65,57,text='Floor %s'% prot.get_value('floor._num'),tag='redraw')
    
    main.create_text(560,155,text='       *    %s'% prot.get_value('yellow_key'),tag='redraw')
    main.create_text(560,175,text='       *    %s'% prot.get_value('blue_key'),tag='redraw')
    main.create_text(560,195,text='       *    %s'% prot.get_value('red_key'),tag='redraw')
   
   

