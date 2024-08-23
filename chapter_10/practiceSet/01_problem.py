class Programmer:
    company = "Micro-Soft";
    def __init__(self, name, salary, pincode):
        self.name = name;
        self.salary = salary;
        self.pin = pincode;

p = Programmer("Ankush", 1290000, 700035);
r = Programmer("Rohan", 13000, 700108);
# r.company = "Fusion";

print(f"Name: {p.name}, Salary: {p.salary}, Pincode: {p.pin}, Company: {p.company}");
print(f"Name: {r.name}, Salary: {r.salary}, Pincode: {r.pin}, Company: {r.company}");