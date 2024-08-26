class Employee:
    company = "ITC"
    name = "Ankush"
    def show(self):
        print(f"The name of the employee is {self.name} and company is {self.company}")

class Coder:
    language = "Python"
    def printLanguage(self):
        print(f"Out of all the languages here is your language: {self.language}")

class Programmer(Employee, Coder):
    company = "ITC Infotech"
    def showLang(self):
        print(f"The name of the employee is {self.name} and language is {self.language}")

a = Employee()
b = Programmer()

b.show()
b.printLanguage()
b.showLang()