from obj import Obj
from ele_lib import *
#from pygame import mixer

from PIL.ImageTk import PhotoImage

class Display(Obj):
    tick=True
    def __init__(self,i,j,name,floor):
        super().__init__(i,j)
        self._name = name
        self._floor=floor
        
    def get_location(self):
        self._x,self._y = self._i*Obj.side+35+125, self._j *Obj.side+41
        return self._x, self._y
    
    def display(self, canvas,tick):
        self._tick=tick
        self._canvas=canvas

        set_image(self)
        self._image=lib[self._name].image[tick] if isinstance(lib[self._name].image,tuple) else lib[self._name].image
        self._tag=canvas.create_image(*self.get_location(),image=self._image,tag='redraw')

       
    def disappear(self):
        try:
            if self._name in self._floor.get_floor(self._i,self._j)._name :
                self._floor.del_floor(self._i,self._j)
        except:
            pass
        
    
    def move_to(self,i,j):
        if type(self).__name__!='Protagonist':
            self.disappear()
            self._floor.set_floor(i,j,self._name)
        self._i,self._j=i,j
        
        
        