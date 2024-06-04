"""
printing the summ of numbers up to the given limit
"""

limit = int(input("enter a limit : "))
i = 1
result = 0
while i <= limit:
    result += i
    i += 1
print("the sum of the give numbers is : ", result)
