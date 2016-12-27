class Obj:
    
    side = 32
    
    def __init__(self,i,j):
        
        self._i,self._j = i,j
    
    
    
    def get_position(self):
        return self._i,self._j
    
    def set_position(self,i,j):
        self._i,self.j=i,j
#     def get_name(self):
#         return self._name
    
    