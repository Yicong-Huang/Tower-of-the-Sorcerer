from display import Display

class Item(Display):
    
    def interact(self,prot):
        self.disappear()
        prot._moved=True
        