from item import Item
import view, ele_lib

class Hallow(Item):
    def __init__(self,i,j,name,floor):
        Item.__init__(self,i,j,name,floor)
        
    def interact(self,prot):
        #print(self,prot,'!!!!!!')
        if self._name=='transmit':
            view.main.create_image(33,200,image=view.transmit_up_icon,tag='page_up')
            view.main.create_image(33,216,image=view.transmit_down_icon,tag='page_down')
        elif self._name=='cross': 
            view.main.create_image(65,336,image=ele_lib.lib['cross'].image)
            prot._cross=True
        elif self._name=='pickaxe': 
            view.main.create_image(97,336,image=ele_lib.lib['pickaxe'].image)
        Item.interact(self,prot)