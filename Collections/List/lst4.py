lst = [1, 2, 84, 4, 23, 6, 21, 72, 14, 100, 83, 11]

print([i ** 2 for i in lst if i % 2 != 0])

for element in lst:
    if element % 2 != 0:
        print(element ** 2)
