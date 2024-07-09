"""
        *
     *     *
   *    *    *


"""

limit = int(input("enter a limit : "))


for i in range(1, limit+1):
    print(" " * (limit - i), (str(i) + " ") * i)
