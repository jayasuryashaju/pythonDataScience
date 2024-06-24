"""
Write a function to calculate the factorial of a number recursively.
"""


def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n - 1)


result = fact(5)
print(result)
