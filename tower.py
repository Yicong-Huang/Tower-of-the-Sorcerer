from floor import Floor


class Tower():
    def __init__(self,floors:list):
        self._tower=floors
        self._height=len(floors)
        self._current= floors[0]
    
    def add(self,floor):
        self._tower.append(floor)
        
    def load_floor(flo):
        with open(flo,'r') as file:
            n=0
            temp_tower=[]
            for line in file:
                n+=1
                temp_floor={}
                line=line.strip('\n').strip('(').strip(')').split(')((')
                for entry in line:
                    point,item=entry.split('), ')
                    i,j= point.split(', ')
 
                    temp_floor.update({(int(i),int(j)):item.strip("'")})
                temp_tower.append(Floor(n,*temp_floor.items()))
            return Tower(temp_tower)
    
    def __iter__(self):
        for floor in self._tower:
            yield floor
    
    def get_num(self,floor):
        return self._tower.index(floor)
    
    def current_floor(self):
        return self._current
    
    def next_floor(self):
        if self._current!=self._tower[-1]:
            self._current = self._tower[self.get_num(self._current)+1]
        return self._current
    
    def previous_floor(self):
        if self._current!=self._tower[0]:
            self._current = self._tower[self.get_num(self._current)-1]
        return self._current
        
        
    
    
    
    
            
            