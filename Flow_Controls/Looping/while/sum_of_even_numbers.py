lower_limit = int(input("enter a limit : "))
upper_limit = int(input("enter a limit : "))
result = 0
while lower_limit <= upper_limit:
    if lower_limit % 2 == 0:
        result += lower_limit
    lower_limit += 1
print("the sum of even numbers up to the limit = ", result)
