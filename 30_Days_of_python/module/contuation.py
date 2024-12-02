import string

print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~


otp = string.ascii_letters + string.digits
print(otp[0:6]) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ012345678

from random import random, randint, choice
print(random())
print(randint(6, 100))


def random_user_id():
    id = ""
    for i in range(3):
        digits = str(randint(0, 2))
        letters = choice(string.ascii_letters)
        id += digits + letters
        
    return id       
        
print(random_user_id())
        
        
        
def user_id_gen_by_user():
    number = input('Enter the number of id you need ')
    character = input('Enter the number of characters you need in your id ')


user_id_gen_by_user()
    