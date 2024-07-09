"""
Write a python program to read four numbers (representing the four octets of an IP) and print
the next five IP address
Eg:
Input:
192 168 255 252
----------Output---------
192 168 255 253
192 168 255 254
192 168 255 255
192 169 0 0
192 169 0 1

"""

n1 = int(input("enter first number : "))
n2 = int(input("enter second number : "))
n3 = int(input("enter third number : "))
n4 = int(input("enter forth number : "))

for i in range(5):
    print(n1, n2, n3, n4)
    n4 += 1
    if n4 > 255:
        n4 = 0
        n3 += 1
        if n3 >= 255:
            n3 = 0
            n4 = 0



