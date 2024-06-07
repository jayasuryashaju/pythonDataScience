#1.

for i in "luminar Technolab":
    if i == "r":
        break
    print(i)

"""
what is the output of this problem?
ans:
    l
    u
    m
    i
    n
    a
"""

#2.


for i in "luminar Technolab":
    if i == "a":
        continue
    print(i)

"""
what is the output of this program?

ans: 

    l
    u
    m
    i
    n
    r
    
    t
    e
    c
    h
    n
    o
    l
    b
"""

#3.


for i in "luminar Technolab":
    if i == "a":
        pass
    print(i)

"""
what is the output of this program?

ans: 

    l
    u
    m
    i
    n
    a
    r

    t
    e
    c
    h
    n
    o
    l
    a
    b
"""

#4.

x = 0
a = 5
b = 3
c = 7
if a < c:
    if a < b:
        x = x + 2
    else:
        x = x + 4
else:
    x = x + 4

"""
what is the output of this program?

ans:
    4
"""

#5.

for num in range(-2, -5, -1):
    print(num, end=",")

"""
what is the output of the function?

ans:
    -2, -3, -4
    
"""

#6

a, b = 5, 12
if a + b:
    print("True")
else:
    print("False")

"""
what is the output of this function?
ans:
    True

explanation:
    if the output number of a + b is positive or negative number := If condition is true
    else if output is zero := if condition ius false
"""

x = 0
for i in range(10):
    for j in range(-1, -10, -1):
        x += 1
print(x)

"""
what is the output of this program?

ans:
    90
explanation:
    1st loops iterates 10 times and inner loop iterates 9 times:
        so in total 10 * 9 = 90
"""

