"""
Create a Python program that prompts the user to enter their age and checks if they are eligible to vote.
Use logical operators to check if the age is greater than or equal to 18 and less than or equal to 120.
Print a message indicating whether the person can vote or not.
"""

age = int(input("enter your age : "))

if 18 <= age <= 120:
    print("eligible to vote")
else:
    print("not eligible to vote")
