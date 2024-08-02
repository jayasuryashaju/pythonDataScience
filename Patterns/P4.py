"""
non pascals triangle
"""


limit = int(input("enter a limit : "))

for i in range(1, limit):
    n = 1
    for j in range(limit, 0, -1):
        if j > i:
            print(" ", end=" ")
        else:
            print(n, end=" ")
            n += 1
    for k in range(i-1, 0, -1):
        print(k, end=" ")
    print()

