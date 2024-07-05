"""
2 classes
    Personal Data
        id
        fname
        lname
        age
    professional data
        profession
        company name
        salary

object for professional data.
    print : id, fname, lname, age, prof, company_namae, salary
"""


class PersonalData:
    def __init__(self, id, fname, lname, age):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.age = age


class ProfessionalData(PersonalData):
    company_name = 'Amazon'

    # def set_value(self, profession, salary):
    #     self.profession = profession
    #     self.salary = salary

    def __init__(self, profession, salary, id, fname, lname, age):
        super().__init__(id, fname, lname, age)
        self.profession = profession
        self.salary = salary

    def print_value(self):
        print(self.id, self.fname, self.lname, self.age, self.profession, ProfessionalData.company_name, self.salary)


# obj1 = ProfessionalData(103, 'vinay', 'k', 23)
# obj1.set_value('Data Analyst', 24000)
# obj1.print_value()
#
# obj2 = ProfessionalData(104, 'arun', 'madhav', 24)
# obj2.set_value('Data Engineer', 54000)
# obj2.print_value()
#
# obj3 = ProfessionalData(105, 'vidhya', 'vimal', 22)
# obj3.set_value('Data Scientist', 48000)
# obj3.print_value()

obj1 = ProfessionalData('data scientist', 23000, 102, 'vinay', 'k', 23)
obj1.print_value()