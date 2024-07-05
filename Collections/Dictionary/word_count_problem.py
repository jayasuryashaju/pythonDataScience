"""
counting the number of times a word is repeated.

line ='cat mat rat cat rat bat mat cat bat'

1. split the line of data into word by word data

2. define dictionary
    dic = {}
3. update key if

"""

word = "cat mat rat cat bat mat rat cat mat rat bat cat bat"

dic = {}

lst = word.split(" ")

for i in lst:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

print(dic)
