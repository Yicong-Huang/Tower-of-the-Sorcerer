from floor import Floor
from protagonist import Protagonist
import controller

class Tower():
    def __init__(self,floors:list):
        self._tower=floors
        self._height=len(floors)
        self._current= floors[0]
    
    def add(self,floor):
        self._tower.append(floor)
        
    def go_to(self,num):
        self._current=self._tower[num]
    def load_tower(flo,newgame=True):
        with open(flo,'r') as file:
 
            temp_tower=[]
            for n, line in enumerate(file,0):
                if n!=51:
                    temp_floor={}
                    line=line.strip('\n').strip('(').strip(')').split(')((')
                    for entry in line:
                        point,item=entry.split('), ')
                        i,j= point.split(', ')
     
                        temp_floor.update({(int(i),int(j)):item.strip("'")})
                    temp_tower.append(Floor(n,*temp_floor.items()))
            
                else:   
                    T=Tower(temp_tower)   
                    T._current=T._tower[int(line.strip('\n').split('/')[6])]   
                    temp=zip(['i','j','hp','attack','defense','gold',
                              'num','yellow_key','blue_key','red_key',
                              'shop','cross','lucky_coin','magic_defense',
                              'dragon_dagger','hallows'],line.strip('\n').split('/'))
                    prot=Protagonist('protagonist',T,**dict([i for i in temp]))
                    
            return T,prot
    
    def save_tower(self,prot):
        with open('game1.sav','w') as file:
            for floor in self._tower:
                file.write(str(floor)+'\n')
            file.write(str(prot))
    
        
    def __iter__(self):
        for floor in self._tower:
            yield floor
    
    def get_num(self,floor):
        return self._tower.index(floor)
    
    def current_floor(self):
        return self._current
    def check_active(self,direction):
        return self._tower[self.get_num(self._current)+{'up':1,'down':-1}[direction]]._active
    def next_floor(self):
        if self._current!=self._tower[-1] and self._current._num!=43:
            self._current = self._tower[self.get_num(self._current)+1]
        elif self._current._num==43:
            self._current = self._tower[self.get_num(self._current)+2]
        self._current._active=True
        return self._current
    
    def previous_floor(self):
        if self._current!=self._tower[0] and self._current._num!=45:
            self._current = self._tower[self.get_num(self._current)-1]
        elif self._current._num==45:
            self._current = self._tower[self.get_num(self._current)-2]
        return self._current
        
        
    
    
    
    
            
            