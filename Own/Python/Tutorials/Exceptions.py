#Cristian Chitiva
#cychitivav@unal.edu.co
#12/Sept/2018

a = 4
b = 0
myList = [3, 4]

try: 
    print(a / b)
    print(myList[9])
except Exception as e:
    print(e)
finally: #Always runs
    print("End")