"""
A, b, c = 0, 0, 0. Write a python program to print all permutations using those three variables.
"""

limit = int(input("enter a limit : "))

# for i in range(0, limit):
#     for j in range(0, limit):
#         for k in range(0, limit):
#             print([i, j, k])

print([(i, j, k) for i in range(0, limit) for j in range(0, limit) for k in range(0, limit)])
