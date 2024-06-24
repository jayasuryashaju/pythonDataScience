"""
nested list:
    lst = [ [] ]
    list inside a list
"""

lst = [[101, 'vinay', 'l', 30, 'bigdata', 1500],
       [102, 'anu', 'p', 28, 'python', 2000],
       [103, 'arjun', 'c', 24, 'bigdata', 3500],
       [104, 'amal', 'p', 31, 'python', 4500],
       [105, 'vipin', 'p', 26, 'python', 2000]]

# for i in lst:
#     if i[3] > 27:
#         print(i[1:5])

# for i in lst:
#     if i[4] == 'bigdata':
#         print(i[1:5])

# for i in lst:
#     if i[3] > 29 and i[5] > 1500:
#         print(i[1::2])
total_salary = 0
for i in lst:
    total_salary += i[5]
print(total_salary)
