"""
0
0 1
0 2 4
0 3 6 9
0 4 8 12 16
"""

for i in range(6):
    for j in range(i + 1):
        print(i * j, end=" ")
    print()
