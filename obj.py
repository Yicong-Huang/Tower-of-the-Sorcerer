class Obj:
    
    side = 32
    
    def __init__(self,i,j):
        
        self._i,self._j = i,j
    
    def get_location(self):
        self._x,self._y = self._i*Obj.side+35+125, self._j *Obj.side+41
        return self._x, self._y
    
    def get_position(self):
        return self._i,self._j
    
    