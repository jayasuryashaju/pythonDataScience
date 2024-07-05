"""
person:
    1. first name
    2. last name
    3. age
    4. location

"""


class Person:
    def set_value(self, fname, lname, age, location):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.location = location

    def print_value(self):
        print(self.fname, self.lname, self.age, self.location)


person1 = Person()
person1.set_value('anu', 'p', 23, 'kannur')
person1.print_value()

person2 = Person()
person2.set_value('arun', 'k v', 30, 'idukki')
person2.print_value()

person3 = Person()
person3.set_value('amal', 'saji', 19, 'kochi')
person3.print_value()

person4 = Person()
person4.set_value('sandra', 'p c', 22, 'thrissur')
person4.print_value()

person5 = Person()
person5.set_value('gopika', 'venu', 25, 'kollam')
person5.print_value()