#Cristian Chitiva
#cychitivav@unal.edu.co
#16/Sept/2018

class TinyIntError(Exception):
    def __init__(self):
        self.message = "The number doesn't have the characteristics of a tinyInt"

    def __str__(self):
        return self.message

def validateTinyInt(value):
    return value >= 0 and value <=255

def validateInt(value):
    return isinstance(value, int)

try:
    number = 'f'
    if validateInt(number):
        if validateTinyInt(number):
            print("The number is correct")
        else:
            raise TinyIntError()
    else:
        raise ValueError("It isn't a integer")
except TinyIntError as e:
    print(e)
except ValueError as e:
    print(e)