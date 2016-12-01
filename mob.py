from character import Character
import ele_lib

class Mob(Character):
    def __init__(self,i,j,name,floor):
        Character.__init__(self,i,j,name,floor)
        values=ele_lib.lib[name]
        self._attack=values.attack
        self._defense=values.defense
        self._hp=values.hp
        self._gold=values.gold
        
    def interact(self,prot):
        attack=((prot._cross and ('zombie' in self._name or 'vampire'in self._name))+1)*prot._attack
        if attack>self._defense:
            damage=max(self._hp//(attack-self._defense)*(self._attack-prot._defense),0)
            if prot._hp>damage:
                prot._hp-=damage
                prot._gold += self._gold
                
                self.disappear()
                prot._moved=True
            else:
                print('hp will get too low')
        else:
            print('defense too high for attack')