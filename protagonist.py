from character import Character

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
    def __init__(self,i,j,name,tower):
        Character.__init__(self,i,j,name,tower.current_floor())
        values=ele_lib.lib[name]
  
        self._attack=values.attack
        self._defense=values.defense
        self._hp=values.hp
        self._gold=values.gold
        self._yellow_key=10
        self._blue_key=10
        self._red_key=10
        self._tower=tower
        self._cross=False
        
        print(self.__dict__)
        
        
    def change_image(self,direction):
        
        self._image=image
        
        
    def move(self,di,dj):
        print(self.__dict__)
        temp_i=self._i+di
        temp_j=self._j+dj

        self._floor = self._tower.current_floor()
        attempt=self._floor.get_floor(temp_i,temp_j)
        if attempt:
            print(attempt._name)
        self._moved=False
        self._interacted=False
        self._plotting=False
        case=None
        if isinstance(attempt, Trigger):

            self._plotting=True
            case=attempt._case

            item= ele_lib.lib[attempt._obj]
            attempt=eval(type(item).__name__+'(temp_i,temp_j,attempt._obj,self._floor)')
           
        if isinstance(attempt, (Build,Enhancement,Mob,Character,Collection,Hallow)):
            attempt.interact(self)
                    
        else:
            self._moved=True
            
        if self._moved and 11>temp_i>=0 and 11>temp_j>=0:
            self._i=temp_i
            self._j=temp_j
        if self._interacted:
            self._floor.del_floor(self._i,self._j)
        if self._plotting:
            if self._floor._num==3:
                self._floor=self._tower.previous_floor()
                self.move(-2, -1)
            else:
                Plot(temp_i,temp_j,self._floor,case)
                
    def get_value(self,name):
        return eval('self._'+name)

       
            
    def __str__(self):
        return 'location: %s,%s\ninteracting: %s'%(self._i,self._j,self._interacted)
        
        