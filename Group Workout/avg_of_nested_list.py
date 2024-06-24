"""
Write a function to calculate the average of all elements in a nested list.
"""


def avg_of_list(lst):
    average = 0
    for i in lst:
        average += sum(i)/len(i)

    return average


nested_list = [[1, 2, 3], [4, 5, 6, 10], [7, 8, 9]]

print("the average of nested list = ", avg_of_list(nested_list))
