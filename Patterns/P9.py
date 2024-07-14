"""
0 1 2 3 4 5
0 1 2 3 4
0 1 2 3
0 1 2
0 1
"""

limit = int(input("enter a limit : "))

for i in range(limit):
    for j in range(limit-i+1):
        print(j, end=" ")
    print()