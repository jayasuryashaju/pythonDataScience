"""
append function is used to add values to a list
lst.append()
append() function can only add a single element at a time

to add more than one element to a list we use extend() function
lst.extend([1, 32, 428, 93])

to add a value to a position insert() function is used
insert(index, object)
lst.insert(0, 845)

"""

lst = [1, 4, 3, 5, 10]

lst.append(132)
lst.append(23)
lst.extend([29, 19, 32])
lst.insert(1, 9384)

print(lst)

