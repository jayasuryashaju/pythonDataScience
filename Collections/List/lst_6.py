lst = []

[lst.append(i) for i in range(1, 51) if i % 5 == 0]
print(lst)

lst2 = []

for i in range(1, 51):
    if i % 5 == 0:
        lst2.append(i)

print(lst2)
