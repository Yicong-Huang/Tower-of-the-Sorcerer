from tkinter import messagebox
from display import Display
import ele_lib

class Character(Display):
    def __init__(self,i,j,name,floor):
        Display.__init__(self,i,j,name,floor)
    
    def interact(self,prot):
        if self._name=='thief':
            if self._floor._num==2:
                if self.get_position()==(2,6):
                    messagebox.showinfo(title='thief', message='hello')
                    self._floor.del_floor(1,6)
                    self.disappear()
                    self._floor.set_floor(0,8,'thief')
                elif self.get_position()==(0,8):
                    messagebox.showinfo(title='thief', message='hello')
                    self.disappear()
                elif self.get_position()==(10,9):
                    messagebox.showinfo(title='thief', message='hello')
                    self.disappear()
                    prot._tower._tower[34].del_floor(3,8)
                    prot._tower._tower[34].set_floor(4,9,'thief')
                    
            elif self._floor._num==15:
                messagebox.showinfo(title='thief', message='hello')
                self._floor.del_floor(7,0)
                self._floor.del_floor(8,0)
            elif self._floor._num==29:
                messagebox.showinfo(title='thief', message='hello')
                self._floor.del_floor(5,2)
                self.disappear()
                prot._tower._tower[1].set_floor(10,9,'thief')
            elif self._floor._num==35:
                messagebox.showinfo(title='thief', message='hello')
               

                
                
                
        elif self._name=='sage':
            messagebox.showinfo(title='sage', message='hello')
            self.disappear()
       
        