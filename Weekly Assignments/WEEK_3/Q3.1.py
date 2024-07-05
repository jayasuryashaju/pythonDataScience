"""
Python program that accepts a word from the user and reverses it.

"""


def reverse_string(word):
    new_str = ""
    # for i in range(len(word)-1, -1, -1):
    #     new_str += word[i]
    # print(new_str)

    for i in word:
        new_str = i + new_str
    print(new_str)


s = input("enter a word : ")

reverse_string(s)



