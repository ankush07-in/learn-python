class Employee:
    language = "Python";
    salary = 123650;

    def __init__(self, name, language, salary): # dunder method which is automatically called
        self.name = name;
        self.language = language;
        self.salary = salary;
        print("I am creating an object");

    def getInfo(self):
        print(f"The language is {self.language}\nThe salary is {self.salary}");

    @staticmethod
    def greet():
        print("Good morning");

stu = Employee("Ankush", "TypeScript", 1346500);
print(stu.name, stu.salary, stu.language);
# stu.getInfo();

stud = Employee("Shivam", "HTML", 135600);