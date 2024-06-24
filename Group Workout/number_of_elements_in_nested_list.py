"""
Write a function to count the total number of elements in a nested list.
"""


def count_of_elements(lst):
    count = 0
    for i in lst:
        count += len(i)

    return count


nested_list = [[1, 2, 3], [4, 5, 6, 10], [7, 8, 9]]

print("the count of all elements = ", count_of_elements(nested_list))