#Cristian Chitiva 
#cychitivav@unal.edu.co
#12/Sept/2018

print()
sString = 'my string, I can to use \ndoubles quotes "Example"'   #Single quotes to write with double quotes and line break \n
print("String with single quotes: ", sString)

dString = "my string, I can to use \nsingle quotes 'Example'"  #Double quotes to write with single quotes and line break \n                  
print("String with double quotes: ", dString)

tstring = '''my string, 
I can do line breaks
with single quotes "Example"'''
print("String with triple quotes: ", tstring)     #Single quotes to write with double quotes and line breaks

tstring = """my string, 
I can do line breaks
with single quotes 'Example'"""
print("String with triple quotes: ", tstring)     #Double quotes to write with single quotes and line breaks

concat = sString + "concatenate with" + dString    #Concatenate srings
print(concat)

concat = sString + "concatenate with " + dString    #Concatenate srings with plus
print(concat)

concat = "%s concatenate with %s" %(sString, dString)    #Concatenate srings with %
print(concat)

concat = "{} concatenate with {}".format(sString, dString)    #Concatenate srings with format
print(concat)

#Strings aas lists
string = "This is a string"
print(string, ", and", string[2], "is the third character",)  #Print the character with index 2
print(string, ", and", string[-2], "is the penultimate character")     #Print the penultimate character
print(string, ", and", string[0:6], "is a part of the string")     #Print from character 0 to character 6
print(string, ", and", string[-4:-2], "is a part of the string")    #Print a part of the string to count down
print(string, ", and", string[::2], "is the string with jumps")     #Print all the string with jumps to 2
print(string, ", and", string[::-1], "is the reverse string")      #Print the reverse string

#String methods
print()
string1 = "Hello"
string2 = "world"

result = "{} {}".format(string1, string2)   #Format string
print(result)
result = "{a} {b}. {b} {a}".format(b = string1, a = string2)    #Format string with variables
print(result) 
result = result.lower()  #Change all the characters to lower case
print(result)
result = result.upper()  #Change all the characters to upper case
print(result)
result = result.title()  #Change the first characters of each word to upper case
print(result)

pos = result.find("Hello")   #Print the position of the first character of the word "Hello"
print(pos)
pos = result.count("l")     #Print how many times i repeats l
print(pos)

newString = result.replace('l', 'y')    #Change l by y
print(newString)

words = result.split(' ')   #Split the string each time that space
print(words)