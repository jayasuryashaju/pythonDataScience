"""
1. 1 - 1000
2. numbers divisible by 8
3. that have 6 in them
4. count the number of spaces in string
5. count the number of vowels in string
6. find all the words in a str that are less than five letters

string = "practice list comprehension to drill your head
"""
vowels = "aeiouAEIOU"
string = "practice list comprehension problems to drill your head"

print("Q1")

print([i for i in range(1, 1001)])

print("Q2")

print([i for i in range(1, 1001) if i % 8 == 0])

print("Q3")

print([i for i in range(1, 1001) if "6" in str(i)])

print("Q4")

print(len([i for i in string if i == " "]))

print("Q5")

print(len([i for i in string if i in vowels]))

print("Q6")

print([i for i in string.split(" ") if len(i) < 5])
