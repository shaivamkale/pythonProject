
# Write a program that generates password using the random library in python, lists and strings.
# Step 1 : Create a list of 10 strings( the strings could be anything but the length of each string
# should be 10 characters. Preferably random characters)
# Step 2 : Generate a random integer between 0 and 10 using the random library in python.
# Step 3 : Use the randomly generated integer as an index to access in each string from the list
# to access that character and store each of those characters in a variable.
# Step 4 : Use the 10 variables that you have for each character to form your password using
# string concatenation.
# Step 5 : Use the shuffle method from the random library to shuffle our generated password to
# increase randomness.
# Step 6 : Neatly print the generated password to inform the user with an appropriate message.
# Challenge : To make the password generation truly random, generate a random index for
# each of the strings.
import random
'''
Archive = ['A2SdEfY34r','B2DrFfh3J4','CdRgZy274r','D37UiopT96']
Archive.append('Er45TuIo97')
Archive.append('Fr45TuIo90')
Archive.append('Gr45TuIo97')
Archive.append('Hr45TuIo97')
Archive.append('Ir45TuIo97')
Archive.append('Jr45TuIo97')
ArchiveStr = 0
RandIndex = random.randrange(0, 10)
temppass = ""

for index in range(0,len(Archive)):
    random.shuffle(Archive)
    temppass += Archive[index]
print('New Generated Password is:', temppass)
'''
'''
x2 = 6
y2 = 7
Equal = x2 + y2
print(Equal)

x = (3,4,5)
print(x)
x = (6,7,8)
print(x)
'''