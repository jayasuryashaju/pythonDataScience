"""
Write a program that takes inputs  from user and prints the multiplication table of that number
"""

number = int(input("enter a number : "))

i = 1
while i <= 10:
    print(i, "*", number, "=", number * i)
    i += 1
