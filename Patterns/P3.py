"""
* * * * *
* * * *
* * *
* *
*
* *
* * *
* * * *
* * * * *

"""

limit = int(input("enter a limit : "))
temp = limit
temp2 = 2

for i in range(0, (limit * 2)-1):
    if i < limit:
        print("* " * temp)
        temp -= 1
    else:
        print("* " * temp2)
        temp2 += 1



