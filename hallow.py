from item import Item
from tkinter import messagebox, Toplevel
import view, ele_lib
from dialogs import Infobox

lib={'transmit':[(33,200),(33,216)],
     'cross':[(33,336)],
     'pickaxe':[(97,208)],
     'st_water':[(97,272)],
     'lucky_coin':[(97,336)],
     'info_book':[(65,208)],
     'ice':[(97,304)],
     'earthquake':[(97,240)],
     'key':[(33,304)],
     'boom':[(65,240)],
     'fly_up':[(33,240)],
     'fly_down':[(33,272)],
     'fly_oppo':[(65,272)],
     'message':[(65,304)],
     'dragon_dagger':[(65,336)]}
class Hallow(Item):
    def __init__(self,i,j,name,floor):
        Item.__init__(self,i,j,name,floor)
        
        self._useable=True
    def interact(self,prot):
        Item.interact(self,prot)
        [view.main.tag_bind(view.main.create_image(i,j,image=image,tag=self._name),'<ButtonRelease>',lambda event: Hallow.clicked(self,prot,event))
          for image ,(i,j) in zip([view.transmit_up_icon,view.transmit_down_icon] if self._name=='transmit' else [ele_lib.lib[self._name].image],lib[self._name])]
        prot._hallows.add(self._name)
        if '_'+self._name in prot.__dict__:
            exec('prot._'+self._name+'=True')
        self._useable=True
        if self._name=='fly_oppo':
            view.main.create_text(75,280,text='3')
        
    def clicked(self,prot,event):
        print('clicked')
        print(self._useable,self._name)
        if self._useable:
            if self._name=='info_book':
                Infobox(prot)
            elif self._name=='transmit' :
                def search_stairs(prot):
                    return any(type(prot._floor.get_floor(prot._i+i,prot._j+j)).__name__=='Build' and 'stairs' in prot._floor.get_floor(prot._i+i,prot._j+j)._name for i in [-1,0,1] for j in [-1,0,1])
                
                if search_stairs(prot) and event.y<=208 and prot._tower.check_active('up'):  
                    prot._floor = prot._tower.next_floor()
                    if prot._floor.get_item('downstairs'):
                        prot.move_to(*prot._floor.get_item('downstairs'))
                    else:
                        prot.move_to(5,10)
                elif search_stairs(prot) and event.y>208 and prot._tower.check_active('down'):  
                    prot._floor = prot._tower.previous_floor()
                    prot.move_to(*prot._floor.get_item('upstairs'))
            elif self._name=='earthquake' :
                for i in [i for i in prot._floor._floor.values() if i._name=='wall']:
                    i.disappear()
                #self._useable=False
            elif self._name=='fly_down':
                prot._tower._current=prot._tower._tower[prot._tower.get_num(prot._tower._current)-1]
                #self._useable=False
            elif self._name=='fly_up':
                prot._tower._current=prot._tower._tower[prot._tower.get_num(prot._tower._current)+1]
                #self._useable=False
            elif self._name=='fly_oppo':
                prot.move_to(10-prot._i,10-prot._j)
                #self._useable=False
            elif self._name=='key':
                for i in [i for i in prot._floor._floor.values() if 'yellow_door' in i._name]:
                    i.disappear()
                #self._useable=False
            elif self._name=='ice':
                self.selecting_remove(prot,('lava'))
                #self._useable=False
            elif self._name=='pickaxe':
                print('here',prot)
                self.selecting_remove(prot,('wall'))
                #self._useable=False
            elif self._name=='boom':
                self.selecting_remove(prot,('great_magic','fake_lord1','fake_lord2','dragon'),mode=False,Type='Mob')
                #self._useable=False
    def selecting_remove(self,prot,name,mode=True,Type=None):  
        print('removing')                       
        for (i,j) in [(0,1),(1,0),(0,-1),(-1,0)]:
            test=prot._floor.get_floor(prot._i+i,prot._j+j)

            if test:
                
                if (test._name in name)==mode:
                    if Type:
                        if type(test).__name__==Type or (type(test).__name__=='Trigger' and type(test._item).__name__==Type):
                            hp,attack,defense,gold=prot._hp,prot._attack,prot._defense,prot._gold
                            prot._attack*=1000
                            prot._defense*=1000
                            prot.move(i,j)
                            prot.move(-i,-j)
                            prot._hp,prot._attack,prot._defense,prot._gold=hp,attack,defense,gold
                    else:
                        print('disappearing',test)
                        test.disappear()