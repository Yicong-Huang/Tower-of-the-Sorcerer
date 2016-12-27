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
        self.fight(prot)
        
    def fight(self,prot,attack_first=False):
        
        attack=((prot._cross and ('zombie' in self._name or 'vampire'in self._name))+1)*prot._attack
        if attack>self._defense:
            harm=self.calculate_harm(prot,attack_first)
            print(harm)
            if prot._hp>harm:
                prot._hp-=harm
                prot._gold +=(prot._lucky_coin+1) *self._gold
                self.disappear()
                prot._moved=True
            else:
                print('hp will get too low')
        else:
            print('defense too high for attack')
    def calculate_harm(self,prot,attack_first=False):
        
        attack=((prot._cross and ('zombie' in self._name or 'vampire'in self._name))or(prot._dragon_dagger and ('dragon' in self._name))+1)*prot._attack
        if attack_first:
            hp=self._hp+prot._attack
        else:
            hp=self._hp
        if attack>self._defense:
            harm=0
            while hp>0:
                hp-=attack-self._defense
                if hp>0:
                    harm+=self._attack-prot._defense
            harm=max(harm,0)
        else:
            harm='N.A'
        return harm
        