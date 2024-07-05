"""
Employee:
    id, fname, lnmae, age, prof, company_nmae
"""


class Employee:
    prof = 'Data Analyst'
    company_name = 'Amazon'

    def __init__(self, id, fname, lname, age):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.age = age

    def print_value(self):
        print(self.id, self.fname, self.lname, self.age, Employee.prof, Employee.company_name)


employee1 = Employee(101, 'varun', 'krishna', 23)
employee1.print_value()

employee2 = Employee(102, 'amal', 'madhav', 24)
employee2.print_value()

employee3 = Employee(103, 'ishan', 'prince', 26)
employee3.print_value()

