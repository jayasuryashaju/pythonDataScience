"""
Write a function to find the sum of each row in a nested list and return the sums as a list.
"""


def sum_of_individual_list(lst):
    new_list = []
    for i in lst:
        new_list.append(sum(i))

    return new_list


nested_list = [[1, 2, 3], [4, 5, 6, 10], [7, 8, 9]]

print("the sum of individual lists in  nested list = ", sum_of_individual_list(nested_list))
