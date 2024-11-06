#Tuple: is a collection which is ordered and unchangeable or unmodifiable(immutable). Allows duplicate members.


tup = ()

sis = ('Cherop', 'Mish')

bro = ('Avis',)

siblings = sis + bro

print(siblings)

print(len(siblings))

lst = list(siblings)

lst.append('Rashid')
lst.append('Mum')

print(lst)


parents = ('Rashid', 'Mum')

family = siblings + parents
print(family)


*siblings_unpacked, parents1, parents2 = family

print(siblings_unpacked)
print(parents1, parents2)


fruits = ('oranges', 'mangoes', 'pawpaw')
animals = ('sheep', 'goat', 'cow')
vegs = ('kales', 'cabbage', 'soik')

food = fruits + animals + vegs
lst1 = list(food)
print(lst1)

len1 = len(lst1)

middle = len1 // 2

# del lst1[middle]

# print(lst1)


del  lst1[0:3]
del lst1[-3:]

print(lst1)

del food



nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)