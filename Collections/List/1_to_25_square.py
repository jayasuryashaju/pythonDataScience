
lst = [i**2 for i in range(1, 26) if i % 2 == 0]
print(lst)
print(sum(lst))

lst2 = []
for i in range(1, 26):
    if i % 2 == 0:
        lst2.append(i**2)
print(lst2)
print(sum(lst2))