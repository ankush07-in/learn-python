# Strore the multiplication tables generated in problem 3 in a file named 'Tables.txt'


n = int(input("Enter a number: "))

table = [n*index for index in range(1, 11)]
# print((f"Table of {n}: {str(table)} \n"))


with open("Tables.txt", "a") as f:
    f.write(f"Table of {n}: {str(table)} \n")


...