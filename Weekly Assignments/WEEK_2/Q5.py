"""
DISCOUNT CALCULATOR
"""

quantity = int(input("enter the quantity : "))
cost = 100

if quantity > 1000:
    total_cost = (quantity * 100) - (quantity * 100) * 0.01
else:
    total_cost = (quantity * 100)


print("the total cost for the product = ", total_cost)