def odd():
    for i in range(10, 31):
        if i % 2 != 0:
            print(i)
            
odd()


list_fruits = ['bananas', 'pineapples', 'guavas']

list_fruits.append('pawpwaw')


del list_fruits[1]

print(list_fruits)