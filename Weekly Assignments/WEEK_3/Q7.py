"""
Print Pascal's Triangle:


"""

n = int(input('Enter no of rows: '))
lst = []
for i in range(n):
    temp_list = []
    for j in range(i + 1):
        if j == 0 or j == i:
            temp_list.append(1)
        else:
            temp_list.append(lst[i - 1][j - 1] + lst[i - 1][j])
    lst.append(temp_list)
for i in range(n):
    for j in range(n - i - 1):
        print(' ', end='')
    for j in range(i + 1):
        print(lst[i][j], end=' ')
    print()
