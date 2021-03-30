#Cristian Chitiva
#cychitivav@unal.edu.co
#13/Sept/2018

import StrucModule #Create the folder "__pycache__" with the compiled file
from Functions import division as newDivision


if __name__ == '__main__':
    value = newDivision(7, 6)
    print(value)

    value = StrucModule.division(7, 6)
    print(value)