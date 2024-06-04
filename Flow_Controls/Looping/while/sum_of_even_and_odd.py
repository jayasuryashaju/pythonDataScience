lower_limit = int(input("enter a limit : "))
upper_limit = int(input("enter a limit : "))

even_sum = 0
odd_sum = 0

while lower_limit <= upper_limit:
    if lower_limit % 2 == 0:
        even_sum += lower_limit
    else:
        odd_sum += lower_limit
    lower_limit += 1

print("the sum of even numbers up to the limit = ", even_sum)
print("the sum of odd numbers up to the limit = ", odd_sum)
