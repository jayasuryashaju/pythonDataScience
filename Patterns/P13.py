limit = int(input("enter an number : "))

for i in range(1, limit + 1):
    for j in range(limit + i):
        if j <= limit - i:
            print(" ", end=" ")
        else:
            print("* ", end="")
    print()
