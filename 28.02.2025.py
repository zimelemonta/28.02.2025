class person:
    def __init__(self, surname, height, name, age):
        self.name= name
        self.age= age
        self.surname = surname
        self. height = height
    def greet(self):
        print(f"hello{self.name}")
        print(f"i am {self.age} y.o")
    def getname(self) -> str:
        return self.name
    def getname(self) -> int:
        return self age
    
    def getsurname(self)-> str:
        return self.surname
    def getheighht(self)->str:
        return self height
    def __str__(self):
        return f"{self.name} {self.age}"

person1 = person ("Monta", "who",18, 168)
person2 = person ("krisitana", "who", 17, 164)
person3 = person ("ieva", "who", 18, 180)
person4 = person ("Angelina", "who", 17, 157)
personList= [person1, person2, person3, person4]
 for i in range(0, len(personlist)):
     if personList[i].getAge() >= 18:
         print("atļauts ienākt")
         print("atļauts aizliegts")
    else:
        print("Nav atļauts ienākt")
         
         
         
''''
person1 = person("Monta", 18)
person2 = person("kristiana",17)
person3 = person("ieva",18)
person4 = person("Angelina",17)


print(person1)
print(person2)
print(person3)
print(person4)

del person4
print(person4)
''''