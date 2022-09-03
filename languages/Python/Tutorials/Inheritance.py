#Cristian Chitiva
#cychitivav@unal.edu.co
#16/Sept/2018

class Feline:
    @property
    def retractableClaws(self):
        return True

class Pet():
    def __init__(self, name = "None"):
        self.name = name
    
    def showName(self):
        print(self.name)


class Cat(Feline, Pet):
    def __init__(self, name = "None"):
        super().__init__(name)
    def hunt(self):
        return "Hunt mouses"
    
    def showName(self):#Override
        Pet.showName(self)
        print("The name of the cat is {}".format(self.name))

class Jaguar(Feline):
    def hunt(self):
        return "Hunt large mammals"

    @classmethod
    def size(cls):
        print("Big")

    def __str__(self):
        return "Overrive method __str__"
    
cat = Cat("Paco")
jaguar = Jaguar()

print(cat.retractableClaws)
print(jaguar.retractableClaws)
print()
print(cat.hunt())
print(jaguar.hunt())

print()
cat.showName()

print()
Jaguar.size()
print(jaguar)