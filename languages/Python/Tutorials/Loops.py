#Cristian Chitiva
#cychitivav@unal.edu.co
#12/Sept/2018
 
index = 0

while index <= 10:
    print(index)
    if index == 7:
        index += 2
        continue #Continue or break
    else:
        index += 1
else:
    print("Finish")

#For
myList = [2, 4, 6, 8, 10]

for value in myList:
    print(value)

myList = range(1, 11)

for value in range(0, 20, 3):
    print(value)

for value in range(0, len(myList)):
    print(value)

for index, value in enumerate(myList):
    print(value, ", index:", index)