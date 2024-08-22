class Employee:
    language = "Python"; # this is a class attribute
    salary = 124560; # this is a class attribute

    
s1 = Employee();
s1.name = "Ankush";
s1.language = "JavaScript"; # this is an instance attribute

s2 = Employee();
s2.name = "Ankit";
s2.salary = 145600;

print(f"{s1.name}, {s1.language}\n{s1.salary}");
print(f"{s2.name}, {s2.language}\n{s2.salary}");

# 'Employee.getInfo(s1)' same as 's1.getInfo()';

# instance attributes take preference over class attributes during assignment and retrieval


...