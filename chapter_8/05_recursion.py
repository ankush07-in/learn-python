'''
factotial(5) = 5 X 4 X 3 X 2 X 1
factotial(4) = 4 X 3 X 2 X 1
factotial(3) = 3 X 2 X 1
factotial(2) = 2 X 1
factotial(1) = 1

factorial(n) = n X n-1 X ... X 3 X 2 X 1

factorial(n) = n X factorial(n-1)

'''

def factorial(n):
    if(n == 1 or n == 0):
        return 1;
    return n * factorial(n-1);

n = int(input("Enter a number: "));

print(f"The factorial of the number is: {factorial(n)}");