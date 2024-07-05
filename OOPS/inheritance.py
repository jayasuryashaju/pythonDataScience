"""
inheriting all the methods and variables from a parent class to a child class.

"""


class A:
    def print_a(self, num1):
        print("Inside class A", num1)


class B(A):

    def print_b(self, num2):
        print("Inside class B", num2)


obj1 = B()
obj1.print_a(21)