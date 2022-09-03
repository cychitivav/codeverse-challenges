#Cristian Chitiva
#cychitivav@unal.edu.co
#12/Sept/2018
 
myList = ['Hi', 5, 6 , 3.4, "i"]    #Create the list
myList.append([4, 5]) #Add sublist [4, 5] to myList
myList.insert(2,"f")    #Add "f" in the position 2
print(myList)

myList = [1, 3, 4, 5, 23, 4, 3, 222, 454, 6445, 6, 4654, 455]
myList.sort()   #Sort the list from lowest to highest
print(myList)
myList.sort(reverse = True)   #Sort the list from highest to lowest
print(myList)

myList.extend([5, 77])    #Add 5 and 77 to myList
print(myList)

#List comprehension
myList = []
for value in range(0, 50):
    myList.append(value)

print(myList)

myList = ["f" for value in range(0,20)]
print(myList)

myList = [value for value in range(0,20)]
print(myList)

myList = [value for value in range(0,60,3) if value % 2 == 0]
print(myList)