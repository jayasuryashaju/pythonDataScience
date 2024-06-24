"""
Write a Python program that takes two numbers as input from the user and performs arithmetic
operations (addition, subtraction, multiplication, division, and modulus) on them. Display
the results of each operation.
"""


def add(num_1, num_2):
    return num_1 + num_2
def sub(num_1, num_2):
    return num_1 - num_2
def mult(num_1, num_2):
    return num_1 * num_2
def div(num_1, num_2):
    return num_1 / num_2
def mod(num_1, num_2):
    return num_1 % num_2

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("Sum of the two numbers = ", add(num1, num2))
print("Difference of the two numbers = ", sub(num1, num2))
print("Product of the two numbers = ", mult(num1, num2))
print("Division of the two numbers = ", div(num1, num2))
print("Modulus of the two numbers = ", mod(num1, num2))
