"""
Python program to check if a given number is an Armstrong number
"""


def armstrong_numbers(number):
    am_number = 0
    check = number
    while number != 0:
        temp = number % 10
        am_number += temp ** len(str(check))
        number = number // 10
    if check == am_number:
        return True
    else:
        return False


num = int(input("enter a number : "))
print(armstrong_numbers(num))
