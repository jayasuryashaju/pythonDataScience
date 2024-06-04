lower_limit = int(input("enter a lower limit : "))
upper_limit = int(input("enter an upper limit  : "))

count = 0

for i in range(lower_limit, upper_limit+1):
    if i % 2 == 0:
        count += 1
print("count of even numbers in given limit : ", count)
