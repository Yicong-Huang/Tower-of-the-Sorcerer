'''Defining class ShopDialog, InfoBox'''
from tkinter import Button, IntVar, Label, Toplevel, messagebox

from ele_lib import LIB


class ShopDialog(Toplevel):
    '''A ShopDialog will prompt player to choose an enhancement option when Protagonist
    reaches the shop'''

    def __init__(self, prot):
        Toplevel.__init__(self)
        self.prot = prot
        self.cost = IntVar()
        self.cost.set(20 * (sum(range(prot.get_value('shop') + 1)) + 1))
        self.k = self.prot.get_value('floor').num // 10 + 1

        Label(self, text='Give me %s gold, and get one upgrade' %
              self.cost.get()).grid()

        Button(self, text='+ %s health' % (100 * (prot.get_value('shop') + 1)),
               command=lambda: self._onbutton('hp', 100 * (prot.get_value('shop') + 1))).grid()
        Button(self, text='+ %s attack' % (2 * self.k),
               command=lambda: self._onbutton('attack', 2 * self.k)).grid()
        Button(self, text='+ %s defense' % (4 * self.k),
               command=lambda: self._onbutton('defense', 4 * self.k)).grid()
        Button(self, text='Leave', command=self.destroy).grid()

    def _onbutton(self, kind, num):
        if self.prot.get_value('gold') >= self.cost.get():
            exec('self.prot._' + kind + '+=' + str(num))
            self.prot.add_value('gold', -self.cost.get())
            self.prot.add_value('shop', 1)
            self.destroy()
        else:
            messagebox.showerror('shop', 'not enough gold to purchase!')


class Infobox(Toplevel):

    def __init__(self, prot):
        Toplevel.__init__(self)
        temp, unique = [], []
        for i in [m[1] for m in prot.get_value('floor')]:
            if type(i).__name__ == 'Mob':
                if i.get_value('name') not in temp:
                    unique.append(i)
                temp.append(i.get_value('name'))
            elif type(i).__name__ == 'Trigger' and type(LIB[i.get_value('obj')]).__name__ == 'Mob':
                if i.get_value('item').get_value('name')not in temp:
                    unique.append(i.get_value('item'))
                temp.append(i.get_value('item').get_value('name'))

        info = '\n\n'.join(['name             hp  attack  defense  harm  gold']
                           + ['{:<20}{:<8}{:<8}{:<8}{:<8}{:<8}'.format(
                               m.get_value('name'),
                               m.get_value('hp'),
                               m.get_value('attack'),
                               m.get_value('defense'),
                               m.calculate_harm(prot),
                               m.get_value('gold'))
                              for m in sorted(unique, key=lambda x: x.get_value('name'))])
        Label(self, text=info).grid()
        Button(self, text='OK', command=self.destroy, default='active').grid()
