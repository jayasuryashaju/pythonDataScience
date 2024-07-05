"""
1. india work, fname, lname, age, prof

2. Age above 50 : fname, lname, age, prof

3. doctor prof : fname, lname, age

4. india work and prof doctor : fname, lname, age

5. uk work and age above 55 : fname, lname, age, prof

6. location count

7. prof count
"""

f = open("C:/Users/jayas/Downloads/customer1.txt", "r")

print("Q1: ")

for i in f:
    data = i.strip("\n").split(",")
    location = data[-1]
    if location == 'india':
        print(data[1:5])







