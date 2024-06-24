"""
Create a Python program that prompts the user to enter two numbers.
Compare the numbers using comparison operators (>, <, ==, !=, >=, <=) and
print out the result of each comparison.
"""

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

if num1 > num2:
    print("Greater is", num1)
    print("Smaller is", num2)
elif num1 < num2:
    print("Greater is", num2)
    print("Smaller is", num1)
else:
    print(num1, "equals", num2)

if num1 != num2:
    print(num1, "not equals", num2)

if num1 >= num2:
    print(num1, "greater than or equals", num2)
else:
    print(num2, "greater than or equals", num1)

if num1 <= num2:
    print(num1, "less than or equals", num2)
else:
    print(num2, "less than or equals", num1)

