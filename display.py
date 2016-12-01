from obj import Obj
from ele_lib import *
import time


class Display(Obj):
    tick=True
    def __init__(self,i,j,name,floor):
        Obj.__init__(self,i,j)
        self._name = name
        self._floor=floor
        print(self.__dict__)
    
    def display(self, canvas,tick):
        self._canvas=canvas
        set_image(self._name)
        

        if type(lib[self._name].image)==tuple:
            self._image=lib[self._name].image[tick%2]
        else:
            self._image=lib[self._name].image
            
        self._tag=canvas.create_image(*self.get_location(),image=self._image,tag='redraw')
           
    def disappear(self):
        self._floor.del_floor(self._i,self._j)
        
        
        