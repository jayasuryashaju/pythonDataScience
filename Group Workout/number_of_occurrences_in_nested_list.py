"""
Write a function that takes a nested list and an element,
and returns the number of times the element appears in the nested list
"""


def occurrence_count(lst, element):
    count = 0
    for i in lst:
        if element in i:
            count += 1

    return count


nested_list = [[1, 2, 3, 2, 10, 8, 2], [4, 5, 2, 6, 10, 9, 1, 5], [7, 3, 8, 9, 1]]
number = int(input("enter a number to find occurrences : "))

print("the number of occurrences in nested list = ", occurrence_count(nested_list, number))
