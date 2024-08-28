class Employee:
    company = "ITC"
    def show(self):
        print(f"The name of the employee is {self.name} and the work is {self.work} company is {self.company} and salary is {self.salary}")

class Programmer(Employee):
    company = "Google"
    def showLang(self):
        print(f"The name of the employee is {self.name} and language is {self.language} and company is {self.company}")

a = Employee()
b = Programmer()

a.name = "Rowdy"
a.work = "Sweeper"
a.salary = 12000

b.name = "Ankush"
b.work = "Programmer"
b.salary = 115400
b.language = "JS"

a.show()
a.showLang()
b.show()
b.showLang()