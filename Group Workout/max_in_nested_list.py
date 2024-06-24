"""
Write a function to find the maximum element in a nested list of integers.
"""


def max_in_nested_list(lst):
    largest = max(lst[0])

    for i in lst:
        if max(i) > largest:
            largest = max(i)

    return largest


nested_list = [[1, 2, 3], [4, 5, 6, 10], [7, 8, 9]]

print("the largest element in nested list = ", max_in_nested_list(nested_list))
