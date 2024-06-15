lst = []

for i in range(1, 101):
    lst.append(i)
print(lst)

lst2 = []

[lst2.append(i) for i in range(1, 101)]
print(lst2)
