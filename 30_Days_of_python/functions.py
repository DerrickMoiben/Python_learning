# def numbers(n):
#     sum = 0
#     for i in range(n+1):
#         sum += i
#     return  sum

# print(numbers(10))
# print(numbers(110))

# def names(first, last):
#     space = ' '

#     full =  first + space + last
#     return full

# fuc = names(first='moiben', last='kimutai')
# print('My full names are kim ', fuc)



# def karatina(name, *units):
#     print(name)
#     for unit in  units:
#         print(str(unit))

# testing = karatina('kim', 'com213', 'com214', 'com245')
# print(testing)


# def generate_groups (team,*args):
#     print(team)
#     for i in args:
#         print(i)
# print(generate_groups('Team-1','Asabeneh','Brook','David','Eyob'))




def add_two_numbers(a, b):
    sum = a + b
    return sum
print(add_two_numbers(5, 10))


import math
def area(r):
    circle = math.pi * r * r
    return circle

print(area(16))

def add(*args):
    sum = 0
    for num in args:
        sum += num

    return sum

addition = add(5, 6, 7, 7, 6, 10)
print(addition)


# def check_season(month):
#     if month in ['December', 'January', 'February']:
#         return 'Winter'
#     elif month in ['March', 'April', 'May']:
#         return 'Spring'
#     elif month in ['June']:
#         return 'Summer'
#     elif month in ['September', 'October', 'November']:
#         return "Autum"
#     else:
#         return 'Invalid Month'

# month = input('Enter the month ')
# season = check_season(month)
# print(f'The season for {month} is {season}')


# def reverse_list(lst):
#     lst.reverse()
#     for item in lst:
#         print((item))

# print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
# print(reverse_list1(["A", "B", "C"]))
# # ["C", "B", "A"]


# def reverse(lsr):
#     reverse_lst = []
#     for item in lsr:
#         reverse_lst.insert(1, item)
#     return reverse_lst

# lsr = [1, 2, 5, 6]
# print(reverse(lsr))


def reverse_list(lst):
    lst.reverse()
    lstreverse= []
    for item in lst:
        lstreverse.append(item)
    return lstreverse

print(reverse_list([1, 2, 3, 4, 5]))



def upper(lst):
    upadated = []
    for item in lst:
        str(lst.upper())
        upadated.append(item)

upper(['kim'])