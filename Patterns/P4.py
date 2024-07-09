"""
non pascals triangle
"""


limit = int(input("enter a limit : "))
temp = limit
for i in range(1, limit):
    print(" " * temp, end="")
    for j in range(1, i*2, 2):
        print(j, end=" ")
    temp -= 1
    print()
