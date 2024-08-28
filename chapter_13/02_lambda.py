'''
Function created using an expression using 'lambda' keyword

Syntax:
    lambda arguments: expressions

    sum = lambda a, b, c : a + b + c

'''

# def square(n):
#     return n*n


# lambda arguments: expressions
square = lambda x: x*x

print(square(85))


a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

sum = lambda a, b, c : a + b + c

print(sum(a, b, c))


...