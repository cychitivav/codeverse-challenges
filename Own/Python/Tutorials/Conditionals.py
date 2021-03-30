#Cristian Chitiva
#cychitivav@unal.edu.co
#12/Sept/2018
 
Example = "Goal"

if Example == "Goal":
    print("Goooooooooaaaaal")
elif Example == 'Stick':
    print('almost')
elif Example == '8':    #Pass for execute the program tentatively
    pass
else:
    print("Out")

Score = True if Example == "Goals Finish" else False
print(Score)

variable = None
variable2 = 7

if variable:
    print("It's full")
elif not variable and variable2 < 10:
    print("Ok")
    if variable2 or variable:
        print("Only one")
else:
    print("Nothing")