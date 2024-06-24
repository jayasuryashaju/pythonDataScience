"""
arithmetic operations
"""

num_1 = int(input("enter a number  : "))
num_2 = int(input("enter a number  : "))

choice = input(" for addition + \n"
               "for subtraction - \n"
               "for multiplication * \n"
               "for division / \n")

if choice == "+":
    print("the sum of the two numbers = ", num_1 + num_2)
elif choice == "-":
    print("the difference of two numbers = ", num_1 - num_2)
elif choice == "*":
    print("the product of two numbers = ", num_1 * num_2)
elif choice == "/":
    print("the division of two number = ", num_1 / num_2)
else:
    print("not a valid choice")
