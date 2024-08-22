class Employee:
    language = "Python"; # this is a class attribute
    salary = 124560; # this is a class attribute

    def getInfo(self):
        print(f"The language is {self.language}, The salary is {self.salary}");

    @staticmethod # if you do not want to put self you simply decorate with this ... decorator
    def greet():
        print(f"Good morning!! {s1.name}");

s1 = Employee();
s1.name = "Ankush";
s1.language = "JavaScript"; # this is an instance attribute

s1.greet();
s1.getInfo();

# 'Employee.getInfo(s1)' same as 's1.getInfo()';
# print(f"{s1.language}\n{s1.salary}");

# instance attributes take preference over class attributes during assignment and retrieval

# self is a convention, we can put any name here in the place of self

# Usually we use "self"


...