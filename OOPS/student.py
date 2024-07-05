
class Student:
    def set_student(self, id, fname, lname, sub1, sub2, sub3):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3

    def print_value(self):
        print(self.fname, self.lname, self.sub1, self.sub2, self.sub3)


student1 = Student()
student1.set_student(101, 'amritha', 'k v', 20, 25, 29)
student1.print_value()

student2 = Student()
student2.set_student(101, 'binoy', 'reji', 15, 20, 22)
student2.print_value()

student3 = Student()
student3.set_student(101, 'ciril', 'thomas', 10, 19, 26)
student3.print_value()

student4 = Student()
student4.set_student(101, 'karthika', 'sreenivasan', 22, 25, 28)
student4.print_value()

student5 = Student()
student5.set_student(101, 'sandra', 'chandran', 25, 28, 29)
student5.print_value()

