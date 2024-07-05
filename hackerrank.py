n = int(input("enter a number"))
number = 0
factor = 1
for i in range(1, n+1):
    temp = i
    while temp > 0:
        factor *= 10
        temp //= 10
    number = number * factor + i
    factor = 1

print(number)
