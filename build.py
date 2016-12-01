from item import Item

class Build(Item):
    def interact(self,prot):
        if self._name in ('hidden_door','background'):
            if prot._i==5 and prot._j==3 and self._floor._num==19:
                prot._floor.set_floor(5, 2,'cross')
            else:
                Item.interact(self,prot)
        elif self._name== 'hidden_wall':
            prot._floor.set_floor(*self.get_position(),'wall')
        elif self._name=='upstairs':
            prot._moved=True
            prot._floor = prot._tower.next_floor()

        elif self._name=='downstairs':
            prot._moved=True
            prot._floor = prot._tower.previous_floor()
        elif self._name in ('yellow_door','blue_door','red_door'):
            if eval('prot._'+self._name[:-4]+'key>=1'):
                print('good')
                exec('prot._'+self._name[:-4]+'key'+'-=1')
                Item.interact(self,prot)
            else:
                print('need key!')