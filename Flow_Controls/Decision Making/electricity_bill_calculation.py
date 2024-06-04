"""
calculating electricity bill
unit (user input)
up to 100 units bill is zero
101-200 unit charges = 5
above 200 unit charges = 10
"""


electricity_units = int(input("enter the units of electricity consumed : "))

if electricity_units > 200:
    bill_amount = 500 + (electricity_units - 200) * 10
elif 100 < electricity_units <= 200:
    bill_amount = (electricity_units - 100) * 5
else:
    bill_amount = 0

print("the bill amount = ", bill_amount)
