"""
Write a function to replace all zeroes in a nested list with ones.
"""


def sum_of_individual_list(lst):
    for i in lst:
        for j in range(len(i)):
            if i[j] == 0:
                i[j] = 1

    return lst


nested_list = [[1, 0, 3], [4, 0, 6, 0], [7, 0, 9]]

print("the updated list = ", sum_of_individual_list(nested_list))
