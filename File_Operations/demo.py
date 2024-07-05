"""
file operations:
    1. read : r
    2. write : w
    3. append : a
creating a file reference:
    var_name = open('arg1', 'arg2')
        arg1 = 'path/to/the/file'
        arg2 = mode of operation
            r, w, a : read, write, append

strip():
    strip function is used to remove element or element parts from a list.

    strip(), lstrip(), rstrip()

"""

f = open("C:/Users/jayas/OneDrive/Desktop/example.txt", 'r')
lst = []


for i in f:
    lst.append(int(i.rstrip("\n")))
print(lst)

print("the sum = ", sum(lst))

