class darbinieks:
    id_counter = 1
  
    def __init__(self, vards, uzvards, alga,):
        self.name = vards
        self.surname = uzvards
        self.salary = alga
        self.id = darbinieks.id_counter
        darbinieks.id_counter += 1
        
    def increase_salary (self, precent):
        self.salary +=self.salary*precent / 100
    def decrease_salary(self, precent):
        self.salary -=self.salary*precent / 100
    def __str__ (self):
        return f"{self.id} {self.name}{self.surname}, Alga::{self.slary:2f}"


