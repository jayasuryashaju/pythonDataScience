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
temp = 1
value = 1
for i in range(1, limit*2):
    if temp < limit:
        print(str(value) * temp)
        temp += 1
        value += 1
    else:
        value -= 1
        temp -= 1
        print(str(value) * temp)
