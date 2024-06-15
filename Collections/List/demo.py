"""
Properties of List:
    lst = []
    lst1 = [1,2,3,4,5]
    print(lst1)

O/P:
    [1,2,3,4,5]

    List supports heterogeneous data.
    List supports duplicate values.
    List is mutable.

index: -
    index is used to get a particular  value from a list.
    index starts from 0.
    lst = [1, 2, 3, 4]
    print(lst[1])

O/P:
    >> 2


"""
lst = [1, 2, 3, 4]
print(lst)

lst2 = list()

lst3 = [1, 2, 3, 'python', True, False]
print(lst3)

lst4 = [10, 2, 10, 'python', 'python', True, False]
print(lst4)

lst = [1, 2, 3, 4, 5, 6, 7, 8]

print(lst[1])
print(lst[4])
print(lst[6])

lst[5] = 43
lst[2] = "Luminar"
print(lst)
