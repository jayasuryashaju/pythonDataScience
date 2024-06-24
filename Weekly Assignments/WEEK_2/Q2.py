"""
leap year or not?
"""

import datetime

print(datetime.datetime.now())


year = int(input("enter a year : "))
leap = False

if year % 4 == 0:
    if year % 100 == 0 and year % 400 == 0:
        leap = True
    elif year % 100 == 0 and year % 400 != 0:
        leap = False
    else:
        leap = True
if leap:
    print("the year is leap year")
else:
    print("the year is not a leap year")
