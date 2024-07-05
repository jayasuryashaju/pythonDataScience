"""
To d0 all list operation in a single line

Three methods to understand:

    1. range of elements added into a list

    2. ranges of elements added into a list based on a condition

    3. ranges of elements added into a list based on multiple conditions

"""

lst = [i for i in range(1, 51)]
print(lst)

print([(i, i**2) for i in range(1, 26)])

print([i+6 for i in range(1, 26)])

print([i ** 3 for i in range(10) if i % 2 != 0])


print([i ** 2 if i % 2 == 0 else i ** 3 for i in range(1, 20)])
