"""
deleting an element from a list:
    remove()
    lst.remove(element)

    pop()
    lst.pop(index)
"""

lst = [1, 2, 3, 2, 4, 2, 4, 6, 4, 7, 8, 0]
lst.remove(2)
lst.remove(6)

print(lst)
lst.pop()
lst.pop(4)
print(lst)
