# Write a program to filter a list of numbers which are divisible by 5


def divisible5(n):
    if(n%5 == 0):
        return True
    return False

a = [1, 2, 353, 890875, 8785, 45, 8905, 364, 87439]

f = list(filter(divisible5, a))

print(f)



...