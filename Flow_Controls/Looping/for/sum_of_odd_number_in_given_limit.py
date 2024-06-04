lower_limit = int(input("enter a lower limit : "))
upper_limit = int(input("enter an upper limit  : "))

result = 0

for i in range(lower_limit, upper_limit + 1):
    if i % 2 != 0:
        result += i

print("sum of odd numbers up to given limit : ", result)

