"""
syntax
    [print1 if condition else print2 range]

more than two conditions:
    [print1 if condition else print 2 if condition2 else print2 range]
"""

"""print([i ** 2 if i % 2 == 0 else i ** 3 for i in range(1, 31)])

print([[i, 'even'] if i % 2 == 0 else [i, 'odd'] for i in range(1, 21)])

print(['small' if 1 <= i <= 15 else "medium" if 16 <= i <= 35 else 'large' for i in range(1, 50)])"""

lst = ['apple', 'orange', 'grape', 'banana', 'cherry']
print([(i, len(i)) for i in lst])

string = 'luminartechnolab'
vowels = 'aeiouAEIOU'
print(len([i for i in string if i in vowels]))
print(len([i for i in string if i not in vowels]))

