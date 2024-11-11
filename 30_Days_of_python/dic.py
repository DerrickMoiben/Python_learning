dog = {
    'name': 'Lasy',
    'colour': 'blue',
    'breed': 'Bulldog',
    'legs': '4'
}

student = {
    'first_name': 'kim',
    'second_name': 'kimtai',
    'third_name': 'moiben',
    'geder': 'male',
    'age': 250,
    'skills': ['django', 'python', 'flask', 'html', 'c'],
    'country':'kenya',
    'address':{
        'pobox': 13,
        'zipcode': 34647
    }
    }

print(len(student))
print(student['skills'])
print(type(student['skills']))

student['skills'].append('css')

print(student['skills'])

keys = student.keys()

print(keys)

values = student.values()
print(values)
