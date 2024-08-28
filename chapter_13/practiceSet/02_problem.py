# Write a program to input name, marks and phone number of a student and format it using the format function like below: 'The name of the student is {name}, his marks are {marks} and phone number is {phNum}'


name = input("Enter name: ")
marks = int(input("Enter marks: "))
phNum = int(input("Phone number: "))

s = "The name of the student is {0}, his marks are {1} out of 100 and phone number is {2}".format(name, marks, phNum)


print(s)



...