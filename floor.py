class Floor():
    def __init__(self,n,*args):
        self._num=n
        self._floor={}
        for point,item in args:
            self.set_floor(*point,item)
    
    def set_floor(self,i,j,item):
        self._floor[(i,j)]=item
        
    def get_floor(self,i,j):
        return self._floor.get((i,j))
    
    def del_floor(self,i,j):
        self._floor.pop((i,j))
    
    def __iter__(self):
        for point, item in self._floor.items():
            yield (point, item)
            
    def save_floor(self):
        with open('floor.flo','w') as file:
            for point, item in self._floor.items():
                file. write(str((point,item)))
  