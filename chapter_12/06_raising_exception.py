a = int(input("Enter first number: "))
b = int(input("Enter second number: "))


if(b == 0):
    raise ZeroDivisionError("\nHey our program is not meant to divide numbers by zero\n\n\n\nTHANK YOU!!\n\n")
else:
    print(f"The division of a/b is: {a/b}")