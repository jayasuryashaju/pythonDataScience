"""
map and filter

map:
    to do an operation on an iterable (list, tuple.)

filter:
    to filter elements in aa iterable with a give condition.


map syntax:
    variable_name = list (map(function, iterable))

filter syntax:
    variable_name = list (filter(function, iterable))

"""

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def square(num):
    return num ** 2


square1 = list(map(square, lst))

print(square1)

square = list(map(lambda x: x ** 2, lst))
print(square)
