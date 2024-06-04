price = int(input("enter the price of the bike : "))

if price >= 100000:
    tax = price * 0.15
elif 50000 <= price < 100000:
    tax = price * 0.1
else:
    tax = price * 0.05

print("tax amount :", round(tax, 2))


