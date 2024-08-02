"""
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15

"""

limit = int(input("enter a limit : "))
value = 1

for i in range(limit):
    for j in range(i+1):
        print(value, end=" ")
        value += 1
    print()
