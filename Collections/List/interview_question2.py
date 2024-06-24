lst = [15, 3, 5, 8, 10, 20, 7, 2]
total = sum(lst)
new_lst = []
for element in lst:
    new_lst.append(total - element)
print(lst)
print(new_lst)
