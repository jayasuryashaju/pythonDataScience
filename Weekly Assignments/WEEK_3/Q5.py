"""
Python program to display all numbers within a range except the prime numbers.
"""


def non_prime_numbers(limit):
    for i in range(limit + 1):
        flag = 0
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                flag = 1
                break
        if flag == 1:
            print(i)


lim = int(input("enter a number : "))

non_prime_numbers(lim)
