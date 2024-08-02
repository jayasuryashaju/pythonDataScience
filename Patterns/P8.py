"""
5 5 5 5 5
5 5 5 5
5 5 5
5 5
5
"""

limit = int(input("enter a limit : "))
for i in range(limit):
    for j in range(limit-i):
        print(limit, end=" ")
    print()