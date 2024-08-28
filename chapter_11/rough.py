class Employee:
    company = "ITC"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"The name is {self.name} and salary is {self.salary} and company is {self.company}")

class Programmer(Employee):
    company = "ITC Infotech"
    
    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language

    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")

# Creating instances
a = Employee("Ankush", 1200)
b = Programmer("Anuj", 36000, "JS")

# Displaying details

a.company = "Google"
a.show()
b.showLanguage()
b.show()
