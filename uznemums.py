from darbinieks import darbinieks

class Uznemums:
    def __init__(self, nosaukums):
        self.nosaukums = nosaukums 
        self. darbinieki = []
        
    def pievienot_darinieku(self, darbinieks):
        self.darbinieki.append(darbinieks)
    def paradit_visus_darbiniekus(self):
        print(f"Uzņēmums:{self.nosaukums}")
        for d in self.darbinieki:
            print(d)
    def augstaka_alga(self):
        if not self.daarbinieki:
            print("nav darbinieku")
            return None
        

