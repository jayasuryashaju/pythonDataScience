tu = (10, 15, 20, 25, 30, 35, 40, 50, 100)

# new_tuple = (tu[0:2] + tuple([75]) + tu[3:])
# print(new_tuple)


lst = list(tu)
lst[2] = 75
tu = tuple(lst)
print(tu)
