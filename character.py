from tkinter import messagebox
from display import Display
import ele_lib
from hallow import Hallow

class Character(Display):
    def __init__(self,i,j,name,floor):
        Display.__init__(self,i,j,name,floor)
    
    def interact(self,prot):
        num=self._floor._num
        if self._name=='thief':
            if num==2:
                if self.get_position()==(2,6):
                    messagebox.showinfo(title='thief', message='hello')
                    self._floor.del_floor(1,6)
                    self.move_to(0,8)
                elif self.get_position()==(0,8):
                    messagebox.showinfo(title='thief', message='hello')
                    self.disappear()
                elif self.get_position()==(10,9):
                    messagebox.showinfo(title='thief', message='hello')
                    self.disappear()
                    prot._tower._tower[34].del_floor(3,8)
                    prot._tower._tower[34].set_floor(4,9,'thief')
                    
            elif num==15:
                messagebox.showinfo(title='thief', message='hello')
                self._floor.del_floor(7,0)
                self.disappear()
            elif num==29:
                messagebox.showinfo(title='thief', message='hello')
                self._floor.del_floor(5,2)
                self.disappear()
                prot._tower._tower[1].set_floor(10,9,'thief')
            elif num==35:
                messagebox.showinfo(title='thief', message='hello')
               

                
                
                
        elif self._name=='sage':
            if num==2:
                prot._gold+=1000
            elif num==3:
                self._floor.set_floor(10,3,'info_book')
                messagebox.showinfo(title='sage', message='hello')
            self.disappear()
        elif self._name =='merchant':
            if num==2 and messagebox.askyesno('merchant', 'Thank you for rescuring me! I can add you 3% more both attack and defense, do you want it now?'):
                prot._attack=round(prot._attack*1.03)
                prot._defense=round(prot._defense*1.03)
                self.disappear()
                
            elif num==6 and messagebox.askyesno('merchant', 'a blue key for 50 gold?') and prot._gold>=50:
                prot._gold-=50
                prot._blue_key+=1
                messagebox.showinfo('merchant',"Thank you!\n\nIn the tower, it's better to get more defense than attack")
                self.disappear()
            elif num==7 and messagebox.askyesno('merchant', '5 yellow keys for 50 gold?') and prot._gold>=50:
                prot._gold-=50
                prot._yellow_key+=5
                messagebox.showinfo('merchant',"Thank you!\n\nIn the tower, it's better to get more defense than attack")
                self.disappear()
            elif num==47 and messagebox.askyesno('merchant', 'earthquake scroll for 4000 gold?') and prot._gold>=4000:
                prot._gold-=4000
                self._floor.set_floor(4,1,'earthquake')
                messagebox.showinfo('merchant',"Thank you!\n\nIn the tower, it's better to get more defense than attack")
                self.disappear()
            elif num==12:
                if self.get_position()==(10,0) and messagebox.askyesno('merchant', 'a yellow key for 1000 gold? I have plenty of them!') and prot._gold>=1000:
                    prot._gold-=1000
                    prot._yellow_key+=1
                elif self.get_position()==(0,0) and messagebox.askyesno('merchant', 'a red key for 800 gold?') and prot._gold>=800:
                    prot._gold-=800
                    prot._red_key+=1
                    self.disappear()
                   
            
       
    def move(self,di=0,dj=0):
        for t in range(max(abs(di),abs(di))):
            if self._tick:
                self.disappear()
                i,j=self.get_position()
                print(i,j)
                self.set_position(i+(di!=0),j+(dj!=0))
                self._floor.set_floor(*self.get_position(),self._name)
                self.display(self._canvas,self._tick)
            else:
                print('not ticking')
            self._tick=not self._tick
            
    def get_value(self,name):
        return eval('self._'+name)

        