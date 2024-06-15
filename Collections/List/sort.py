"""
sorting a list:
    ascending
    descending


"""

lst = [40, 10, 1, 35, 29, 47, 21, 25, 3, 0, 100]

for i in range(len(lst)):
    for j in range(len(lst)):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]

print(lst)

lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)
