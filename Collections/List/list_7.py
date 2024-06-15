lst = [1, 3, 5, 4, 8, 6, 9, 10, 15, 20]

for i in range(1, len(lst) + 1):
    print(lst[i - 1] ** i)

j = 1
for i in lst:
    print(i ** j)
    j += 1
