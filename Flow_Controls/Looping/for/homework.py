"""
lower, upper
print prime numbers up to the limit
"""

lower_limit = int(input("enter a limit : "))
upper_limit = int(input("enter a limit : "))


for i in range(lower_limit, upper_limit+1):
    count = 0
    for j in range(1, (i // 2)+1):
        if i % j == 0:
            count += 1
    if count <= 1:
        print(i)


