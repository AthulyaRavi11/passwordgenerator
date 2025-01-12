import random
import string

l = int(input("Enter the length of the password: "))

def passwordgen(l):
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    special = string.punctuation  # Corrected this line

    allchars = lower + upper + digits + special
    password = ''.join(random.choice(allchars) for i in range(l))
    print("Password is:", password)

passwordgen(l)

    
    
        
