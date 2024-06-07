"""
break
continue
pass

1. Break
    to exit a loop at a particular state

"""
for i in range(1, 51):  #Break
    if i == 25:
        break
    print(i)


"""
2. Continue
    to skip a condition

"""

for i in range(1, 51):  #Continue
    if i == 25 or i == 26:
        continue
    print(i)

"""
3. Pass
    Do nothing
"""
for i in range(1, 51):  #Pass
    if i == 25:
        pass
    print(i)

