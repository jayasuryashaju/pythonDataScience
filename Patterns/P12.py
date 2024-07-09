"""
            1
        1   2   1
    1   2   3   2   1
1   2   3   4   3   2   1

"""

limit = int(input("enter a number : "))
temp = limit

for i in range(1, limit+1):
    value = 1
    for j in range(limit + i):
        if j <= limit - i:
            print(" ", end=" ")
        else:
            if j < limit:
                print(value, end=" ")
                value += 1
            else:
                print(value, end=" ")
                value -= 1
    print()
