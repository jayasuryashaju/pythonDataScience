"""
student:
    id
    fname
    lname
    age
    college

> here college id the same for every student. so we can define it as a static variable.
> other variables like id, fname, lname, age are dynamic variables or instance variable.


"""


class Student:
    college_name = 'MES'

    def set_value(self, id, fname, lname, age):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.age = age

    def print_value(self):
        print(self.id)
        print(self.fname)
        print(self.lname)
        print(self.age)
        print(Student.college_name)


student1 = Student()
student1.set_value(101, 'vinay', 'k', 26)
student1.print_value()

student2 = Student()
student2.set_value(102, 'arun', 'gopan', 30)
student2.print_value()
