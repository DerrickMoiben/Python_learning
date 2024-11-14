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
