import random
import string 

def pass_gen(length, number):
    # Creating a list just in case the user would like to have multiple passwords at once.
    passwords = []
    password = ''
    for _ in range(number):
        for _ in range(length): password += random.choice(string.ascii_letters + string.digits + string.punctuation)
        passwords.append(password)
        password = ''
    return passwords

print(pass_gen(32,1))
