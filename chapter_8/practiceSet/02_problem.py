# c/5 = (f-32)/9
# c = 5 * (f-32)/9

# f = int(input("Enter temperature in F: "));
# c = (5*(f-32))/9;

# print(c);

def f_to_c(f):
    c = 5*(f-32)/9;
    return c;

f = int(input("Enter temperature in F: "));
c = f_to_c(f);

print(f"{round(c, 3)} °C")

