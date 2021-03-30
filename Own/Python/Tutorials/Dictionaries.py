# Cristian Chitiva
# cychitivav@unal.edu.co
# 12/Sept/2018

myDictionary = {3: 43, '6': 54, 36: "Hi",
                32: "vrvr"}  # The keys can't to modify
myDictionary['y6'] = 65  # Add key and value
print(myDictionary['y6'])

value = myDictionary.get("e", "else")  # If "e" don't exists, value is "else"
print(value)

del myDictionary['6']  # Delete the key '6'
print(myDictionary)

keys = list(myDictionary.keys())  # Get the keys of myDictionary
values = tuple(myDictionary.values())  # Get the values of myDictionary
print(keys, values)

myDictionary2 = {4: "tr", 65: 76}
myDictionary.update(myDictionary2)  # Concatenate dictionaries
print(myDictionary)
