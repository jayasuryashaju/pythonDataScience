lower_limit = int(input("enter a lower limit : "))
upper_limit = int(input("enter an upper limit  : "))

odd_sum = 0
even_sum = 0

for i in range(lower_limit, upper_limit + 1):
    if i % 2 != 0:
        odd_sum += i
    else:
        even_sum += i

print("sum of odd numbers up to given limit : ", odd_sum)
print("sum of even numbers up to given limit : ", even_sum)


