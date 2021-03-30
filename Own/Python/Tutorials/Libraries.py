#Cristian Chitiva
#cychitivav@unal.edu.co
#12/Sept/2018

import random
import datetime
import sys
import time

#Random
value = random.randint(0, 3)
print(value)
myList = [1, 5, 'uy', 4]
print(myList)
print(random.choice(myList))
random.shuffle(myList)
print(myList)

#DateTime
print()
print(datetime.datetime.now())
print(datetime.date.today())
date = datetime.datetime(2000,1,1,00,00,00,00000)
date += datetime.timedelta(days = 1)
print(date)
print(datetime.datetime.now().strftime('%d, %b(%m), %Y'))

#Sys
for i in range(101):
    sys.stdout.write("\r{} %".format(i))
    sys.stdout.flush()
    time.sleep(0.1)

print()
'''if sys.argv[1] == 'help':
    print("Call me")'''