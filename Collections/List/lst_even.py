

"""
lst = [i for i in range(1, 101) if i % 2 != 0]
print("the ans  : ", sum(lst)

"""
lst = []
for i in range(1, 101):
    if i % 2 != 0:
        lst.append(i)
print(sum(lst))


print(sum([i for i in range(1, 101) if i % 2 != 0]))

