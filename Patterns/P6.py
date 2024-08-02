"""
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""

limit = int(input("enter a limit : "))

for i in range(limit):
    for j in range(1, limit+1):
        print(j, end=" ")
    print()