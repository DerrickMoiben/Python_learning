numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

#synthax for the list compression is this
# syntax
#[i for i in iterable if expression]

positive = [i for i in numbers if i >= 0]

print(positive)