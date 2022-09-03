#Cristian Chitiva
#cychitivav@unal.edu.co
#12/Sept/2018

def nameFunction():
    return("Hi")

renameFunction = nameFunction
print(renameFunction())

def withArguments(a, b):
    return("Hi")


print(withArguments(1, 3))

def withArgumentsPredetermined(a, b = 'r', function = nameFunction):
    function()
    return("Hi", 3, 5)


print(withArgumentsPredetermined(1, 3))

#Global variables
def withNewGlobal():
    global var
    var = 3
    return True

print(withNewGlobal())

def withGlobal():
    global variable
    variable = 3
    return False
 
print(withGlobal())

#Arguments
def function(*args):       #Create a tuple
    sum = 0
    for value in args:
        sum += value
    return sum

print(function(1, 4, 5, 6, 3, 1, 2))

def twoFunction(**kwargs):       #Create a dictionary
    sum = 0
    for value in kwargs.values():
        sum += value
    return sum

print(twoFunction(a = 4, b = 6))

#Lambda    (anonimous functions) 
miniFunction = lambda firstArg, secondArg : firstArg + secondArg
void = lambda : 8

print(miniFunction(1, 3))
print(void())

#Nested functions
def division(dividend, divider):
    def checkNum():
        return divider != 0
    return dividend / divider if checkNum() else False

print(division(2, 7))
print(division(5, 0))

#Decorator
def decorator(function):
    def newFunction(*args):
        function(*args)
        print("After function")
    print("Before function")
    return newFunction

@decorator
def simpleFunction(t):
    print("During function")

print(simpleFunction(6))

#Generators
def generator(*args):#Create objects without storing them in memory
    for value in args:
        yield 'y', value, True

for value in generator(1, 2, 3):
    print(value)

#Docstring
def documentation():
    """Here is the information of the function
This is the docString
    """

print(documentation.__name__, ": ") 
print(documentation.__doc__)  #help(nameFunction) in console