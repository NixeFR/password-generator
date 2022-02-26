#Import the module random
import random
#Import the module string
import string 

#Creating our password generator function
def pass_gen(length, number):
    #Creating an empty list in case we need multiple passwords
    passwords = []
    #Creating an empty password variable
    password = ''
    #Main loop that generates our password(s).
    for _ in range(number):
        for _ in range(length): password += random.choice(string.ascii_letters + string.digits + string.punctuation)
        passwords.append(password)
        password = ''
    return passwords

#Printing our result
print(pass_gen(32,1))