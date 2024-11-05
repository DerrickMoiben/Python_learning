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


sortedlist = sorted(companies, reverse=True)
print(sortedlist)
print(companies)

slice1 = companies[3:8]
print(slice1)