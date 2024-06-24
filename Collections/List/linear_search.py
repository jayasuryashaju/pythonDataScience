"""
linear search
time complexity in higher
"""


lst = [2, 5, 3, 7, 2, 4, 3, 67, 77]

num = int(input("enter a number : "))
i = 0
while i < len(lst):
    if lst[i] == num:
        print("element found")
        break
    else:
        i += 1
else:
    print("element not found")
