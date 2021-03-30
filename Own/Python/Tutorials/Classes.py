#Cristian Chitiva
#cychitivav@unal.edu.co
#13/Sept/2018
 
class Pencil:
    _length = '10 cm'#Class variable notation

    def __new__(self, color = 'Rojo', eraser = True, graphite = False):#Constructor
        self.__init__(self, color, eraser, graphite)
    
    def __init__(self, color, eraser, graphite):
        self.color = color
        self.__eraser = eraser#Private
        self.graphite = graphite
    
    def draw(self):
        print("The pencil is drawing")
    
    def __erase(self):#Private
        if self.__eraser:
            print("The pencill is erasing")
        else:
            print("It's not possible to erase")
    
    def getErase(self):
        return self.__erase()

    #Properties
    @property #Getter
    def eraser(self):
        return self.__eraser

    @eraser.setter
    def eraser(self, newValue):
        self.__eraser = newValue

    @staticmethod
    def thickness():
        return '0.65 cm'

pen = Pencil("Verde", True, True)
#pen.draw()
#pen.getErase()
print(Pencil._length)
Pencil(1)
#Info class
#print('\n', pen.__dict__)
print()

print(pen.eraser)
pen.eraser = False
print(pen.eraser)

print("Class:", Pencil.thickness())
print("Instance:", pen.thickness())