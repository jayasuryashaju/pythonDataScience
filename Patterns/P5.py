"""
1
22
333
4444
333
22
1
"""

limit = int(input("enter a limit : "))

for i in range(1, limit):
    for j in range(i):
        print(i, end=" ")
    print()

for i in range(limit-2, 0, -1):
    for j in range(i):
        print(i, end=" ")
    print()
