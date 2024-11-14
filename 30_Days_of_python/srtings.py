a = 'Thirty '
c = 'Days '
d = 'of '
e = 'Python'

f = a  + c + d + e

print(f)

i = 'Coding '
j =  'For '
k = 'All'

m = i + j + k
print(m)

company = m
print(company)
print(len(company))
print(company.upper())
b = company.lower()
print(b)
print(company.capitalize().title())
print(company.swapcase())
b = company[7:14]
print(b)
print('Coding' in 'company')
print(company.replace('Coding', 'Python'))
print(company.split( ))

companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" 

print(companies.split(','))
print(company[0])
print(company.find('Coding'))


python = 'Python For Everyone'

print(company.find('C'))
print(company.find('F'))
print(company.rfind('i'))


sentence = 'You cannot end a sentence with because because because is a conjuction'

print(sentence.find('because'))
print(sentence.rfind('because'))

sen_1 = sentence[0:30]
sen_2 = sentence[55:70]

sen_3 = sen_1 + sen_2

print(sen_3)

print(company.startswith('Coding'))
print(company.endswith('coding'))

remove = ' Coding For All '
print(remove.strip(' '))
print(remove)

var1 = '30DayOfPython'
var2 = 'thirty_days_of_python'

print(var1.isidentifier())
print(var2.isidentifier())

list = ['django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = ' #'.join(list)
print(result)


y = 'I am enjoying this challenge'
k = 'I just wonder what is next'

print(y.expandtabs(10))

radius = 10
area = 3.142 * radius ** 2


print('radius = 10')
print('area = 3.142 * radius ** 2')
print(f'The area of a circle with radius {radius} is {area} meters square')


# import math
# radius = int(input('Enter the radius'))
# area = print(f'area = {math.pi} ** {radius} ** {2}')
# print(f'The area of the circle with {radius} is {math.pi} meters square')

a =  8
b = 6

print(f'{a} + {b} = {a+b}')
print(f'{a} - {b} = {a-b}')




companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" 

print(companies.split(','))