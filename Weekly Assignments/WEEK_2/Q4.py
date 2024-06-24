"""
wage calculation
"""

age = int(input("enter your age : "))
sex = input("enter your sex : (M / F)  : ")
number_of_days = int(input("enter how many days worked : "))

if sex == 'M' or sex == 'm':
    if 18 <= age < 30:
        wage = 700 * number_of_days
    elif 30 <= age <= 40:
        wage = 800 * number_of_days
    else:
        wage = 0
elif sex == 'F' or sex == 'f':
    if 18 <= age < 30:
        wage = 750 * number_of_days
    elif 30 <= age <= 40:
        wage = 850 * number_of_days
    else:
        wage = 0
print("your wage is ", wage)
