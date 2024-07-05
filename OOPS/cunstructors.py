"""
to replace a method,
also values can be passed when creating an object for a class


"""


class Person:
    def __init__(self, id, fname, lname, age):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.age = age

    def print_value(self):
        print(self.id, self.fname, self.lname, self.age)


person1 = Person(101, 'arun', 'gopi', 23)
person1.print_value()

# person1 = Person(101, 'arun', 'gopi', 23)
# person1.print_value()
#
# person1 = Person(101, 'arun', 'gopi', 23)
# person1.print_value()
#
# person1 = Person(101, 'arun', 'gopi', 23)
# person1.print_value()

