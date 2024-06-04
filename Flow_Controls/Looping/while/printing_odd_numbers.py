lower_limit = int(input("enter a limit : "))
upper_limit = int(input("enter a limit : "))

while lower_limit <= upper_limit:
    if lower_limit % 2 != 0:
        print(lower_limit)
    lower_limit += 1

