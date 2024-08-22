class Employee:
    language = "Python"; # this is a class attribute
    salary = 120000; # this is a class attribute

student = Employee()
student.name = "Ankush"; # this is an instance attribute
print(student.name+", "+student.language);
print(student.salary);

rohan = Employee();
rohan.name = "Rohan Basu"
print(f"{rohan.name}, {rohan.language}\n{rohan.salary}");

# Here name is an instance attribute / object attribute and salary and language are class attributes as they directly belong to the class

# insctance attrbute is nothing but object attribute

# instance attributes take preference over class attributes during assignment and retrieval


...