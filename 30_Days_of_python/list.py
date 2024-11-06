
#List: is a collection which is ordered and changeable(modifiable). Allows duplicate members.

l = [1, 2, 3, 4, 5]

print(len(l))
one = l[0]
middle = l[2]
last = l[4]

print(one, middle, last)

mix = ['Moiben', 19, 6.0, 'confused', 13]
companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBm', 'Oracle', 'Amazon']
print(mix)
result = len(companies)
print(companies[0])

r = result // 2

print(companies[r])
print(companies[-1])
companies[0] = 'X'
print(companies)
companies.append('IT')
print(companies)
companies.insert(r, 'IT')
print(companies)
two = companies[1]
y = two.upper()
print(y)
print(companies)
c = '#'.join(companies)
print(c)
find = 'IT' in companies
print(find)


# sortedlist = sorted(companies, reverse=True)
# print(sortedlist)
# print(companies)

# slice1 = companies[3:8]
# print(slice1)

# del companies[5:8]
# print(companies)

result = len(companies)

r3 = result // 2

del companies[r3]
print(companies)

del companies[0]
print(companies)

del companies[6]
del companies[2]

print(companies)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

joined = front_end + back_end
print(joined)

fullstack = joined.copy()
fullstack.insert(5, 'Python')
fullstack.insert(6, 'SQL')

print(fullstack)


ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
sortedages = sorted(ages)
print(sortedages)
min = sortedages[0]
max = sortedages[-1]

print(min, max)
sortedages.append(19)
sortedages.append(26)
print(sortedages)

median = len(sortedages)

result = median // 2
print(sortedages[result])

j = 0
for i in sortedages:
    j += i

avarage = j / median
print(avarage)