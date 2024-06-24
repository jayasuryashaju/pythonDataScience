"""
binary search:
    1. sort given list.
    2. set lower and upper variables,
        lower = starting index of list
        upper = ending index of list
    3. calculate midpoint of list,
        mid = (lower + upper) // 2
    4. 3 conditions to check:
        1.if search_element > lst[mid]
            lower = mid + 1
        2. search_element < lst[mid]
            upper = mid - 1
        3. search_element == lst[mid]
            element found


"""
import datetime

lst = [3, 5, 4, 6, 8, 4, 22, 45, 2, 77, 43, 56, 9, 7, 33, 65]

search_element = int(input("enter a number : "))

lst.sort()
lower = 0
upper = len(lst) - 1


while lower <= upper:
    mid = (lower + upper) // 2
    if search_element > lst[mid]:
        lower = mid + 1
    elif search_element < lst[mid]:
        upper = mid - 1
    elif search_element == lst[mid]:
        print("element found")
        break
else:
    print("element not found")
