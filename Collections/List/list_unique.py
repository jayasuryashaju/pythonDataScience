lst = [1, 2, 1, 3, 5, 6, 9, 7, 3, 9, 8, 4, 5, 6, 3, 2, 1, 5, 2, 10]

new_list = []
for element in lst:
    if element not in new_list:
        new_list.append(element)

print(lst)
print(new_list)
