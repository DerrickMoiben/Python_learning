# for i in (range(11)):
#     print(i)


# st = 0

# while st < 10:
#     print(st)
#     st = st + 1

# else:
#     print(st)

# numbers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# for number in numbers:
#     print(number)

# st = 10
# while st > 0:
#     print(st)
#     st = st - 1


# for i in range(0, 8):
#     print('#' * i)


# y = 'kim'
# for x in y:
#     for t in x:
#         print(t)


# for i in range(9):
#     print('#########')


for i in range(9):
    for j in range(9):
        print('#', end='')

    print()

# for i in range(0, 11):
#     print(i)
#     for j in range(11):
#         print (f'{i} * {j} = {i * j}')
# print()


for i in range(11):
    print(f'{i} * {i} = {i * i}')


ls =  ['Python', 'Numpy','Pandas','Django', 'Flask']

for item in ls:
    print(item)

even = 0
odd = 0
for i in range(0, 100):
    if i % 2 == 0:
        even = even + 1
        print('This is an even number', i)
    else:
        odd = odd + 1
        print('THis is an odd number', i)
print(f'The sum of even numbers is {even} while the numbers of the odd numbers is {odd}')


sum = 0
even = 0
odd = 0
for i in range(0, 101):
    sum = sum + i
    if i % 2 == 0:
        even = even + i
    else:
        odd = odd + i
    
print('The sum of all numbers is', sum)
print(f'The sum of even numbers is {even}, while the sum of odd numbers is {odd}')

from . import countries

for i in countries:
    j = 'land' in i
    print(j)