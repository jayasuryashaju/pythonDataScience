"""
finding the second-largest number
"""

num1 = int(input("enter a number : "))
num2 = int(input("enter a number : "))
num3 = int(input("enter a number : "))

if (num2 < num1 < num3) or (num3 < num1 < num2):
    print(num1, "is the second-largest number")
elif (num1 < num2 < num3) or (num3 < num2 < num1):
    print(num2, "is the second-largest number")
elif (num1 < num3 < num2) or (num2 < num3 < num1):
    print(num3, "is the second-largest number")
else:
    print("invalid input")

#method using nested if conditions


if num1 < num3 and num2 < num3:
    if num2 > num1:
        print(num2, "is the second-largest number")
    else:
        print(num1, "is the second-largest number")
elif num1 < num2 and num3 < num2:
    if num1 > num3:
        print(num1, "is the second-largest number")
    else:
        print(num3, "is the second-largest number")
elif num2 < num1 and num3 < num1:
    if num2 < num3:
        print(num3, "is the second-largest number")
    else:
        print(num2, "is the second-largest number")
else:
    print("invalid input")
