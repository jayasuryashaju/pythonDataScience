number = int(input("enter a number : "))

reverse_number = 0
while number > 0:
    reverse_number *= 10
    reverse_number += (number % 10)
    number = number // 10
print("reversed number = ", reverse_number)
