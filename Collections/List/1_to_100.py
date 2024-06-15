
"""
lst = [i for i in range(1, 101)]
lst_even = [i for i in lst if i % 2 == 0]
lst_odd = [i for i in lst if i % 2 != 0]
print(sum(lst))
print(sum(lst_even))
print(sum(lst_odd))

"""
lst = []
lst_even = []
lst_odd = []
for i in range(1, 101):
    lst.append(i)
for i in lst:
    if i % 2 == 0:
        lst_even.append(i)
    else:
        lst_odd.append(i)
print(lst)
print(lst_even)
print(lst_odd)
print(sum(lst))
print(sum(lst_even))
print(sum(lst_odd))
