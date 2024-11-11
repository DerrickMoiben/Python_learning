# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
print(it_companies)
it_companies.add('Twitter')
print(it_companies)

it_companies.update(['codverse tech', 'mobidev', 'mbtrix'])
print(it_companies)

it_companies.remove('mbtrix')
print(it_companies)

act = it_companies.pop()
print(act)

act = it_companies.pop()
print(act)

it_companies.discard('kim')

c = A.union(B)

A.intersection(B)
print(A)


d = A.issubset(B)
print(d)

e = A.isdisjoint(B)
print(e)

d = B.union(A)


print(c)
print(d)


print(A)
print(B)

A.symmetric_difference(B)
print(A)

del A
print(A)

del B
print(B)