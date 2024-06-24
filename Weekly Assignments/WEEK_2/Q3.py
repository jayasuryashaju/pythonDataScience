"""
largest among three numbers

"""

number_1 = int(input("enter a number : "))
number_2 = int(input("enter a number : "))
number_3 = int(input("enter a number : "))

largest = number_1

if number_2 > number_1 > number_3 or number_2 > number_3 > number_1:
    largest = number_2
elif number_3 > number_1 > number_2 or number_3 > number_2 > number_1:
    largest = number_3
else:
    largest = number_1

print("the largest number = ", largest)

