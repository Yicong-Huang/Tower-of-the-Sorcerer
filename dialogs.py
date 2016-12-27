from tkinter import *
from tkinter import messagebox
import ele_lib


class ShopDialog(Toplevel):
    def __init__(self,prot):
        Toplevel.__init__(self)
        self.prot=prot
        self.cost=IntVar()
        self.cost.set(20*(sum(range(prot._shop+1))+1))
        self.k=self.prot._floor._num//10+1

        Label(self,text='Give me %s gold, and get one upgrade'%self.cost.get()).grid()

        Button(self,text='+ %s health'% (100*(prot._shop+1)),command=lambda: self._OnButton('hp', 100*(prot._shop+1))).grid()
        Button(self,text='+ %s attack'% (2*self.k),command=lambda:self._OnButton('attack', 2*self.k)).grid()
        Button(self,text='+ %s defense'% (4*self.k),command=lambda: self._OnButton('defense', 4*self.k)).grid()
        Button(self,text='Leave',command=self.destroy).grid()


    def _OnButton(self,kind,num):
        if self.prot._gold>=self.cost.get():
            exec('self.prot._'+kind+'+='+str(num))
            self.prot._gold-=self.cost.get()
            self.prot._shop+=1
            self.destroy()
        else:
            messagebox.showerror('shop', 'not enough gold to purchase!')


class Infobox(Toplevel):
    def __init__(self,prot):
        Toplevel.__init__(self)
        temp,unique=[],[]
        for i in [m[1]for m in prot._floor]:
            if type(i).__name__ =='Mob':
                if i._name not in temp:
                    unique.append(i)
                temp.append(i._name)
            elif type(i).__name__ =='Trigger' and type(ele_lib.lib[i._obj]).__name__=='Mob':
                if i._item._name not in temp:
                    unique.append(i._item)
                temp.append(i._item._name)

        info= '\n\n'.join(['name             hp  attack  defense  harm  gold']
        +['{:<20}{:<8}{:<8}{:<8}{:<8}{:<8}'.format(
            m._name,
            m._hp,
            m._attack,
            m._defense,
            m.calculate_harm(prot),
            m._gold)  for m in sorted(unique,key=lambda x:x._name)])
        Label(self,text=info).grid()
        Button(self,text='OK',command=self.destroy,default='active').grid()
