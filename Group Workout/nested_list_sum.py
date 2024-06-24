"""
Write a function that takes a nested list of integers and returns the sum of all elements
"""


def nested_sum(lst):
    result = 0
    for i in lst:
        result += sum(i)
    return result


nested_list = [[1, 2, 3], [4, 5, 6, 10], [7, 8, 9]]

print("the sum of all the elements in the list = ", nested_sum(nested_list))
