"""
Count the total number of digits in a number

"""

number = int(input("enter a number : "))

count = 0

while number:
    count += 1
    number //= 10

print("the number of digits in the number : ", count)
