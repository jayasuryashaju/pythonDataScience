"""
Write a function to flatten a nested list (i.e., convert it into a single list containing all the elements).
"""


def single_list(lst):
    new_list = []
    for i in lst:
        for j in i:
            new_list.append(j)
    return new_list


nested_list = [[1, 2, 3], [4, 5, 6, 10], [7, 8, 9]]

print("the new list = ", single_list(nested_list))
