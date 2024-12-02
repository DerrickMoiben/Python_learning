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
        

from math import *    
        
def user_id_gen_by_user():
    number = int(input('Enter the number of id you need '))
    ids = int(input('Enter the number of characters you need in your id '))
    for i in range(ids):
        id = ""
        div = number / 2
        times = ceil(div)
        for i in range(times):
            digits = str(randint(0, times))
            letters = choice(string.ascii_letters)
            id += digits + letters
            
    return f"#{id}"

print(user_id_gen_by_user())
    
    
def rgb_color_gen():
    color1 =  randint(0, 255)
    color2 =  randint(0, 225)
    color3 =  randint(0, 255)
    
    return f'RGB{color1}, {color2}, {color3}'

print(rgb_color_gen())    