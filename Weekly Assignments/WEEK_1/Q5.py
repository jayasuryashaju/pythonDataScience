"""
Write a Python program that takes three numbers as
input from the user and prints out the maximum and
minimum numbers in the list.
"""

num_1 = int(input("enter a number : "))
num_2 = int(input("enter a number : "))
num_3 = int(input("enter a number : "))

if num_1 > num_2 > num_3 or num_1 > num_3 > num_2:
    print(num_1, "is the largest number")
elif num_2 > num_1 > num_3 or num_2 > num_3 > num_1:
    print(num_2, "is the largest number")
else:
    print(num_3, "is the largest number")

if num_1 < num_2 < num_3 or num_1 < num_3 < num_2:
    print(num_1, "is the smallest number")
elif num_2 < num_1 < num_3 or num_2 < num_3 < num_1:
    print(num_2, "is the smallest number")
else:
    print(num_3, "is the smallest number")



